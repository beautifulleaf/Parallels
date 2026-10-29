#!/usr/bin/env python3
"""Fetch Northwest Semitic inscriptions (Moabite, Hebrew, Phoenician, Aramaic, ...)
from open editions and normalize them to one JSON file per inscription.

Sources (all fetched live, nothing typed by hand):
  * en.wikisource.org  - H.F.B. Compston, "The Inscription on the Stele of Mesa" (1919),
                         public domain (proofread transcription on Wikisource).
  * he.wikisource.org  - Siloam inscription transcription (CC BY-SA 4.0).
  * en.wikipedia.org / he.wikipedia.org - article sections that reproduce the text
                         of the inscription (CC BY-SA 4.0); each article names the
                         scholarly edition it follows (KAI, Ahituv, Cooke 1903, ...).

No open, licensed source with lemmas/morphology was found for these texts
(CAL forbids scraping), so "lemmas" is always an empty list.

Usage:  python3 fetch_nws.py [out_dir]       (stdlib only)
"""
import html
import json
import os
import random
import re
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

UA = ("ParallelsCorpusFetcher/0.1 (https://github.com/beautifulleaf/parallels; "
      "research corpus builder; python-urllib)")
CC = "CC BY-SA 4.0 (Wikimedia Terms of Use; attribution via page history at the revision URL)"
PD = "Public domain (US; published 1919); Wikisource transcription CC BY-SA 4.0"


# --------------------------------------------------------------------------- HTTP
def _ssl_ctx():
    for ca in (os.environ.get("SSL_CERT_FILE"), "/root/.ccr/ca-bundle.crt"):
        if ca and os.path.exists(ca):
            return ssl.create_default_context(cafile=ca)
    return ssl.create_default_context()


_CTX = _ssl_ctx()


def http_get(url, tries=60, headers=False):
    """GET with polite retry on 429/5xx (Wikimedia rate limits shared IPs hard)."""
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, context=_CTX, timeout=60) as r:
                body = r.read()
                return (body, dict(r.headers)) if headers else body
        except urllib.error.HTTPError as e:
            last = e
            if (e.code == 429 or e.code >= 500) and i < tries - 1:
                ra = e.headers.get("Retry-After")
                try:
                    ra = float(ra)
                except (TypeError, ValueError):
                    ra = 1.0
                time.sleep(min(60, max(ra, 1.0) + random.uniform(0.5, 3.0) + i * 0.5))
                continue
            raise
        except urllib.error.URLError as e:
            last = e
            if i < tries - 1:
                time.sleep(2 + i)
    raise RuntimeError(f"giving up on {url}: {last}")


class Wiki:
    """Fetch page wikitext (with revision id) via the MediaWiki API, cached on disk."""

    def __init__(self, cache_dir):
        self.cache_dir = cache_dir
        os.makedirs(cache_dir, exist_ok=True)

    def page(self, host, title):
        key = re.sub(r"[^\w.-]+", "_", f"{host}__{title}")[:180] + ".json"
        fn = os.path.join(self.cache_dir, key)
        if os.path.exists(fn):
            with open(fn, encoding="utf-8") as f:
                return json.load(f)
        # The action API is rate-limited much harder than action=raw from shared IPs,
        # so content comes from action=raw; the revision id is looked up best-effort.
        t = title
        for _ in range(3):  # follow redirects
            body, hdrs = http_get(f"https://{host}/w/index.php?title="
                                  f"{urllib.parse.quote(t.replace(' ', '_'))}&action=raw", headers=True)
            text = body.decode("utf-8")
            m = re.match(r"\s*#(?:REDIRECT|הפניה)\s*\[\[([^\]|#]+)", text, flags=re.I)
            if not m:
                break
            t = m.group(1).strip()
        revid = None
        try:
            q = urllib.parse.urlencode({"action": "query", "format": "json", "formatversion": "2",
                                        "prop": "revisions", "rvprop": "ids|timestamp", "titles": t})
            pg = json.loads(http_get(f"https://{host}/w/api.php?{q}", tries=3).decode())["query"]["pages"][0]
            revid, ts = pg["revisions"][0]["revid"], pg["revisions"][0]["timestamp"]
        except Exception:
            ts = next((v for k, v in hdrs.items() if k.lower() == "last-modified"), None)
        enc = urllib.parse.quote(t.replace(" ", "_"))
        out = {"host": host, "title": t, "revid": revid, "timestamp": ts, "text": text,
               "retrieved": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
               "url": f"https://{host}/w/index.php?title={enc}" + (f"&oldid={revid}" if revid else "")}
        with open(fn, "w", encoding="utf-8") as f:
            json.dump(out, f, ensure_ascii=False)
        time.sleep(1.0)
        return out


# ---------------------------------------------------------------- wikitext utils
PIPE = "\x01"          # placeholder for {{!}} (a literal "|" in the inscription)
KEEP_LAST = {
    "script", "script/phoenician", "script/hebrew", "script/aramaic", "hebrew", "lang",
    "transliteration", "transl", "sc", "smallcaps", "overline", "underline",
    "not a typo", "sup", "sub", "nowrap", "ציטוטון", '""', "rtl-para", "larger",
    "smaller", "small", "big", "nobr", "lang-he", "lang-phn", "lang-arc", "rtl",
}
KEEP_FIRST = {"מונחון", "פ"}


def find_templates(text, name):
    """Yield (start, end, inner) for balanced {{name|...}} templates."""
    pat = re.compile(r"\{\{\s*" + re.escape(name) + r"\s*(?=[|}])", re.I)
    pos = 0
    while True:
        m = pat.search(text, pos)
        if not m:
            return
        depth, i = 0, m.start()
        while i < len(text):
            if text.startswith("{{", i):
                depth += 1
                i += 2
            elif text.startswith("}}", i):
                depth -= 1
                i += 2
                if depth == 0:
                    break
            else:
                i += 1
        inner = text[m.end():i - 2]
        yield m.start(), i, inner[1:] if inner.startswith("|") else inner
        pos = i


