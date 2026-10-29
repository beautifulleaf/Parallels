# Full read of the Quran: reading protocol

The whole Quran is read verse by verse from the Quranic Arabic Corpus
(Uthmani script) and tagged with motifs. The protocol is the same as the
Hebrew Bible's (`../hb/README.md`); the differences are below.

The goal is lead generation. Surface every detail that might parallel, echo
or answer another tradition, and especially obscure details. The Hebrew Bible
is already fully tagged, so reusing its motif ids wherever the Quran shares a
motif is what makes cross-tradition matches appear.

## Steps for a reader

1. **Print the text.** Use `python3 tools/qread.py surah <s1> <s2>` or
   `python3 tools/qread.py range <s>:<v1>-<v2>`, a portion at a time. Read
   every verse. `python3 tools/qread.py plan` shows the chunks.
2. **Search the vocabulary by keyword.** It holds about 8,000 motifs, so do
   not print it all. Use for example `python3 tools/hbread.py vocab flood`,
   `python3 tools/hbread.py vocab golden calf` or
   `python3 tools/hbread.py vocab staff serpent`. Use an existing id when it
   fits. Define new ids under `new_motifs` only when nothing fits.
3. **Write your file.** Use `data/motif-tags/quran/NN-surah-S.yaml`, where NN
   is the chunk number and S the first surah, for example `04-surah-12.yaml`.
4. **Validate.** Run `python3 tools/motifs.py --validate <your file>` until it
   prints ok. It checks references, read ranges, chunk boundaries and full
   coverage of the chunk.
5. **Keep scratch files** only in `<scratchpad>/quran-chunkNN/`. Touch no
   repo file except your own. Do not commit.

## File format

```yaml
new_motifs:
  hoopoe-brings-news: {label: "A hoopoe brings the king news of a distant queen", cluster: solomon}
units:
  - id: quran-27-solomon-hoopoe        # quran-<surah>-<slug>, unique
    tradition: islam
    title: Solomon, the hoopoe and the Queen of Sheba
    corpus: quran
    original: true
    tagger: Claude (model), reading the Arabic
    read: ["27:15-44"]
    tags:
      - {motif: hoopoe-brings-news, refs: ["27:20", "27:22"]}
      - {motif: queen-of-sheba-tests-with-riddles, refs: ["27:41", "27:42"], note: "here the test is a disguised throne"}
    hints:
      - "Compare Targum Sheni to Esther 1:2 (the hoopoe/bird and the queen)."
```

References are `surah:verse`. Read ranges are `s:v1-v2` and may list several
ranges. Every verse of the chunk must be in some unit's `read`.

## What to tag

- **Narratives:** prophets, peoples and parables, episode by episode, with
  concrete motifs. Prefer the Hebrew Bible's ids for shared material (Adam
  and Iblis, Noah, Abraham, Lot, Joseph, Moses and Pharaoh, the calf, David,
  Solomon, Jonah, Job). Tag what the Quran has that the Bible lacks with
  equal care.
- **Theology and eschatology:** the divine names and attributes, creation,
  the day of judgment, paradise and hell imagery, intercession, the
  scales, the books of deeds, resurrection proofs.
- **Law and ritual:** prayer, fasting, pilgrimage, food, marriage and
  divorce, inheritance, penalties, oaths. Note where a ruling matches or
  revises biblical or rabbinic law.
- **Polemic and dialogue:** the People of the Book, Christology, claims of
  scriptural alteration, Abraham as neither Jew nor Christian.
- **Form:** oath clusters (by the dawn, by the fig...), the disconnected
  letters, refrains (e.g. 55:13), formulas, and rhetorical patterns.
- **Rare and specific details:** names, numbers, objects and places (al-Jūdī,
  the 300+9 years, the she-camel, Sijjīn) are often the links.

Aim for density. A typical narrative unit has 4–12 tags; a short surah has
2–6.
