#!/bin/bash
# Example usage of pandoc filters for conditional slide hiding

# Full presentation (all slides)
pandoc tretc-2026-slides-john-zak.md \
  -t revealjs \
  -o presentation-full.html

# Short presentation (hides optional and appendix slides)
pandoc tretc-2026-slides-john-zak.md \
  -t revealjs \
  --lua-filter=hide-slides.lua \
  -o presentation-short.html

# PowerPoint version (full)
pandoc tretc-2026-slides-john-zak.md \
  -o presentation-full.pptx

# PowerPoint version (short, using Python filter)
pandoc tretc-2026-slides-john-zak.md \
  --filter=hide-slides-python.py \
  -o presentation-short.pptx

# PDF version (short)
pandoc tretc-2026-slides-john-zak.md \
  --lua-filter=hide-slides.lua \
  -o presentation-short.pdf


