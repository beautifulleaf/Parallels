"""Download the ancient Near Eastern corpora into data/raw/ane/ (not committed).

Usage: python3 tools/anefetch.py [source ...]      # sources: ebl etcsl oracc ugaritic egyptian hittite nws; default all

Every text is normalized to one JSON file, data/raw/ane/<source>/<file>.json:

  {"siglum": "Gilg SB", "title": ..., "language": "akk", "source": "eBL", "edition": ..., "license": ..., "url": ...,
   "sections": [{"name": "XI", "lines": [{"n": "11", "text": "<original>", "lemmas": [...], "translation": ...}]}]}

`text` is the original: a normalized reconstruction (eBL), a transliteration
(ETCSL, ORACC, Ugaritic, Hittite, Egyptian) or the inscription as edited. A
line's `lemmas` are {form, lemma, gloss, pos} where the edition has them.
Translations are reading aids. data/raw/ane/index.json lists every text.

Sources and terms are in data/ane/SCOPE.md. Raw downloads stay out of git:
several editions do not allow redistribution, and all are re-fetchable.

ORACC's server omits an intermediate certificate, so ORACC requests use the
system bundle plus data/certs/incommon-rsa-server-ca2.pem. TLS verification
is never disabled.
"""
import html
import json
import os
import pathlib
import re
import ssl
import sys
import time
import urllib.parse
import urllib.request
import zipfile
from concurrent.futures import ThreadPoolExecutor

ROOT = pathlib.Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw" / "ane"
SYSTEM_BUNDLE = os.environ.get("SSL_CERT_FILE") or "/root/.ccr/ca-bundle.crt"

EBL = "https://www.ebl.lmu.de/api"
ETCSL = "https://etcsl.orinst.ox.ac.uk"
ORACC_JSON = "https://build-oracc.museum.upenn.edu/json/{}.zip"


def ssl_context(oracc=False):
    ctx = ssl.create_default_context(cafile=SYSTEM_BUNDLE if pathlib.Path(SYSTEM_BUNDLE).exists() else None)
    if oracc:
        ctx.load_verify_locations(cafile=str(ROOT / "data" / "certs" / "incommon-rsa-server-ca2.pem"))
    return ctx


def get(url, retries=5, oracc=False, timeout=300):
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "parallels-pipeline"})
            with urllib.request.urlopen(req, timeout=timeout, context=ssl_context(oracc)) as r:
                return r.read()
        except Exception as e:
            if attempt == retries - 1 or getattr(e, "code", 0) == 404:
                raise
            time.sleep(2 ** (attempt + 1))


def write(source, name, doc):
    path = RAW / source / f"{name}.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(doc, ensure_ascii=False, indent=0), encoding="utf-8")
    return path


def clean_name(s):
    """Section names become single tokens: 'Schøyen₁' -> 'Schøyen1', 'VA+BM' stays."""
    s = s.translate(str.maketrans("₀₁₂₃₄₅₆₇₈₉", "0123456789"))
    return re.sub(r"\s+", "_", s.strip()) or "main"


def unique_n(lines):
    """Line numbers must be unique within a section: repeats get a, b, ... suffixes."""
    seen = {}
    for line in lines:
        n = line["n"]
        if n in seen:
            seen[n] += 1
            line["n"] = f"{n}{'abcdefghijklmnopqrstuvwxyz'[min(seen[n] - 1, 25)]}"
        else:
            seen[n] = 0
    return lines


# ---------------------------------------------------------------- eBL

