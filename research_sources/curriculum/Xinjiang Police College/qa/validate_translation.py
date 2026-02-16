#!/usr/bin/env python3
"""
Validate translated output against source_blocks.jsonl.

Checks:
- ID coverage: all IDs appear exactly once in translation (across one or more files)
- Empty translation: EN lines exist and are non-empty for every ID
- Table shape: EN_ROW pipes count matches ZH row pipes count (for table_row blocks)
- Numeric token fidelity: tokens containing digits from ZH appear in EN for the same block
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


ID_RE = re.compile(r"^<!-- id: ([pt]\d{6}) type: (paragraph|table_row) -->\s*$")
EN_LINE_RE = re.compile(r"^EN:\s*(.*)\s*$")
EN_ROW_RE = re.compile(r"^EN_ROW:\s*(\|.*\|)\s*$")
ZH_LINE_RE = re.compile(r"^ZH:\s*(.*)\s*$")
ZH_ROW_RE = re.compile(r"^ZH_ROW:\s*(\|.*\|)\s*$")

# Tokens that contain digits (e.g. XJNS-2025-HW-006-2, 3700000.00, ISO27001, 财库〔2022〕19号,
# 00:00-12:00). Hyphen must be last (or escaped) inside a character class.
NUM_TOKEN_RE = re.compile(r"[A-Za-z]*\d+[A-Za-z0-9./:：%-]*")


@dataclass
class SourceBlock:
    bid: str
    btype: str
    text_zh: str


def load_source_blocks(jsonl_path: Path) -> list[SourceBlock]:
    blocks: list[SourceBlock] = []
    for line in jsonl_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        obj = json.loads(line)
        blocks.append(SourceBlock(bid=obj["id"], btype=obj["type"], text_zh=obj["text_zh"]))
    return blocks


def parse_translation_files(paths: list[Path]) -> dict[str, dict[str, str]]:
    """
    Return mapping id -> { 'type': ..., 'zh': ..., 'en': ... }.
    Assumes bilingual format:
      <!-- id: ... type: ... -->
      ZH: ...
      (optional multiple ZH lines)
      EN: ...
      (optional multiple EN lines)
    For table_row blocks:
      ZH_ROW: | ... |
      EN_ROW: | ... |
    """
    out: dict[str, dict[str, str]] = {}
    seen: Counter[str] = Counter()

    for path in paths:
        lines = path.read_text(encoding="utf-8").splitlines()
        i = 0
        while i < len(lines):
            m = ID_RE.match(lines[i].strip())
            if not m:
                i += 1
                continue
            bid, btype = m.group(1), m.group(2)
            seen[bid] += 1
            i += 1
            zh_parts: list[str] = []
            en_parts: list[str] = []
            zh_row = ""
            en_row = ""

            # Consume until next id or EOF
            while i < len(lines) and not ID_RE.match(lines[i].strip()):
                line = lines[i]
                mzh = ZH_LINE_RE.match(line)
                men = EN_LINE_RE.match(line)
                mzhrow = ZH_ROW_RE.match(line)
                menrow = EN_ROW_RE.match(line)
                if mzh:
                    zh_parts.append(mzh.group(1))
                elif men:
                    en_parts.append(men.group(1))
                elif mzhrow:
                    zh_row = mzhrow.group(1).strip()
                elif menrow:
                    en_row = menrow.group(1).strip()
                i += 1

            if btype == "table_row":
                zh_text = zh_row or "\n".join(zh_parts).strip()
                en_text = en_row or "\n".join(en_parts).strip()
            else:
                zh_text = "\n".join(zh_parts).strip()
                en_text = "\n".join(en_parts).strip()

            out[bid] = {"type": btype, "zh": zh_text, "en": en_text}

    # Attach counts for external check if needed
    out["__id_counts__"] = {k: str(v) for k, v in seen.items()}  # type: ignore[assignment]
    return out


def count_pipes(row: str) -> int:
    return row.count("|")


def numeric_tokens(text: str) -> set[str]:
    toks = []
    for t in NUM_TOKEN_RE.findall(text):
        if not any(ch.isdigit() for ch in t):
            continue
        # Ignore single-digit tokens (e.g. month numbers in dates like 7月) which may be
        # rendered as words in English ("July") without loss of fidelity.
        if re.fullmatch(r"\d", t):
            continue
        toks.append(t)
    return set(toks)


def normalize_for_numeric_check(s: str) -> str:
    # normalize common dash variants and fullwidth punctuation
    return (
        s.replace("–", "-")
        .replace("—", "-")
        .replace("－", "-")
        .replace("：", ":")
        .replace("％", "%")
    )


def validate(source: list[SourceBlock], trans: dict[str, dict[str, str]]) -> list[str]:
    errors: list[str] = []

    id_counts = trans.get("__id_counts__", {})  # type: ignore[assignment]
    # Remove sentinel
    trans = {k: v for k, v in trans.items() if k != "__id_counts__"}

    source_ids = [b.bid for b in source]
    trans_ids = list(trans.keys())

    # Coverage
    missing = [bid for bid in source_ids if bid not in trans]
    extra = [bid for bid in trans_ids if bid not in set(source_ids)]
    duplicates = [bid for bid, c in id_counts.items() if int(c) != 1]
    if missing:
        errors.append(f"Missing IDs: {len(missing)} (e.g. {missing[:10]})")
    if extra:
        errors.append(f"Extra IDs not in source: {len(extra)} (e.g. {extra[:10]})")
    if duplicates:
        errors.append(f"Duplicate/non-unique IDs: {len(duplicates)} (e.g. {duplicates[:10]})")

    # Per-block checks
    for b in source:
        t = trans.get(b.bid)
        if not t:
            continue
        en = (t.get("en") or "").strip()
        if not en:
            errors.append(f"Empty EN translation for {b.bid}")
            continue

        if b.btype == "table_row":
            zh_row = t.get("zh", "")
            en_row = t.get("en", "")
            if count_pipes(zh_row) != count_pipes(en_row):
                errors.append(
                    f"Pipe-count mismatch for {b.bid}: zh={count_pipes(zh_row)} en={count_pipes(en_row)}"
                )

        # Numeric tokens fidelity
        zh_tokens = numeric_tokens(b.text_zh)
        if zh_tokens:
            en_norm = normalize_for_numeric_check(en)
            missing_tokens = [
                tok for tok in sorted(zh_tokens) if normalize_for_numeric_check(tok) not in en_norm
            ]
            if missing_tokens:
                errors.append(f"Numeric token(s) missing in {b.bid}: {missing_tokens[:8]}")

    return errors


def main(argv: list[str]) -> int:
    if len(argv) < 3:
        print(
            "Usage: validate_translation.py <source_blocks.jsonl> <translated_file_or_dir> [report.md]",
            file=sys.stderr,
        )
        return 2
    src_path = Path(argv[1]).expanduser().resolve()
    translated_path = Path(argv[2]).expanduser().resolve()
    report_path = Path(argv[3]).expanduser().resolve() if len(argv) >= 4 else src_path.parent / "translation_validation_report.md"

    source = load_source_blocks(src_path)

    files: list[Path] = []
    if translated_path.is_dir():
        files = sorted(translated_path.glob("*.md"))
    else:
        files = [translated_path]

    trans = parse_translation_files(files)
    errors = validate(source, trans)

    with report_path.open("w", encoding="utf-8") as f:
        f.write("# Translation validation report\n\n")
        f.write(f"- Source blocks: {len(source)}\n")
        f.write(f"- Translation files checked: {len(files)}\n\n")
        if errors:
            f.write(f"## FAIL ({len(errors)} issues)\n\n")
            for e in errors[:500]:
                f.write(f"- {e}\n")
            if len(errors) > 500:
                f.write(f"\n... truncated, {len(errors)-500} more ...\n")
        else:
            f.write("## PASS\n\nAll checks passed.\n")

    print(f"Wrote report: {report_path}")
    if errors:
        print(f"FAIL: {len(errors)} issues")
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

