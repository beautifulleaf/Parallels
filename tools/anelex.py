"""Lexical links between the ancient Near Eastern languages and the Hebrew Bible and Quran, and loan chains.

Usage: python3 tools/anelex.py        # writes results/lexical/loan-chains.json and prints a summary
(tools/lexical.py runs it too, checks its benchmarks and writes its leads.)

Languages and their lemmas:
  sux  Sumerian: ETCSL lemmas (with ETCSL glosses) and ORACC epsd2 citation forms, counted in the texts read
  akk  Akkadian: the eBL dictionary (meaning, forms, logograms), counted in the eBL and ORACC texts
  uga  Ugaritic: ORACC's lemmatized Ugaritic letters and records (English glosses) and EUPT's lemmas
  arc  Biblical Aramaic and he Hebrew: OSHB lemmas with Strong's definitions
  ar   Arabic: Quranic Arabic Corpus lemmas with word-by-word glosses

Edges:
  sux -> akk  loan: an Akkadian word written with a Sumerian logogram (eBL: kussû = GU.ZA) whose
              Sumerian reading is a Sumerian lemma (gu-za) and sounds like the Akkadian word, voicing
              aside (g~k, d~t, b~p, z~s). Basis: lexicon (the logogram) and original (the forms).
  akk -> arc/he/ar, uga -> he/arc/ar, arc -> ar
              cognate or loan: the consonants correspond (gutturals and weak letters set aside, sibilants
              merged) and the meanings share a word (eBL meaning or ORACC gloss against Strong's
              definition or the Quran's word glosses). A geminate may dissimilate to r + consonant
              (Akkadian kussû, Hebrew kissēʾ ~ Aramaic korsêʾ, Arabic kursī). Basis: original + gloss.
A loan chain is a path through these edges from Sumerian or Akkadian to Hebrew, Aramaic or Arabic.
The meaning check is gloss-based: every link is a lead to check in the originals.
"""
import json
import pathlib
import re
import sys
import unicodedata
from collections import Counter, defaultdict

import yaml

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import corpora  # noqa: E402

ROOT = corpora.ROOT
RAW = corpora.RAW / "ane"
OUT = ROOT / "results" / "lexical"
SCOPE = ROOT / "data" / "ane" / "texts.yaml"

STOP = corpora.STOP_GLOSS | set("""occas transf part piece kind sort person thing type general term
mng meaning see cf lit esp opp pl sg du qv var adj adv obj subj usu well down away ing act good state time
oneself political take two one making make put set give get go come bring hand place side man men
being have having become becoming certain other own""".split())


# ---------------------------------------------------------------- sound

def plain(s):
    s = unicodedata.normalize("NFD", s or "")
    return "".join(c for c in s if not unicodedata.combining(c)).lower()


SIBILANT = "S"
LATIN_CLASS = {"s": SIBILANT, "š": SIBILANT, "ś": SIBILANT, "ṯ": SIBILANT, "ṣ": "C", "ẓ": "C", "ḍ": "C",
               "ṭ": "T", "z": "Z", "ḏ": "Z", "b": "b", "p": "p", "f": "p", "g": "g", "k": "k", "q": "q",
               "d": "d", "t": "t", "l": "l", "m": "m", "n": "n", "r": "r", "ḫ": "H", "ḥ": "H", "x": "H",
               "h": "", "ʾ": "", "'": "", "ʿ": "", "ġ": "", "w": "", "y": "", "j": "", "v": "b"}


def latin_skeleton(word):
    """Consonant classes of a transliterated word (Akkadian, Ugaritic, Sumerian)."""
    w = unicodedata.normalize("NFC", (word or "").lower())
    w = re.sub(r"[₀-₉0-9{}()\[\]⸢⸣<>.?!/\\+*-]", "", w)
    out = []
    for ch in w:
        base = ch if ch in LATIN_CLASS else plain(ch)
        if base in LATIN_CLASS:
            out.append(LATIN_CLASS[base])
    return "".join(out)


def latin_geminates(word):
    """Positions (in skeleton terms) of doubled consonants, for the rC dissimilation."""
    w = re.sub(r"[^a-zšṣṭḫḥśṯḏẓġʾʿ]", "", plain_keep(word))
    sk, gem, prev = [], set(), None
    for ch in w:
        cls = LATIN_CLASS.get(ch, None) if ch in LATIN_CLASS else None
        if cls is None or cls == "":
            prev = None
            continue
        if ch == prev:
            gem.add(len(sk) - 1)
            continue
        sk.append(cls)
        prev = ch
    return "".join(sk), gem


