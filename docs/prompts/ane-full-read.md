# Prompt: full read of the ancient Near East corpus

Paste everything below the line into a new Claude Code session attached to the
`beautifulleaf/parallels` repository.

---

You are continuing **Parallels**, a lead-generation project in the
`beautifulleaf/parallels` repository. It finds parallels, convergences and
responses between religious traditions. Your job is a **full read of the
ancient Near Eastern (ANE) corpus from the original texts**, done to the same
standard as the Hebrew Bible, which is already fully read and tagged.

## Start here

1. Base your work on `main`, which has everything so far. Develop on your
   session's designated branch, created from `main`, and push there. Do not
   push to `main` or to `claude/nifty-einstein-ewlse8`; another session works
   on those.
2. Read these, in order:
   - `README.md`
   - `PLAN.md`, especially "Standing requirements for every text",
     "Grounding in the originals" and the ANE source plan.
   - `TRADITIONS.md`, the Ancient Near East section.
   - `leads/README.md`
   - `data/motif-tags/hb/README.md`, the reading protocol to mirror.
   - `results/COVERAGE.md`
3. Run `python3 tools/fetch.py` to download the existing raw corpora.
   `data/raw/` is gitignored.

## Goal

Every ANE text in scope gets the project's standing treatment:

1. **The original text is in the repo**, with lemmas or morphology where the
   edition has them. Raw downloads go under `data/raw/` (not committed);
   loaders go in `tools/`.
2. **A full read.** Every line or section is read in the original
   (transliteration with lemmas and glosses where the edition provides
   them) and tagged with motifs in `data/motif-tags/ane/`. Every tag cites
   lines inside its unit's `read` ranges. Nothing counts as covered until it
   has been read in full.
3. **The linguistic layer** (`tools/linguistic.py`): add an adapter per
   corpus for phrases, formulas, doublets, hapax legomena and loanwords.
4. **Lexical and cognate links.** Connect Akkadian, Ugaritic and Aramaic to
   the Hebrew and Arabic lemmas already in the project, and build
   **loan chains**: Sumerian → Akkadian → Aramaic → Hebrew/Arabic. Add
   benchmarks to `data/benchmarks/lexical.yaml`. The chain must recover
   *guza → kussû → korsêʾ → kursī* and *é-gal → ekallu → hêkhāl/haykal*,
   and should link *tinūru → tannûr/tannūr*. Today the pipeline recovers
   *kursī ↔ korsêʾ* but misses the Hebrew *kissēʾ*.
5. **Replace the units tagged from secondary knowledge** (Gilgamesh XI,
   Atrahasis, Eridu Genesis, the Sargon Birth Legend, the Tale of Two
   Brothers, in `data/motif-tags/*.yaml`) with units read from the original.
   Keep the benchmark pairs in `data/benchmarks/motifs.yaml` passing.

## Scope and sources (all checked as reachable from a session like this)

