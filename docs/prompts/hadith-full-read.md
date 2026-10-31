# Prompt: full read of the hadith corpus (the Islamic side, with the Quran)

Paste everything below the line into a new Claude Code session attached to the
`beautifulleaf/parallels` repository. The corpus is about as large as the
Quran and the Hebrew Bible together, so plan for the work to continue into a
second session; the scope file and chunk plan make that seamless.

**When to run it.** Together with the Quran observation layer, this is the
project's *Islamic foundation*. It runs **before every other tradition's
round**, so that each later round compares against the Quran and the hadith
from the start and needs no hadith top-up afterwards. The order is:

1. The ANE read and the ANE × Quran comparison pilot, which settles the
   observation-record schema (`data/records/README.md`).
2. The Quran observation layer: records for all 6,236 verses.
3. **This hadith read.**
4. Then the other rounds: Greco-Roman, Zoroastrian, Manichaean and Mandaean,
   Covenantal, Christianity and philosophy, Sikh, Jain, Hindu, Buddhist,
   East Asian.

The HB × Quran comparison gets its hadith top-up in this session (see
"After the read").

---

You are continuing **Parallels**, a lead-generation project in the
`beautifulleaf/parallels` repository. It finds parallels, convergences and
responses between religious traditions. **It is a Quran-centred project.**

The Quran has been read in full. This session adds the **hadith corpus
alongside the Quran**, so that the Islamic side of every comparison is the
Quran *and* the hadith. Prophetic reports often carry exactly the details the
Quran leaves out: names, numbers, sequences, and stories of earlier prophets
and peoples. Those are where the unique parallels and divergences are.

Your job:
1. Ingest the corpus.
2. Read it in full in the original Arabic.
3. Link it to the Quran.
4. Rerun the comparisons that already exist with the hadith added to the
   Islamic side.

## Start here

1. Base your work on `main`. Develop on your session's designated branch,
   created from `main`, and push there. Do not push to `main`.
2. Read these, in order:
   - `README.md`
   - `PLAN.md`, especially the Islamic row of the corpus table (which names
     this hadith corpus), "Standing requirements for every text" and
     "Grounding in the originals"
   - `TRADITIONS.md`, the Islam section
   - `leads/README.md`
   - `docs/prompts/reading-at-scale.md`, **especially "Discovery, not
     confirmation"**: the method, tools, lessons and translation protocol
   - `docs/CLEANUP.md`
   - `data/records/README.md`: the slot-structured **observation records**
     piloted in the ANE × Quran comparison. If it is not there yet, see
     "Observation records" below.
   - `data/motif-tags/quran/` (a few files): how the Quran was read
   - `data/alignments/README.md`
3. Run `python3 tools/fetch.py` and `python3 tools/anefetch.py`.

## The corpus

***al-Jāmiʿ al-Kāmil fī l-ḥadīth al-ṣaḥīḥ al-shāmil al-murattab ʿalā abwāb
al-fiqh***, by Muḥammad Ḍiyāʾ al-Raḥmān al-Aʿẓamī (d. 1441/2020), is
**Shamela book 47**. It is downloaded and readable through the Shamela MCP
tools in this environment (`shamela_get_toc`, `shamela_get_pages_range`,
`shamela_get_book_section`, `shamela_get_citation`).

- It gathers the ṣaḥīḥ hadith of the major collections, arranged in **67
  books (*kutub*)**, about **8,700 pages**.
- Edition, editor and publisher are not recorded in Shamela. **Do not invent
  them.**
- Cite by the book's own hadith numbering and the Shamela page. Note that
  page numbers are **Shamela's automatic numbering** unless matched to the
  print.
- Follow the Shamela tools' instructions:
  - Distinguish the main text (*matn*, the body) from the footnotes (*ḥāshiya*).
    The footnotes are the compiler's or an editor's, not the hadith.
  - Never complete a text from memory.

**Ingest.** Write `tools/hadithfetch.py`. It walks the table of contents
and the pages through the Shamela tools, and writes one normalized JSON per
book to `data/raw/hadith/`. Normalize it to the shared text model described
in `reading-at-scale.md` and used by `originals.AneCorpus`:

- Siglum `Jāmiʿ`; sections are the 67 books; a "line" is one hadith.
- Fields for each hadith:
  - `n`: its number in the book;
  - `text`: the full Arabic as printed;
  - `isnad` and `matn`: separated where the text allows;
  - `takhrij`: the sources cited in the footnotes, such as *al-Bukhārī 123,
    Muslim 456*, kept as structured references;
  - `page`: the Shamela page.
- If an MCP call fails partway, the fetcher resumes; it never fills gaps from
  memory.
- Shamela text is the user's local library: keep the raw text out of git.
- **Cross-check against the Hadith MCP tools** (`fetch_hadith`, with canonical
  collections and their URLs). For every hadith whose `takhrij` names
  al-Bukhārī or Muslim, record the canonical id and URL that the tool returns.
  That gives each lead a verifiable link. Never construct hadith URLs
  yourself; use only the `url` field the tool returns.

## The read

Read every hadith's **matn** in the Arabic. The isnad is not tagged for
motifs; record only its first transmitter (the Companion) as metadata.

**Order of chunks.** The plan follows the book's order. Run first the books
that carry narrative and cosmology, so that comparisons can start early:

| Book | Contents |
|---|---|
| 1 | *al-waḥy* |
| 45 | *bad' al-khalq* |
| 46 | *akhbār al-māḍīn* |
| 47 | *akhbār al-anbiyāʾ* |
| 48 | the *sīra* |
| 58 | dreams |
| 60 | tafsir |
| 65 | the trials and signs of the Hour |
| 66 | the Resurrection |
| 67 | paradise and hell |

