#!/usr/bin/env python3
"""Fetch Hittite myths, prayers, treaties and rituals from the Hethitologie-Portal Mainz.

Sources
-------
1. hethiter.net text editions (https://hethport.net/txhet_{myth,gebet,svh,besrit}/):
   per composition an introduction (INTR, manuscript list), a transliteration per
   manuscript ("exemplar", TX) with paragraph (§) and clause ("Kolon") numbers, and a
   German translation (TRde) numbered by the same Kolon numbers.
2. TLHdig XML dataset, Beta 0.3 (Zenodo doi:10.5281/zenodo.20328284, CC BY 4.0):
   lemmatised transliterations per manuscript.  Used (a) to attach lemmas to the
   Kolons of the editions and (b) as transliteration-only fallback (no translation)
   for targets without a hethiter.net edition (CTH 1, 19, 264, 68, 106, 409).

Output: one JSON per composition (see `fetch`).  Python 3 standard library only.
"""
import hashlib
import html
import io
import json
import os
import re
import ssl
import sys
import time
import urllib.parse
import urllib.request
import zipfile

BASE = "https://hethport.net"
ZENODO_RECORD = "https://zenodo.org/api/records/20328284"
ZENODO_DOI = "10.5281/zenodo.20328284"
UA = "Parallels-research-fetcher/0.1 (polite; stdlib urllib)"
DELAY = 0.7

LICENSE_EDITION = (
    "hethiter.net text editions: no licence stated on the edition pages (some intro pages "
    "carry '© Universität Mainz – Institut für Altertumswissenschaften'); the Hethitologie-"
    "Portal Mainz footer states 'This work is licensed under a Creative Commons Attribution-"
    "ShareAlike 4.0 International License' (CC BY-SA 4.0). Cite as given in 'edition'. "
    "Lemmas: TLHdig dataset Beta 0.3 (Müller/Prechel/Rieken/Schwemer), Zenodo doi:"
    + ZENODO_DOI + ", CC BY 4.0."
)
LICENSE_TLH = (
    "TLHdig dataset Beta 0.3 (G. Müller, D. Prechel, E. Rieken, D. Schwemer), Zenodo doi:"
    + ZENODO_DOI + ", CC BY 4.0 (TLHdig website: CC BY-SA 4.0). Cite: Thesaurus Linguarum "
    "Hethaeorum digitalis, hethiter.net/: TLHdig – Beta Version 0.3."
)

LANG = {"Hit": "hit", "Akk": "akk", "Sum": "sux", "Hur": "xhu", "Luw": "xlu", "Pal": "plq", "Hat": "xht"}

# ---------------------------------------------------------------- targets


def _base(cth):
    m = re.match(r"CTH (\d+)", cth)
    return int(m.group(1)) if m else -1


def want(group, cth):
    b = _base(cth)
    if group == "myth":
        return 321 <= b <= 337 or 342 <= b <= 353 or 360 <= b <= 365
    if group == "gebet":
        return 371 <= b <= 389
    if group == "svh":
        return 25 <= b <= 147
    if group == "besrit":
        return 390 <= b <= 418 or b == 757
    return False


# editions present on the server but not listed in the svh index (probed)
SVH_PROBE = [44, 49, 50, 57, 67, 68, 75, 76, 78, 89, 92, 96, 100, 106, 122, 132, 133, 134,
             135, 136, 138, 139, 140, 144, 146]

# transliteration-only fallback from TLHdig XML: (CTH, title, preferred folder suffixes)
TLH_ONLY = [
    ("CTH 1", "Anitta-Text", ["HAnn", "TLH"]),
    ("CTH 19", "Erlass des Telipinu", ["HAnn", "TLH"]),
    ("CTH 264", "Instruktionen für Tempelbedienstete", ["TLH"]),
    ("CTH 68", "Vertrag Muršilis II. mit Kupanta-Kurunta von Mira-Kuwaliya", ["SVH", "TLH"]),
    ("CTH 106", "Vertrag Tutḫaliyas IV. mit Kurunta von Tarḫuntašša (u. a. Bronzetafel)", ["SVH", "TLH"]),
    ("CTH 409", "Ritual der Tunnawiya", ["BESRIT", "TLH"]),
]

# ---------------------------------------------------------------- http


