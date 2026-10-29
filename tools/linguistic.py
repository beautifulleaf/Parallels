"""Linguistic layer: recurring phrases, rare words, and loanword candidates.

Usage: python3 tools/linguistic.py

Runs over the whole Hebrew Bible (OSHB lemmas, Hebrew and Aramaic) and the
whole Quran (Quranic Arabic Corpus lemmas):

  phrases   sequences of 3+ content lemmas (nouns incl. names, verbs,
            adjectives) recurring inside verses in different places. Long
            verbatim parallels between two chapters (Samuel-Kings and
            Chronicles, Ps 18 and 2 Sam 22, Isa 36-39 and 2 Kgs 18-20) are
            reported separately as doublets; the rest are echoes.
  rare      lemmas found once (hapax legomena) or twice (dis legomena)
  loans     lemmas whose Strong's entry calls them foreign, Egyptian,
            Persian etc. (Hebrew; a dated 1894 lexicon), and rootless lemmas
            (Quran; the QAC gives no root, which often marks a loanword)

Writes results/linguistic/*.json and results/linguistic/REPORT.md.

Adding a corpus: every text added to the project gets this layer. Write an
adapter returning (verses, counts, first_ref, names) like `hebrew_tokens` /
`quran_tokens` (ordered content lemmas per verse or line, token counts per
lemma, first place of each lemma, and the set of proper-noun lemmas), then
run it in `main` alongside the Hebrew Bible and Quran. Phrase, doublet and rare-word
detection are corpus-independent.
"""
import json
import math
import pathlib
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from datetime import date

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import corpora  # noqa: E402

ROOT = corpora.ROOT
OUT = ROOT / "results" / "linguistic"
MIN_N, MAX_N = 3, 10
MAX_PHRASE_COUNT = 12      # more frequent sequences are stock formulas, listed separately
DOUBLET_MIN_SHARED = 4     # chapter pairs sharing this many long phrases are doublets
LOAN_PATTERN = re.compile(r"\b(foreign|egyptian|persian|chaldee|assyrian|babylonian|sanskrit|greek|hittite|"
                          r"of uncertain derivation|probably of foreign)\b", re.I)


# ---------------------------------------------------------------- tokens

def hebrew_tokens():
    """Ordered content lemmas per verse, plus per-lemma token counts and language."""
    verses, counts, aramaic, first_ref = {}, Counter(), set(), {}
    pos = defaultdict(Counter)
    for book in corpora.BOOK_ORDER:
        tree = ET.parse(corpora.RAW / "oshb" / f"{book}.xml")
        for vel in tree.iter(corpora.OSIS + "verse"):
            ref = vel.get("osisID")
            seq = []
            for w in vel.iter(corpora.OSIS + "w"):
                morph = w.get("morph", "")
                lang, parts = morph[:1], morph[1:].split("/")
                for lem, m in zip(w.get("lemma", "").split("/"), parts):
                    num = re.match(r"(\d+)", lem.strip())
                    if not num:
                        continue
                    lid = "H" + num.group(1)
                    counts[lid] += 1
                    pos[lid]["Np" if m[:2] == "Np" else m[:1]] += 1
                    first_ref.setdefault(lid, ref)
                    if lang == "A":
                        aramaic.add(lid)
                    if m[:1] in ("N", "V", "A"):
                        seq.append(lid)
            verses[ref] = seq
    names = {l for l, c in pos.items() if c.most_common(1)[0][0] == "Np"}
    return verses, counts, aramaic, first_ref, names


def quran_tokens():
    verses, counts, first_ref, roots, names = defaultdict(list), Counter(), {}, {}, set()
    for line in (corpora.RAW / "quran-morphology.txt").read_text(encoding="utf-8").splitlines():
        loc, _form, tag, feats = line.split("\t")
        s, v, _w, _seg = loc.split(":")
        ref = f"{s}:{v}"
        f = dict(x.split(":", 1) if ":" in x else (x, True) for x in feats.split("|"))
        if "LEM" not in f or "PREF" in f or "SUFF" in f:
            continue
        lid = unicodedata.normalize("NFC", f["LEM"])
        counts[lid] += 1
        first_ref.setdefault(lid, ref)
        roots.setdefault(lid, f.get("ROOT", ""))
        if "PN" in f:
            names.add(lid)
        if tag in ("N", "V") or "PN" in f or "ADJ" in f:
            verses[ref].append(lid)
    return dict(verses), counts, first_ref, roots, names


# ---------------------------------------------------------------- phrases

def chapter_of(ref):
    return ref.rsplit(".", 1)[0] if "." in ref else ref.split(":")[0]


