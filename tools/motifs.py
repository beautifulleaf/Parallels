"""Motif track: compare story units across traditions by shared motifs.

Usage: python3 tools/motifs.py [--write-leads]
       python3 tools/motifs.py --validate <tag file>

Units and their verse-anchored motif tags live in data/motif-tags/*.yaml;
the vocabulary is data/motifs.yaml. Each motif is weighted by how rare it is
across units (log N/df), so a shared rare motif counts for more than a shared
common one. Pairs of units from different traditions are ranked by the summed
weight of their shared motifs.

Side-by-side comparisons in data/alignments/ add confirmed shared tags to both
units of a pair (see data/alignments/README.md).

Writes results/motifs/pairs.json and results/motifs/REPORT.md, checks
data/benchmarks/motifs.yaml, and with --write-leads creates or refreshes
pipeline leads in leads/.
"""
import json
import math
import re
import pathlib
import sys
from collections import Counter
from datetime import date

import yaml

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import corpora  # noqa: E402
import lexical  # noqa: E402
import originals  # noqa: E402

ROOT = corpora.ROOT
DATA = ROOT / "data"
OUT = ROOT / "results" / "motifs"
MIN_SHARED = 2
TOP_PER_UNIT = 3
MAX_PASSAGE_MOTIFS = 10   # passages shown per lead: the rarest shared motifs
MAX_ONLY = 12             # unshared motifs listed per side in a lead
MAX_INTERNAL_LEADS = 30   # internal pairs (one text echoing itself) written as lead files, per corpus; the rest stay in the report


def load(strict=True):
    """Vocabulary from data/motifs.yaml plus each tag file's `new_motifs`, and
    all units. With strict=False, unreadable tag files are skipped (used while
    reader agents are still writing theirs)."""
    vocab = yaml.safe_load((DATA / "motifs.yaml").read_text(encoding="utf-8"))["motifs"]
    units = []
    for path in sorted((DATA / "motif-tags").rglob("*.yaml")):
        try:
            doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        except yaml.YAMLError:
            if strict:
                raise
            print(f"skipping unreadable {path.relative_to(DATA)}", file=sys.stderr)
            continue
        rel = str(path.relative_to(DATA / "motif-tags"))
        for mid, m in (doc.get("new_motifs") or {}).items():
            if mid in vocab and vocab[mid]["label"] != m["label"]:
                # same id, different wording: the first definition wins; variants are reviewed at merge time
                vocab[mid].setdefault("label_variants", []).append({"label": m["label"], "file": rel})
                continue
            vocab.setdefault(mid, {**m, "proposed_in": rel})
        for u in doc.get("units") or []:
            u["file"] = rel
            units.append(u)
    load_alignments(vocab, units)
    # merged ids (data/motif-aliases.yaml): tags resolve to the canonical id
    alias_path = DATA / "motif-aliases.yaml"
    aliases = (yaml.safe_load(alias_path.read_text(encoding="utf-8")) or {}).get("aliases", {}) if alias_path.exists() else {}
    for a, c in aliases.items():
        if a in vocab:
            vocab[a]["alias_of"] = c
    for u in units:
        for t in u["tags"]:
            if t["motif"] in aliases:
                t["written_as"] = t["motif"]
                t["motif"] = aliases[t["motif"]]
    return vocab, units


DIVERGING = ("divergence", "response", "contrast")
CONFIRMED = {}       # frozenset({unit a, unit b}) -> match details, from data/alignments/
ALIGN_ERRORS = []


