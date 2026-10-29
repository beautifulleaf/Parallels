#!/usr/bin/env python3
"""Fetch Egyptian literary/religious texts from the Thesaurus Linguae Aegyptiae (TLA) raw data.

Source
------
The live TLA web app (thesaurus-linguae-aegyptiae.de / tla.digital) is behind a bot-verification
gate, and the Hugging Face TLA datasets are shuffled single sentences without text ids (their
README states they are "not suitable for reconstructing entire ancient source texts").
The only openly downloadable full-text dump with text structure is the BBAW raw-data release:

  "Teilauszug der Datenbank des Vorhabens 'Strukturen und Transformationen des Wortschatzes der
   aegyptischen Sprache' vom Januar 2018", ed. T. S. Richter & I. Hafemann (BBAW / SAW Leipzig),
   urn:nbn:de:kobv:b4-opus4-29190, CC BY-SA 4.0
   https://edoc.bbaw.de/files/2919/corpus.zip      (BTS JSON: text objects + texts)
   https://edoc.bbaw.de/files/2919/vocabulary.zip  (BTS JSON: lemma list aaew_wlist.json)

Text membership / order
-----------------------
Each BTSText document has a stable TLA id (same ids as on the TLA website: /text/<id>) and a
"partOf" relation to its parent object; following partOf gives the object path (corpus /
genre / work / manuscript / text).  textContent.textItems is the ordered list of sentences
(BTSSenctence, each with a stable TLA sentence id); within a sentence, sentenceItems is the
ordered list of words (BTSWord: wChar = transliteration, lKey = lemma id, translation = gloss)
and markers (BTSMarker type 'lc' = line/column count of the manuscript, 'para' = conventional
counting).  A line's "n" is the manuscript line (lc) in force where the sentence starts; if
several sentences start in the same line they get "/2", "/3", ...

Usage:  python3 -I fetch_egyptian.py OUT_DIR [CACHE_DIR]
Stdlib only.
"""
import json
import os
import re
import ssl
import sys
import time
import urllib.error
import urllib.request
import zipfile

CORPUS_URL = "https://edoc.bbaw.de/files/2919/corpus.zip"
VOCAB_URL = "https://edoc.bbaw.de/files/2919/vocabulary.zip"
EDITION = ("TLA raw data: 'Teilauszug der Datenbank des Vorhabens \"Strukturen und Transformationen "
           "des Wortschatzes der aegyptischen Sprache\" vom Januar 2018', ed. T. S. Richter & "
           "I. Hafemann (BBAW) and H.-W. Fischer-Elfert & P. Dils (SAW Leipzig), 2018, "
           "urn:nbn:de:kobv:b4-opus4-29190")
LICENSE = "CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)"
TLA_TEXT_URL = "https://thesaurus-linguae-aegyptiae.de/text/{}"
CA_DEFAULT = "/root/.ccr/ca-bundle.crt"