def split_top(s, sep="|"):
    """Split on sep at nesting level 0 (ignores separators inside {{ }} and [[ ]])."""
    out, cur, depth, i = [], [], 0, 0
    while i < len(s):
        two = s[i:i + 2]
        if two in ("{{", "[["):
            depth += 1
            cur.append(two)
            i += 2
            continue
        if two in ("}}", "]]"):
            depth -= 1
            cur.append(two)
            i += 2
            continue
        if s[i] == sep and depth == 0:
            out.append("".join(cur))
            cur = []
        else:
            cur.append(s[i])
        i += 1
    out.append("".join(cur))
    return out


def tpl_param(inner, pname):
    for part in split_top(inner):
        if "=" in part:
            k, v = part.split("=", 1)
            if k.strip() == pname:
                return v
    return None


def strip_refs(t):
    t = re.sub(r"<!--.*?-->", "", t, flags=re.S)
    t = re.sub(r"<ref[^>/]*/>", "", t)
    t = re.sub(r"<ref[^>]*>.*?</ref>", "", t, flags=re.S)
    t = re.sub(r"</?noinclude>", "", t)
    return t


def _expand(m):
    parts = m.group(1).split("|")
    name = parts[0].strip()
    lname = name.lower()
    args = [a for a in parts[1:] if not re.match(r"^\s*[\w\- ]+\s*=", a)]
    if name == "!":
        return PIPE
    if name == "ש":
        return "\n"
    if name == "ר":
        return " "
    if lname in KEEP_FIRST:
        return args[0] if args else ""
    if lname in KEEP_LAST:
        return args[-1] if args else ""
    return ""


def clean(t, br="\n"):
    """Wikitext -> plain text (templates expanded/dropped, links unwrapped)."""
    t = strip_refs(t)
    t = t.replace("{{!}}", PIPE)
    prev = None
    while prev != t:
        prev = t
        t = re.sub(r"\{\{([^{}]*)\}\}", _expand, t)
    # file links (may contain nested links in captions)
    for _ in range(3):
        t = re.sub(r"\[\[(?:File|Image|קובץ|תמונה):[^\[\]]*\]\]", "", t, flags=re.I)
        t = re.sub(r"\[\[(?:File|Image|קובץ|תמונה):[^\[\]]*(\[\[[^\[\]]*\]\][^\[\]]*)*\]\]",
                   "", t, flags=re.I)
    t = re.sub(r"\[\[(?:[^\]|]*\|)?([^\]]*)\]\]", r"\1", t)
    t = re.sub(r"<br\s*/?>", br, t, flags=re.I)
    t = re.sub(r"</?(?:sup|sub|small|span|div|pre|big|u|s|i|b|font|center)[^>]*>", "", t, flags=re.I)
    t = t.replace("'''", "").replace("''", "")
    t = html.unescape(t).replace(" ", " ")
    t = t.replace("{{", "").replace("}}", "")  # stray braces of unbalanced wrappers
    t = t.replace(PIPE, "|")
    return t


def norm_line(s):
    s = s.replace("ﬠ", "ע")  # Hebrew alternative ayin (presentation form) -> ayin
    s = re.sub("[‎‏‪-‮]", "", s)  # bidi marks
    s = s.replace("‏", "").replace("‎", "").replace("‫", "").replace("‬", "")
    return re.sub(r"[ \t]+", " ", s).strip()


def lines_of(t, drop_empty=True):
    out = [norm_line(x) for x in t.split("\n")]
    return [x for x in out if x] if drop_empty else out


NUM_RE = re.compile(r"^\s*(?:\((\d+[a-z]?(?:\s*[-–]\s*\d+)?)\.?\)|(\d+[a-z]?)[.)](?=\s))\s*")


def split_num(s):
    m = NUM_RE.match(s)
    if m:
        return (m.group(1) or m.group(2)).replace(" ", ""), s[m.end():].strip()
    return None, s


def between(text, start, end=None, start_at=0):
    m = re.search(start, text[start_at:], flags=re.M)
    if not m:
        raise ValueError(f"start marker not found: {start!r}")
    s = start_at + m.end()
    if end is None:
        return text[s:]
    m2 = re.search(end, text[s:], flags=re.M)
    return text[s:s + m2.start()] if m2 else text[s:]


def table_rows(t):
    """Parse a wikitable fragment into rows of raw cell strings."""
    body = t
    if "{|" in body:
        body = body[body.index("{|") + 2:]
    if "|}" in body:
        body = body[:body.rindex("|}")]
    rows = []
    for chunk in re.split(r"^\s*\|-.*$", body, flags=re.M):
        cells = []
        for line in chunk.split("\n"):
            ls = line.strip()
            if ls.startswith("|+") or ls.startswith("!"):
                continue
            if ls.startswith("|"):
                for c in split_top(ls[1:].replace("||", "\x02"), "\x02"):
                    cells.append(c)
            elif cells:
                cells[-1] += "\n" + line
        if cells:
            # drop leading attribute part:  style="..." | content
            fixed = []
            for c in cells:
                parts = split_top(c)
                if len(parts) > 1 and re.match(r'^\s*(?:[\w-]+\s*=\s*"[^"]*"\s*)+$', parts[0]):
                    c = "|".join(parts[1:])
                fixed.append(c)
            rows.append(fixed)
    return rows


