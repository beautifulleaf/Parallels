"""Observation records, one per narrative or ritual detail (data/records/README.md).

Usage: python3 tools/records.py --validate data/records/<corpus>/NN-<slug>.yaml

A record file holds `records:`, each with an `id` (neutral: corpus, ref, a word), the `ref` of the
passage in its corpus, the `unit` of the motif-tag file that contains it, and any of the slots. A slot
holds one value or a list of values from the text. For a chunk file of a full read, every ref must lie
inside the chunk.
"""
import pathlib
import re
import sys

import yaml

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import motifs  # noqa: E402
import originals  # noqa: E402

SLOTS = ("agent", "action", "object", "recipient", "instrument", "place", "time", "number", "name", "quoted",
         "outcome")
FIELDS = {"id", "ref", "unit", "note"} | set(SLOTS)


def resolve(corpus, ref, quran_text):
    if corpus == "hadith":
        import hadith
        return ["|".join(k) for k in hadith.hadith_refs(ref) or []]
    if corpus == "quran":
        return originals.quran_refs(ref, quran_text) or []
    if corpus == "ane":
        return ["|".join(k) for k in originals.ane_refs(ref) or []]
    return []


def validate(path):
    path = pathlib.Path(path).resolve()
    rel = str(path.relative_to(motifs.DATA / "records"))
    corpus = rel.split("/")[0]
    doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    _, units = motifs.load(strict=False)
    by_id = {u["id"]: u for u in units}
    quran_text = originals.load_quran_text()
    errors, ids = [], set()
    chunk_keys = None
    m = re.match(r"hadith/(\d+)-", rel)
    if m:
        import hadith
        want = hadith.chunk_pages(int(m.group(1)))
        chunk_keys = {"|".join(k) for k in hadith.corpus().keys.get(hadith.SIGLUM, [])
                      if int(k[2].split(".")[0]) in want}
    for i, r in enumerate(doc.get("records") or []):
        where = f"{rel}: record {r.get('id', i)}"
        extra = set(r) - FIELDS
        if extra:
            errors.append(f"{where}: unknown fields {sorted(extra)} (slots: {', '.join(SLOTS)})")
        if not r.get("id"):
            errors.append(f"{where}: missing id")
        elif r["id"] in ids:
            errors.append(f"{where}: duplicate id")
        ids.add(r.get("id"))
        keys = resolve(corpus, str(r.get("ref", "")), quran_text)
        if not keys:
            errors.append(f"{where}: ref {r.get('ref')!r} does not resolve in the {corpus} corpus")
        elif chunk_keys is not None and not set(keys) <= chunk_keys:
            errors.append(f"{where}: ref {r['ref']} lies outside chunk {m.group(1)}")
        u = by_id.get(r.get("unit"))
        if u is None:
            errors.append(f"{where}: unit {r.get('unit')!r} not found in data/motif-tags/")
        elif keys:
            read = set()
            for rr in u.get("read") or []:
                read |= set(motifs.unit_refs(u, rr, quran_text, {}) or [])
            if not set(keys) <= read:
                errors.append(f"{where}: ref {r['ref']} is outside unit {u['id']}'s read ranges")
        if not any(r.get(s) for s in SLOTS):
            errors.append(f"{where}: no slot filled")
        for s in SLOTS:
            v = r.get(s)
            if v is not None and not isinstance(v, (str, int, float, list)):
                errors.append(f"{where}: slot {s} must be a value or a list of values")
    print(f"{rel}: {len(doc.get('records') or [])} records")
    if errors:
        print("\n".join(errors[:60]), file=sys.stderr)
        sys.exit(1)
    print("ok")


if __name__ == "__main__":
    if "--validate" in sys.argv:
        validate(sys.argv[sys.argv.index("--validate") + 1])
    else:
        sys.exit(__doc__)
