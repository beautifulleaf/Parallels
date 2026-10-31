# Prompt: full read of Chinese religion and Shinto

Paste everything below the line into a new Claude Code session attached to the
`beautifulleaf/parallels` repository. Plan for the round to continue into a
second session; the scope file and the chunk plan make that seamless.

---

You are continuing **Parallels**, a lead-generation project in the
`beautifulleaf/parallels` repository. It finds parallels, convergences and
responses between religious traditions. **It is a Quran-centred project.**

Your job is a **full read of the Chinese religious classics (Confucian,
Daoist, Neo-Confucian), the Chinese texts of the Abrahamic religions (the Han
Kitab and the Nestorian and Kaifeng steles), and the Shinto myth and ritual
corpus**:

- read in the original Classical Chinese, kanbun and Old Japanese;
- where no open original exists, read from public-domain translations,
  labelled;
- hold the read to the standard of the Hebrew Bible, Quran and ancient Near
  East reads;
- follow it with a side-by-side comparison with the Quran.

## Start here

1. Base your work on `main`. Develop on your session's designated branch,
   created from `main`, and push there. Do not push to `main`.
2. Read these, in order:
   - `README.md`
   - `PLAN.md`: "Standing requirements for every text", "Grounding in the
     originals", and the concept layer; note that the Han Kitab ↔ Zhu Xi
     pair is in the v0 gold set
   - `TRADITIONS.md`: the Chinese religion and Shinto sections
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

## Corpora

| Corpus id | Tradition id(s) | Contents |
|---|---|---|
| `chinese` | `confucianism`, `daoism`; Han Kitab units under `islam` with corpus `chinese`; the steles under their own traditions | the classics, the Daoist core, Neo-Confucian works, Chinese Abrahamic texts |
| `shinto` | `shinto` | the myth and ritual corpus |

Add any missing tradition ids to `data/traditions.yaml`. Raw data goes in
`data/raw/<corpus>/` and tags in `data/motif-tags/<corpus>/`. Write one scope
file per corpus, `data/<corpus>/SCOPE.md`.

## Scope

### Chinese religion

