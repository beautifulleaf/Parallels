"""Load the Quran and Hebrew Bible into a common shape, with narrative labels.

Each corpus loads as a list of Verse objects, each holding its lemma
occurrences. Lemmas are corpus-specific ids: the QAC lemma for the Quran and
the Strong's number for the Hebrew Bible.
"""
import json
import pathlib
import re
import unicodedata
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from dataclasses import dataclass, field

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
NARRATIVES = ROOT / "data" / "narratives"


@dataclass
class Verse:
    ref: str            # "20:39" or "Exod.2.3"
    document: str       # dispersion unit: surah (Quran) or chapter (Hebrew Bible)
    lemmas: list = field(default_factory=list)
    narratives: set = field(default_factory=set)


@dataclass
class Lemma:
    id: str
    form: str
    pos: str
    root: str = ""
    gloss: str = ""
    translit: str = ""
    definition: str = ""    # full dictionary text, used to check cognate meanings


@dataclass
class Corpus:
    name: str
    verses: list
    lemmas: dict        # id -> Lemma
    narratives: dict    # id -> display name


# ---------------------------------------------------------------- Quran

# QAC POS tags that carry content words. Proper nouns (PN) are excluded from
# the analysis: names concentrate in their own stories trivially.
QURAN_CONTENT_POS = {"N", "V", "ADJ"}
STOP_GLOSS = set("""a an the and or of in on at to for from with by as is are was were be been
it its he him his she her they them their we us our you your i me my this that those these
then so not no indeed surely verily will shall would do did does has have had which who whom
what when there upon into over about one ones all most more than very lo o
properly literally figuratively generally specifically especially used implication extension
intensive causative intransitive transitive also perhaps great various application applications
latitude something abstractly concretely""".split())


def quran_ref_range(r):
    """'7:103-156' or '18:50' -> list of 'surah:verse' refs."""
    s, vv = r.split(":")
    a, _, b = vv.partition("-")
    return [f"{s}:{v}" for v in range(int(a), int(b or a) + 1)]


def head_gloss(glosses):
    """Most frequent content word across a lemma's word-by-word glosses."""
    words = Counter()
    for g in glosses:
        for w in re.findall(r"[a-z]+", (g or "").lower()):
            if w not in STOP_GLOSS and len(w) > 1:
                words[w[:-1] if w.endswith("s") and len(w) > 3 and not w.endswith("ss") else w] += 1
    return words.most_common(1)[0][0] if words else ""


def load_quran():
    glosses = json.loads((RAW / "quran-glosses.json").read_text(encoding="utf-8"))
    verses, lemmas, lemma_glosses = {}, {}, defaultdict(list)
    for line in (RAW / "quran-morphology.txt").read_text(encoding="utf-8").splitlines():
        loc, form, tag, feats = line.split("\t")
        s, v, w, _seg = loc.split(":")
        ref = f"{s}:{v}"
        verse = verses.setdefault(ref, Verse(ref=ref, document=s))
        f = dict(x.split(":", 1) if ":" in x else (x, True) for x in feats.split("|"))
        if "LEM" not in f or "PREF" in f or "SUFF" in f:
            continue
        pos = "PN" if "PN" in f else ("ADJ" if "ADJ" in f else tag)
        if pos not in QURAN_CONTENT_POS:
            continue
        lid = unicodedata.normalize("NFC", f["LEM"])
        verse.lemmas.append(lid)
        lemmas.setdefault(lid, Lemma(id=lid, form=lid, pos=pos, root=f.get("ROOT", "")))
        lemma_glosses[lid].append(glosses.get(f"{s}:{v}:{w}"))
    for lid, lem in lemmas.items():
        lem.gloss = head_gloss(lemma_glosses[lid])
    names = attach_narratives(verses, "quran.yaml", quran_ref_range)
    return Corpus("quran", list(verses.values()), lemmas, names)


# ---------------------------------------------------------------- Hebrew Bible

HEBREW_CONTENT_POS = {"Nc", "V", "A"}   # common noun, verb, adjective
OSIS = "{http://www.bibletechnologies.net/2003/OSIS/namespace}"
BOOK_ORDER = ["Gen", "Exod", "Lev", "Num", "Deut", "Josh", "Judg", "Ruth", "1Sam", "2Sam",
              "1Kgs", "2Kgs", "1Chr", "2Chr", "Ezra", "Neh", "Esth", "Job", "Ps", "Prov",
              "Eccl", "Song", "Isa", "Jer", "Lam", "Ezek", "Dan", "Hos", "Joel", "Amos",
              "Obad", "Jonah", "Mic", "Nah", "Hab", "Zeph", "Hag", "Zech", "Mal"]