# readable sigla for the eBL corpus: (genre, category, index) -> abbreviation; stage codes follow
EBL_SIGLA = {
    ("L", 0, 0): "CatAuth", ("L", 1, 1): "Atr", ("L", 1, 2): "Ee", ("L", 1, 3): "ElevBab", ("L", 1, 4): "Gilg",
    ("L", 1, 5): "Erra", ("L", 1, 6): "NergEresh", ("L", 1, 7): "Adapa", ("L", 1, 8): "IshDesc", ("L", 1, 9): "Etana",
    ("L", 1, 10): "Anzu", ("L", 1, 11): "PoorMan", ("L", 1, 12): "NaramSin", ("L", 2, 1): "Theod",
    ("L", 2, 2): "Ludlul", ("L", 2, 3): "CounsWis", ("L", 2, 4): "DialPess", ("L", 2, 5): "AdvPrince",
    ("L", 2, 6): "ShupeAm", ("L", 2, 7): "Aluzinnu", ("L", 2, 8): "Poplar", ("L", 2, 9): "OxHorse",
    ("L", 2, 10): "Fox", ("L", 2, 11): "Spider", ("L", 2, 12): "PalmVine", ("L", 2, 13): "Wren",
    ("L", 3, 1): "PrMarduk1", ("L", 3, 2): "PrMarduk2", ("L", 3, 3): "MardDemons", ("L", 3, 4): "ShamashHymn",
    ("L", 3, 5): "NabuPr", ("L", 3, 6): "QueenNippur", ("L", 3, 7): "GulaHymn", ("L", 3, 8): "IshtarSyncr",
    ("L", 3, 9): "Ishtar2", ("L", 3, 10): "NinurtaSavior", ("L", 3, 11): "MardSyncr", ("L", 3, 12): "GulaSyncr",
    ("L", 3, 13): "NinurtaMacr", ("L", 4, 1): "Angim", ("Mag", 1, 1): "Maqlu", ("Mag", 3, 10): "Sagba",
    ("Mag", 4, 1): "BitMeseri", ("Lex", 1, 1): "Tintir", ("Sum", 4, 3): "IsinDyn",
}
STAGE_CODES = {"Old Babylonian": "OB", "Middle Babylonian": "MB", "Standard Babylonian": "SB", "Neo-Assyrian": "NA",
               "Neo-Babylonian": "NB", "Late Babylonian": "LB", "Old Assyrian": "OA", "Middle Assyrian": "MA",
               "Old Akkadian": "OAkk", "Uncertain": "Unc", "Hittite": "Hit", "Ur III": "Ur3", "Persian": "Pers",
               "Hellenistic": "Hel", "Parthian": "Parth", "Standard Babylonian (Esagil-kīn-apli)": "SB-EKA"}
# genres in scope: literature and religious incantation series. Divination (D), medicine (Med) and lexical (Lex)
# are left out; see data/ane/SCOPE.md.
EBL_GENRES = {"L", "Mag", "Šui", "Sum"}


def ebl_siglum(t):
    key = (t["genre"], t["category"], t["index"])
    if key in EBL_SIGLA:
        return EBL_SIGLA[key]
    name = re.sub(r"[*‘’“”()]", "", t["name"])
    if name.startswith("šuʾila"):
        return "Shuila " + re.sub(r"^šuʾilas? (to )?", "", name).replace(" ", "")
    return f"eBL {t['genre']}.{t['category']}.{t['index']}"


def ebl_line(line):
    num = line["number"]
    variants = line.get("variants") or []
    v = variants[0] if variants else {}
    text = (v.get("reconstruction") or "").split("\n")[0]
    text = re.sub(r"%[a-z]+\s*", "", text).replace(" || ", " ‖ ").replace(" | ", " ").replace("|", "").strip()
    lemmas = []
    for tok in v.get("reconstructionTokens") or []:
        if tok.get("uniqueLemma"):
            lemmas.append({"form": tok.get("cleanValue") or tok.get("value"), "lemma": tok["uniqueLemma"][0]})
    if not lemmas and (not text or set(re.sub(r"[\s.…\[\]x]", "", text)) == set()):
        mss = v.get("manuscripts") or []
        if mss:
            text = (mss[0].get("atf") or "").strip()
            text = f"{text}  [ms. {''.join(mss[0].get('labels') or [])} {mss[0].get('number', '')}]".strip()
    tr = []
    trs = line.get("translation") or []
    for t in [trs] if isinstance(trs, str) else trs:
        if isinstance(t, dict):
            t = t.get("prefix", "") + "".join(p.get("text", "") for p in t.get("parts") or [])
        m = re.match(r"#tr\.(\w+)(?:\.\((\d+)\))?:\s*(.*)", t, re.S)
        if m and m.group(1) == "en":
            tr.append(m.group(3).strip() + (f" [translation covers {m.group(2)} lines]" if m.group(2) else ""))
    out = {"n": str(num), "text": text, "lemmas": lemmas}
    if tr:
        out["translation"] = " ".join(tr)
    if len(variants) > 1:
        out["variants"] = [re.sub(r"%[a-z]+\s*", "", (x.get("reconstruction") or "").split("\n")[0]).replace("|", "").strip()
                           for x in variants[1:]]
    return out