Then read all the rest. The legal books (purity, prayer, fasting, pilgrimage,
trade, marriage, inheritance and the others) are read in full too: their
specific rulings, numbers and ritual details are prime material for
comparison with the Mishnah, the Hittite and Hebrew Bible ritual law, and
Zoroastrian purity law. Chunks are about 2,000 hadith-lines.

**Two outputs per chunk:**

1. **Motif tags**, as in the Quran read: units of one hadith or a short run on
   one subject, in `data/motif-tags/hadith/NN-<slug>.yaml`, tradition
   `islam`, corpus `hadith`. Reuse the Quran readers' ids first.
2. **Observation records** for every narrative or ritual detail:
   - slot-structured: agent, action, object, recipient, instrument, place,
     time, number, name, quoted words;
   - stored in `data/records/hadith/NN-<slug>.yaml`.

   This is the new matching currency. See `data/records/README.md`.

**Links to the Quran.** Book 60 (tafsir) and many other hadith name the verse
they explain or the occasion of its revelation. Record those links
explicitly, as `quran: ["2:255"]` on the unit. They let a hadith detail be
anchored to the Quran verse it expands, so the Ledger's annotated-Quran page
can show it under that verse.

## Observation records (if `data/records/README.md` does not exist yet)

Define the schema, a validator (`tools/records.py --validate`) and the
README yourself, as `reading-at-scale.md` describes the layer. Then record in
`docs/CLEANUP.md` that the ANE pilot's schema, if it appears later, must be
merged with yours.

## After the read

1. **Merge near-duplicate motifs.**
2. **Make the Islamic side Quran + hadith.**
   - Generalize `tools/compare.py` so that the Islamic side of a pair can be
     the Quran and the hadith together. Add the side `islam` = `quran` ∪
     `hadith`.
   - Rerun the comparisons that already exist with the hadith added:
     HB × Islam, and ANE × Islam if it has run. For each pair, compare only
     the hadith units against the other tradition's units; the Quran side
     is already done.
   - Use blind judges: they do not see the readers' hints.
   - Record specific parallels, echoes and deliberate divergences only, as
     "Discovery, not confirmation" requires.
   - Make sure the generalized `compare.py` keeps `hb-quran` working.
3. **Run the pipeline.**
   - Commands: `motifs.py --write-leads`, `lexical.py --write-leads`,
     `linguistic.py` (add a hadith adapter using the corpus's surface forms;
     the Quranic Arabic Corpus lemmas cover only the Quran), `originals.py`
     (fill hadith passages, with the canonical URL where known), `coverage.py`,
     `build.py`.
   - **Ledger.** The annotated-Quran page shows each verse's linked hadith.
     A lead may now have a hadith on the Islamic side.
4. **Add a dated entry to `docs/CLEANUP.md`.**
5. **Report:**
   - the inventory: books and hadith read, and anything left out;
   - the Quran ↔ hadith links made;
   - comparison counts by relation;
   - the most interesting hadith ↔ HB and hadith ↔ ANE leads and divergences,
     with references on both sides (hadith number, Shamela page and
     canonical URL).

## Known leads (benchmarks, not reading targets)

- The raven teaching burial; Cain's punishment (against *Pirqei de-Rabbi
  Eliezer* 21).
- Moses and the stone that ran off with his clothes (against the rabbinic
  Moses traditions).
- Solomon's hundred wives and the "in shāʾ Allāh" omission.
- The hadith of the night journey's ladder (*miʿrāj*) against the ascent
  literature.
- Dajjāl and the Antichrist traditions.

These are benchmarks only. Do not give them to the readers.

## Stance: Islamic, and academic

The project reads the hadith as the Islamic tradition reads it, and reports
it as an academic would.

- **The hadith as *bayān*.** The hadith is the Quran's primary explanation.
  Links from hadith to verse are the tradition's own; record them as such.
- **Gradings are the tradition's.**
  - Use the attributions al-Jāmiʿ al-Kāmil gives, or a grading a tool result
    states, credited to whoever made it.
  - The project never grades a hadith itself.
- **No theory of hadith dating in the data.**
  - The Western debates on dating and authenticity (Schacht, Juynboll,
    Motzki and others) are not built into tags, records or leads.
  - The wording stays neutral about who influenced whom, and leads keep
    `standing: proposed`. A scholar's view may be cited in a lead's notes,
    attributed, as one view among others.
- ***Isrāʾīliyyāt* are a separate layer.**
  - Reports drawn from Jewish and Christian lore, found mostly in tafsir, are
    where many academic parallels lie. Islamic scholarship treats them as
    weak or of outside origin.
  - Al-Jāmiʿ al-Kāmil collects only ṣaḥīḥ hadith, so they will mostly be
    absent here. Do not add them to this corpus.
  - Record in `docs/CLEANUP.md` a later, clearly labelled *isrāʾīliyyāt*
    layer (for instance from al-Ṭabarī's tafsir), with its own corpus id, so
    that it never mixes with the ṣaḥīḥ hadith.
- **Respect.** Keep the notes descriptive and respectful. The Prophet and the
  Companions are named as the sources name them.

## Rules

- **Originals first.** Every claim states its basis.
- **Grounding and citation.**
  - Follow the Hadith and Shamela tools' grounding rules.
  - Never quote a hadith from memory.
  - Cite as the tools require.
  - Attach to every hadith citation the canonical URL the Hadith tool returns.
- **Never grade a hadith yourself.** Report a grading only when a tool result
  states it, and attribute it.
- **Keep raw text out of git.**
- **Pull requests:** don't create any unless asked.
- **Other sessions' folders:** don't edit their tag or alignment folders.
  The Quran's motif files in `data/motif-tags/quran/` stay as they are.
  Links go on the hadith units.
