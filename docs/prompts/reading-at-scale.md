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
- **Pilot one chunk before a wave.** In the ANE comparison, the pilot exposed
  slow tools, a YAML trap and a flag rule that could never fire. Fixing them
  before the other 30 chunks saved a wave.
- **Readers build their file in their scratch folder.** They copy it into
  the repo only when it is complete, then validate it there. The validator
  needs the repo copy, because it loads the other chunks' motif ids.
  - In the ANE session, half-written chunk files in the repo broke other
    chunks' validation and the motif loader.
  - They also forced about 75 "WIP snapshot" commits to keep the stop hook's
    tree clean.
- **Validate and commit each chunk as it arrives**, with a commit message
  naming its range. The commit script must stop on a failed validation: use
  `set -o pipefail`, or don't pipe the validator through `tail`.
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
  `<corpus> × Islam`: the Quran, and the hadith corpus once it is read
  (`docs/prompts/hadith-full-read.md`). Readers' hints written as
  `Q surah:verse` become its candidates. Write one only when a particular Quran passage comes to
  mind for a particular detail (see "Discovery, not confirmation"). Hebrew
  Bible references are welcome as secondary hints.
- **Reuse motif ids.** The vocabulary holds the HB, Quran, ANE and later
  ids: search by keyword, reuse the Quran readers' ids first, never redefine
  an id with a different label, and define new ones only after searching.
  The ANE read still left 4,459 of its 7,377 ids used once, so search harder
  before defining.
- **Labels describe the line in its own terms.**
  - Never word a tag label after the parallel the reader has in mind.
  - ANE examples that did: `yhwh-my-shepherd` on a Sumerian line,
    `adopt-as-son-perhaps-useful` in the Q 28:9 wording on a Hittite text
    that lacks the clause.
  - Such labels leak the reader's hint to blind judges and put on the line
    words it does not say.
  - The comparison belongs in `hints`.
- **Versions and manuscript witnesses are separate units**, with `version`
  set. Mark each copy with `witness_of: <unit id of the best witness>`. The
  comparison then records a correspondence once, on the best witness. In the
  ANE pass, BD 125, Sinuhe and the SAA 2 6 / 15 treaty copies counted the
  same finding several times.
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

## Central and Eastern traditions

The western rounds rested on contact. The ANE, the Hebrew Bible and the Quran share Semitic roots,
story lines and legal forms, so a shared motif or cognate is evidence. Farther east that thins:
there are few cognates and few shared stories, contact runs through intermediaries (Persian,
Manichaean, Sogdian, Arabic translation, the Mughal court), and many texts are later than the
Quran. Run unchanged, the motif method would return either universal motifs (floods, cosmic eggs,
ascetics) or the worldview contrasts that "Discovery, not confirmation" rules out. These rounds add
six methods.

1. **Routes first.** Before comparing, record the documented transmission routes with their dates
   in `data/routes.yaml`, each with a source. Examples:
   - the Pañcatantra → Pahlavi → Ibn al-Muqaffaʿ's *Kalīla wa-Dimna*;
   - the Buddha legend → *Bilawhar wa-Būdhāsaf*;
   - Sanskrit astronomy and medicine through Pahlavi (Ibn al-Nadīm lists the Indian books in Arabic);
   - Manichaean Sogdian and Uyghur;
   - al-Bīrūnī's Arabic Sāṃkhya and Patañjali;
   - Dārā Shikōh's Persian Upaniṣads and Akbar's Persian *Razmnāma*;
   - the Chinese Islamic writings (Han Kitab).

   Every match then carries one of three labels: `route` (a documented path whose dates fit),
   `reception` (the text is later than the Quran) or `convergence` (no route). Convergence is a
   result, labelled as such. The labels say nothing about the direction of influence.
2. **Decoy pairs.** The coordinator slips pairs of units known to be unrelated into each judge's
   chunk, without saying which, and reports the rate at which judges find matches in them. Each
   round states its measured false-match rate beside its match rate.
3. **Other corpora as controls.** Before a match is called notable, check whether the same element
   recurs in the ANE, Greco-Roman or Iranian corpora. A widespread element is weaker evidence than
   a rare one. Record the check on the match.
4. **Images and argument forms, not doctrines.** Record similes as three slots: what is described,
   the image used, and the point of likeness. Record arguments by their form, as in "they cannot
   hear you" or "rain revives dead earth, so…". For example, the spider is the creator spinning out
   the world and drawing it back in Bṛhadāraṇyaka 2.1.20 and Muṇḍaka 1.1.7, and the frailest of
   houses for false protectors in Q 29:41. That is a specific divergence, not a doctrinal contrast.
