# Prompt: full read of the Hindu scriptures (three phases)

The Hindu corpus dwarfs everything read so far: the Mahābhārata alone has
about 75,000 verses. The round is therefore split into **three phases, one or
more sessions each, run in order**. Paste everything below the line into a new
Claude Code session attached to the `beautifulleaf/parallels` repository,
and **set the phase** in the first line.

---

**Phase: <1 | 2 | 3>** (see "Phases" below; do only your phase)

You are continuing **Parallels**, a lead-generation project in the
`beautifulleaf/parallels` repository. It finds parallels, convergences and
responses between religious traditions. **It is a Quran-centred project.**

- **The task:** a full read of your phase's Hindu texts in the original
  Sanskrit (Vedic and Classical), and in the vernaculars, Persian and Arabic
  where your phase includes them.
- **The standard:** the same as the Hebrew Bible, Quran and ancient Near
  East reads.
- **Afterwards:** compare the texts read with the Quran side by side.

**Central and Eastern rounds:** follow "Central and Eastern traditions" in `docs/prompts/reading-at-scale.md` as well: the route graph, decoy pairs, the image and argument records, the translators' lexicon, and the Islamic reception layer for this tradition.

## Start here

1. Base your work on `main`. Develop on your session's designated branch,
   created from `main`, and push there. Do not push to `main`.
2. Read these, in order:
   - `README.md`
   - `PLAN.md`, especially "Standing requirements for every text",
     "Grounding in the originals" and the concept layer
   - `TRADITIONS.md`: the Hinduism section, and the Zoroastrianism section
     for the shared Indo-Iranian vocabulary
   - `leads/README.md`
   - `docs/prompts/reading-at-scale.md`: the method, the tools, the lessons
     and the translation protocol. Follow it.
   - `docs/CLEANUP.md`, including the entries of earlier phases
   - `data/motif-tags/ane/README.md`: the reading protocol to adapt
   - `data/ane/SCOPE.md`: the model for the scope file
   - `data/alignments/README.md`
3. Run `python3 tools/fetch.py` and `python3 tools/anefetch.py`. From phase 2
   on, read the earlier phase's SCOPE.md and reuse its tools.
4. Use the shared concept vocabulary `data/concepts.yaml` if it exists.
   Otherwise build one as `docs/prompts/christian-philosophy-full-read.md`
   phase 3 describes, and record it in `docs/CLEANUP.md` for merging.

## Corpus

- **Ids:** corpus `hindu`, tradition `hinduism`. Add the tradition to
  `data/traditions.yaml` if it is missing.
- **Folders:**
  - raw data: `data/raw/hindu/`
  - tags: `data/motif-tags/hindu/`
  - scope file: `data/hindu/SCOPE.md`, one section per phase
- **References:** use the standard ones, written as `RV 10.129.1`,
  `ŚB 1.8.1.1`, `BĀU 1.4.10`, `BhG 2.47`, `MBh 3.185.1`, `Rām 1.1.1` and
  `BhP 8.24.1`. Record the edition each follows (for the epics, the critical
  editions).

## Phases

### Phase 1: the Vedic and Upanishadic core, philosophy, and the Indo-Persian encounter

- **Rigveda, in full.** Use VedaWeb (Cologne; TEI on GitHub
  `cceh/c-salt_vedaweb_tei`, reachable) or the DCS lemmatized text; record
  the edition. Key passages include the creation hymn (*Nāsadīya*,
  RV 10.129), the sacrifice of the primordial person (*Puruṣa Sūkta*,
  RV 10.90) and the golden embryo (*Hiraṇyagarbha*, RV 10.121).
- **Other Saṃhitās.** The Atharvaveda in full where open. For the Yajurveda
  and Sāmaveda, read the hymnal and mantra core and state the selection.
- **Brāhmaṇas.** The narrative portions of the *Śatapatha Brāhmaṇa*,
  including Manu and the fish (ŚB 1.8.1) and the creation and sacrifice
  myths; the *Aitareya Brāhmaṇa* (Śunaḥśepa); the *Jaiminīya Brāhmaṇa*
  narratives where open.
