"""Experiment: align Quran and Hebrew Bible verses through shared cognate roots (TF-IDF over cognate classes)."""
import sys, math
from collections import defaultdict, Counter
import numpy as np
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parents[2] / "tools"))
import corpora, lexical

STRICT = "--strict" in sys.argv   # require gloss match
q, h = corpora.load_quran(), corpora.load_hebrew_bible()
h_occ = defaultdict(set)
for i, v in enumerate(h.verses):
    for l in v.lemmas:
        h_occ[l].add(i)
index = lexical.hebrew_index(h, h_occ)

# map each Quran lemma to a cognate class = sorted tuple of Hebrew lemma ids
qmap = {}
for lid, lem in q.lemmas.items():
    cogs = lexical.cognates(lem, index, h, h_occ)
    if STRICT:
        cogs = lexical.matched(cogs)
    else:
        cogs = lexical.matched(cogs) or cogs[:1]
    if cogs:
        qmap[lid] = [c["lemma"] for c in cogs[:2]]
print("Quran lemmas with a cognate:", len(qmap), "of", len(q.lemmas))

# features live in Hebrew-lemma space
feats = sorted({x for v in qmap.values() for x in v})
fi = {f: i for i, f in enumerate(feats)}
df = Counter()
for v in h.verses:
    for l in set(v.lemmas):
        if l in fi:
            df[l] += 1
N = len(h.verses)
idf = np.array([math.log((N + 1) / (df[f] + 1)) + 1 for f in feats])

def vec_q(v):
    x = np.zeros(len(feats))
    for l in v.lemmas:
        for f in qmap.get(l, []):
            x[fi[f]] = 1
    return x * idf

def vec_h(v):
    x = np.zeros(len(feats))
    for l in v.lemmas:
        if l in fi:
            x[fi[l]] = 1
    return x * idf

Q = np.array([vec_q(v) for v in q.verses]); H = np.array([vec_h(v) for v in h.verses])
Q /= np.linalg.norm(Q, axis=1, keepdims=True) + 1e-9; H /= np.linalg.norm(H, axis=1, keepdims=True) + 1e-9
q_lab = [v.narratives for v in q.verses]; h_lab = [v.narratives for v in h.verses]
shared = sorted(set(q.narratives) & set(h.narratives))
S = Q @ H.T
for n in shared:
    qi = [i for i, l in enumerate(q_lab) if n in l]
    base = sum(1 for l in h_lab if n in l) / len(h_lab)
    top = S[qi].argmax(1)
    acc = np.mean([n in h_lab[j] for j in top])
    print(f"  {n:12s} verses={len(qi):4d} top1={acc:.2f} base={base:.3f} lift={acc/max(base,1e-9):.1f}")

def centroid(E, lab, n):
    idx = [i for i, l in enumerate(lab) if n in l]
    c = E[idx].mean(0); return c / (np.linalg.norm(c) + 1e-9)
hc = {n: centroid(H, h_lab, n) for n in h.narratives}
correct = 0
for n in shared:
    c = centroid(Q, q_lab, n)
    ranked = sorted(hc, key=lambda k: -float(c @ hc[k]))
    correct += ranked[0] == n
    print(f"  centroid {n:12s} -> {ranked[0]} (rank of true: {ranked.index(n)+1})")
print(f"narrative-level accuracy: {correct}/{len(shared)}")
