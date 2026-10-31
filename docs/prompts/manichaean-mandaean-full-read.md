# Prompt: full read of the Manichaean and Mandaean corpora

Paste everything below the line into a new Claude Code session attached to the
`beautifulleaf/parallels` repository.

---

You are continuing **Parallels**, a lead-generation project in the
`beautifulleaf/parallels` repository. It finds parallels, convergences and
responses between religious traditions. **It is a Quran-centred project.**
Your job is a **full read of the Manichaean and Mandaean corpora**, in the
original wherever an open machine-readable original exists, and otherwise
from a public-domain translation, clearly labelled. Use the standard of the
Hebrew Bible, Quran and ancient Near East reads. Afterwards, compare these
texts with the Quran side by side.

## Start here

1. Base your work on `main`. Develop on your session's designated branch,
   created from `main`, and push there. Do not push to `main`.
2. Read these, in order:
   - `README.md`
   - `PLAN.md`, especially "Standing requirements for every text" and
     "Grounding in the originals"
   - `TRADITIONS.md`: the Manichaeism and Mandaeism sections
   - `leads/README.md`
   - `docs/prompts/reading-at-scale.md`, the method, the tools to reuse and
     the lessons. **Follow it**, including the section on reading from a
     translation.
   - `docs/CLEANUP.md`
   - `data/motif-tags/ane/README.md`, the reading protocol to adapt
   - `data/ane/SCOPE.md`, the model for the scope file
   - `data/alignments/README.md`
3. Run `python3 tools/fetch.py` and `python3 tools/anefetch.py`.

## Goal

Two corpora, `manichaean` and `mandaean`, each with the standing treatment
described in `reading-at-scale.md`:
- **Raw data:** `data/raw/<corpus>/`.
- **Tags:** `data/motif-tags/<corpus>/`.
- **Scope files:** `data/<corpus>/SCOPE.md`.
- **Linguistic adapters:** Coptic, Middle Persian/Parthian, Chinese and
  Mandaic, wherever lemmas exist.
- **Lexical links to the Quran.**
- **Comparison passes:** `manichaean-quran` and `mandaean-quran`.

Do not run a comparison against the Hebrew Bible or the ANE. Record those as
deferred in `docs/CLEANUP.md`.

## Scope

### Manichaean

| Language | Texts | Where to look |
|---|---|---|
| Middle Persian, Parthian, Sogdian, Uyghur | Turfan fragments with religious content: the *Shābuhragān*, the hymn cycles (*Huwīdagmān*, *Angad Rōšnān*), the parables, cosmogony and eschatology fragments | **Digitales Turfan-Archiv** (turfan.bbaw.de, reachable). Probe for transliterations; if only images exist, say so. |
| Coptic | The *Psalm-Book* (Allberry 1938); the *Kephalaia*; the Homilies | **Coptic Scriptorium** (GitHub `CopticScriptorium/corpora`, reachable) and other open editions. Check what exists. The Kephalaia may be under copyright: list it, don't use it unless openly licensed. |
| Greek | The Cologne Mani Codex | Open text only. Likely not available: say so if not. |
| Chinese | The *Compendium of the Teachings of Mani* (摩尼光佛教法儀略, Taishō T2141A); the Hymnscroll (下部讚) | CBETA, if reachable; check its terms. |
| Arabic (hostile and doxographic) | Ibn al-Nadīm, *al-Fihrist*, the chapter on Mani; al-Bīrūnī's report of the *Shābuhragān*; al-Shahrastānī on the Manichaeans | The **Shamela MCP tools** in this environment (`shamela_*`). Cite their pages as the tools require. |

The Arabic is the Islamic world's own window onto Manichaeism. It is
**response** material: read and tag it like the rest.

### Mandaean

| Text | Notes |
|---|---|
| Ginza Rabba, Right and Left | |
| The Book of John (*Drashe d-Yahya*) | |
| The Qolasta / Canonical Prayerbook | |
| *Haran Gawaita* | |
| *Diwan Abatur* | Include if available. |

- **Original.** Look for an open machine-readable Mandaic text of each.
  - The CAL has a lemmatized Mandaic corpus. It asks not to be scraped, so
    do not scrape it. Its data dumps are available on request: tell the
    user, who can ask for them.
  - Petermann's 1867 Ginza edition is public domain, but scanned only.
- **Translation.** Where no original can be had, read Lidzbarski's German
  translations: *Ginzā* (1925), *Das Johannesbuch der Mandäer* (1915) and
  *Mandäische Liturgien* (1920). They are public domain (Lidzbarski
  d. 1928).
  - Use a scanned text from the Internet Archive with good OCR. Correct the
    OCR where needed, recording how.
  - Label the units `original: false`, `basis: translation`, "reading
    Lidzbarski's German translation".
  - Drower's and Gelbert's translations are under copyright. Do not use
    them as data.

Measure everything and write both SCOPE files before planning chunks.

## Quran-facing questions for the readers

Readers put these in hints first, with exact `Q surah:verse` references.

- **Seal of the prophets.** Mani as the "seal of the prophets" against
  Q 33:40. This is a contested gold-set lead: surface it, and label it
  contested.
- **The Sabians** (Q 2:62, 5:69, 22:17) and the Mandaeans. This is a
  contested identification.
- **Baptism.** Mandaic *ṣbā* "baptize" against the *ṣibgha* of God
  (Q 2:138).
- **John the Baptist (Yahya)** in Q 19:2–15 and 3:38–41, against the Book of
  John.
- **Jesus.** The Manichaean Jesus of splendour, and Jesus in both corpora,
  against Q 4:157–158 (the crucifixion), 3:55 and 5:116–117.
- **Light imagery** against the Light verse (Q 24:35).
- **Dualism** against Q 6:1 ("made the darkness and the light") and
  Q 16:51 ("do not take two gods").
- **The soul's ascent through watch-houses** against the ascension
  (Q 70:3–4, 32:5).
- **The elect and the hearers.**
- **The zindīq.** Note that the Quran does not name it; the term is later.

## Lexical benchmarks (`data/benchmarks/lexical.yaml`)

Extend `tools/anelex.py` with Mandaic, using Drower–Macuch through the
public pages only. Lemmas come only from a lexicon or edition that is
licensed for use.

- **Mandaic *yama* ↔ *yamm*.** Must recover. It is the project's founding
  example.
- **Mandaic *ṣbā* ↔ *ṣibgha* and *ṣābiʾūn*.** Contested: mark it
  `expect: false` if it is not recovered.
- **Middle Persian *dēn*.** Coordinate with the Zoroastrian session's
  result.

## Report back, in this order

1. An inventory: what was read from the original, what from a translation,
   and what was left out, each with its edition and number of lines.
2. The benchmark results.
3. The comparison counts by relation, for each corpus.
4. The most interesting Manichaean ↔ Quran and Mandaean ↔ Quran leads and
   deliberate divergences, with references on both sides.

## Rules

- **Originals first.** Every claim states its basis; translations are
  labelled as such.
- **Licenses.** Check each source's license, and keep raw text out of git.
- **Respect.** The Mandaeans are a living, persecuted community, and some
  of their material is esoteric. Use only published texts, and keep the
  notes descriptive and respectful.
- Don't create pull requests unless asked.
- Don't edit other sessions' tag or alignment folders.
