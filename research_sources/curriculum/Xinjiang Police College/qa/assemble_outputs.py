#!/usr/bin/env python3
"""
Assemble translated chunk files into:
- xinjiang-police-college-cyberspace-security-lab-bilingual.md
- xinjiang-police-college-cyberspace-security-lab-en.md (English-only, still ID-tagged)

Input: a directory of bilingual chunk files (*.md) that follow validate_translation.py format.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ID_RE = re.compile(r"^<!-- id: ([pt]\d{6}) type: (paragraph|table_row) -->\s*$")
ZH_RE = re.compile(r"^ZH:\s*(.*)\s*$")
EN_RE = re.compile(r"^EN:\s*(.*)\s*$")
ZH_ROW_RE = re.compile(r"^ZH_ROW:\s*(\|.*\|)\s*$")
EN_ROW_RE = re.compile(r"^EN_ROW:\s*(\|.*\|)\s*$")


def english_only_from_bilingual(text: str) -> str:
    """
    Keep ID lines, keep EN/EN_ROW lines converted to plain text/table row,
    drop ZH lines entirely.
    """
    out_lines: list[str] = []
    lines = text.splitlines()
    for line in lines:
        if ID_RE.match(line.strip()):
            out_lines.append(line)
            continue
        m = EN_RE.match(line)
        if m:
            out_lines.append(m.group(1))
            continue
        m = EN_ROW_RE.match(line)
        if m:
            out_lines.append(m.group(1))
            continue
        # keep blank lines for readability
        if line.strip() == "":
            out_lines.append("")
            continue
        # drop everything else (ZH, headers, etc.)
    # normalize multiple blank lines
    normalized: list[str] = []
    blank = False
    for l in out_lines:
        if l.strip() == "":
            if not blank:
                normalized.append("")
            blank = True
        else:
            normalized.append(l)
            blank = False
    return "\n".join(normalized).strip() + "\n"


def main(argv: list[str]) -> int:
    if len(argv) < 3:
        print("Usage: assemble_outputs.py <translated_chunks_dir> <out_dir>", file=sys.stderr)
        return 2
    chunks_dir = Path(argv[1]).expanduser().resolve()
    out_dir = Path(argv[2]).expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    chunk_files = sorted(chunks_dir.glob("*.md"))
    if not chunk_files:
        print(f"No chunk files found in {chunks_dir}", file=sys.stderr)
        return 1

    bilingual_out = out_dir / "xinjiang-police-college-cyberspace-security-lab-bilingual.md"
    english_out = out_dir / "xinjiang-police-college-cyberspace-security-lab-en.md"

    bilingual_parts: list[str] = []
    for p in chunk_files:
        bilingual_parts.append(p.read_text(encoding="utf-8").strip())

    bilingual_text = "\n\n".join(bilingual_parts).strip() + "\n"
    bilingual_out.write_text(bilingual_text, encoding="utf-8")

    english_text = english_only_from_bilingual(bilingual_text)
    english_out.write_text(english_text, encoding="utf-8")

    print(f"Wrote:\n- {bilingual_out}\n- {english_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

