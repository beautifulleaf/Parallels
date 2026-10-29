"""Experiment: can a multilingual encoder align Quran and Hebrew Bible stories from the originals?"""
import sys, re, unicodedata, time, json, pathlib
import numpy as np
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parents[2] / "tools"))
import corpora, originals
from sentence_transformers import SentenceTransformer

MODEL = sys.argv[1] if len(sys.argv) > 1 else "sentence-transformers/LaBSE"
OUT = pathlib.Path(__file__).resolve().parent / "embeddings"
OUT.mkdir(exist_ok=True)

def plain_ar(s):
    s = s.replace("ٱ", "ا")
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if not unicodedata.combining(c) and not ("ۖ" <= c <= "ۭ"))
    return re.sub(r"\s+", " ", s).strip()

def plain_he(s):
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.replace("־", " ")  # maqaf
    return re.sub(r"[^א-ת ]", "", s).strip()

q, h = corpora.load_quran(), corpora.load_hebrew_bible()
qt, ht = originals.load_quran_text(), originals.load_hebrew_text()
q_refs = [v.ref for v in q.verses]; h_refs = [v.ref for v in h.verses]
q_lab = [v.narratives for v in q.verses]; h_lab = [v.narratives for v in h.verses]

tag = MODEL.split("/")[-1]
m = SentenceTransformer(MODEL, device="cpu")
prefix = "query: " if "e5" in MODEL else ""
t = time.time()
qe_path, he_path = OUT / f"{tag}-quran.npy", OUT / f"{tag}-hebrew.npy"
if qe_path.exists():
    qe, he = np.load(qe_path), np.load(he_path)
else:
    qe = m.encode([prefix + plain_ar(qt[r]) for r in q_refs], batch_size=64, normalize_embeddings=True, show_progress_bar=False)
    he = m.encode([prefix + plain_he(ht[r]) for r in h_refs], batch_size=64, normalize_embeddings=True, show_progress_bar=False)
    np.save(qe_path, qe); np.save(he_path, he)
print(f"{tag}: encoded in {time.time()-t:.0f}s")

shared = sorted(set(q.narratives) & set(h.narratives))
sims = qe @ he.T
# verse-level: top-1 Hebrew verse lands in the same narrative?
res = {}
for n in shared:
    qi = [i for i, l in enumerate(q_lab) if n in l]
    base = sum(1 for l in h_lab if n in l) / len(h_lab)
    top = sims[qi].argmax(1)
    acc = np.mean([n in h_lab[j] for j in top])
    top10 = np.argsort(-sims[qi], 1)[:, :10]
    acc10 = np.mean([[n in h_lab[j] for j in row] for row in top10])
    res[n] = (len(qi), round(float(acc), 3), round(float(acc10), 3), round(base, 3))
for n, r in res.items():
    print(f"  {n:12s} verses={r[0]:4d} top1={r[1]:.2f} top10share={r[2]:.2f} base={r[3]:.3f} lift={r[1]/max(r[3],1e-9):.1f}")

# narrative-level: mean embedding per narrative, nearest Hebrew narrative
def centroid(E, lab, n):
    idx = [i for i, l in enumerate(lab) if n in l]
    c = E[idx].mean(0); return c / np.linalg.norm(c)
hc = {n: centroid(he, h_lab, n) for n in h.narratives}
correct = 0
for n in shared:
    c = centroid(qe, q_lab, n)
    best = max(hc, key=lambda k: float(c @ hc[k]))
    correct += best == n
    print(f"  centroid {n:12s} -> {best}")
print(f"narrative-level accuracy: {correct}/{len(shared)}")
