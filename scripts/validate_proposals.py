#!/usr/bin/env python3

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
PROPOSALS_DIR = ROOT / "proposals"
DRAFTS_DIR = ROOT / "drafts"

PROPOSAL_FILE_RE = re.compile(r"^mip-\d{4}-[a-z0-9-]+\.md$")
DRAFT_FILE_RE = re.compile(r"^mip-draft-[a-z0-9-]+\.md$")

ALLOWED_STATUS = {
    "draft",
    "discussion",
    "candidate",
    "accepted",
    "active",
    "rejected",
    "withdrawn",
    "superseded",
}

ALLOWED_TYPE = {
    "standard",
    "operational",
    "informational",
    "process",
}

ALLOWED_SCOPE = {
    "national",
    "regional",
    "experimental",
    "recommendation",
}

REQUIRED_FIELDS = {
    "status",
    "type",
    "scope",
    "author",
    "created",
    "discussion",
}


def list_markdown_files(folder: Path):
    if not folder.exists():
        return []
    return sorted([p for p in folder.glob("*.md") if p.name.lower() != "readme.md"])


def parse_metadata(lines):
    metadata = {}
    started = False

    for raw in lines:
        line = raw.rstrip("\n")
        if line.startswith("# "):
            started = True
            continue
        if not started:
            continue
        if line.startswith("## "):
            break
        if not line.strip():
            continue
        m = re.match(r"^([A-Za-z][A-Za-z0-9() \-]*):\s*(.*)$", line)
        if not m:
            continue
        key = m.group(1).strip().lower()
        value = m.group(2).strip()
        metadata[key] = value
    return metadata


def extract_section(lines, title):
    section_lines = []
    in_section = False
    heading = f"## {title}".lower()

    for raw in lines:
        line = raw.rstrip("\n")
        if line.lower().startswith("## "):
            if line.lower() == heading:
                in_section = True
                continue
            if in_section:
                break
        if in_section:
            section_lines.append(line)

    return "\n".join(section_lines).strip()


def validate_file(path: Path, is_draft: bool):
    errors = []
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(True)
    metadata = parse_metadata(lines)

    expected_pattern = DRAFT_FILE_RE if is_draft else PROPOSAL_FILE_RE
    if not expected_pattern.match(path.name):
        errors.append(
            f"{path}: invalid filename. Expected pattern "
            f"{expected_pattern.pattern}"
        )

    missing = [k for k in REQUIRED_FIELDS if k not in metadata]
    if missing:
        errors.append(f"{path}: missing required fields: {', '.join(sorted(missing))}")

    status = metadata.get("status", "").lower()
    ptype = metadata.get("type", "").lower()
    scope = metadata.get("scope", "").lower()

    if status and status not in ALLOWED_STATUS:
        errors.append(f"{path}: invalid Status '{metadata.get('status')}'")
    if ptype and ptype not in ALLOWED_TYPE:
        errors.append(f"{path}: invalid Type '{metadata.get('type')}'")
    if scope and scope not in ALLOWED_SCOPE:
        errors.append(f"{path}: invalid Scope '{metadata.get('scope')}'")

    if scope == "experimental":
        review_date = metadata.get("review date", "").strip()
        expiry_date = metadata.get("expiry date", "").strip()
        if not review_date and not expiry_date:
            errors.append(
                f"{path}: experimental proposal requires Review Date or Expiry Date"
            )

    if status in {"accepted", "active", "superseded"}:
        decision = extract_section(lines, "Decision")
        if not decision:
            errors.append(
                f"{path}: accepted/active/superseded proposals require Decision section"
            )

    return errors


def main():
    files = []
    files.extend([(p, False) for p in list_markdown_files(PROPOSALS_DIR)])
    files.extend([(p, True) for p in list_markdown_files(DRAFTS_DIR)])

    errors = []
    for path, is_draft in files:
        errors.extend(validate_file(path, is_draft))

    if errors:
        print("Proposal validation failed:")
        for err in errors:
            print(f"- {err}")
        return 1

    print("Proposal validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

