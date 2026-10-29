"""Motif track: compare story units across traditions by shared motifs.

Usage: python3 tools/motifs.py [--write-leads]

Units and their verse-anchored motif tags live in data/motif-tags/*.yaml;
the vocabulary is data/motifs.yaml. Each motif is weighted by how rare it is
across units (log N/df), so a shared rare motif counts for more than a shared
common one. Pairs of units from different traditions are ranked by the summed
weight of their shared motifs.

Writes results/motifs/pairs.json and results/motifs/REPORT.md, checks
data/benchmarks/motifs.yaml, and with --write-leads creates or refreshes
pipeline leads in leads/.
"""
import json
import math
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


def load():
    vocab = yaml.safe_load((DATA / "motifs.yaml").read_text(encoding="utf-8"))["motifs"]
    units = []
    for path in sorted((DATA / "motif-tags").glob("*.yaml")):
        for u in yaml.safe_load(path.read_text(encoding="utf-8"))["units"]:
            u["file"] = path.name
            units.append(u)
    return vocab, units


def validate(vocab, units, quran_text, hebrew_text):
    errors, seen = [], set()
    tradition_ids = {t["id"] for t in yaml.safe_load((DATA / "traditions.yaml").read_text(encoding="utf-8"))["traditions"]}
    for u in units:
        where = f"{u['file']}:{u.get('id')}"
        if u["id"] in seen:
            errors.append(f"{where}: duplicate unit id")
        seen.add(u["id"])
        if u.get("tradition") not in tradition_ids:
            errors.append(f"{where}: unknown tradition {u.get('tradition')}")
        read = set()
        if u.get("original"):
            for r in u.get("read") or []:
                found = (originals.quran_refs(r, quran_text) if u.get("corpus") == "quran"
                         else originals.hebrew_refs(r, hebrew_text))
                if not found:
                    errors.append(f"{where}: read range {r} does not resolve")
                read |= set(found or [])
        for t in u["tags"]:
            if u.get("original"):
                for r in t["refs"]:
                    keys = (originals.quran_refs(r, quran_text) if u.get("corpus") == "quran"
                            else originals.hebrew_refs(r, hebrew_text)) or []
                    if not set(keys) <= read:
                        errors.append(f"{where}: tag {t['motif']} cites {r}, which is outside the unit's read ranges")
            if t["motif"] not in vocab:
                errors.append(f"{where}: unknown motif {t['motif']}")
            if u.get("original"):
                for r in t["refs"]:
                    if passage_for(u, r, quran_text, hebrew_text) is None:
                        errors.append(f"{where}: ref {r} does not resolve to an original verse")
    return errors


def passage_ref(u, r):
    if u.get("corpus") == "quran":
        return f"Quran {r}"
    if u.get("corpus") == "hebrew-bible":
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


def pairs(units, w):
    out = []
    for i, a in enumerate(units):
        ma = {t["motif"]: t for t in a["tags"]}
        for b in units[i + 1:]:
            if a["tradition"] == b["tradition"]:
                continue
            mb = {t["motif"]: t for t in b["tags"]}
            shared = sorted(set(ma) & set(mb), key=lambda m: -w[m])
            if len(shared) < MIN_SHARED:
                continue
            out.append(dict(a=a["id"], b=b["id"], score=round(sum(w[m] for m in shared), 3),
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
    lines += ["", "## Motif frequency", "", "| Motif | Units |", "|---|---|"]
    for m, c in sorted(df.items(), key=lambda x: (x[1], x[0])):
        lines.append(f"| {vocab[m]['label']} | {c} |")
    (OUT / "REPORT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_leads(units, vocab, w, ps, bench, quran_text, hebrew_text):
    by_id = {u["id"]: u for u in units}
    spec = yaml.safe_load((DATA / "benchmarks" / "motifs.yaml").read_text(encoding="utf-8"))
    groups = [set(v) for v in (spec.get("lead_units") or {}).values()]
    leads = []
    for p in ps:
        if any(p["a"] in g and p["b"] in g for g in groups):
            continue
        if not any(w[m] >= 1.5 for m in p["shared"]):   # needs at least one fairly rare motif
            continue
        a, b = by_id[p["a"]], by_id[p["b"]]
        passages, evidence = [], []
        for m in p["shared"]:
            for u in (a, b):
                t = next(t for t in u["tags"] if t["motif"] == m)
                for r in t["refs"][:3]:
                    psg = passage_for(u, r, quran_text, hebrew_text)
                    psg["note"] = vocab[m]["label"] + (f" ({t['note']})" if t.get("note") else "")
                    passages.append(psg)
        originals.fill_passages(passages, quran_text, hebrew_text)
        evidence.append({"text": f"Shared motifs, rarest first: " + "; ".join(f"{vocab[m]['label']} (weight {w[m]:.1f})" for m in p["shared"])
                                 + f". Pair score {p['score']:.1f}.", "basis": "reading"})
        for u, only in ((a, p["only_a"]), (b, p["only_b"])):
            # divergences only mean something when both units are fully tagged from their texts
            if only and a.get("original") and b.get("original"):
                evidence.append({"text": f"Only in {u['title']}: " + "; ".join(vocab[m]["label"] for m in only) + ".",
                                 "basis": "reading"})
        for u in (a, b):
            evidence.append({"text": f"{u['title']}: tagged by {u['tagger']}.",
                             "basis": "reading" if u.get("original") else "scholarship"})
        traditions = list(dict.fromkeys([a["tradition"], b["tradition"]]))
        leads.append({
            "id": f"motif-{a['id']}-vs-{b['id']}",
            "title": f"{a['title']} ↔ {b['title']}",
            "summary": f"These two units share {len(p['shared'])} motifs: "
                       + ", ".join(vocab[m]["label"].lower() for m in p["shared"][:4])
                       + ("…" if len(p["shared"]) > 4 else "") + ".",
            "status": "new", "relations": ["transmission", "convergence"], "standing": "proposed",
            "traditions": traditions, "layers": ["motif"], "motifs": p["shared"],
            "passages": passages, "evidence": evidence, "origin": "pipeline", "added": date.today().isoformat(),
        })
    return leads


def main():
    vocab, units = load()
    quran_text, hebrew_text = originals.load_quran_text(), originals.load_hebrew_text()
    errors = validate(vocab, units, quran_text, hebrew_text)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        sys.exit(1)
    w, df = weights(units)
    ps = pairs(units, w)
    bench = check_benchmarks(ps)
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "pairs.json").write_text(json.dumps(dict(weights=w, pairs=ps), ensure_ascii=False, indent=1), encoding="utf-8")
    write_report(units, vocab, w, df, ps, bench)
    print(f"{len(units)} units, {len(ps)} pairs")
    for b in bench:
        print(("  recovered " if b["recovered"] else "  MISSED    ") + f"{b['a']} <-> {b['b']}")
    if "--write-leads" in sys.argv:
        for lead in build_leads(units, vocab, w, ps, bench, quran_text, hebrew_text):
            print(f"  lead {lead['id']}: {lexical.write_lead(lead)}")
    print("wrote results/motifs/")
    if any(not b["recovered"] for b in bench):
        sys.exit("benchmark expectations missed")


if __name__ == "__main__":
    main()
