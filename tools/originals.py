"""Fill lead passages with original-language text from the corpora.

Usage: python3 tools/originals.py

For every passage in leads/*.md whose ref is a Quran, Hebrew Bible or
ancient Near Eastern reference (see `ane_refs`), sets `text` (the original), `lang`, and `source`. Passages longer
than MAX_VERSES are left without text and marked as such. A passage whose
text came from somewhere else (a different `source`) is not overwritten.
Notes and all other fields are left untouched.
"""
import json
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
    m = re.match(r"^((?:\d ?)?[A-Z][a-z]+(?: of [A-Z][a-z]+)?) (\d+)(?::(\d+))?(?:[–-](\d+)(?::(\d+))?)?$", spec.strip())
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


# ---------------------------------------------------------------- ancient Near East

ANE_INDEX = ROOT / "data" / "ane" / "texts.yaml"
ANE_RAW = corpora.RAW / "ane"
ANE_LANG = {"akk": "akk", "sux": "sux", "uga": "uga", "hit": "hit", "egy": "egy"}
_ANE = None


class AneCorpus:
    """The ANE texts in scope (data/ane/texts.yaml), read from data/raw/ane/.

    A line's key is (siglum, section, n). References look like
      'Gilg SB XI:11', 'Gilg SB XI:11-20', 'Gilg SB XI:300-XII:5', 'Gilg SB XI' (a section),
      'ETCSL 1.7.4 C:1-27', 'KTU 1.3 II:5', 'Gilg SB' (a whole text);
    in a text with one unnamed section the line stands alone: 'ETCSL 1.1.1 5-10'.
    Several references can be joined with ';'."""

    def __init__(self):
        spec = yaml.safe_load(ANE_INDEX.read_text(encoding="utf-8"))
        self.meta, self.keys, self.lines, self.sections, self.section_titles = {}, {}, {}, {}, {}
        for t in spec["texts"]:
            path = ANE_RAW / t["file"]
            if not path.exists():
                continue
            doc = json.loads(path.read_text(encoding="utf-8"))
            sig = t["siglum"]
            self.meta[sig] = {**{k: doc.get(k) for k in ("title", "language", "source", "edition", "license", "url")}, **t}
            keys, secs = [], {}
            for s in doc["sections"]:
                if s.get("title") and s["lines"]:
                    self.section_titles[(sig, norm_loc(s["name"], s["lines"][0]["n"])[0])] = s["title"]
                for line in s["lines"]:
                    sec, n = norm_loc(s["name"], line["n"])
                    key = (sig, sec, n)
                    if key in self.lines:
                        continue
                    self.lines[key] = line
                    keys.append(key)
                    secs.setdefault(sec, []).append(key)
            self.keys[sig] = keys
            self.sections[sig] = secs
        self.pos = {k: i for sig in self.keys for i, k in enumerate(self.keys[sig])}
        self.sigla = sorted(self.keys, key=len, reverse=True)

    def siglum_of(self, ref):
        for sig in self.sigla:
            if ref == sig or ref.startswith(sig + " "):
                return sig
        return None

    def refs(self, spec):
        out = []
        for part in spec.split(";"):
            part = part.strip()
            sig = self.siglum_of(part)
            if sig is None:
                return None
            rest = part[len(sig):].strip()
            found = self._resolve(sig, rest)
            if found is None:
                return None
            out += found
        return out or None

    def _loc(self, sig, loc, default_sec=None):
        """'XI:11' -> key; '11' -> key in default_sec or the single unnamed section."""
        secs = self.sections[sig]
        if ":" in loc:
            sec, n = loc.split(":", 1)
        elif default_sec is not None:
            sec, n = default_sec, loc
        elif list(secs) == [""]:
            sec, n = "", loc
        else:
            return None
        key = (sig, sec, n)
        return key if key in self.lines else None

    def _resolve(self, sig, rest):
        secs = self.sections[sig]
        if not rest:
            return list(self.keys[sig])
        if rest in secs and rest != "":
            return list(secs[rest])
        a, sep, b = rest.partition("-")
        start = self._loc(sig, a)
        if start is None:
            return None
        if not sep:
            return [start]
        end = self._loc(sig, b, default_sec=start[1])
        if end is None or self.pos[end] < self.pos[start]:
            return None
        return self.keys[sig][self.pos[start]:self.pos[end] + 1]

    def label(self, key):
        sig, sec, n = key
        return f"{sig} {sec}:{n}" if sec else f"{sig} {n}"


def norm_loc(section, n):
    """Section and line ids as single tokens. ORACC labels such as 'o i 10' or 'Seg.A, 5' split into a
    section ('o.i', 'Seg.A') and a line; characters used by the reference syntax are replaced."""
    section, n = section.strip(), str(n).strip()
    if not section and " " in n:
        section, _, n = n.rpartition(" ")
    section = re.sub(r"§\s+", "§", section)          # Hittite paragraphs: '§ 12' -> '§12'
    section = re.sub(r"[,\s]+", ".", section).strip(".")
    n = re.sub(r"[\s:;,]+", "_", n).replace("-", "–")
    n = re.sub(r"^0+(?=\d)", "", n)            # ORACC pads line numbers: 001 -> 1
    section = section.replace(":", ".").replace("-", "–")
    return section, n


def ane():
    global _ANE
    if _ANE is None:
        _ANE = AneCorpus()
    return _ANE


def ane_refs(spec, corpus=None):
    """ANE reference -> ordered line keys, or None if it does not resolve."""
    if not ANE_INDEX.exists():
        return None
    return (corpus or ane()).refs(spec)


def ane_line_text(line):
    return line.get("text", "")


def ane_original(ref):
    corpus = ane()
    keys = ane_refs(ref, corpus)
    if keys is None:
        return None
    sig = keys[0][0]
    m = corpus.meta[sig]
    source = f"{m.get('source')}: {m.get('title')}"
    lang = ANE_LANG.get(m.get("language") or "", m.get("language") or "")
    if len(keys) > MAX_VERSES:
        return ("", lang, source)
    if len(keys) == 1:
        return (ane_line_text(corpus.lines[keys[0]]), lang, source)
    return (" ".join(f"({k[1] + ':' if k[1] else ''}{k[2]}) {ane_line_text(corpus.lines[k])}" for k in keys), lang, source)


def original_for(passage, quran_text, hebrew_text):
    """Returns (text, lang, source) or None when the ref is not parseable."""
    ref = passage.get("ref", "")
    if str(passage.get("tradition", "")).startswith("ane-"):
        return ane_original(ref)
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
        if p.get("text") and p.get("source") not in (QURAN_SOURCE, HEBREW_SOURCE) and not str(p.get("tradition", "")).startswith("ane-"):
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