def _ctx():
    for ca in (os.environ.get("SSL_CERT_FILE"), "/root/.ccr/ca-bundle.crt"):
        if ca and os.path.exists(ca):
            return ssl.create_default_context(cafile=ca)
    return ssl.create_default_context()


class Http:
    def __init__(self, cache_dir):
        self.cache = cache_dir
        os.makedirs(cache_dir, exist_ok=True)
        self.ctx = _ctx()
        self.last = 0.0

    def get(self, url, binary=False, cache=True):
        key = os.path.join(self.cache, hashlib.sha1(url.encode()).hexdigest())
        if cache and os.path.exists(key):
            with open(key, "rb") as f:
                data = f.read()
        else:
            wait = DELAY - (time.time() - self.last)
            if wait > 0:
                time.sleep(wait)
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            for attempt in range(3):
                try:
                    with urllib.request.urlopen(req, context=self.ctx, timeout=300) as r:
                        data = r.read()
                    break
                except Exception:
                    if attempt == 2:
                        raise
                    time.sleep(3 * (attempt + 1))
            self.last = time.time()
            if cache:
                with open(key, "wb") as f:
                    f.write(data)
        return data if binary else data.decode("utf-8", "replace")


def q(s):
    return urllib.parse.quote(s, safe="")


def page_url(group, page, cth, ed, expl=None, prgr=None, lg="DE"):
    u = "%s/txhet_%s/%s.php?xst=%s" % (BASE, group, page, q(cth))
    if prgr is not None:
        u += "&prgr=" + q(prgr)
    if expl is not None:
        u += "&expl=" + q(expl)
    return u + "&lg=" + lg + "&ed=" + q(ed)


# ---------------------------------------------------------------- html helpers

SUB = str.maketrans("0123456789x", "₀₁₂₃₄₅₆₇₈₉ₓ")


def render(frag):
    """Edition HTML fragment -> plain transliteration / translation text."""
    s = re.sub(r"(?is)<a\s+NAME='fn[^']*'[^>]*>.*?</a>", "", frag)  # footnote anchors
    s = re.sub(r"(?is)<a[^>]*>\s*<hr\s*/?>\s*</a>", " ", s)  # paragraph line
    s = re.sub(r"(?is)<hr\s*/?>", " ", s)
    # determinatives -> {X}, indices -> subscripts (inner markup may contain bracket spans)
    s = re.sub(r'(?is)<span class=["\']AODeterm["\']>(.*?)</span>(?!</span>)',
               lambda m: "{" + re.sub(r"<[^>]+>", "", m.group(1)) + "}", s)
    s = re.sub(r'(?is)<span class=["\']AO--index["\']>(.*?)</span>',
               lambda m: re.sub(r"<[^>]+>", "", m.group(1)).translate(SUB), s)
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s).replace("¬¬¬", " ").replace("===", " ")
    return re.sub(r"\s+", " ", s).strip()


def norm_ln(s):
    s = html.unescape(re.sub(r"<[^>]+>", "", s))
    s = s.replace("′", "'").replace("″", "''").replace("’", "'")
    return re.sub(r"\s+", " ", s).strip()


def line_key(s):
    return re.sub(r"\s+", " ", norm_ln(s).replace(".", " ")).strip()


def sig_frag(siglum):
    m = re.search(r"(\d+)$", siglum.translate(str.maketrans("₀₁₂₃₄₅₆₇₈₉", "0123456789")))
    return m.group(1) if m else None


def citatio(page):
    m = re.search(r"Citatio:</span>(.*?)</span>", page, re.S)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", m.group(1)))).strip() if m else ""


# ---------------------------------------------------------------- edition parsing


def parse_index(page):
    out = []
    for tr in re.split(r"(?i)<tr>", page):
        m = re.search(r"class='zcth'>(.*?)</p>", tr, re.S)
        if not m:
            continue
        ti = re.search(r"class='ztitel'>(.*?)</p>", tr, re.S)
        ed = re.search(r"class='zeditor'>(.*?)</p>", tr, re.S)
        out.append({
            "cth": re.sub(r"\s+", " ", html.unescape(m.group(1))).strip(),
            "title": render(ti.group(1)) if ti else "",
            "editor": html.unescape(ed.group(1)).strip() if ed else "",
        })
    return out


