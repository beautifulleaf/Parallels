# Prompt: full read of the Jewish and Samaritan corpora (post-biblical)

This round is too large for one session: the classical rabbinic corpus alone
is several times the size of the ancient Near East read. It is split into
**four phases, one session each, run in order**. Paste everything below the
line into a new Claude Code session attached to the `beautifulleaf/parallels`
repository, and **set the phase** in the first line.

---

**Phase: <1 | 2 | 3 | 4>** (see "Phases" below; do only your phase)

You are continuing **Parallels**, a lead-generation project in the
`beautifulleaf/parallels` repository. It finds parallels, convergences and
responses between religious traditions. **It is a Quran-centred project.**
The Hebrew Bible has already been read in full. Your job is a full read of the
post-biblical Jewish and Samaritan literature, done to the standard of the
Hebrew Bible, Quran and ancient Near East reads:

- Read in the original Hebrew and Aramaic, plus Greek, Ge'ez or Arabic where
  that is what survives.
- Where only a translation is open, read the translation and label the units
  as such.
- After the read, compare these texts with the Quran side by side.

## Start here

1. Base your work on `main`. Develop on your session's designated branch,
   created from `main`, and push there. Do not push to `main`.
2. Read these, in order:
   - `README.md`
   - `PLAN.md`, especially "Standing requirements for every text" and
     "Grounding in the originals"
   - `TRADITIONS.md`: the Judaism and Samaritanism sections
   - `leads/README.md`
   - `docs/prompts/reading-at-scale.md`: the method, the tools to reuse,
     the lessons and the translation protocol. Follow it.
   - `docs/CLEANUP.md`, including the entries of earlier phases
   - `data/motif-tags/ane/README.md`: the reading protocol to adapt
   - `data/ane/SCOPE.md`: the model for the scope file
   - `data/alignments/README.md`
3. Run `python3 tools/fetch.py` and `python3 tools/anefetch.py`.
4. **From phase 2 on**, read the earlier phases' `data/<corpus>/SCOPE.md`
   files and reuse their tools. Don't rebuild them.

## Corpora and folders

| Corpus id | Contents | Folders |
|---|---|---|
| `second-temple` | the Pseudepigrapha, Ben Sira, the Dead Sea Scrolls, Philo and Josephus (selected) | `data/raw/second-temple/`, `data/motif-tags/second-temple/` |
| `samaritan` | the Samaritan Pentateuch, Targum, *Tibat Marqe*, liturgy and chronicles | `…/samaritan/` |
| `targum` | the Targums of the Pentateuch, the Prophets and the Writings | `…/targum/` |
| `rabbinic` | the Mishnah, Tosefta, halakhic and aggadic midrash, both Talmuds | `…/rabbinic/` |

Tradition ids:
- `judaism` for the Jewish corpora.
- Add `samaritanism` to `data/traditions.yaml` if it is missing.

## Phases

### Phase 1: Second Temple, Samaritan, Targums

**Second Temple.** Every text carries its own language note:

- **Jubilees:** Hebrew fragments from Qumran; otherwise the Ge'ez text, or
  Charles's public-domain translation, labelled.
- **1 Enoch:** the Aramaic Qumran fragments and the Ge'ez; *The Book of the
  Watchers* and the *Book of Giants* are key.
- **Ben Sira:** the Hebrew manuscripts (Cairo Genizah, Masada) where open;
  otherwise the Greek.
- **Testaments of the Twelve Patriarchs** and **Joseph and Aseneth**: the
  Greek.
- **Wisdom of Solomon** and **Tobit**.
- **Life of Adam and Eve**, Greek *Apocalypse of Moses*. Coordinate with
  the Christian session if it already read it.
- **Apocalypse of Abraham:** Slavonic only, so a translation.
- **Dead Sea Scrolls**, the sectarian texts: the Community Rule, War Scroll,
  Damascus Document, Hodayot, Genesis Apocryphon, Temple Scroll, and
  4QMMT. The ETCBC `dss` Text-Fabric dataset is on GitHub, and
  raw.githubusercontent.com is reachable from these sessions; check its
  license.
