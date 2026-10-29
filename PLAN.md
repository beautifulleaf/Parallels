# Parallels — Project Plan

A lead-generation engine for finding parallels, convergences, and responses
across religious and mythological traditions. It surfaces candidates; humans
investigate them. Recall matters more than precision, but every lead must carry
its evidence so it can be checked quickly.

Motivating example: *al-yamm* ("the sea") occurs 8 times in the Quran (7:136,
20:39 ×2, 20:78, 20:97, 28:7, 28:40, 51:40), spread across 4 surahs but used
only in the Moses/Pharaoh narrative, while *bahr* is the general word for sea.
It has cognates in Hebrew *yam*, Ugaritic *Yam*, Mandaic *yama*, and a
(Semitic-derived) Egyptian loan *ym*. The system should find leads like this
automatically.

## Scope

**No tradition is out of scope.** Ingestion order is driven by data
availability and by the contact graph, not by any judgment of relevance.
Traditions are grouped as Western / Central / Eastern; per-tradition
outlines are in [TRADITIONS.md](TRADITIONS.md).

Known priority corpora (non-exhaustive):

| Tradition | Key texts | Notes |
|---|---|---|
| Islamic | Quran, hadith, tafsir | Quranic Arabic Corpus morphology; Quran/Hadith/Shamela MCP tools |
| Hebrew Bible / Jewish | Tanakh, Targums, midrash, Talmud | ETCBC/BHSA, OSHB, Sefaria, CAL |
| Christian | Septuagint, NT, Peshitta, apocrypha | MorphGNT, CATSS, ETCBC Peshitta |
| Mandaean | Ginza Rba, Book of John, Qolasta | Classical Mandaic is Aramaic → lexical track; Lidzbarski's German translations are public domain; candidate for the Quran's Sabians (2:62, 5:69, 22:17). Living community: respect esoteric material |
| Manichaean | Kephalaia, Psalm-Book, Cologne Mani Codex, Turfan fragments, Chinese Hymnscroll | Coptic, Greek, Middle Persian, Parthian, Sogdian, Uyghur, Chinese. Deliberately adapted itself to Christian, Zoroastrian, Buddhist, and Daoist vocabulary, which makes it a key "response" tradition. Digitales Turfan-Archiv; many translations under copyright (personal use) |
| Sumerian | Literary corpus, Eridu Genesis, Gilgamesh precursors | ETCSL, ePSD2, ORACC, CDLI; source of loan chains (e.g., *guza* → *kussû* → *kursī*) |
| Akkadian / Ugaritic / Egyptian | Atrahasis, Gilgamesh, Baal Cycle, Egyptian corpus | ORACC/eBL, Ugaritic lexica, TLA |
| Hittite | Kumarbi cycle, Illuyanka, treaties | TLHdig / Hethitologie-Portal Mainz, eDiAna; Sumerograms/Akkadograms bridge the scripts |
| Zoroastrian | Avesta, Pahlavi books | TITUS |
| Chinese | Confucian, Daoist, Buddhist canons; **Han Kitab** (Wang Daiyu, Liu Zhi, Ma Zhu) | ctext.org API, Kanripo, CBETA; Han Kitab digitization is patchy |
| Indic | Vedas, Brahmanas, epics, Puranas, Pali canon | Digital Corpus of Sanskrit, GRETIL, SuttaCentral (has parallel mappings) |
| Greek / Roman | Hesiod, Homer, Ovid, mystery cults | Perseus / Scaife |
| Others | Norse, Mesoamerican, African, Indigenous | Only openly published material; follow the CARE principles |

Translations are acceptable when they are all that is available. Each text
unit records whether it is original or translated, and lexical claims require
the original.

## Relation types

Every link the system proposes is classified as one of the following.

