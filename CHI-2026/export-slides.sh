#!/usr/bin/env bash
# Export CHI 2026 workshop slides to PDF and optionally PPTX.
# Outputs go to build/ so the main folder stays uncluttered (no .aux, .out, etc.).
# Supports multiple slide sets: main deck (default) and Miro board content.
# Requires: pandoc, pdflatex (for PDF).
# Usage: ./export-slides.sh [pdf|pptx|all] [set]
#   set: chi (default) | miro

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"
BUILD_DIR="${SCRIPT_DIR}/build"
mkdir -p "$BUILD_DIR"

# Slide set: chi = main deck, miro = Miro board content
SLIDE_SET="${2:-chi}"
case "$SLIDE_SET" in
  chi)
    INPUT="chi-2026-slides.md"
    BASE="chi-2026-slides"
    ;;
  miro)
    INPUT="miro-board-slides.md"
    BASE="miro-board-slides"
    ;;
  *)
    echo "Unknown set: $SLIDE_SET (use chi or miro)"
    exit 1
    ;;
esac

OUTPUT_PDF="$BUILD_DIR/${BASE}.pdf"
OUTPUT_PPTX="$BUILD_DIR/${BASE}.pptx"

export_pdf() {
  echo "Exporting to PDF: $OUTPUT_PDF (set=$SLIDE_SET)"
  (cd "$BUILD_DIR" && pandoc "../$INPUT" -t beamer -o "${BASE}.pdf")
  echo "Done. Open with: open $OUTPUT_PDF"
}

export_pptx() {
  echo "Exporting to PowerPoint: $OUTPUT_PPTX (set=$SLIDE_SET)"
  pandoc "$INPUT" -o "$OUTPUT_PPTX"
  echo "Done. Open and optionally Save As PDF from PowerPoint."
}

case "${1:-all}" in
  pdf)  export_pdf ;;
  pptx) export_pptx ;;
  all)
    export_pdf
    export_pptx
    ;;
  *)
    echo "Usage: $0 [pdf|pptx|all] [set]"
    echo "  pdf  - export to PDF only (Beamer)"
    echo "  pptx - export to PowerPoint only"
    echo "  all  - export to both (default)"
    echo "  set  - chi (main deck, default) | miro (Miro board content)"
    exit 1
    ;;
esac