def parse_intro(page):
    """-> (title, {siglum: [publications]}, citation, copyright)"""
    sig = {}
    cur = None
    for tr in re.split(r"(?i)<tr[ >]", page):
        cells = re.findall(r"(?is)<td[^>]*>(.*?)</td>", tr)
        if not cells:
            continue
        m = re.search(r"expl=([^&\"']*)&", cells[0]) if 'AOExemplar' in cells[0] else None
        if m and m.group(1):
            cur = html.unescape(urllib.parse.unquote(m.group(1)))
            sig.setdefault(cur, [])
        pubs = re.findall(r'class="AOTxtPubl">(.*?)</span>', tr)
        if cur and pubs:
            sig[cur].extend(render(p) for p in pubs)
    title = ""
    m = re.search(r"CTH [\w.]+ - (.*?)</", page)
    if m:
        title = render(m.group(1))
    cp = re.search(r"(© [^<]*)", page)
    return title, sig, citatio(page), (cp.group(1).strip() if cp else "")


ROW = re.compile(
    r"<p class='AOExemplar'>(.*?)</p></td><td[^>]*><p class='LineNr'>(.*?)</p></td>\s*"
    r"<td>\s*<p class='AOTextline-(\w+)'>(.*?)</p></td></tr>", re.S)
KOLON = re.compile(r"<span class='KolonNr'>([^<]*)</span>")


def parse_exemplar(page):
    """-> list of (para, siglum, line, lang, [(kolon, text, n_words)])"""
    rows = []
    last_k = None
    for ex, ln, lang, body in ROW.findall(page):
        exs = norm_ln(ex)
        para = ""
        m = re.search(r"\[\s*(§[^\]]*?)\s*\]", exs)
        if m:
            para = m.group(1).strip()
        sigl = exs.split("]")[-1].strip()
        parts = KOLON.split(body)
        segs = []
        if parts[0].strip() and last_k is not None and render(parts[0]):
            segs.append((last_k, parts[0]))
        for i in range(1, len(parts), 2):
            last_k = parts[i].strip()
            segs.append((last_k, parts[i + 1]))
        out = []
        for k, frag in segs:
            words = [render(a) for a in re.findall(r'(?is)<a\s+href="q\.php[^>]*>(.*?)</a>', frag)]
            nw = sum(1 for w in words if w and w not in ("...", "…", "¬¬¬"))
            txt = render(frag)
            if txt or nw:
                out.append((k, txt, nw))
        rows.append((para, sigl, norm_ln(ln), lang, out))
    return rows


def parse_translation(page):
    """-> ordered list of (para, kolon, master_siglum, text, lang)"""
    toks = []
    pat = re.compile(
        r"partitur\.php\?[^\"']*?prgr=(§[^&\"']*)"
        r"|<span class=\"AOKolonNr\">([^<]*)</span>(.*?)<span class=\"AOTranslat-(\w+)\">(.*?)</span>\s*</div>",
        re.S)
    para = ""
    for m in pat.finditer(page):
        if m.group(1):
            para = html.unescape(urllib.parse.unquote(m.group(1))).strip()
            continue
        mid = m.group(3)
        if "AOKolonNr" in mid:  # kolon without translation; skip to avoid swallowing the next
            continue
        ms = re.search(r"class='masterT'>([^<]*)<", mid)
        toks.append((para, m.group(2).strip(), ms.group(1).strip() if ms else "", render(m.group(5)), m.group(4)))
    return toks


# ---------------------------------------------------------------- TLHdig XML

W_TOK = re.compile(r'<lb\b([^>]*)/>|<clb\b[^>]*\bid="([^"]*)"[^>]*/>|<w\b([^>]*?)(?:/>|>(.*?)</w>)', re.S)
CIRC = re.compile(r"[①-⑳]")


def attrs(s):
    return {k: html.unescape(v) for k, v in re.findall(r'([\w:.-]+)="([^"]*)"', s)}


def xml_form(inner):
    s = re.sub(r"(?s)<note\b.*?/>", "", inner or "")
    s = re.sub(r"<d>(.*?)</d>", lambda m: "{" + re.sub(r"<[^>]+>", "", m.group(1)) + "}", s)
    s = s.replace("<del_in/>", "[").replace("<del_fin/>", "]")
    s = s.replace("<laes_in/>", "⌈").replace("<laes_fin/>", "⌉")
    s = re.sub(r'<corr c="([^"]*)"/>', r"\1", s)
    s = re.sub(r'<gap c="([^"]*)"/>', r" \1 ", s)
    s = re.sub(r"<[^>]+>", "", s)
    return re.sub(r"\s+", " ", html.unescape(s)).strip()