def ebl_chapter(t, ch):
    g, c, i = t["genre"], t["category"], t["index"]
    url = f"{EBL}/texts/{urllib.parse.quote(g)}/{c}/{i}/chapters/{urllib.parse.quote(ch['stage'])}/{urllib.parse.quote(ch['name'])}"
    d = json.loads(get(url))
    lines = unique_n([ebl_line(l) for l in d.get("lines") or []])
    editors = [f"{a.get('prefix', '')} {a.get('name', '')}".strip() for a in (d.get("record") or {}).get("authors", [])
               if a.get("role") == "EDITOR"]
    return {"name": clean_name(ch["name"]), "title": "".join(p.get("text", "") for p in ch.get("title") or []),
            "editors": editors, "lines": lines}


def fetch_ebl():
    texts = json.loads(get(f"{EBL}/texts"))
    jobs = []
    for t in texts:
        if t["genre"] not in EBL_GENRES or t["category"] == 99 or not t.get("chapters"):
            continue
        by_stage = {}
        for ch in t["chapters"]:
            by_stage.setdefault(ch["stage"], []).append(ch)
        for stage, chs in by_stage.items():
            siglum = f"{ebl_siglum(t)} {STAGE_CODES.get(stage, clean_name(stage))}"
            fname = re.sub(r"[^A-Za-z0-9.-]+", "_", siglum)
            if (RAW / "ebl" / f"{fname}.json").exists():
                continue
            jobs.append((t, stage, chs, siglum, fname))

    def run(job):
        t, stage, chs, siglum, fname = job
        sections = []
        for ch in chs:
            try:
                sections.append(ebl_chapter(t, ch))
            except Exception as e:
                print(f"  eBL {siglum} {ch['name']}: {e}", file=sys.stderr)
        name = re.sub(r"[*]", "", t["name"])
        doc = {"siglum": siglum, "title": f"{name} ({stage})", "language": "akk" if t["genre"] != "Sum" else "sux",
               "source": "eBL", "stage": stage, "genre": t["genre"],
               "edition": "electronic Babylonian Library (eBL) corpus, LMU Munich; editors: "
                          + ", ".join(sorted({e for s in sections for e in s.get("editors", [])})),
               "license": "eBL terms of use; raw data not redistributed",
               "url": f"https://www.ebl.lmu.de/corpus/{t['genre']}/{t['category']}/{t['index']}",
               "sections": sections}
        write("ebl", fname, doc)
        print(f"  eBL {siglum}: {sum(len(s['lines']) for s in sections)} lines")

    with ThreadPoolExecutor(4) as ex:
        list(ex.map(run, jobs))
    fetch_ebl_words()


def fetch_ebl_words():
    """Dictionary entries (meaning, logograms) for every lemma the eBL texts use."""
    path = RAW / "ebl-words.json"
    words = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    used = set()
    for f in (RAW / "ebl").glob("*.json"):
        for s in json.loads(f.read_text(encoding="utf-8"))["sections"]:
            for l in s["lines"]:
                used |= {x["lemma"] for x in l.get("lemmas") or []}
    todo = sorted(used - set(words))

    def one(w):
        try:
            d = json.loads(get(f"{EBL}/words/{urllib.parse.quote(w)}", retries=3, timeout=60))
            return w, {"lemma": " ".join(d.get("lemma") or []), "meaning": d.get("meaning", ""), "pos": d.get("pos", []),
                       "logograms": [" ".join(l.get("logogram") or []) for l in d.get("logograms") or []],
                       "guideWord": d.get("guideWord", "")}
        except Exception:
            return w, None
    with ThreadPoolExecutor(6) as ex:
        for w, d in ex.map(one, todo):
            if d:
                words[w] = d
    path.write_text(json.dumps(words, ensure_ascii=False), encoding="utf-8")
    print(f"  eBL dictionary: {len(words)} lemmas")


# ---------------------------------------------------------------- ETCSL

def etcsl_catalogue():
    out = {}
    for i in range(1, 7):
        t = get(f"{ETCSL}/catalogue/catalogue{i}.htm").decode("latin-1")
        t = html.unescape(re.sub(r"\s+", " ", re.sub("<[^>]+>", " ", t)))
        for num, title in re.findall(r"(\d\.\d+(?:\.\d+)*[a-z]?) (.+?): composite text", t):
            out.setdefault(num, title.strip())
    return out


TIP = re.compile(r"doTooltip\(event, '(.*?)'\)")


def etcsl_text(t):
    t = re.sub(r"<sub>(.*?)</sub>", r"\1", t)
    t = re.sub(r"<sup>(.*?)</sup>", r"{\1}", t)
    return html.unescape(re.sub(r"\s+", " ", re.sub("<[^>]+>", "", t))).strip()


