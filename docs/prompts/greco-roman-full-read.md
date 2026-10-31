# Prompt: full read of the Greco-Roman corpus

Paste everything below the line into a new Claude Code session attached to the
`beautifulleaf/parallels` repository.

---

You are continuing **Parallels**, a lead-generation project in the
`beautifulleaf/parallels` repository. It finds parallels, convergences and
responses between religious traditions. **It is a Quran-centred project.**
Your job is a **full read of the Greco-Roman religious canon from the
original Greek and Latin**. It is held to the same standard as the Hebrew
Bible, the Quran and the ancient Near East, which are already fully read and
tagged. After the read comes a **side-by-side comparison of the Greco-Roman
texts with the Quran**.

## Start here

1. Base your work on `main`. Develop on your session's designated branch,
   created from `main`, and push there. Do not push to `main`.
2. Read these, in order:
   - `README.md`
   - `PLAN.md`, especially "Standing requirements for every text" and
     "Grounding in the originals"
   - `TRADITIONS.md`, the Greco-Roman section
   - `leads/README.md`
   - `docs/CLEANUP.md`, especially the ANE entry and its lessons
   - `data/motif-tags/ane/README.md`, the reading protocol to adapt
   - `data/ane/SCOPE.md`, the model for your scope file
   - `data/alignments/README.md`
   - `results/COVERAGE.md`
3. Run `python3 tools/fetch.py` (the Quran and the Hebrew Bible) and
   `python3 tools/anefetch.py` (the ANE texts, whose motif ids you will
   reuse). `data/raw/` is gitignored.

## Goal

Every text in scope gets the project's standing treatment:

1. **The original text is in the repo**, with lemmas where an edition has
   them. Raw downloads go under `data/raw/greco-roman/` and are not
   committed. Fetchers go in `tools/`.
2. **A full read.** Every line or section is read in the Greek or Latin and
   tagged with motifs in `data/motif-tags/greco-roman/`. Every tag cites
   lines inside its unit's `read` ranges. Nothing counts as covered until it
   has been read in full.
3. **The linguistic layer** (`tools/linguistic.py`): add an adapter for
   Greek and one for Latin.
4. **Lexical links to the Quran.** Greek loanwords in Quranic Arabic,
   usually through Aramaic or Syriac, extending the loan-chain module
   `tools/anelex.py` (Greek → Aramaic/Syriac → Arabic). Add benchmarks to
   `data/benchmarks/lexical.yaml`:
   - *drachmē → dirham*: must recover (Q 12:20).
   - *euangelion → injīl*: must recover.
   - *chartēs → qirṭās*: must recover (Q 6:7, 6:91).
   - *paradeisos → firdaws*: should recover, and should note the Iranian
     origin (*pairidaēza*).
   - *kalamos → qalam*: optional.
   - *dikastēs (?) → qisṭās*: contested; record it as `expect: false` if
     it is not recovered.
5. **Replace the unit tagged from secondary knowledge**: `gr-deucalion` in
   `data/motif-tags/flood.yaml`. Replace it with units read from Ovid
   (*Met.* I), Apollodorus (1.7.2) and Pindar or Lucian where in scope, and
   keep the benchmark pairs in `data/benchmarks/motifs.yaml` passing.
6. **Compare with the Quran side by side**, as below. Do not run a
   Greco-Roman × Hebrew Bible or Greco-Roman × ANE pass. List those as
   deferred in `docs/CLEANUP.md`.

## Scope: the core religious canon

Greek and Latin only. The Syriac and Arabic intermediaries are left to a later
Syriac session: the Syriac Alexander Legend (Neshana), the Syriac Seven
Sleepers, and the Arabic *Theology of Aristotle*. Name them in hints wherever
they are the real link to the Quran, e.g. Q 18:83–98 against the Neshana.