- **Upaniṣads.** The principal Upaniṣads in full: *Bṛhadāraṇyaka*,
  *Chāndogya*, *Taittirīya*, *Aitareya*, *Kauṣītaki*, *Kena*, *Kaṭha*,
  *Īśā*, *Muṇḍaka*, *Māṇḍūkya*, *Praśna*, *Śvetāśvatara*, *Maitrī*.
- **Bhagavad Gītā,** in full.
- **Philosophy.** Patañjali, *Yoga Sūtras*; Bādarāyaṇa, *Brahma Sūtras*;
  the *Sāṃkhya Kārikā*; Śaṅkara's *Upadeśasāhasrī*.
- **Indo-Persian and Arabic texts.** Their Quranic and Sufi vocabulary is
  part of the Islamic analysis; there is no separate Sufi round. Read:
  - Dārā Shikōh, *Majmaʿ al-Baḥrayn* (Persian) and *Sirr-i Akbar* (the
    Upaniṣads in Persian), where open;
  - al-Bīrūnī, *Taḥqīq mā li-l-Hind* (Arabic; Sachau's 1887 edition is
    public domain, try the Internet Archive) and his *Kitāb Pātanjal*,
    where open;
  - the *Amṛtakuṇḍa* in its Arabic or Persian versions (*Ḥawḍ al-ḥayāt*),
    where open.

### Phase 2: the epics

- **Rāmāyaṇa** (Vālmīki), in full, from the critical edition.
- **Mahābhārata,** in full, from the critical edition: the narrative, the
  *Nārāyaṇīya*, the *Anuśāsana* and *Śānti* teachings, and the flood story
  of Manu and the fish (MBh 3.185).
- **Harivaṃśa,** where open.

At about 2,000 verses a chunk, the Mahābhārata alone is about 40 chunks.
Run waves of 8 and resume after API limits, as `reading-at-scale.md`
describes.

### Phase 3: the Purāṇas and Bhakti

- **Purāṇas.** *Bhāgavata* in full; *Viṣṇu*; *Matsya*, with the flood
  (Matsya 1–2); *Mārkaṇḍeya*, with the *Devīmāhātmya*; *Śiva*; *Liṅga*
  (selected). Record each one's extent in SCOPE.md.
- **Bhakti.**
  - Tulsīdās, *Rāmcaritmānas* (Awadhi), and the *Dohāvalī* and *Kavitāvalī*
    (GRETIL).
  - Sūrdās and Mīrābāī where open.
  - The Tamil Āḻvārs (the *Nālāyira Divya Prabandham*) and Nāyaṉmārs
    (*Tēvāram*), where open machine-readable editions exist.
  - Kabir is read in the Sikh round from the Guru Granth Sahib. Read the
    other Kabir collections (the *Bījak*) here if open.
- **Persian translations of the epics,** if open: the Mughal *Razmnāma*
  (the Mahābhārata) and Persian Rāmāyaṇas.

## Sources (probe each; most were reachable from a sibling session)

- **Digital Corpus of Sanskrit (DCS)**, lemmatized and morphologically
  tagged. The data is on GitHub (OliverHellwig). Attach the repository with
  `add_repo` if it is not reachable through `raw.githubusercontent.com`;
  check its license. Prefer it wherever it covers a text: its lemmas feed
  the lexical work.
- **GRETIL** (gretil.sub.uni-goettingen.de, reachable): Sanskrit, Prakrit and
  New Indo-Aryan e-texts, with a bulk download per section. Check the
  terms per text.
- **VedaWeb** (Cologne) and its TEI repository, for the Rigveda.
- **TITUS**, for Vedic texts.
- **sanskritdocuments.org**: many texts; check its terms.
- **The critical editions of the epics** (BORI's Mahābhārata, Baroda's
  Rāmāyaṇa) as e-texts via GRETIL; record the edition.