- **Philo:** *De opificio mundi*, the *Life of Moses* and *De Abrahamo*, in
  Greek (Perseus).
- **Josephus:** *Antiquities* books I–XI in Greek (Perseus), where they
  retell the Bible.

**Samaritan.**

- **Samaritan Pentateuch:** read every variant against the Masoretic text,
  tagging each deliberate one as a divergence. Gerizim in the Decalogue and
  "the place he has chosen" against "will choose" are examples.
- **The Samaritan Targum.**
- ***Tibat Marqe*:** the original if open; Macdonald's 1963 translation is
  under copyright and is not to be used as data.
- **The liturgy:** Cowley, 1909, public domain.
- **The chronicles:** Abu'l-Fatḥ in Arabic (Vilmar 1865, public domain),
  the *Tolidah* and the *Asatir*.
- **The Samaritan Arabic Pentateuch** (Abū Saʿīd), if any open text exists.

**Targums.**

- Onqelos; Pseudo-Jonathan; Neofiti and the Fragment Targums.
- Jonathan to the Prophets.
- The Targums to the Writings: Psalms, Job, Ruth, Esther I and II, Song.

The expansions in the Targums are the point: where a Targum adds to the
Hebrew, tag what it adds. Examples are Cain and Abel's quarrel at Gen 4:8
and Abraham in the furnace at Gen 11:28.

### Phase 2: Mishnah, Tosefta, halakhic midrash

- **Mishnah**, in full.
- **Tosefta**, in full.
- **Mekhilta de-Rabbi Yishmael** and **Mekhilta de-Rabbi Shimon**.
- **Sifra**, **Sifre** (Numbers and Deuteronomy), **Sifre Zuta**.
- **Avot** and **Avot de-Rabbi Natan** (A and B).
- The minor tractates if time allows. State the cut in SCOPE.md.

### Phase 3: aggadic midrash

- **Midrash Rabbah**, all ten books.
- **Tanhuma** (both recensions).
- **Pesiqta de-Rav Kahana** and **Pesiqta Rabbati**.
- **Pirqei de-Rabbi Eliezer**.
- **Seder Olam**, **Midrash Tehillim**, **Midrash Mishle**,
  **Midrash Shmuel**, **Tanna de-Be Eliyahu**.
- **Otzar ha-Midrashim**: the narrative pieces only (Alphabet of Ben Sira,
  Chronicles of Moses, Sefer ha-Yashar), each stated.
- **Hekhalot**: Hekhalot Rabbati and 3 Enoch, if open. These matter for the
  heavenly ascent.

### Phase 4: the Talmuds

- **Yerushalmi**, in full.
- **Bavli**, in full.

The Bavli is the largest single text in the project. Chunk it by tractate
and folio (about 2,000 Sefaria segments per chunk). Expect around 40–60
chunks; run several waves, and resume after API limits as
`reading-at-scale.md` describes.

## Sources (probe each; reachable from a sibling session)

- **Sefaria** has the Mishnah, Tosefta, both Talmuds, midrash and Targums:
  - API: `https://www.sefaria.org/api/texts/...`, `/api/index`;
  - bulk export: the `Sefaria/Sefaria-Export` repository on GitHub.

  Use the bulk export rather than thousands of API calls. Record the license
  of each version used: many Hebrew/Aramaic texts are public domain or
  CC0/CC-BY; some translations are CC-BY-NC, and some are copyrighted.
  Prefer public-domain base texts, such as the Vilna edition for the Bavli.
  Use translations as reading aids only.
- **Dicta** (dicta.org.il): open vocalization and lemmatization tools for
  rabbinic Hebrew. Check its terms. Use it for lemmas where the base text
  has none.
- **The CAL** (cal.huc.edu): Targums and Jewish Aramaic, lemmatized. It asks
  not to be scraped; it offers data dumps on request (skaufman@huc.edu).
  Ask the user to request one if the Targums need its lemmas.