def he_quotes(text):
    """All {{ציטוט|תוכן=...}} blocks (he.wikipedia) with their character offset."""
    out = []
    for s, e, inner in find_templates(text, "ציטוט"):
        content = tpl_param(inner, "תוכן")
        if content is not None:
            out.append((s, content))
    return out


# ------------------------------------------------------------------- record build
def mk_lines(texts, translations=None, numbers=None, extra=None):
    out = []
    for i, tx in enumerate(texts):
        n = numbers[i] if numbers and i < len(numbers) and numbers[i] else str(i + 1)
        rec = {"n": n, "text": tx, "lemmas": []}
        if translations and i < len(translations) and translations[i]:
            rec["translation"] = translations[i]
        if extra:
            for k, vals in extra.items():
                if vals and i < len(vals) and vals[i]:
                    rec[k] = vals[i]
        out.append(rec)
    return out


def numbered(lines):
    nums, txt = [], []
    for l in lines:
        n, t = split_num(l)
        nums.append(n)
        txt.append(t)
    return nums, txt


def record(siglum, title, language, pages, edition, sections, license_=CC, notes=None):
    pages = pages if isinstance(pages, list) else [pages]
    src = "; ".join(f"{p['host']}: {p['title']} (" + (f"rev {p['revid']}, " if p.get("revid") else "")
                    + f"{p.get('timestamp') or ''}; retrieved {p.get('retrieved', '')})" for p in pages)
    rec = {"siglum": siglum, "title": title, "language": language, "source": src,
           "edition": edition, "license": license_, "url": pages[0]["url"],
           "sections": sections}
    if len(pages) > 1:
        rec["urls"] = [p["url"] for p in pages]
    if notes:
        rec["notes"] = notes
    return rec


def sec(name, lines, **kw):
    d = {"name": name, "lines": lines}
    d.update(kw)
    return d


# ======================================================================= extractors
EN, HE, ENWS, HEWS = "en.wikipedia.org", "he.wikipedia.org", "en.wikisource.org", "he.wikisource.org"
COMPSTON = "Page:The Inscription on the Stele of Méša commonly called the Moabite Stone.djvu/"


def x_mesha(W):
    pages = {n: W.page(ENWS, COMPSTON + str(n)) for n in range(7, 17)}

    def line_tpl(nums):
        res = {}
        for n in nums:
            t = strip_refs(pages[n]["text"])
            # one paragraph per line; the {{line|N}} marker may stand before or after the text
            for chunk in re.split(r"\n\s*\n", t):
                m = re.search(r"\{\{line\|(\d+)\|?\}\}", chunk)
                if m:
                    body = chunk[:m.start()] + chunk[m.end():]
                    body = re.sub(r"</?div[^>]*>", "", body)
                    res[int(m.group(1))] = norm_line(clean(body).replace("\n", " "))
        return res

    heb = line_tpl([11, 12, 13])
    phn = line_tpl([7, 8, 9, 10])
    tr = {}
    for n in (14, 15, 16):
        t = strip_refs(pages[n]["text"])
        for s, e, inner in find_templates(t, "np2"):
            a = split_top(inner)
            if len(a) >= 2 and a[0].strip().isdigit():
                tr[int(a[0])] = norm_line(clean("|".join(a[1:])).replace("\n", " "))
    nums = sorted(heb)
    lines = mk_lines([heb[k] for k in nums], [tr.get(k) for k in nums], [str(k) for k in nums],
                     {"text_phoenician_script": [phn.get(k) for k in nums]})
    return record("KAI 181", "Mesha Stele (Moabite Stone)", "moabite",
                  [pages[11], pages[7], pages[14]],
                  "H. F. B. Compston, The Inscription on the Stele of Méšaʿ, commonly called the "
                  "Moabite Stone (London: SPCK, 1919): II. Text in Hebrew square script; "
                  "I. Phoenician-script text; III. Translation (line-by-line). Square brackets = "
                  "conjectural restorations.",
                  [sec("main", lines)], license_=PD)


def x_siloam(W):
    p = W.page(HEWS, "כתובת השילוח")
    blk = next(find_templates(between(p["text"], r"==הכתובת בציטוט מדויק, כצורתו=="), "רן"))[2]
    txt = lines_of(clean(blk))
    tp = W.page(EN, "Siloam inscription")
    trs = [norm_line(clean(m.group(1))) for m in
           re.finditer(r"^:''(.*)$", between(tp["text"], r"^==Translation==", r"^==[^=]"), flags=re.M)]
    trs = trs if len(trs) == len(txt) else None
    return record("KAI 189", "Siloam tunnel inscription", "hebrew", [p, tp],
                  "Hebrew Wikisource transcription 'exact quotation, in its form' (square script, "
                  "word dividers as '.'); English translation from English Wikipedia (after G. Barkay).",
                  [sec("main", mk_lines(txt, trs))])


def x_tel_dan(W):
    p = W.page(EN, "Tel Dan stele")
    t = p["text"]
    block = between(t, r"^===Text===", r"^Romanized:")
    phn = []
    for m in re.finditer(r"^(\d+)\.\s*(\{\{Script/Phoenician.*)$", block, flags=re.M):
        phn.append((m.group(1), norm_line(clean(m.group(2)).replace("\n", " "))))
    rom = [norm_line(clean(l[1:])) for l in between(t, r"^Romanized:", r"^The 1995 translation").split("\n")
           if l.startswith("#")]
    trs = [norm_line(clean(l[1:])) for l in between(t, r"^The 1995 translation", r"^Other scholars").split("\n")
           if l.startswith("#")]
    nums = [n for n, _ in phn]
    lines = mk_lines([x for _, x in phn], trs if len(trs) == len(phn) else None, nums,
                     {"transliteration": rom if len(rom) == len(phn) else None})
    return record("KAI 310", "Tel Dan stele", "aramaic", p,
                  "English Wikipedia: transcription after A. Biran & J. Naveh (IEJ 1993/1995), in "
                  "Phoenician-script Unicode with romanization; translation by Biran 1995.",
                  [sec("Fragments A+B (joined)", lines)])


