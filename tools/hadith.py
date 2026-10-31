"""The hadith corpus: al-Jāmiʿ al-Kāmil fī l-ḥadīth al-ṣaḥīḥ al-shāmil (Shamela book 47).

Usage:
  python3 tools/hadith.py plan                 # the reading chunks: pages and books
  python3 tools/hadith.py show <chunk>         # the hadith a reader saved for a chunk, one line each (⏎ marks a line break)
  python3 tools/hadith.py check <chunk>        # check a chunk's raw file: every page read, every line well formed

The text reaches the project only through the Shamela MCP tools: the library is the user's own, and
shamela.ws disallows Anthropic's crawlers, so it is never fetched from the web. Readers read the pages
with `shamela_get_pages_range` and save each hadith's matn in `data/raw/hadith/NN.json` (gitignored;
the compilation is modern and copyrighted). That file follows the ANE text model, so references
resolve like ANE ones:

  siglum `Jāmiʿ`, section = the book number (1-67), line = `<page_id>.<k>`, the k-th hadith (•) that
  begins on that Shamela page:  'Jāmiʿ 47:4925.2', 'Jāmiʿ 47:4925.1-4926.3', 'Jāmiʿ 47' (a whole book).

Page ids are Shamela's internal ids; each line also keeps the printed page ('7/ 470') for citation.
"""
import json
import pathlib
import re
import sys

import yaml

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import corpora  # noqa: E402
import originals  # noqa: E402

ROOT = corpora.ROOT
RAW = corpora.RAW / "hadith"
BOOKS = ROOT / "data" / "hadith" / "books.yaml"
SIGLUM = "Jāmiʿ"
CHUNK_PAGES = 120
# narrative and cosmology first, so comparisons can start early (docs/prompts/hadith-full-read.md)
PRIORITY = [1, 45, 46, 47, 48, 58, 60, 65, 66, 67]


def books():
    return yaml.safe_load(BOOKS.read_text(encoding="utf-8"))["books"]


