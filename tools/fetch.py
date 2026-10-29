"""Download the raw corpora used by the lexical pipeline into data/raw/.

Usage: python3 tools/fetch.py

Raw data is not committed (see .gitignore); rerun this on a fresh checkout.
Sources:
  - Quranic Arabic Corpus morphology (GPL), via the mustafa0x/quran-morphology mirror
  - quran.com word-by-word English glosses (API v4)
  - Open Scriptures Hebrew Bible (OSHB) morphology, WLC text (CC BY 4.0)
  - Strong's Hebrew dictionary (Open Scriptures JSON, CC BY-SA)
"""
import json
import pathlib
import time
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"

QURAN_MORPHOLOGY = "https://raw.githubusercontent.com/mustafa0x/quran-morphology/master/quran-morphology.txt"
QURAN_WORDS = "https://api.quran.com/api/v4/verses/by_chapter/{ch}?words=true&language=en&word_fields=location&per_page=50&page={page}"
OSHB = "https://raw.githubusercontent.com/openscriptures/morphhb/master/wlc/{book}.xml"
STRONGS = "https://raw.githubusercontent.com/openscriptures/strongs/master/hebrew/strongs-hebrew-dictionary.js"

OSHB_BOOKS = ["Gen", "Exod", "Lev", "Num", "Deut", "Josh", "Judg", "Ruth", "1Sam", "2Sam",
              "1Kgs", "2Kgs", "1Chr", "2Chr", "Ezra", "Neh", "Esth", "Job", "Ps", "Prov",
              "Eccl", "Song", "Isa", "Jer", "Lam", "Ezek", "Dan", "Hos", "Joel", "Amos",
              "Obad", "Jonah", "Mic", "Nah", "Hab", "Zeph", "Hag", "Zech", "Mal"]


def get(url, retries=4):
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "parallels-pipeline"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except Exception:
            if attempt == retries - 1:
                raise
            time.sleep(2 ** (attempt + 1))


def save(path, url):
    if path.exists():
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(get(url))
    print("fetched", path.relative_to(ROOT))


def fetch_quran_glosses():
    path = RAW / "quran-glosses.json"
    if path.exists():
        return
    glosses = {}
    for ch in range(1, 115):
        page = 1
        while page:
            data = json.loads(get(QURAN_WORDS.format(ch=ch, page=page)))
            for verse in data["verses"]:
                for w in verse["words"]:
                    if w.get("char_type_name") == "word":
                        glosses[w["location"]] = (w.get("translation") or {}).get("text")
            page = data["pagination"]["next_page"]
    path.write_text(json.dumps(glosses, ensure_ascii=False), encoding="utf-8")
    print("fetched", path.relative_to(ROOT), len(glosses), "word glosses")


def main():
    save(RAW / "quran-morphology.txt", QURAN_MORPHOLOGY)
    fetch_quran_glosses()
    for book in OSHB_BOOKS:
        save(RAW / "oshb" / f"{book}.xml", OSHB.format(book=book))
    save(RAW / "strongs-hebrew-dictionary.js", STRONGS)


if __name__ == "__main__":
    main()
