# Observation records

Motif tags say *what kind of thing* a passage contains. Observation records
say *exactly what happens*: who acts, what they do, to what, with what, where,
when, how many, under what name, with what words, and how it ends. Two
passages that share a motif can then be compared slot by slot. A deliberate
divergence shows up as two records that agree in every slot but one, such as
the same bird released from the same vessel with a different outcome.

The records were first used in the ANE × Quran comparison pass
(`data/alignments/ane-quran/`), where each match carries one. The Quran
observation layer and the hadith read
(`docs/prompts/hadith-full-read.md`) store them per passage in
`data/records/<corpus>/`.

## Slots

| Slot | What goes in it | Example |
|---|---|---|
| `agent` | who acts | Utnapishtim; Nūḥ; the sun god |
| `action` | the act, as a short verb phrase | releases a bird |
| `object` | what is acted on | raven |
| `recipient` | to or for whom | the gods; Pharaoh |
| `instrument` | with what | a reed wall; a staff |
| `place` | where | Mount Nimuš; al-Jūdī |
| `time` | when, or how long | seventh day; forty nights |
| `number` | a count the text gives | 7; 950 years |
| `name` | a proper name, title or epithet used in the passage | Lord of the worlds |
| `quoted` | the decisive words, in the original, transliterated | ul iturram (it did not come back) |
| `outcome` | how it ends | does not return |

Rules:

- **Values come from the text in front of you.** Write in English, but keep
  names and the decisive words in the original (transliterated). If a slot is
  not in the passage, leave it out; do not fill it from the other text or
  from what you know.
- **Short and comparable.** Use the same wording on both sides where the
  texts agree ("releases a bird" and "releases a bird"), so a machine can see
  the agreement; let the wording differ only where the texts do.
- **Fill only what matters for the match.** Three or four slots usually
  suffice. A slot that agrees on both sides is evidence; a slot that differs
  is a candidate divergence.

## In a comparison file

Each match has a `record`: every slot is a pair `[this side, other side]`,
with `null` for a side that lacks it.

```yaml
      - with: quran-11-noah-ark
        motif: bird-release
        refs: ["Gilg SB XI:154-156"]
        with_refs: ["11:44"]
        relation: divergence
        record:
          agent: [Utnapishtim, null]
          action: [releases a raven, null]
          outcome: [raven does not return, the waters are made to sink]
        note: "..."
```

`python3 tools/compare.py <pair> validate <file>` checks the slots, and
`python3 tools/compare.py <pair> flags` lists the matches whose records
agree in every filled slot but one (at least three slots filled on both
sides).

## Per passage (`data/records/<corpus>/NN-<slug>.yaml`)

```yaml
records:
  - id: q-7-133-blood            # neutral id: corpus, ref, a word
    ref: "7:133"
    unit: quran-7-plagues        # the motif-tag unit containing it
    agent: God
    action: sends plagues
    object: [flood, locusts, lice, frogs, blood]
    recipient: Pharaoh's people
    number: 5
    quoted: "al-ṭūfān wa-l-jarād wa-l-qummal wa-l-ḍafādiʿ wa-l-dam"
```

Here each slot holds one side's value, and a list where the text gives
several. The validator for this form (`tools/records.py --validate`) comes
with the Quran observation layer.
