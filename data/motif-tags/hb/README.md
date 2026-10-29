# Full read of the Hebrew Bible: reading protocol

The whole Hebrew Bible is read verse by verse from the Westminster Leningrad
Codex (Hebrew and Aramaic) and tagged with motifs. The goal is lead
generation: surface every detail that might parallel, echo or answer another
tradition (Quran, rabbinic and Christian literature, the ancient Near East,
Greek, Iranian, Indic and Chinese material), and especially obscure details.
A detail that seems minor is often exactly the one that links two texts.

The canon is split into 24 chunks (`python3 tools/hbread.py plan`). Each chunk
is read by one reader and written to one file in this folder.

## Steps for a reader

1. **Print the text.** Use `python3 tools/hbread.py text <Book> <c1> <c2>`, a
   few chapters at a time. Read every verse. Do not skim or skip genealogies,
   lists, laws or poetry.
2. **Check the vocabulary.** `python3 tools/hbread.py vocab` prints the
   existing motifs. Use an existing id when it fits. Otherwise define a new
   one under `new_motifs` in your file.
3. **Write your file.** Use `data/motif-tags/hb/NN-<first-book>-<first-chapter>.yaml`,
   for example `01-gen-1.yaml`. Write it as you go, in chapter order.
4. **Validate.** Run `python3 tools/motifs.py --validate <your file>` and fix
   every error. Validation checks that every reference resolves to a real
   verse, that every tag cites a verse inside its unit's `read` ranges, and
   that every motif id exists.
5. **Check coverage.** The `read` ranges of your units must together cover
   every verse of your chunk. The validator prints how many verses your units
   read; it must equal the chunk's verse count.

Touch no file except your own. Keep scratch files only in your own folder,
`<scratchpad>/chunkNN/`: readers run in parallel, and shared scratch file
names have mixed one reader's units into another's file. The validator
rejects any unit outside your chunk.

## File format

```yaml
new_motifs:
  boy-raised-by-priest: {label: "Child raised by a priest at a sanctuary", cluster: childhood}
units:
  - id: hb-1sam-1-hannah                # hb-<book>-<chapter>-<slug>, unique
    tradition: judaism
    title: Hannah's vow and Samuel's birth
    corpus: hebrew-bible
    original: true
    tagger: Claude (model), reading the Hebrew   # "reading the Aramaic" for Aramaic sections
    read: ["1Sam 1:1-28"]                 # every verse read for this unit
    tags:
      - {motif: mother-dedicates-child, refs: ["1Sam 1:11"]}
      - {motif: barren-wife-rival-wife, refs: ["1Sam 1:2", "1Sam 1:6"], note: "Peninnah provokes her"}
    hints:                                # optional; from memory, not from the text
      - "Compare Quran 3:35 (Imran's wife's vow) and Protevangelium of James 4."
```

- **References:** use book codes as printed (`Gen`, `Exod`, `1Sam`, `Ps`,
  `Song` …). Write a verse as `Gen 6:14`. Write a range as `Gen 6:1-22`, a
  whole chapter as `Gen 6`, or a range across chapters as `Gen 6:9-9:29`.
- **Units:** one per episode, speech, law collection, psalm or oracle, and
  usually 5–40 verses. Every verse of the chunk belongs to at least one unit.
- **Tags:** cite the exact verses. Tag only what the text says. Add a `note`
  when a tag involves interpretation or when a precise wording matters.
- **Hints:** for parallels you know of from other texts. They come from
  memory, so they are kept separate from tags and labeled as secondary.

## What to tag

- **Narrative:** every episode-level motif, concrete and specific. Write
  "Wife of the master tries to seduce the hero", not "temptation". Names,
  numbers, objects, places and formulas that recur elsewhere are valuable.
- **Law:** distinctive rulings and their rationales, e.g. "Eye for an eye",
  "Ox that gores", "Release of slaves in the seventh year", "Prohibition of
  boiling a kid in its mother's milk".
- **Poetry, wisdom, prophecy:** cosmological and theological motifs and
  images, e.g. "Sea monster defeated by God", "Divine council", "Mountain of
  God in the north", "Day of the Lord", "Wisdom personified as a woman",
  "Righteous sufferer argues with God", "Heavenly scroll eaten by the
  prophet".
- **Genealogies and lists:** tag what stands out, such as long lifespans,
  notable firsts, wonders and anomalies.

Aim for density. A typical narrative unit has 4–12 tags. A typical psalm or
oracle has 2–6.

## New motifs

- **Ids:** kebab-case and descriptive (`ark-of-reeds`, not `m1`).
- **Labels:** one concrete sentence that two readers would apply the same way.
- **Clusters:** a short theme name (`creation`, `patriarchs`, `exodus`, `law`,
  `kingship`, `prophecy`, `wisdom`, `cosmology`, `cult` …).
- Before adding a motif, check that the vocabulary has no equivalent.
  Near-duplicates are merged after all chunks are read.
