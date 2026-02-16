#!/usr/bin/env python3
"""
Build a lossless, ID-tagged block stream from the Xinjiang Police College .docx.

Outputs (in the same directory as this script, unless overridden):
- source_blocks.jsonl : one JSON object per block (paragraph or table_row)
- source_blocks.md    : Chinese-only Markdown with per-block stable IDs

Block IDs:
- Paragraph blocks: p000001, p000002, ...
- Table-row blocks: t000001, t000002, ...

Notes:
- This does NOT attempt to infer page breaks. It guarantees completeness w.r.t. the OOXML
  body order (paragraphs + tables) as extracted from word/document.xml.
"""

from __future__ import annotations

import json
import re
import sys
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Optional

import xml.etree.ElementTree as ET

WORD_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"


def ns(tag: str) -> str:
    return "{%s}%s" % (WORD_NS, tag)


def paragraph_text(p_elem: ET.Element) -> str:
    """Collect all w:t text in a paragraph, in order."""
    parts: list[str] = []
    for t in p_elem.iter(ns("t")):
        if t.text:
            parts.append(t.text)
        if t.tail and t.tail.strip():
            parts.append(t.tail)
    return "".join(parts).strip()


def is_heading(text: str) -> bool:
    """
    Heuristic heading detector to provide context; does not affect ordering.
    """
    t = re.sub(r"\s+", "", text)
    if not t:
        return False
    # Common Chinese headings in this document
    if any(k in t for k in ["部分", "章", "节", "目录", "公告", "评标", "投标人须知", "合同条款"]):
        # Avoid false positives for long sentences
        return len(t) <= 40
    if re.match(r"^第[一二三四五六七八九十0-9]+[部分章节条款].*$", t):
        return True
    return False


@dataclass(frozen=True)
class Block:
    order: int
    block_id: str
    block_type: str  # "paragraph" | "table_row"
    text_zh: str
    context: list[str]
    # table metadata (only for table_row)
    cells_zh: Optional[list[str]] = None
    cell_count: Optional[int] = None

    def to_json(self) -> dict[str, Any]:
        obj: dict[str, Any] = {
            "order": self.order,
            "id": self.block_id,
            "type": self.block_type,
            "text_zh": self.text_zh,
            "context": self.context,
        }
        if self.block_type == "table_row":
            obj["cells_zh"] = self.cells_zh or []
            obj["cell_count"] = self.cell_count or 0
        return obj


def extract_blocks_from_docx(docx_path: Path) -> list[Block]:
    with zipfile.ZipFile(docx_path, "r") as z:
        xml_bytes = z.read("word/document.xml")

    root = ET.fromstring(xml_bytes)
    body = root.find(ns("body"))
    if body is None:
        raise RuntimeError("Could not locate w:body in word/document.xml")

    blocks: list[Block] = []
    order = 0
    p_i = 0
    t_i = 0
    context_stack: list[str] = []

    def push_context_if_heading(text: str) -> None:
        nonlocal context_stack
        if is_heading(text):
            context_stack = (context_stack + [text])[-4:]

    for child in body:
        if child.tag == ns("p"):
            text = paragraph_text(child)
            if not text:
                continue
            push_context_if_heading(text)
            order += 1
            p_i += 1
            bid = f"p{p_i:06d}"
            blocks.append(
                Block(
                    order=order,
                    block_id=bid,
                    block_type="paragraph",
                    text_zh=text,
                    context=list(context_stack),
                )
            )
        elif child.tag == ns("tbl"):
            # Iterate rows in document order
            for tr in child.findall(f".//{ns('tr')}"):
                row_cells: list[str] = []
                for tc in tr.findall(f".//{ns('tc')}"):
                    cell_paras: list[str] = []
                    for p in tc.findall(f".//{ns('p')}"):
                        t = paragraph_text(p)
                        if t:
                            cell_paras.append(t)
                    row_cells.append("\n".join(cell_paras).strip())

                # Keep even empty rows if there is at least one cell
                if not row_cells:
                    continue

                order += 1
                t_i += 1
                bid = f"t{t_i:06d}"
                # Markdown row (no header inference)
                row_text = "| " + " | ".join(c.replace("\n", "<br/>") for c in row_cells) + " |"
                blocks.append(
                    Block(
                        order=order,
                        block_id=bid,
                        block_type="table_row",
                        text_zh=row_text,
                        context=list(context_stack),
                        cells_zh=row_cells,
                        cell_count=len(row_cells),
                    )
                )
        else:
            # Ignore other body children (e.g., sectPr)
            continue

    return blocks


def write_outputs(blocks: list[Block], out_dir: Path) -> tuple[Path, Path]:
    out_jsonl = out_dir / "source_blocks.jsonl"
    out_md = out_dir / "source_blocks.md"

    with out_jsonl.open("w", encoding="utf-8") as f:
        for b in blocks:
            f.write(json.dumps(b.to_json(), ensure_ascii=False) + "\n")

    with out_md.open("w", encoding="utf-8") as f:
        f.write("# Source blocks (Chinese)\n\n")
        f.write("This file is auto-generated. Each block has a stable ID.\n\n")
        for b in blocks:
            f.write(f"<!-- id: {b.block_id} type: {b.block_type} -->\n")
            # Include minimal context as HTML comment for debugging
            if b.context:
                f.write(f"<!-- context: {' > '.join(b.context)} -->\n")
            f.write(b.text_zh.strip() + "\n\n")

    return out_jsonl, out_md


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("Usage: build_source_blocks.py <input.docx> [out_dir]", file=sys.stderr)
        return 2
    docx_path = Path(argv[1]).expanduser().resolve()
    out_dir = Path(argv[2]).expanduser().resolve() if len(argv) >= 3 else Path(__file__).parent
    out_dir.mkdir(parents=True, exist_ok=True)

    blocks = extract_blocks_from_docx(docx_path)
    out_jsonl, out_md = write_outputs(blocks, out_dir)
    print(f"Wrote {len(blocks)} blocks")
    print(f"- {out_jsonl}")
    print(f"- {out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

