# Prompt: full read of the Sikh scriptures

Paste everything below the line into a new Claude Code session attached to the
`beautifulleaf/parallels` repository. The round is large (the Guru Granth
Sahib alone is about 60,000 lines), so plan for it to continue in a second
session. The scope file and chunk plan make that seamless.

---

You are continuing **Parallels**, a lead-generation project in the
`beautifulleaf/parallels` repository. It finds parallels, convergences and
responses between religious traditions. **It is a Quran-centred project.**
Your job is a **full read of the Sikh scriptures in the original Gurmukhi**
(and Persian for the *Zafarnama*), done to the standard of the Hebrew Bible,
Quran and ancient Near East reads. A **side-by-side comparison with the
Quran** follows.

**Central and Eastern rounds:** follow "Central and Eastern traditions" in `docs/prompts/reading-at-scale.md` as well: the route graph, decoy pairs, the image and argument records, the translators' lexicon, and the Islamic reception layer for this tradition.

## Start here

1. Base your work on `main`. Develop on your session's designated branch,
   created from `main`, and push there. Do not push to `main`.
2. Read these, in order:
   - `README.md`
   - `PLAN.md`, especially "Standing requirements for every text",
     "Grounding in the originals" and the concept layer
   - `TRADITIONS.md`: the Sikhism section
   - `leads/README.md`
   - `docs/prompts/reading-at-scale.md`: the method, tools, lessons and
     translation protocol. Follow it.
   - `docs/CLEANUP.md`
   - `data/motif-tags/ane/README.md`: the reading protocol to adapt
   - `data/ane/SCOPE.md`: the model for the scope file
   - `data/alignments/README.md`
3. Run `python3 tools/fetch.py` and `python3 tools/anefetch.py`.
4. If the Christian round's phase 3 has run, `data/concepts.yaml` exists:
   use it. If it has not, build a small concept vocabulary as that prompt
   describes, and record it in `docs/CLEANUP.md` so the two can be merged.

## Corpus

Corpus id `sikh` and tradition id `sikhism` (add it to `data/traditions.yaml`
if missing). Raw data goes in `data/raw/sikh/`, tags in
`data/motif-tags/sikh/`, and the scope file is `data/sikh/SCOPE.md`.

| Text | Notes |
|---|---|
| **Guru Granth Sahib, in full** | All 1,430 angs: the Gurus' compositions (Nanak, Angad, Amar Das, Ram Das, Arjan, Tegh Bahadur) and the *bhagat bani* (Sheikh Farid, Kabir, Namdev, Ravidas, Trilochan, Beni, Dhanna, Sain, Pipa, Surdas, Parmanand, Ramanand, Sadhna, Bhikhan, Jaidev), plus the *Bhatt* and *Sadd*. Cite by ang and line, recording raga, author and composition: `GGS 1:1`, or the Shabad OS ids. |
| **Bhai Gurdas, *Vaaran*** | All 40 vaars, including Var 1 (Guru Nanak at Mecca and Baghdad), and the *Kabitt Savaiye* if available. |
| **Dasam Granth, in full** | Jaap Sahib, Akal Ustat, Bachitar Natak, Chandi Charitar, Chaupai, the Avatars, the *Charitropakhyan*, and the *Zafarnama* in Persian. The community disputes the authorship and content of parts of it, especially the *Charitropakhyan*. Read it fully and record the dispute in SCOPE.md and in the units' notes, neutrally. |
| **Janamsakhis** | The Puratan and B40 janamsakhis, and the Bala tradition where open. Read the original Gurmukhi where an open text exists; otherwise Macauliffe's *The Sikh Religion* (1909, public domain), labelled as a translation per `reading-at-scale.md`. |

Measure every text and write SCOPE.md before planning chunks. Chunks are
about 2,000 lines, keeping compositions whole within a raga where possible.

## Sources (reachable from a sibling session)

