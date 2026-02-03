# CHI 2026 Workshop Submission

**Workshop**: Tools for Thought with Generative AI 2026
**Conference**: CHI 2026, Barcelona, April 2026
**Deadline**: February 12, 2026 AoE

## Submission Files

| File | Description | Status |
|------|-------------|--------|
| [chi-2026-paper.md](./chi-2026-paper.md) | Workshop paper source (revised per suitability plan) | Ready |
| [chi-2026-paper.tex](./chi-2026-paper.tex) | ACM sigconf LaTeX (4 pages, CCS concepts) | Ready |
| [chi-2026-slides.md](./chi-2026-slides.md) | Workshop pitch / presentation slides (aligned to paper) | Ready |
| [build/](./build/) | **Slide outputs:** PDF and PPTX go here (run `./export-slides.sh` or `node build-pptx.js` from repo root). Paper LaTeX aux/out can be moved here to unclutter. | Generated |
| [build/chi-2026-slides.pdf](./build/chi-2026-slides.pdf) | PDF from pandoc/Beamer (`./export-slides.sh pdf`) | In build/ |
| [build/chi-2026-slides.pptx](./build/chi-2026-slides.pptx) | PPTX from pandoc (`./export-slides.sh pptx`) | In build/ |
| [build/chi-2026-slides-skill.pptx](./build/chi-2026-slides-skill.pptx) | PPTX via Anthropic pptx skill; from repo root: `node CHI-2026/build-pptx.js` | In build/ |
| [miro-board-content.md](./miro-board-content.md) | Content for the workshop Miro mini-poster template | Reference |
| [miro-board-slides.md](./miro-board-slides.md) | Miro content as slides (same format as main deck); export with `./export-slides.sh pdf miro` or `./export-slides.sh pptx miro` | Source |
| [build/miro-board-slides.pdf](./build/miro-board-slides.pdf), [build/miro-board-slides.pptx](./build/miro-board-slides.pptx) | Miro slides exported to PDF/PPTX | In build/ |
| [pptx-slides/](./pptx-slides/) | HTML source for the skill-built deck (one file per slide). Edit these and re-run build-pptx.js to regenerate the skill PPTX. | Source |
| [build-pptx.js](./build-pptx.js) | Build script for html2pptx (uses `skills/pptx/`) | Ready |
| [export-slides.sh](./export-slides.sh) | Export slides to PDF (Beamer) or PPTX (pandoc) | Ready |
| [abstract.md](./abstract.md) | Standalone abstract and keywords (for forms) | Ready |
| [proposal-summary.md](./proposal-summary.md) | Short proposal text (for submission forms) | Ready |
| [SUBMISSION.md](./SUBMISSION.md) | Submission checklist and instructions | Ready |
| [miro-board-content.md](./miro-board-content.md) | Content for Miro mini-poster template | Updated |
| [personal-statement.md](./personal-statement.md) | Author personal statement (150 words max) | Template |
| [conference-overview.md](./conference-overview.md) | Workshop call for papers | Reference |

## Submission Requirements

### Paper

- Up to 4 pages (excluding references)
- ACM 2-column format (`\documentclass[sigconf,screen]{acmart}`)
- Upload PDF + source files (LaTeX or Word)

### Miro Board Mini-Poster

1. Create Miro account
2. Duplicate template from workshop website
3. Fill using content from `miro-board-content.md`
4. Export as PDF + sharing URL

### Personal Statement

- Max 150 words per attending author
- Confirm number of attendees (1-2 max)

## Workshop Theme Alignment

**Primary**: TfT Outcomes: Definition and Measurement

- Five Learning Economies as measurable cognitive dimensions
- Operationalizable metrics for each economy

**Secondary**: TfT Strategies: Design and Usage

- Economy-specific design patterns
- Reflective advisor loop (cybernetic feedback framing)
- Scope across learning levels (early education through doctoral/vocational); reframing of gifted education as multi-economy fluency
- Link to LLM architectural principles (Section 2.3)

## Slides export (PDF / PPTX) — outputs in `build/`

All slide builds write to **`build/`** so the main folder stays uncluttered (no .aux, .out, etc.). Copy the file you want from `build/` into the main folder if needed (e.g. for submission).

**Slide sets:** The same script handles multiple decks. Pass a **set** as the second argument: `chi` (default, main deck) or `miro` (Miro board content).

- **Main deck (chi):**  
  `./export-slides.sh pdf` → `build/chi-2026-slides.pdf`  
  `./export-slides.sh pptx` → `build/chi-2026-slides.pptx`
- **Miro board as slides (miro):**  
  `./export-slides.sh pdf miro` → `build/miro-board-slides.pdf`  
  `./export-slides.sh pptx miro` → `build/miro-board-slides.pptx`  
  Source: `miro-board-slides.md` (derived from `miro-board-content.md`).
- **PowerPoint (Anthropic pptx skill):** From repo root run `npm install` (once), then `node CHI-2026/build-pptx.js`. Writes `build/chi-2026-slides-skill.pptx` from the HTML in `pptx-slides/`. Uses the [Anthropic pptx skill](https://github.com/anthropics/skills/tree/main/skills/pptx) (html2pptx).
- **`pptx-slides/`** holds the HTML source for the skill-built deck. Edit those HTML files and re-run the build script to regenerate the skill PPTX.

## Submission Checklist

See [SUBMISSION.md](./SUBMISSION.md) for a step-by-step checklist (paper PDF + source, Miro URL + PDF, personal statement, abstract), author placeholders to replace, and key dates.

## Key Dates

- **Submission deadline**: Thursday, February 12, 2026 AoE
- **Notification**: Wednesday, February 25, 2026
- **Camera-ready**: Thursday, March 26, 2026

## Resources

- Workshop website: <https://ai-tools-for-thought.github.io/workshop/>
- GuildCon 2025 presentation: <https://www.youtube.com/watch?v=kIBo1JevzuE>
