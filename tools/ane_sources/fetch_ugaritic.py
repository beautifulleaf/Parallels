#!/usr/bin/env python3
"""Fetch the Ugaritic poetic corpus from EUPT (Edition des ugaritischen
poetischen Textkorpus, Goettingen) via its SUB TextAPI and normalise it.

Sources
-------
* TextAPI base: https://eupt.uni-goettingen.de/api/eupt/
    collection.json                      -> lists only *published* manifests
    {KTU__1.x}/manifest.json             -> metadata, licence (CC BY-SA 4.0)
    html/KTU_1.x_facsimile.html          -> diplomatic transliteration per tablet line
    html/KTU_1.x_philology.html          -> cola: vocalisation, morphology, lemma ids,
                                            German translation, notes
  The server also serves (unlisted) draft editions of other KTU 1.x tablets;
  they are found by probing html/KTU_1.N_facsimile.html.
* Lemma ids (lemma:d2eNNN) are resolved with the EUPT Ugaritic glossary
  published in the MIT-licensed repo gitlab.gwdg.de/subugoe/eupt/eupt-xml
  (samples/Ugaritisches-Glossar_2026-02-21.xml). The live lexicon used by the
  server is private; ids missing from the public snapshot keep only the id.

Usage:  python3 -I fetch_ugaritic.py OUT_DIR [RAW_DIR]
Stdlib only.
"""
import concurrent.futures as cf
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET

BASE = "https://eupt.uni-goettingen.de/api/eupt"
VIEWER = "https://eupt.uni-goettingen.de/edition.html"
GLOSSARY_URL = ("https://gitlab.gwdg.de/api/v4/projects/29060/repository/files/"
                "samples%2FUgaritisches-Glossar_2026-02-21.xml/raw?ref=master")
GLOSSARY_SRC = ("https://gitlab.gwdg.de/subugoe/eupt/eupt-xml/-/blob/master/"
                "samples/Ugaritisches-Glossar_2026-02-21.xml (MIT)")
PROBE_RANGE = range(1, 201)          # KTU 1.1 .. 1.200
XH = "{http://www.w3.org/1999/xhtml}"
TEI = "{http://www.tei-c.org/ns/1.0}"
XML_ID = "{http://www.w3.org/XML/1998/namespace}id"
UA = {"User-Agent": "Parallels-corpus-fetcher/1.0 (research; stdlib urllib)"}

TITLES = {
    "1.1": "Baal Cycle, tablet 1", "1.2": "Baal Cycle, tablet 2: Baal and Yam",
    "1.3": "Baal Cycle, tablet 3: Baal and Anat", "1.4": "Baal Cycle, tablet 4: Baal's palace",
    "1.5": "Baal Cycle, tablet 5: Baal and Mot", "1.6": "Baal Cycle, tablet 6: Baal and Mot",
    "1.7": "Mythological fragment (Baal/Anat)", "1.9": "Mythological fragment",
    "1.10": "Baal and Anat (Baal and the heifer)", "1.11": "Baal and Anat (fragment)",
    "1.12": "Baal and the Devourers", "1.13": "Hymn to Anat",
    "1.14": "Kirta Epic, tablet 1", "1.15": "Kirta Epic, tablet 2", "1.16": "Kirta Epic, tablet 3",
    "1.17": "Aqhat Epic, tablet 1", "1.18": "Aqhat Epic, tablet 2", "1.19": "Aqhat Epic, tablet 3",
    "1.20": "Rephaim text, tablet 1", "1.21": "Rephaim text, tablet 2", "1.22": "Rephaim text, tablet 3",
    "1.23": "Birth of the Gracious Gods (Shachar and Shalim)", "1.24": "Nikkal and Yarikh",
    "1.100": "Horon and the snakes (snake incantation)", "1.108": "Rapiu hymn",
    "1.114": "El's Marzeah",
}
ROMAN = {"i", "ii", "iii", "iv", "v", "vi", "vii", "viii"}


# ---------------------------------------------------------------- network
def get(url, tries=5, html=False):
    """GET with retries. For HTML, require a complete document (</html>)."""
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=120) as r:
                data = r.read()
            if html and data.strip() and not data.rstrip().endswith(b"</html>"):
                raise IOError("truncated HTML (%d bytes)" % len(data))
            return data
        except (urllib.error.URLError, IOError, OSError) as e:  # noqa: PERF203
            last = e
            time.sleep(2 * (i + 1))
    raise IOError("failed %s: %s" % (url, last))


def cached(url, path, html=False):
    if path and os.path.exists(path) and os.path.getsize(path) > 0:
        data = open(path, "rb").read()
        if not html or not data.strip() or data.rstrip().endswith(b"</html>"):
            return data
    data = get(url, html=html)
    if path:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "wb") as f:
            f.write(data)
    return data


