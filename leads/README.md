# Leads

One file per lead: `leads/<id>.md`. Each file has YAML front matter followed by
free-form Markdown review notes. Git history serves as the review log.

The pipeline may create leads and refresh their evidence. It never changes the
fields marked **human** below, and it never changes the notes body.

## Front matter

| Field | Required | Owner | Values |
|---|---|---|---|
| `id` | yes | — | kebab-case; must match the filename |
| `title` | yes | — | short headline |
| `summary` | yes | — | one or two sentences |
| `status` | yes | **human** | `new` · `investigating` · `promising` · `rejected` |
| `relations` | yes | — | one or more of `internal` · `inheritance` · `transmission` · `convergence` · `response` (`internal` = a pattern inside one tradition's text) |
| `direction` | no | — | free text when the relation is directional, e.g. `islam -> christianity-western` |
| `standing` | yes | — | scholarly standing of the claim: `established` · `proposed` · `contested` · `fringe` |
| `traditions` | yes | — | ids from `data/traditions.yaml`; two or more unless the only relation is `internal` |
| `layers` | yes | — | one or more of `lexical` · `motif` · `concept` |
| `motifs` | no | — | kebab-case motif tags (pipeline leads use narrative ids here) |
| `concepts` | no | — | kebab-case concept tags |
| `lexical` | no | — | list of `{lang, form, translit, gloss}` |
| `passages` | no | — | list of `{tradition, ref, text?, lang?, source?, translation?, note?}`. `text` is always the original language, filled by `tools/originals.py` from the corpora; `translation` is optional and secondary |
| `evidence` | no | — | list of `{text, basis}`; `basis` is `original` (read or counted from the original text), `reading` (a reader's interpretation of the original, e.g. a motif tag), `lexicon` (a cited dictionary), `gloss` (depends on English glosses or translations), or `scholarship` (a secondary-literature claim to verify) |
| `sources` | no | — | list of `{label, url?}` |
| `benchmark` | no | — | `true` for the v0 gold set of known parallels |
| `reviews` | no | **human** | list of `{by, date, verdict, scope?, note?}`; `verdict` is `confirmed` · `corrected` · `disputed` |
| `origin` | yes | — | `human` or `pipeline` |
| `added` | yes | — | ISO date |

`status` records your review. `standing` records where scholarship stands.
They are independent: an `established` parallel can still be `rejected` as
uninteresting, and a `fringe` one can be `promising` for your purposes.

## Checking a lead in the original

Every lead shows the original-language text of its passages first. English
glosses appear only as reading aids. Evidence marked `gloss` or `scholarship`
is the part that most needs a reader of the original.

After checking, add an entry to `reviews` (initials or name are fine):

```yaml
reviews:
  - by: A. Reviewer
    date: 2026-11-02
    verdict: corrected          # confirmed | corrected | disputed
    scope: Arabic passages and cognate
    note: yamm and bahr are not interchangeable in 20:77-78; see notes.
```

Correct the lead itself where needed, and explain in the notes. The pipeline
never edits `reviews`, `status`, or the notes.

## Body

Free Markdown. The pipeline never touches it. Suggested headings are
`## Questions` and `## Notes`.

Run `python3 tools/build.py` to validate every lead and regenerate the
artifact.
