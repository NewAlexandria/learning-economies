# CHI 2026 Workshop — Submission Checklist

**Workshop:** Tools for Thought with Generative AI 2026  
**Deadline:** Thursday, February 12, 2026 AoE  
**Submission form:** [Workshop submission](https://forms.fillout.com/t/u5Dx2rkszPus)

---

## Required Items

### 1. Workshop paper
- [ ] **PDF:** `chi-2026-paper.pdf` (from `chi-2026-paper.tex`; build in `CHI-2026/` or copy from `build/` if you build with `-output-directory=build`)
- [ ] **Source:** `chi-2026-paper.tex` (LaTeX) or Word equivalent
- **Format:** ACM sigconf, up to 4 pages excluding references
- **Build:** Run `pdflatex chi-2026-paper.tex` twice in `CHI-2026/`

### 2. Miro mini-poster
- [ ] Duplicate the [workshop Miro template](https://miro.com/app/board/uXjVGVr33NA=/?share_link_id=778756096429) (log in required)
- [ ] Fill using content from `miro-board-content.md`
- [ ] Create sharing URL and export as PDF
- [ ] Submit both URL and PDF via the submission form

### 3. Personal statement
- [ ] Use `personal-statement.md` (max 150 words per attending author)
- [ ] Confirm number of attendees (min 1, max 2)

### 4. Abstract (if form asks)
- [ ] Use text from `abstract.md` (paste-ready paragraph and keywords)

---

## Before Submitting

- [ ] Replace placeholder author/affiliation/email in `chi-2026-paper.tex` (search for "Anonymized", "Institution", "email@example.com")
- [ ] Confirm references and citations in the paper
- [ ] Verify PDF is 4 pages or fewer (excluding references)

---

## File Reference

| Item           | Source file(s)                    | Output / action                    |
|----------------|-----------------------------------|------------------------------------|
| Paper          | `chi-2026-paper.tex`, `.md`       | PDF + .tex upload                   |
| Abstract       | `abstract.md`                     | Paste into form if required        |
| Proposal text  | `proposal-summary.md`             | Use if form has "proposal" field   |
| Miro content   | `miro-board-content.md`           | Fill Miro template → URL + PDF     |
| Personal stmt  | `personal-statement.md`           | Paste into form                    |
| Slides         | `chi-2026-slides.md`              | For workshop pitch / presentation  |
| Slides PDF     | Run `./export-slides.sh pdf` in CHI-2026 | Produces `build/chi-2026-slides.pdf`  |
| Slides PPTX    | Run `./export-slides.sh pptx` or `node CHI-2026/build-pptx.js` from repo root | Produces `build/chi-2026-slides.pptx` or `build/chi-2026-slides-skill.pptx`  |

---

## Key Dates

- **Submission deadline:** Thursday, February 12, 2026 AoE  
- **Notification:** Wednesday, February 25, 2026  
- **Camera-ready:** Thursday, March 26, 2026 AoE  
