# Reading a corpus at scale: lessons from the HB, Quran and ANE reads

Every full-read prompt points here. Follow it unless the prompt says
otherwise.

## Discovery, not confirmation

The project exists to surface what nobody has listed yet. The model lead is
*al-yamm*: the Quran's usual word for the sea is *baḥr*, but *al-yamm*
appears 8 times across 4 surahs, always in the Moses story, and it is the
Semitic sea word shared with Hebrew, Ugaritic and Mandaic. That is a
specific, checkable, surprising detail. Aim for findings like it.

- **Don't lead the readers.** Prompts and reader instructions do not list the
  parallels to find. Known leads are **benchmarks**: after the read, check
  that the pipeline surfaces them. They are not reading targets. A reader
  primed with a list finds the list.
- **Stay at the level of the passage.** Tag what this line says, concretely:
  - the word chosen;
  - an odd number;
  - a name, an object, a gesture;
  - a formula that recurs elsewhere;
  - a detail a retelling adds, drops or changes.

  "Hymn to a god" or "prayer for help" is not a tag; the particular image
  or turn of phrase in that hymn is.
- **No surface-level contrasts.** Worldview-level differences between whole
  traditions are not findings, and are never recorded as divergences:
  - "Islam affirms a creator, the Jains do not";
  - "one life against rebirth";
  - "monotheism against polytheism".

  Every reader knows them, and they are true of the traditions, not of any
  passage.
- **Divergence means a specific element changed.** The same story element,
  formula or ruling appears on both sides, and a detail differs:
  - who acts or speaks;
  - a name or title;
  - a number;
  - the order of events;
  - the motive;
  - the outcome;
  - what one side leaves out.

  Quote the decisive words on both sides.
- **Hints are specific too.** Write a hint only when a particular passage on
  the other side comes to mind for a particular detail, and name both: "the
  raven sent last and not returning (XI:154–156) against Gen 8:7, where it
  goes first".

  Don't hint thematic resemblances ("compare the Quran's view of judgment").
  Don't force hints: a unit with none is fine.
- **Prefer the rare.** A detail that occurs in one text out of hundreds is
  worth more than one that occurs everywhere; the motif weights already
  reflect this. Readers should notice and tag the odd detail even when they
  know no parallel for it. Unmatched details are tomorrow's leads.
- **Empty is a result.** A comparison reader who finds nothing specific
  records an empty match list. A generic match recorded to fill the list is
  worse than none.

## Order of work

1. **Probe the sources in parallel.** Send one agent per source family. Each
   writes a stdlib-only fetcher and normalized JSON to its own scratch folder
   (see `tools/ane_sources/`).
   - Integrate the fetchers into `tools/`; raw data goes under
     `data/raw/<corpus>/`, which is not committed.
   - Check every license. When a text cannot be had in machine-readable
     form, say so and list it; never tag it from memory as if read.
2. **Write the scope file** (`data/<corpus>/SCOPE.md`; model:
   `data/ane/SCOPE.md`). List every text with its edition, license and size,
   and what is left out and why.
3. **Generate the chunk plan** with the reading helper and freeze it.
   - Chunks of about 2,000 lines, keeping texts whole.
   - Once reading starts, regenerate only if the chunks already handed out
     keep their texts. Snapshot the assignment and compare before and after.
4. **Read in waves of 8**, then merge near-duplicate motifs, then run the
   side-by-side comparison with the Quran, then the pipeline, then the
   CLEANUP entry and the report.

## Tools: generalize, don't copy

- **One text loader.** `originals.AneCorpus` loads any corpus normalized to
  one JSON per text:
  - text: `{siglum, title, language, source, edition, license, url, sections}`
  - section: `{name, lines}`
  - line: `{n, text, lemmas?, translation?}`

  References are `<siglum> <section>:<line>`, with ranges
  `<siglum> <section>:<a>-<b>` or across sections `…:<a>-<section2>:<b>`; a
  bare section or siglum reads all of it. Section and line ids are
  normalized by `originals.norm_loc` (no spaces, colons or hyphens).
  Generalize the loader to take the corpus name and scope file; keep the
  existing corpora working.
- **One reading helper.** It has these commands: `scope --write`, `plan`,
  `texts <chunk>`, `text <ref>`, `lemmas <ref>`, and `vocab <words>`. The
  vocabulary search must take well under a second
  (`aneread.quick_vocab`), because readers call it hundreds of times.
