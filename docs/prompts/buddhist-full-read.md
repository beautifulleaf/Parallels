# Prompt: full read of the Buddhist scriptures (three phases)

The Buddhist canons are vast: the Pali canon alone has about 2.7 million
words, and the Chinese canon is far larger. The round is split into **three
phases, one or more sessions each, run in order**. Paste everything below the
line into a new Claude Code session attached to the `beautifulleaf/parallels`
repository, and **set the phase** in the first line.

---

**Phase: <1 | 2 | 3>** (see "Phases" below; do only your phase)

You are continuing **Parallels**, a lead-generation project in the
`beautifulleaf/parallels` repository. It finds parallels, convergences and
responses between religious traditions. **It is a Quran-centred project.**

Your job is a full read of your phase's Buddhist texts:
- in the original Pali, Buddhist Sanskrit, Gāndhārī, Chinese or Tibetan;
- or in Arabic and Persian where the phase includes them;
- or, where no open original exists, from an openly licensed translation,
  labelled as such.

Hold the read to the standard of the Hebrew Bible, Quran and ancient Near
East reads. After it, compare the texts with the Quran side by side.

## Start here

1. Base your work on `main`. Develop on your session's designated branch,
   created from `main`, and push there. Do not push to `main`.
2. Read these, in order:
   - `README.md`
   - `PLAN.md`, especially "Standing requirements for every text",
     "Grounding in the originals" and the concept layer
   - `TRADITIONS.md`: the Buddhism section, and the Manichaeism section for
     the Turfan exchange
   - `leads/README.md`
   - `docs/prompts/reading-at-scale.md`: the method, tools, lessons and
     translation protocol. Follow it.
   - `docs/CLEANUP.md`, including the entries of earlier phases
   - `data/motif-tags/ane/README.md`: the reading protocol to adapt
   - `data/ane/SCOPE.md`: the model for the scope file
   - `data/alignments/README.md`
3. Run `python3 tools/fetch.py` and `python3 tools/anefetch.py`.
   - From phase 2 on, read the earlier phases' SCOPE files and reuse their
     tools.
4. Use the shared concept vocabulary `data/concepts.yaml` if it exists.
   Otherwise build one as `docs/prompts/christian-philosophy-full-read.md`
   phase 3 describes, and record it in `docs/CLEANUP.md` for merging.

## Corpus

- **Ids:** corpus `buddhist`, tradition `buddhism`. Add the tradition to
  `data/traditions.yaml` if it is missing.
- **Folders:**
  - raw data: `data/raw/buddhist/`
  - tags: `data/motif-tags/buddhist/`
  - scope file: `data/buddhist/SCOPE.md`, one section per phase
- **References:** cite by the SuttaCentral ids (`dn16:1.1`, `mn26:5`,
  `sn56.11:1`, `dhp1`) and the Taishō numbers (`T262` with the fascicle and
  line).

## Phases

### Phase 1: the early discourses, the Buddha legend and the Barlaam chain

- **The Sutta Piṭaka in Pali, in full.** That is the *Dīgha*, *Majjhima*,
  *Saṃyutta* and *Aṅguttara Nikāyas*.
- **The early Khuddaka:**
  - *Dhammapada*;
  - *Sutta Nipāta*;
  - *Udāna*;
  - *Itivuttaka*;
  - *Theragāthā* and *Therīgāthā*.
- **The Vinaya's narrative portions:** the *Mahāvagga* (the awakening and
  the first sermons) and the *Cullavagga* (the councils, the founding of
  the order of nuns).
- ***Milindapañha*** (a Greek king questions the monk Nāgasena).
- **The Buddha-legend texts behind the Barlaam chain:**
  - *Lalitavistara* (Sanskrit);
  - Aśvaghoṣa, *Buddhacarita*;
  - *Mahāvastu*, where open (all three via GRETIL and the DSBC);
  - the *Nidānakathā* (the introduction to the Jātakas).
- **The Islamic response texts on the Buddha.** They are part of the
  Islamic analysis, with no separate Sufi round. Read them where open:
  - the Arabic *Kitāb Bilawhar wa-Būdhāsf*. Check the Shamela tools in this
    environment, and the Internet Archive for public-domain editions;
  - Ibn Bābawayh's version;
  - the *Life of the Buddha* in Rashīd al-Dīn's *Jāmiʿ al-tawārīkh*.

### Phase 2: the Mahāyāna sūtras and the Jātakas

