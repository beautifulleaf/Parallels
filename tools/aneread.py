"""Helpers for the full read of the ancient Near Eastern corpus.

Usage:
  python3 tools/aneread.py scope --write        # (re)build data/ane/texts.yaml from data/raw/ane/ and the rules below
  python3 tools/aneread.py plan                 # list the reading chunks
  python3 tools/aneread.py texts [chunk]        # texts in scope (of one chunk), with line counts
  python3 tools/aneread.py text <chunk>         # print a whole chunk
  python3 tools/aneread.py text <ref>           # print a text, a section or a range, e.g. 'Gilg SB XI' or 'ETCSL 1.7.4 C:1-27'
  python3 tools/aneread.py lemmas <ref>         # the same lines word by word: form, lemma, gloss
  python3 tools/aneread.py vocab [words...]     # motifs whose id or label contains all the words

Each printed line is `<section>:<line>  <original>`. Under it, `  = ` gives the
edition's translation, a reading aid, and `  ~ ` gives word glosses when the
edition has no translation for that line. ETCSL translates by paragraph: the
paragraph is printed at its first line, with the lines it covers.

The original is what is tagged; translations and glosses help reading it.
"""
import json
import pathlib
import re
import signal
import sys
from collections import Counter, defaultdict

import yaml

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import originals  # noqa: E402

ROOT = originals.ROOT
RAW = originals.ANE_RAW
SCOPE = originals.ANE_INDEX
CHUNK_LINES = 2000

TRADITION = {"sux": "ane-sumerian", "akk": "ane-akkadian", "uga": "ane-ugaritic", "egy": "ane-egyptian",
             "hit": "ane-hittite", "hurr": "ane-hittite", "nws": "ane-levantine"}


# ---------------------------------------------------------------- scope rules (see data/ane/SCOPE.md)

ORACC_ALL = {"saao-saa02", "saao-saa03", "saao-saa09", "saao-saa20"}
ORACC_PICK = {   # royal inscriptions with religious content or a bearing on the Hebrew Bible
    "ribo-babylon8": ["Cyrus II 01"],
    "rinap-rinap3": ["Sennacherib 022"],
    "rinap-rinap4": ["Esarhaddon 001", "Esarhaddon 104", "Esarhaddon 105"],
    "ribo-babylon7": ["Nabonidus 03", "Nabonidus 28", "Nabonidus 47", "Nabonidus 2001"],
}
GKAB_GENRES = {"Literary", "Hymn-Prayer", "Incantation-Ritual", "Ritual", "Incantation", "Prayer", "Hymn"}
UGARIT_RELIGIOUS = {"māmītu", "adê", "riksu", "rikiltu", "nīšu", "ilu", "kirru"}


def oracc_docs(proj):
    for f in sorted((RAW / "oracc" / proj).glob("*.json")):
        yield f, json.loads(f.read_text(encoding="utf-8"))


def nlines(d):
    return sum(len(s["lines"]) for s in d["sections"])


