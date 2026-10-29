"""Lexical track: distribution anomalies within each corpus, plus cognate links.

Usage: python3 tools/lexical.py [--write-leads]

Finds three kinds of signal:
  concentration  a lemma whose verses cluster in one narrative, spread over
                 two or more separate tellings (surahs or chapters)
  bridge         a rare lemma found almost only inside exactly two narratives
  synonym skew   a concentrated lemma that has a common same-gloss sibling
                 used elsewhere (bahr vs yamm)
Quran candidates are then linked to Hebrew cognates by root correspondence.

Writes results/lexical/*.json and results/lexical/REPORT.md, checks the
benchmark expectations in data/benchmarks/lexical.yaml, and with
--write-leads creates or refreshes pipeline leads in leads/.
"""
import itertools
import json
import math
import pathlib
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from datetime import date

import yaml

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import corpora  # noqa: E402
import originals  # noqa: E402

ROOT = corpora.ROOT
OUT = ROOT / "results" / "lexical"
LEADS = ROOT / "leads"

MIN_VERSES = 3          # a lemma must occur in at least this many verses
MIN_SHARE = 0.6         # share of its verses inside the narrative
MIN_DISPERSION = 2      # separate surahs/chapters inside the narrative
MAX_Q = 0.05            # Benjamini-Hochberg threshold
BRIDGE_MAX_VERSES = 40
BRIDGE_MIN_INSIDE = 0.9


# ---------------------------------------------------------------- statistics

def log_comb(n, k):
    return math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)


def hypergeom_sf(k, V, K, n):
    """P(X >= k) drawing n of V verses, K of which are in the narrative."""
    total = log_comb(V, n)
    terms = [log_comb(K, i) + log_comb(V - K, n - i) - total for i in range(k, min(n, K) + 1)]
    if not terms:
        return 0.0
    m = max(terms)
    return min(1.0, math.exp(m) * sum(math.exp(t - m) for t in terms))


def bh_qvalues(pvalues):
    order = sorted(range(len(pvalues)), key=lambda i: pvalues[i])
    q, prev = [0.0] * len(pvalues), 1.0
    for rank, i in reversed(list(enumerate(order, 1))):
        prev = min(prev, pvalues[i] * len(pvalues) / rank)
        q[i] = prev
    return q


# ---------------------------------------------------------------- analysis

