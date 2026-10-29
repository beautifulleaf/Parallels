"""Helpers for the full read of the Hebrew Bible.

Usage:
  python3 tools/hbread.py plan                 # list the reading chunks
  python3 tools/hbread.py text <chunk>         # print a chunk's text, verse by verse
  python3 tools/hbread.py text <Book> <c1> [c2]  # print chapters c1..c2 of one book
  python3 tools/hbread.py vocab [words...]     # print motifs (id: label), optionally only those matching all words

Text is the Westminster Leningrad Codex (OSHB) with cantillation marks
removed and vowels kept. Chunks split the canon at chapter boundaries into
pieces of roughly equal verse count.
"""
import pathlib
import re
import sys

import yaml

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import corpora  # noqa: E402
import originals  # noqa: E402

CHUNK_VERSES = 970
CANTILLATION = re.compile("[֑-ֽ֯]")


def chapters(text):
    """Ordered list of (book, chapter, [verse osisIDs])."""
    out, index = [], {}
    for ref in text:
        b, c, _v = ref.split(".")
        key = (b, int(c))
        if key not in index:
            index[key] = len(out)
            out.append((b, int(c), []))
        out[index[key]][2].append(ref)
    order = {b: i for i, b in enumerate(corpora.BOOK_ORDER)}
    return sorted(out, key=lambda x: (order[x[0]], x[1]))


def plan(text):
    chunks, cur, n = [], [], 0
    for b, c, refs in chapters(text):
        if n >= CHUNK_VERSES and cur:
            chunks.append(cur)
            cur, n = [], 0
        cur.append((b, c, refs))
        n += len(refs)
    if cur:
        chunks.append(cur)
    return chunks


def label(chunk):
    first, last = chunk[0], chunk[-1]
    return f"{first[0]} {first[1]} – {last[0]} {last[1]}"


def print_chapters(chs, text):
    for b, c, refs in chs:
        print(f"\n## {b} {c}")
        for r in refs:
            print(f"{c}:{r.rsplit('.', 1)[1]} {CANTILLATION.sub('', text[r])}")


def main():
    text = originals.load_hebrew_text()
    cmd = sys.argv[1] if len(sys.argv) > 1 else "plan"
    chunks = plan(text)
    if cmd == "plan":
        for i, ch in enumerate(chunks, 1):
            print(f"{i:2d}  {label(ch):32s} {sum(len(r) for _, _, r in ch):5d} verses  {len(ch):3d} chapters")
    elif cmd == "text" and len(sys.argv) == 3:
        print_chapters(chunks[int(sys.argv[2]) - 1], text)
    elif cmd == "text":
        book, c1 = sys.argv[2], int(sys.argv[3])
        c2 = int(sys.argv[4]) if len(sys.argv) > 4 else c1
        print_chapters([x for x in chapters(text) if x[0] == book and c1 <= x[1] <= c2], text)
    elif cmd == "vocab":
        import motifs
        vocab, _units = motifs.load(strict=False)
        words = [w.lower() for w in sys.argv[2:]]
        for mid, m in vocab.items():
            if m.get("alias_of"):
                continue
            line = f"{mid}: {m['label']}"
            if all(w in line.lower() for w in words):
                print(line)
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