def _morph(field, letter):
    alts = re.findall(r"\{\s*([A-Za-z])\s*→\s*([^}]*)\}", field)
    if not alts:
        return field.strip()
    if letter:
        for k, v in alts:
            if k == letter:
                return v.strip()
    return " | ".join(v.strip() for _, v in alts)


def parse_mrp(s, letters=""):
    parts = s.split("@")
    lemma = CIRC.sub("", parts[0]).strip()
    gloss = parts[1].strip() if len(parts) > 1 else ""
    lo = "".join(c for c in letters if c.islower())
    up = "".join(c for c in letters if c.isupper())
    pos = _morph(parts[2], lo) if len(parts) > 2 else ""
    rest = "@".join(parts[3:])
    d = {"lemma": lemma.replace("=", ""), "gloss": gloss, "pos": pos}
    m = re.search(r"\+=\s*([^@]*)@([^@]*)", rest)
    if m:
        d["enclitic"] = m.group(1).strip()
        d["enclitic_pos"] = _morph(m.group(2), up)
    if not pos:
        m2 = re.match(r"([^@+]*)", rest)
        if m2 and re.fullmatch(r"\s*[A-Z][A-Za-z.]*\s*", m2.group(1) or ""):
            d["pos"] = m2.group(1).strip()
    return d


def word_lemma(a, inner):
    sel = a.get("mrp0sel")
    form = xml_form(inner)
    if sel is None:
        return {"form": form, "lemma": None, "gloss": "", "pos": ""} if a.get("trans") else None
    opts = {int(k[3:]): v for k, v in a.items() if re.fullmatch(r"mrp\d+", k) and k != "mrp0"}
    if sel.strip() == "DEL":
        return None
    if not opts:
        d = {"form": form, "lemma": None, "gloss": "", "pos": ""}
        if a.get("lg"):
            d["lang"] = a["lg"]
        return d
    m = re.fullmatch(r"\s*(\d+)\s*([A-Za-z]*)\s*", sel)
    if m and int(m.group(1)) in opts:
        d = parse_mrp(opts[int(m.group(1))], m.group(2))
    elif len(opts) == 1:
        d = parse_mrp(next(iter(opts.values())))
    else:
        ps = [parse_mrp(opts[k]) for k in sorted(opts)]
        lem = list(dict.fromkeys(p["lemma"] for p in ps))
        d = {"lemma": " | ".join(lem),
             "gloss": " | ".join(dict.fromkeys(p["gloss"] for p in ps)),
             "pos": " | ".join(dict.fromkeys(x for p in ps for x in p["pos"].split(" | ") if x)),
             "ambiguous": True}
    d = {"form": form, **d}
    if a.get("lg"):
        d["lang"] = a["lg"]
    return d


def parse_xml(text):
    """-> list of lines: {lnr, txtid, lg, words:[(clb, form, lemma|None)]}"""
    lines = []
    clb = None
    cur = None
    for m in W_TOK.finditer(text):
        if m.group(1) is not None:
            a = attrs(m.group(1))
            raw = norm_ln(a.get("lnr", ""))
            fm = re.match(r"\{€\s*([^}]*)\}\s*", raw)
            cur = {"lnr": raw, "key": line_key(raw[fm.end():] if fm else raw),
                   "frag": (re.sub(r"\D", "", fm.group(1)) or None) if fm else None,
                   "txtid": a.get("txtid", ""), "lg": a.get("lg", ""), "words": []}
            lines.append(cur)
        elif m.group(2) is not None:
            clb = m.group(2)
        elif cur is not None:
            a = attrs(m.group(3) or "")
            form = xml_form(m.group(4))
            if not form:
                continue
            cur["words"].append((clb, form, word_lemma(a, m.group(4))))
    return lines