def analyze(corpus):
    V = len(corpus.verses)
    narr_size = Counter(n for v in corpus.verses for n in v.narratives)
    occ = defaultdict(set)
    for i, v in enumerate(corpus.verses):
        for lid in set(v.lemmas):
            occ[lid].add(i)

    concentration = []
    for lid, idx in occ.items():
        n = len(idx)
        if n < MIN_VERSES:
            continue
        best = None
        for nid, K in narr_size.items():
            inside = [i for i in idx if nid in corpus.verses[i].narratives]
            k = len(inside)
            if k < MIN_VERSES:
                continue
            p = hypergeom_sf(k, V, K, n)
            if best is None or p < best["p"]:
                best = dict(narrative=nid, k=k, p=p, inside=inside)
        if best is None:
            continue
        docs = {corpus.verses[i].document for i in best["inside"]}
        concentration.append(dict(
            lemma=lid, n=n, narrative=best["narrative"], k=best["k"], share=best["k"] / n,
            base_rate=narr_size[best["narrative"]] / V, dispersion=len(docs), p=best["p"],
            refs=[corpus.verses[i].ref for i in sorted(idx)]))
    for c, q in zip(concentration, bh_qvalues([c["p"] for c in concentration])):
        c["q"] = q
    concentration = [c for c in concentration
                     if c["share"] >= MIN_SHARE and c["dispersion"] >= MIN_DISPERSION and c["q"] <= MAX_Q]

    # synonym skew: siblings share POS and head gloss
    by_gloss = defaultdict(list)
    for lid, lem in corpus.lemmas.items():
        g = corpora.head_gloss([lem.gloss])
        if g and len(occ.get(lid, ())) >= MIN_VERSES:
            by_gloss[(g, lem.pos[:1])].append(lid)
    for c in concentration:
        lem = corpus.lemmas[c["lemma"]]
        key = (corpora.head_gloss([lem.gloss]), lem.pos[:1])
        siblings = []
        for sib in by_gloss.get(key, []):
            if sib == c["lemma"]:
                continue
            sidx = occ[sib]
            share = sum(1 for i in sidx if c["narrative"] in corpus.verses[i].narratives) / len(sidx)
            if len(sidx) > c["n"] and share < 0.3:
                siblings.append(dict(lemma=sib, n=len(sidx), share_in_narrative=round(share, 3)))
        c["synonym_skew"] = siblings

    # bridges: rare lemmas living almost only inside exactly two narratives
    bridges = []
    for lid, idx in occ.items():
        n = len(idx)
        if not 2 <= n <= BRIDGE_MAX_VERSES:
            continue
        labelled = [corpus.verses[i].narratives for i in idx]
        inside = [s for s in labelled if s]
        if len(inside) / n < BRIDGE_MIN_INSIDE:
            continue
        touched = Counter(x for s in inside for x in s)
        # narratives with a verse not shared with another touched narrative
        distinct = {x for s in inside if len(s) == 1 for x in s}
        if len(distinct) != 2:
            continue
        a, b = sorted(distinct)
        if any(a in s and b in s for s in inside):
            continue
        K = sum(1 for v in corpus.verses if a in v.narratives or b in v.narratives)
        p = hypergeom_sf(len(inside), V, K, n)
        bridges.append(dict(lemma=lid, n=n, narratives=[a, b], counts=[touched[a], touched[b]],
                            p=p, refs=[corpus.verses[i].ref for i in sorted(idx)]))
    bridges.sort(key=lambda b: b["p"])
    return concentration, bridges, occ


# ---------------------------------------------------------------- cognates

AR_TO_HE = {
    "ء": "א", "أ": "א", "إ": "א", "آ": "א", "ؤ": "א", "ئ": "א", "ا": "א",
    "ب": "ב", "ت": "ת", "ث": "ש", "ج": "ג", "ح": "ח", "خ": "ח", "د": "ד", "ذ": "ז",
    "ر": "ר", "ز": "ז", "س": "שס", "ش": "ש", "ص": "צ", "ض": "צ", "ط": "ט", "ظ": "צ",
    "ع": "ע", "غ": "ע", "ف": "פ", "ق": "ק", "ك": "כ", "ل": "ל", "م": "מ", "ن": "נ",
    "ه": "ה", "و": "וי", "ي": "י", "ى": "י", "ة": "הת",
}
AR_TRANSLIT = {
    "ء": "ʾ", "أ": "ʾ", "إ": "ʾ", "آ": "ʾā", "ؤ": "ʾ", "ئ": "ʾ", "ا": "ā", "ب": "b", "ت": "t",
    "ث": "th", "ج": "j", "ح": "ḥ", "خ": "kh", "د": "d", "ذ": "dh", "ر": "r", "ز": "z",
    "س": "s", "ش": "sh", "ص": "ṣ", "ض": "ḍ", "ط": "ṭ", "ظ": "ẓ", "ع": "ʿ", "غ": "gh",
    "ف": "f", "ق": "q", "ك": "k", "ل": "l", "م": "m", "ن": "n", "ه": "h", "و": "w",
    "ي": "y", "ى": "ā", "ة": "a", "ٱ": "",
}


def strip_ar(s):
    s = unicodedata.normalize("NFD", s)
    return "".join(c for c in s if not unicodedata.combining(c) and "ء" <= c <= "ي" or c == "ٱ").replace("ٱ", "ا")


