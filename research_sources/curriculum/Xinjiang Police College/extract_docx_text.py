#!/usr/bin/env python3
"""Extract plain text from a .docx file (word/document.xml). Preserves paragraph and table order."""

import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

WORD_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS_MAP = {"w": WORD_NS}


def ns(tag: str) -> str:
    return "{%s}%s" % (WORD_NS, tag)


def paragraph_text(p_elem) -> str:
    """Collect all w:t text in a paragraph, in order."""
    parts = []
    for t in p_elem.iter(ns("t")):
        if t.text:
            parts.append(t.text)
        # Some elements have tail (e.g. after a tab)
        if t.tail and t.tail.strip():
            parts.append(t.tail)
    return "".join(parts).strip()


def extract_body(root):
    """Extract text from document body in order: paragraphs and tables."""
    body = root.find(ns("body"))
    if body is None:
        return []

    lines = []
    for child in body:
        if child.tag == ns("p"):
            text = paragraph_text(child)
            if text:
                lines.append(text)
        elif child.tag == ns("tbl"):
            # Table: each row, then cells (paragraphs in each cell)
            for tr in child.iter(ns("tr")):
                row_cells = []
                for tc in tr.iter(ns("tc")):
                    cell_texts = []
                    for p in tc.iter(ns("p")):
                        t = paragraph_text(p)
                        if t:
                            cell_texts.append(t)
                    row_cells.append(" | ".join(cell_texts) if cell_texts else "")
                if row_cells:
                    lines.append("| " + " | ".join(row_cells) + " |")
    return lines


def extract_docx(docx_path: Path) -> str:
    with zipfile.ZipFile(docx_path, "r") as z:
        try:
            xml_bytes = z.read("word/document.xml")
        except KeyError:
            raise FileNotFoundError("word/document.xml not found in docx")

    root = ET.fromstring(xml_bytes)
    lines = extract_body(root)
    return "\n\n".join(lines)


def main():
    if len(sys.argv) != 2:
        print("Usage: python extract_docx_text.py <file.docx>", file=sys.stderr)
        sys.exit(1)
    path = Path(sys.argv[1])
    if not path.exists():
        print(f"File not found: {path}", file=sys.stderr)
        sys.exit(1)
    text = extract_docx(path)
    print(text)


if __name__ == "__main__":
    main()
