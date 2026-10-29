"""Helpers for the full read of the Quran.

Usage:
  python3 tools/qread.py plan                  # list the reading chunks
  python3 tools/qread.py chunk <n>             # print a whole chunk, verse by verse
  python3 tools/qread.py surah <s1> [<s2>]     # print surahs s1..s2
  python3 tools/qread.py range <s>:<v1>-<v2>   # print a verse range

Text is the Quranic Arabic Corpus (Uthmani script). Chunks split the Quran
at surah boundaries into pieces of roughly equal word count.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import originals  # noqa: E402

CHUNK_WORDS = 9800


def surahs(text):
    out = {}
    for ref in text:
        s, _v = ref.split(":")
        out.setdefault(int(s), []).append(ref)
    return [(s, sorted(refs, key=lambda r: int(r.split(":")[1]))) for s, refs in sorted(out.items())]


def plan(text):
    chunks, cur, n = [], [], 0
    for s, refs in surahs(text):
        words = sum(len(text[r].split()) for r in refs)
        if n and n + words > CHUNK_WORDS * 1.15:
            chunks.append(cur)
            cur, n = [], 0
        cur.append((s, refs))
        n += words
    if cur:
        chunks.append(cur)
    return chunks


def show(refs, text):
    for r in refs:
        print(f"{r} {text[r]}")


def main():
    text = originals.load_quran_text()
    cmd = sys.argv[1] if len(sys.argv) > 1 else "plan"
    chunks = plan(text)
    if cmd == "plan":
        for i, ch in enumerate(chunks, 1):
            refs = [r for _, rs in ch for r in rs]
            words = sum(len(text[r].split()) for r in refs)
            print(f"{i:2d}  surahs {ch[0][0]:3d}–{ch[-1][0]:3d}  {len(refs):5d} verses  {words:6d} words")
    elif cmd == "chunk":
        for s, refs in chunks[int(sys.argv[2]) - 1]:
            print(f"\n## Surah {s}")
            show(refs, text)
    elif cmd == "range":
        show(originals.quran_refs(sys.argv[2], text), text)
    elif cmd == "surah":
        s1 = int(sys.argv[2])
        s2 = int(sys.argv[3]) if len(sys.argv) > 3 else s1
        for s, refs in surahs(text):
            if s1 <= s <= s2:
                print(f"\n## Surah {s}")
                show(refs, text)
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
