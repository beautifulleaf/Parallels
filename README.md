# Parallels

A lead-generation engine for parallels, convergences, and responses across
religious and philosophical traditions. It surfaces candidates, and humans
investigate them.

- [PLAN.md](PLAN.md): scope, relation types, architecture, phases
- [TRADITIONS.md](TRADITIONS.md): an outline for each tradition
- [leads/](leads/): one file per lead, with review status and notes ([format](leads/README.md))
- [data/traditions.yaml](data/traditions.yaml): the tradition taxonomy

## Build

```bash
pip install pyyaml
python3 tools/build.py          # validate leads, regenerate site/index.html
python3 tools/build.py --check  # validate only
```

`site/index.html` is the searchable Parallels Ledger. It is generated from
`site/template.html` and the lead files, so edit those rather than the output.
