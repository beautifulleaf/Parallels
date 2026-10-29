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
| `relations` | yes | — | one or more of `inheritance` · `transmission` · `convergence` · `response` |
| `direction` | no | — | free text when the relation is directional, e.g. `islam -> christianity-western` |
| `standing` | yes | — | scholarly standing of the claim: `established` · `proposed` · `contested` · `fringe` |
| `traditions` | yes | — | two or more ids from `data/traditions.yaml` |
| `layers` | yes | — | one or more of `lexical` · `motif` · `concept` |
| `motifs` | no | — | kebab-case motif tags |
| `concepts` | no | — | kebab-case concept tags |
| `lexical` | no | — | list of `{lang, form, translit, gloss}` |
| `passages` | no | — | list of `{tradition, ref, text?, note?}`; `text` only when it comes from a verified source |
| `evidence` | no | — | list of strings: counts, observations, arguments |
| `sources` | no | — | list of `{label, url?}` |
| `benchmark` | no | — | `true` for the v0 gold set of known parallels |
| `origin` | yes | — | `human` or `pipeline` |
| `added` | yes | — | ISO date |

`status` records your review. `standing` records where scholarship stands.
They are independent: an `established` parallel can still be `rejected` as
uninteresting, and a `fringe` one can be `promising` for your purposes.

## Body

Free Markdown. The pipeline never touches it. Suggested headings are
`## Questions` and `## Notes`.

Run `python3 tools/build.py` to validate every lead and regenerate the
artifact.