def translit(s):
    """Rough scholarly transliteration of a vocalized Arabic word."""
    out = ""
    for c in unicodedata.normalize("NFC", s):
        if c == "\u064e":                      # fatha
            out += "a"
        elif c == "\u0650":                    # kasra
            out += "i"
        elif c == "\u064f":                    # damma
            out += "u"
        elif c == "\u0651" and out:            # shadda doubles the consonant
            m = re.search(r"(th|kh|dh|sh|gh|[^aiuāīū])([aiu]?)$", out)
            if m:
                out = out[:m.start()] + m.group(1) * 2 + m.group(2)
        elif c == "ة":
            out += "" if out.endswith("a") else "a"
        elif c == "\u0670":                    # dagger alif
            out += "ā"
        elif c in "اى" and out.endswith("a"):
            out = out[:-1] + "ā"
        elif c == "و" and out.endswith("u"):
            out = out[:-1] + "ū"
        elif c == "ي" and out.endswith("i"):
            out = out[:-1] + "ī"
        elif c == "ا" and not out:
            out += "a"
        else:
            out += AR_TRANSLIT.get(c, "")
    return out


def slug(s):
    t = translit(s)
    t = unicodedata.normalize("NFD", t)
    t = "".join(c for c in t if c.isascii() and c.isalnum())
    return t.lower() or "x"


def arabic_consonants(lemma):
    """Root letters, or for rootless (often foreign) lemmas the skeleton of
    the lemma with long-vowel letters removed."""
    if lemma.root:
        return strip_ar(lemma.root)
    s = strip_ar(lemma.form).replace("ا", "")
    return s[:1] + re.sub(r"[وي]", "", s[1:]) if s else s


def hebrew_candidates(letters):
    options = [AR_TO_HE.get(c, "") for c in letters]
    if not all(options):
        return set()
    cands = {"".join(p) for p in itertools.product(*options)}
    if len(letters) == 3 and letters[1] == letters[2]:          # geminate: ymm -> ym
        cands |= {c[:2] for c in cands}
    cands |= {re.sub(r"(?<=.)[וי](?=.)", "", c) for c in cands}  # hollow roots
    cands |= {c[:-1] + "ה" for c in cands if c.endswith("ת")}    # feminine -t / -h
    return {c for c in cands if len(c) >= 2}


def hebrew_index(heb, heb_occ):
    index = defaultdict(list)
    for lid, lem in heb.lemmas.items():
        if lem.pos not in corpora.HEBREW_CONTENT_POS or lid not in heb_occ:
            continue
        sk = corpora.skeleton_hebrew(lem.form)
        keys = {sk, sk[:1] + re.sub(r"[וי]", "", sk[1:])}
        if sk.endswith("ה") and len(sk) > 2:
            keys.add(sk[:-1])
        for key in keys:
            index[key].append(lid)
    return index


def cognates(lemma, index, heb, heb_occ):
    """Hebrew lemmas matching by sound correspondence. A match whose Strong's
    definition contains the Arabic gloss word is marked gloss_match and
    ranked first; only those count as cognate evidence downstream."""
    found = {}
    gloss = corpora.head_gloss([lemma.gloss])
    for cand in hebrew_candidates(arabic_consonants(lemma)):
        for lid in index.get(cand, []):
            if lid in found:
                continue
            h = heb.lemmas[lid]
            words = {w[:-1] if w.endswith("s") and len(w) > 3 else w for w in re.findall(r"[a-z]+", h.definition)}
            found[lid] = dict(lemma=lid, form=h.form, translit=h.translit, gloss=h.gloss,
                              verses=len(heb_occ[lid]), gloss_match=bool(gloss) and gloss in words)
    return sorted(found.values(), key=lambda f: (not f["gloss_match"], -f["verses"]))[:5]


def matched(cogs):
    return [g for g in cogs if g["gloss_match"]]


def sound_only_note(corpus, c):
    """For rootless (likely foreign) lemmas, glosses often differ across
    languages, so sound-only matches are worth showing, labelled as such."""
    if corpus.name != "quran" or corpus.lemmas[c["lemma"]].root or matched(c.get("cognates", [])):
        return ""
    weak = c.get("cognates", [])[:1]
    return f"possible Hebrew cognate by sound only: {weak[0]['form']} *{weak[0]['translit']}* {weak[0]['lemma']} “{weak[0]['gloss']}”" if weak else ""


# ---------------------------------------------------------------- reporting

