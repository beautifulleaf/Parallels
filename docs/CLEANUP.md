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