- **Internet Archive**, for public-domain editions and translations:
  - Sachau's al-Bīrūnī;
  - *Sacred Books of the East* translations (Max Müller's Upaniṣads,
    Eggeling's *Śatapatha*), as reading aids only.
- **Not usable:** sacred-texts.com is blocked by the proxy.

## Concept layer

Tag concepts beside motifs. Examples:

- *ṛta* and *dharma* (cosmic and moral order);
- the unity of the self and the absolute (*ātman*–*brahman*);
- *māyā*;
- *karma* and rebirth;
- liberation (*mokṣa*);
- devotion (*bhakti*);
- divine descent (the avatars);
- the impersonal and the personal godhead (*nirguṇa*/*saguṇa*);
- the cosmic ages (*yugas*) and their dissolution (*pralaya*);
- sacrifice as the order of the world;
- renunciation;
- the divine name and its recitation;
- creation from the One's desire.

## Known leads (benchmarks, not reading targets)

- Manu and the fish ↔ the flood
- Dārā Shikōh's *Majmaʿ al-Baḥrayn* and *Sirr-i Akbar*
- al-Bīrūnī's *Taḥqīq mā li-l-Hind* and *Kitāb Pātanjal*

These are already known. They are **benchmarks**: after the read, check that
the pipeline surfaces them. Do not give them to the readers, and do not read
for them. Follow "Discovery, not confirmation" in
`docs/prompts/reading-at-scale.md`: the aim is the specific detail nobody has
listed yet.

## Lexical

Indo-Iranian inheritance (*deva*/*daēva*, *asura*/*ahura*, *Mitra*/*Mithra*,
*soma*/*haoma*, *ṛta*/*aša*) is the Zoroastrian round's ground. Coordinate
through `tools/anelex.py`'s Iranian branch, and add the Sanskrit side here.

Sanskrit loans in Quranic Arabic are few and contested. The candidates:
- *zanjabīl* ← *śṛṅgavera*, through Middle Persian;
- *misk* ← Middle Persian *mušk* ← Sanskrit *muṣka*;
- *kāfūr* ← *karpūra*;
- *sundus*, contested.

Benchmarks:
- *kāfūr* ← *karpūra* (Q 76:5) and *zanjabīl* (Q 76:17) **should** be
  recovered through the Iranian branch.
- The others are recorded with `expect: false` if missed.

## Every phase ends with

1. Merging near-duplicate motifs and concepts.
2. The **Hindu × Quran comparison** for the texts read in that phase, on motifs and concepts alike (a concept match needs a specific shared formulation, argument or image, not a shared or opposed doctrine).
   - Use neutral ids for divergences.
   - Quote the decisive Sanskrit (transliterated) and the Arabic.
3. The pipeline run, with every benchmark passing.
4. A dated `docs/CLEANUP.md` entry. List as deferred the comparisons with
   the Hebrew Bible, the ANE, Zoroastrianism, Buddhism, Jainism and Sikhism.
5. A report:
   - the inventory: read from the original, from a translation, and left
     out;
   - the benchmarks;
   - the comparison counts by relation;
   - the most interesting Hindu ↔ Quran leads and divergences, with
     references on both sides.

## Rules

- **Originals first.** Every claim states its basis.
- **Dates.** Vedic and epic dating is uncertain. Use direction-neutral
  wording, and keep leads at `standing: proposed`.
- **Licenses.** Check each source's license, and keep raw text out of git.
- **Respect.** These are living traditions. Keep notes descriptive and
  respectful, and record sectarian and scholarly disputes neutrally.
- Don't create pull requests unless asked.
- Don't edit other sessions' tag or alignment folders. The pilot unit
  `hin-shatapatha-manu` in `data/motif-tags/flood.yaml` is tagged from
  secondary knowledge: **replace it** in phase 1 with units read from
  ŚB 1.8.1, and keep the flood benchmarks passing.