def find_phrases(verses):
    occ = defaultdict(set)
    for ref, seq in verses.items():
        for n in range(MIN_N, MAX_N + 1):
            for i in range(len(seq) - n + 1):
                occ[tuple(seq[i:i + n])].add(ref)
    # keep sequences found in at least two different chapters
    cand = {g: refs for g, refs in occ.items() if len({chapter_of(r) for r in refs}) >= 2}
    # drop a sequence when a longer one covers exactly the same verses
    maximal = {}
    for g in sorted(cand, key=len, reverse=True):
        refs = frozenset(cand[g])
        covered = any(refs == frozenset(cand[h]) and len(h) > len(g) and
                      any(h[i:i + len(g)] == g for i in range(len(h) - len(g) + 1))
                      for h in maximal.get(refs, []))
        if not covered:
            maximal.setdefault(refs, []).append(g)
    phrases = [(g, sorted(refs)) for refs, gs in maximal.items() for g in gs]

    # doublets: chapter pairs that share many long phrases
    pair_count = Counter()
    for g, refs in phrases:
        if len(g) >= 4 and len(refs) <= 4:
            chs = sorted({chapter_of(r) for r in refs})
            for i in range(len(chs)):
                for j in range(i + 1, len(chs)):
                    pair_count[(chs[i], chs[j])] += 1
    doublet_pairs = {p for p, c in pair_count.items() if c >= DOUBLET_MIN_SHARED}
    return phrases, doublet_pairs, pair_count


def classify(phrases, doublet_pairs, verses, names):
    """Score = sum over the phrase's lemmas of log(verses / verses containing
    the lemma), times log(verses / occurrences): rare words in a rare
    sequence score highest. Sequences that are mostly names (genealogies,
    lists) go to a separate list."""
    n_verses = len(verses)
    df = Counter(l for seq in verses.values() for l in set(seq))
    echoes, formulas, doublet_hits, lists = [], [], [], []
    for g, refs in phrases:
        chs = sorted({chapter_of(r) for r in refs})
        pairs = {(chs[i], chs[j]) for i in range(len(chs)) for j in range(i + 1, len(chs))}
        rarity = sum(math.log(n_verses / df[l]) for l in g)
        entry = dict(lemmas=list(g), refs=refs, count=len(refs), chapters=len(chs),
                     score=round(rarity * math.log(n_verses / len(refs)) / 10, 2))
        if len(refs) > MAX_PHRASE_COUNT:
            formulas.append(entry)
        elif pairs and pairs <= doublet_pairs:
            doublet_hits.append(entry)
        elif sum(l in names for l in g) / len(g) > 0.4:
            lists.append(entry)
        else:
            echoes.append(entry)
    for lst in (echoes, formulas, doublet_hits, lists):
        lst.sort(key=lambda e: -e["score"])
    return echoes, formulas, doublet_hits, lists


# ---------------------------------------------------------------- report