def x_deir_alla(W):
    p = W.page(HE, "כתובת בלעם")
    sect = between(p["text"], r"^==\s*הכתובת\s*==", r"^==[^=]")
    q = he_quotes(sect)
    txt = lines_of(clean(q[0][1]))
    return record("KAI 312", "Deir Alla plaster inscription (Balaam son of Beor)", "deir-alla", p,
                  "Hebrew Wikipedia, after Sh. Aḥituv, HaKetav VehaMikhtav (Bialik 2012), pp. 405, 419; "
                  "square script, restorations in [ ]. Only the first combination is given there.",
                  [sec("Combination I", mk_lines(txt))],
                  notes="Combination II is not reproduced in any open source found.")


KA_NAMES = {  # Hebrew Wikipedia headings -> English section labels
    "פיטס א'": "Pithos A", "פיטס ב'": "Pithos B", "פיטס ג'": "Pithos C",
    "הכתובת הארוכה": "long inscription (Meshel 3.1: YHWH of Samaria and his asherah)",
    "כתובות קצרות": "short inscription (names)",
    "המכתב הראשון": "first letter (Meshel 3.6: YHWH of Teman and his asherah)",
    "המכתב השני": "second letter (Meshel 3.9)",
    "רשימת שמות": "list of names",
    "כתובת הטיח העברית בכתב פיניקי": "Hebrew plaster inscription in Phoenician script (Meshel 4.1.1)",
    "הכתובת הפיניקית": "Phoenician-language plaster inscription (Meshel 4.2)",
    "שרידי כתובות קצרים": "short fragments",
}


def x_kuntillet(W):
    p = W.page(HE, "כתובות חורבת תימן")
    t = p["text"]
    heads = [(m.start(), m.group(2).strip()) for m in re.finditer(r"^(=+)\s*(.*?)\s*\1\s*$", t, flags=re.M)]

    def path(pos):
        h2 = h3 = None
        for s, name in heads:
            if s > pos:
                break
            lvl = len(re.match(r"=+", t[s:]).group(0))
            if lvl == 2:
                h2, h3 = name, None
            elif lvl >= 3:
                h3 = name
        return h2, h3

    start = t.index("== פיטס א'")
    stop = t.index("=== כתובות על פיטסים טרם צריפתם")
    sections, seen = [], {}
    for pos, content in he_quotes(t):
        if not (start <= pos < stop):
            continue
        h2, h3 = path(pos)
        name = " – ".join(KA_NAMES.get(h, h) for h in (h2, h3) if h)
        seen[name] = seen.get(name, 0) + 1
        if seen[name] > 1:
            name += f" (reading {seen[name]})"
        sections.append(sec(name, mk_lines(lines_of(clean(content)))))
    for s_ in sections:
        if s_["name"].startswith("Phoenician-language plaster") and "(reading" not in s_["name"]:
            s_["name"] += " (reading 1)"
    # English Wikipedia: Meshel numbering, transliteration + English translation
    ep = W.page(EN, "Kuntillet Ajrud inscriptions")
    et = ep["text"]
    for label in ("Meshel 3.1", "Meshel 3.6", "Meshel 3.9", "Meshel 4.1.1", "Meshel № 4.2", "Meshel 4.3"):
        body = between(et, r"^====\s*" + re.escape(label) + r"\s*====", r"^={2,4}[^=]")
        lines = []
        if "{|" in body:
            for row in table_rows(body):
                cells = [norm_line(clean(c, br=" ")) for c in row]
                cells = [c for c in cells if c]
                if not cells:
                    continue
                n, tx = split_num(cells[0])
                if n is None and re.fullmatch(r"\d+", cells[0]):
                    n, tx, cells = cells[0], cells[1] if len(cells) > 1 else "", cells[1:]
                else:
                    cells = [tx] + cells[1:]
                tr = None
                if len(cells) > 1:
                    _, tr = split_num(cells[1])
                if tx:
                    lines.append({"n": n or str(len(lines) + 1), "text": tx, "lemmas": [],
                                  **({"translation": tr} if tr else {})})
        else:
            cl = clean(body)
            items = []
            for l in lines_of(cl):
                n, tx = split_num(l)
                if n:
                    items.append((n, tx))
            half = len(items) // 2
            if label == "Meshel 3.1":
                tl = [l for l in lines_of(cl) if l.startswith('"')]
                n, tx = items[0]
                lines.append({"n": n, "text": tx, "lemmas": [],
                              **({"translation": tl[0].strip().rstrip('.').strip('"')} if tl else {})})
            elif items and len(items) % 2 == 0:
                for (n, tx), (_, tr) in zip(items[:half], items[half:]):
                    lines.append({"n": n, "text": tx, "lemmas": [], "translation": tr})
        if lines:
            sections.append(sec(label + " (transliteration; English Wikipedia)", lines,
                                source_url=ep["url"]))
    return record("Kuntillet Ajrud", "Kuntillet ʿAjrud (Horvat Teman) inscriptions", "hebrew", [p, ep],
                  "Hebrew Wikipedia sections in square script after Sh. Aḥituv, E. Eshel & Z. Meshel, "
                  "'The Inscriptions', in Z. Meshel (ed.), Kuntillet ʿAjrud (IES 2012), with page refs; "
                  "plus English Wikipedia transliterations + translations (Meshel numbers; Puech 2014, "
                  "Allen, Mastin 2009).",
                  sections)