class TLH:
    def __init__(self, http, cache_dir):
        path = os.path.join(cache_dir, "TLHdig_Beta_03.zip")
        if not os.path.exists(path):
            meta = json.loads(http.get(ZENODO_RECORD, cache=False))
            f = meta["files"][0]
            data = http.get(f["links"]["self"], binary=True, cache=False)
            md5 = f.get("checksum", "").replace("md5:", "")
            if md5 and hashlib.md5(data).hexdigest() != md5:
                raise RuntimeError("TLHdig zip checksum mismatch")
            with open(path, "wb") as fh:
                fh.write(data)
        self.z = zipfile.ZipFile(path)
        self.folders = {}
        for n in self.z.namelist():
            if n.startswith("__MACOSX") or not n.endswith(".xml"):
                continue
            p = n.split("/")
            if len(p) == 3:
                self.folders.setdefault(p[1], []).append(n)
        self._cache = {}

    def files_for(self, base, suffixes=None):
        out = []
        for folder, files in self.folders.items():
            m = re.match(r"CTH (\d+)_XML_(\w+)$", folder)
            if m and int(m.group(1)) == base and (suffixes is None or m.group(2) in suffixes):
                out.extend(sorted(files))
        return out

    def lines(self, name):
        if name not in self._cache:
            self._cache[name] = parse_xml(self.z.read(name).decode("utf-8", "replace"))
        return self._cache[name]

    def find(self, base, pubs):
        cands = self.files_for(base)
        for pub in pubs:
            for n in cands:
                stem = n.rsplit("/", 1)[1][:-4].rstrip("+").strip()
                if stem == pub.strip():
                    return n
        return None


# ---------------------------------------------------------------- composition builders


