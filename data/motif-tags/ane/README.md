# Full read of the ancient Near Eastern corpus: reading protocol

The ANE texts in scope (`data/ane/texts.yaml`, described in
`data/ane/SCOPE.md`) are read line by line in the original and tagged with
motifs, to the same standard as the Hebrew Bible and the Quran. The goal is
lead generation: surface every detail that might parallel, echo, answer or
diverge from another tradition, and above all the Hebrew Bible and the Quran.
A detail that seems minor is often exactly the one that links two texts.

The corpus is split into chunks of about 2,000 lines
(`python3 tools/aneread.py plan`). Each chunk is read by one reader and
written to one file in this folder.

## The originals

| Source | Language | What a line is | Reading aids printed with it |
|---|---|---|---|
| eBL (Gilgamesh, Atrahasis, Enūma eliš, Ludlul, Erra, Maqlû, …) | Akkadian | a verse of the reconstructed text, normalized (`šurippak ālu ša tīdûšu attā`) | eBL's English translation (`=`); `lemmas` shows each word's lemma and dictionary gloss |
| ETCSL | Sumerian | a line of the composite transliteration | ETCSL's English prose translation, by paragraph, printed at the paragraph's first line with the lines it covers (`= [1-10]`) |
| ORACC (SAA treaties, prophecies, literary texts, rituals; Amarna; Ugarit; royal inscriptions; Uruk tablets; Sumerian composites ETCSL lacks) | Akkadian, Sumerian, Ugaritic | a line of the tablet, as transliterated | each word's lemma and gloss (`~`); ORACC's translations are not in its data downloads |
| EUPT (KTU 1.1–1.24, 1.100) | Ugaritic | a line of the tablet, consonantal | EUPT's German translation per colon, printed at the colon's first line (`= [3-4]`) |
| TLA, 2018 open export | Egyptian | a sentence, numbered by the manuscript line where it starts (`5.12`, `5.12/2`) | TLA's German translation (`=`); `lemmas` gives each word's lemma and gloss |
| hethiter.net / TLHdig | Hittite | as the edition numbers it | the edition's translation, where given |
| Northwest Semitic inscriptions | Moabite, Hebrew, Phoenician, Aramaic | a line of the inscription | the edition's translation, where given |

Translations and glosses are reading aids. **What you tag is what the
original says.** Where a translation is free, a restoration or an
interpretation, say so in a `note`, and quote the original words that carry
the motif.

## Steps for a reader

1. **List your texts:** `python3 tools/aneread.py texts <chunk>`.
2. **Print the text** a piece at a time, by text, section or range:
   `python3 tools/aneread.py text 'Gilg SB XI'`,
   `python3 tools/aneread.py text 'ETCSL 1.7.4 C:1-27'`,
   `python3 tools/aneread.py text 'KTU 1.3 III'`. Read every line. Do not
   skim lists, incantation repetitions, letter formulae or broken passages:
   note what survives.
3. **Look up words** when a translation is missing or free:
   `python3 tools/aneread.py lemmas '<ref>'`.
4. **Search the vocabulary** by keyword: `python3 tools/aneread.py vocab flood boat`.
   It has more than 8,000 motifs, so never print it whole. Reuse existing
   ids, above all the Hebrew Bible's and the Quran's, so that matches
   appear. Never redefine an existing id with a different label; if no id
   fits, define a new one under `new_motifs`.
5. **Write your file** as you go, in text order:
   `data/motif-tags/ane/NN-<slug-of-first-text>.yaml`, e.g. `01-etcsl-1-1-1.yaml`.
6. **Validate:** `python3 tools/motifs.py --validate <your file>`, and fix
   every error until it prints `ok`. It checks every reference, that every
   tag cites lines inside its unit's `read` ranges, that every motif id
   exists, that no unit reads outside the chunk, and that the units together
   read every line of the chunk.

Touch no file except your own. Keep scratch files only in your own folder,
`<scratchpad>/ane-chunkNN/`.

## References

A reference is the text's siglum, then the place:

- `Gilg SB XI:11` (section XI, line 11); `Gilg SB XI:11-20`; across sections
  `Gilg SB XI:300-XII:5`; a whole section `Gilg SB XI`; a whole text `Gilg SB`.
