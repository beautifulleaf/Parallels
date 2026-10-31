# Prompt: side-by-side comparison judge

The prompt for one judge of a `<corpus> × Quran` comparison pass, as used in the ANE × Quran pass
(31 chunks, 2026-10-31). The coordinator copies it to its scratch folder and fills in:
- `{PAIR}` (e.g. `ane-quran`), `{N}` (chunk number) and `{NN}` (zero-padded);
- `{SIDE}` (the reviewed corpus, e.g. "ANE") and `{LANGS}` (its languages);
- `{SCRATCH}` (the judge's private scratch folder).

It launches each judge with "read the prompt file and carry it out". The lessons behind it are in
`docs/prompts/reading-at-scale.md` under "After the read".

---

You are a comparison judge for **Parallels** (repo `/home/user/Parallels`), a Quran-centred
project that surfaces specific, checkable parallels and divergences between traditions. Your job:
the **{SIDE} × Quran side-by-side pass, chunk {N}**.

**Do not commit or push.** Build your output in `{SCRATCH}/{NN}-{PAIR}.yaml`; keep all scratch files
in `{SCRATCH}/`. Only when every unit is reviewed, copy it to `data/alignments/{PAIR}/` and validate
it there. The validator needs the repo copy, because it loads the other chunks' motif ids. Edit no
other repo file.

## Read first
- `data/alignments/README.md`: the method and file format. Follow it, with the changes below.
- `data/records/README.md`: the observation-record slots. Every match carries a `record`.
- In `docs/prompts/reading-at-scale.md`, the section **"Discovery, not confirmation"**.

## You judge blind
`python3 tools/compare.py {PAIR} show {N}` lists your {SIDE} units and their candidate Quran units,
without saying why each was proposed. The `unit` command does not show the readers' hints. This is
deliberate: decide from the texts alone. Do not go looking for the hints in the tag files.

**Speed.** Start with one command:

```
python3 tools/compare.py {PAIR} dump {N} {SCRATCH}/units
```

It writes one file per unit (tags plus text) for your units and all their candidates. The `unit` and
`text` commands reload everything and take about 20 s each, so use them only for partners you find
yourself.

## Steps for each unit in your chunk
1. Read the unit's tags and original text, with its translation.
2. Triage the candidates on their tags, then read the Arabic of every candidate that might
   correspond.
3. **Look beyond the candidates.** Most of them come from label similarity and will not hold up.
   Many of the best matches in the ANE pass were with Quran units no tool proposed.
   - Use `python3 tools/compare.py {PAIR} find <word>` (one word at a time).
   - Or search the Quran tag files directly.
   - List any partner you find under `checked` and `matches`.
4. Record only what you can point to in **both** originals, citing each side's own lines and verses.
5. **Manuscript witnesses.** When several units are copies of one text (`witness_of`, or the same
   composition in several manuscripts), record a correspondence once, on the best witness. Leave the
   other copies empty, so one finding is not counted several times.

## What counts
- **A specific element**, not a theme:
  - the same act, object, number, name, formula or image;
  - or the same element with one detail changed (`divergence`).
- **Record each match.** Fill the slots that matter, usually 3–5 of: agent, action, object,
  recipient, instrument, place, time, number, name, quoted, outcome.
  - Write each slot as `[{SIDE} value, Quran value]`, with `null` for a side that lacks it.
  - Use values from the text in front of you, in short comparable wording.
  - **Where the texts agree, write the identical words on both sides.** Let the wording differ only
    where the texts differ: the one-slot divergence flag depends on it.
  - Put the decisive words in `quoted`, transliterated: {LANGS} on the left, Arabic on the right.
  - Quote any value that contains a comma.
- **Neutral ids** for `divergence`, `response` and `contrast` (see the README).
  - First check the shared list of neutral ids other judges have defined, which the coordinator
    names. Reuse an id there before coining one.
- **Never record:**
  - worldview-level contrasts, such as one god against many, creator or none, rebirth against one
    life;
  - generic resemblances, such as both praising a god;
  - a match that rests on a restored word, unless the note says so.

  **An empty `matches` list is a result**, and is expected for most units. A generic match recorded
  to fill the list is worse than none.

## Validate
Copy your finished file to `data/alignments/{PAIR}/{NN}-{PAIR}.yaml` and run
`python3 tools/compare.py {PAIR} validate data/alignments/{PAIR}/{NN}-{PAIR}.yaml` until it prints
`ok`. Fix the scratch copy and copy it again each time.
- Every unit of the chunk must be reviewed.
- Every candidate must be listed under `checked`.
- Write the scratch file incrementally, so a cut-off (an API limit, a restart) loses nothing.

## Report back
- **Counts:** units reviewed, and matches by relation.
- **Best matches:** the 5–8 most specific or surprising, with refs on both sides and the decisive
  words.
- **Weakest matches:** any the checkers should look at first.
- **Data problems:** tags that do not fit their text, restorations, gloss errors, tool problems.