# ---------------------------------------------------------------------------------------------
# Selection.  Each work: corpus file in corpus.zip, regex over the object path of BTSText docs,
# optional exclude regex, and the TLA ids of the witnesses to put first (main witness first).
# All matching texts with >= 1 sentence become sections (one per manuscript witness).
# ---------------------------------------------------------------------------------------------
SAWLIT = "aaew_corpus_sawlit.json"
PT = "aaew_corpus_bbawpyramidentexte.json"
WORKS = [
    dict(siglum="Amenemope", title="Instruction of Amenemope", corpus=SAWLIT,
         include=r"〈Die Lehre des Amenemope〉", first=["5JO44VJZERAB3HQUHMFSMNXH6I"]),
    dict(siglum="TwoBrothers", title="Tale of Two Brothers (pD'Orbiney)", corpus=SAWLIT,
         include=r"〈Das Zweibrüdermärchen〉", exclude=r"Verwaltungstext"),
    dict(siglum="Sinuhe", title="Story of Sinuhe", corpus=SAWLIT,
         include=r"〈Die Geschichte des Sinuhe〉",
         first=["JIPPXMXOTNCQDIKJIQVYWMKOWU", "QZCOZWR7YVAGNLPTMZIMHL6TYQ"]),
    dict(siglum="AtenHymn", title="Great Hymn to the Aten (Amarna, tomb of Ay)",
         corpus="aaew_corpus_bbawamarna.json",
         include=r"Nr\. 25: Eje / Eingang / Westwand / Großer Sonnenhymnus / Hymnus$"),
    dict(siglum="BD125", title="Book of the Dead, chapter 125", corpus="aaew_corpus_tb.json",
         include=r"/ (V )?Tb 125\b",
         first=["FGGZPRDYGBHV3AFOH5EXBPKDQY", "ZJ45MN6I2BEBXIOF4E2OH4PK64", "S4KP2OGKXFCPPK7Q5MHFEE6R7A"]),
    dict(siglum="ShipwreckedSailor", title="Tale of the Shipwrecked Sailor", corpus=SAWLIT,
         include=r"〈Die Geschichte des Schiffbrüchigen〉"),
    dict(siglum="EloquentPeasant", title="Tale of the Eloquent Peasant", corpus=SAWLIT,
         include=r"〈Der beredte Bauer〉",
         first=["2NTZNJ65V5FZBCZ3BM55HZEQDQ", "PVLMEE7Y45FPXBSMF47T6PNPEE", "TTH5MM5DPRBI5MM2U5M5YT3RME"]),
    dict(siglum="Ipuwer", title="Admonitions of Ipuwer (pLeiden I 344 recto)", corpus=SAWLIT,
         include=r"〈Der Dialog von Ipuwer mit dem Allherrn"),
    dict(siglum="ManAndBa", title="Dispute of a Man with his Ba (Lebensmüder)", corpus=SAWLIT,
         include=r"〈Der Lebensmüde〉"),
    dict(siglum="Ptahhotep", title="Instruction of Ptahhotep", corpus=SAWLIT,
         include=r"〈Die Lehre des Ptahhotep〉", exclude=r"Hymnus auf Theben",
         first=["DKAFDVSXYFADJDS3Z3AOISAP4U", "3W45TQYQ3RCX5DXZ7DIZ43JWNQ", "KETLFI2GYFFA5BT77EZJJRIEGQ"]),
    dict(siglum="Merikare", title="Instruction for Merikare", corpus=SAWLIT,
         include=r"〈Die Lehre für Merikare〉", first=["YZSISQLOINELTMJDPXQ45O5IUU"]),
    dict(siglum="NileHymn", title="Hymn to the Nile/Hapi (Great Nile Hymn)", corpus=SAWLIT,
         include=r"〈Der große Nilhymnus〉", first=["PMARXRST45A6PL4SDWQ7URKABI"]),
    dict(siglum="HarpersSongs", title="Harper's Songs", corpus=SAWLIT,
         include=r"〈Harfnerlieder〉", exclude=r"/ Rahmentext$",
         first=["CRNQNNDNPNBYNNLJCWIBBH3PNY"]),
    dict(siglum="HeavenlyCow", title="Book of the Heavenly Cow (Destruction of Mankind)", corpus=SAWLIT,
         include=r"〈Das Buch von der Himmelskuh", first=["WHEOIX5P5ZAVVFU4BGO6OWASV4"]),
    dict(siglum="HorusSeth", title="Contendings of Horus and Seth (pChester Beatty I)", corpus=SAWLIT,
         include=r"〈Der Streit zwischen Horus und Seth〉"),
    dict(siglum="DoomedPrince", title="Tale of the Doomed Prince (pHarris 500 verso)", corpus=SAWLIT,
         include=r"Das Prinzenmärchen"),
    dict(siglum="TruthFalsehood", title="Blinding of Truth by Falsehood (pChester Beatty II)", corpus=SAWLIT,
         include=r"〈Wahrheit und Lüge〉", exclude=r"Verwaltungstext"),
    dict(siglum="Neferti", title="Prophecy of Neferti", corpus=SAWLIT,
         include=r"〈Die Prophezeiungen des Neferti〉"),
    dict(siglum="Westcar", title="Khufu and the Magicians (pWestcar)", corpus=SAWLIT,
         include=r"〈Die Erzählungen des Papyrus Westcar〉"),
    # Pyramid Texts: principled selection (Cannibal Hymn; Atum creation spells; Unas Re/Osiris
    # spells; ascension spells), every pyramid witness present in the dump.
    dict(siglum="PT273-274", title="Pyramid Texts 273-274 (Cannibal Hymn)", corpus=PT,
         include=r"/ PT 273 \+ PT 274$", first=["BRJCKLT7KNED5EKQX5DWGX3T4A"]),
    dict(siglum="PT527", title="Pyramid Text 527 (Atum's creation of Shu and Tefnut)", corpus=PT,
         include=r"/ PT 527$"),
    dict(siglum="PT600", title="Pyramid Text 600 (Atum-Khepri; Shu and Tefnut; protection of the pyramid)",
         corpus=PT, include=r"/ PT 600$"),
    dict(siglum="PT213", title="Pyramid Text 213 (Unas: 'you have not gone dead')", corpus=PT,
         include=r"/ PT 213$", first=["TF2LOMXASJFZLLVT7N4FRIOTUM"]),
    dict(siglum="PT217", title="Pyramid Text 217 (Unas to Re-Atum)", corpus=PT,
         include=r"/ PT 217$", first=["FZQ6IM7ENFHHROXB2W6PTYMXNE"]),
    dict(siglum="PT219", title="Pyramid Text 219 (Osiris litany)", corpus=PT,
         include=r"/ PT 219$", first=["LL7OMQELWZDY7KOZ2UUBVSSVH4"]),
    dict(siglum="PT302", title="Pyramid Text 302 (ascension)", corpus=PT,
         include=r"/ PT 302$", first=["ZI3U3TNFEFBY7D4NUGT6WMGU7E"]),
    dict(siglum="PT306", title="Pyramid Text 306 (ascension by the ladder)", corpus=PT,
         include=r"/ PT 306$", first=["3OKMEWIUAND2XAHSACCABANLZI"]),
]