5. **Historical translators' equivalences.** Build a lexicon only from equivalences a historical
   translator chose, each sourced: Liu Zhi's *zhenzhu* 真主 for God, Dārā Shikōh's Brahman =
   *al-Ḥaqq*, al-Bīrūnī's Arabic rendering of Patañjali's terms. These give concept matches that
   come from the period, not from us, and they anchor the concept layer.
6. **Practice in exact terms.** Record the numbers and directions of ritual: prayer times and
   prostrations, fasting rules, purity and what defiles, dietary law, the direction of
   circumambulation (pradakṣiṇa keeps the shrine on the right, ṭawāf keeps the Kaaba on the left).

Two more rules for these rounds:
- **Tag in each tradition's own terms.** Write *tīrthaṅkara*, *bodhisattva*, *kami*, never
  "prophet" or "angel". Map to Islamic terms only when comparing, or the reading forces Islamic
  categories onto the texts.
- **Mark retrieval-assisted reading.** For the largest canons (the Chinese Buddhist canon, the full
  Purāṇas), retrieval anchored on the Quran's observation records may be needed to choose what to
  read closely. It carries the confirmation risk, so pair it with decoys and label it in SCOPE.md.

### How Islamic scholars read these traditions: a reception layer

Muslim scholars examined these traditions for a thousand years. Their works belong in the project in
three ways:
- as **reception texts**, read on the Islamic side as part of the Islamic analysis, with no separate
  round;
- as **sources for the route graph and the translators' lexicon**;
- as a **benchmark of what was already noticed**, so that our leads are measured against it.

Located in the Shamela library (cite as `shamela_get_citation` gives; page numbers as printed unless
noted):

- **al-Bīrūnī (d. 440), *Taḥqīq mā li-l-Hind* (Shamela 11655).** The method precedent for this project.
  - His book "is not a book of argument and polemic … but a book of report (*kitāb ḥikāya*): I give
    the words of the Indians as they are, and add what the Greeks have like them, to show the
    nearness between them". He brings in the Sufis or Christians only "because of the closeness of
    the matter among them all in *ḥulūl* and *ittiḥād*" (p. 16).
  - He had translated the Sāṃkhya and Patañjali into Arabic (p. 16), and he sets Patañjali's path
    beside Sufi sayings throughout (pp. 28, 44, 52, 56, 59, 62).
  - So: report each side in its own terms, and compare only where a specific closeness exists.
- **al-Shahrastānī (d. 548), *al-Milal wa-l-niḥal* (Shamela 11812).**
  - He divides the Brahmins into followers of the Budd, followers of meditation, and followers of
    transmigration (3/97).
  - He defines the Budd as "a person in this world who is not born, does not marry, does not eat…"
    (3/97), with ten stages ending in giving up the spirit in longing for the Real (3/98).
  - An early doxographic reading of Buddhism.
