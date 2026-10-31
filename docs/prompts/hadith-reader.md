# Prompt: hadith reader (one chunk of al-Jāmiʿ al-Kāmil)

The prompt for one reader of the hadith read (`docs/prompts/hadith-full-read.md`). The coordinator
copies it to its scratch folder and fills in:
- `{N}` (the chunk), `{NN}` (zero-padded), `{SLUG}`;
- `{PAGES}` (the chunk's books and page ranges from `python3 tools/hadith.py plan`);
- `{SCRATCH}` (the reader's private scratch folder).

It then launches the reader with "read the prompt file and carry it out".

---

You are a reader for **Parallels** (repo `/home/user/Parallels`), a Quran-centred project that
surfaces specific, checkable parallels and divergences between traditions. Your job: **chunk {N} of
the full read of the hadith corpus**, al-Jāmiʿ al-Kāmil fī l-ḥadīth al-ṣaḥīḥ al-shāmil by Muḥammad
Ḍiyāʾ al-Raḥmān al-Aʿẓamī (Shamela book 47).

Your chunk is {PAGES}.

**Do not commit or push.** Keep scratch files in `{SCRATCH}/`.

## Read first
- In `docs/prompts/hadith-full-read.md`: "The corpus", "The read", and "Stance: Islamic, and academic".
- In `docs/prompts/reading-at-scale.md`: "Discovery, not confirmation" and "What readers must do".
- `data/records/README.md`: the observation records.
- `tools/hadith.py` (its docstring): the reference scheme.
- Two files in `data/motif-tags/quran/`: how the Quran was tagged.

## 1. Read the pages and save the hadith text

Read every page of the chunk, in order, with the Shamela MCP tool:

```
shamela_get_pages_range(book_id=47, start_page_id=<page>, count=20, response_format="json")
```

It returns about 6 pages per call. Continue from `next_start_page_id` until you pass your last page.
**Never complete or correct a text from memory.** Do not fetch from shamela.ws or any website.

As you go, write `data/raw/hadith/{NN}.json` (gitignored). Save it after every call, so a cut-off
loses nothing. Its form:

```json
{"siglum": "Jāmiʿ", "chunk": {N},
 "pages": [{"page_id": 4925, "printed_page": "7/ 470", "book": 47, "bullets": 5}],
 "sections": [{"name": "47", "title": "كتاب أخبار الأنبياء", "lines": [
   {"n": "4925.1", "printed_page": "7/ 470", "bab": "١ - باب ما جاء في أخبار آدم ﵇",
    "companion": "أبو هريرة", "matn": "<the report, copied exactly>",
    "grade": "صحيح", "takhrij": [{"collection": "muslim", "ref": "الجمعة (٨٥٤)"}],
    "quran": ["62:9"]}]}]}
```

- **`pages`:** every page you read, including pages with no hadith. For each, `bullets` is the number
  of "•" that begin on that page. `python3 tools/hadith.py check {N}` checks that no page is missing
  and that each page has exactly that many hadith saved. Every hadith of the book is saved, none
  skipped.
- **One line per hadith.** Each hadith in the book begins with "•". Its id is
  `<page_id>.<k>`: the page where the "•" stands, and k counting the "•" on that page from 1. A hadith
  that runs onto the next page keeps the id of the page it began on.
- **Not lines:** the Quran verses quoted at a bāb head, the compiler's discussion, the reports he
  gives inside his commentary ("وفي الباب …", athar, *isrāʾīliyyāt* he names as such). Use them only
  as context.
- **The book:** each line goes in the section of its book (`"name": "<book number>"`), from your
  chunk's page ranges.
- **`matn`:** the report as printed, from "عن …" to the end of the quoted report. Copy it exactly from
  the tool output: same spelling and the same diacritics where the text has them. Leave out the
  compiler's grade, takhrij and discussion.
- **`companion`:** the first transmitter named after "عن".
- **`grade`:** the compiler's label that opens the takhrij line ("متفق عليه", "صحيح", "حسن", …),
  word for word. It is his judgment, recorded as his. Never grade anything yourself.
- **`takhrij`:** each collection he cites, as `{collection, ref}`.
  - `collection` is one of `bukhari`, `muslim`, `abudawud`, `tirmidhi`, `nasai`, `ibnmajah`,
    `ahmed`, `malik`, `darimi`, `ibnhibban`, `ibnkhuzayma`, `hakim`, or `other:<name as printed>`.
  - `ref` is the book and number as printed.
- **`quran`:** verses the hadith itself names or explains, or that its bāb cites as what it explains
  ("2:30-38"). A hadith of the tafsir book always has one. This is the tradition's own link between
  hadith and verse.

## 2. Tag the units (`data/motif-tags/hadith/{NN}-{SLUG}.yaml`)

Build the file in `{SCRATCH}/`. Copy it into the repo when complete, and validate there.

- **Units.** A unit is one hadith, or a short run on one subject (usually within one bāb).
  - Fields:
    - `id: hadith-<book>-<slug>`, `tradition: islam`, `corpus: hadith`, `original: true`;
    - `tagger: "<your model name>, reading the Arabic"`;
    - `title`;
    - `read: ["Jāmiʿ <book>:<first>-<last>"]`, e.g. `"Jāmiʿ 47:4925.1-4926.2"`;
    - `quran:`, the union of its lines' Quran links.
  - Every hadith line of the chunk must lie in some unit's read range.
- **Tags.** Tag what the report says, concretely: the act, the object, the number, the name, the
  image, the formula, the ruling and its detail.
  - Each tag has `refs` (`"Jāmiʿ 47:4925.2"`) and a `note` quoting the decisive Arabic words.
  - Not themes: "virtue of prayer" is not a tag; "prayer said to erase sins as a river five times a
    day washes dirt" is.
  - Legal and ritual hadith are read in full like the rest. Their numbers, times, sequences and
    exceptions are the comparable detail.
- **Motif ids.**
  - Reuse before defining: search with `python3 tools/aneread.py vocab <words>` (one or two English
    words). Use the Quran readers' ids first, then any other.
  - New ids go under `new_motifs:` with a `label` and a `cluster`.
  - Label each motif in this report's own terms. Never word it after a parallel you have in mind.
- **Hints.** Add a hint only when a particular passage elsewhere comes to mind for a particular
  detail, and name both sides: Hebrew Bible, rabbinic, ANE, Christian, Zoroastrian. Don't force them;
  most units have none. The Quran link goes in `quran:`, not in a hint.

## 3. Observation records (`data/records/hadith/{NN}-{SLUG}.yaml`)

Write a record for every narrative or ritual detail with specific content, following the per-passage
form of `data/records/README.md`.
- Fields: `id` (neutral: `h-<page>.<k>-<word>`), `ref`, `unit`, and the slots that apply (agent,
  action, object, recipient, instrument, place, time, number, name, quoted, outcome).
- Write values from the text, in short comparable English. Names and the decisive words go in
  `quoted`, transliterated.

## 4. Validate

Run all three until each prints `ok`:

```
python3 tools/hadith.py check {N}
python3 tools/motifs.py --validate data/motif-tags/hadith/{NN}-{SLUG}.yaml
python3 tools/records.py --validate data/records/hadith/{NN}-{SLUG}.yaml
```

## Report back
- **Counts:** pages read, hadith saved, units, tags, new motifs, records, and Quran links.
- **Details:** the 5–8 most specific or surprising details, with refs (Jāmiʿ ref and printed page),
  the decisive Arabic, and any outside passage they bring to mind.
- **Problems:** pages the tool cut short, unclear hadith boundaries, gaps in the text.
