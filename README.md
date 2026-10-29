# Parallels

A lead-generation engine for parallels, convergences, and responses across
religious and philosophical traditions. It surfaces candidates, and humans
investigate them.

- [PLAN.md](PLAN.md): scope, relation types, architecture, phases
- [TRADITIONS.md](TRADITIONS.md): an outline for each tradition
- [leads/](leads/): one file per lead, with review status and notes ([format](leads/README.md))
- [data/traditions.yaml](data/traditions.yaml): the tradition taxonomy

## Build

```bash
pip install pyyaml
python3 tools/fetch.py                  # download corpora into data/raw/ (not committed)
python3 tools/lexical.py --write-leads  # lexical track: results/lexical/ + pipeline leads
python3 tools/motifs.py --write-leads   # motif track: results/motifs/ + pipeline leads
python3 tools/originals.py              # fill lead passages with original Arabic/Hebrew text
python3 tools/linguistic.py             # phrases, doublets, rare words, loanword candidates
python3 tools/coverage.py               # results/COVERAGE.md: what has been scanned and read
python3 tools/build.py                  # validate leads, regenerate site/index.html
```

`tools/build.py --check` validates without regenerating. `tools/lexical.py` exits
with an error if it misses a benchmark it is expected to recover
(`data/benchmarks/lexical.yaml`).

## Lexical track (v1)

- **Corpora:** Quranic Arabic Corpus morphology, with quran.com word-by-word
  glosses; Open Scriptures Hebrew Bible, with Strong's dictionary. The
  Aramaic sections are left out of the Hebrew statistics.
- **Narratives:** hand-drawn verse ranges per story in `data/narratives/`.
  They're drafts, and refining them improves every result.
- **Concentration:** lemmas whose verses cluster in one narrative across
  several surahs or chapters (hypergeometric test, Benjamini–Hochberg
  corrected).
- **Synonym skew:** a concentrated lemma with a more common same-gloss
  sibling used elsewhere.
- **Bridges:** rare lemmas found almost only inside exactly two narratives.
- **Cognates:** Arabic roots mapped to Hebrew by regular sound
  correspondence. They're kept only when the Strong's definition shares the
  Arabic gloss word, except for rootless (likely loanword) lemmas, which are
  also shown as sound-only matches.
- **Output:** see [results/lexical/REPORT.md](results/lexical/REPORT.md).
  Pipeline leads are written with `origin: pipeline`. Reruns refresh only
  their evidence fields; `status` and notes are never touched.

`site/index.html` is the searchable Parallels Ledger. It is generated from
`site/template.html` and the lead files, so edit those rather than the output.

## Motif track (v1)

- **Vocabulary:** `data/motifs.yaml` defines each motif concretely enough
  that two readers would tag the same verse the same way.
- **Units:** `data/motif-tags/*.yaml` holds story units with verse-anchored
  tags. Units marked `original: true` (Quran, Hebrew Bible) are tagged from
  the Arabic, Hebrew or Aramaic text in this repo, and every ref is checked
  against it. Other units are tagged from secondary knowledge until their
  texts are added. Every unit names its tagger.
- **Matching:** each motif is weighted by rarity (log N/df), and pairs of
  units from different traditions are ranked by shared weight.
  `data/benchmarks/motifs.yaml` lists known pairs that must rank near the
  top. Those test the machinery, not discovery.
- **Why tags, not embeddings:** cross-lingual sentence models were tested on
  aligning Quran and Hebrew Bible stories from the originals and did poorly
  (see `results/alignment-experiments.md`). Explicit tags are slower, but
  every claim points to a verse a reader can check.