- **Ibn al-Nadīm (d. 380), *al-Fihrist* (Shamela 1455, Ayman al-Sayyid's edition).**
  - The translators from Indian languages (2/424 ff.), the Indian scholars whose books on
    astronomy and medicine reached Arabic, and a list of Indian medical books in Arabic.
  - The temples of India and the *budd* images, partly after Abū Dulaf's report (2/424-428).
  - A ready source for the route graph.
- **Abū Zayd al-Sīrāfī (fl. 4th c.), *Riḥla* (Shamela 11269).** Merchant reports on India and China:
  - cremation (heading at title 29);
  - the abstinence of Indian kings (title 31);
  - the people of India and China holding that "the *budd* speak to them, when it is their
    worshippers who speak" (p. 50).
- **The *Sumaniyya*** (śramaṇas) run through Islamic theology and legal theory (360 hits): from Jahm's
  debate with them (al-Bukhārī, *Khalq afʿāl al-ʿibād*, p. 30) to the jurists' theory of knowledge
  (al-Juwaynī, *al-Talkhīṣ* 2/281). They appear as the party that limits knowledge to the senses and
  denies knowledge by mass-transmitted report. That is an argument-form record of exactly the kind
  method 4 calls for.
- **South Asia, in ʿAbd al-Ḥayy al-Ḥasanī (d. 1341), *Nuzhat al-khawāṭir* (Shamela 1584),** the
  biographical dictionary of Muslim India:
  - Dārā Shikōh's Persian Upaniṣads, whose preface calls the text "the kernel of the Quran", and his
    "book on reconciling (*al-taṭbīq*) the creed of the Hindus with that of the people of Islam",
    with the two opposed judgments of him reported side by side (5/527);
  - Badāyūnī's Persian translation of the Atharvaveda, which "they claim agrees in some rulings with
    the Islamic Sharia", made with a Brahmin convert (5/570);
  - the Mahābhārata translated as the *Razmnāma* (5/498, 5/534);
  - scholars who studied with Brahmins, debated "the scholars of the Hindus", or answered
    Rammohun Roy's Brahmo Samaj (7/972).
- **Sulaymān al-Nadwī (d. 1373), *al-Risāla al-Muḥammadiyya* (Shamela 9821),** lectures given in India.
  He argues that the founders' lives are not historically recoverable in the case of the Buddha
  (p. 43) and still less of Confucius. This is a historicity argument, one that sets the founders'
  biographies against the Prophet's documented sīra.
- **Muḥammad Sulaymān Manṣūrpūrī (d. 1348), *Raḥmatan li-l-ʿĀlamīn* (Shamela 14328, translated from
  Urdu).**
  - Reads Q 35:24, "there is no community but a warner has passed among it", as the ground for
    honouring the righteous of the Hindus and for mutual respect between the nations' teachers
    (p. 964).
  - Sets tayammum against the 36-ingredient *havan* the Ārya Samāj prescribes for worship, citing
    the *Satyārth Prakāś* (p. 700).
  - Answers the objection that the splitting of the moon would appear in Hindu books (p. 740).
- **Southeast Asia.** It appears in Shamela mainly through questions sent to the Arab heartlands, for
  example Ibn Yaʿqūb al-Madanī (d. 1066), *al-Jādda al-qawīma … fī l-jawāb ʿan al-asʾila al-wārida
  min Jāwa*, on the question of being (in Ismāʿīl Bāshā, *Hadiyyat al-ʿārifīn* 1/245).

**Gaps outside Shamela.** Some of the most important works are not in Arabic or not in Shamela:
- Persian: Dārā Shikōh's *Majmaʿ al-Baḥrayn* and *Sirr-i Akbar*, Aḥmad Sirhindī's *Maktūbāt*;
- Chinese: the Han Kitab of Wang Daiyu and Liu Zhi;
- Malay: Nūr al-Dīn al-Rānīrī's *Tibyān fī maʿrifat al-adyān*;
- Urdu originals.

Each round lists them in its SCOPE.md and reads them where an open text exists. They are reception
texts in their own right.

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
   - **Use `docs/prompts/comparison-judge.md`** as the judge prompt. It
     carries the lessons of the ANE pass:
     - **Judge blind.** Without the readers' hints and candidate reasons,
       judges found matches no reader had tagged, such as the root ḥ-n-p in
       EA 288 against *ḥanīf*.
     - **One `dump` per chunk,** not per-unit tool calls.
     - **Every match carries an observation record.**
     - **An empty result is the norm.** About 75% of ANE units had no match.
   - **Candidates are weak; judges must search.** In the ANE pass, label
     similarity produced 80% of the candidates, and few of them held up.
     Many of the best matches were with Quran units no tool had proposed.
     - Give judges a quick way to list and search every unit of the other
       side.
     - Treat lexical-trace candidates with suspicion (*imnu*/*ayman* proposed
       dozens of unrelated pairs).
   - **Keep one shared list of new neutral ids** between waves, so parallel
     judges reuse each other's ids instead of coining overlapping ones
     (`no-one-changes-the-spoken-word` ~ `immutable-divine-word`).
   - **Records need shared wording.** Where both texts agree, write the same
     words on both sides of a slot. The one-slot divergence flag found only
     3 of 1,105 ANE matches, because judges worded agreeing sides
     differently.
3. **Run the pipeline:** `motifs.py --write-leads`, `lexical.py
   --write-leads`, `linguistic.py`, `originals.py`, `coverage.py` and
   `build.py`. All benchmarks must pass, apart from documented expected
   misses.
   - Run it once with `--write-leads` midway through a session too. In the
     ANE session a lead-writing bug surfaced only at the end.
   - Check the leads a new layer writes before committing them. The first
     run wrote 108 chain leads for ordinary shared Semitic words (*akālu* ~
     *akala*). Only chains classed `loan` become leads; inherited cognates
     are background.
4. **Add a dated entry to `docs/CLEANUP.md`**, and report back as the
   prompt asks.
