#!/usr/bin/env python3
"""Split extracted text into chunks of ~CHUNK_SIZE chars at paragraph boundaries."""

import sys
from pathlib import Path

CHUNK_SIZE = 10_000  # target size per chunk
MIN_PARAS = 2  # keep at least this many paragraphs per chunk

def main():
    if len(sys.argv) != 2:
        print("Usage: python split_for_translation.py <extracted.txt>", file=sys.stderr)
        sys.exit(1)
    path = Path(sys.argv[1])
    text = path.read_text(encoding="utf-8")
    # Split into paragraphs (blank-line separated)
    paras = text.split("\n\n")
    out_dir = path.parent / "translation_chunks"
    out_dir.mkdir(exist_ok=True)
    chunk_num = 0
    current = []
    current_len = 0
    for i, p in enumerate(paras):
        p_len = len(p) + 2  # +2 for \n\n
        if current_len + p_len > CHUNK_SIZE and len(current) >= MIN_PARAS:
            chunk_num += 1
            out_file = out_dir / f"chunk_{chunk_num:02d}.txt"
            out_file.write_text("\n\n".join(current), encoding="utf-8")
            current = []
            current_len = 0
        current.append(p)
        current_len += p_len
    if current:
        chunk_num += 1
        out_file = out_dir / f"chunk_{chunk_num:02d}.txt"
        out_file.write_text("\n\n".join(current), encoding="utf-8")
    print(f"Wrote {chunk_num} chunks to {out_dir}")

if __name__ == "__main__":
    main()