def heb_ref(osis):
    b, c, v = osis.split(".")
    return f"{b} {c}:{v}"


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    strongs = corpora.load_strongs()

    hv, hcounts, aramaic, hfirst, hnames = hebrew_tokens()
    h_phr, h_doub, h_pairs = find_phrases(hv)
    h_echo, h_form, h_doubhits, h_lists = classify(h_phr, h_doub, hv, hnames)

    def hform(lid):
        e = strongs.get(lid, {})
        return f"{e.get('lemma', lid)} *{e.get('xlit', '')}*"

    h_rare = []
    for lid, c in hcounts.items():
        if c <= 2:
            e = strongs.get(lid, {})
            h_rare.append(dict(lemma=lid, count=c, form=e.get("lemma", ""), translit=e.get("xlit", ""),
                               gloss=re.sub(r"[{}]", "", e.get("strongs_def", ""))[:100],
                               derivation=e.get("derivation", ""), aramaic=lid in aramaic,
                               ref=heb_ref(hfirst[lid])))
    h_loans = []
    for lid, c in hcounts.items():
        e = strongs.get(lid, {})
        # only the etymology counts: a word *meaning* "foreign" is not a loanword
        text = e.get("derivation", "") + " " + " ".join(re.findall(r"of [a-z]+ (?:origin|derivation)", e.get("strongs_def", ""), re.I))
        m = LOAN_PATTERN.search(text)
        if m and lid not in hnames:
            h_loans.append(dict(lemma=lid, count=c, form=e.get("lemma", ""), translit=e.get("xlit", ""),
                                gloss=re.sub(r"[{}]", "", e.get("strongs_def", ""))[:100],
                                derivation=e.get("derivation", ""), marker=m.group(1).lower(),
                                aramaic=lid in aramaic, ref=heb_ref(hfirst[lid])))
    h_loans.sort(key=lambda x: (x["marker"], -x["count"]))

    qv, qcounts, qfirst, qroots, qnames = quran_tokens()
    q_phr, q_doub, _ = find_phrases(qv)
    q_echo, q_form, q_doubhits, q_lists = classify(q_phr, q_doub, qv, qnames)
    q_rare = [dict(lemma=l, count=c, root=qroots.get(l, ""), ref=qfirst[l]) for l, c in qcounts.items() if c <= 2]
    q_rootless = sorted([dict(lemma=l, count=c, ref=qfirst[l]) for l, c in qcounts.items() if not qroots.get(l)],
                        key=lambda x: -x["count"])

    payload = dict(
        hebrew_bible=dict(echoes=h_echo, formulas=h_form, doublet_phrases=h_doubhits, name_lists=h_lists,
                          doublet_chapter_pairs=sorted(f"{a} = {b} ({h_pairs[(a, b)]})" for a, b in h_doub),
                          rare=h_rare, loans=h_loans),
        quran=dict(echoes=q_echo, formulas=q_form, rare=q_rare, rootless=q_rootless))
    (OUT / "linguistic.json").write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")

    hap = [r for r in h_rare if r["count"] == 1]
    lines = [
        "# Linguistic layer", "",
        f"Generated {date.today().isoformat()} by `tools/linguistic.py` over the whole Hebrew Bible "
        f"({len(hv):,} verses, Hebrew and Aramaic) and the whole Quran ({len(qv):,} verses). Full data is in "
        "`linguistic.json`.", "",
        "Phrases are sequences of content lemmas (nouns including names, verbs, adjectives) inside one verse, "
        "found in at least two chapters or surahs. Function words are skipped, so a phrase can match across "
        "different prepositions and particles. Score: the rarer the words and the rarer the sequence, the higher.", "",
        "## Hebrew Bible: summary", "",
        f"- Phrase echoes (≤{MAX_PHRASE_COUNT} occurrences, outside doublet chapters): {len(h_echo):,}",
        f"- Stock formulas (>{MAX_PHRASE_COUNT} occurrences): {len(h_form):,}",
        f"- Name-heavy sequences (genealogies, lists), listed in the JSON only: {len(h_lists):,}",
        f"- Doublet chapter pairs (verbatim parallels): {len(h_doub):,}",
        f"- Hapax legomena (lemma occurs once): {len(hap):,}; dis legomena: {len(h_rare) - len(hap):,}",
        f"- Loanword candidates by Strong's derivation: {len(h_loans):,} (a dated 1894 lexicon; treat as leads)", "",
        "## Hebrew Bible: top phrase echoes", "",
        "| Score | Phrase (lemmas) | Count | Places |", "|---|---|---|---|"]
    for e in h_echo[:200]:
        lines.append(f"| {e['score']} | {' · '.join(hform(l) for l in e['lemmas'])} | {e['count']} | "
                     f"{', '.join(heb_ref(r) for r in e['refs'])} |")
    lines += ["", "## Hebrew Bible: doublet chapter pairs", "",
              "Chapter pairs sharing at least "
              f"{DOUBLET_MIN_SHARED} long phrases: verbatim parallel passages, kept apart from the echoes.", ""]
    lines += [f"- {p}" for p in payload["hebrew_bible"]["doublet_chapter_pairs"]]
    lines += ["", "## Hebrew Bible: most frequent stock formulas", "", "| Phrase | Count |", "|---|---|"]
    for e in sorted(h_form, key=lambda e: -e["count"])[:40]:
        lines.append(f"| {' · '.join(hform(l) for l in e['lemmas'])} | {e['count']} |")
    lines += ["", "## Hebrew Bible: loanword candidates", "",
              "| Marker | Lemma | Count | Gloss | First place |", "|---|---|---|---|---|"]
    for x in h_loans:
        lines.append(f"| {x['marker']} | {x['form']} *{x['translit']}* ({x['lemma']}{', Aram.' if x['aramaic'] else ''}) | "
                     f"{x['count']} | {x['gloss']} | {x['ref']} |")
    lines += ["", f"## Hebrew Bible: hapax legomena ({len(hap):,})", "",
              "| Lemma | Gloss | Place |", "|---|---|---|"]
    for x in sorted(hap, key=lambda x: x["ref"]):
        lines.append(f"| {x['form']} *{x['translit']}* ({x['lemma']}{', Aram.' if x['aramaic'] else ''}) | {x['gloss']} | {x['ref']} |")
    lines += ["", "## Quran: top phrase echoes", "", "| Score | Phrase (lemmas) | Count | Places |", "|---|---|---|---|"]
    for e in q_echo[:100]:
        lines.append(f"| {e['score']} | {' · '.join(e['lemmas'])} | {e['count']} | {', '.join(e['refs'])} |")
    lines += ["", f"## Quran: rootless lemmas (loanword candidates, {len(q_rootless):,})", "",
              "| Lemma | Count | First place |", "|---|---|---|"]
    lines += [f"| {x['lemma']} | {x['count']} | {x['ref']} |" for x in q_rootless]
    (OUT / "REPORT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Hebrew Bible: {len(h_echo)} echoes, {len(h_form)} formulas, {len(h_doub)} doublet pairs, "
          f"{len(hap)} hapax, {len(h_loans)} loan candidates")
    print(f"Quran: {len(q_echo)} echoes, {len(q_form)} formulas, {len(q_rootless)} rootless lemmas")
    print("wrote results/linguistic/")


if __name__ == "__main__":
    main()
