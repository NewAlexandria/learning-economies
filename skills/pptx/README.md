# PPTX Skill (Anthropic)

This folder contains the **Anthropic pptx skill** for presentation creation, editing, and analysis. It is copied from [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/pptx) for use in this repo.

## What it provides

- **SKILL.md** — Instructions for creating/editing .pptx files (workflows, design principles, dependencies).
- **html2pptx.md** — Guide for converting HTML slides to PowerPoint using the `html2pptx` library.
- **ooxml.md** — Office Open XML reference for editing existing .pptx files.
- **scripts/** — `html2pptx.js` (Node), `thumbnail.py`, `inventory.py`, `replace.py`, `rearrange.py`.
- **ooxml/scripts/** — `unpack.py`, `pack.py`, `validate.py` for raw OOXML editing.

## Using the skill in this repo

1. **Creating a new presentation from HTML (no template)**  
   Read `html2pptx.md` fully. Create one HTML file per slide (body dimensions 720pt × 405pt for 16:9). All text must be in `<p>`, `<h1>`–`<h6>`, `<ul>`/`<ol>`, or `<span>`. Run a Node script that uses `scripts/html2pptx.js` and PptxGenJS to convert HTML to .pptx.

2. **Editing an existing .pptx**  
   Read `ooxml.md`. Unpack with `python ooxml/scripts/unpack.py`, edit XML, validate with `python ooxml/scripts/validate.py`, pack with `python ooxml/scripts/pack.py`.

3. **Using a template**  
   Follow the "Creating a new PowerPoint presentation using a template" workflow in SKILL.md (extract text, thumbnail grid, template inventory, outline, rearrange, inventory, replace).

## Dependencies

- **Node:** `pptxgenjs`, `playwright`, `sharp` (for html2pptx).
- **Python:** `markitdown[pptx]`, `defusedxml` (for extraction and OOXML scripts).
- **Optional:** LibreOffice (PDF conversion), poppler-utils (pdftoppm).

## Source and license

- **Source:** https://github.com/anthropics/skills/tree/main/skills/pptx  
- **License:** See [LICENSE.txt](https://github.com/anthropics/skills/blob/main/skills/pptx/LICENSE.txt) in the Anthropic repo. This copy is for local use with Cursor/agents; see that repo for full terms.

## Reference

- [Simon Willison — Claude skills](https://simonwillison.net/2025/Oct/10/claude-skills/)