- A text with one unnamed section takes the line alone: `ETCSL 1.1.1 5-10`.
- ORACC lines carry their surface and column as the section: `EA 287 r:5`
  (reverse, line 5), `SAA 02 006 o.i:12` (obverse, column i). Egyptian
  manuscript witnesses are sections `W1`, `W2` …, and a line is the
  manuscript line where a sentence starts: `Sinuhe W1:Am.2/2`.
- Always copy the section and line exactly as `aneread.py text` prints them
  (`<section>:<line>`), with the siglum in front.
- Line numbers are kept as edited, primes included (`Gilg OB II:12'`).
  Ranges follow the edition's order, not numeric order.

## File format

```yaml
new_motifs:
  gods-gather-like-flies: {label: "The gods crowd round the sacrifice like flies", cluster: flood}
units:
  - id: ane-gilg-sb-11-flood                  # ane-<text>-<section>-<slug>, unique
    tradition: ane-akkadian                     # as printed by `aneread.py texts`
    title: Ūta-napišti tells the flood (Gilgamesh SB XI)
    corpus: ane
    original: true
    tagger: Claude (model), reading the Akkadian   # the Sumerian, Ugaritic, Egyptian, Hittite, Hebrew, Aramaic, Moabite, Phoenician
    version: Standard Babylonian                 # optional: the version or manuscript tradition
    read: ["Gilg SB XI:1-206"]                  # every line read for this unit
    tags:
      - {motif: warning-through-wall, refs: ["Gilg SB XI:21-22"], note: "igāru igāru šimēma: 'wall, wall, listen!'"}
      - {motif: bird-release, refs: ["Gilg SB XI:147-156"]}
    hints:                                      # optional; from memory, not from the text
      - "Compare Gen 8:6-12 (raven and dove) and Q 11:44."
```

## Fragmentary tablets

- **Tag only what the preserved text says.** A restoration in square
  brackets may carry a tag only if the note says it rests on a restoration:
  `note: "restored: [ina quppi]"`.
- **Record lacunae** that matter in a note on the nearest tag, e.g. "lines
  7–12 broken; the dove's return is lost".
- **Versions are separate units.** Old Babylonian and Standard Babylonian
  Gilgamesh, Sumerian and Akkadian versions, the witnesses of an Egyptian
  text: each its own unit, with `version` saying which. A later witness that
  only repeats the main one may be one short unit whose tags note the
  variants.

## What to tag

- **Narrative and myth:** every episode-level motif, concrete and specific:
  "Gods send a flood because human noise keeps them awake", not "flood".
  Names, numbers, objects, places and formulas that recur elsewhere are
  valuable: seven days, the raven, a reed hut, bitumen, the mountain where
  the boat lands.
- **Hymns, prayers, incantations, laments:** divine epithets and titles,
  images (the god as shepherd, as light, riding the storm), the structure of
  a petition or a confession, the ritual acts, the evils named.
- **Wisdom and instructions:** each distinctive saying, and its image.
- **Treaties, oaths, decrees:** the clauses and the curses one by one:
  "Curse: the sky turned to bronze", "Loyalty sworn to the crown prince",
  "The vassal must not listen to a prophet's word against the king".
- **Letters:** what stands out: prostration formulae, the Habiru, a city's
  god, a prophetic word, a ruler calling himself a servant or dust.
- **Royal inscriptions:** the god's anger and return, the chosen king,
  tribute, the restoration of a temple and its gods, a named king of Israel
  or Judah.
- **Lists and omens:** tag what stands out (a long reign, a first, a wonder).

Aim for density. A narrative unit typically has 4–12 tags; a hymn, prayer or
letter 2–6.

## Basis labels

- Every unit read from its original is `original: true`, with
  `tagger: "<model>, reading the <language>"`.
- Parallels you recall from memory go in `hints`, never in tags.
- An interpretive reading carries a `note`.

## New motifs

- **Ids:** kebab-case and descriptive (`reed-hut-warned`, not `m1`).
- **Labels:** one concrete sentence that two readers would apply the same
  way.
- **Clusters:** a short theme name (`creation`, `flood`, `kingship`,
  `cult`, `wisdom`, `cosmology`, `treaty`, `underworld`, `prophecy` …).
- Before adding one, search the vocabulary. Near-duplicates are merged after
  all chunks are read.