def x_el_qom(W):
    p = W.page(HE, "חורבת אל כום")
    t = p["text"]
    sect = between(t, r"^===\s*כתובת אריהו\s*===", r"^===\s*כתובות בני נתניהו")
    rows = table_rows(sect)
    sq = None
    for row in rows:
        for c in row:
            if "ציטוט" in c and "{{פ|" not in c:
                sq = lines_of(clean(tpl_param(next(find_templates(c, "ציטוט"))[2], "תוכן")))
    ep = W.page(EN, "Khirbet el-Qom")
    tr = [norm_line(clean(m.group(1))).strip('"') for m in
          re.finditer(r'^::(.*)$', ep["text"], flags=re.M)]
    tr = tr[:4] if len(tr) >= 4 and sq and len(sq) == 4 else None
    secs = [sec("Inscription 3 (Uriyahu)", mk_lines(sq, tr), translation_source=ep["url"])]
    sect2 = between(t, r"^===\s*כתובות בני נתניהו\s*===", r"^==[^=]")
    for i, (pos, content) in enumerate(he_quotes(sect2)):
        secs.append(sec(["Inscription 1 (incised: 'to ʿOphai son of Netanyahu')",
                         "Inscription 2 (painted: 'to ʿUzzah son of Netanyahu')"][i] if i < 2 else f"inscr. {i+1}",
                        mk_lines(lines_of(clean(content)))))
    return record("Khirbet el-Qom 3", "Khirbet el-Qom tomb inscriptions (Uriyahu)", "hebrew", [p, ep],
                  "Hebrew Wikipedia transcription (square script, sources cited there); English "
                  "translation of no. 3 from English Wikipedia after Keel & Uehlinger 1998, p. 239.",
                  secs)


def x_ketef_hinnom(W):
    p = W.page(HE, "לוחיות ברכת כהנים")
    sect = between(p["text"], r"^==נוסח הלוחיות", r"^==[^=]")
    parts = re.split(r"לוחית מס' (\d)", sect)
    ep = W.page(EN, "Ketef Hinnom scrolls")
    secs = []
    for k in range(1, len(parts), 2):
        num, body = parts[k], parts[k + 1]
        L = body.split("\n")
        i0 = next(i for i, l in enumerate(L) if "background-color: silver" in l)
        paleo = [re.sub(r'^.*silver;"\s*\|', "", L[i0])]
        i = i0 + 1
        while i < len(L) and not L[i].startswith("|"):
            paleo.append(L[i])
            i += 1
        sq = [L[i][1:]]
        i += 1
        while i < len(L) and not L[i].startswith("|"):
            sq.append(L[i])
            i += 1
        paleo_l = [x for x in lines_of(clean("\n".join(paleo)))]
        sq_l = [x for x in lines_of(clean("\n".join(sq)))]
        # English Wikipedia translation (Barkay et al. 2004), numbered '#' list
        try:
            eb = between(ep["text"], r"^===\s*KH" + num + r"\s*===", r"^===?[^=]")
            eb = eb.split("{{col-4}}")[0]
            etr = [norm_line(clean(l[1:])) for l in eb.split("\n") if l.startswith("#")]
        except ValueError:
            etr = []
        secs.append(sec(f"Amulet KH {['', 'I', 'II'][int(num)]}",
                        mk_lines(sq_l, etr if len(etr) == len(sq_l) else None, None,
                                 {"text_paleo_hebrew_script": paleo_l if len(paleo_l) == len(sq_l) else None}),
                        translation_source=ep["url"] if len(etr) == len(sq_l) else None))
    return record("KH 1-2", "Ketef Hinnom silver amulets (Priestly Blessing)", "hebrew", [p, ep],
                  "Hebrew Wikipedia, after Sh. Aḥituv, HaKetav VehaMikhtav (2012), pp. 29-31 "
                  "(square script with restorations, plus paleo-Hebrew rendering); English line "
                  "translation from English Wikipedia (Barkay et al. 2004) where line counts agree.",
                  secs)


def x_arslan_tash(W):
    p = W.page(EN, "Arslan Tash amulets")
    t = p["text"]
    secs = []
    for lab in ("AT1", "AT2"):
        try:
            body = between(t, r"^===\s*" + lab + r"\s*===", r"^==[^=]|^===[^=]")
        except ValueError:
            continue
        lines = []
        for row in table_rows(body):
            cells = [norm_line(clean(c, br=" ")) for c in row]
            if len(cells) >= 3 and re.fullmatch(r"\(\d+\)", cells[0]):
                lines.append({"n": cells[0].strip("()"), "text": cells[1], "lemmas": [],
                              "translation": cells[2]})
        secs.append(sec(f"Amulet {lab}", lines))
    return record("KAI 27", "Arslan Tash amulets (incantations)", "phoenician", p,
                  "English Wikipedia: consonantal transliteration (capitals) with line translation; "
                  "AT1 per S. D. Sperling, HUCA 53 (1982); AT2 per the article's cited edition.",
                  secs)


def x_sefire(W):
    p = W.page(HE, "כתובות ספירה")
    t = p["text"]
    out = []
    for kai, title, nxt in (("222", "Sefire stele I (treaty of Bar-Gaʾyah and Matiʿel)", r"^===\s*כתובת הלוח השני"),
                            ("223", "Sefire stele II", r"^==[^=]")):
        body = between(t, r"^===\s*כתובת הלוח \S+ \(KAI " + kai + r"\)\s*===", nxt)
        secs = []
        for pos, content in he_quotes(body):
            pre = body[:pos]
            side = re.findall(r"צד (\S+?)['׳]?:", pre)
            nm = {"א": "Face A", "ב": "Face B", "ג": "Face C"}.get(side[-1] if side else "", f"part {len(secs)+1}")
            secs.append(sec(nm, mk_lines(lines_of(clean(content)))))
        out.append(record("KAI " + kai, title, "aramaic", p,
                          "Hebrew Wikipedia transcription (Old Aramaic in square script, restorations in [ ], "
                          "'-' = illegible letter, '...' = lost line(s)); KAI 222-224 numbering as cited there.",
                          secs, notes="Line numbers are sequential within each face as rendered in the source."))
    return out