def etcsl_composition(num, title):
    c = get(f"{ETCSL}/cgi-bin/etcsl.cgi?text=c.{num}&display=Crit&charenc=gcirc").decode("utf-8", "replace")
    tr = get(f"{ETCSL}/cgi-bin/etcsl.cgi?text=t.{num}&display=Crit&charenc=gcirc").decode("utf-8", "replace")
    compact = num.replace(".", "")
    sections, order = {}, []
    # each line is a table row holding <a name='c174.A.1'>
    for row in re.findall(r"<tr>(.*?)</tr>", c, re.S):
        m = re.search(r"<a name='c" + re.escape(compact) + r"\.([^']+)'>", row)
        if not m:
            continue
        lid = m.group(1)
        sec, _, n = lid.rpartition(".")
        cells = re.findall(r"<td[^>]*>(.*?)</td>", row, re.S)
        body = cells[-1] if cells else ""
        lemmas = []
        for span in re.finditer(r"<span onMouseover=\"doTooltip\(event, '(.*?)'\)\"[^>]*>(.*?)</span>", body, re.S):
            tip = etcsl_text(span.group(1))
            mm = re.match(r"(.*?) \(([^)]*)\) (.*)", tip)
            if mm and mm.group(1) not in ("…", ""):
                lemmas.append({"form": etcsl_text(span.group(2)), "lemma": mm.group(1), "pos": mm.group(2), "gloss": mm.group(3)})
        if sec not in sections:
            sections[sec] = []
            order.append(sec)
        sections[sec].append({"n": n, "text": etcsl_text(body), "lemmas": lemmas})
    # translation paragraphs: <a href='...lineid=c174.A.1'>1-10.</a><a name='t174.p1'></a> text</p>
    for m in re.finditer(r"lineid=c" + re.escape(compact) + r"\.([^']+)'>([^<]*)</a>(.*?)</p>", tr, re.S):
        lid, rng, body = m.groups()
        sec, _, n = lid.rpartition(".")
        for line in sections.get(sec, []):
            if line["n"] == n:
                line["translation"] = etcsl_text(body)
                line["translation_lines"] = rng.strip().rstrip(".")
                break
    secs = [{"name": clean_name(s) if s else "", "lines": unique_n(sections[s])} for s in order]
    return {"siglum": f"ETCSL {num}", "title": title, "language": "sux", "source": "ETCSL",
            "edition": "The Electronic Text Corpus of Sumerian Literature (Black, Cunningham, Robson, Zólyomi et al., Oxford 1998–2006)",
            "license": "ETCSL terms: free for non-commercial research; raw data not redistributed",
            "url": f"{ETCSL}/cgi-bin/etcsl.cgi?text=c.{num}", "sections": secs}


def fetch_etcsl():
    cat = etcsl_catalogue()
    todo = [(n, t) for n, t in cat.items() if not (RAW / "etcsl" / f"c.{n}.json").exists()]

    def run(job):
        n, t = job
        try:
            doc = etcsl_composition(n, t)
            write("etcsl", f"c.{n}", doc)
            return f"  ETCSL {n}: {sum(len(s['lines']) for s in doc['sections'])} lines"
        except Exception as e:
            return f"  ETCSL {n}: failed ({e})"
    with ThreadPoolExecutor(4) as ex:
        for msg in ex.map(run, todo):
            print(msg)


# ---------------------------------------------------------------- ORACC

# projects and the texts taken from each (None = every text); see data/ane/SCOPE.md
ORACC_PROJECTS = {
    "saao-saa02": None,          # Neo-Assyrian treaties and loyalty oaths (incl. Esarhaddon's Succession Treaty)
    "saao-saa03": None,          # court poetry and literary miscellanea
    "saao-saa09": None,          # Assyrian prophecies
    "saao-saa12": None,          # grants, decrees and gifts (incl. temple decrees)
    "saao-saa20": None,          # Assyrian royal rituals and cultic texts
    "aemw-amarna": None,         # Amarna letters
    "aemw-ugarit": None,         # texts from Ugarit (Akkadian, and lemmatized alphabetic Ugaritic letters and records)
    "saao-saa08": None,          # astrological reports (omens)
    "saao-saa10": None,          # letters from Assyrian and Babylonian scholars
    "saao-saa13": None,          # letters from priests
    "rinap-rinap3": None,        # Sennacherib's inscriptions (the 701 campaign against Judah)
    "rinap-rinap4": None,        # Esarhaddon's inscriptions
    "rinap-rinap5": None,        # Ashurbanipal's inscriptions
    "ribo-babylon7": None,       # Nabonidus' inscriptions
    "ribo-babylon8": None,       # Cyrus and later Achaemenid inscriptions from Babylon (the Cyrus Cylinder)
    "cams-gkab": None,           # scholarly and literary tablets from Uruk (Geography of Knowledge)
}


