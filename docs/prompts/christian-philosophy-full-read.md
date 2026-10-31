# Prompt: full read of Christianity and Western philosophy

This round is split into **four sessions, run in order of closeness to the
Quran**. Paste everything below the line into a new Claude Code session
attached to the `beautifulleaf/parallels` repository, and **set the phase** in
the first line.

**Coverage.** The earlier the sources, the wider the read:

- Phases 1 and 2 (early and Eastern Christianity) read **everything openly
  available** in scope.
- Phase 3 (the Western Middle Ages to the Enlightenment) reads a **broad
  stated canon**.
- Phase 4 (newer movements and modern philosophy) reads **key works only**.

---

**Phase: <1 | 2 | 3 | 4>** (see "Phases" below; do only your phase)

You are continuing **Parallels**, a lead-generation project in the
`beautifulleaf/parallels` repository. It finds parallels, convergences and
responses between religious traditions, and **it is Quran-centred**.

- **Your task:** a full read of your phase's Christian and philosophical
  texts, done to the standard of the Hebrew Bible, Quran and ancient Near
  East reads.
- **Language:** read in the original wherever an open edition exists, and
  otherwise from a public-domain translation, labelled as such.
- **Afterwards:** compare the texts read with the Quran, side by side.
- **Phases 3 and 4** also build and use a **concept layer** for philosophy
  and theology.

## Start here

1. Base your work on `main`. Develop on your session's designated branch,
   created from `main`, and push there. Do not push to `main`.
2. Read these, in order:
   - `README.md`
   - `PLAN.md`, especially "Standing requirements for every text",
     "Grounding in the originals" and the concept layer under "Relation
     types"
   - `TRADITIONS.md`: the Christianity sections and Western Philosophy
   - `leads/README.md`
   - `docs/prompts/reading-at-scale.md`: the method, the tools to reuse,
     the lessons and the translation protocol. Follow it.
   - `docs/CLEANUP.md`, including the entries of earlier phases
   - `data/motif-tags/ane/README.md`: the reading protocol to adapt
   - `data/ane/SCOPE.md`: the model for the scope file
   - `data/alignments/README.md`
3. Run `python3 tools/fetch.py` and `python3 tools/anefetch.py`. From phase 2
   on, also read the earlier phases' SCOPE files and reuse their tools.

## Corpora, traditions, folders

| Phase | Corpus id | Tradition ids |
|---|---|---|
| 1 | `early-christian` | `christianity-early` (add `gnostic` if `data/traditions.yaml` separates it) |
| 2 | `eastern-christian` | `christianity-eastern` |
| 3 | `western-christian` | `christianity-western` |
| 4 | `modern` | `christianity-modern`, `western-philosophy` |

Check `data/traditions.yaml` and add any id that is missing, with its group
and family. Raw data goes in `data/raw/<corpus>/`, tags in
`data/motif-tags/<corpus>/`, and the scope file is `data/<corpus>/SCOPE.md`.

## Phases

### Phase 1: early Christianity and the Gnostics (to about the 5th century). Everything open.

- **New Testament** in Greek:
  - text: SBLGNT and MorphGNT, both on GitHub, with lemmas and morphology;
  - license: CC BY-SA. Fetch through `raw.githubusercontent.com`; the
    github.com website is blocked.
- **The Septuagint's additions** to the Hebrew canon: Tobit, Judith, Wisdom,
  1–4 Maccabees, the Greek additions to Daniel and Esther, Baruch, Prayer of
  Manasseh, Psalm 151.
  - Use an open LXX text with morphology if one exists (look on GitHub). The
    CATSS morphology has restrictive terms: check them.
  - Use the LXX itself only where it diverges meaningfully from the Hebrew
    already read.
- **Apostolic Fathers.**
- **Apocrypha and infancy gospels:**
  - the Protevangelium of James;
  - the Infancy Gospel of Thomas;
  - Pseudo-Matthew;
  - the Arabic and Syriac Infancy Gospels;
  - the Gospel of Nicodemus;
  - the Transitus Mariae;
  - the apocryphal Acts (Thomas, with the Hymn of the Pearl; John; Paul and
    Thecla);
  - the Apocalypse of Paul;
  - the *Life of Adam and Eve* (coordinate with the Covenantal round, which
    may read it).

  Read them in the original where open; otherwise use M. R. James 1924 or
  the ANF translations, labelled.
