# Cleanup log

The project gets one thorough cleanup and reorganization **after every
tradition's texts have been read and compared**. Until then, each text adds
to this log whatever it leaves behind, so that the final pass works from a
list.

Between texts, do only the light tidy that would otherwise compound:
- merge obvious near-duplicate motifs after each read (`data/motif-aliases.yaml`);
- keep the tools working for any pair of texts;
- give every divergence, response and contrast a neutral id.

Everything else waits for the final pass.

## How to add an entry

After each text or tradition, add a dated section under "Entries" with:
- what was added;
- what it left behind (counts where possible);
- any shortcut taken that the final pass should undo.

Keep entries factual and short.

## Standing items for the final pass

- **Motif vocabulary.** Consolidate it into a structure that serves every
  tradition: canonical ids, clusters and any hierarchy. Resolve label
  variants and alias chains, and drop or fold ids nobody uses.
- **Derived divergence ids.** Re-examine the `<motif>-as-<relation>` ids made
  by the loader against the neutral ids readers defined, and keep one
  scheme.
- **Units from secondary knowledge.** Replace or retire every unit not read
  from an original.
- **Stale leads.** Decide each one: keep it with a note, or delete it.
- **Lead organization.** Arrange the lead files, for example in subfolders by
  tradition pair, and decide how human leads and pipeline leads sit together.
- **Tools.** Remove one-pair assumptions and dead code, consolidate the
  per-corpus helpers, and add tests for the loaders and validators.
- **Docs.** Rewrite the READMEs and the reading and comparison protocols as
  one description of the system as it finally stands.
- **Ledger.** Redesign it for the full scale: navigation across traditions,
  performance, and highlighting the decisive words in the originals (this
  needs the exact original words recorded in a structured field).
- **Git history.** Decide whether to squash the "WIP snapshot" commits that
  the stop hook produced.

## Entries

### 2026-10-31: Ancient Near East, read in full and compared with the Quran

**Added:**
- the ANE corpus in the original: 1,610 texts, 117,278 lines in 6 traditions (Sumerian, Akkadian,
  Egyptian, Hittite/Hurrian, Ugaritic, Northwest Semitic inscriptions), fetched by `tools/anefetch.py`
  and `tools/ane_sources/` into `data/raw/ane/` (scope and licenses: `data/ane/SCOPE.md`);