def plain_keep(s):
    """Lowercase, length marks removed, special consonants kept."""
    s = unicodedata.normalize("NFC", (s or "").lower())
    return s.translate(str.maketrans("āēīūâêîûàèìùáéíú", "aeiuaeiuaeiuaeiu"))


HEB_CLASS = {"א": "", "ב": "b", "ג": "g", "ד": "d", "ה": "", "ו": "", "ז": "Z", "ח": "H", "ט": "T", "י": "",
             "כ": "k", "ך": "k", "ל": "l", "מ": "m", "ם": "m", "נ": "n", "ן": "n", "ס": SIBILANT, "ע": "",
             "פ": "p", "ף": "p", "צ": "C", "ץ": "C", "ק": "q", "ר": "r", "ש": SIBILANT, "ת": "t"}
AR_CLASS = {"ء": "", "أ": "", "إ": "", "آ": "", "ؤ": "", "ئ": "", "ا": "", "ب": "b", "ت": "t", "ث": SIBILANT,
            "ج": "g", "ح": "H", "خ": "H", "د": "d", "ذ": "Z", "ر": "r", "ز": "Z", "س": SIBILANT, "ش": SIBILANT,
            "ص": "C", "ض": "C", "ط": "T", "ظ": "C", "ع": "", "غ": "", "ف": "p", "ق": "q", "ك": "k", "ل": "l",
            "م": "m", "ن": "n", "ه": "", "و": "", "ي": "", "ى": "", "ة": ""}


def heb_skeleton(form):
    out, gem = [], set()
    # a dagesh (doubling) is lost in skeleton_hebrew; read it from the pointed form
    letters = [c for c in unicodedata.normalize("NFD", form) if "א" <= c <= "ת" or c == "ּ"]
    for i, c in enumerate(letters):
        if c == "ּ":
            continue
        cls = HEB_CLASS.get(c, "")
        if not cls:
            continue
        doubled = i + 1 < len(letters) and letters[i + 1] == "ּ" and i > 0 and c not in "בגדכפת" or (
            i + 1 < len(letters) and letters[i + 1] == "ּ" and i > 0)
        out.append(cls)
        if doubled:
            gem.add(len(out) - 1)
    return "".join(out), gem


def ar_skeleton(form, root=""):
    s = unicodedata.normalize("NFD", root or form)
    letters = [c for c in s if "ء" <= c <= "ي"]
    out = "".join(AR_CLASS.get(c, "") for c in letters)
    return re.sub(r"(.)\1", r"\1", out), set()


def variants(sk, gem):
    """A skeleton plus its dissimilated forms: a geminate CC may appear as rC (or nC)."""
    out = {sk}
    for i in gem:
        if 0 <= i < len(sk):
            out.add(sk[:i] + "r" + sk[i:])
            out.add(sk[:i] + "n" + sk[i:])
    # Hebrew and Akkadian geminate written once; a dissimilated r in the other language is optional
    for i, c in enumerate(sk):
        if c in "rn" and 0 < i < len(sk) - 1:
            out.add(sk[:i] + sk[i + 1:])
    return {v for v in out if len(v) >= 2}


VOICE = str.maketrans({"g": "k", "q": "k", "d": "t", "T": "t", "b": "p", "Z": SIBILANT, "C": SIBILANT})


def voiceless(sk):
    return sk.translate(VOICE)


# ---------------------------------------------------------------- meaning

def words(text):
    out = set()
    for w in re.findall(r"[a-z]+", (text or "").lower()):
        if len(w) > 2 and w not in STOP:
            out.add(w[:-1] if w.endswith("s") and len(w) > 3 and not w.endswith("ss") else w)
    return out


def akk_meaning_words(meaning):
    """English meanings in an eBL entry are the quoted words: 'f. "chair, stool, throne" [GU.ZA] ...'."""
    quoted = re.findall(r'"([^"]+)"', meaning or "")
    return words(" ".join(quoted)) if quoted else words(meaning)


# ---------------------------------------------------------------- lexicons with attestations

def scope_files():
    if not SCOPE.exists():
        return []
    return yaml.safe_load(SCOPE.read_text(encoding="utf-8"))["texts"]