| Group | Texts |
|---|---|
| Five Classics | *Shijing*, *Shangshu*, *Liji*, *Yijing* (with the *Xici*), *Chunqiu* with the *Zuozhuan* (selected: the religious and omen narratives) |
| Four Books | *Lunyu*, *Mengzi*, *Daxue*, *Zhongyong* |
| Daoist philosophy | *Daodejing*, *Zhuangzi*, *Liezi*, *Huainanzi* (the cosmogony and the flood chapters, or all of it if time allows) |
| Daoist canon, core | The *Daozang*'s central scriptures, by a stated rule: the *Taiping jing*, the *Huangting jing*, the *Duren jing*, the *Laozi xiang'er* commentary, the *Baopuzi* inner chapters, the *Taishang ganying pian* |
| Neo-Confucianism | Zhou Dunyi, *Taijitu shuo*; Zhu Xi, the *Jinsi lu*, the commentaries on the Four Books (selected) and *Zhuzi yulei* (selected) |
| Han Kitab (Chinese Islamic texts) | Wang Daiyu, *Zhengjiao zhenquan* and *Qingzhen daxue*; Liu Zhi, *Tianfang xingli*, *Tianfang dianli*, *Zhenjing zhaowei* (Jāmī's *Lawāʾiḥ* in Chinese); Ma Zhu, *Qingzhen zhinan*. Read wherever an open text exists; Murata, Chittick and Tu's translations are under copyright and are not data. |
| Other Abrahamic steles | The Nestorian Stele (781); the Kaifeng Jewish steles (1489, 1512, 1663) |
| Chinese Manichaean texts | Only if the Manichaean round did not read them |

**The Han Kitab are the round's centre.**
- They are Islam written in Neo-Confucian and Daoist idiom: 真一 "the Real
  One", *li* and *qi*, the Ultimateless (*wuji*) and the Supreme Ultimate
  (*taiji*).
- The gold-set pair is the **Han Kitab ↔ Zhu Xi response lead**.
- Compare their Quranic proof-texts and their Arabic and Persian sources,
  which belong to the Islamic analysis: there is no separate Sufi round.
- Record every Chinese rendering of a Quranic or Islamic term.

### Shinto

- *Kojiki* (712), Old Japanese and kanbun.
- *Nihon Shoki* (720), kanbun, books 1–2 (the age of the gods) in full;
  the rest selected for its religious narratives.
- The *norito* in the *Engishiki*, book 8, including the Great Purification
  (*Ōharae no kotoba*).
- *Kogoshūi*.
- The *Fudoki*, selected: the myths.
- The *Man'yōshū*, selected: the poems about the kami and the dead.

## Sources (probe each; reachable from a sibling session)

- **ctext.org**, with an API; check its terms and rate limits.
  - It has the classics, the Daoist and Confucian corpora, and parallel
    passages.
  - Bulk use may need an API key. If it does, say so and use Kanripo
    instead.
- **Kanripo**, through its texts on GitHub (`kanripo/KR…` repositories).
  - Reach them at `raw.githubusercontent.com`; the kanripo.org website
    refused requests.
  - It has the full *Daozang* and many classics, under CC BY-SA. Prefer it
    for bulk text.
- **CBETA**: Buddhist texts in Chinese, only where needed (the Buddhist
  round reads the canon).
- **Japanese Wikisource**: the *Kojiki*, *Nihon Shoki* and the *norito*.
  - Check the texts against a scholarly edition where possible.
  - Chamberlain's *Kojiki* (1882) and Aston's *Nihongi* (1896) are public
    domain. Use them as reading aids.
- **The Japanese Historical Text Initiative** (jhti.berkeley.edu) and the
  **National Institute of Japanese Literature**: check the terms.
- **Han Kitab**: look for open scans and e-texts of the Chinese originals
  (the Internet Archive, Chinese digital libraries, ctext's wiki). If none
  is machine-readable, say so plainly.

## Concept layer

Tag concepts alongside motifs:

- Heaven (*tian*) and Heaven's mandate (*tianming*)
- the Way (*dao*) and virtue (*de*)
- principle and vital energy (*li*, *qi*)
- the Supreme Ultimate and the Ultimateless (*taiji*, *wuji*)
- the One (*yi*), and the Real One (真一) in the Han Kitab
- the sage
- filial piety, ritual (*li*) and humaneness (*ren*)
- non-action (*wuwei*)
- immortality and inner alchemy
- the kami
- purity and pollution (*kegare*, *harae*, *misogi*)
- sacred kingship
- the land of the dead (Yomi)

## Quran-facing questions the readers should keep in mind

Hints go in first, with exact `Q surah:verse` references.

- **The Han Kitab's Quranic and Sufi sources.**
  - Tag each passage that renders a Quranic verse or a Sufi doctrine:
    *tawḥīd*, the Names, the "hidden treasure" hadith, the Perfect Human.
  - Hint the verse: Q 112, 7:180, 57:3, 50:16.
  - These are the round's strongest **response** leads.
- **Creation.**
  - Pangu and the primordial chaos in the *Huainanzi* and the *Kojiki*:
    heaven and earth separate, and the creating pair stirs the brine.
  - Compare Q 21:30 and 41:9–12.
- **The flood.**
  - Gun and Yu taming the flood (*Shangshu*, *Mengzi*, *Huainanzi*).
  - Compare Noah: Q 11:25–49, 71. Record what differs: Yu channels the
    waters, nobody escapes them in an ark, and no sin causes the flood.
- **The underworld and pollution.**
  - Izanagi in Yomi and the purification after it.
  - Compare ablution (Q 5:6) and the barrier between the living and the
    dead (Q 23:100).
- **The serpent slain and the sun hidden.**
  - Susanoo and the eight-headed serpent: compare the Ugaritic and Hittite
    serpents in the ANE units.
  - Amaterasu in the cave, the world dark.
  - The Quran has no serpent combat. Record this as an absence, not a
    match.
- **Heaven's mandate.**
  - Compare kingship given and taken by God (Q 3:26), and the righteous
    inheriting the earth (Q 21:105).
- **The Nestorian and Kaifeng steles.**
  - Christianity and Judaism presented in Daoist, Buddhist and Confucian
    idiom.
  - Their Chinese renderings of God, Messiah, scripture and Sabbath set
    against the Han Kitab's renderings.
  - These are response leads.

## Lexical

Build a table of the Chinese renderings of Islamic terms in the Han Kitab:
- 真主 / 真一 for Allah and the One;
- 天方 for Arabia, the Kaʿba;
- 至聖 for the Prophet;
- 經 for the Quran;
- 拜 / 禮拜 for *ṣalāt*;
- and others found in the reading.

Do the same for the Nestorian Stele (阿羅訶 *Aluohe*, 彌施訶 *Mishihe*) and
the Kaifeng steles. These are the round's lexical benchmarks: the table must
cover every rendering of a Quranic or Islamic term found in the reading.

## After the read

1. Merge near-duplicate motifs and concepts.
2. Run the **Chinese × Quran** and **Shinto × Quran** comparisons, mainly on
   the concept layer.
   - Use neutral ids for divergences.
   - Quote the decisive Classical Chinese or Japanese and the Arabic.
   - For the Han Kitab, record how each rendering keeps, bends or drops the
     Quranic sense.
3. Run the pipeline, with every benchmark passing. The **Han Kitab ↔ Zhu Xi**
   gold-set lead must be recovered.
4. Add a dated `docs/CLEANUP.md` entry. Record as deferred the comparisons
   with Buddhism, Hinduism, the ANE and Christianity.
5. Report:
   - the inventory: what was read from the original, what from a
     translation, and what was left out;
   - the benchmarks;
   - the comparison counts by relation;
   - the most interesting Chinese ↔ Quran and Shinto ↔ Quran leads and
     divergences, with references on both sides.

## Rules

- **Originals first.** Every claim states its basis.
- **Licenses.** Check each source's license, and keep raw text out of git.
- **Contact and convergence.** Premodern Shinto had essentially no contact
  with the Abrahamic religions, so its leads are convergence, not
  transmission.
  - Label them so.
  - Use direction-neutral wording throughout.
- **Respect.** These are living traditions. Keep notes descriptive and
  respectful.
- Don't create pull requests unless asked.
- Don't edit other sessions' tag or alignment folders.