def load_alignments(vocab, units):
    """Side-by-side comparison files (data/alignments/<pair>/*.yaml, see its README).
    Each confirmed match adds one shared tag to both units, citing each unit's own
    verses, so the ordinary motif matching sees it; the pair is also recorded as
    confirmed, which makes it a lead even on a single shared motif."""
    CONFIRMED.clear()
    ALIGN_ERRORS.clear()
    by_id = {u["id"]: u for u in units}
    for path in sorted((DATA / "alignments").rglob("[0-9]*.yaml")):
        rel = str(path.relative_to(DATA))
        try:
            doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        except yaml.YAMLError as e:
            ALIGN_ERRORS.append(f"{rel}: unreadable ({e.__class__.__name__})")
            continue
        for mid, m in (doc.get("new_motifs") or {}).items():
            if mid in vocab and vocab[mid]["label"] != m["label"]:
                vocab[mid].setdefault("label_variants", []).append({"label": m["label"], "file": rel})
                continue
            vocab.setdefault(mid, {**m, "proposed_in": rel})
        for r in doc.get("reviewed") or []:
            for x in r.get("matches") or []:
                a, b = by_id.get(r.get("unit")), by_id.get(x.get("with"))
                if a is None or b is None:
                    ALIGN_ERRORS.append(f"{rel}: unknown unit {r.get('unit') if a is None else x.get('with')}")
                    continue
                mid, relation = x.get("motif"), x.get("relation") or "parallel"
                if relation in DIVERGING and mid in vocab:
                    # a divergence shares the matter, not the claim: neither verse gets the other side's label
                    base, mid = mid, f"{mid}-as-{relation}"
                    vocab.setdefault(mid, {"label": f"{vocab[base]['label']} [{relation} between the texts]",
                                           "cluster": vocab[base].get("cluster"), "proposed_in": rel, "diverges_from": base})
                for u, refs in ((a, x.get("refs") or []), (b, x.get("with_refs") or [])):
                    if not refs:
                        ALIGN_ERRORS.append(f"{rel}: {r['unit']} ~ {x['with']}: {x.get('motif')} needs refs on both sides")
                    t = next((t for t in u["tags"] if t["motif"] == mid), None)
                    if t is None:
                        u["tags"].append({"motif": mid, "refs": list(refs), "via": rel,
                                          **({"note": x["note"]} if x.get("note") else {})})
                    else:
                        t["refs"] = list(dict.fromkeys(t["refs"] + list(refs)))
                c = CONFIRMED.setdefault(frozenset((a["id"], b["id"])), {"file": rel, "relations": set(), "notes": [], "matches": []})
                c["relations"].add(relation)
                c["matches"].append({"motif": mid, "base": x.get("motif"), "relation": relation, "note": x.get("note") or "",
                                     "refs": {a["id"]: list(x.get("refs") or []), b["id"]: list(x.get("with_refs") or [])}})
                if x.get("note"):
                    c["notes"].append(x["note"])


def validate(vocab, units, quran_text, hebrew_text):
    errors, seen = list(ALIGN_ERRORS), set()
    tradition_ids = {t["id"] for t in yaml.safe_load((DATA / "traditions.yaml").read_text(encoding="utf-8"))["traditions"]}
    for u in units:
        where = f"{u['file']}:{u.get('id')}"
        if u["id"] in seen:
            errors.append(f"{where}: duplicate unit id")
        seen.add(u["id"])
        if u.get("tradition") not in tradition_ids:
            errors.append(f"{where}: unknown tradition {u.get('tradition')}")
        for q in u.get("quran") or []:      # hadith units: the verses they explain (tafsir, occasions)
            if not originals.quran_refs(str(q), quran_text):
                errors.append(f"{where}: quran link {q} does not resolve to a verse")
        read = set()
        if u.get("original"):
            for r in u.get("read") or []:
                found = unit_refs(u, r, quran_text, hebrew_text)
                if not found:
                    errors.append(f"{where}: read range {r} does not resolve")
                read |= set(found or [])
        for t in u["tags"]:
            if u.get("original"):
                for r in t["refs"]:
                    keys = unit_refs(u, r, quran_text, hebrew_text) or []
                    if not set(keys) <= read:
                        errors.append(f"{where}: tag {t['motif']} cites {r}, which is outside the unit's read ranges")
            if t["motif"] not in vocab:
                errors.append(f"{where}: unknown motif {t['motif']}")
            if u.get("original"):
                for r in t["refs"]:
                    if passage_for(u, r, quran_text, hebrew_text) is None:
                        errors.append(f"{where}: ref {r} does not resolve to an original verse")
    return errors