def hebrew_ref(osis):
    b, c, v = osis.split(".")
    return f"{b} {c}:{v}"


def describe(corpus, lid):
    lem = corpus.lemmas[lid]
    if corpus.name == "quran":
        root = f" (root {strip_ar(lem.root)})" if lem.root else " (no root: loanword candidate)"
        return f"{lem.form} *{translit(lem.form)}* “{lem.gloss}”{root}"
    return f"{lem.form} *{lem.translit}* “{lem.gloss}” ({lid})"


def run():
    quran, heb = corpora.load_quran(), corpora.load_hebrew_bible()
    q_conc, q_bridges, q_occ = analyze(quran)
    h_conc, h_bridges, h_occ = analyze(heb)
    h_best = {c["lemma"]: c for c in h_conc}
    h_bridge = {b["lemma"]: b for b in h_bridges}
    index = hebrew_index(heb, h_occ)

    for c in q_conc + q_bridges:
        c["cognates"] = cognates(quran.lemmas[c["lemma"]], index, heb, h_occ)
        targets = [c["narrative"]] if "narrative" in c else c["narratives"]
        c["cross_corpus"] = [dict(lemma=g["lemma"], narrative=h_best[g["lemma"]]["narrative"],
                                  share=round(h_best[g["lemma"]]["share"], 3))
                             for g in matched(c["cognates"])
                             if g["lemma"] in h_best and h_best[g["lemma"]]["narrative"] in targets]
        # a cognate that is itself a Hebrew bridge touching one of the same narratives
        c["cross_bridge"] = [dict(lemma=g["lemma"], narratives=h_bridge[g["lemma"]]["narratives"],
                                  counts=h_bridge[g["lemma"]]["counts"])
                             for g in matched(c["cognates"])
                             if g["lemma"] in h_bridge and set(h_bridge[g["lemma"]]["narratives"]) & set(targets)]

    def score(c):
        return -math.log10(max(c["p"], 1e-300)) * c["share"] * (2 if c["synonym_skew"] else 1) * (2 if c["cross_corpus"] else 1)
    for c in q_conc + h_conc:
        c.setdefault("cross_corpus", [])
        c["score"] = round(score(c), 2)
    q_conc.sort(key=lambda c: -c["score"])
    h_conc.sort(key=lambda c: -c["score"])

    OUT.mkdir(parents=True, exist_ok=True)
    for name, corpus, conc, bridges in (("quran", quran, q_conc, q_bridges), ("hebrew-bible", heb, h_conc, h_bridges)):
        def lem_info(lid):
            l = corpus.lemmas[lid]
            return dict(form=l.form, gloss=l.gloss, root=l.root, pos=l.pos,
                        translit=translit(l.form) if name == "quran" else l.translit)
        payload = dict(corpus=name, verses=len(corpus.verses), narratives=corpus.narratives,
                       parameters=dict(min_verses=MIN_VERSES, min_share=MIN_SHARE, min_dispersion=MIN_DISPERSION,
                                       max_q=MAX_Q, bridge_max_verses=BRIDGE_MAX_VERSES),
                       concentration=[{**c, **lem_info(c["lemma"])} for c in conc],
                       bridges=[{**b, **lem_info(b["lemma"])} for b in bridges])
        (OUT / f"{name}.json").write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")

    bench = check_benchmarks(quran, heb, q_conc, h_conc, q_bridges, h_bridges)
    write_report(quran, heb, q_conc, h_conc, q_bridges, h_bridges, bench)
    return quran, heb, q_conc, h_conc, q_bridges, h_bridges, bench