- **Validator.** `tools/motifs.py --validate` checks chunk files for every
  corpus. Add the new corpus's `NN-` files there: refs resolve, tags sit
  inside `read` ranges, motifs exist, units stay inside the chunk, and the
  units together cover every line of the chunk.
- **Comparison.** `tools/compare.py <pair>` (pairs in `PAIRS`). Add
  `<corpus>-quran`. Readers' hints written as `Q 18:9` or `Quran 18:9–26`
  become candidates automatically.
- **Coverage, linguistic and lexical layers.** Extend `tools/coverage.py`,
  `tools/linguistic.py` (one adapter per language) and, for loanwords and
  cognates, `tools/anelex.py` (loan chains into Arabic) with benchmarks in
  `data/benchmarks/lexical.yaml`.

## Running the readers

- **Prompt.** Keep the reader prompt in one scratch file and launch each agent
  with "read the prompt file and carry it out with N = …, file = …". Each
  reader gets a private scratch folder.
- **Keep eight running.** Start the next chunk the moment one finishes.
  - A reader takes 10–25 minutes and 300–500k tokens for 2,000 lines.
  - Lines without a translation, read from word glosses, are slower.
- **Validate and commit each chunk as it arrives**, with a commit message
  naming its range.
  - The stop hook wants a clean tree, so commit readers' in-progress files as
    "WIP snapshot" commits.
  - Give each validated chunk its own commit; use `--allow-empty` when the
    snapshot already holds the final file.
- **Collect each reader's report** (5–10 best details with refs) in one
  scratch findings file; the final report draws on it.
- **API limits.** A weekly limit cut off a whole wave in the ANE session. The
  agents' work is saved: when the limit resets, `SendMessage` each agent to
  continue. Don't start a new agent for a chunk already begun.

## What readers must do

- **Read every line in the original.** Translations and glosses are reading
  aids; tag what the original says, and quote the decisive original words
  in a `note`.
- **Hints, specific and unforced.** The side-by-side pass is
  `<corpus> × Quran`, and readers' hints written as `Q surah:verse` become
  its candidates. Write one only when a particular Quran passage comes to
  mind for a particular detail (see "Discovery, not confirmation"). Hebrew
  Bible references are welcome as secondary hints.
- **Reuse motif ids.** The vocabulary holds the HB, Quran, ANE and later
  ids: search by keyword, reuse the Quran readers' ids first, never redefine
  an id with a different label, and define new ones only after searching.
- **Versions and manuscript witnesses are separate units**, with `version`
  set.
- **Fragmentary texts:**
  - Tag only what survives.
  - A tag resting on a restoration says so in its note.
  - Note the lacunae that matter.
- **Basis labels:**
  - `original: true` and `tagger: "<model>, reading the <language>"` for the
    original.
  - Memory goes in `hints`, never in tags.
  - An interpretive tag carries a `note`.

## When only a translation exists

Some texts have no open machine-readable original. Where the session prompt
allows it, such a text may be read from a **public-domain or openly licensed
translation**, clearly labelled:

- **Units:** `original: false`, `basis: translation`, and
  `tagger: "<model>, reading <translator>'s <language> translation (<year>)"`.
- **SCOPE.md:** lists the text under "read from a translation", naming the
  edition the translation follows.
- **Validator:** checks refs and read ranges for `basis: translation` units
  exactly as for originals (extend `motifs.validate` to do so).
- **Leads:** label the evidence `gloss`, never `original` or `reading`.
- **CLEANUP:** record every such unit as owed a reading from the original.

## After the read

1. **Merge near-duplicate motifs** through `data/motif-aliases.yaml`, using
   embedding candidates judged pair by pair.
2. **Run the side-by-side comparison with the Quran.**
   - Use waves of about 8 readers, one file per chunk:
     `data/alignments/<corpus>-quran/NN-<corpus>-quran.yaml`.
   - Record parallels, echoes, deliberate divergences, responses and
     contrasts, quoting the decisive words of both sides.
   - Give every divergence, response and contrast a **neutral motif id**
     naming the shared matter, never one side's claim. Put this rule in the
     comparison readers' prompt from the start.
3. **Run the pipeline:** `motifs.py --write-leads`, `lexical.py
   --write-leads`, `linguistic.py`, `originals.py`, `coverage.py` and
   `build.py`. All benchmarks must pass, apart from documented expected
   misses.
4. **Add a dated entry to `docs/CLEANUP.md`**, and report back as the
   prompt asks.