def attestations():
    """Lemma -> list of 'siglum section:line' refs, per language, from the texts in scope."""
    import originals
    att = {"sux": defaultdict(list), "akk": defaultdict(list), "uga": defaultdict(list), "egy": defaultdict(list),
           "akk_gloss": {}, "sux_gloss": {}, "uga_gloss": {}}
    for t in scope_files():
        path = RAW / t["file"]
        if not path.exists():
            continue
        d = json.loads(path.read_text(encoding="utf-8"))
        src = d.get("source", "")
        for s in d["sections"]:
            for line in s["lines"]:
                sec, n = originals.norm_loc(s["name"], line["n"])
                ref = f"{t['siglum']} {sec}:{n}" if sec else f"{t['siglum']} {n}"
                for x in line.get("lemmas") or []:
                    lem = x.get("lemma") or ""
                    if not lem:
                        continue
                    lang = x.get("lang") or ""
                    if src == "eBL":
                        key, l = lem, ("sux" if d.get("language") == "sux" else "akk")
                    elif src == "ETCSL" or lang.startswith("sux") or (src.startswith("ORACC epsd2") and not lang):
                        key, l = sux_key(lem), "sux"
                        att["sux_gloss"].setdefault(key, x.get("gloss") or x.get("sense") or "")
                    elif lang.startswith("uga") or src == "EUPT":
                        key, l = lem, "uga"
                        if x.get("gloss") and src != "EUPT":
                            att["uga_gloss"].setdefault(key, x.get("gloss") or "")
                    elif lang.startswith("akk") or (src.startswith("ORACC") and re.search(r"[aeiuāēīū]", lem)
                                                     and "ʿ" not in lem):
                        key, l = lem, "akk"
                        att["akk_gloss"].setdefault(key, x.get("gloss") or "")
                    elif src == "TLA":
                        key, l = lem, "egy"
                    else:
                        continue
                    if len(att[l][key]) < 50:
                        att[l][key].append(ref)
                    else:
                        att[l][key].append(None)
    return att


def sux_key(s):
    """'e2-gal', 'egal', 'E₂.GAL', 'gu-za', 'guza' -> 'egal', 'guza'."""
    s = plain(s).replace("ĝ", "g").replace("ŋ", "g").replace("ḫ", "h").replace("š", "sz")
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[₀-₉0-9]", "", s)
    s = re.sub(r"\{[^}]*\}", "", s)
    return re.sub(r"[^a-z]", "", s.lower())


def akk_id_cf(eid):
    return re.sub(r"\s+[IVX]+$", "", eid)


def load_akkadian(att):
    path = RAW / "ebl-dictionary.json"
    d = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    lex = {}
    cf_index = defaultdict(list)
    for eid, e in d.items():
        cf = e.get("lemma") or akk_id_cf(eid)
        if cf.startswith("-") or cf.endswith("-") or len(cf) < 3:
            continue
        lex[eid] = {"id": eid, "cf": cf, "meaning": e.get("meaning", ""), "logograms": e.get("logograms") or [],
                    "words": akk_meaning_words(e.get("meaning", "")) | words(e.get("guideWord", "")),
                    "refs": list(att["akk"].get(eid, []))}
        cf_index[cf].append(eid)
    # ORACC citation forms join the eBL entry of the same form (first homonym) or stand alone
    for cf, refs in att["akk"].items():
        if cf in lex:
            continue
        ids = cf_index.get(cf)
        if ids:
            lex[ids[0]]["refs"] += refs
        else:
            lex[cf] = {"id": cf, "cf": cf, "meaning": att["akk_gloss"].get(cf, ""), "logograms": [],
                       "words": words(att["akk_gloss"].get(cf, "")), "refs": list(refs)}
    for e in lex.values():
        e["n"] = len(e["refs"])
        e["refs"] = [r for r in e["refs"] if r][:6]
        e["skeleton"], e["gem"] = akk_skeleton(e["cf"])
    return lex


def akk_skeleton(cf):
    """Akkadian citation form -> consonant classes, without the case ending, and its geminates."""
    w = plain_keep(cf)
    w = re.sub(r"(u|um|û|ū|i|a|tu|tum)$", "", w) if len(re.sub(r"[aeiu]", "", w)) > 2 else re.sub(r"(u|um|û|ū)$", "", w)
    sk, gem = latin_geminates(w)
    return sk, gem


# ---------------------------------------------------------------- edges