# Requested but absent from the 2018 dump (checked by path/name search).
NOT_IN_DUMP = [
    "Leiden hymns to Amun (pLeiden I 350)", "Memphite Theology (Shabaka stone)",
    "Setne/Khamwas (Demotic; no Demotic corpus in the 2018 dump)",
    "Coffin Texts (CT 75-80, CT 1130; no Coffin Texts corpus in the 2018 dump)",
]


# ---------------------------------------------------------------------------------------------
def _ssl_ctx():
    ca = os.environ.get("SSL_CERT_FILE") or (CA_DEFAULT if os.path.exists(CA_DEFAULT) else None)
    return ssl.create_default_context(cafile=ca) if ca else ssl.create_default_context()


def download(url, dest, tries=6):
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        return dest
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    ctx, delay = _ssl_ctx(), 5
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Parallels-research-fetcher/1.0"})
            with urllib.request.urlopen(req, context=ctx, timeout=300) as r, open(dest + ".part", "wb") as f:
                while True:
                    b = r.read(1 << 20)
                    if not b:
                        break
                    f.write(b)
            os.replace(dest + ".part", dest)
            return dest
        except (urllib.error.URLError, OSError) as e:
            code = getattr(e, "code", None)
            if code is not None and code not in (429, 500, 502, 503, 504):
                raise
            print(f"  download {url} failed ({e}); retry in {delay}s", file=sys.stderr)
            time.sleep(delay)
            delay *= 2
    raise RuntimeError(f"could not download {url}")


def load_member(zpath, name):
    with zipfile.ZipFile(zpath) as z, z.open(name) as f:
        return json.load(f)


def _tr(obj, lang="de"):
    if not isinstance(obj, dict):
        return None
    for t in obj.get("translations") or []:
        if t.get("lang") == lang and t.get("value"):
            return t["value"].strip()
    return None