# ---------------------------------------------------------------- helpers
def cls(el):
    return (el.get("class") or "").split()


def strip_html(s):
    if not s:
        return s
    s = re.sub(r"<[^>]+>", " ", s)
    s = s.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
    return re.sub(r"\s+([.,;:)])", r"\1", re.sub(r"\s+", " ", s)).strip()


def _clean(chunk, in_seg, edge=""):
    """Pretty-print newlines: removed at node edges and inside words (seg),
    otherwise (e.g. '[x x\\n   x]') they stand for one space."""
    chunk = re.sub(r"^\n\s*", "" if in_seg else edge, chunk)
    chunk = re.sub(r"\n\s*$", "" if in_seg else edge, chunk)
    return re.sub(r"\n\s*", "" if in_seg else " ", chunk)


def text_of(el, skip=("notes-container", "ling_information"), in_seg=False, edge=""):
    # edge=" ": newlines at node edges separate words (vocalisation); default ""
    # because in the transliteration they are artefacts ('l</span>\n<span>pnh').
    out = []
    seg = in_seg or "seg" in cls(el) or el.tag == XH + "label"
    if el.text:
        out.append(_clean(el.text, seg, edge))
    for ch in el:
        if not any(c in skip for c in cls(ch)):
            out.append(text_of(ch, skip, seg, edge))
        if ch.tail:
            out.append(_clean(ch.tail, seg, edge))
    return "".join(out)


def notes_of(container):
    res = []
    if container is None:
        return res
    for li in container.iter(XH + "li"):
        if "note-item" not in cls(li):
            continue
        typ = ""
        for sp in li.iter(XH + "span"):
            if "noteType" in cls(sp):
                typ = "".join(sp.itertext()).strip()
                break
        body = [c for c in li if c.tag == XH + "span"]
        txt = " ".join(re.sub(r"\s+", " ", "".join(b.itertext())).strip() for b in body)
        if txt:
            res.append({"type": typ, "text": txt} if typ else {"text": txt})
    return res


def find_class(el, name, tag=None):
    for x in el.iter(tag) if tag else el.iter():
        if name in cls(x):
            return x
    return None


# ---------------------------------------------------------------- lexicon
def load_lexicon(raw_dir):
    path = os.path.join(raw_dir, "Ugaritisches-Glossar_2026-02-21.xml") if raw_dir else None
    root = ET.fromstring(cached(GLOSSARY_URL, path))
    lex = {}
    for e in root.iter(TEI + "entry"):
        eid = e.get(XML_ID)
        term = e.find(TEI + "form/" + TEI + "term")
        term = " ".join("".join(term.itertext()).split()) if term is not None else None
        pos = e.find(".//" + TEI + "gramGrp/" + TEI + "pos")
        glosses = []
        for s in e.findall(TEI + "sense"):
            for d in s.findall(TEI + "div"):
                if d.get("type") == "translation":
                    g = " ".join("".join(d.itertext()).split())
                    if g and g not in glosses:
                        glosses.append(g)
        ent = {"lemma": term, "pos": pos.get("norm") if pos is not None else None,
               "gloss": "; ".join(glosses) or None}
        lex[eid] = ent
        # newer files point at senses (e.g. lemma:mlk-II-1) instead of entries
        for s in e.findall(TEI + "sense"):
            sid = s.get(XML_ID)
            if not sid:
                continue
            g = [" ".join("".join(d.itertext()).split()) for d in s.findall(TEI + "div")
                 if d.get("type") == "translation"]
            lex[sid] = dict(ent, gloss="; ".join(x for x in g if x) or ent["gloss"])
    return lex


# ---------------------------------------------------------------- parsing
def section_from_part(pid, ktu):
    for pre in ("line_%s_" % ktu, "line_%s_" % ktu.replace(".", "_")):
        if pid.startswith(pre):
            rest = pid[len(pre):].rsplit("_", 2)
            if len(rest) == 3:
                return rest[0]
    return None


def norm_n(label, section):
    lab = label.strip()
    m = re.match(r"^(\(?)([ivx]+)\s+(.+?)(\)?)$", lab)
    if m and section and m.group(2).upper() == section and m.group(2) in ROMAN:
        inner = m.group(3)
        return "(%s)" % inner if m.group(1) and m.group(4) else inner
    return lab