def hebrew_side():
    heb, ara = corpora.load_hebrew_bible(), corpora.load_hebrew_bible("A")
    occ = Counter(l for v in heb.verses for l in set(v.lemmas))
    aocc = Counter(l for v in ara.verses for l in set(v.lemmas))
    out = {}
    for lang, c, o in (("he", heb, occ), ("arc", ara, aocc)):
        for lid, lem in c.lemmas.items():
            if lem.pos not in corpora.HEBREW_CONTENT_POS or not o.get(lid):
                continue
            key = f"{lang}:{lid}"
            if lang == "arc" and f"he:{lid}" in out:
                continue
            sk, gem = heb_skeleton(lem.form)
            out[key] = {"lang": lang, "id": lid, "form": lem.form, "translit": lem.translit, "gloss": lem.gloss,
                        "words": words(lem.definition), "skeleton": sk, "gem": gem, "n": o[lid]}
    return out


def quran_side():
    q = corpora.load_quran()
    occ = Counter(l for v in q.verses for l in set(v.lemmas))
    out = {}
    for lid, lem in q.lemmas.items():
        if not occ.get(lid):
            continue
        sk, gem = ar_skeleton(lem.form, lem.root)
        out[f"ar:{lid}"] = {"lang": "ar", "id": lid, "form": lem.form, "root": lem.root, "gloss": lem.gloss,
                            "words": set(lem.gloss_words) | words(lem.gloss), "skeleton": sk, "gem": gem, "n": occ[lid]}
    return out


def index(entries):
    idx = defaultdict(list)
    for k, e in entries.items():
        for v in variants(e["skeleton"], e["gem"]):
            idx[v].append(k)
    return idx


def sumerian_loans(akk, att):
    """Akkadian words written with a Sumerian logogram whose Sumerian reading they echo."""
    sux_known = set(att["sux"]) | set(att["sux_gloss"])
    out = []
    for e in akk.values():
        for logo in e["logograms"]:
            for part in re.split(r"[,;]\s*|\s+", logo):
                key = sux_key(part)
                if len(key) < 3:
                    continue
                s_sk = voiceless(latin_skeleton(key.replace("sz", "š")))
                a_sk = voiceless(e["skeleton"])
                if len(s_sk) < 2 or s_sk != a_sk:
                    continue
                out.append({"akk": e["id"], "sux": key, "logogram": part, "attested_sux": key in sux_known,
                            "sux_gloss": att["sux_gloss"].get(key, ""), "sux_refs": [r for r in att["sux"].get(key, []) if r][:4],
                            "sux_n": len(att["sux"].get(key, []))})
    seen, uniq = set(), []
    for x in out:
        if (x["akk"], x["sux"]) not in seen:
            seen.add((x["akk"], x["sux"]))
            uniq.append(x)
    return uniq


def cognate_edges(src, targets, idx, need_meaning=True):
    """Pairs (src key, target key) whose skeletons correspond and whose meanings share a word."""
    out = []
    for k, e in src.items():
        if not e.get("words") and need_meaning:
            continue
        seen = set()
        for v in variants(e["skeleton"], e["gem"]):
            for tk in idx.get(v, []):
                if tk in seen:
                    continue
                seen.add(tk)
                t = targets[tk]
                shared = e["words"] & t["words"]
                if need_meaning and not shared:
                    continue
                out.append({"from": k, "to": tk, "shared": sorted(shared), "skeleton": v,
                            "dissimilation": v != e["skeleton"] or v != t["skeleton"]})
    return out