def _flat_passport(node, pre=""):
    out = []
    for c in (node or {}).get("children") or []:
        p = pre + "/" + str(c.get("type"))
        if c.get("value"):
            out.append((p, c["value"]))
        out += _flat_passport(c, p)
    return out


def build_lemma_index(wlist):
    idx = {}
    for x in wlist:
        idx[x["_id"]] = dict(name=x.get("name"), type=x.get("type"), subtype=x.get("subtype"),
                             en=_tr(x.get("translations"), "en"), de=_tr(x.get("translations"), "de"))
    return idx


def object_path(doc, by_id):
    parts, seen, x = [], set(), doc
    while x is not None:
        parts.append(x.get("name", "?"))
        pid = next((r.get("objectId") for r in x.get("relations") or [] if r.get("type") == "partOf"), None)
        if not pid or pid in seen:
            break
        seen.add(pid)
        x = by_id.get(pid)
    return " / ".join(reversed(parts))


def _lc_name(m):
    t = m.get("type") or ""
    if t == "lc":
        v = m.get("name") or ""
    elif t.startswith("lc:"):
        v = t[3:]
    else:
        return None
    v = v.strip().strip("[]").strip()
    return v or None


def _words(items):
    """Yield (kind, item, ambiguous) in order, expanding BTSAmbivalence to its first case."""
    for it in items or []:
        ec = (it.get("eClass") or "").rsplit("//", 1)[-1]
        if ec == "BTSAmbivalence":
            cases = it.get("cases") or []
            for w in (cases[0].get("scenario") if cases else []) or []:
                wec = (w.get("eClass") or "").rsplit("//", 1)[-1]
                yield ("word" if wec == "BTSWord" else "marker", w, True)
        elif ec == "BTSWord":
            yield ("word", it, False)
        else:
            yield ("marker", it, False)


def convert_text(doc, lemmas):
    lines, cur_lc, start_counts = [], None, {}
    for s in (doc.get("textContent") or {}).get("textItems") or []:
        toks, lcs, started, start_lc, paras = [], [], False, None, []
        for kind, it, amb in _words(s.get("sentenceItems")):
            if kind == "marker":
                lc = _lc_name(it)
                if lc:
                    cur_lc = lc
                    lcs.append(lc)
                elif it.get("type") == "para" and it.get("name"):
                    paras.append(it["name"].strip())
                continue
            if not started:
                started, start_lc = True, cur_lc
            lk = it.get("lKey")
            lem = lemmas.get(lk) if lk else None
            tok = {"form": it.get("wChar"),
                   "lemma": lem["name"] if lem else None,
                   "gloss": _tr(it.get("translation"), "de"),
                   "pos": (lem["type"] if lem else None),
                   "lemma_id": lk,
                   "flex": it.get("flexCode")}
            if lem and lem.get("subtype"):
                tok["pos_detail"] = lem["subtype"]
            if lem and lem.get("en"):
                tok["lemma_gloss_en"] = lem["en"]
            if amb:
                tok["ambiguous"] = True
            toks.append(tok)
        if not started:
            start_lc = cur_lc if cur_lc is not None else (lcs[0] if lcs else None)
        base = start_lc if start_lc is not None else "0"
        k = start_counts.get(base, 0) + 1
        start_counts[base] = k
        rec = {"n": base if k == 1 else f"{base}/{k}", "id": s.get("_id"),
               "text": " ".join(t["form"] for t in toks if t["form"]),
               "lemmas": toks, "translation": _tr(s.get("translation"), "de")}
        en = _tr(s.get("translation"), "en")
        if en:
            rec["translation_en"] = en
            if not rec["translation"]:  # e.g. Ipuwer: TLA 2018 has only English translations
                rec["translation"], rec["translation_lang"] = en, "en"
        end_lc = cur_lc
        if start_lc is not None and end_lc is not None and end_lc != start_lc:
            rec["line_end"] = end_lc
        if paras:
            rec["para"] = paras
        lines.append(rec)
    return lines