- **Shabad OS database** (GitHub `shabados/database`; check its license).
  It has the Guru Granth Sahib, Dasam Granth and Bhai Gurdas in Gurmukhi,
  line by line, with transliterations and English (and Punjabi)
  translations. Prefer it: one bulk download.
- **BaniDB API** (`https://api.banidb.com/v2/…`, open), as a fallback and
  for cross-checks.
- **SearchGurbani** and **srigranth.org**, for checking readings only.
- **Macauliffe 1909** on the Internet Archive, for the janamsakhis when no
  original is open.

Lemmas: none of these has lemmatization. Read the Gurmukhi with the
transliteration and translation as aids. The **lexical** work below runs on
the surface forms, through a word list of Arabic and Persian loans.

## Concept layer

The Sikh scriptures are hymnic and theological rather than narrative. Tag
**concepts** beside motifs, using the shared `data/concepts.yaml`, for
example:

- the oneness of God (Ik Onkar against *tawḥīd*);
- the divine Name (*Nām* against *dhikr*);
- the divine order (*hukam*, from Arabic *ḥukm*);
- grace (*nadar*, *karam*, from Arabic *karam*);
- the true Guru;
- transmigration and liberation;
- the lover and the Beloved;
- the critique of external ritual (fasting, pilgrimage, the qazi and the
  pandit);
- divine judgment (*dargah*, the *lekha* account);
- the transience of life.

## Known leads (benchmarks, not reading targets)

- Sheikh Farid's saloks
- the *Zafarnama*
- Guru Nanak at Mecca
- the Arabic and Persian vocabulary of the Guru Granth Sahib

These are already known. They are **benchmarks**: after the read, check that
the pipeline surfaces them. Do not give them to the readers, and do not read
for them. Follow "Discovery, not confirmation" in
`docs/prompts/reading-at-scale.md`: the aim is the specific detail nobody has
listed yet.

## Lexical benchmarks (`data/benchmarks/lexical.yaml`)

Build a surface-form matcher from Gurmukhi transliterations to Quranic
lemmas, as a loanword list with attestations. These must recover:

- *hukam* ← *ḥukm*
- *karam* ← *karam*
- *khalak* ← *khalq*
- *kudarat* ← *qudra*
- *dargah* ← Persian *dargāh*
- *Allāh*, *Rahīm*, *Karīm*

*Nām* ~ *ism* is a concept link, not a loan.

## After the read

1. **Merge near-duplicate motifs** (and concepts).
2. **Run the Sikh × Quran comparison**, on motifs and concepts alike. A concept match needs a specific shared formulation, argument or image, not a shared or opposed doctrine, with
   neutral ids for divergences, quoting the decisive Gurmukhi (with
   transliteration) and Arabic.
   - Divergences matter as much as parallels, but only specific ones (see
     "Discovery, not confirmation" in `reading-at-scale.md`). Worldview-level
     contrasts true of whole traditions are not findings: never record them.
3. **Run the pipeline**, with every benchmark passing.
4. **Add a dated `docs/CLEANUP.md` entry.** Record the deferred comparisons
   against the Hebrew Bible, the ANE and Hinduism. The Sufi material within
   the Islamic tradition (Farid's Chishti setting, Kabir's Sufi milieu,
   authors such as al-Ghazali) belongs to the Islamic side of the analysis,
   not to a separate round: when the Islamic texts beyond the Quran are read,
   their units are natural partners for these hymns.
5. **Report:**
   - the inventory: read from the original, from a translation, left out;
   - the benchmarks;
   - the comparison counts by relation;
   - the most interesting Sikh ↔ Quran leads and divergences, with
     references on both sides.

## Rules

- **Originals first.** Every claim states its basis.
- **Licenses.** Check each source's license; keep raw text out of git.
- **Respect.** The Guru Granth Sahib is the living Guru of a living
  community. Keep notes descriptive and respectful. Record disputed
  attributions (the bhagat bani, the Dasam Granth) as disputed, without
  taking sides.
- Don't create pull requests unless asked.
- Don't edit other sessions' tag or alignment folders.
