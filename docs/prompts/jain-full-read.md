# Prompt: full read of the Jain scriptures

Paste everything below the line into a new Claude Code session attached to the
`beautifulleaf/parallels` repository.

---

You are continuing **Parallels**, a lead-generation project in the
`beautifulleaf/parallels` repository. It finds parallels, convergences and
responses between religious traditions. **It is a Quran-centred project.**

Your job is a **full read of the Jain scriptures and core literature, for both
Śvetāmbara and Digambara traditions**. Read in the original Ardhamāgadhī,
other Prakrits, Apabhraṃśa, Sanskrit and Old Hindi wherever an open e-text
exists, and otherwise from public-domain translations, labelled. Hold the read
to the standard of the Hebrew Bible, Quran and ancient Near East reads. A
**side-by-side comparison with the Quran** follows.

**Central and Eastern rounds:** follow "Central and Eastern traditions" in `docs/prompts/reading-at-scale.md` as well: the route graph, decoy pairs, the image and argument records, the translators' lexicon, and the Islamic reception layer for this tradition.

## Start here

1. Base your work on `main`. Develop on your session's designated branch,
   created from `main`, and push there. Do not push to `main`.
2. Read these, in order:
   - `README.md`
   - `PLAN.md`, especially "Standing requirements for every text",
     "Grounding in the originals" and the concept layer
   - `TRADITIONS.md`: the Jainism section
   - `leads/README.md`
   - `docs/prompts/reading-at-scale.md`: the method, tools, lessons and
     translation protocol. Follow it.
   - `docs/CLEANUP.md`
   - `data/motif-tags/ane/README.md`: the reading protocol to adapt
   - `data/ane/SCOPE.md`: the model for the scope file
   - `data/alignments/README.md`
3. Run `python3 tools/fetch.py` and `python3 tools/anefetch.py`.
4. Use the shared concept vocabulary `data/concepts.yaml` if it exists.
   Otherwise build one as `docs/prompts/christian-philosophy-full-read.md`
   phase 3 describes, and record it in `docs/CLEANUP.md` for merging.

## Corpus

Use corpus id `jain` and tradition id `jainism`; add the tradition to
`data/traditions.yaml` if it is missing.

- Raw data: `data/raw/jain/`
- Tags: `data/motif-tags/jain/`
- Scope file: `data/jain/SCOPE.md`

**All openly available texts, both sects.** Measure each text and record in
SCOPE.md its edition, sect, language and license, whether it is read from
the original or from a translation, and what is left out and why.