def x_zakkur(W):
    p = W.page(HE, "כתובת זכור")
    body = between(p["text"], r"^===\s*מקור\s*===", r"^===[^=]")
    names = ["Face A (front)", "Face B (left side)", "Face C (right side)"]
    secs = [sec(names[i] if i < 3 else f"part {i+1}", mk_lines(lines_of(clean(c))))
            for i, (pos, c) in enumerate(he_quotes(body))]
    return record("KAI 202", "Zakkur stele (Zakkur of Hamath and Luʿash)", "aramaic", p,
                  "Hebrew Wikipedia transcription (square script; final forms not used; restorations in [ ]); "
                  "the article's modern-Hebrew rendering follows KAI II (1964) pp. 204-205.",
                  secs)


def x_kilamuwa(W):
    p = W.page(EN, "Kilamuwa Stela")
    body = between(p["text"], r'<div lang="phn" dir="rtl">', r"</div>")
    txt = lines_of(clean(body))
    return record("KAI 24", "Kilamuwa stele", "phoenician", p,
                  "English Wikipedia, square-script transcription after J. C. L. Gibson, Textbook of "
                  "Syrian Semitic Inscriptions III (1982), pp. 33-34.",
                  [sec("main", mk_lines(txt))])


def _cooke_numbered(p, start):
    body = between(p["text"], start, r"^==[^=]")
    nums, txt = [], []
    for m in re.finditer(r"^(\d+)\.\s*(\{\{Script/Phoenician.*)$", body, flags=re.M):
        nums.append(m.group(1))
        txt.append(norm_line(clean(m.group(2)).replace("\n", " ").rstrip("}").strip()))
    return nums, txt


def x_hadad(W):
    p = W.page(EN, "Hadad Statue")
    nums, txt = _cooke_numbered(p, r"Text-book of North-Semitic Inscriptions")
    return record("KAI 214", "Hadad statue inscription (Panamuwa I)", "samalian", p,
                  "English Wikipedia, text after G. A. Cooke, A Text-Book of North-Semitic Inscriptions "
                  "(1903), rendered in Phoenician-script Unicode (dots under letters = uncertain).",
                  [sec("main", mk_lines(txt, None, nums))])


def x_panamuwa(W):
    p = W.page(EN, "Panamuwa II inscription")
    nums, txt = _cooke_numbered(p, r"^==Text==")
    return record("KAI 215", "Panamuwa II inscription (by Bar-Rakib)", "samalian", p,
                  "English Wikipedia, text after G. A. Cooke, A Text-Book of North-Semitic Inscriptions "
                  "(1903), rendered in Phoenician-script Unicode.",
                  [sec("main", mk_lines(txt, None, nums))])


def x_eshmunazar(W):
    p = W.page(EN, "Sarcophagus of Eshmunazar II")
    body = between(p["text"], r"^====\s*English translation of the lid inscription\s*====", r"^==[^=]")
    lines = []
    for row in table_rows(body):
        c = [norm_line(clean(x, br=" ")) for x in row]
        if len(c) >= 5 and c[0].isdigit():
            lines.append({"n": c[0], "text": c[1], "lemmas": [], "transliteration": c[2],
                          "vocalized": c[3], "translation": c[4]})
    return record("KAI 14", "Eshmunazar II sarcophagus inscription (lid)", "phoenician", p,
                  "English Wikipedia table: Phoenician text and transliteration after Rosenthal 2011 / "
                  "Haelewyck 2012; hypothetical vocalization and translation after Haelewyck 2012.",
                  [sec("Lid", lines)])


def x_ahiram(W):
    p = W.page(EN, "Ahiram sarcophagus")
    body = between(p["text"], r"^== Inscriptions ==", r"^\(The meaning")
    lines, part = [], None
    for row in table_rows(body):
        c = [norm_line(clean(x, br=" ")) for x in row]
        c = [x for x in c]
        if c and c[0].startswith("(text"):
            part, c = c[0].strip("():"), c[1:]
        if len(c) >= 3 and re.search("[\U00010900-\U0001091F]", c[0]):
            lines.append({"n": str(len(lines) + 1), "text": c[0], "lemmas": [], "transliteration": c[1],
                          "translation": c[2], **({"part": part} if part else {})})
    return record("KAI 1", "Ahiram sarcophagus inscription", "phoenician", p,
                  "English Wikipedia table: text after KAI (5th ed. 2002) no. 1; translation after "
                  "Krahmalkov 2000. Rows are phrase units, not physical lines.",
                  [sec("main", lines)])