def build_edition(http, tlh, group, entry, stats):
    cth, ed = entry["cth"], entry["editor"]
    intro_url = page_url(group, "intro", cth, ed, prgr="")
    intro = http.get(intro_url)
    title, sigla, intr_cit, copyright_ = parse_intro(intro)
    # German translation is the default; some editions (e.g. A. Mouton, B.-J. Collins) are FR/EN
    for tr_lg in ("DE", "EN", "FR", "IT"):
        tr_url = page_url(group, "translatio", cth, ed, expl="", lg=tr_lg)
        trp = http.get(tr_url)
        trans = parse_translation(trp)
        if trans:
            break
    if not trans:
        tr_lg = None
        tr_url = page_url(group, "translatio", cth, ed, expl="")
        trp = http.get(tr_url)
    if not title:
        m = re.search(r"([^<>]{5,200}?)\(\s*(?:<[^>]+>\s*)*" + re.escape(cth) + r"\s*(?:<[^>]+>\s*)*\)", intro)
        if m:
            title = render(m.group(1))
    lead_url = page_url(group, "exemplar", cth, ed, expl="")
    leadp = http.get(lead_url)
    tx_cit = citatio(leadp)
    tr_cit = citatio(trp)
    if not trans and not ROW.search(leadp):
        return None

    # kolon -> {siglum: {"para", "texts":[(line,text)], "nw"}}
    kol = {}
    order_tx = []
    langs = {}

    def absorb(rows, default_sig):
        for para, sigl, ln, lang, segs in rows:
            s = sigl or default_sig
            for k, txt, nw in segs:
                d = kol.setdefault(k, {}).setdefault(s, {"para": para, "texts": [], "nw": 0, "letter": re.sub(r"[\d₀-₉]+$", "", s)})
                d["texts"].append((ln, txt))
                d["nw"] += nw
                langs[lang] = langs.get(lang, 0) + 1
                if k not in order_tx:
                    order_tx.append(k)

    lead_rows = parse_exemplar(leadp)
    absorb(lead_rows, "A")
    lead_letters = {re.sub(r"[\d₀-₉]+$", "", r[1]) for r in lead_rows if r[1]}
    fetched = set(lead_letters) | {""}
    tr_k = [t[1] for t in trans]

    def need_more():
        return [k for k in tr_k if not any(v["nw"] for v in kol.get(k, {}).values())]

    urls = {"": lead_url}
    for s in sigla:
        if not need_more():
            break
        if s in fetched:
            continue
        u = page_url(group, "exemplar", cth, ed, expl=s)
        urls[s] = u
        absorb(parse_exemplar(http.get(u)), s)
        fetched.add(s)

    # lemma lookup per manuscript letter
    xml_lines = {}

    def lemmas_for(letter, k, lnset, frag):
        if letter not in xml_lines:
            name = tlh.find(_base(cth), sigla.get(letter, []))
            xml_lines[letter] = (name, tlh.lines(name) if name else [])
        name, lines = xml_lines[letter]
        keys = {line_key(x) for x in lnset}
        out = []
        for L in lines:
            if L["key"] in keys and (frag is None or L["frag"] is None or L["frag"] == frag):
                out.extend(lem for c, f, lem in L["words"] if c == k and lem)
        return out, name

    tr_map = {}
    for para, k, master, txt, lg in trans:
        tr_map.setdefault(k, (para, master, txt))
    keys = list(dict.fromkeys(tr_k + [k for k in order_tx if k not in tr_k]))
    if tr_k:  # keep translation order, insert TX-only kolons after their predecessor
        keys = []
        tx_only = [k for k in order_tx if k not in tr_map]
        for k in tr_k:
            if k not in keys:
                keys.append(k)
        for k in tx_only:
            i = order_tx.index(k)
            prev = next((order_tx[j] for j in range(i - 1, -1, -1) if order_tx[j] in keys), None)
            keys.insert(keys.index(prev) + 1 if prev else 0, k)

    sections = []
    secmap = {}
    xml_used = set()
    n_lem = 0
    for k in keys:
        wit = kol.get(k, {})
        choice = None
        if wit:
            lead = [s for s in wit if wit[s]["letter"] in lead_letters and wit[s]["nw"] > 0]
            choice = lead[0] if lead else max(wit, key=lambda s: wit[s]["nw"])
        para = tr_map[k][0] if k in tr_map else (wit[choice]["para"] if choice else "")
        line = {"n": k, "text": "", "lemmas": [], "translation": tr_map[k][2] if k in tr_map else ""}
        if choice:
            d = wit[choice]
            line["text"] = " ".join(t for _, t in d["texts"]).strip()
            line["witness"] = choice
            lns = [l for l, _ in d["texts"]]
            line["ref"] = "%s %s" % (choice, lns[0] if len(lns) == 1 else lns[0] + " – " + lns[-1])
            lem, name = lemmas_for(d["letter"], k, set(lns), sig_frag(choice))
            if any(x.get("lemma") for x in lem):
                line["lemmas"] = lem
                n_lem += any(x.get("lemma") for x in lem)
                xml_used.add(name)
        if not line["text"] and not line["translation"]:
            continue
        sec = secmap.get(para)
        if sec is None:
            sec = {"name": para or "(ohne §)", "lines": []}
            secmap[para] = sec
            sections.append(sec)
        sec["lines"].append(line)

    lang = max(langs, key=langs.get) if langs else "Hit"
    nlines = sum(len(s["lines"]) for s in sections)
    stats.append((cth, title or entry["title"], len(sections), nlines,
                  sum(1 for s in sections for l in s["lines"] if l["translation"]), n_lem))
    edition = "; ".join(x for x in (tx_cit, tr_cit, intr_cit) if x)
    return {
        "siglum": cth,
        "title": title or entry["title"],
        "language": LANG.get(lang, lang.lower()),
        "source": "hethiter.net (Hethitologie-Portal Mainz) / TLHdig",
        "edition": edition + (" | editor: " + ed if ed else ""),
        "license": LICENSE_EDITION + (" Intro page: " + copyright_ if copyright_ else ""),
        "url": tr_url,
        "urls": {"introductio": intro_url, "translatio": tr_url,
                 "exemplar": {k or "lead": v for k, v in urls.items()}},
        "manuscripts": sigla,
        "translation_language": (tr_lg or "").lower() or None,
        "lemma_source": sorted(n.split("/", 1)[1] for n in xml_used),
        "unit": "Kolon (clause) as numbered in the edition; sections = § paragraphs",
        "sections": sections,
    }