| Group | Texts | Source |
|---|---|---|
| Śvetāmbara Āgamas, original | *Āyāraṅga* (Ācārāṅga); *Sūyagaḍa* (Sūtrakṛtāṅga) 1; *Uttarajjhāyā* (Uttarādhyayana); *Dasaveyāliya* (Daśavaikālika); *Isibhāsiyāiṃ* (the sayings of the seers, including non-Jain sages) | GRETIL Prakrit section, input by Ousaka and Yamazaki; check the terms |
| Śvetāmbara Āgamas, translation where no original is open | *Kalpa Sūtra* (the lives of the Jinas, Mahāvīra's birth and the embryo transfer); *Sūyagaḍa* 2; *Ācārāṅga* where GRETIL's text has gaps | Jacobi, *Sacred Books of the East* 22 and 45, public domain, labelled. Look first for an open Prakrit e-text: jainelibrary.org and jainqq.org have scans, and some e-texts. |
| Both sects | Umāsvāti, *Tattvārtha Sūtra* (Sanskrit) | GRETIL, sanskritdocuments.org or another open e-text |
| Digambara | Kundakunda, *Samayasāra*, *Pravacanasāra*, *Pañcāstikāya*; the *Ṣaṭkhaṇḍāgama* if any open e-text exists | Look for open Prakrit texts; list the rest |
| Philosophy and polemic | Haribhadra, *Śāstravārtāsamuccaya* (comparative review of other doctrines) and *Dhuttakkhāṇa* (satire of Hindu myth); Samantabhadra, *Āptamīmāṃsā*, if open | GRETIL |
| Narrative | Vimalasūri or Svayambhū, *Paumacariu* (the Jain Rāmāyaṇa, Apabhraṃśa); Saṅghadāsa, *Vasudevahiṇḍi*, if open; the Jain *Harivaṃśa*, if open | GRETIL |
| Jain–Mughal | Banārasīdās, *Ardhakathānaka* (Old Hindi, 1641, at the Mughal court's edge); texts of Hīravijaya Sūri's circle at Akbar's court, and the Mughal farmans for Jain holy days, where open (Persian or Sanskrit) | GRETIL; Internet Archive for public-domain editions |

Not usable: sacred-texts.com is blocked by the proxy.

## Concept layer

Jain texts are largely doctrinal. Tag concepts beside motifs. Examples:

- **Ahiṃsā**, and the care for the smallest life forms.
- **Anekāntavāda and syādvāda**: many-sidedness, against claims to sole
  truth.
- **Karma as subtle matter**, the soul (*jīva*) bound and freed.
- **The uncreated, eternal universe**: no creator God.
- **The Jina as an exemplar, not a saviour.**
- **Renunciation**: the monk's vows, nudity among the Digambaras.
- **Fasting**, up to *sallekhanā*.
- **Cosmic time**: the cycles, the *avasarpiṇī*.
- **Omniscience** (*kevala-jñāna*).
- **Rebirth** in the four destinies, among them the hells and the heavens.

## Known leads (benchmarks, not reading targets)

- the Jain retellings of the Hindu epics
- Hīravijaya Sūri at Akbar's court

These are already known. They are **benchmarks**: after the read, check that
the pipeline surfaces them. Do not give them to the readers, and do not read
for them. Follow "Discovery, not confirmation" in
`docs/prompts/reading-at-scale.md`: the aim is the specific detail nobody has
listed yet.

## Lexical

Jain texts carry few Arabic loans. The Mughal-era Old Hindi and Persian
texts do: Banārasīdās, the farmans. Build a surface-form loan list for
those, matched against Quranic lemmas, as the Sikh round does. There is no
must-recover benchmark. Record what is found.

## After the read

1. **Merge** near-duplicate motifs and concepts.
2. **Compare with the Quran** (Jain × Quran), on motifs and concepts alike. A concept match needs a specific shared formulation, argument or image, not a shared or opposed doctrine.
   - Use neutral ids for divergences, quoting the decisive Prakrit or
     Sanskrit (transliterated) and Arabic.
   - Divergences matter as much as parallels, but only specific ones (see
     "Discovery, not confirmation" in `reading-at-scale.md`). Worldview-level
     contrasts true of whole traditions are not findings: never record them.
3. **Run the pipeline**, with every benchmark passing.
4. **Add a dated `docs/CLEANUP.md` entry.**
   - Record comparisons against Hinduism, Buddhism and Manichaeism as
     deferred. Manichaeism matters here because of the Manichaean elect's
     rules.
   - Islamic texts beyond the Quran, al-Ghazali and other Sufi authors
     among them, belong to the Islamic analysis, not a separate round. Note
     their units as natural partners once they are read.
5. **Report:**
   - the inventory: read from the original, from a translation, left out;
   - the comparison counts by relation;
   - the most interesting Jain ↔ Quran leads and divergences, with
     references on both sides.

## Rules

- **Originals first.** Every claim states its basis.
- **Licenses.** Check each source's license, and keep raw text out of git.
- **Respect.** This is a living community.
  - Record sectarian differences (the canon, Digambara and Śvetāmbara
    positions) neutrally.
  - Keep the notes descriptive and respectful.
- **No pull requests** unless asked.
- **Other sessions' folders.** Don't edit their tag or alignment folders.
