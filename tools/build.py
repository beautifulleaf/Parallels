"""Validate leads and regenerate the artifact.

Usage: python3 tools/build.py [--check]

Reads data/traditions.yaml and leads/*.md, validates every lead against the
format in leads/README.md, then writes site/leads.json, site/index.html
(site/template.html with the taxonomy embedded) and the page data in site/data/:
index.json (a light record per lead), surah-NNN.json (verses and the leads
anchored there) and other-NN.json (leads with no Quran side). --check validates only.
"""
import json
import pathlib
import re
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
LEADS_DIR = ROOT / "leads"
SITE = ROOT / "site"
PART_BYTES = 4_000_000

STATUSES = {"new", "investigating", "promising", "rejected"}
RELATIONS = {"internal", "inheritance", "transmission", "convergence", "response"}
STANDINGS = {"established", "proposed", "contested", "fringe"}
LAYERS = {"lexical", "motif", "concept"}
ORIGINS = {"human", "pipeline"}
BASES = {"original", "reading", "lexicon", "gloss", "scholarship"}
VERDICTS = {"confirmed", "corrected", "disputed"}
REQUIRED = ["id", "title", "summary", "status", "relations", "standing",
            "traditions", "layers", "origin", "added"]
SLUG = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def parse_lead(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        raise ValueError("missing YAML front matter")
    meta = yaml.safe_load(m.group(1)) or {}
    meta["notes"] = m.group(2).strip()
    return meta


def validate(lead, path, tradition_ids):
    errors = []
    for key in REQUIRED:
        if key not in lead:
            errors.append(f"missing '{key}'")
    if errors:
        return errors
    if lead["id"] != path.stem:
        errors.append(f"id '{lead['id']}' does not match filename")
    if not SLUG.match(lead["id"]):
        errors.append("id must be kebab-case")
    if lead["status"] not in STATUSES:
        errors.append(f"status must be one of {sorted(STATUSES)}")
    if lead["standing"] not in STANDINGS:
        errors.append(f"standing must be one of {sorted(STANDINGS)}")
    if lead["origin"] not in ORIGINS:
        errors.append(f"origin must be one of {sorted(ORIGINS)}")
    for key, allowed in (("relations", RELATIONS), ("layers", LAYERS)):
        values = lead[key]
        if not isinstance(values, list) or not values:
            errors.append(f"'{key}' must be a non-empty list")
        elif set(values) - allowed:
            errors.append(f"unknown {key}: {sorted(set(values) - allowed)}")
    traditions = lead["traditions"]
    min_traditions = 1 if lead["relations"] == ["internal"] else 2
    if not isinstance(traditions, list) or len(traditions) < min_traditions:
        errors.append(f"'traditions' needs at least {min_traditions} id(s)")
    else:
        unknown = [t for t in traditions if t not in tradition_ids]
        if unknown:
            errors.append(f"unknown traditions: {unknown}")
    for p in lead.get("passages") or []:
        if p.get("tradition") not in tradition_ids:
            errors.append(f"passage '{p.get('ref')}' has unknown tradition")
    for e in lead.get("evidence") or []:
        if isinstance(e, dict) and (not e.get("text") or e.get("basis") not in BASES):
            errors.append(f"evidence items need 'text' and a 'basis' in {sorted(BASES)}")
            break
    for r in lead.get("reviews") or []:
        if not isinstance(r, dict) or not r.get("by") or r.get("verdict") not in VERDICTS:
            errors.append(f"reviews need 'by' and a 'verdict' in {sorted(VERDICTS)}")
            break
        r["date"] = str(r.get("date", ""))
    for key in ("motifs", "concepts"):
        bad = [v for v in lead.get(key) or [] if not SLUG.match(str(v))]
        if bad:
            errors.append(f"{key} must be kebab-case: {bad}")
    return errors


def main():
    check_only = "--check" in sys.argv
    taxonomy = yaml.safe_load((ROOT / "data" / "traditions.yaml").read_text(encoding="utf-8"))
    tradition_ids = {t["id"] for t in taxonomy["traditions"]}

    leads, failures = [], 0
    for path in sorted(LEADS_DIR.glob("*.md")):
        if path.name == "README.md":
            continue
        try:
            lead = parse_lead(path)
            errors = validate(lead, path, tradition_ids)
        except (ValueError, yaml.YAMLError) as exc:
            errors = [str(exc)]
        if errors:
            failures += 1
            for e in errors:
                print(f"{path.relative_to(ROOT)}: {e}", file=sys.stderr)
            continue
        lead["added"] = str(lead["added"])
        leads.append(lead)

    if failures:
        print(f"{failures} invalid lead(s)", file=sys.stderr)
        sys.exit(1)
    print(f"{len(leads)} leads valid")
    if check_only:
        return

    payload = {"groups": taxonomy["groups"], "traditions": taxonomy["traditions"], "leads": leads}
    (SITE / "leads.json").write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
    write_site(taxonomy, leads)


# ---------------------------------------------------------------- page data
# The page is organised around the Quran: a light index drives the home map, filters and search;
# each surah ships its verses and the full leads anchored in it; leads with no Quran side ship apart.

QREF = re.compile(r"(\d{1,3}):(\d{1,3})(?:\s*[–—-]\s*(?:(\d{1,3}):)?(\d{1,3}))?")
SURA_ONLY = re.compile(r"\bsura\s+(\d{1,3})\b", re.I)


def quran_verses(ref):
    """'Quran 7:136; 20:39', 'Quran 18:83–98', 'Quran 11:25–49; sura 71' -> [(surah, verse|None), ...]."""
    ref = str(ref or "")
    if not re.match(r"^\s*(Quran|Qur'?an|Q)\b", ref, re.I):
        return []
    out = []
    for part in re.split(r"[;,]", re.sub(r"^\s*\S+\s*", "", ref)):
        m = QREF.search(part)
        if m:
            s, a = int(m.group(1)), int(m.group(2))
            if m.group(3) and int(m.group(3)) != s:   # a range across surahs: keep its first verse only
                out.append((s, a))
                continue
            b = int(m.group(4) or a)
            out += [(s, v) for v in range(a, max(a, b) + 1)]
            continue
        m = SURA_ONLY.search(part)
        if m:
            out.append((int(m.group(1)), None))
    return [(s, v) for s, v in out if 1 <= s <= 114]


def quran_anchors(lead):
    """{surah: sorted verses} for every Quran verse the lead touches (an empty list = the surah as a whole)."""
    found = {}
    for m in lead.get("matches") or []:
        for side in m.get("sides") or []:
            if side.get("tradition") == "islam":
                for p in side.get("passages") or []:
                    for s, v in quran_verses(p.get("ref")):
                        found.setdefault(s, set()).add(v)
    for p in lead.get("passages") or []:
        if p.get("tradition") == "islam":
            for s, v in quran_verses(p.get("ref")):
                found.setdefault(s, set()).add(v)
    if not found:
        for u in lead.get("units") or []:
            m = re.match(r"^quran-(\d+)", str(u.get("id", "")))
            if m and 1 <= int(m.group(1)) <= 114:
                found.setdefault(int(m.group(1)), set()).add(None)
    return {s: sorted(v for v in vs if v is not None) for s, vs in found.items()}


def primary_surah(lead, anchors):
    for u in lead.get("units") or []:
        m = re.match(r"^quran-(\d+)", str(u.get("id", "")))
        if m and int(m.group(1)) in anchors:
            return int(m.group(1))
    return min(anchors) if anchors else None


def family_of(tradition_id, trad_by_id):
    t = trad_by_id.get(tradition_id) or {}
    fam = t.get("family", "")
    if tradition_id in ("judaism", "samaritanism"):
        return "hb"
    if fam == "Ancient Near East":
        return "ane"
    if fam == "Greco-Roman":
        return "gr"
    if fam == "Christianity":
        return "chr"
    return "oth"


def partner_traditions(lead):
    ts = [t for t in lead.get("traditions") or [] if t != "islam"]
    units = [u for u in lead.get("units") or [] if u.get("tradition") != "islam"]
    if units:
        first = units[0]["tradition"]
        ts = [first] + [t for t in ts if t != first]
    return ts


def first_note(lead):
    for m in lead.get("matches") or []:
        if m.get("note"):
            return m["note"]
    return lead.get("summary", "")


def clip(text, n):
    text = re.sub(r"\s+", " ", str(text or "")).strip()
    return text if len(text) <= n else text[: n - 1].rsplit(" ", 1)[0] + "…"


def search_text(lead, rec):
    """Words a reader may search for that the light record does not already carry (finding, note, unit titles)."""
    have = " ".join([rec["f"], rec["n"], rec.get("t", "")]).lower()
    bits = [lead.get("title") if not lead.get("units") else "", lead.get("summary"), lead.get("direction"),
            *(lead.get("motifs") or []), *(lead.get("concepts") or []),
            *[m.get("label") for m in lead.get("matches") or []],
            *[x for lx in lead.get("lexical") or [] for x in (lx.get("form"), lx.get("translit"), lx.get("gloss"))],
            *[p.get("ref") for p in lead.get("passages") or []]]
    seen, out = set(), []
    for b in bits:
        b = re.sub(r"\s+", " ", str(b or "")).strip()
        if b and b.lower() not in seen and b.lower() not in have:
            seen.add(b.lower())
            out.append(b)
    return clip(" · ".join(out), 400)


def load_verses(leads):
    """{'12:23': text}. From the Quranic Arabic Corpus when data/raw is present, else from the leads' own passages."""
    try:
        sys.path.insert(0, str(ROOT / "tools"))
        import originals  # noqa: E402
        return originals.load_quran_text(), "Quranic Arabic Corpus (Uthmani script)"
    except Exception as exc:  # raw corpus missing: fall back to what the leads quote
        print(f"note: Quran corpus unavailable ({exc}); using verse texts from the leads", file=sys.stderr)
    texts = {}
    for lead in leads:
        ps = list(lead.get("passages") or [])
        for m in lead.get("matches") or []:
            for side in m.get("sides") or []:
                if side.get("tradition") == "islam":
                    ps += side.get("passages") or []
        for p in ps:
            got = quran_verses(p.get("ref"))
            if len(got) == 1 and got[0][1] and p.get("text"):
                texts.setdefault(f"{got[0][0]}:{got[0][1]}", p["text"])
    return texts, "verse texts quoted in the leads (corpus not available)"


def chunk(items, limit, size_of):
    parts, part, size = [], [], 0
    for it in items:
        n = size_of(it)
        if part and size + n > limit:
            parts.append(part)
            part, size = [], 0
        part.append(it)
        size += n
    if part:
        parts.append(part)
    return parts


def jsize(obj):
    return len(json.dumps(obj, ensure_ascii=False).encode())


def write_json(path, obj):
    data = json.dumps(obj, ensure_ascii=False, separators=(",", ":"))
    if len(data.encode()) > PART_BYTES:
        sys.exit(f"{path.name} would be {len(data.encode())} bytes, over the host's limit")
    path.write_text(data, encoding="utf-8")


def write_site(taxonomy, leads):
    trad_by_id = {t["id"]: t for t in taxonomy["traditions"]}
    data_dir = SITE / "data"
    data_dir.mkdir(exist_ok=True)
    for old in [*data_dir.glob("leads-*.json"), *data_dir.glob("index*.json"),
                *data_dir.glob("surah-*.json"), *data_dir.glob("other-*.json")]:
        old.unlink()

    verses, verse_source = load_verses(leads)
    verse_count = {}
    for ref in verses:
        s, v = map(int, ref.split(":"))
        verse_count[s] = max(verse_count.get(s, 0), v)

    records, by_surah, others, unit_table = [], {}, [], {}
    for lead in leads:
        anchors = quran_anchors(lead)
        prim = primary_surah(lead, anchors)
        partners = partner_traditions(lead)
        fam = family_of(partners[0], trad_by_id) if partners else "oth"
        units = lead.get("units") or []
        rec = {
            "id": lead["id"],
            "f": lead.get("finding") or lead["title"],
            "k": lead.get("kinds") or [],
            "tr": lead["traditions"],
            "fam": fam,
            "u": [u.get("id") for u in lead.get("units") or []],
            "q": [[s, vs[0] if vs else 0, vs[-1] if vs else 0] for s, vs in sorted(anchors.items(), key=lambda x: x[0] != prim)],
            "n": clip(first_note(lead), 200),
            "sd": lead["standing"],
            "rel": lead["relations"],
            "ly": lead["layers"],
        }
        for u in lead.get("units") or []:
            unit_table.setdefault(u.get("id"), [u.get("title"), u.get("tradition")])
        # only what differs from the common case is written, to keep the index light
        if not lead.get("units") and lead["title"] != rec["f"]:
            rec["t"] = lead["title"]
        if lead["status"] != "new":
            rec["st"] = lead["status"]
        if lead.get("reviews"):
            rec["rv"] = 1
            if any(r.get("verdict") == "confirmed" for r in lead["reviews"]):
                rec["cf"] = 1
        if lead.get("benchmark"):
            rec["b"] = 1
        if lead["origin"] != "pipeline":
            rec["o"] = lead["origin"]
        if lead.get("matches"):
            rec["m"] = len(lead["matches"])
        extra = search_text(lead, rec)
        if extra:
            rec["s"] = extra
        if not units:   # leads without units: their passages stand in for the partner side
            rec["pp"] = [[p.get("tradition"), p.get("ref")] for p in lead.get("passages") or [] if p.get("tradition") != "islam"]
        records.append(rec)
        if anchors:
            for s in anchors:
                by_surah.setdefault(s, []).append(lead)
        else:
            others.append((rec, lead))

    # leads with no Quran side, in parts
    other_parts = chunk(others, PART_BYTES - 50_000, lambda x: jsize(x[1]))
    other_names = []
    for i, part in enumerate(other_parts, 1):
        name = f"data/other-{i:02d}.json"
        for rec, _ in part:
            rec["p"] = name
        write_json(SITE / name, {"leads": [lead for _, lead in part]})
        other_names.append(name)

    # one file per surah: its verses and the full leads anchored in it (a big surah spills into -2, -3, ...)
    surahs = []
    for s in range(1, 115):
        n_verses = verse_count.get(s, 0)
        texts = [verses.get(f"{s}:{v}", "") for v in range(1, n_verses + 1)]
        anchored = by_surah.get(s, [])
        surahs.append({"n": s, "v": n_verses, "c": len(anchored)})
        head = {"surah": s, "source": verse_source, "verses": texts, "leads": [], "more": []}
        budget = PART_BYTES - 50_000 - jsize(head)
        parts = chunk(anchored, budget, jsize) or [[]]
        head["leads"] = parts[0]
        extra = []
        for j, part in enumerate(parts[1:], 2):
            name = f"data/surah-{s:03d}-{j}.json"
            write_json(SITE / name, {"leads": part})
            extra.append(name)
        head["more"] = extra
        write_json(SITE / f"data/surah-{s:03d}.json", head)

    fam_of = {r["id"]: r["fam"] for r in records}
    for entry in surahs:
        fams = {}
        for lead in by_surah.get(entry["n"], []):
            fams[fam_of[lead["id"]]] = fams.get(fam_of[lead["id"]], 0) + 1
        entry["fam"] = fams

    # the index, split if it ever outgrows one file
    shell_meta = {"surahs": surahs, "units": unit_table, "others": other_names, "verseSource": verse_source}
    idx_parts = chunk(records, PART_BYTES - 100_000 - jsize(shell_meta), jsize)
    idx_names = [f"data/index-{i:02d}.json" for i in range(2, len(idx_parts) + 1)]
    write_json(data_dir / "index.json", {**shell_meta, "leads": idx_parts[0] if idx_parts else [], "more": idx_names})
    for name, part in zip(idx_names, idx_parts[1:]):
        write_json(SITE / name, {"leads": part})

    shell = {"groups": taxonomy["groups"], "traditions": taxonomy["traditions"], "index": "data/index.json"}
    embedded = json.dumps(shell, ensure_ascii=False).replace("<", "\\u003c")
    template = (SITE / "template.html").read_text(encoding="utf-8")
    if "__DATA__" not in template:
        sys.exit("site/template.html is missing the __DATA__ placeholder")
    (SITE / "index.html").write_text(template.replace("__DATA__", embedded, 1), encoding="utf-8")
    print(f"wrote site/leads.json, site/index.html and {2 + len(idx_names) + len(other_names) + 114} file(s) in site/data/ "
          f"({len(records) - len(others)} leads on the Quran, {len(others)} beyond it)")

if __name__ == "__main__":
    main()