def x_yehimilk(W):
    p = W.page(EN, "Yehimilk inscription")
    lines = []
    for s, e, inner in find_templates(p["text"], "interlinear"):
        a = split_top(inner)
        num = tpl_param(inner, "number")
        pos = [x for x in a if not x.strip().startswith("number=")]
        if len(pos) >= 2:
            lines.append({"n": (num or "").strip("() ") or str(len(lines) + 1),
                          "text": norm_line(clean(pos[0])), "lemmas": [],
                          "translation": norm_line(clean(pos[1]))})
    hp = W.page(HE, "כתובות מלכי גבל")
    sq = None
    try:
        q = he_quotes(between(hp["text"], r"^==כתובת יחמלך==", r"^==[^=]"))
        sq = lines_of(clean(q[0][1]))
    except (ValueError, IndexError):
        pass
    secs = [sec("main (transliteration, English Wikipedia)", lines)]
    if sq:
        secs.append(sec("square script (Hebrew Wikipedia)", mk_lines(sq), source_url=hp["url"]))
    return record("KAI 4", "Yehimilk inscription (Byblos)", "phoenician", [p, hp],
                  "English Wikipedia: transliteration and translation, text after KAI (2002) I, 1; "
                  "Hebrew Wikipedia: square-script transcription.",
                  secs)


def x_byblian_others(W):
    hp = W.page(HE, "כתובות מלכי גבל")
    out = []
    for head, sig, title in (("כתובת אבבעל", "KAI 5", "Abibaʿal inscription (Byblos)"),
                             ("כתובת אלבעל", "KAI 6", "Elibaʿal inscription (Byblos)"),
                             ("כתובת שפטבעל", "KAI 7", "Shipitbaʿal inscription (Byblos)")):
        try:
            q = he_quotes(between(hp["text"], r"^==" + head + r"==", r"^==[^=]"))
        except ValueError:
            continue
        if q:
            out.append(record(sig, title, "phoenician", hp,
                              "Hebrew Wikipedia, square-script transcription (restorations in [ ]).",
                              [sec("main", mk_lines(lines_of(clean(q[0][1]))))]))
    return out


def x_yehawmilk(W):
    p = W.page(HE, "מצבת יחומלך")
    q = he_quotes(between(p["text"], r"^== הכתובת ==", r"^==[^=]"))
    nums, txt = numbered(lines_of(clean(q[0][1])))
    return record("KAI 10", "Yehawmilk stele (Byblos)", "phoenician", p,
                  "Hebrew Wikipedia, square-script transcription (KAI 10 = CIS I 1).",
                  [sec("main", mk_lines(txt, None, nums))])


def _he_letters(p, head_re, sect_start, sect_end):
    body = between(p["text"], sect_start, sect_end)
    heads = [(m.start(), m.group(1)) for m in re.finditer(head_re, body, flags=re.M)]
    secs = []
    for i, (s, num) in enumerate(heads):
        e = heads[i + 1][0] if i + 1 < len(heads) else len(body)
        chunk = body[s:e]
        qs = he_quotes(chunk)
        sides = ["obverse", "reverse"] if len(qs) == 2 and "{|" in chunk else [None] * len(qs)
        for (pos, content), side in zip(qs, sides):
            lines = lines_of(clean(content))
            if lines:
                secs.append(sec(f"No. {num}" + (f", {side}" if side else ""), mk_lines(lines)))
    return secs


def x_lachish(W):
    p = W.page(HE, "מכתבי לכיש")
    secs = _he_letters(p, r"^===\s*חרס (\d+)\s*===", r"^==תוכן החרסים==", r"^==[^=]")
    return record("KAI 192-199", "Lachish ostraca (letters)", "hebrew", p,
                  "Hebrew Wikipedia: text with partial vocalization and restorations after N. H. Tur-Sinai "
                  "and Sh. Aḥituv (vowel points are editorial, not in the ostraca).",
                  secs)


def x_arad(W):
    p = W.page(HE, "מכתבי ערד")
    secs = _he_letters(p, r"^===\s*מכתב (\d+)\s*===", r"^== מכתבים בולטים ==", r"^== המכתבים הארמיים")
    return record("Arad ostraca", "Arad ostraca (Eliashib archive, selected letters)", "hebrew", p,
                  "Hebrew Wikipedia, transcriptions after Y. Aharoni, Arad Inscriptions (1975); "
                  "letter 24 with editorial vocalization.",
                  secs)


def x_elephantine(W):
    p = W.page(HE, "מכתבי יב")
    t = p["text"]
    secs = []
    q = he_quotes(between(t, r'^==="איגרת הפסח"', r"^===[^=]"))
    if q:
        secs.append(sec("Passover letter (TAD A4.1)", mk_lines(lines_of(clean(q[0][1])))))
    body = between(t, r"^===מכתב אל בגוהי הפחה", r"^===[^=]")
    lines = []
    for row in table_rows(body):
        c = [norm_line(clean(x, br=" ")) for x in row]
        if len(c) >= 2 and c[0]:
            lines.append({"n": str(len(lines) + 1), "text": c[0], "lemmas": [],
                          "translation_modern_hebrew": c[1]})
    if lines:
        secs.append(sec("Petition to Bagohi (TAD A4.7), excerpt", lines))
    q = he_quotes(between(t, r"^=== שטר נישואים ===", r"^===[^=]"))
    if q:
        ls = lines_of(clean(q[0][1]))
        cut = next((i for i, l in enumerate(ls) if l.startswith(":")), len(ls))  # editorial note "on the verso:"
        secs.append(sec("Marriage document of Ananiah and Tamet, recto", mk_lines(ls[:cut])))
        if ls[cut + 1:]:
            secs.append(sec("Marriage document of Ananiah and Tamet, verso", mk_lines(ls[cut + 1:])))
    return record("Elephantine (selection)", "Elephantine Aramaic papyri (selection)", "aramaic", p,
                  "Hebrew Wikipedia transcriptions (Imperial Aramaic in square script); TAD numbers in section "
                  "names were added by the fetcher, not taken from the source.",
                  secs)


