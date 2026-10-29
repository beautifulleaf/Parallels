"""Fill lead passages with original-language text from the corpora.

Usage: python3 tools/originals.py

For every passage in leads/*.md whose ref is a Quran or Hebrew Bible
reference, sets `text` (the original), `lang`, and `source`. Passages longer
than MAX_VERSES are left without text and marked as such. A passage whose
text came from somewhere else (a different `source`) is not overwritten.
Notes and all other fields are left untouched.
"""
import pathlib
import re
import sys
import xml.etree.ElementTree as ET

import yaml

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import corpora  # noqa: E402

ROOT = corpora.ROOT
LEADS = ROOT / "leads"
MAX_VERSES = 12
QURAN_SOURCE = "Quranic Arabic Corpus (Uthmani script)"
HEBREW_SOURCE = "Westminster Leningrad Codex (OSHB)"

HEBREW_BOOKS = {
    "Genesis": "Gen", "Exodus": "Exod", "Leviticus": "Lev", "Numbers": "Num", "Deuteronomy": "Deut",
    "Joshua": "Josh", "Judges": "Judg", "Ruth": "Ruth", "1 Samuel": "1Sam", "2 Samuel": "2Sam",
    "1 Kings": "1Kgs", "2 Kings": "2Kgs", "1 Chronicles": "1Chr", "2 Chronicles": "2Chr", "Ezra": "Ezra",
    "Nehemiah": "Neh", "Esther": "Esth", "Job": "Job", "Psalms": "Ps", "Psalm": "Ps", "Proverbs": "Prov",
    "Ecclesiastes": "Eccl", "Song of Songs": "Song", "Isaiah": "Isa", "Jeremiah": "Jer",
    "Lamentations": "Lam", "Ezekiel": "Ezek", "Daniel": "Dan", "Hosea": "Hos", "Joel": "Joel",
    "Amos": "Amos", "Obadiah": "Obad", "Jonah": "Jonah", "Micah": "Mic", "Nahum": "Nah",
    "Habakkuk": "Hab", "Zephaniah": "Zeph", "Haggai": "Hag", "Zechariah": "Zech", "Malachi": "Mal",
}
HEBREW_BOOKS.update({code: code for code in corpora.BOOK_ORDER})


def load_quran_text():
    words = {}
    for line in (corpora.RAW / "quran-morphology.txt").read_text(encoding="utf-8").splitlines():
        loc, form, _tag, _f = line.split("\t")
        s, v, w, _seg = loc.split(":")
        words.setdefault(f"{s}:{v}", {}).setdefault(int(w), []).append(form)
    return {ref: " ".join("".join(ws[k]) for k in sorted(ws)) for ref, ws in words.items()}


def load_hebrew_text():
    texts = {}
    for book in corpora.BOOK_ORDER:
        tree = ET.parse(corpora.RAW / "oshb" / f"{book}.xml")
        for vel in tree.iter(corpora.OSIS + "verse"):
            ws = ["".join(w.itertext()).replace("/", "") for w in vel.iter(corpora.OSIS + "w")]
            texts[vel.get("osisID")] = " ".join(ws)
    return texts


def quran_refs(spec, text):
    """'20:38–39; 28:7–13' or '3:35–37, 3:44' -> ordered verse refs."""
    refs = []
    for part in re.split(r"[;,]\s*", spec):
        m = re.match(r"^(\d+):(\d+)(?:[–-](\d+))?$", part.strip())
        if not m:
            return None
        s, a, b = m.group(1), int(m.group(2)), int(m.group(3) or m.group(2))
        refs += [f"{s}:{v}" for v in range(a, b + 1)]
    return refs if all(r in text for r in refs) else None


def hebrew_refs(spec, text):
    """'Exodus 2:1–10', 'Genesis 6–9', 'Proverbs 22:17–24:22' -> osisIDs."""
    m = re.match(r"^((?:\d )?[A-Z][a-z]+(?: of [A-Z][a-z]+)?) (\d+)(?::(\d+))?(?:[–-](\d+)(?::(\d+))?)?$", spec.strip())
    if not m or m.group(1) not in HEBREW_BOOKS:
        return None
    book = HEBREW_BOOKS[m.group(1)]
    c1, v1, x, y = m.group(2), m.group(3), m.group(4), m.group(5)
    if v1 is None:                       # whole chapters: 'Genesis 6–9'
        start, end = (int(c1), 1), (int(x or c1), 10**6)
    elif y is not None:                  # 'Proverbs 22:17–24:22'
        start, end = (int(c1), int(v1)), (int(x), int(y))
    else:                                # 'Exodus 2:1–10' or 'Exodus 15:4'
        start, end = (int(c1), int(v1)), (int(c1), int(x or v1))
    refs = []
    for ref in text:
        b, c, v = ref.split(".")
        if b == book and start <= (int(c), int(v)) <= end:
            refs.append(ref)
    return refs or None


def original_for(passage, quran_text, hebrew_text):
    """Returns (text, lang, source) or None when the ref is not parseable."""
    ref = passage.get("ref", "")
    if passage.get("tradition") == "islam" and ref.startswith("Quran "):
        refs = quran_refs(ref[len("Quran "):], quran_text)
        if refs is None:
            return None
        if len(refs) > MAX_VERSES:
            return ("", "ar", QURAN_SOURCE)
        if len(refs) == 1:
            return (quran_text[refs[0]], "ar", QURAN_SOURCE)
        return (" ".join(f"({r}) {quran_text[r]}" for r in refs), "ar", QURAN_SOURCE)
    refs = hebrew_refs(ref, hebrew_text)
    if refs is None:
        return None
    if len(refs) > MAX_VERSES:
        return ("", "he", HEBREW_SOURCE)
    if len(refs) == 1:
        return (hebrew_text[refs[0]], "he", HEBREW_SOURCE)
    return (" ".join(f"({r.split('.', 1)[1].replace('.', ':')}) {hebrew_text[r]}" for r in refs), "he", HEBREW_SOURCE)


def fill_passages(passages, quran_text, hebrew_text):
    changed = 0
    for p in passages or []:
        if p.get("text") and p.get("source") not in (QURAN_SOURCE, HEBREW_SOURCE):
            continue
        found = original_for(p, quran_text, hebrew_text)
        if not found:
            continue
        text, lang, source = found
        new = {"lang": lang, "source": source}
        if text:
            new["text"] = text
        else:
            new["text_omitted"] = f"longer than {MAX_VERSES} verses; read it in the source"
        if any(p.get(k) != v for k, v in new.items()):
            p.pop("text", None)
            p.pop("text_omitted", None)
            p.update(new)
            changed += 1
    return changed


def main():
    quran_text, hebrew_text = load_quran_text(), load_hebrew_text()
    total = 0
    for path in sorted(LEADS.glob("*.md")):
        if path.name == "README.md":
            continue
        raw = path.read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---\n?(.*)$", raw, re.S)
        meta, body = yaml.safe_load(m.group(1)), m.group(2)
        changed = fill_passages(meta.get("passages"), quran_text, hebrew_text)
        if changed:
            path.write_text("---\n" + yaml.safe_dump(meta, allow_unicode=True, sort_keys=False, width=100)
                            + "---\n" + body, encoding="utf-8")
            print(f"{path.name}: {changed} passage(s) filled")
            total += changed
    print(f"{total} passage(s) updated")


if __name__ == "__main__":
    main()