def oracc_lines(doc):
    """Walk an ORACC corpusjson tree: one entry per line, with lemmas."""
    lines, cur = [], None

    def walk(n):
        nonlocal cur
        if not isinstance(n, dict):
            return
        if n.get("node") == "d" and n.get("type") == "line-start":
            cur = {"n": (n.get("label") or n.get("n") or "").strip(), "words": [], "lemmas": []}
            lines.append(cur)
        elif n.get("node") == "l" and cur is not None:
            f = n.get("f") or {}
            cur["words"].append(f.get("form") or "")
            if f.get("cf"):
                lemma = f.get("cf")
                lemmas = {"form": f.get("form"), "lemma": lemma, "gloss": f.get("gw") or "", "pos": f.get("pos") or "",
                          "sense": f.get("sense") or "", "lang": f.get("lang") or ""}
                if f.get("norm"):
                    lemmas["norm"] = f["norm"]
                cur["lemmas"].append(lemmas)
        for x in n.get("cdl") or []:
            walk(x)
    walk(doc)
    return lines


def oracc_translations(z, project, textid):
    """ORACC translations ship as HTML pages in some zips; absent ones are fine."""
    return {}


def fetch_oracc():
    for proj, only in ORACC_PROJECTS.items():
        target = RAW / "oracc" / proj
        zpath = RAW / "oracc" / f"{proj}.zip"
        if target.exists() and not zpath.exists():
            continue
        if not zpath.exists():
            try:
                data = get(ORACC_JSON.format(proj), oracc=True, timeout=600)
            except Exception as e:
                print(f"  ORACC {proj}: failed ({e})", file=sys.stderr)
                continue
            zpath.parent.mkdir(parents=True, exist_ok=True)
            zpath.write_bytes(data)
        oracc_extract(zpath, proj, only)
        zpath.unlink()


def oracc_extract(zpath, proj, only=None, siglum_prefix=None):
    z = zipfile.ZipFile(zpath)
    names = z.namelist()
    cat_name = next(n for n in names if n.endswith("/catalogue.json") and n.count("/") == proj.count("-") + 1)
    cat = json.loads(z.read(cat_name))
    members = cat.get("members", {})
    lic = cat.get("license", "")
    n_texts = 0
    for name in names:
        m = re.search(r"/corpusjson/([PQX]\d+)\.json$", name)
        if not m or (only and m.group(1) not in only):
            continue
        tid = m.group(1)
        meta = members.get(tid, {})
        try:
            doc = json.loads(z.read(name))
        except ValueError:
            continue
        lines = []
        for l in oracc_lines(doc):
            lines.append({"n": l["n"] or str(len(lines) + 1), "text": " ".join(l["words"]), "lemmas": l["lemmas"]})
        if not lines:
            continue
        title = meta.get("designation") or meta.get("title") or tid
        out = {"siglum": f"{siglum_prefix or proj.split('-')[-1].upper()} {tid}", "title": title, "id": tid,
               "language": meta.get("language", ""), "source": f"ORACC {proj.replace('-', '/')}",
               "genre": meta.get("genre", ""), "subgenre": meta.get("subgenre", ""), "period": meta.get("period", ""),
               "edition": f"ORACC {proj.replace('-', '/')}" + (f"; {meta['publication_history']}" if meta.get("publication_history") else ""),
               "license": lic, "url": f"https://oracc.museum.upenn.edu/{proj.replace('-', '/')}/{tid}",
               "meta": {k: meta[k] for k in ("designation", "primary_publication", "museum_no", "provenience",
                                               "publication_history", "sources", "keywords", "chap", "sec1", "sec2")
                        if k in meta},
               "sections": [{"name": "", "lines": unique_n(lines)}]}
        write(f"oracc/{proj}", tid, out)
        n_texts += 1
    print(f"  ORACC {proj}: {n_texts} texts")


