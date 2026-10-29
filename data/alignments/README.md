# Side-by-side comparison pass

Separate full reads only match where two readers happened to pick the same
motif id: after the full Hebrew Bible and Quran reads, only 22% of the Quran's
tags shared an id with the Hebrew Bible, and 225 of 414 Quran units had no
Hebrew Bible partner. This pass fixes that. A reader takes each unit of one
text, compares it in the original with candidate units of the other text, and
records what really corresponds, and also where the texts deliberately
diverge.

Each folder is one pair of texts (`hb-quran/`). `candidates.yaml` is the plan,
written by `python3 tools/compare.py candidates`. It holds every unit to
compare, its candidates, the reason for each, and the chunk it belongs to.
`NN-<slug>.yaml` holds a reader's results for chunk NN.

## Steps for a reader

1. `python3 tools/compare.py show <chunk>` lists your units and their
   candidates.
2. For each unit, run `python3 tools/compare.py unit <id>` and
   `python3 tools/compare.py text <id>`: the tags, the hints and the original.
3. Run the same two commands for each candidate. Triage on the tags first,
   then read the original of every candidate that might correspond.
4. Look beyond the candidates. `python3 tools/compare.py find <words>` lists
   Hebrew Bible units with matching motifs, and
   `python3 tools/hbread.py vocab <words>` searches the vocabulary. A better
   partner you find yourself goes under `checked` and `matches` like any
   other.
5. Record each correspondence you can point to in **both** originals, citing
   each side's own verses.
6. Validate: `python3 tools/compare.py validate <your file>` until it prints
   ok. It checks that every unit of the chunk is reviewed, every candidate is
   listed under `checked`, refs are inside each unit's read ranges, and
   motifs exist.

## File format

```yaml
new_motifs:
  thunder-praises-god: {label: "Thunder is God's voice, or praises him", cluster: nature}
reviewed:
  - unit: quran-13-thunder-and-lightning       # a unit of your chunk
    checked: [hb-ps-29-voice-of-yhwh, hb-job-37-thunder, hb-prov-11-sayings]   # every candidate, plus any you found
    matches:
      - with: hb-ps-29-voice-of-yhwh
        motif: thunder-praises-god              # an id already on one side, or a new one
        refs: ["13:13"]                         # verses in `unit`
        with_refs: ["Ps 29:3", "Ps 29:9"]       # verses in `with`
        relation: parallel                      # parallel | echo | divergence | response | contrast
        note: "yusabbiḥu r-raʿdu bi-ḥamdihi; qôl YHWH ʿal-hammāyim: the thunder praises vs. the thunder is his voice"
```

- **relation:**
  - `parallel`: the same motif or story element.
  - `echo`: a shared phrase or image.
  - `divergence`: the same episode or element with a detail deliberately
    changed: who acts, a title, an outcome, the order, what is left out. For
    example, Moses goes to Pharaoh from "YHWH, the God of the Hebrews"
    (Exod 3:18, 5:3) but as "a messenger of the Lord of the worlds"
    (Q 7:104, 26:16). A particular god of one people becomes the universal
    Lord. Name the shared element as the motif; the note says what changed on
    each side.
  - `response`: one text explicitly answers or corrects a claim of the other,
    for example 46:38 "no weariness touched him" against Exod 31:17 "he rested
    and was refreshed".
  - `contrast`: opposite rulings on the same matter, for example
    Deut 24:1–4 against Q 2:230.

  **Divergences matter as much as similarities.** Where two units already tell
  the same story, go through it element by element and record each
  deliberate change:
  - divine titles and epithets;
  - who speaks or acts;
  - motives;
  - endings;
  - what one text omits or adds;
  - details reversed.

  Do not record differences that are only a matter of length or genre.
- **motif:** for `parallel` and `echo`, if one side already has a tag that
  fits, reuse its id. The loader adds that tag to the other unit at your refs.
  Otherwise define a shared id under `new_motifs`. Several matches per pair
  are expected; each is one motif.

  For `divergence`, `response` and `contrast`, use a **neutral id** that names
  the shared matter, such as `payment-for-a-life` or `divine-title-sent-to-pharaoh`.
  Do not use one side's claim, because the loader would put a label such as
  "no ransom for a murderer" on the verse that says the opposite. Reuse a
  neutral id when one already exists.
- **note:** quote or transliterate the decisive words of each side. The note
  is what the people checking the Arabic and Hebrew will check first.
- An empty `matches` list is a result: those candidates were compared and
  nothing corresponds.

## How the results are used

`tools/motifs.py` loads these files after the tag files. Each match becomes a
shared tag on both units, with a `via` field naming the file. Every confirmed
pair becomes a lead, even on a single motif, and its evidence says it was
confirmed side by side. The tag files themselves are not edited.