def unit_refs(u, r, quran_text, hebrew_text):
    """A unit's reference resolved against its own corpus: verse refs, or ANE line keys."""
    if u.get("corpus") == "quran":
        return originals.quran_refs(r, quran_text)
    if u.get("corpus") == "ane":
        keys = originals.ane_refs(r)
        return ["|".join(k) for k in keys] if keys else None
    if u.get("corpus") == "hadith":
        import hadith
        keys = hadith.hadith_refs(r)
        return ["|".join(k) for k in keys] if keys else None
    return originals.hebrew_refs(r, hebrew_text)


def passage_ref(u, r):
    if u.get("corpus") == "quran":
        return f"Quran {r}"
    if u.get("corpus") in ("hebrew-bible", "ane", "hadith"):
        return r
    return f"{u['title']}: {r}"


def passage_for(u, r, quran_text, hebrew_text):
    p = {"tradition": u["tradition"], "ref": passage_ref(u, r)}
    if not u.get("original"):
        return p
    return p if originals.original_for(p, quran_text, hebrew_text) else None


def weights(units):
    df = Counter(m for u in units for m in {t["motif"] for t in u["tags"]})
    n = len(units)
    return {m: math.log(n / c) for m, c in df.items()}, df


def internal_pair(a, b):
    """Two units from the same text, e.g. two Quran narratives echoing each other."""
    return a["tradition"] == b["tradition"] and a.get("original") and b.get("original") and a.get("corpus") == b.get("corpus")


def overlapping(a, b, keys):
    """Units of the same text whose read ranges overlap tag the same verses; pairing them is noise."""
    return bool(keys.get(a["id"], set()) & keys.get(b["id"], set()))


def pairs(units, w, df, keys=None):
    keys = keys or {}
    out = []
    for i, a in enumerate(units):
        ma = {t["motif"]: t for t in a["tags"]}
        for b in units[i + 1:]:
            if a["tradition"] == b["tradition"] and not internal_pair(a, b):
                continue
            if internal_pair(a, b) and overlapping(a, b, keys):
                continue
            mb = {t["motif"]: t for t in b["tags"]}
            shared = sorted(set(ma) & set(mb), key=lambda m: -w[m])
            # one shared motif is enough when no other unit has it: obscure links are often a single detail
            unique = len(shared) == 1 and df[shared[0]] == 2
            confirmed = frozenset((a["id"], b["id"])) in CONFIRMED
            if len(shared) < MIN_SHARED and not unique and not confirmed:
                continue
            out.append(dict(a=a["id"], b=b["id"], internal=bool(internal_pair(a, b)), confirmed=confirmed,
                            score=round(sum(w[m] for m in shared), 3),
                            shared=shared, only_a=sorted(set(ma) - set(mb)), only_b=sorted(set(mb) - set(ma))))
    return sorted(out, key=lambda p: -p["score"])


def top_for_unit(ps, uid):
    return [p for p in ps if uid in (p["a"], p["b"])][:TOP_PER_UNIT]


def check_benchmarks(ps):
    spec = yaml.safe_load((DATA / "benchmarks" / "motifs.yaml").read_text(encoding="utf-8"))
    results = []
    for b in spec["expectations"]:
        pair = {b["a"], b["b"]}
        hit = any({p["a"], p["b"]} == pair for p in top_for_unit(ps, b["a"]) + top_for_unit(ps, b["b"]))
        results.append({**b, "recovered": hit})
    return results