def fetch(out_dir, cache_dir=None):
    out_dir = os.path.abspath(out_dir)
    cache_dir = os.path.abspath(cache_dir or os.path.join(os.path.dirname(out_dir), "dl", "edoc2919"))
    os.makedirs(out_dir, exist_ok=True)
    cz = download(CORPUS_URL, os.path.join(cache_dir, "corpus.zip"))
    vz = download(VOCAB_URL, os.path.join(cache_dir, "vocabulary.zip"))
    lemmas = build_lemma_index(load_member(vz, "aaew_wlist.json"))

    summary, by_corpus = [], {}
    for w in WORKS:
        by_corpus.setdefault(w["corpus"], []).append(w)
    for corpus, works in by_corpus.items():
        docs = load_member(cz, corpus)
        by_id = {d["_id"]: d for d in docs}
        # BTS uses U+2329/U+232A angle brackets; normalise to U+3008/U+3009 for matching
        _br = str.maketrans("\u2329\u232a", "\u3008\u3009")
        texts = [(d, object_path(d, by_id)) for d in docs if d.get("textContent")]
        texts = [(d, p, p.translate(_br)) for d, p in texts]
        for w in works:
            inc = re.compile(w["include"])
            exc = re.compile(w["exclude"]) if w.get("exclude") else None
            sel = [(d, p) for d, p, q in texts if inc.search(q) and not (exc and exc.search(q))
                   and (d["textContent"].get("textItems") or [])]
            first = w.get("first", [])
            sel.sort(key=lambda dp: (first.index(dp[0]["_id"]) if dp[0]["_id"] in first else len(first), dp[1]))
            sections, nsent = [], 0
            for d, p in sel:
                pp = dict(_flat_passport(d.get("passport")))
                lines = convert_text(d, lemmas)
                nsent += len(lines)
                short = " / ".join(x for x in p.split(" / ")[-3:])
                sections.append({
                    "name": short, "tla_text_id": d["_id"], "tla_text_name": d.get("name"),
                    "witness": pp.get("/text/textual_metadata/egyTextName") or short,
                    "path": p, "url": TLA_TEXT_URL.format(d["_id"]),
                    "bibliography": pp.get("/bibliography/bibliographical_text_field"),
                    "protocol": pp.get("/definition/main_group/protocol"),
                    "line_count_note": pp.get("/definition/main_group/line_count"),
                    "revision_state": d.get("revisionState"),
                    "lines": lines})
            rec = {"siglum": w["siglum"], "title": w["title"], "language": "egy", "source": "TLA",
                   "edition": EDITION, "license": LICENSE,
                   "url": sections[0]["url"] if sections else None,
                   "source_files": [CORPUS_URL + "#" + corpus, VOCAB_URL + "#aaew_wlist.json"],
                   "note": ("One section per manuscript witness (TLA text); first section = main witness. "
                            "'n' = manuscript line/column (TLA 'lc' marker) where the sentence starts, "
                            "'/k' for the k-th sentence starting in that line; 'id' = TLA sentence id. "
                            "Transliteration and glosses as in the 2018 BTS export (German glosses)."),
                   "sections": sections}
            with open(os.path.join(out_dir, w["siglum"] + ".json"), "w", encoding="utf-8") as f:
                json.dump(rec, f, ensure_ascii=False, indent=1)
            summary.append((w["siglum"], len(sections), nsent,
                            [(s["tla_text_id"], len(s["lines"]), s["witness"]) for s in sections]))
        del docs, by_id, texts
    with open(os.path.join(out_dir, "_summary.json"), "w", encoding="utf-8") as f:
        json.dump({"works": [{"siglum": s, "sections": n, "sentences": m,
                              "witnesses": [{"id": a, "sentences": b, "witness": c} for a, b, c in ws]}
                             for s, n, m, ws in summary],
                   "not_in_source": NOT_IN_DUMP, "edition": EDITION, "license": LICENSE},
                  f, ensure_ascii=False, indent=1)
    return summary


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("usage: fetch_egyptian.py OUT_DIR [CACHE_DIR]")
    for s, n, m, ws in fetch(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None):
        print(f"{s:18s} witnesses={n:3d} sentences={m:5d}  main={ws[0][2] if ws else '-'}")
