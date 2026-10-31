# Prompt: full read of the Zoroastrian corpus

Paste everything below the line into a new Claude Code session attached to the
`beautifulleaf/parallels` repository.

---

You are continuing **Parallels**, a lead-generation project in the
`beautifulleaf/parallels` repository. It finds parallels, convergences and
responses between religious traditions. **It is a Quran-centred project.**
Your job is a **full read of the Zoroastrian corpus from the original Avestan
and Middle Persian (Pahlavi)**, done to the standard of the Hebrew Bible,
Quran and ancient Near East reads. A **side-by-side comparison of the
Zoroastrian texts with the Quran** follows the read.

## Start here

1. Base your work on `main`. Develop on your session's designated branch,
   created from `main`, and push there. Do not push to `main`.
2. Read these, in order:
   - `README.md`
   - `PLAN.md`, especially "Standing requirements for every text" and
     "Grounding in the originals"
   - `TRADITIONS.md`, the Zoroastrianism section
   - `leads/README.md`
   - `docs/prompts/reading-at-scale.md`: **the method, the tools to reuse
     and the lessons. Follow it.**
   - `docs/CLEANUP.md`
   - `data/motif-tags/ane/README.md`, the reading protocol to adapt
   - `data/ane/SCOPE.md`, the model for the scope file
   - `data/alignments/README.md`
3. Run `python3 tools/fetch.py` and `python3 tools/anefetch.py`. You will
   reuse the Quran text and the ANE ids.

## Goal

Every text in scope gets the standing treatment, as set out in
`reading-at-scale.md`:
- the original in the repo (raw data in `data/raw/zoroastrian/`, fetchers in
  `tools/`);
- a full read tagged in `data/motif-tags/zoroastrian/`;
- the linguistic layer, with Avestan and Pahlavi adapters;
- lexical links to the Quran;
- the Zoroastrian × Quran comparison pass.

Do not run a Zoroastrian × Hebrew Bible or × ANE pass; record them in
`docs/CLEANUP.md` as deferred.

## Scope: the core books

| Group | Texts |
|---|---|
| Avesta, in full | Yasna (with the Gathas, Y 28–34, 43–51, 53, and the Yasna Haptanghaiti, Y 35–41); Visperad; the Yashts; Vendidad (Videvdad); Khorda Avesta (Nyayeshes, Gahs, Sirozas, Afrinagans); Hadokht Nask and the Aogemadaeca if available |
| Pahlavi, core | Bundahishn (Greater, Iranian), the cosmogony and eschatology; *Arda Wiraz Namag* (the tour of heaven and hell); *Zand-i Wahman Yasn* (the apocalypse); *Menog-i Khrad*; *Dadestan-i Denig*; the Denkard books 5, 7 (the legend of Zarathustra) and 9 (the Nask summaries), and a stated selection from book 3; *Ayadgar-i Jamaspig*; *Shkand-gumanig Wizar*, the 9th-century Zoroastrian polemic against Islam, Judaism, Christianity and Manichaeism and a key "response" text; *Pahlavi Rivayat* if available |

Measure every text, and write `data/zoroastrian/SCOPE.md` before planning
chunks.

**Dating caveat.** Most Pahlavi books were written down after the Islamic
conquest. The comparison readers must not assume a direction of influence,
and leads keep `standing: proposed` with direction-neutral wording.

## Sources (probe each; these were reachable from a sibling session)

- **TITUS** (titus.uni-frankfurt.de): Avestan texts, the Geldner edition in
  transliteration, and several Pahlavi texts. Check the terms of use.
- **avesta.org**: Avestan transliterations and the public-domain *Sacred
  Books of the East* translations (Darmesteter, Mills, West). Use them as
  reading aids for the Avesta and, where no Pahlavi original can be had, for
  the Pahlavi books.
- **Avestan Digital Archive** (ada.geschkult.fu-berlin.de): manuscript
  images, for checking readings only.
- **CAIS** (cais-soas.com): transliterations and translations of some
  Pahlavi texts. Check the terms.
- **Middle Persian Corpus and Dictionary** (mpcorpus.org): lemmatized
  Pahlavi. It refused a scripted request from a sibling session. Try it
  politely; if it stays closed, say so.
- **Not usable:** sacred-texts.com is blocked by the proxy. Do not route
  around it.

**Translations.** The user allows a text with no open machine-readable
original to be read from a public-domain translation, labelled as
`reading-at-scale.md` describes (`original: false`, `basis: translation`, the
translator named). Prefer the original wherever it exists, even without
lemmas.

## Known leads (benchmarks, not reading targets)

- the Majūs (Q 22:17)
- Chinvat ↔ the *ṣirāṭ* (contested)
- *Arda Wiraz* ↔ the Night Journey (contested)
- Haurvatāt/Amərətāt ↔ Hārūt/Mārūt (Q 2:102)
- *pairidaēza* ↔ *firdaws*

These are already known. They are **benchmarks**: after the read, check that
the pipeline surfaces them. Do not give them to the readers, and do not read
for them. Follow "Discovery, not confirmation" in
`docs/prompts/reading-at-scale.md`: the aim is the specific detail nobody has
listed yet.

## Lexical benchmarks (`data/benchmarks/lexical.yaml`)

Extend `tools/anelex.py` with an Iranian branch: Avestan or Old Persian, then
Middle Persian, then Aramaic or Arabic.

| Chain | Requirement |
|---|---|
| *pairidaēza* → *firdaws* (Q 18:107, 23:11) | Must recover. A Greco-Roman session may also claim it, through *paradeisos*; one chain should show both routes. |
| *Haurvatāt*/*Amərətāt* → *Hārūt*/*Mārūt* (Q 2:102) | Must recover. Label it `scholarship` and `proposed`. |
| Old Persian *maguš* → *majūs* (Q 22:17) | Must recover. |
| *dēn* ~ *dīn* | Contested: Arabic *dīn* has Semitic roots too. Record the result either way, with `expect: false` if it is not recovered. |
| *barzakh* | Contested. Record the result either way, with `expect: false` if it is not recovered. |

## Report back, in this order

1. An inventory of what was read: from the original, from a translation,
   and what was left out, each with its edition and number of lines.
2. The benchmark results.
3. The comparison counts by relation.
4. The most interesting Zoroastrian ↔ Quran leads and deliberate
   divergences, with references on both sides.

## Rules

- **Originals first.** Every claim states its basis.
- Check each source's license, and keep raw text out of git.
- This is a living community. Use only published texts, and keep the notes
  descriptive and respectful.
- Don't create pull requests unless asked.
- Don't edit other sessions' tag or alignment folders: `hb/`, `quran/`,
  `ane/`, and the existing `data/alignments/` pairs.