def hebrew_pos(morph_part):
    """'Ncmsa' -> 'Nc', 'Vqp3ms' -> 'V', 'Aamsa' -> 'A'."""
    if morph_part.startswith("N"):
        return morph_part[:2]
    return morph_part[:1]


def load_strongs():
    js = (RAW / "strongs-hebrew-dictionary.js").read_text(encoding="utf-8")
    start = js.index("{", js.index("strongsHebrewDictionary"))
    return json.loads(js[start:js.rindex("}") + 1])


def load_hebrew_bible():
    strongs = load_strongs()
    verses, lemmas, pos_votes = {}, {}, defaultdict(Counter)
    for book in BOOK_ORDER:
        tree = ET.parse(RAW / "oshb" / f"{book}.xml")
        for vel in tree.iter(OSIS + "verse"):
            ref = vel.get("osisID")
            verse = verses.setdefault(ref, Verse(ref=ref, document=ref.rsplit(".", 1)[0]))
            for w in vel.iter(OSIS + "w"):
                parts = w.get("lemma", "").split("/")
                if w.get("morph", "").startswith("A"):
                    continue    # Aramaic sections (Daniel, Ezra) would swamp the Hebrew statistics
                morph = w.get("morph", "")[1:].split("/")
                # the content word is the last lemma part that is a number
                for lem_part, m in zip(reversed(parts), reversed(morph)):
                    num = re.match(r"(\d+)", lem_part.strip())
                    if num:
                        lid = "H" + num.group(1)
                        pos_votes[lid][hebrew_pos(m)] += 1
                        verse.lemmas.append(lid)
                        break
    for lid, votes in pos_votes.items():
        pos = votes.most_common(1)[0][0]
        entry = strongs.get(lid, {})
        lemmas[lid] = Lemma(id=lid, form=entry.get("lemma", lid), pos=pos,
                            gloss=re.sub(r"[{}]", "", entry.get("strongs_def") or "").split(";")[0][:80],
                            translit=entry.get("xlit", ""),
                            definition=f"{entry.get('strongs_def', '')} {entry.get('kjv_def', '')}".lower())
    for verse in verses.values():
        verse.lemmas = [l for l in verse.lemmas if lemmas[l].pos in HEBREW_CONTENT_POS]
    names = attach_narratives(verses, "hebrew-bible.yaml", lambda r: hebrew_ref_range(r, verses))
    return Corpus("hebrew-bible", list(verses.values()), lemmas, names)


def hebrew_ref_range(r, verses):
    """'Gen 6-9', 'Gen 13', 'Gen 11:27-25:11', '1Kgs 17:1-2Kgs 2:12' -> osisIDs."""
    m = re.match(r"^(\S+) (\d+)(?::(\d+))?(?:-(?:(\S+) )?(\d+)(?::(\d+))?)?$", r)
    if not m:
        raise ValueError(f"bad range: {r}")
    b1, c1, v1, b2, c2, v2 = m.groups()
    b2 = b2 or b1
    c2 = c2 or c1
    start = (BOOK_ORDER.index(b1), int(c1), int(v1 or 1))
    end = (BOOK_ORDER.index(b2), int(c2), int(v2) if v2 else 10**6)
    out = []
    for ref in verses:
        b, c, v = ref.split(".")
        key = (BOOK_ORDER.index(b), int(c), int(v))
        if start <= key <= end:
            out.append(ref)
    return out


# ---------------------------------------------------------------- shared

def attach_narratives(verses, filename, expand):
    spec = yaml.safe_load((NARRATIVES / filename).read_text(encoding="utf-8"))
    names = {}
    for nid, n in spec["narratives"].items():
        names[nid] = n["name"]
        for r in n["ranges"]:
            refs = expand(r)
            if not refs:
                raise ValueError(f"{filename}: range {r} matched no verses")
            for ref in refs:
                if ref not in verses:
                    raise ValueError(f"{filename}: {ref} not in corpus")
                verses[ref].narratives.add(nid)
    return names


def skeleton_hebrew(s):
    """Consonantal skeleton of a pointed Hebrew word, final forms normalized."""
    s = "".join(c for c in unicodedata.normalize("NFD", s) if not unicodedata.combining(c))
    s = s.translate(str.maketrans("ךםןףץ", "כמנפצ"))
    return "".join(c for c in s if "א" <= c <= "ת")
