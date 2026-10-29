"""Side-by-side comparison pass between two fully read texts.

Separate full reads only match where two readers chose the same motif id. This
pass takes each unit of one text, proposes candidate partners in the other,
and a reader compares the originals side by side and records what really
corresponds (data/alignments/<pair>/NN.yaml, see data/alignments/README.md).

Usage:
  python3 tools/compare.py candidates            # write data/alignments/hb-quran/candidates.yaml
  python3 tools/compare.py plan                  # list the comparison chunks
  python3 tools/compare.py show <chunk>          # the units of a chunk and their candidates
  python3 tools/compare.py unit <unit id>        # a unit's tags (label, refs) and hints
  python3 tools/compare.py text <unit id>        # the original text of a unit's read ranges
  python3 tools/compare.py find <words...>       # Hebrew Bible units with a motif whose id or label has all words
  python3 tools/compare.py validate <file>       # check a comparison file

Candidates for a Quran unit come from three sources, all recorded with the
reason: Hebrew Bible passages its reader cited in hints, units it already
shares one or two motifs with, and the units most similar by their motif
labels (a weak signal, used only to propose). Every Quran unit is included:
units the motif track already pairs strongly are where the deliberate
divergences are, and those are recorded too.
"""
import pathlib
import re
import sys
from collections import Counter

import yaml

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import motifs  # noqa: E402
import originals  # noqa: E402

DATA = motifs.DATA
PAIR_DIR = DATA / "alignments" / "hb-quran"
CANDIDATES = PAIR_DIR / "candidates.yaml"
MAX_CANDIDATES = 6
SIMILAR = 3           # embedding neighbours proposed per unit
CHUNKS = 8
RELATIONS = ("parallel", "echo", "divergence", "response", "contrast")
# 'Gen 18', 'Exod 22:4', '1 Sam 1:13', 'Psalm 37:29', 'Jonah 1-4' inside free-text hints
HINT_REF = re.compile(r"\b((?:[123] ?)?(?:" + "|".join(sorted((re.escape(k) for k in originals.HEBREW_BOOKS),
                                                                key=len, reverse=True))
                      + r"))\.? (\d+)(?::(\d+))?(?:[–-](\d+)(?::(\d+))?)?")


def hb_and_quran(units):
    hb = [u for u in units if u["file"].startswith("hb/")]
    qu = [u for u in units if u["file"].startswith("quran/")]
    return hb, qu


def verse_index(hb, hebrew_text):
    keys = motifs.read_keys(hb, {}, hebrew_text)
    index = {}
    for uid, ks in keys.items():
        for k in ks:
            index.setdefault(k.split(":", 1)[1], []).append(uid)
    return index


def hint_targets(u, index, hebrew_text):
    out = []
    for h in u.get("hints") or []:
        for m in HINT_REF.finditer(h):
            book = m.group(1).replace(".", "")
            spec = f"{book} {m.group(2)}" + (f":{m.group(3)}" if m.group(3) else "")
            if m.group(4):
                spec += f"-{m.group(4)}" + (f":{m.group(5)}" if m.group(5) else "")
            for ref in (originals.hebrew_refs(spec, hebrew_text) or [])[:40]:
                for uid in index.get(ref, []):
                    if uid not in out:
                        out.append(uid)
    return out


def candidates():
    import numpy as np
    from sentence_transformers import SentenceTransformer
    vocab, units = motifs.load()
    hb, qu = hb_and_quran(units)
    hebrew_text = originals.load_hebrew_text()
    index = verse_index(hb, hebrew_text)
    hb_motifs = {u["id"]: {t["motif"] for t in u["tags"]} for u in hb}
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2", device="cpu")

    def vec(u):
        e = model.encode([vocab[t["motif"]]["label"] for t in u["tags"]], normalize_embeddings=True, show_progress_bar=False)
        v = e.mean(0)
        return v / np.linalg.norm(v)
    H = np.stack([vec(u) for u in hb])
    out = []
    for q in qu:
        mine = {t["motif"] for t in q["tags"]}
        shared = sorted(((len(mine & ms), uid) for uid, ms in hb_motifs.items() if mine & ms), reverse=True)
        cands = {}
        for uid in hint_targets(q, index, hebrew_text):
            cands.setdefault(uid, []).append("hint")
        for n, uid in shared[:3]:
            cands.setdefault(uid, []).append(f"shares {n}")
        sims = H @ vec(q)
        for j in np.argsort(-sims)[:SIMILAR]:
            cands.setdefault(hb[j]["id"], []).append(f"similar {sims[j]:.2f}")
        ranked = sorted(cands.items(), key=lambda kv: ("hint" not in kv[1], not any(r.startswith("shares") for r in kv[1])))
        out.append({"unit": q["id"], "candidates": [{"with": uid, "why": why} for uid, why in ranked[:MAX_CANDIDATES]]})
    # chunks of about equal candidate count, keeping Quran order
    total = sum(len(o["candidates"]) for o in out)
    chunk, n = 1, 0
    for o in out:
        if n >= total / CHUNKS * chunk and chunk < CHUNKS:
            chunk += 1
        o["chunk"] = chunk
        n += len(o["candidates"])
    PAIR_DIR.mkdir(parents=True, exist_ok=True)
    CANDIDATES.write_text(yaml.safe_dump({"note": "Candidates for" + __doc__.split("Candidates for", 1)[1].rstrip(),
                                          "units": out}, allow_unicode=True, sort_keys=False, width=100), encoding="utf-8")
    print(f"{len(out)} of {len(qu)} Quran units need comparison; {total} candidate pairs in {CHUNKS} chunks")
    print(Counter(w.split()[0] for o in out for c in o["candidates"] for w in c["why"]))