- **The Mahāyāna sūtras:**
  - the Lotus Sūtra (Sanskrit, and Kumārajīva's Chinese, T262);
  - the core *Prajñāpāramitā* (the Heart, the Diamond, the
    *Aṣṭasāhasrikā*);
  - the *Vimalakīrtinirdeśa*;
  - the Pure Land sūtras (the larger and smaller *Sukhāvatīvyūha*, the
    Contemplation Sūtra);
  - the *Laṅkāvatāra*;
  - the *Avataṃsaka* (the *Gaṇḍavyūha*, selected).
- **The Jātakas:** the Pali Jātaka verses and stories, in full.
- **The Chinese Āgamas** (*Dīrgha*, *Madhyama*, *Saṃyukta*, *Ekottara*),
  read only where they diverge from the Pali. SuttaCentral's parallel maps
  show which do.

### Phase 3: Tibetan and Chinese-only works, selected

State the selection rule in SCOPE.md. Candidates:

- **Tibetan:**
  - Kangyur sūtras with no Indic original, from 84000's translations, read
    as translation; check 84000's license;
  - Milarepa;
  - the Tibetan Book of the Dead (*Bardo Thödol*) if open.
- **Chinese:** the Platform Sūtra; the Chinese apocrypha (the *Sūtra of
  the Ten Kings*, on the judgment of the dead, and Maitreya scriptures).
- **The Buddhist–Manichaean and Buddhist–Christian texts in Chinese and
  Uyghur**, where the Manichaean round did not read them.

## Sources (probe each; most were reachable from a sibling session)

- **SuttaCentral, `bilara-data` on GitHub.** It has the Pali root texts
  segment by segment, with Bhikkhu Sujato's English, which is CC0. Its
  parallel tables map Pali, Chinese, Sanskrit and Tibetan parallels; use
  them as **a ready-made benchmark** for the motif track, as `TRADITIONS.md`
  notes. The API is reachable (`suttacentral.net/api/...`). Prefer the bulk
  data.
- **CBETA, `cbeta-org/xml-p5` on GitHub:** the Taishō canon in TEI. Check
  its license (CC BY-NC-SA). The CBETA website itself refused requests.
- **GRETIL and the Digital Sanskrit Buddhist Canon (DSBC):** Buddhist
  Sanskrit texts.
- **84000:** English translations of the Kangyur. Check the license; the
  translations are not originals.
- **Lemmas:** the Digital Pali Dictionary and its open data, if it is
  reachable. Lemmatize with it where the text has no lemmas.
- **Not usable:** sacred-texts.com is blocked by the proxy.

## Concept layer

Tag concepts beside motifs:

- the four truths;
- dependent origination;
- non-self (*anattā*) against the soul;
- impermanence;
- karma and rebirth;
- nirvana;
- the bodhisattva and compassion;
- emptiness (*śūnyatā*);
- the Buddha's nature and bodies;
- the Pure Land;
- the future Buddha (Maitreya);
- the cosmos of world systems and its eons;
- the hells and the judgment of the dead;
- renunciation and the order of monks and nuns;
- the gods (*devas*) as beings within saṃsāra.

## Known leads (benchmarks, not reading targets)

- the Buddha legend → *Bilawhar wa-Būdhāsf* → Barlaam and Josaphat
- the *Milindapañha*
- Dhul-Kifl ↔ the Buddha (fringe)

These are already known. They are **benchmarks**: after the read, check that
the pipeline surfaces them. Do not give them to the readers, and do not read
for them. Follow "Discovery, not confirmation" in
`docs/prompts/reading-at-scale.md`: the aim is the specific detail nobody has
listed yet.

## Lexical

Buddhist loans in Quranic Arabic: none is established. Record the
*Būdhāsf*/*bodhisattva* chain (Sanskrit, then Middle Persian, then Arabic)
as a lexical lead outside the Quran. Build the Pali and Sanskrit adapters for
the linguistic layer.

## Every phase ends with

1. Merging near-duplicate motifs and concepts.
2. The Buddhist × Quran comparison for the texts read in that phase, on motifs and concepts alike (a concept match needs a specific shared formulation, argument or image, not a shared or opposed doctrine), with neutral ids for divergences.
   - Quote the decisive Pali, Sanskrit or Chinese and the Arabic.
   - Divergences matter as much as parallels, but only specific ones (see
     "Discovery, not confirmation" in `reading-at-scale.md`). Worldview-level
     contrasts true of whole traditions are not findings: never record them.
3. Running the pipeline, with every benchmark passing. This includes the
   **SuttaCentral parallel benchmark**: known Pali–Chinese parallels must
   rank among each unit's top matches.
4. A dated `docs/CLEANUP.md` entry. List as deferred the comparisons with
   Hinduism, Jainism, Manichaeism, Chinese religion and Christianity
   (Barlaam).
5. A report:
   - the inventory: read from the original, from a translation, and left
     out;
   - the benchmarks;
   - the comparison counts by relation;
   - the most interesting Buddhist ↔ Quran leads and divergences, with
     references on both sides.

## Rules

- **Originals first.** Every claim states its basis.
- **Licenses.** Check each source's license, and keep raw text out of git.
- **Respect.** These are living traditions. Keep notes descriptive and
  respectful, and record sectarian canon differences neutrally.
- Don't create pull requests unless asked.
- Don't edit other sessions' tag or alignment folders.