- **Nag Hammadi and related:**
  - the Gospel of Thomas;
  - the Apocryphon of John;
  - the Gospel of Truth;
  - the Gospel of Philip;
  - the Hypostasis of the Archons;
  - On the Origin of the World;
  - the Second Treatise of the Great Seth;
  - the Apocalypse of Peter (NHC VII,3);
  - the Gospel of Judas.

  Use Coptic Scriptorium (GitHub `CopticScriptorium/corpora`) for what it
  has, and open translations otherwise. Modern translations are under
  copyright: do not use them as data.
- **Jewish-Christian texts:**
  - the Pseudo-Clementine *Homilies* and *Recognitions*;
  - the fragments of the Ebionite and Nazarene gospels (in the
    heresiologists).
- **Heresiologists** (ANF and NPNF, public domain, as translation; Greek
  and Latin originals where open):
  - Irenaeus, *Against Heresies*;
  - Hippolytus, *Refutation*;
  - Epiphanius, *Panarion*: the sections on the Ebionites, Elchasaites,
    Nazarenes, Basilides, the Collyridians (Mary worship) and the Sabians if
    present.
- **Diatessaron:** the Arabic Diatessaron and Ephrem's commentary, where
  open.
- **The Fathers to Augustine,** all openly available, in Greek, Latin or the
  ANF/NPNF translations:
  - Justin Martyr;
  - Tertullian;
  - Origen;
  - Athanasius;
  - the Cappadocians;
  - Augustine's *Confessions*, *City of God* and *De Trinitate*.

  Chunk the large corpora by work.

### Phase 2: Eastern Christianity. Everything open.

- **Syriac** (highest priority for Quran leads):
  - The Peshitta: the ETCBC `peshitta` Text-Fabric data on GitHub.
  - Ephrem: the Hymns on Paradise, on Faith, on the Nativity, and the
    Madrashe generally.
  - Jacob of Serugh: the homilies, above all those on the Sleepers of
    Ephesus and on Alexander.
  - Narsai.
  - The *Cave of Treasures*: Syriac (Bezold 1888, public domain) and Budge
    1927.
  - The Syriac Alexander Legend (Neshana) and the Alexander poem attributed
    to Jacob of Serugh: Budge 1889, public domain.
  - The Syriac Sleepers of Ephesus.
  - The *Apocalypse of Pseudo-Methodius*.
  - The *Doctrina Addai*.
  - The Acts of Thomas in Syriac.
  - Bahira legend texts.

  Sources: the Digital Syriac Corpus (Beth Mardutho; check its license),
  Syriaca.org, ETCBC/peshitta, and public-domain editions on the Internet
  Archive.
- **Byzantine:**
  - John of Damascus, *On Heresies* 100 (the "Ishmaelites") and the
    *Disputatio*;
  - Theophanes on Muhammad;
  - Pseudo-Dionysius;
  - Maximus the Confessor (selected);
  - the *Philokalia* (selected; public-domain parts only);
  - Gregory Palamas (the *Triads*, selected).

  Use the Greek from the PG where open, or public-domain translations.
- **Coptic:** Shenoute and the Coptic martyr acts and apocrypha in Coptic
  Scriptorium.