| Type | Meaning | Primary evidence |
|---|---|---|
| **Inheritance** | Shared ancestry | Regular sound correspondences, shared roots |
| **Transmission** | Moved through contact | Dates, geography, route in the contact graph, loan chains |
| **Convergence** | Similar theme, no plausible contact | Motif similarity + absence of a contact path |
| **Response** | One tradition consciously engaging another | Borrowed technical vocabulary, explicit reference, polemic, apologetic reframing (Han Kitab ↔ Neo-Confucianism; Dara Shikoh's *Majmaʿ al-Baḥrayn*; Manichaean "Buddha of Light") |

The classification is a hypothesis attached to the lead, not a verdict.

Traditions and movements that postdate Islam considerably, such as later
Christian movements and modern philosophy, are compared mainly through a
**concept layer**: metaphysics, theology, and philosophy, rather than words
or stories. Their leads are mostly response or convergence, plus **reverse
transmission** from the Islamic world (e.g., Avicenna and Averroes in
scholasticism).

## Architecture

```
 corpora ──► 1. ingest ──► common text-unit model (SQLite)
                               │
              ┌────────────────┼──────────────────┐
              ▼                ▼                  ▼
     2. lexical track   3. motif track      4. contact graph
     (roots, cognates,  (motif tags,        (who met whom,
      loan chains,       cross-lingual       when, where)
      distribution       embeddings,
      anomalies)         theme matching)
              └────────────────┼──────────────────┘
                               ▼
                    5. lead scoring + typing
                               ▼
                    6. searchable artifact
```

1. **Ingest.** Per-corpus adapters normalize everything into text units (id,
   tradition, corpus, reference, language, original/translation, date range,
   place, text, optional morphology).
2. **Lexical track** (where morphology exists):
   - *Distribution anomalies* within a corpus: lemma concentration per
     narrative or topic (log-odds with an informative Dirichlet prior),
     dispersion counted in documents/chapters rather than tokens, and
     synonym-choice skew (*bahr* vs *yamm*). Permutation nulls guard against
     false positives.
   - *Cognates*: consonantal-skeleton matching with Semitic sound
     correspondence tables.
   - *Loan chains*: a word graph (Sumerian → Akkadian → Aramaic → Hebrew/Arabic,
     Hittite Sumerograms/Akkadograms, Middle Persian ↔ Aramaic, Sanskrit →
     Chinese Buddhist transcription, Arabic/Persian → Han Kitab transcription).
3. **Motif track** (all traditions):
   - Segment texts into narrative and thematic units.
   - Tag units with motifs, seeded from the Thompson Motif-Index and ATU and
     extended with theological concepts (divine unity, primordial waters,
     cosmic order, light vs darkness, seal of prophecy, the infant set adrift…).
     LLM-assisted tagging, stored with provenance.
   - Cross-lingual retrieval with multilingual embeddings over originals and
     translations.
4. **Contact graph.** Traditions and communities as nodes, with dated,
   located, sourced edges (trade, conquest, translation movements, missions,
   diaspora). This is what separates transmission from convergence.
5. **Lead scoring.**
   - Specificity beats similarity: rare motif *combinations* and rare lemmas
     outweigh common single motifs ("a flood" alone is weak).
   - Penalize generic matches. Score each relation type separately.
   - Every lead stores its evidence: passages, counts, cognate forms,
     contact-path edges, and scores.
6. **Artifact.** A searchable, organized web page.
   - Filter by tradition, relation type, motif, lemma/root, and score.
   - Each lead is a card with side-by-side passages (original + translation),
     its evidence, and links to sources.
   - Browse views: by motif, by tradition pair, and a contact-graph view.
   - Review status per lead (new / investigating / promising / rejected) plus
     notes. These are read from the repo; the artifact is a read-only view.

## Review notes live in the repo

Every lead is a file under `leads/`. Each file has YAML front matter (id,
traditions, relation type, status, scores, evidence references) followed by
free-form Markdown notes. Git history is the review log. The pipeline may add
new leads and refresh evidence, but it never overwrites human-edited status or
notes. The artifact is regenerated from the repo.

## Guarding against parallelomania

- **Benchmark-first.** A gold set of established parallels must be recovered
  before the system's output counts as meaningful.
- **Hard negatives.** Generic motifs that appear everywhere are tracked so
  their matches can be down-weighted.
- **Raw counts beside every score.** Small-n findings are labeled as such.
- **Direction-neutral language.** Write "shared vocabulary/motif," never
  "borrowed from," unless the evidence is directional.

### Gold set (v0)

- Lexical: *yamm* / *yam*; *kursī* ← *kussû* ← *guza*; *tannūr* ← *tinūru*;
  *haykal* ← *ekallu* ← *é-gal*
- Flood narratives: Sumerian (Ziusudra), Atrahasis, Gilgamesh XI, Genesis 6–9,
  Quran (Noah), Shatapatha Brahmana (Manu and the fish), Deucalion, Gun-Yu
- Transmission: Panchatantra → *Kalila wa Dimna*; the Buddha legend →
  *Barlaam and Josaphat*
- Form: Hittite vassal treaties ↔ Deuteronomy
- Myth: Kumarbi cycle ↔ Hesiod's *Theogony*
- Response: Han Kitab (Wang Daiyu, Liu Zhi) ↔ Zhu Xi; Chinese Manichaean
  texts ↔ Buddhist idiom
- Contested leads (must be surfaced *and* labeled contested): Mani as "seal
  of the prophets" ↔ Quran 33:40; the Sabians ↔ Mandaeans

## Phases

- **v0 — foundation.** Data model, ingest framework, gold set, and an artifact
  skeleton that can display hand-entered leads.
- **v1 — first pipeline.**
  - Corpora: Quran + Hebrew Bible, with both tracks.
  - Reference lexica only: Akkadian, Ugaritic, Egyptian, Sumerian.
  - One cross-family response pair: Han Kitab ↔ Zhu Xi.
  - Exit criterion: the v1 slice of the gold set is recovered.
- **v2 — Aramaic world and the ancient Near East.**
  - Syriac Peshitta, Targums, Septuagint.
  - **Mandaean** (Aramaic lexical track plus motifs).
  - Sumerian, Akkadian, and Hittite story corpora; the loan-chain graph.
  - The full flood-narrative set.
- **v3 — Silk Road and beyond.**
  - **Manichaean** corpora across languages; Zoroastrian, Buddhist, Daoist.
  - Wider Han Kitab coverage; Indic and Greek corpora.
  - Corpus order guided by the contact graph.
- **v4+ — everything else** with usable data.

## Stack (initial)

- Python, SQLite with FTS5 for search, JSON exports for the artifact.
- Text-Fabric for ETCBC data; the Quran MCP tools / Quranic Arabic Corpus for
  Quranic morphology.
- Multilingual embedding model for cross-lingual motif retrieval.
- A static HTML artifact reading exported JSON, published privately and
  shareable later.

## Open questions

- Which languages the reviewer reads (affects the review UI: originals-first
  or translation-first).
- Licensing: copyrighted translations (e.g., many Manichaean and Mandaean
  English translations) can be used for personal exploration but should not be
  redistributed in a public artifact.