def fetch_oracc_literary():
    """ORACC epsd2/literary: lemmatized composite texts of Sumerian literature (CC0), Q-numbers keyed to ETCSL."""
    zpath = RAW / "oracc" / "epsd2-literary.zip"
    if (RAW / "oracc" / "epsd2-literary").exists() and not zpath.exists():
        return
    zpath.parent.mkdir(parents=True, exist_ok=True)
    if not zpath.exists():
        zpath.write_bytes(get(ORACC_JSON.format("epsd2-literary"), oracc=True, timeout=900))
    z = zipfile.ZipFile(zpath)
    cat = json.loads(z.read("epsd2/literary/catalogue.json"))["members"]
    only = {k for k in cat if k.startswith("Q")}
    oracc_extract(zpath, "epsd2-literary", only, siglum_prefix="Q")
    zpath.unlink()


# ---------------------------------------------------------------- others (agents' fetchers, see tools/ane_sources/)

def fetch_module(name):
    sys.path.insert(0, str(ROOT / "tools" / "ane_sources"))
    mod = __import__(f"fetch_{name}")
    mod.fetch(str(RAW / name))
    short_witnesses(RAW / name)
    attach_cola(RAW / name)


def attach_cola(folder):
    """EUPT translates by colon, not by tablet line: each line gets the translations of the cola that
    start on it, with the lines they cover, so the reading helper shows every colon once."""
    for f in folder.glob("*.json"):
        d = json.loads(f.read_text(encoding="utf-8"))
        if not isinstance(d, dict) or not d.get("cola"):
            continue
        starts = {}
        for c in d["cola"]:
            if c.get("translation") and c.get("lines"):
                starts.setdefault((c["section"], c["lines"][0]), []).append(c)
        for s in d["sections"]:
            for line in s["lines"]:
                cs = starts.get((s["name"], line.get("label_n", line["n"]))) or starts.get((s["name"], line["n"]))
                if cs:
                    line["translation"] = " / ".join(c["translation"] for c in cs)
                    span = [c["lines"][0] for c in cs] + [c["lines"][-1] for c in cs]
                    line["translation_lines"] = f"{span[0]}-{span[-1]}" if span[0] != span[-1] else span[0]
                    line["vocalised"] = " / ".join(c.get("vocalised", "") for c in cs)
                else:
                    line.pop("translation", None)
        f.write_text(json.dumps(d, ensure_ascii=False, indent=0), encoding="utf-8")


def short_witnesses(folder):
    """Texts kept in several manuscript witnesses (Egyptian) carry one section per witness. Long witness
    names become W1, W2, ... (the name is kept as the section's title); a single witness is unnamed."""
    for f in folder.glob("*.json"):
        if f.name.startswith("_"):
            continue
        d = json.loads(f.read_text(encoding="utf-8"))
        secs = d["sections"]
        if not any(" " in s["name"] or "/" in s["name"] for s in secs):
            continue
        for i, s in enumerate(secs, 1):
            s.setdefault("title", s.get("witness") or s["name"])
            s["name"] = "" if len(secs) == 1 else f"W{i}"
        f.write_text(json.dumps(d, ensure_ascii=False, indent=0), encoding="utf-8")


def index():
    out = []
    for f in sorted(RAW.rglob("*.json")):
        if f.name in ("index.json", "ebl-words.json") or f.name.startswith("_"):
            continue
        d = json.loads(f.read_text(encoding="utf-8"))
        if "sections" not in d:
            continue
        out.append({"siglum": d["siglum"], "title": d["title"], "language": d.get("language", ""), "source": d.get("source", ""),
                    "file": str(f.relative_to(RAW)), "sections": len(d["sections"]),
                    "lines": sum(len(s["lines"]) for s in d["sections"])})
    (RAW / "index.json").write_text(json.dumps(out, ensure_ascii=False, indent=0), encoding="utf-8")
    print(f"index: {len(out)} texts, {sum(x['lines'] for x in out)} lines")


SOURCES = {"ebl": fetch_ebl, "etcsl": fetch_etcsl, "oracc": lambda: (fetch_oracc_literary(), fetch_oracc()),
           "ugaritic": lambda: fetch_module("ugaritic"), "egyptian": lambda: fetch_module("egyptian"),
           "hittite": lambda: fetch_module("hittite"), "nws": lambda: fetch_module("nws")}


def main():
    wanted = sys.argv[1:] or list(SOURCES)
    for s in wanted:
        print(f"fetching {s}")
        try:
            SOURCES[s]()
        except Exception as e:
            print(f"  {s} failed: {e}", file=sys.stderr)
    index()


if __name__ == "__main__":
    main()