def write_report(units, vocab, w, df, ps, bench):
    by_id = {u["id"]: u for u in units}
    lines = ["# Motif track report", "",
             f"Generated {date.today().isoformat()} by `tools/motifs.py` from {len(units)} tagged units "
             f"and {len(w)} motifs in use.", "",
             "Weights: a motif found in fewer units counts for more (log N/df). The tags themselves "
             "are a reader's interpretation. Units marked *original* are tagged from the Arabic or Hebrew "
             "text in this repo; the others are tagged from secondary knowledge until their texts are added.", "",
             "Benchmarks check the matching machinery, not discovery: these parallels were known when the "
             "units were tagged.", "",
             "## Benchmarks", "", "| Expected pair | Recovered |", "|---|---|"]
    for b in bench:
        lines.append(f"| {by_id[b['a']]['title']} ↔ {by_id[b['b']]['title']} | {'yes' if b['recovered'] else '**no**'} |")
    lines += ["", "## Ranked pairs", "", "| Score | Pair | Shared motifs |", "|---|---|---|"]
    for p in ps:
        a, b = by_id[p["a"]], by_id[p["b"]]
        shared = ", ".join(f"{vocab[m]['label']} ({w[m]:.1f})" for m in p["shared"])
        lines.append(f"| {p['score']:.1f} | {a['title']} ↔ {b['title']} | {shared} |")
    lines += ["", "## Unmatched motifs: search targets", "",
              "Motifs found in only one unit. For units read from their original text, these are the details "
              "no other tagged text shares yet, so they are the places to look next (rabbinic, Syriac, "
              "apocryphal and other literature).", ""]
    for u in units:
        if not u.get("original"):
            continue
        lonely = [t for t in u["tags"] if df[t["motif"]] == 1]
        if lonely:
            lines.append(f"**{u['title']}**")
            lines += [f"- {vocab[t['motif']]['label']} ({', '.join(t['refs'])})" for t in lonely]
            lines.append("")
    hinted = [u for u in units if u.get("hints")]
    if hinted:
        lines += ["", "## Reader hints (from memory, not from the text)", "",
                  "Parallels the reader recalled while tagging. They are secondary and unverified: use them as "
                  "places to look, not as evidence.", ""]
        for u in hinted:
            lines.append(f"**{u['title']}** ({', '.join(u.get('read') or [])})")
            lines += [f"- {h}" for h in u["hints"]]
            lines.append("")
    lines += ["", "## Motif frequency", "", "| Motif | Units |", "|---|---|"]
    for m, c in sorted(df.items(), key=lambda x: (x[1], x[0])):
        lines.append(f"| {vocab[m]['label']} | {c} |")
    (OUT / "REPORT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


KIND_ORDER = ["divergence", "contrast", "response", "parallel", "echo", "shared"]
KIND_WORDS = {"divergence": "deliberately changed", "contrast": "opposite ruling", "response": "answers the other",
              "parallel": "same element", "echo": "shared wording", "shared": "shared motif"}
MAX_MATCHES = 12          # match rows per lead
REFS_PER_SIDE = 3


def plain_label(vocab, mid):
    return re.sub(r" \[[a-z]+ between the texts\]$", "", vocab[mid]["label"])


def side_passages(u, refs, quran_text, hebrew_text):
    out = [x for x in (passage_for(u, r, quran_text, hebrew_text) for r in refs[:REFS_PER_SIDE]) if x]
    originals.fill_passages(out, quran_text, hebrew_text)
    return [{k: v for k, v in x.items() if k in ("ref", "text", "lang", "text_omitted")} for x in out]


def build_matches(left, right, p, conf, vocab, w, quran_text, hebrew_text):
    """One row per correspondence: what kind it is, a plain label, the reader's note once, and each side's verses.
    Confirmed side-by-side matches come first; motifs the two reads merely share follow."""
    rows, covered = [], set()
    for x in sorted((conf or {}).get("matches", []), key=lambda x: KIND_ORDER.index(x["relation"])):
        covered |= {x["motif"], x["base"]}
        rows.append({"kind": x["relation"], "label": plain_label(vocab, x["base"] if x["base"] in vocab else x["motif"]),
                     "note": x["note"],
                     "sides": [{"tradition": u["tradition"], "passages": side_passages(u, x["refs"].get(u["id"], []), quran_text, hebrew_text)}
                               for u in (left, right)]})
    for m in p["shared"]:
        if len(rows) >= MAX_MATCHES:
            break
        if m in covered:
            continue
        sides = []
        for u in (left, right):
            t = next(t for t in u["tags"] if t["motif"] == m)
            sides.append({"tradition": u["tradition"], "passages": side_passages(u, t["refs"], quran_text, hebrew_text),
                          **({"note": t["note"]} if t.get("note") else {})})
        rows.append({"kind": "shared", "label": plain_label(vocab, m), "sides": sides})
    return rows


def lead_summary(matches, p):
    confirmed = [m for m in matches if m["kind"] != "shared"]
    if confirmed:
        counts = Counter(m["kind"] for m in confirmed)
        return (f"{len(confirmed)} correspondence{'s' if len(confirmed) > 1 else ''} read side by side: "
                + ", ".join(f"{n} {KIND_WORDS[k]}" for k, n in sorted(counts.items(), key=lambda kv: KIND_ORDER.index(kv[0]))) + ".")
    n = len(p["shared"])
    return f"{n} shared motif{'s' if n > 1 else ''}, found by the separate reads; not yet compared side by side."


def build_leads(units, vocab, w, ps, bench, quran_text, hebrew_text):
    by_id = {u["id"]: u for u in units}
    spec = yaml.safe_load((DATA / "benchmarks" / "motifs.yaml").read_text(encoding="utf-8"))
    groups = [set(v) for v in (spec.get("lead_units") or {}).values()]
    leads, internal = [], Counter()
    for p in ps:
        if any(p["a"] in g and p["b"] in g for g in groups):
            continue
        if not p.get("confirmed") and not any(w[m] >= 1.5 for m in p["shared"]):   # needs at least one fairly rare motif
            continue
        a, b = by_id[p["a"]], by_id[p["b"]]
        if p["internal"]:
            # cross-tradition pairs are the point; a fully read text echoes itself thousands of times
            internal[a["corpus"]] += 1
            if internal[a["corpus"]] > MAX_INTERNAL_LEADS:
                continue
        conf = CONFIRMED.get(frozenset((a["id"], b["id"])))
        # the reference tradition (Islam) reads on the right; otherwise keep pair order
        left, right = (b, a) if a["tradition"] == "islam" and b["tradition"] != "islam" else (a, b)
        matches = build_matches(left, right, p, conf, vocab, w, quran_text, hebrew_text)
        evidence = []
        evidence.append({"text": f"Shared motifs, rarest first: " + "; ".join(f"{vocab[m]['label']} (weight {w[m]:.1f})" for m in p["shared"])
                                 + f". Pair score {p['score']:.1f}.", "basis": "reading"})
        for u, only in ((a, p["only_a"]), (b, p["only_b"])):
            # divergences only mean something when both units are fully tagged from their texts
            if only and a.get("original") and b.get("original"):
                shown = sorted(only, key=lambda m: -w[m])[:MAX_ONLY]   # rarest first; the full lists are in results/motifs/pairs.json
                evidence.append({"text": f"Only in {u['title']}: " + "; ".join(vocab[m]["label"] for m in shown)
                                         + (f"; and {len(only) - len(shown)} more" if len(only) > len(shown) else "") + ".",
                                 "basis": "reading"})
        if conf:
            evidence.insert(0, {"text": f"Read side by side in both originals ({conf['file']}).", "basis": "reading"})
        for u in (a, b):
            evidence.append({"text": f"{u['title']}: tagged by {u['tagger']}.",
                             "basis": "reading" if u.get("original") else "scholarship"})
        traditions = list(dict.fromkeys([a["tradition"], b["tradition"]]))
        leads.append({
            "id": f"motif-{a['id']}-vs-{b['id']}",
            "title": f"{a['title']} ↔ {b['title']}",
            "summary": lead_summary(matches, p),
            "finding": matches[0]["label"] if matches else "",
            "kinds": list(dict.fromkeys(m["kind"] for m in matches)),
            "units": [{"id": u["id"], "title": u["title"], "tradition": u["tradition"]} for u in (left, right)],
            "matches": matches,
            "status": "new",
            "relations": (["internal"] if p["internal"] else
                          sorted({"response" if r in ("divergence", "response", "contrast") else "convergence" for r in conf["relations"]}
                                 | ({"transmission"} if "parallel" in conf["relations"] else set())) if conf else
                          ["transmission", "convergence"]),
            "standing": "proposed",
            "traditions": traditions, "layers": ["motif"], "motifs": p["shared"],
            "passages": [], "evidence": evidence, "origin": "pipeline", "added": date.today().isoformat(),
        })
    return leads


def read_keys(units, quran_text, hebrew_text):
    keys = {}
    for u in units:
        if u.get("original"):
            ks = set()
            for r in u.get("read") or []:
                found = unit_refs(u, r, quran_text, hebrew_text)
                ks |= {f"{u.get('corpus')}:{k}" for k in found or []}
            keys[u["id"]] = ks
    return keys


def validate_file(path):
    """Check one tag file against the shared vocabulary (for reader agents)."""
    vocab, units = load(strict=False)
    path = pathlib.Path(path).resolve()
    rel = str(path.relative_to(DATA / "motif-tags"))
    mine = [u for u in units if u["file"] == rel]
    quran_text, hebrew_text = originals.load_quran_text(), originals.load_hebrew_text()
    errors = validate(vocab, mine, quran_text, hebrew_text)
    ids = {}
    for u in units:
        ids.setdefault(u["id"], []).append(u["file"])
    errors += [f"{rel}: unit id {uid} also used in {[f for f in fs if f != rel]}"
               for uid, fs in ids.items() if rel in fs and len(fs) > 1]
    covered = set().union(*read_keys(mine, quran_text, hebrew_text).values()) if mine else set()
    m = re.match(r"(hb|quran|ane|hadith)/(\d+)-", rel)
    if m:   # a full-read chunk file may only hold units inside its own chunk
        if m.group(1) == "hadith":
            import hadith
            want = hadith.chunk_pages(int(m.group(2)))
            allowed = {"hadith:" + "|".join(k) for k in hadith.corpus().keys.get(hadith.SIGLUM, [])
                       if int(k[2].split(".")[0]) in want}
        elif m.group(1) == "ane":
            import aneread
            allowed = {"ane:" + "|".join(k) for k in aneread.chunk_keys(int(m.group(2)))}
        elif m.group(1) == "hb":
            import hbread
            chunk = hbread.plan(hebrew_text)[int(m.group(2)) - 1]
            allowed = {f"hebrew-bible:{r}" for _, _, refs in chunk for r in refs}
        else:
            import qread
            chunk = qread.plan(quran_text)[int(m.group(2)) - 1]
            allowed = {f"quran:{r}" for _, refs in chunk for r in refs}
        for u in mine:
            outside = read_keys([u], quran_text, hebrew_text)[u["id"]] - allowed
            if outside:
                errors.append(f"{rel}: unit {u['id']} reads verses outside chunk {m.group(2)} "
                              f"(e.g. {sorted(outside)[0].split(':', 1)[1]}); it belongs to another reader's file")
        missing = allowed - covered
        if missing:
            errors.append(f"{rel}: {len(missing)} verses of chunk {m.group(2)} not yet in any unit's read ranges "
                          f"(e.g. {sorted(missing)[0].split(':', 1)[1]})")
    print(f"{rel}: {len(mine)} units, {sum(len(u['tags']) for u in mine)} tags, {len(covered)} verses read")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        sys.exit(1)
    print("ok")


def main():
    if "-h" in sys.argv or "--help" in sys.argv:
        print(__doc__)
        return
    if "--validate" in sys.argv:
        validate_file(sys.argv[sys.argv.index("--validate") + 1])
        return
    vocab, units = load()
    quran_text, hebrew_text = originals.load_quran_text(), originals.load_hebrew_text()
    errors = validate(vocab, units, quran_text, hebrew_text)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        sys.exit(1)
    w, df = weights(units)
    ps = pairs(units, w, df, read_keys(units, quran_text, hebrew_text))
    bench = check_benchmarks(ps)
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "pairs.json").write_text(json.dumps(dict(weights=w, pairs=ps), ensure_ascii=False, indent=1), encoding="utf-8")
    write_report(units, vocab, w, df, ps, bench)
    print(f"{len(units)} units, {len(ps)} pairs")
    for b in bench:
        print(("  recovered " if b["recovered"] else "  MISSED    ") + f"{b['a']} <-> {b['b']}")
    if "--write-leads" in sys.argv:
        leads = build_leads(units, vocab, w, ps, bench, quran_text, hebrew_text)
        for lead in leads:
            print(f"  lead {lead['id']}: {lexical.write_lead(lead)}")
        lexical.flag_stale({lead["id"] for lead in leads}, ("motif-",))
    print("wrote results/motifs/")
    if any(not b["recovered"] for b in bench):
        sys.exit("benchmark expectations missed")


if __name__ == "__main__":
    main()