def run(verbose=True):
    att = attestations()
    akk = load_akkadian(att)
    akk = {k: v for k, v in akk.items() if len(v["skeleton"]) >= 2}
    heb = hebrew_side()
    qur = quran_side()
    heb_idx, qur_idx = index(heb), index(qur)
    # Akkadian in the corpus (attested) or in a Sumerian loan: compare with Hebrew, Aramaic and Arabic
    loans = sumerian_loans(akk, att)
    loan_akk = {x["akk"] for x in loans}
    akk_cmp = {k: v for k, v in akk.items() if v["n"] or k in loan_akk}
    a_h = cognate_edges(akk_cmp, heb, heb_idx)
    a_q = cognate_edges(akk_cmp, qur, qur_idx)
    h_q = cognate_edges({k: v for k, v in heb.items() if v["lang"] == "arc"}, qur, qur_idx)
    h_q += cognate_edges({k: v for k, v in heb.items() if v["lang"] == "he"}, qur, qur_idx)
    # Ugaritic (ORACC lemmas with English glosses)
    uga = {}
    for lem, refs in att["uga"].items():
        g = att["uga_gloss"].get(lem, "")
        sk, gem = latin_geminates(plain_keep(lem))
        if len(sk) >= 2:
            uga[f"uga:{lem}"] = {"lang": "uga", "id": lem, "form": lem, "gloss": g, "words": words(g), "skeleton": sk,
                                 "gem": gem, "n": len(refs), "refs": [r for r in refs if r][:6]}
    u_h = cognate_edges(uga, heb, heb_idx)
    u_q = cognate_edges(uga, qur, qur_idx)

    # chains: Sumerian -> Akkadian -> (Aramaic/Hebrew) -> Arabic, and Akkadian -> Hebrew/Aramaic -> Arabic
    by_from = defaultdict(list)
    for e in a_h + a_q + h_q:
        by_from[e["from"]].append(e)
    chains = []
    sux_of = defaultdict(list)
    for x in loans:
        sux_of[x["akk"]].append(x)
    for ak in akk_cmp:
        nxt = by_from.get(ak, [])
        if not nxt:
            continue
        links, hops = [], []
        aw = akk[ak]["words"]
        for e in nxt:
            links.append(e["to"])
            for e2 in by_from.get(e["to"], []):
                # a second hop must still share a meaning with the Akkadian word
                t = heb.get(e2["to"]) or qur.get(e2["to"])
                if aw & t["words"]:
                    links.append(e2["to"])
                    hops.append(e2)
        links = list(dict.fromkeys(links))
        langs = {k.split(":")[0] for k in links}
        chain = {"akk": ak, "akk_cf": akk[ak]["cf"], "akk_meaning": akk[ak]["meaning"][:200], "akk_n": akk[ak]["n"],
                 "akk_refs": akk[ak]["refs"], "sux": sux_of.get(ak, []), "links": links,
                 "edges": list(nxt) + hops,
                 "langs": sorted(langs | {"akk"} | ({"sux"} if sux_of.get(ak) else set()))}
        chains.append(chain)

    def show(k):
        e = heb.get(k) or qur.get(k)
        return {"key": k, "form": e["form"], "gloss": e["gloss"], "translit": e.get("translit", ""), "n": e["n"]}
    for c in chains:
        c["targets"] = [show(k) for k in c["links"]]
    for c in chains:
        c["langs"] = sorted({k.split(":")[0] for k in c["links"]} | {"akk"} | ({"sux"} if c["sux"] else set()))
        # a loan chain spans a Sumerian source or more than one later language; the rest are cognate pairs
        c["kind"] = "chain" if c["sux"] or len(set(c["langs"]) - {"akk", "sux"}) >= 2 else "cognate"
    chains.sort(key=lambda c: (-len(c["langs"]), -(c["akk_n"] > 0), c["akk_cf"]))
    payload = {"sumerian_loans": loans, "chains": chains,
               "ugaritic": [{**e, "to_form": (heb.get(e["to"]) or qur.get(e["to"]))["form"]} for e in u_h + u_q],
               "counts": {"akkadian_lemmas": len(akk), "akkadian_compared": len(akk_cmp), "sumerian_loans": len(loans),
                          "akk_heb_edges": len(a_h), "akk_ar_edges": len(a_q), "heb_ar_edges": len(h_q),
                          "uga_edges": len(u_h) + len(u_q), "chains": len(chains)}}
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "loan-chains.json").write_text(json.dumps(payload, ensure_ascii=False, indent=1, default=list), encoding="utf-8")
    if verbose:
        print(payload["counts"])
    return payload


def chain_has(payload, forms):
    """True if one chain links every form given: Akkadian cf, Sumerian key, or 'he:H3678' / 'ar:<lemma>' keys."""
    for c in payload["chains"]:
        have = {c["akk_cf"], c["akk"]} | {s["sux"] for s in c["sux"]} | set(c["links"])
        loose = {plain(h) for h in have}       # Akkadian length marks optional: ekallu = ēkallu
        if all(f in have or sux_key(f) in have or plain(f) in loose for f in forms):
            return c
    return None


if __name__ == "__main__":
    p = run()
    for forms in (["guza", "kussû", "arc:H3764", "he:H3678"], ["egal", "ēkallu", "he:H1964"], ["tinūru", "he:H8574"]):
        c = chain_has(p, forms)
        print(forms, "->", bool(c), c and [t["form"] for t in c["targets"]])