| Corpus | Source | Notes |
|---|---|---|
| **Sumerian** literature | ETCSL (etcsl.orinst.ox.ac.uk): transliterations and translations of about 400 compositions; ORACC ePSD2 (lemmatized) | Read all of ETCSL's literary corpus. |
| **Akkadian** literature and religion | eBL (ebl.lmu.de: Babylonian literature corpus, including Gilgamesh, Atrahasis, Enuma Elish, Ludlul, Erra, the Theodicy); ORACC projects (`json/<project>.zip`); CDLI | ORACC's server omits an intermediate certificate. Append `data/certs/incommon-rsa-server-ca2.pem` to the system bundle (`/root/.ccr/ca-bundle.crt`) for those requests. **Never disable TLS verification.** |
| Akkadian treaties, prophecies, letters | ORACC SAAo (e.g. `saao/saa02` for Esarhaddon's Succession Treaty), Amarna (`aemw/amarna`), Ugarit's Akkadian texts (`aemw/ugarit`) | Prioritize treaties, prophecies, omens, incantations and royal inscriptions with religious content. List what you leave out and why. |
| **Ugaritic** | EUPT (Göttingen): public `eupt-xml` repository on gitlab.gwdg.de (TEI, MIT license, Kirta KTU 1.14–1.15 and a motif glossary); the full poetic corpus (Baal Cycle, Aqhat) is in its web edition via TextAPI | Probe the TextAPI to get the Baal Cycle and Aqhat. KTU scans on the Internet Archive are borrow-only: use them to check readings, not as data. If a text can't be obtained machine-readably, say so plainly. Don't tag it from memory as if read. |
| **Hittite / Hurrian** | Hethitologie-Portal Mainz (hethport.uni-wuerzburg.de) / TLHdig, by CTH number | Myths (Kumarbi cycle, Illuyanka, Telipinu), prayers (Mursili's plague prayers), treaties, rituals. |
| **Egyptian** | Thesaurus Linguae Aegyptiae (thesaurus-linguae-aegyptiae.de; also on Hugging Face, rate-limited without a token) | Literary and religious texts: Amenemope, Two Brothers, Sinuhe, the Aten hymn, Book of the Dead 125, and selections from the Pyramid and Coffin Texts with stated criteria. |
| **Northwest Semitic inscriptions** | Wherever an open edition exists | Mesha, Deir Alla (Balaam), Tel Dan, Kuntillet Ajrud and Khirbet el-Qom: small but high value. |

First, write `data/ane/SCOPE.md`. List every corpus and text you will read,
its edition and license, its size (lines or sections), and what is out of
scope and why. Plan the reading chunks from those sizes.

## How to read at scale (lessons from the Hebrew Bible and Quran reads)

- **Parallel readers, in waves of about 8 agents.** Each reads one chunk of
  roughly equal size. Follow the patterns in `tools/hbread.py`,
  `tools/qread.py` and `tools/motifs.py`:
  - A per-corpus reading helper (`tools/aneread.py`) that prints a chunk's
    original text with line numbers.
  - A loader that resolves ANE references for validation and passage text.
    Extend `tools/originals.py` and the validator in `tools/motifs.py`, and
    add a chunk-boundary check for `ane/NN-...` files the way `hb/` and
    `quran/` have one.
  - A protocol file, `data/motif-tags/ane/README.md`, adapted from
    `data/motif-tags/hb/README.md`.
- **Give each reader a private scratch folder** (`<scratchpad>/ane-chunkNN/`).
  Shared scratch file names once mixed one reader's units into another's
  file.
- Readers search the vocabulary by keyword (`python3 tools/hbread.py vocab
  <words>`). It has more than 8,000 motifs, so it must never be printed whole.
  Readers reuse existing ids, especially the Hebrew Bible's, so that matches
  appear. They never redefine an id with a different label. Near-duplicates
  are merged afterwards through `data/motif-aliases.yaml`.
- **Tablets are fragmentary.** Record lacunae and restorations in tag notes.
  Tag only what the preserved text says. Treat different versions as
  separate units, e.g. Old Babylonian vs Standard Babylonian Gilgamesh, or
  Sumerian vs Akkadian versions.
- **Basis labels.** Tags read from the original are `original: true` with
  `tagger: "<model>, reading the Akkadian"` (or Sumerian, Ugaritic and so on).
  Parallels recalled from memory go in `hints`, never in tags. Interpretive
  readings carry a `note`.
- Validate every file with `python3 tools/motifs.py --validate <file>` until
  it prints ok. Commit each validated chunk, with a commit message naming its
  range.

## After the read

1. Merge near-duplicate motifs. Use embedding candidates, judged pair by
   pair, as was done for the Hebrew Bible and the Quran (see the commits
   "Merge duplicate motifs…" and "Merge near-duplicate motifs after the full
   Quran read…").
2. **Side-by-side comparison pass.** This is required, not optional. Separate
   full reads only match where two readers chose the same motif id. After the
   Hebrew Bible and Quran reads, only 22% of the Quran's tags shared an id
   with the Hebrew Bible, and more than half of the Quran's units had no
   Hebrew Bible partner. The comparison pass fixes this.
   - Read `data/alignments/README.md` and `tools/compare.py`. They implement
     the pass for HB × Quran.
   - Generalize `tools/compare.py` to take the pair as an argument, so that it
     works for `ane-hb` and `ane-quran`. Keep `hb-quran` working unchanged.
   - Generate candidates for every ANE unit from three sources: the reader's
     hints, units sharing one or two motifs, and label similarity.
   - Run comparison readers in waves of about 8. Each one reads both originals
     side by side and writes `data/alignments/<pair>/NN-<pair>.yaml`.
   - Readers record parallels, echoes, **deliberate divergences** (the same
     element deliberately changed: divine titles, who acts, motives, endings,
     omissions, reversals), responses and contrasts. Each records the decisive
     words of both sides in the note.
   - Divergences matter as much as similarities. One example is the flood
     hero's motive and the gods' hunger after the flood (Atrahasis III)
     against Gen 8:21. Another is the birth story told of Sargon against
     the one told of Moses.
   - For divergences, responses and contrasts, readers use a **neutral motif
     id** naming the shared matter, such as `cause-of-the-flood` or
     `who-sends-the-flood`, never one side's claim (see
     `data/alignments/README.md`). Put this rule in the readers' prompt
     from the start. In the HB × Quran pass it arrived mid-run, and most
     readers had to rewrite more than 100 matches each.
   - Validate each file with `python3 tools/compare.py validate <file>`. The
     loader in `tools/motifs.py` turns confirmed matches into shared tags,
     and every confirmed pair becomes a lead. Each lead's card in the Ledger
     shows the two texts side by side (`site/template.html`).
3. Run `python3 tools/motifs.py --write-leads`, `python3 tools/lexical.py
   --write-leads`, `python3 tools/linguistic.py`, `python3 tools/originals.py`,
   `python3 tools/coverage.py` and `python3 tools/build.py`. All benchmarks
   must pass, apart from documented, expected misses.
4. Add a dated entry to `docs/CLEANUP.md`, following its format. Record
   what the ANE work added, what it left behind (duplicate ids, label
   variants, stale leads, units still from secondary knowledge, one-off
   patches, texts left out) and any shortcut the final cleanup should undo.
   Don't clean up beyond the light tidy that file describes. The full
   cleanup happens once, after every tradition is done.
5. Report back, in this order:
   - an inventory of what was fully read (text, edition, lines), what was
     partly read and what was left out;
   - the benchmark results;
   - the comparison pass's counts by relation;
   - the most interesting new leads and deliberate divergences, ANE ↔ Hebrew
     Bible and ANE ↔ Quran, with line and verse references.

## Rules

- **Originals first.** Translations and English glosses are reading aids.
  Every claim states its basis (`original`, `reading`, `lexicon`, `gloss`,
  `scholarship`).
- Check each source's license. Keep raw copyrighted text out of git when the
  license doesn't allow redistribution, and say what you did.
- Don't create pull requests unless asked.
- Don't edit `data/motif-tags/hb/`, `data/motif-tags/quran/` or
  `data/alignments/hb-quran/`. Those reads belong to other sessions.