def plan_units():
    return yaml.safe_load(CANDIDATES.read_text(encoding="utf-8"))["units"]


def show_unit(uid, vocab, by_id):
    u = by_id[uid]
    print(f"# {u['id']}: {u['title']}  (read {', '.join(u.get('read') or [])})")
    for t in u["tags"]:
        print(f"  {t['motif']}: {vocab[t['motif']]['label']}  [{', '.join(t['refs'])}]"
              + (f"  — {t['note']}" if t.get("note") else ""))
    for h in u.get("hints") or []:
        print(f"  hint: {h}")


def show_text(u):
    if u.get("corpus") == "quran":
        text = originals.load_quran_text()
        for r in u["read"]:
            for ref in originals.quran_refs(r, text):
                print(f"{ref} {text[ref]}")
    else:
        import hbread
        text = originals.load_hebrew_text()
        for r in u["read"]:
            for ref in originals.hebrew_refs(r, text):
                b, c, v = ref.split(".")
                print(f"{b} {c}:{v} {hbread.CANTILLATION.sub('', text[ref])}")


def validate(path):
    vocab, units = motifs.load(strict=False)
    path = pathlib.Path(path).resolve()
    rel = str(path.relative_to(DATA))
    m = re.match(r"alignments/hb-quran/(\d+)-", rel)
    errors = [e for e in motifs.ALIGN_ERRORS if e.startswith(rel)]
    doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    touched = {r["unit"] for r in doc.get("reviewed") or []} | {x["with"] for r in doc.get("reviewed") or []
                                                                 for x in r.get("matches") or []}
    by_id = {u["id"]: u for u in units}
    mine = [by_id[i] for i in touched if i in by_id]
    errors += [e for e in motifs.validate(vocab, mine, originals.load_quran_text(), originals.load_hebrew_text())
               if "unknown motif" in e or "outside the unit" in e or "does not resolve" in e]
    if m:
        assigned = {o["unit"]: {c["with"] for c in o["candidates"]} for o in plan_units() if o["chunk"] == int(m.group(1))}
        done = {r["unit"]: r for r in doc.get("reviewed") or []}
        for uid, cands in assigned.items():
            if uid not in done:
                errors.append(f"{rel}: unit {uid} of chunk {m.group(1)} not yet reviewed")
                continue
            missing = cands - set(done[uid].get("checked") or [])
            if missing:
                errors.append(f"{rel}: {uid}: candidates not listed under checked: {sorted(missing)}")
        for uid in done:
            if uid not in assigned:
                errors.append(f"{rel}: unit {uid} is not in chunk {m.group(1)}")
    for r in doc.get("reviewed") or []:
        for x in r.get("matches") or []:
            if x.get("relation") not in RELATIONS:
                errors.append(f"{rel}: {r['unit']} ~ {x.get('with')}: relation must be one of {', '.join(RELATIONS)}")
    n = sum(len(r.get("matches") or []) for r in doc.get("reviewed") or [])
    print(f"{rel}: {len(doc.get('reviewed') or [])} units reviewed, {n} matches")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        sys.exit(1)
    print("ok")


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "plan"
    if cmd == "candidates":
        return candidates()
    if cmd == "validate":
        return validate(sys.argv[2])
    if cmd == "plan":
        c = Counter()
        for o in plan_units():
            c[o["chunk"]] += 1
        for o in sorted(c):
            n = sum(len(x["candidates"]) for x in plan_units() if x["chunk"] == o)
            print(f"{o:2d}  {c[o]:3d} Quran units  {n:4d} candidate pairs")
        return
    vocab, units = motifs.load(strict=False)
    by_id = {u["id"]: u for u in units}
    if cmd == "show":
        for o in plan_units():
            if o["chunk"] == int(sys.argv[2]):
                print(f"{o['unit']}: {by_id[o['unit']]['title']}")
                for c in o["candidates"]:
                    print(f"    {c['with']}: {by_id[c['with']]['title']}  ({', '.join(c['why'])})")
    elif cmd == "unit":
        show_unit(sys.argv[2], vocab, by_id)
    elif cmd == "text":
        show_text(by_id[sys.argv[2]])
    elif cmd == "find":
        words = [w.lower() for w in sys.argv[2:]]
        for u in units:
            if not u["file"].startswith("hb/"):
                continue
            hits = [t for t in u["tags"] if all(w in f"{t['motif']} {vocab[t['motif']]['label']}".lower() for w in words)]
            for t in hits:
                print(f"{u['id']}: {t['motif']} [{', '.join(t['refs'])}] {vocab[t['motif']]['label']}")
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