| Group | Texts |
|---|---|
| Archaic myth and hymn | Hesiod, *Theogony*, *Works and Days*, the fragments of the *Catalogue*; *Homeric Hymns*; Homer, *Iliad* and *Odyssey* |
| Orphica | *Orphic Hymns*; *Orphic Argonautica*; the Derveni papyrus where an open text exists; the gold tablets |
| Plato | *Timaeus*, *Phaedo*, *Phaedrus*, *Symposium*, *Republic* (all of it, the Myth of Er included), *Laws* X, *Gorgias* (the judgment myth), *Critias* |
| Neoplatonism | Plotinus, *Enneads* (all six, prioritizing IV–VI, the source of the Arabic *Theology of Aristotle*); Proclus, *Elements of Theology*; Porphyry, *Life of Plotinus* and *On the Cave of the Nymphs*; Iamblichus, *De mysteriis* |
| Hermetica | *Corpus Hermeticum* I–XVIII; Latin *Asclepius* |
| Mythography | Apollodorus, *Bibliotheca*; Ovid, *Metamorphoses* (Deucalion I, Baucis and Philemon VIII, Phaethon, the ages of man) and *Fasti* |
| Late antique religion | Apuleius, *Metamorphoses* XI (Isis); Plutarch, *On Isis and Osiris*, *On the E at Delphi*, *On the Delays of Divine Vengeance*; Lucian, *On the Syrian Goddess*; Cicero, *De natura deorum* and the *Somnium Scipionis* |
| Legend | the Greek *Alexander Romance* (Pseudo-Callisthenes, the recension available); the Greek *Seven Sleepers of Ephesus* (the Passio, where an open text exists) |

Measure first, then fix the scope. Count every text's size in lines or
sections and record it in `data/greco-roman/SCOPE.md`, with each text's
edition and license and what is left out and why. Plan the chunks from those
counts.

## Sources (check each before relying on it)

- **Perseus canonical-greekLit and canonical-latinLit** (GitHub, TEI, CTS
  URNs, CC BY-SA). Fetch them through `raw.githubusercontent.com`, which
  works from these sessions; the github.com website is blocked.
- **First1KGreek** (OpenGreekAndLatin, GitHub, CC BY-SA), for the later
  Greek: the Neoplatonists, the Hermetica and Lucian.
- **Lemmatized Ancient Greek XML** (gcelano, GitHub): Perseus and First1K
  texts with automatic POS tags and lemmas. Use its lemmas, and say that
  they are automatic.
- **Perseus Ancient Greek Dependency Treebank** and **PROIEL**: gold
  lemmas for Homer, Hesiod, Herodotus and others. Prefer them where they
  cover a text.
- **Latin:** Perseus canonical-latinLit. For lemmas, LASLA or LiLa where
  they are reachable and licensed; otherwise read without them.
- **The Latin Library** is reachable, for texts Perseus lacks. Check its
  terms.
- The **Glossarium Graeco-Arabicum** (Bochum) did not answer from the ANE
  session. Try it again; if it still fails, say so.
- The TLG is paywalled: do not use it.

If a text cannot be obtained in a machine-readable original, say so plainly,
list it in SCOPE.md, and do not tag it from memory as if read.

## Tools: generalize, don't copy

The ANE session built a general machinery. Reuse it:

- **Text loader.** `originals.AneCorpus` loads any corpus normalized to one
  JSON per text: siglum; sections, each with lines; each line with
  `n`, `text`, `lemmas` and `translation`. References read
  `<siglum> <section>:<line>`.
  - Generalize it to take a corpus name and its scope file, rather than
    writing a second loader.
  - Canonical citations fit it as they are: `Il. 1:1-52`, `Od. 9:105`,
    `Ti. 22b-23c`, `Enn. IV.8:1`, `CH I:12`.
  - Keep the ANE references working.
- **Reading helper.** Adapt `tools/aneread.py`:
  - commands `scope --write`, `plan`, `texts <chunk>`, `text <ref>`,
    `lemmas <ref>`, `vocab <words>`;
  - the fast vocabulary loader, so a search takes well under a second;
  - chunk assignments written to the scope file and frozen once reading
    starts.
- **Validator.** `tools/motifs.py --validate` already checks `ane/NN-…`
  chunk files. Add `greco-roman/NN-…` the same way.
- **Comparison.** `tools/compare.py` takes a pair (`hb-quran`, `ane-hb`,
  `ane-quran`). Add `gr-quran` (reviewed side `greco-roman`, candidates from
  `quran`).
  - Its Quran hint pattern (`Q 18:9`, `Quran 18:9–26`) turns readers' hints
    into candidates. So readers must write Quran references in that form.

## How to read at scale (lessons from the ANE read)

- **Probe sources in parallel first.** Use one agent per source family,
  each writing a stdlib-only fetcher and normalized JSON in its own scratch
  folder. Integrate them into `tools/` (see `tools/ane_sources/`).
- **Chunks of about 2,000 lines**, keeping texts whole. Use **waves of about
  8 reader agents**, and start the next chunk whenever one finishes so that
  eight are always running.
  - Readers took 10–25 minutes and 300–500k tokens per chunk.
  - Give each reader a private scratch folder.
  - Keep the reader prompt in one file, and launch each agent with "read
    the prompt file and carry it out with N = …".