def parse_facsimile(html, ktu):
    root = ET.fromstring(html)
    sections, seg2line, part2line = {}, {}, {}
    order = []
    for col in root.iter(XH + "div"):
        if "column" not in cls(col):
            continue
        cur = None
        col_notes = []
        if col.text and col.text.strip():
            col_notes.append(" ".join(col.text.split()))
        for lc in col:
            if lc.tail and lc.tail.strip():
                col_notes.append(" ".join(lc.tail.split()))
            if "line-container" not in cls(lc):
                continue
            line = find_class(lc, "line", XH + "div")
            if line is None:
                continue
            nr = find_class(line, "line-nr", XH + "span")
            body = find_class(line, "line-body", XH + "span")
            label = "".join(nr.itertext()).strip() if nr is not None else ""
            parts = [p.get("id") for p in body.iter(XH + "span") if "part" in cls(p)] if body is not None else []
            sec = None
            for p in parts:
                sec = section_from_part(p, ktu)
                if sec:
                    break
            if not sec:
                m = re.match(r"^\(?([ivx]+)\s", label)
                sec = m.group(1).upper() if m else (cur or "I")
            cur = sec
            if sec not in sections:
                sections[sec] = {"name": sec, "lines": []}
                order.append(sec)
            if col_notes:
                sections[sec].setdefault("notes", []).extend(col_notes)
                col_notes = []
            text = text_of(body).strip() if body is not None else ""
            ln = {"n": norm_n(label, sec), "text": text}
            if ln["n"] != label:
                ln["label"] = label
            nts = notes_of(find_class(lc, "notes-container", XH + "div"))
            if nts:
                ln["notes"] = nts
            idx = (sec, len(sections[sec]["lines"]))
            sections[sec]["lines"].append(ln)
            for p in parts:
                part2line[p] = idx
            if body is not None:
                for s in body.iter(XH + "span"):
                    if "seg" in cls(s) and s.get("id"):
                        seg2line[s.get("id")] = idx
        if col_notes and cur:
            sections[cur].setdefault("notes", []).extend(col_notes)
    return [sections[s] for s in order], seg2line, part2line


def parse_philology(html, lex):
    root = ET.fromstring(html)
    cola = []
    for unit in root.iter(XH + "div"):
        if "unit" not in cls(unit):
            continue
        voc = find_class(unit, "vocalisation-text", XH + "div")
        tr = find_class(unit, "translation", XH + "div")
        words = []
        if voc is not None:
            for wc in voc.iter(XH + "span"):
                if "word_container" not in cls(wc):
                    continue
                w = next((x for x in wc if "w" in cls(x)), None)
                if w is None:
                    continue
                lab = w.find(XH + "label")
                form = text_of(lab if lab is not None else w).strip()
                morph = lem = None
                li = next((x for x in wc if "ling_information" in cls(x)), None)
                if li is not None:
                    for x in li:
                        if "morph" in cls(x):
                            morph = " ".join("".join(x.itertext()).split()) or None
                        if "lem" in cls(x):
                            lem = "".join(x.itertext()).strip() or None
                wd = {"form": form}
                lids = [x.split(":", 1)[-1] for x in lem.split()] if lem else []
                if lids:
                    es = [lex[i] for i in lids if i in lex]
                    if es:
                        wd["lemma"] = " + ".join(e["lemma"] or "?" for e in es)
                        gl = [e["gloss"] for e in es if e["gloss"]]
                        if gl:
                            wd["gloss"] = " + ".join(gl)
                        ps = [e["pos"] for e in es if e["pos"]]
                        if ps:
                            wd["pos"] = " + ".join(ps)
                    wd["lemma_id"] = " ".join(lids)
                if morph:
                    wd["morph"] = morph
                segs = (w.get("data-corresp") or "").split()
                words.append((wd, segs))
        notes = notes_of(next((x for x in unit if "notes-container" in cls(x)), None))
        colon = {
            "id": unit.get("id"),
            "parts": (unit.get("data-corresp") or "").split(),
            "vocalised": re.sub(r"\s+", " ", text_of(voc, skip=("ling_information", "lb"), edge=" ")).strip() if voc is not None else "",
            "translation": re.sub(r"\s+", " ", text_of(tr)).strip() if tr is not None else "",
            "words": words,
        }
        if notes:
            colon["notes"] = notes
        cola.append(colon)
    return cola


