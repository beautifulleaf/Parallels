"""Validate leads and regenerate the artifact.

Usage: python3 tools/build.py [--check]

Reads data/traditions.yaml and leads/*.md, validates every lead against the
format in leads/README.md, then writes site/leads.json and site/index.html
(site/template.html with the data embedded). --check validates only.
"""
import json
import pathlib
import re
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
LEADS_DIR = ROOT / "leads"
SITE = ROOT / "site"

STATUSES = {"new", "investigating", "promising", "rejected"}
RELATIONS = {"internal", "inheritance", "transmission", "convergence", "response"}
STANDINGS = {"established", "proposed", "contested", "fringe"}
LAYERS = {"lexical", "motif", "concept"}
ORIGINS = {"human", "pipeline"}
REQUIRED = ["id", "title", "summary", "status", "relations", "standing",
            "traditions", "layers", "origin", "added"]
SLUG = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def parse_lead(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        raise ValueError("missing YAML front matter")
    meta = yaml.safe_load(m.group(1)) or {}
    meta["notes"] = m.group(2).strip()
    return meta


def validate(lead, path, tradition_ids):
    errors = []
    for key in REQUIRED:
        if key not in lead:
            errors.append(f"missing '{key}'")
    if errors:
        return errors
    if lead["id"] != path.stem:
        errors.append(f"id '{lead['id']}' does not match filename")
    if not SLUG.match(lead["id"]):
        errors.append("id must be kebab-case")
    if lead["status"] not in STATUSES:
        errors.append(f"status must be one of {sorted(STATUSES)}")
    if lead["standing"] not in STANDINGS:
        errors.append(f"standing must be one of {sorted(STANDINGS)}")
    if lead["origin"] not in ORIGINS:
        errors.append(f"origin must be one of {sorted(ORIGINS)}")
    for key, allowed in (("relations", RELATIONS), ("layers", LAYERS)):
        values = lead[key]
        if not isinstance(values, list) or not values:
            errors.append(f"'{key}' must be a non-empty list")
        elif set(values) - allowed:
            errors.append(f"unknown {key}: {sorted(set(values) - allowed)}")
    traditions = lead["traditions"]
    min_traditions = 1 if lead["relations"] == ["internal"] else 2
    if not isinstance(traditions, list) or len(traditions) < min_traditions:
        errors.append(f"'traditions' needs at least {min_traditions} id(s)")
    else:
        unknown = [t for t in traditions if t not in tradition_ids]
        if unknown:
            errors.append(f"unknown traditions: {unknown}")
    for p in lead.get("passages") or []:
        if p.get("tradition") not in tradition_ids:
            errors.append(f"passage '{p.get('ref')}' has unknown tradition")
    for key in ("motifs", "concepts"):
        bad = [v for v in lead.get(key) or [] if not SLUG.match(str(v))]
        if bad:
            errors.append(f"{key} must be kebab-case: {bad}")
    return errors


def main():
    check_only = "--check" in sys.argv
    taxonomy = yaml.safe_load((ROOT / "data" / "traditions.yaml").read_text(encoding="utf-8"))
    tradition_ids = {t["id"] for t in taxonomy["traditions"]}

    leads, failures = [], 0
    for path in sorted(LEADS_DIR.glob("*.md")):
        if path.name == "README.md":
            continue
        try:
            lead = parse_lead(path)
            errors = validate(lead, path, tradition_ids)
        except (ValueError, yaml.YAMLError) as exc:
            errors = [str(exc)]
        if errors:
            failures += 1
            for e in errors:
                print(f"{path.relative_to(ROOT)}: {e}", file=sys.stderr)
            continue
        lead["added"] = str(lead["added"])
        leads.append(lead)

    if failures:
        print(f"{failures} invalid lead(s)", file=sys.stderr)
        sys.exit(1)
    print(f"{len(leads)} leads valid")
    if check_only:
        return

    payload = {"groups": taxonomy["groups"], "traditions": taxonomy["traditions"], "leads": leads}
    (SITE / "leads.json").write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
    embedded = json.dumps(payload, ensure_ascii=False).replace("<", "\\u003c")
    template = (SITE / "template.html").read_text(encoding="utf-8")
    if "__DATA__" not in template:
        sys.exit("site/template.html is missing the __DATA__ placeholder")
    (SITE / "index.html").write_text(template.replace("__DATA__", embedded, 1), encoding="utf-8")
    print("wrote site/leads.json and site/index.html")


if __name__ == "__main__":
    main()