- **Validate and commit each chunk** as it arrives, with a commit message
  naming its range.
  - The stop hook requires a clean tree, so commit readers' in-progress
    files as "WIP snapshot" commits.
  - Every chunk still gets its own validated commit. Use `--allow-empty`
    when the snapshot already holds the final file.
- **Quran-first hints.** Each reader asks of every unit what in the Quran
  it might parallel, echo, answer or diverge from, and writes precise
  `Q surah:verse` hints. Some examples:
  - the Cave (18:9–26) against the Sleepers;
  - Dhul-Qarnayn (18:83–98) against the *Alexander Romance*;
  - Idris (19:56–57, 21:85) against Hermes;
  - the people of Lot against Baucis and Philemon;
  - the flood;
  - Iblis's refusal (7:11–18) against Prometheus and the Titans;
  - the barzakh, the scales and the bridge against Plato's judgment myths;
  - "He begets not" (112:3) against the theogonies;
  - the soul's descent and return against Plotinus.

  Hebrew Bible references are secondary.
- **Reuse ids.** Search the vocabulary by keyword. It holds the HB, Quran
  and ANE ids, about 20,000 in all. Reuse the Quran readers' ids first,
  never redefine an id with a different label, and leave near-duplicates
  for the merge.
- **Versions and witnesses are separate units**, as with Gilgamesh OB/SB
  and the Egyptian witnesses.
- **Mixed sections.** When a text has both unnamed and named sections, a
  bare line now resolves to the unnamed one. Keep section and line ids free
  of spaces, colons and hyphens; `originals.norm_loc` handles most cases.
- **API limits.** A weekly limit cut off a wave in the ANE session. The
  agents' work is saved, and `SendMessage` to each agent resumes it once
  the limit resets. Don't start a new agent for a chunk already begun.
- **Basis labels.** Tags read from the original are `original: true` with
  `tagger: "<model>, reading the Greek"` (or "the Latin"). Parallels from
  memory go in `hints`, never in tags. An interpretive reading carries a
  `note` quoting the Greek or Latin.

## After the read

1. **Merge near-duplicate motifs** through `data/motif-aliases.yaml`, using
   embedding candidates judged pair by pair, as the earlier reads did.
2. **The GR × Quran comparison pass.** This is required.
   - Run `python3 tools/compare.py gr-quran candidates`. Candidates come
     from hints, from units sharing one or two motifs, and from label
     similarity.
   - Run comparison readers in waves of about 8. Each reads both originals
     side by side and writes `data/alignments/gr-quran/NN-gr-quran.yaml`.
   - Record parallels, echoes, **deliberate divergences**, responses and
     contrasts, quoting the decisive Greek or Latin and Arabic words of
     both sides in the note.
   - **Divergences matter as much as similarities.** Examples:
     - the Sleepers' number and the years in the cave, against Q 18:22
       and 18:25, which itself reports the disputes;
     - the Alexander of the *Romance* against Dhul-Qarnayn, who acts by
       God's leave and builds the barrier;
     - Hermes the thrice-great against Idris raised "to a high place";
     - divine sonship in the theogonies against Q 112.
   - Use a **neutral motif id** for every divergence, response and contrast,
     naming the shared matter (`number-of-the-sleepers`,
     `builder-of-the-iron-barrier`), never one side's claim. Put this in
     the comparison readers' prompt from the start.
   - Validate each file with `python3 tools/compare.py gr-quran validate <file>`.
3. **Run the pipeline:**
   - `python3 tools/motifs.py --write-leads`
   - `python3 tools/lexical.py --write-leads`
   - `python3 tools/linguistic.py`
   - `python3 tools/originals.py`
   - `python3 tools/coverage.py` (extend it to the Greco-Roman corpus)
   - `python3 tools/build.py`

   All benchmarks must pass, apart from documented expected misses.
4. **Add a dated entry to `docs/CLEANUP.md`** in its format. Record what
   was added, what was left behind, the deferred GR × HB and GR × ANE
   passes, and any shortcut to undo.
5. **Report back:**
   - an inventory of what was read, partly read and left out;
   - the benchmark results;
   - the comparison counts by relation;
   - the most interesting GR ↔ Quran leads and deliberate divergences,
     with line and verse references.

## Rules

- **Originals first.** Translations are reading aids. Every claim states
  its basis (`original`, `reading`, `lexicon`, `gloss`, `scholarship`).
- Check each source's license. Keep raw text out of git.
- Don't create pull requests unless asked.
- Don't edit `data/motif-tags/hb/`, `data/motif-tags/quran/`,
  `data/motif-tags/ane/`, or the existing `data/alignments/` pairs. Those
  reads belong to other sessions.