def check_benchmarks(quran, heb, q_conc, h_conc, q_bridges, h_bridges):
    spec = yaml.safe_load((ROOT / "data" / "benchmarks" / "lexical.yaml").read_text(encoding="utf-8"))
    pools = {("quran", "concentration"): q_conc, ("hebrew-bible", "concentration"): h_conc,
             ("quran", "bridge"): q_bridges, ("hebrew-bible", "bridge"): h_bridges}
    results = []
    for b in spec["expectations"]:
        pool = pools[(b["corpus"], b["kind"])] if b["kind"] != "cognate" else q_conc + q_bridges
        hit = None
        for c in pool:
            if c["lemma"] != b["lemma"]:
                continue
            if b["kind"] == "concentration" and c["narrative"] == b["narrative"]:
                hit = c
            elif b["kind"] == "bridge" and sorted(c["narratives"]) == sorted(b["narratives"]):
                hit = c
            elif b["kind"] == "cognate" and any(g["lemma"] == b["hebrew"] for g in matched(c["cognates"])):
                hit = c
        if b["kind"] == "cognate" and not hit:
            # cognate benchmarks also count when the lemma is not itself a candidate
            index = hebrew_index(heb, {l: {0} for l in heb.lemmas})
            lem = quran.lemmas.get(b["lemma"])
            if lem and any(g["lemma"] == b["hebrew"] for g in matched(cognates(lem, index, heb, defaultdict(set)))):
                hit = {"lemma": b["lemma"]}
        results.append({**b, "recovered": bool(hit), "expect": b.get("expect", True)})
    return results