def in_scope():
    """Every text in scope, in reading order, with its tradition. Returns (texts, left_out)."""
    texts, out = [], []

    def add(f, d, tradition=None, title=None, siglum=None):
        lang = d.get("language") or ""
        lang = {"Sumerian": "sux", "Akkadian": "akk"}.get(lang, lang)
        texts.append({"siglum": siglum or d["siglum"], "title": title or d["title"], "file": str(f.relative_to(RAW)),
                      "tradition": tradition or TRADITION.get(lang[:3], "ane-akkadian"), "language": lang,
                      "source": d.get("source", ""), "lines": nlines(d)})

    # Sumerian: ETCSL, with ORACC's lemmatized composite where ETCSL has no composite online
    etcsl_done = set()
    for f in sorted((RAW / "etcsl").glob("*.json"), key=lambda p: [int(x) if x.isdigit() else x for x in re.split(r"[.]", p.stem[2:])]):
        d = json.loads(f.read_text(encoding="utf-8"))
        num = d["siglum"].split()[1]
        if nlines(d):
            add(f, d, "ane-sumerian")
            etcsl_done.add(num)
    for f, d in oracc_docs("epsd2-literary"):
        m = re.search(r"text=c\.([\d.]+[a-z]?)", (d.get("meta") or {}).get("publication_history", ""))
        num = m.group(1).rstrip(".") if m else None
        if num and num in etcsl_done:
            continue
        if num:
            add(f, d, "ane-sumerian", siglum=f"ETCSL {num}", title=f"{d['title']} (ORACC composite)")
            etcsl_done.add(num)
        else:
            out.append((d["siglum"], d["title"], nlines(d), "ORACC epsd2/literary composite outside ETCSL's catalogue; left for a later pass"))
    # Akkadian (and Sumerian) literature and incantation series from eBL
    for f in sorted((RAW / "ebl").glob("*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        if nlines(d):
            add(f, d, "ane-sumerian" if d.get("language") == "sux" else "ane-akkadian")
    # ORACC: treaties, literary, prophecies, rituals; selected royal inscriptions; Uruk religious tablets
    for proj in sorted(ORACC_ALL):
        for f, d in oracc_docs(proj):
            add(f, d, "ane-akkadian", siglum=d["title"])
    for proj, picks in ORACC_PICK.items():
        for f, d in oracc_docs(proj):
            if d["title"] in picks:
                add(f, d, "ane-akkadian", siglum=d["title"])
    for f, d in oracc_docs("cams-gkab"):
        if d.get("genre") in GKAB_GENRES:
            add(f, d, "ane-akkadian", siglum=f"GKAB {d['id']}", title=f"{d['title']} ({d.get('subgenre') or d.get('genre')})")
    for f, d in oracc_docs("aemw-amarna"):
        add(f, d, "ane-akkadian", siglum=d["title"].split(" (")[0] if d["title"].startswith("EA") else f"Amarna {d['id']}")
    for f, d in oracc_docs("aemw-ugarit"):
        lemmas = {x["lemma"] for s in d["sections"] for l in s["lines"] for x in l.get("lemmas") or []}
        dns = {x["lemma"] for s in d["sections"] for l in s["lines"] for x in l.get("lemmas") or [] if x.get("pos") == "DN"}
        if nlines(d) >= 5 and (lemmas & UGARIT_RELIGIOUS or len(dns) >= 3):
            alpha = any((x.get("lang") or "").startswith("uga") for s in d["sections"] for l in s["lines"] for x in l.get("lemmas") or [])
            add(f, d, "ane-ugaritic" if alpha else "ane-akkadian", siglum=f"Ugarit {d['title'].split(' (')[0]}")
    # the other sources, written by tools/ane_sources/fetch_<name>.py
    for name, trad in (("ugaritic", "ane-ugaritic"), ("egyptian", "ane-egyptian"), ("hittite", "ane-hittite"), ("nws", "ane-levantine")):
        for f in sorted(p for p in (RAW / name).glob("*.json") if not p.name.startswith("_")):
            d = json.loads(f.read_text(encoding="utf-8"))
            if nlines(d):
                add(f, d, trad)
    # sigla must be unique
    seen = Counter(t["siglum"] for t in texts)
    for t in texts:
        if seen[t["siglum"]] > 1:
            t["siglum"] = f"{t['siglum']} [{pathlib.Path(t['file']).stem}]"
    return texts, out


def assign_chunks(texts):
    """Chunks of about CHUNK_LINES lines in reading order. A text longer than 1.5 chunks is split at section
    boundaries; its entry then lists `parts`: {chunk: [sections]}."""
    chunk, n = 1, 0
    for t in texts:
        if t["lines"] > CHUNK_LINES * 1.5:
            d = json.loads((RAW / t["file"]).read_text(encoding="utf-8"))
            parts = defaultdict(list)
            for s in d["sections"]:
                if n >= CHUNK_LINES:
                    chunk, n = chunk + 1, 0
                parts[chunk].append(s["name"])
                n += len(s["lines"])
            if len(parts) > 1 and all(parts.values()):
                t["parts"] = {k: [originals.norm_loc(x, "1")[0] for x in v] for k, v in parts.items()}
                t["chunk"] = min(parts)
                continue
            t["chunk"] = chunk
            continue
        if n and n + t["lines"] > CHUNK_LINES * 1.15:
            chunk, n = chunk + 1, 0
        t["chunk"] = chunk
        n += t["lines"]
    return texts


def write_scope():
    texts, out = in_scope()
    texts = assign_chunks(texts)
    doc = {"note": "Texts in the ANE full read, in reading order, with their reading chunk. Generated by "
                   "`python3 tools/aneread.py scope --write`; see data/ane/SCOPE.md. Chunk assignments are fixed once "
                   "reading starts: regenerate only before then.",
           "texts": texts, "left_out": [{"siglum": s, "title": t, "lines": n, "why": w} for s, t, n, w in out]}
    SCOPE.parent.mkdir(parents=True, exist_ok=True)
    SCOPE.write_text(yaml.safe_dump(doc, allow_unicode=True, sort_keys=False, width=140), encoding="utf-8")
    print(f"{len(texts)} texts, {sum(t['lines'] for t in texts)} lines, {max(t['chunk'] for t in texts)} chunks; "
          f"{len(out)} left out")


# ---------------------------------------------------------------- chunks

def scope():
    return yaml.safe_load(SCOPE.read_text(encoding="utf-8"))["texts"]


def chunk_keys(n, corpus=None):
    """Line keys a chunk's readers must cover."""
    corpus = corpus or originals.ane()
    keys = []
    for t in scope():
        if t["siglum"] not in corpus.keys:
            continue
        if "parts" in t:
            for c, secs in t["parts"].items():
                if int(c) == n:
                    for s in secs:
                        keys += corpus.sections[t["siglum"]].get(s, [])
        elif t["chunk"] == n:
            keys += corpus.keys[t["siglum"]]
    return keys


def chunk_texts(n):
    out = []
    for t in scope():
        if "parts" in t and n in {int(c) for c in t["parts"]}:
            secs = t["parts"].get(n) or t["parts"].get(str(n))
            out.append((t, secs))
        elif "parts" not in t and t["chunk"] == n:
            out.append((t, None))
    return out


def plan():
    rows = defaultdict(lambda: [0, 0, Counter()])
    corpus = originals.ane()
    for t in scope():
        chunks = [int(c) for c in t["parts"]] if "parts" in t else [t["chunk"]]
        for c in chunks:
            rows[c][0] += 1
            rows[c][2][t["tradition"]] += 1
    for c in sorted(rows):
        keys = chunk_keys(c, corpus)
        texts = chunk_texts(c)
        first, last = texts[0][0]["siglum"], texts[-1][0]["siglum"]
        trad = ", ".join(f"{k.replace('ane-', '')} {v}" for k, v in rows[c][2].most_common())
        print(f"{c:2d}  {len(keys):5d} lines  {len(texts):3d} texts  {first} … {last}  ({trad})")


# ---------------------------------------------------------------- printing

def gloss_line(line):
    out = []
    for x in line.get("lemmas") or []:
        g = x.get("gloss") or x.get("sense") or ""
        lem = x.get("lemma", "")
        if g and g not in ("1", lem):
            out.append(f"{lem}[{g}]")
        elif lem:
            out.append(lem)
    return " ".join(out)


def ebl_gloss(lemma, words):
    w = words.get(lemma)
    if not w:
        return ""
    m = re.search(r'"([^"]+)"', w.get("meaning", ""))
    return m.group(1) if m else (w.get("guideWord") or "")


_WORDS = None


def ebl_words():
    global _WORDS
    if _WORDS is None:
        p = RAW / "ebl-words.json"
        _WORDS = json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}
    return _WORDS


def print_keys(keys, corpus, lemmas=False):
    cur_text, cur_sec = None, None
    for k in keys:
        sig, sec, n = k
        if sig != cur_text:
            m = corpus.meta[sig]
            print(f"\n# {sig}: {m.get('title')}  [{m.get('source')}; {m.get('language')}]")
            cur_text, cur_sec = sig, None
        if sec != cur_sec:
            if sec:
                title = corpus.section_titles.get((sig, sec))
                print(f"\n## {sig} {sec}" + (f"  ({title})" if title else ""))
            cur_sec = sec
        line = corpus.lines[k]
        loc = f"{sec}:{n}" if sec else n
        print(f"{loc}  {line.get('text', '')}")
        for v in line.get("variants") or []:
            print(f"    (variant) {v}")
        if lemmas:
            for x in line.get("lemmas") or []:
                g = x.get("gloss") or x.get("sense") or ebl_gloss(x.get("lemma", ""), ebl_words())
                print(f"      {x.get('form', '')}  {x.get('lemma', '')}  {g}  {x.get('pos', '')}")
            continue
        if line.get("translation"):
            rng = f" [{line['translation_lines']}]" if line.get("translation_lines") else ""
            print(f"  ={rng} {re.sub(r'@[a-z]+[{]([^{}]*)[}]', r'\1', line['translation'])}")
        elif line.get("lemmas") and corpus.meta[sig].get("source", "").startswith(("ORACC", "eBL")):
            g = gloss_line(line) if not corpus.meta[sig]["source"].startswith("eBL") else " ".join(
                f"{x['lemma']}[{ebl_gloss(x['lemma'], ebl_words())}]" if ebl_gloss(x["lemma"], ebl_words()) else x["lemma"]
                for x in line["lemmas"])
            if g:
                print(f"  ~ {g}")


def main():
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    cmd = sys.argv[1] if len(sys.argv) > 1 else "plan"
    if cmd == "scope":
        if "--write" in sys.argv:
            return write_scope()
        texts, out = in_scope()
        print(f"{len(texts)} texts, {sum(t['lines'] for t in texts)} lines")
        for k, v in Counter(t["tradition"] for t in texts).items():
            print(f"  {k}: {v} texts, {sum(t['lines'] for t in texts if t['tradition'] == k)} lines")
        return
    if cmd == "plan":
        return plan()
    if cmd == "texts":
        for t in scope():
            if len(sys.argv) > 2 and not (t.get("chunk") == int(sys.argv[2]) or int(sys.argv[2]) in {int(c) for c in t.get("parts", {})}):
                continue
            parts = f"  parts {t['parts']}" if "parts" in t else ""
            print(f"{t['chunk']:3d}  {t['lines']:5d}  {t['siglum']}: {t['title']}  ({t['tradition']}){parts}")
        return
    if cmd == "vocab":
        import motifs
        vocab, _units = motifs.load(strict=False)
        words = [w.lower() for w in sys.argv[2:]]
        if not words:
            sys.exit("give one or more words: the vocabulary is too large to print whole")
        for mid, m in vocab.items():
            if m.get("alias_of"):
                continue
            line = f"{mid}: {m['label']}"
            if all(w in line.lower() for w in words):
                print(line)
        return
    corpus = originals.ane()
    if cmd in ("text", "lemmas") and len(sys.argv) > 2:
        arg = " ".join(sys.argv[2:])
        keys = chunk_keys(int(arg), corpus) if arg.isdigit() else originals.ane_refs(arg, corpus)
        if not keys:
            sys.exit(f"does not resolve: {arg}")
        print_keys(keys, corpus, lemmas=cmd == "lemmas")
        return
    sys.exit(__doc__)


if __name__ == "__main__":
    main()