def x_gezer(W):
    p = W.page(EN, "Gezer calendar")
    t = p["text"]
    sq = [norm_line(clean(m.group(1))) for m in re.finditer(r"^:+(\{\{Script/Hebrew.*)$", t, flags=re.M)]
    ph = [norm_line(clean(m.group(1))) for m in re.finditer(r"^:+(\{\{Script\|Phnx.*)$", t, flags=re.M)]
    tr = [norm_line(clean(m.group(1))) for m in re.finditer(r"^:+('''.*)$", t, flags=re.M)]
    return record("KAI 182", "Gezer calendar", "hebrew", p,
                  "English Wikipedia: square-script, Phoenician-script and romanized text.",
                  [sec("main", mk_lines(sq, None, None,
                                        {"text_phoenician_script": ph if len(ph) == len(sq) else None,
                                         "transliteration": tr if len(tr) == len(sq) else None}))])


def x_yavne_yam(W):
    p = W.page(EN, "Yavne-Yam ostracon")
    s, e, inner = next(find_templates(p["text"], "Text and translation"))
    a = split_top(inner)
    ph_block = next(find_templates(a[0], "Rtl-para"))[2]
    ph = lines_of(clean(ph_block.split("|", 1)[1] if ph_block.startswith("|") else ph_block))
    rom = lines_of(clean(a[1]))
    return record("KAI 200", "Yavne-Yam (Meṣad Ḥashavyahu) ostracon", "hebrew", p,
                  "English Wikipedia: Paleo-Hebrew (Phoenician-script Unicode) and romanized text; "
                  "{ } = uncertain/restored per the article.",
                  [sec("main", mk_lines(ph, None, None, {"transliteration": rom if len(rom) == len(ph) else None}))])


def x_pyrgi(W):
    p = W.page(EN, "Pyrgi Tablets")
    body = between(p["text"], r"^==Phoenician text==", r"^===? ?Translation variants")
    items = re.split(r"^'''\s*(\{\{Transliteration\|sem\|.*?\}\})[.,]?'''\s*$", body, flags=re.M)
    lines = []
    for k in range(1, len(items), 2):
        tx = norm_line(clean(items[k]))
        tr = lines_of(clean(items[k + 1]))
        lines.append({"n": str(len(lines) + 1), "text": tx, "lemmas": [],
                      **({"translation": tr[0]} if tr else {})})
    return record("KAI 277", "Pyrgi tablets (Phoenician text)", "phoenician", p,
                  "English Wikipedia: consonantal transliteration with translation (after Bonfante; "
                  "Zamora 2015-16). Units are clauses, not physical lines.",
                  [sec("Phoenician tablet", lines)])


def x_tabnit(W):
    p = W.page(EN, "Tabnit sarcophagus")
    body = between(p["text"], r"KAI\]\]\s*13", r"^\|\}")
    rows = table_rows(body + "\n|}")
    row = next(r for r in rows if r and "Phnx" in r[0])
    cols = [lines_of(clean(c)) for c in row]
    ph, sq, tl = cols[0], cols[1], cols[2]
    n = len(ph)
    return record("KAI 13", "Tabnit sarcophagus inscription", "phoenician", p,
                  "English Wikipedia table: Phoenician script, square-script equivalent (partly vocalized "
                  "by the article), transliteration; translation and Haelewyck's restored pronunciation are "
                  "in the article but not line-aligned.",
                  [sec("main", mk_lines(ph, None, None,
                                        {"text_square_script": sq if len(sq) == n else None,
                                         "transliteration": tl if len(tl) == n else None}))])


EXTRACTORS = [x_mesha, x_siloam, x_tel_dan, x_deir_alla, x_kuntillet, x_el_qom, x_ketef_hinnom,
              x_arslan_tash, x_sefire, x_zakkur, x_kilamuwa, x_hadad, x_panamuwa, x_eshmunazar,
              x_ahiram, x_yehimilk, x_byblian_others, x_yehawmilk, x_lachish, x_arad, x_elephantine,
              x_gezer, x_yavne_yam, x_pyrgi, x_tabnit]


def fname(siglum):
    return re.sub(r"[^\w.-]+", "_", siglum).strip("_") + ".json"


def fetch(out_dir, cache_dir=None, only=None):
    os.makedirs(out_dir, exist_ok=True)
    W = Wiki(cache_dir or os.path.join(out_dir, ".cache"))
    summary = []
    for fn in EXTRACTORS:
        if only and fn.__name__ not in only:
            continue
        try:
            res = fn(W)
        except Exception as ex:  # keep going; report failure
            summary.append({"extractor": fn.__name__, "error": f"{type(ex).__name__}: {ex}"})
            print(f"[FAIL] {fn.__name__}: {type(ex).__name__}: {ex}", file=sys.stderr)
            continue
        for rec in (res if isinstance(res, list) else [res]):
            rec["sections"] = [s for s in rec["sections"] if s["lines"]]
            nlines = sum(len(s["lines"]) for s in rec["sections"])
            if not nlines:
                summary.append({"extractor": fn.__name__, "siglum": rec["siglum"], "error": "no lines"})
                continue
            path = os.path.join(out_dir, fname(rec["siglum"]))
            with open(path, "w", encoding="utf-8") as f:
                json.dump(rec, f, ensure_ascii=False, indent=1)
            summary.append({"siglum": rec["siglum"], "title": rec["title"], "lines": nlines,
                            "sections": len(rec["sections"]), "file": os.path.basename(path),
                            "license": rec["license"], "url": rec["url"]})
            print(f"[ok] {rec['siglum']:<24} {nlines:4d} lines  {rec['title']}", flush=True)
    with open(os.path.join(out_dir, "_summary.json"), "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=1)
    return summary


if __name__ == "__main__":
    fetch(sys.argv[1] if len(sys.argv) > 1 else "out",
          only=set(sys.argv[2:]) or None)