- **ETCBC/dss** for the Scrolls, and **ETCBC/bhsa** for cross-reference to
  the Hebrew Bible already in the repo.
- **Perseus** (GitHub) for Philo and Josephus in Greek.
- **Internet Archive** for public-domain editions and translations: Charles
  1913, Cowley's Samaritan liturgy, and Vilmar's Abu'l-Fatḥ. Use OCR text
  where it is good; record corrections.

## Known leads (benchmarks, not reading targets)

- Genesis Rabbah 38:13 ↔ Abraham and the idols (Q 21:51–70)
- *Pirqei de-Rabbi Eliezer* 21 ↔ Cain and the raven (Q 5:31)
- Mishnah Sanhedrin 4:5 ↔ Q 5:32
- the Watchers ↔ Hārūt and Mārūt (Q 2:102)
- the mountain held over Sinai (b. Shabbat 88a) ↔ Q 2:63
- *al-Sāmirī* and the calf (contested)

These are already known. They are **benchmarks**: after the read, check that
the pipeline surfaces them. Do not give them to the readers, and do not read
for them. Follow "Discovery, not confirmation" in
`docs/prompts/reading-at-scale.md`: the aim is the specific detail nobody has
listed yet.

## Lexical benchmarks (`data/benchmarks/lexical.yaml`)

Extend `tools/anelex.py` with Jewish Aramaic, using the Targums and the
Talmud, and Rabbinic Hebrew, so that Quranic Arabic links to its nearest
Aramaic or Hebrew form.

| Chain | Requirement |
|---|---|
| *gê hinnōm* → *gēhinnām* → *jahannam* | must recover |
| *šəkīntā* / *šəḵīnā* → *sakīna* | must recover |
| Aramaic *purqān* → *furqān* | should recover |
| Aramaic *ṭāʿūtā* → *ṭāghūt* | should recover |
| *rabbān* → *rabbāniyyūn* | should recover |
| *ḥaber* → *ḥibr*, pl. *aḥbār* | should recover |
| *tōrā* → *tawrāt* | should recover |
| *šabbətā* → *sabt* | should recover |
| *Shmuel / Samaritan* ~ *al-Sāmirī* | contested: record the result |

## Every phase ends with

1. Merging near-duplicate motifs.
2. The `<corpus> × Quran` side-by-side comparison for the corpora read in
   that phase, with neutral ids for divergences.

   Divergences matter as much as parallels, but only specific ones (see
     "Discovery, not confirmation" in `reading-at-scale.md`). Worldview-level
     contrasts true of whole traditions are not findings: never record them.
3. The pipeline run, with every benchmark passing.
4. A dated `docs/CLEANUP.md` entry listing what is deferred to later
   phases.
5. A report, in this order:
   - the inventory: read from the original, read from a translation, left
     out;
   - the benchmarks;
   - the comparison counts by relation;
   - the most interesting leads and deliberate divergences, with references
     on both sides.

Do not run comparisons against the Hebrew Bible or the ANE. Record them as
deferred.

## Rules

- **Originals first.** Every claim states its basis.
- **Rabbinic dates are later than many traditions they record.** Leads stay
  `standing: proposed` and use direction-neutral wording ("shared motif",
  never "borrowed from") unless the evidence is directional.
- **Licenses.** Check each source's license; keep raw text out of git.
- **Samaritan sources.** The Samaritans are a small living community; use
  published texts and write respectful, descriptive notes.
- Don't create pull requests unless asked.
- Don't edit other sessions' folders: `hb/`, `quran/`, `ane/`, and the
  existing alignment pairs. The pilot units in `data/motif-tags/abraham.yaml`
  and `joseph.yaml` (Genesis Rabbah 38, Sanhedrin 108b, Sotah 36b, Tanhuma
  Vayeshev) are tagged from secondary knowledge. **Replace them** with units
  read from the original in the phase that reads their source, and keep the
  benchmark pairs in `data/benchmarks/motifs.yaml` passing.