def build_tlh_only(tlh, cth, title, suffixes, stats):
    files = []
    for suf in suffixes:
        fs = tlh.files_for(_base(cth), [suf])
        if fs:
            files = fs
            break
    if not files:
        return None
    sections = []
    langs = {}
    n_lem = 0
    for name in files:
        lines = tlh.lines(name)
        sec = {"name": name.rsplit("/", 1)[1][:-4] + " (" + name.split("/")[1] + ")", "lines": []}
        seen = {}
        for L in lines:
            if not L["words"]:
                continue
            n = L["lnr"] or "?"
            if L["txtid"] and L["txtid"] not in sec["name"]:
                n = L["txtid"] + " " + n
            seen[n] = seen.get(n, 0) + 1
            if seen[n] > 1:
                n = "%s (%d)" % (n, seen[n])
            lem = [w[2] for w in L["words"] if w[2]]
            if not any(x.get("lemma") for x in lem):
                lem = []
            n_lem += any(x.get("lemma") for x in lem)
            langs[L["lg"]] = langs.get(L["lg"], 0) + 1
            sec["lines"].append({"n": n, "text": " ".join(w[1] for w in L["words"]),
                                 "lemmas": lem, "translation": ""})
        if sec["lines"]:
            sections.append(sec)
    lang = max(langs, key=langs.get) if langs else "Hit"
    stats.append((cth, title, len(sections), sum(len(s["lines"]) for s in sections), 0, n_lem))
    return {
        "siglum": cth, "title": title, "language": LANG.get(lang, lang.lower()),
        "source": "TLHdig XML dataset (Zenodo)",
        "edition": "Thesaurus Linguarum Hethaeorum digitalis, hethiter.net/: TLHdig – Beta Version 0.3 "
                   "(dataset published 2026-05-21, doi:%s); per-manuscript transliterations, no composite text, "
                   "no translation" % ZENODO_DOI,
        "license": LICENSE_TLH,
        "url": "https://doi.org/" + ZENODO_DOI,
        "lemma_source": [n.split("/", 1)[1] for n in files],
        "unit": "physical tablet line; one section per manuscript (tablet/fragment)",
        "sections": sections,
    }


# ---------------------------------------------------------------- main


def safe(cth):
    return re.sub(r"[^\w.]+", "_", cth).strip("_")


def fetch(out_dir, cache_dir=None, limit=None):
    out_dir = os.path.abspath(out_dir)
    cache_dir = cache_dir or os.path.join(os.path.dirname(out_dir), "dl", "cache")
    os.makedirs(out_dir, exist_ok=True)
    http = Http(cache_dir)
    tlh = TLH(http, cache_dir)
    stats, failures = [], []

    entries = []
    for g in ("myth", "gebet", "svh", "besrit"):
        idx = parse_index(http.get("%s/txhet_%s/textindex.php?g=%s&x=x" % (BASE, g, g)))
        seen = {e["cth"] for e in idx}
        for e in idx:
            if want(g, e["cth"]):
                entries.append((g, e))
        if g == "svh":
            for n in SVH_PROBE:
                c = "CTH %d" % n
                if c in seen:
                    continue
                p = http.get(page_url(g, "intro", c, "", prgr=""))
                if "Citatio" in p and ROW.search(http.get(page_url(g, "exemplar", c, "", expl=""))):
                    entries.append((g, {"cth": c, "title": "", "editor": ""}))
    if limit:
        entries = entries[:limit]

    done = set()
    for g, e in entries:
        try:
            doc = build_edition(http, tlh, g, e, stats)
        except Exception as ex:  # keep going
            failures.append((e["cth"], repr(ex)))
            continue
        if doc is None:
            failures.append((e["cth"], "no edition content"))
            continue
        with open(os.path.join(out_dir, safe(e["cth"]) + ".json"), "w", encoding="utf-8") as f:
            json.dump(doc, f, ensure_ascii=False, indent=1)
        done.add(_base(e["cth"]))
        print("ok", e["cth"], file=sys.stderr)

    for cth, title, sufs in TLH_ONLY:
        if _base(cth) in done:
            continue
        doc = build_tlh_only(tlh, cth, title, sufs, stats)
        if doc is None:
            failures.append((cth, "no TLHdig XML"))
            continue
        with open(os.path.join(out_dir, safe(cth) + ".TLHdig.json"), "w", encoding="utf-8") as f:
            json.dump(doc, f, ensure_ascii=False, indent=1)
        print("ok (TLHdig only)", cth, file=sys.stderr)

    with open(os.path.join(out_dir, "_summary.tsv"), "w", encoding="utf-8") as f:
        f.write("siglum\ttitle\tsections\tlines\tlines_with_translation\tlines_with_lemmas\n")
        for s in stats:
            f.write("\t".join(str(x) for x in s) + "\n")
        for c, why in failures:
            f.write("%s\tFAILED: %s\n" % (c, why))
    return stats, failures


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
    lim = int(sys.argv[2]) if len(sys.argv) > 2 else None
    st, fl = fetch(out, limit=lim)
    print("%d compositions, %d failures" % (len(st), len(fl)))