- the full read: 54 chunks, 3,015 units in `data/motif-tags/ane/`, every line covered;
- the ANE × Quran comparison, judged blind (no readers' hints): 31 chunks, 1,105 matches in 1,059
  pairs (476 divergence, 321 echo, 278 parallel, 19 contrast, 11 response); 2,237 of 3,015 units
  have no match;
- observation records on every match (`data/records/README.md`);
- loan chains and cognates (`tools/anelex.py`), with an inherited/loan class on each chain;
- ANE traces: Quran words concentrated in one narrative followed to their ANE cognates. The
  al-yamm → Yammu (KTU 1.2) trace is a benchmark;
- the ANE linguistic layer and ANE rows in `results/COVERAGE.md`;
- 4,853 leads (3,612 on the Quran); 1,096 are ANE × Quran.

**Deferred:**
- ANE × Hebrew Bible side-by-side pass. The user chose ANE × Quran only; the 441 ANE × HB leads
  come from shared motif ids alone.

**Left behind:**
- **Vocabulary:** 7,377 motif ids defined by the ANE read; 4,459 are used once. The third merge
  round folded 153 (480 pairs judged). The comparison pass coined 700 more neutral ids in parallel,
  some overlapping across chunks (`no-one-changes-the-spoken-word` ~ `immutable-divine-word`).
  Neutral ids live in alignment files, not the vocabulary, and the validator does not catch an id
  redefined with a different label (`dominion-from-sunrise-to-sunset`).
- **Tags that lead:** some ANE tag labels carry Hebrew Bible or Quran wording onto lines that do not
  say it (`yhwh-my-shepherd` and `vanity-of-vanities` on Sumerian; `adopt-as-son-perhaps-useful`
  with the Q 28:9 wording on CTH 363.1; `protective-spirits-go-before-and-behind` on a text with
  right and left; `slanderers-eat-pieces-before-king` on EA 097, where the text has none). Some Quran
  tag notes carry Hebrew Bible comparison notes that blind judges can see.
- **Witnesses as separate units:** manuscript witnesses of one text are separate units (BD 125, the
  Eloquent Peasant, Sinuhe, SAA 2 6 and its Tayinat copy SAA 2 15), so a correspondence can be
  recorded once per witness and counted several times. Group witnesses.
- **One-slot flags:** `compare.py flags` found only 3 matches, because judges word the two sides of a
  record differently even where the texts agree. It needs normalized or fuzzy slot comparison.
- **Text data:**
  - some Ugarit texts labelled `ane-ugaritic` are in Akkadian;
  - Hittite edition footnotes are pasted into last lines;
  - the CTH 133 §10-12 German glosses are shifted against the transliteration;
  - CTH 396.3 §3:8 "stehend" mistranslates TUŠ-aš, and CTH 402 §41 is duplicated;
  - Mesha lines 10 and 21 keep Wikisource `<pagequality>` markup;
  - ORACC glosses misread some words (*wašāru*, *mašlu*);
  - ORACC Sumerian composites (Dumuzid, Martu, the laments) and the SAA texts have word glosses
    only, and the Northwest Semitic inscriptions have no lemmas or translations;
  - line labels with an en dash for merged lines (`Priv:6–7`) break ranges that start or end on them.
- **Not obtainable:**
  - the Sargon Birth Legend (no ATF), whose unit stays secondary;
  - Old Babylonian Atrahasis II–III (no lines in eBL), so `akk-atrahasis` is assembled from the
    Middle Babylonian fragments only;
  - the Rephaim and Marzeah texts, the Coffin Texts, the Leiden Amun hymns, the Memphite Theology,
    Deir ʿAlla II, Sefire III and Ahiqar.
- **Secondary units:** 18 remain, Sargon among them; Gilgamesh XI, Atrahasis, Eridu Genesis and the
  Two Brothers are now assembled from the read.
- **Lexical:**
  - the Sumerian loan detector has false positives (*silim*/*salām*, *gin*/*kāna*, *qal*/*qalīl*,
    *adama*/*dam*, *satu*/*sadd*);
  - EUPT Ugaritic glosses are German, so trace matches against them are not meaning-checked;
  - the *imnu*/*ayman* trace proposed many unrelated candidates.
- **Tools:**
  - `compare.py unit`/`text` reload everything (about 20 s per call); `dump` was added as a stopgap;
  - `find` searches motif labels only and returns nothing for multi-word queries;
  - validator errors for an alignment ref are reported under the tag file's path;
  - a half-written chunk file breaks validation of the others.
- **Stale leads:** 22 more flagged by the motif track.
- **Git history:** about 75 more "WIP snapshot" commits.

**Shortcuts to undo:**
- Chain leads are written only for loan-like chains. The 108 inherited-vocabulary chain leads made
  in the same run were deleted, not flagged.

### 2026-10-29: Hebrew Bible and Quran, read in full and compared

**Added:**
- the full Hebrew Bible read: 24 chunks, 23,213 verses;
- the full Quran read: 8 chunks, 6,236 verses;
- the HB × Quran comparison pass: 8 chunks, 2,689 matches in 2,298 pairs;
- 2,573 leads in the Ledger.

**Left behind:**
- **Vocabulary:** 11,731 canonical motif ids. 7,110 are used only once and
  453 are not used at all.
- **Label variants:** 99 ids carry different labels in different files.
- **Aliases:** 298, from two merge rounds: after the HB read and after the
  Quran read.
- **Neutral ids:** 1,271 ids were defined by comparison readers, most of them
  neutral ids for divergences. Readers coined them in parallel, so some
  overlap: `divine-sonship`, for example, was reused across chunks, but
  similar ideas may have different ids.
- **Derived ids:** the loader made 760 `-as-<relation>` ids for divergence
  matches that reused one side's id.
- **Secondary units:** 21 units are still tagged from secondary knowledge.
  The Gilgamesh, Atrahasis and Sargon units are to be replaced by the ANE
  read.
- **Stale leads:** 18 leads are flagged as no longer produced.
- **Git history:** 21 "WIP snapshot" commits.
- **Tools tied to one pair:** `tools/compare.py` assumes HB × Quran (the ANE
  session is asked to generalize it). `tools/hbread.py vocab` is the shared
  vocabulary search but lives in the HB helper.
- **Ledger:** leads ship in fetched part files (`site/data/`) to stay under
  the host's size limit, which is a stopgap. The decisive words are not
  highlighted in the verses.

**Shortcuts to undo:**
- **Internal pairs:** lead files are capped at 30 internal pairs per corpus
  (`MAX_INTERNAL_LEADS`). The rest are only in `results/motifs/pairs.json`.
- **Unshared motifs:** each lead lists at most 12 unshared motifs per side
  (`MAX_ONLY`).