def build(ktu, fac_html, phil_html, manifest, lex, published):
    sections, seg2line, part2line = parse_facsimile(fac_html, ktu)
    cola = parse_philology(phil_html, lex) if phil_html and b"<div" in phil_html else []
    line_units = {}
    out_cola = []
    for i, c in enumerate(cola):
        lines = []
        for p in c["parts"]:
            if p in part2line and part2line[p] not in lines:
                lines.append(part2line[p])
        for li in lines:
            line_units.setdefault(li, []).append(i)
        c["_lines"] = lines
        for wd, segs in c["words"]:
            tgt = next((seg2line[s] for s in segs if s in seg2line), lines[0] if lines else None)
            if tgt is not None:
                sec, k = tgt
                ln = next(s for s in sections if s["name"] == sec)["lines"][k]
                ln.setdefault("lemmas", []).append(wd)
        oc = {"id": c["id"], "section": lines[0][0] if lines else None,
              "lines": [next(s for s in sections if s["name"] == a)["lines"][b]["n"] for a, b in lines],
              "vocalised": c["vocalised"]}
        if c["translation"]:
            oc["translation"] = c["translation"]
        if c.get("notes"):
            oc["notes"] = c["notes"]
        out_cola.append(oc)
    # line translation only where the line is covered exactly by whole cola
    for (sec, k), units in line_units.items():
        if all(cola[u]["_lines"] == [(sec, k)] for u in units):
            tr = " ".join(cola[u]["translation"] for u in units if cola[u]["translation"])
            if tr:
                next(s for s in sections if s["name"] == sec)["lines"][k]["translation"] = tr
    meta = {m["key"]: m.get("value") for m in manifest.get("metadata", [])}
    lic = manifest.get("license") or [{}]
    rec = {
        "siglum": "KTU " + ktu,
        "title": TITLES.get(ktu, "KTU " + ktu),
        "language": "uga",
        "source": "EUPT",
        "edition": strip_html(meta.get("Zitationshinweis")),
        "license": lic[0].get("id", "CC-BY-SA-4.0"),
        "url": "%s/KTU__%s/manifest.json" % (BASE, ktu),
        "viewer": VIEWER,
        "status": "published" if published else "draft (served by API but not listed in collection.json)",
        "genre": strip_html(meta.get("Genre")),
        "translation_language": "de",
        "transliteration_source": "%s/html/KTU_%s_facsimile.html" % (BASE, ktu),
        "philology_source": "%s/html/KTU_%s_philology.html" % (BASE, ktu),
        "lemma_source": GLOSSARY_SRC,
        "sections": sections,
        "cola": out_cola,
    }
    return rec


# ---------------------------------------------------------------- driver
def fetch(out_dir, raw_dir=None, probe=PROBE_RANGE, workers=6):
    os.makedirs(out_dir, exist_ok=True)
    raw = lambda name: os.path.join(raw_dir, name) if raw_dir else None  # noqa: E731
    coll = json.loads(cached(BASE + "/collection.json", raw("collection.json")))
    published = {s["label"].replace("KTU ", "") for s in coll.get("sequence", [])}
    lex = load_lexicon(raw_dir)

    def try_fac(n):
        k = "1.%d" % n
        d = cached("%s/html/KTU_%s_facsimile.html" % (BASE, k), raw("KTU_%s_facsimile.html" % k), html=True)
        return k, d

    found = {}
    with cf.ThreadPoolExecutor(workers) as ex:
        for k, d in ex.map(try_fac, probe):
            if d and re.search(rb'class="line"', d):
                found[k] = d
    for k in published:
        if k not in found:
            found[k] = cached("%s/html/KTU_%s_facsimile.html" % (BASE, k), raw("KTU_%s_facsimile.html" % k), html=True)
    summary = []
    for k in sorted(found, key=lambda s: tuple(int(x) for x in s.split("."))):
        phil = cached("%s/html/KTU_%s_philology.html" % (BASE, k), raw("KTU_%s_philology.html" % k), html=True)
        man = json.loads(cached("%s/KTU__%s/manifest.json" % (BASE, k), raw("KTU_%s_manifest.json" % k)))
        rec = build(k, found[k], phil, man, lex, k in published)
        fn = os.path.join(out_dir, "KTU_%s.json" % k)
        with open(fn, "w", encoding="utf-8") as f:
            json.dump(rec, f, ensure_ascii=False, indent=1)
        nl = sum(len(s["lines"]) for s in rec["sections"])
        nlem = sum(len(l.get("lemmas", [])) for s in rec["sections"] for l in s["lines"])
        nres = sum(1 for s in rec["sections"] for l in s["lines"] for w in l.get("lemmas", []) if "lemma" in w)
        ntr = sum(1 for s in rec["sections"] for l in s["lines"] if "translation" in l)
        summary.append({"siglum": rec["siglum"], "status": rec["status"].split(" ")[0],
                        "sections": [s["name"] for s in rec["sections"]], "lines": nl,
                        "cola": len(rec["cola"]), "cola_translated": sum(1 for c in rec["cola"] if c.get("translation")),
                        "lines_with_translation": ntr, "words": nlem, "lemmas_resolved": nres})
    with open(os.path.join(out_dir, "_summary.json"), "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=1)
    return summary


if __name__ == "__main__":
    s = fetch(sys.argv[1] if len(sys.argv) > 1 else "out", sys.argv[2] if len(sys.argv) > 2 else None)
    for r in s:
        print(json.dumps(r, ensure_ascii=False))