- **Ethiopic:** the *Kebra Nagast* (Budge, public domain; Ge'ez where open);
  Ethiopic 1 Enoch only if the Covenantal round did not read it.
- **Armenian:** the Armenian Adam books and the Infancy Gospel, if open.
- **Arabic Christianity and the encounter with Islam:**
  - the dialogue of Timothy I with the caliph al-Mahdi (Mingana 1928);
  - Theodore Abu Qurrah;
  - the *Apology of al-Kindi*;
  - the Bahira legend;
  - early Arabic Gospel translations, where open.

  These are response material: tag what they answer in the Quran.

### Phase 3: Western Christianity and philosophy to the Enlightenment. A broad stated canon.

**First, build the concept layer.**

- **Vocabulary.** Write `data/concepts.yaml`: a vocabulary of philosophical
  and theological concepts. Examples:
  - being and existence;
  - essence and existence;
  - the One;
  - emanation;
  - the intellect;
  - causation and occasionalism;
  - divine attributes and divine simplicity;
  - divine unity and Trinity;
  - creation from nothing and the eternity of the world;
  - the soul and its immortality;
  - prophecy and revelation;
  - revelation against reason;
  - free will and predestination;
  - grace;
  - the beatific vision;
  - mystical union;
  - natural law;
  - the proofs of God.

  Each concept needs a definition concrete enough that two readers apply it
  alike.
- **Tags and matching.** Concept tags sit beside motif tags in the unit
  format, as `concepts: [{concept, refs, note}]`. Extend `tools/motifs.py`,
  or write `tools/concepts.py`, to load, validate and match them, and make
  concept leads with `layers: [concept]`.
- **The Quran side.** Concept-tag the Quran, all 6,236 verses, in chunks
  as the Quran read did. This is a separate workstream run before the
  phase-3 reading: comparison needs concepts on both sides. Use
  `data/motif-tags/quran-concepts/` and do not edit the Quran's motif files.

**Then read**, tagging motifs and concepts:

| Period | Texts |
|---|---|
| Early Middle Ages | Boethius, *Consolation*; Eriugena, *Periphyseon* (selected); Anselm, *Proslogion*, *Monologion*, *Cur Deus homo* |
| The Latin Quran and Latin Islam | Robert of Ketton's Latin Quran (1143) and Bibliander's printed Quran (1543), where scans have usable OCR; the *Liber scalae Machometi*; Peter the Venerable, *Contra sectam Saracenorum*; Riccoldo da Monte di Croce, *Contra legem Sarracenorum*; Nicholas of Cusa, *Cribratio Alkorani* and *De pace fidei* (Cusanus-Portal) |
| Scholasticism | Aquinas, *Summa contra gentiles* (all) and the *Summa theologiae* Prima pars (from the lemmatized Corpus Thomisticum); Bonaventure, *Itinerarium*; Duns Scotus, *De primo principio*; Ockham (selected) |
| Medieval mysticism | Eckhart (Latin and German sermons, selected); Ramon Llull, *Book of the Lover and the Beloved* and the *Book of the Gentile and the Three Wise Men* (Llull DB) |
| Renaissance and Reformation | Ficino (selected); Pico, *Oration*; Erasmus (selected); Luther, *Bondage of the Will*; Calvin, *Institutes* I; Servetus; the Racovian Catechism (Socinian) |
| Early modern | Descartes, *Meditations*; Malebranche (occasionalism); Spinoza, *Ethics* and the *Theological-Political Treatise*; Leibniz, *Monadology* and *Theodicy* (selected); Locke, *Essay* II and the *Reasonableness of Christianity*; Hume, *Dialogues* and *Enquiry* X ("Of Miracles") |
| Latin translations from Arabic | Avicenna Latinus, Averroes, al-Ghazali's *Maqāṣid*, where an open Latin text exists. These are reverse transmission: record them as such |

Sources:

- Corpus Thomisticum;
- The Latin Library;
- CCEL;
- Perseus Latin;
- the Cusanus-Portal;
- Llull DB;
- Project Gutenberg;
- Early Modern Texts. These are modernized editions; check their terms, and
  prefer the originals.

### Phase 4: newer movements and modern philosophy. Key works only, open texts only.

- **Newer movements:**
  - Swedenborg (*Heaven and Hell*, *True Christian Religion*; public
    domain);
  - the Book of Mormon and the Doctrine and Covenants (public domain;
    Joseph Smith Papers);
  - Mary Baker Eddy, *Science and Health* (1875 edition);
  - Quaker founding texts (Fox, Barclay);
  - Christadelphian and early Jehovah's Witness texts where public domain;
  - Unitarian founding texts (Channing).
- **Philosophy from the Enlightenment on**, concept layer:
  - Lessing, *Nathan the Wise* (the ring parable);
  - Kant, *Religion within the Bounds of Bare Reason*;
  - Hegel, *Lectures on the Philosophy of Religion* (selected);
  - Schleiermacher, *On Religion*;
  - Feuerbach;
  - Kierkegaard, *Fear and Trembling*;
  - Nietzsche (selected).

  All are public domain. Twentieth-century theology (Barth, Tillich,
  Teilhard) and most 20th-century philosophy are under copyright: list
  them as out of scope.

## Quran-facing questions the readers should keep in mind

Hints go in first, with exact `Q surah:verse` references.

- **Infancy:**
  - Mary in the Temple, Zechariah and the lots: Q 3:35–44;
  - the palm and the stream: Q 19:22–26;
  - the speech in the cradle: Q 19:29–33, 3:46, 5:110;
  - the clay birds: Q 3:49, 5:110.
- **Jesus:**
  - the crucifixion and its denial or appearance, with docetism and Simon of
    Cyrene: Q 4:157–158;
  - "son of God" and the Trinity: Q 4:171, 5:72–75, 5:116, 112;
  - the table from heaven: Q 5:112–115;
  - "Aḥmad" and the Paraclete: Q 61:6;
  - the disciples (*ḥawāriyyūn*): Q 3:52, 5:111, 61:14.
- **Mary:** Mary as "sister of Aaron", Q 19:28; Collyridian Mary worship,
  Q 5:116.
- **Satan's refusal to bow:** the *Life of Adam and Eve* and the *Cave of
  Treasures* against Q 2:34, 7:11–18, 15:28–42, 38:71–85.
- **The Sleepers of Ephesus,** Q 18:9–26, and the **Alexander Legend**,
  Q 18:83–98.
- **The People of the Book's scholars and monks,** Q 5:82–83, 9:31, 57:27
  ("monasticism they invented").
- **Theology:**
  - divine unity and the attributes: Q 112, 42:11, 2:255;
  - the Logos and "his word": Q 4:171;
  - prophecy and the seal: Q 33:40;
  - revelation against reason.

## Lexical benchmarks (`data/benchmarks/lexical.yaml`)

Extend `tools/anelex.py` with Syriac (the Peshitta lemmas), Greek and Ge'ez
branches.

| Benchmark | Requirement |
|---|---|
| Syriac *ṣlōtā* → *ṣalāt* | must recover |
| Ge'ez *ḥawārya* → *ḥawāriyyūn* | must recover |
| Syriac *qeryānā* → *qurʾān* | proposed; `expect: false` if missed |
| *euangelion* → *injīl* | coordinate with the Greco-Roman round |
| Syriac *mašīḥā* → *masīḥ* | must recover |
| Syriac *ṭaybūtā* / Greek *charis* | concept link only |
| Syriac *paraqlīṭā* ~ *aḥmad* | contested; record the result, labelled fringe or contested |

## Every phase ends with

1. Merging near-duplicate motifs (and, in phases 3–4, concepts).
2. The `<corpus> × Quran` side-by-side comparison.
   - Use neutral ids for divergences, and quote the decisive words of both
     sides.
   - Divergences matter as much as parallels. Examples:
     - who dies on the cross;
     - the Jesus who speaks in the cradle to defend his mother against the
       infancy gospels' wonder-child;
     - Satan's reason for refusing.
   - In phases 3–4, comparison runs mainly on the concept layer.
3. Running the pipeline, with every benchmark passing.
4. A dated `docs/CLEANUP.md` entry, listing what is deferred.
5. A report:
   - the inventory: read from the original, read from a translation, left
     out;
   - the benchmarks;
   - the comparison counts by relation;
   - the most interesting leads and divergences, with references on both
     sides.

Do not run comparisons against the Hebrew Bible, the ANE or the other
traditions; record them as deferred.

## Rules

- **Originals first.** Every claim states its basis, and every translation
  is labelled.
- **Copyright.** Check each source's license. Keep raw text out of git, and
  don't use copyrighted modern translations as data.
- **Fringe claims.** Claims of a Syriac Quran in the style of Luxenberg are
  fringe: label them so.
- **Direction.** Use direction-neutral wording unless the evidence is
  directional.
- **Replace secondary units.** The pilot units in `data/motif-tags/infancy.yaml`
  (Protevangelium, Pseudo-Matthew, the Arabic Infancy Gospel, the Infancy
  Gospel of Thomas, Matthew 2) are tagged from secondary knowledge. Replace
  them with units read from the original in phase 1, keeping the benchmark
  pairs in `data/benchmarks/motifs.yaml` passing.
- Don't create pull requests unless asked.
- Don't edit other sessions' tag or alignment folders.