def write_report(quran, heb, q_conc, h_conc, q_bridges, h_bridges, bench):
    lines = ["# Lexical track report", "",
             f"Generated {date.today().isoformat()} by `tools/lexical.py`. Raw candidates are in "
             "`quran.json` and `hebrew-bible.json`.", "",
             "Verses are counted, not tokens, so a word repeated within one verse counts once. "
             "Narrative labels come from `data/narratives/`.", "",
             "## Benchmarks", "", "| Expectation | Recovered |", "|---|---|"]
    for b in bench:
        verdict = "yes" if b["recovered"] else ("no (expected: known limitation)" if not b["expect"] else "**no**")
        lines.append(f"| {b['description']} | {verdict} |")
    for title, corpus, conc, bridges in (("Quran", quran, q_conc, q_bridges), ("Hebrew Bible", heb, h_conc, h_bridges)):
        lines += ["", f"## {title}: concentration ({len(conc)} candidates)", "",
                  "| Score | Lemma | Narrative | In narrative | Units | q | Flags |", "|---|---|---|---|---|---|---|"]
        for c in conc[:40]:
            flags = []
            if c["synonym_skew"]:
                flags.append("synonym skew vs " + ", ".join(
                    f"{corpus.lemmas[s['lemma']].form} ({s['n']}, {s['share_in_narrative']:.0%} here)" for s in c["synonym_skew"][:2]))
            if matched(c.get("cognates", [])):
                flags.append("Hebrew cognate " + ", ".join(f"{g['form']} *{g['translit']}* {g['lemma']}" for g in matched(c["cognates"])[:2]))
            if c["cross_corpus"]:
                flags.append("**same narrative in Hebrew Bible**")
            if sound_only_note(corpus, c):
                flags.append(sound_only_note(corpus, c))
            lines.append(f"| {c['score']} | {describe(corpus, c['lemma'])} | {corpus.narratives[c['narrative']]} | "
                         f"{c['k']}/{c['n']} ({c['share']:.0%}; base {c['base_rate']:.0%}) | {c['dispersion']} | {c['q']:.1e} | {'; '.join(flags)} |")
        lines += ["", f"## {title}: bridges ({len(bridges)} candidates)", "",
                  "| p | Lemma | Narratives | Verses |", "|---|---|---|---|"]
        for b in bridges[:50]:
            names = " + ".join(f"{corpus.narratives[n]} ({k})" for n, k in zip(b["narratives"], b["counts"]))
            m = matched(b.get("cognates", []))
            cog = f" · Hebrew cognate {m[0]['form']} *{m[0]['translit']}* {m[0]['lemma']}" if m else ""
            if sound_only_note(corpus, b):
                cog += " · " + sound_only_note(corpus, b)
            if b.get("cross_bridge"):
                cog += " · **cognate is also a Hebrew Bible bridge**"
            lines.append(f"| {b['p']:.1e} | {describe(corpus, b['lemma'])}{cog} | {names} | {b['n']} |")
    (OUT / "REPORT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- leads

QURAN_TEXT, HEBREW_TEXT = {}, {}
PIPELINE_FIELDS = {"title", "summary", "relations", "standing", "traditions", "layers", "lexical",
                   "passages", "evidence", "motifs"}


def write_lead(lead):
    """Create a lead, or refresh only pipeline-owned fields of an existing one."""
    path = LEADS / f"{lead['id']}.md"
    body = "## Questions\n\n## Notes\n"
    if path.exists():
        text = path.read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
        old, body = yaml.safe_load(m.group(1)), m.group(2).lstrip("\n")
        if old.get("origin") != "pipeline":
            return "skipped (human lead)"
        merged = {**old, **{k: v for k, v in lead.items() if k in PIPELINE_FIELDS}}
        lead, state = merged, "refreshed"
    else:
        state = "created"
    path.write_text("---\n" + yaml.safe_dump(lead, allow_unicode=True, sort_keys=False, width=100)
                    + "---\n\n" + body, encoding="utf-8")
    return state


def quran_ref_label(ref):
    return f"Quran {ref}"


def build_leads(quran, heb, q_conc, q_bridges, bench):
    covered = {b["lemma"] for b in bench if b.get("lead")}
    leads = []
    for c in q_conc:
        if c["lemma"] in covered or not (c["synonym_skew"] or c["cross_corpus"]) or c["q"] > 0.01:
            continue
        lem = quran.lemmas[c["lemma"]]
        narr = quran.narratives[c["narrative"]]
        sib = c["synonym_skew"][0] if c["synonym_skew"] else None
        summary = (f"{lem.form} ({translit(lem.form)}, “{lem.gloss}”) occurs in {c['n']} verses; {c['k']} of them "
                   f"({c['share']:.0%}) are in the {narr} narrative, which is {c['base_rate']:.0%} of the Quran, "
                   f"across {c['dispersion']} surahs.")
        if sib:
            s = quran.lemmas[sib["lemma"]]
            summary += f" The more common same-gloss word {s.form} ({translit(s.form)}, {sib['n']} verses) has only {sib['share_in_narrative']:.0%} of its verses there."
        leads.append(_lead(quran, heb, c, f"quran-{c['narrative']}-{slug(lem.form)}",
                           f"{translit(lem.form)}: a {lem.gloss or 'word'} word concentrated in {narr}", summary, [c["narrative"]]))
    for rank, b in enumerate(q_bridges):
        # top bridges, plus any rootless (likely loanword) bridge
        if b["lemma"] in covered or b["p"] > 0.01 or (rank >= 8 and quran.lemmas[b["lemma"]].root):
            continue
        lem = quran.lemmas[b["lemma"]]
        n1, n2 = (quran.narratives[n] for n in b["narratives"])
        summary = (f"{lem.form} ({translit(lem.form)}, “{lem.gloss}”) occurs in {b['n']} verses, all or nearly all inside "
                   f"two narratives: {n1} ({b['counts'][0]}) and {n2} ({b['counts'][1]}). A rare word linking two stories.")
        b.setdefault("synonym_skew", [])
        leads.append(_lead(quran, heb, b, f"quran-bridge-{slug(lem.form)}",
                           f"{translit(lem.form)}: a word shared by {n1} and {n2}", summary, b["narratives"]))
    return leads


def _lead(quran, heb, c, lid, title, summary, narratives):
    lem = quran.lemmas[c["lemma"]]
    lexical = [{"lang": "ar", "form": lem.form, "translit": translit(lem.form), "gloss": lem.gloss}]
    for s in c.get("synonym_skew", [])[:1]:
        sl = quran.lemmas[s["lemma"]]
        lexical.append({"lang": "ar", "form": sl.form, "translit": translit(sl.form), "gloss": f"{sl.gloss} (common synonym)"})
    for g in matched(c.get("cognates", []))[:2]:
        lexical.append({"lang": "he", "form": g["form"], "translit": g["translit"], "gloss": f"{g['gloss']} ({g['lemma']}, possible cognate)"})
    def ev(text, basis):
        return {"text": text, "basis": basis}
    evidence = [ev(f"p = {c['p']:.1e} (hypergeometric, verse level)" + (f", q = {c['q']:.1e}" if "q" in c else "")
                   + ". Counted from the original text with the Quranic Arabic Corpus lemmas.", "original")]
    for sk in c.get("synonym_skew", [])[:2]:
        sl = quran.lemmas[sk["lemma"]]
        evidence.append(ev(f"Synonym skew: {sl.form} ({translit(sl.form)}, {sk['n']} verses) has only "
                           f"{sk['share_in_narrative']:.0%} of its verses in this narrative. The two words are paired "
                           "only because their English word-by-word glosses match; confirm in the Arabic that they "
                           "are real synonyms.", "gloss"))
    if not lem.root:
        evidence.append(ev("The Quranic Arabic Corpus gives no root, which often marks a loanword.", "original"))
        weak = [g for g in c.get("cognates", []) if not g["gloss_match"]][:1]
        if weak and not matched(c.get("cognates", [])):
            g = weak[0]
            evidence.append(ev(f"Possible Hebrew cognate by consonants only: {g['form']} ({g['translit']}, {g['lemma']}). "
                               "The meanings were not compared.", "original"))
    for x in c.get("cross_corpus", []):
        evidence.append(ev(f"Hebrew cognate {heb.lemmas[x['lemma']].form} ({x['lemma']}) is also concentrated in the same "
                           f"narrative in the Hebrew Bible ({x['share']:.0%} of its verses).", "gloss"))
    for x in c.get("cross_bridge", []):
        names = " and ".join(f"{heb.narratives[n]} ({k})" for n, k in zip(x["narratives"], x["counts"]))
        evidence.append(ev(f"Hebrew cognate {heb.lemmas[x['lemma']].form} ({x['lemma']}) is itself a rare word linking two "
                           f"Hebrew Bible narratives: {names}. Both words connect stories, and they share at least one.", "gloss"))
    if matched(c.get("cognates", [])):
        evidence.append(ev("Hebrew cognates are matched by regular sound correspondence on the original consonants, then "
                           "kept only if Strong's English definition contains the Arabic word's English gloss. The meaning "
                           "check is gloss-based; confirm it in the originals.", "gloss"))
    passages = [{"tradition": "islam", "ref": quran_ref_label(r)} for r in c["refs"][:15]]
    originals.fill_passages(passages, QURAN_TEXT, HEBREW_TEXT)
    return {
        "id": lid, "title": title, "summary": summary, "status": "new",
        "relations": ["internal"] + (["inheritance"] if matched(c.get("cognates", [])) else []),
        "standing": "proposed",
        "traditions": ["islam"] + (["judaism"] if matched(c.get("cognates", [])) else []),
        "layers": ["lexical"], "motifs": narratives,
        "lexical": lexical,
        "passages": passages,
        "evidence": evidence, "origin": "pipeline", "added": date.today().isoformat(),
    }


def main():
    quran, heb, q_conc, h_conc, q_bridges, h_bridges, bench = run()
    print(f"Quran: {len(q_conc)} concentration, {len(q_bridges)} bridges")
    print(f"Hebrew Bible: {len(h_conc)} concentration, {len(h_bridges)} bridges")
    for b in bench:
        label = "recovered " if b["recovered"] else ("expected miss " if not b["expect"] else "MISSED    ")
        print("  " + label + b["description"])
    if "--write-leads" in sys.argv:
        global QURAN_TEXT, HEBREW_TEXT
        QURAN_TEXT, HEBREW_TEXT = originals.load_quran_text(), originals.load_hebrew_text()
        for lead in build_leads(quran, heb, q_conc, q_bridges, bench):
            print(f"  lead {lead['id']}: {write_lead(lead)}")
    print("wrote results/lexical/")
    if any(b["expect"] and not b["recovered"] for b in bench):
        sys.exit("benchmark expectations missed")


if __name__ == "__main__":
    main()
