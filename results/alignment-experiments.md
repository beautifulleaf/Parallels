# Alignment experiments (2026-10-29)

**Question:** can Quran passages be automatically aligned with the matching
Hebrew Bible stories using only the original texts? A method that worked
would serve as a discovery engine for the motif track.

**Test:** each Quran verse in a story shared by both corpora (12 stories,
from `data/narratives/`) is matched to its most similar Hebrew Bible verse.
Two scores:
- **top1:** the share of Quran verses whose nearest Hebrew verse is in the
  same story. The `base` column is the chance rate.
- **narrative level:** for each story, the average Quran embedding is matched
  to the nearest average Hebrew story embedding.

Text was unvocalized Arabic (Uthmani with diacritics removed) and unpointed
Hebrew.

| Method | Narrative-level accuracy | Typical verse top1 |
|---|---|---|
| LaBSE (sentence-transformers) | 4 / 12 | 0.0–0.2 (Joseph 0.21, Moses 0.19) |
| multilingual-e5-base | 0 / 12 (most stories map to Ruth) | 0.0–0.4, unstable |
| Shared cognate roots (TF-IDF over sound-correspondence matches) | 0 / 12 | ≈ chance |
| Same, gloss-checked cognates only | 0 / 12 | ≈ chance |

**Conclusion:** none of these is reliable enough to find parallels.

- The sentence models were trained on modern languages. Quranic Arabic and
  Biblical Hebrew are far from that, and their scores sit only a few times
  above chance.
- Sound-correspondence cognates are too noisy at the scale of whole verses.

The motif track therefore uses explicit, verse-anchored tags. These could be
revisited with models trained on classical Arabic and Biblical Hebrew, or
with verse-aligned translations used as a bridge. Any such method must
report results on this same test before it is used.

The scripts are in `results/experiments/` and need `torch` and
`sentence-transformers`, which are not part of the core pipeline.