def plan():
    """Chunks of about CHUNK_PAGES pages, priority books first, books kept whole where they fit.
    Each chunk: list of (book number, first page, last page)."""
    bs = {b["n"]: b for b in books()}
    order = PRIORITY + [n for n in sorted(bs) if n not in PRIORITY]
    chunks, cur, size = [], [], 0
    for n in order:
        b = bs[n]
        first, last = b["first_page"], b["last_page"]
        while first <= last:
            room = CHUNK_PAGES - size
            span = last - first + 1
            if span <= room or (span <= room + CHUNK_PAGES // 4 and not cur):
                cur.append((n, first, last))
                size += span
                first = last + 1
            elif room >= CHUNK_PAGES // 4:
                cur.append((n, first, first + room - 1))
                first += room
                size = CHUNK_PAGES
            else:
                size = CHUNK_PAGES
            if size >= CHUNK_PAGES:
                chunks.append(cur)
                cur, size = [], 0
    if cur:
        chunks.append(cur)
    return chunks


def chunk_pages(n):
    return {p for _, a, b in plan()[n - 1] for p in range(a, b + 1)}


def raw_path(n):
    return RAW / f"{n:02d}.json"


class HadithCorpus(originals.AneCorpus):
    """All saved chunks as one text: siglum Jāmiʿ, sections = books, lines = '<page>.<k>'."""

    def __init__(self):
        self.meta, self.keys, self.lines, self.sections, self.section_titles = {}, {}, {}, {}, {}
        lines = []
        for path in sorted(RAW.glob("[0-9]*.json")):
            doc = json.loads(path.read_text(encoding="utf-8"))
            for s in doc.get("sections") or []:
                self.section_titles[(SIGLUM, str(s["name"]))] = s.get("title", "")
                for line in s["lines"]:
                    lines.append((int(s["name"]), line))
        lines.sort(key=lambda x: (x[0], int(str(x[1]["n"]).split(".")[0]), int(str(x[1]["n"]).split(".")[1])))
        keys, secs = [], {}
        for book, line in lines:
            key = (SIGLUM, str(book), str(line["n"]))
            if key in self.lines:
                continue
            self.lines[key] = line
            keys.append(key)
            secs.setdefault(str(book), []).append(key)
        self.keys[SIGLUM], self.sections[SIGLUM] = keys, secs
        self.meta[SIGLUM] = {"title": "al-Jāmiʿ al-Kāmil fī l-ḥadīth al-ṣaḥīḥ al-shāmil", "language": "ar",
                             "source": "Shamela book 47, through the user's library (Shamela MCP tools)",
                             "edition": "not recorded in Shamela", "license": "copyrighted; raw text kept out of git"}
        self.pos = {k: i for i, k in enumerate(keys)}
        self.sigla = [SIGLUM]


_CORPUS = None


def corpus():
    global _CORPUS
    if _CORPUS is None:
        _CORPUS = HadithCorpus()
    return _CORPUS


def hadith_refs(spec):
    return corpus().refs(spec)


def original(ref):
    """(text, lang, source) for a hadith reference, as originals.original_for returns."""
    keys = hadith_refs(ref)
    if not keys:
        return None
    c = corpus()
    if len(keys) > originals.MAX_VERSES:
        return ("", "ar", c.meta[SIGLUM]["source"])
    parts = []
    for k in keys:
        line = c.lines[k]
        parts.append((f"({k[2]}) " if len(keys) > 1 else "") + line.get("matn", line.get("text", "")))
    return (" ".join(parts), "ar", "al-Jāmiʿ al-Kāmil (Shamela 47), " + ", ".join(
        sorted({f"p. {c.lines[k].get('printed_page', '')}" for k in keys})))


def check(n):
    """Problems in a chunk's raw file, or [] when it is complete."""
    path = raw_path(n)
    if not path.exists():
        return [f"{path}: missing"]
    doc = json.loads(path.read_text(encoding="utf-8"))
    errors = []
    want = chunk_pages(n)
    got = {p["page_id"] for p in doc.get("pages") or []}
    if want - got:
        errors.append(f"chunk {n}: {len(want - got)} pages not read (e.g. {min(want - got)})")
    if got - want:
        errors.append(f"chunk {n}: pages outside the chunk recorded (e.g. {min(got - want)})")
    book_of = {p: b for b, a, z in plan()[n - 1] for p in range(a, z + 1)}
    seen = set()
    per_page = {}
    for s in doc.get("sections") or []:
        for line in s["lines"]:
            per_page[str(line.get("n", "")).split(".")[0]] = per_page.get(str(line.get("n", "")).split(".")[0], 0) + 1
    for p in doc.get("pages") or []:      # every hadith the book marks with "•" is a line
        if "bullets" not in p:
            errors.append(f"page {p['page_id']}: no 'bullets' count")
        elif p["bullets"] != per_page.get(str(p["page_id"]), 0):
            errors.append(f"page {p['page_id']}: {p['bullets']} hadith marked with • but "
                          f"{per_page.get(str(p['page_id']), 0)} saved")
    for s in doc.get("sections") or []:
        for line in s["lines"]:
            nid = str(line.get("n", ""))
            m = re.fullmatch(r"(\d+)\.(\d+)", nid)
            if not m:
                errors.append(f"line id {nid!r}: must be <page_id>.<k>")
                continue
            page = int(m.group(1))
            if page not in want:
                errors.append(f"{nid}: page outside chunk {n}")
            elif str(book_of[page]) != str(s["name"]):
                errors.append(f"{nid}: page {page} belongs to book {book_of[page]}, not {s['name']}")
            if nid in seen:
                errors.append(f"{nid}: duplicate")
            seen.add(nid)
            if not (line.get("matn") or "").strip():
                errors.append(f"{nid}: empty matn")
    return errors


def main():
    args = sys.argv[1:]
    cmd = args[0] if args else "plan"
    if cmd == "plan":
        for i, ch in enumerate(plan(), 1):
            pages = sum(b - a + 1 for _, a, b in ch)
            print(f"{i:2d}  {pages:4d} pages  " + ", ".join(f"book {n} p.{a}-{b}" for n, a, b in ch))
        return
    if cmd == "check":
        errs = check(int(args[1]))
        doc = json.loads(raw_path(int(args[1])).read_text(encoding="utf-8")) if raw_path(int(args[1])).exists() else {}
        n = sum(len(s["lines"]) for s in doc.get("sections") or [])
        print(f"chunk {args[1]}: {len(doc.get('pages') or [])} pages, {n} hadith")
        if errs:
            print("\n".join(errs[:40]), file=sys.stderr)
            sys.exit(1)
        print("ok")
        return
    if cmd == "show":
        doc = json.loads(raw_path(int(args[1])).read_text(encoding="utf-8"))
        for s in doc["sections"]:
            print(f"## {SIGLUM} {s['name']}: {s.get('title', '')}")
            for line in s["lines"]:
                print(f"{SIGLUM} {s['name']}:{line['n']}  [{line.get('printed_page', '')}] {line.get('companion', '')} | "
                      f"{line.get('grade', '')} | " + " ⏎ ".join(x.strip() for x in line.get('matn', '').splitlines() if x.strip()))
        return
    sys.exit(__doc__)


if __name__ == "__main__":
    main()
