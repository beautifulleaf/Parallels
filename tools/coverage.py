"""Report what has actually been checked, per corpus and per layer.

Usage: python3 tools/coverage.py

Writes results/COVERAGE.md. The point is to make blind spots visible: a
parallel can only surface from text the pipeline has scanned or a reader has
read.
"""
import pathlib
import sys
import xml.etree.ElementTree as ET
from collections import defaultdict
from datetime import date

import yaml

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import corpora  # noqa: E402
import motifs  # noqa: E402
import originals  # noqa: E402

ROOT = corpora.ROOT


def expand_read(unit, quran_text, hebrew_text):
    """Verse keys ('20:39' or 'Exod.2.3') covered by a unit's `read` ranges."""
    out = set()
    for r in unit.get("read") or []:
        if unit.get("corpus") == "quran":
            out |= set(originals.quran_refs(r, quran_text) or [])
        else:
            out |= set(originals.hebrew_refs(r, hebrew_text) or [])
    return out


def aramaic_only_verses():
    verses = set()
    for book in corpora.BOOK_ORDER:
        tree = ET.parse(corpora.RAW / "oshb" / f"{book}.xml")
        for vel in tree.iter(corpora.OSIS + "verse"):
            morphs = [w.get("morph", "") for w in vel.iter(corpora.OSIS + "w")]
            if morphs and all(m.startswith("A") for m in morphs):
                verses.add(vel.get("osisID"))
    return verses


def pct(a, b):
    return f"{a:,} / {b:,} ({a / b:.1%})" if b else "0"


def main():
    quran, heb = corpora.load_quran(), corpora.load_hebrew_bible()
    quran_text, hebrew_text = originals.load_quran_text(), originals.load_hebrew_text()
    vocab, units = motifs.load()
    taxonomy = yaml.safe_load((ROOT / "data" / "traditions.yaml").read_text(encoding="utf-8"))

    read = defaultdict(set)
    for u in units:
        if u.get("original"):
            read[u["corpus"]] |= expand_read(u, quran_text, hebrew_text)
    aramaic = aramaic_only_verses()

    lines = [f"# Coverage", "", f"Generated {date.today().isoformat()} by `tools/coverage.py`.", "",
             "A parallel can only surface from text that the pipeline has scanned or a reader has read. This "
             "page lists both, so the blind spots are explicit.", "",
             "## Original texts in the repo", "",
             "| Corpus | Verses | Scanned by the lexical track | Inside a narrative label | Read in full for motif tagging |",
             "|---|---|---|---|---|"]
    q_lab = sum(1 for v in quran.verses if v.narratives)
    h_lab = sum(1 for v in heb.verses if v.narratives)
    lines.append(f"| Quran (QAC) | {len(quran.verses):,} | {pct(len(quran.verses), len(quran.verses))} | "
                 f"{pct(q_lab, len(quran.verses))} | {pct(len(read['quran']), len(quran.verses))} |")
    lines.append(f"| Hebrew Bible (WLC/OSHB) | {len(heb.verses):,} | {pct(len(heb.verses) - len(aramaic), len(heb.verses))} "
                 f"(Aramaic sections excluded) | {pct(h_lab, len(heb.verses))} | {pct(len(read['hebrew-bible']), len(heb.verses))} |")
    lines += ["", "Concentration and bridge detection only see verses inside narrative labels. Synonym "
              "and cognate checks see every scanned verse.", ""]

    for name, corpus in (("Quran", quran), ("Hebrew Bible", heb)):
        key = corpus.name
        lines += [f"### {name}: narratives", "", "| Narrative | Labeled verses | Read for motifs |", "|---|---|---|"]
        for nid, nname in corpus.narratives.items():
            refs = {v.ref for v in corpus.verses if nid in v.narratives}
            lines.append(f"| {nname} | {len(refs):,} | {pct(len(refs & read[key]), len(refs))} |")
        lines.append("")

    lines += ["## Motif units tagged from secondary knowledge", "",
              "These were tagged from what is known about the text, not from the text itself, which is not yet in the repo.",
              "", "| Unit | Tradition | Tags |", "|---|---|---|"]
    names = {t["id"]: t["name"] for t in taxonomy["traditions"]}
    for u in units:
        if not u.get("original"):
            lines.append(f"| {u['title']} | {names.get(u['tradition'], u['tradition'])} | {len(u['tags'])} |")

    leads = [p for p in (ROOT / "leads").glob("*.md") if p.name != "README.md"]
    human = [p for p in leads if "\norigin: human\n" in p.read_text(encoding="utf-8")]
    lines += ["", "## Leads", "",
              f"- {len(leads)} leads in total; {len(human)} written by hand (the benchmark set) and "
              f"{len(leads) - len(human)} by the pipeline.",
              "- The hand-written benchmark leads were drafted from secondary knowledge. Only their Quran and "
              "Hebrew passages show original text.", "",
              "## Traditions with no original text in the repo yet", ""]
    have = {"islam", "judaism"}
    for t in taxonomy["traditions"]:
        if t["id"] not in have:
            lines.append(f"- {t['name']}")
    lines += ["", "Judaism counts only the Hebrew Bible. Rabbinic literature, the Targums and the Second "
              "Temple texts are not in the repo yet."]
    out = ROOT / "results" / "COVERAGE.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines[8:12]))
    print("wrote results/COVERAGE.md")


if __name__ == "__main__":
    main()
