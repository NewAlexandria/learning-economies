# PPTX Skill — Quick Reference

Full skill: [anthropics/skills/pptx](https://github.com/anthropics/skills/tree/main/skills/pptx). Read **html2pptx.md** and **ooxml.md** in this folder for full syntax before creating or editing presentations.

## Creating a new presentation (no template) — html2pptx

1. **Design:** Choose subject-appropriate colors and fonts. Use web-safe fonts only: Arial, Helvetica, Times New Roman, Georgia, Courier New, Verdana, Tahoma, Trebuchet MS, Impact.
2. **HTML slides:** One HTML file per slide. Body dimensions: `width: 720pt; height: 405pt` (16:9). **All text** must be inside `<p>`, `<h1>`–`<h6>`, `<ul>`/`<ol>`, or `<span>` — text in bare `<div>` is ignored.
3. **No manual bullets** — use `<ul><li>` or `<ol><li>`; never type •, -, *.
4. **No CSS gradients** in HTML — rasterize to PNG first with Sharp, then reference in HTML.
5. **Node script:** Use `html2pptx(htmlFile, pptx)` from `scripts/html2pptx.js`. Set `pptx.layout = 'LAYOUT_16x9'`. Add charts/tables to placeholders with PptxGenJS. Save with `pptx.writeFile()`.
6. **Validation:** Run `python scripts/thumbnail.py output.pptx` and check for text cutoff, overlap, contrast.

## Editing an existing .pptx (OOXML)

1. Unpack: `python ooxml/scripts/unpack.py input.pptx`
2. Edit XML (e.g. `ppt/slides/slideN.xml`).
3. Validate: `python ooxml/scripts/validate.py --original input.pptx`
4. Pack: `python ooxml/scripts/pack.py`

## Key paths (unpacked)

- `ppt/presentation.xml` — slide order
- `ppt/slides/slide{N}.xml` — slide content
- `ppt/theme/theme1.xml` — colors, fonts
- `ppt/slideLayouts/`, `ppt/slideMasters/` — layouts

## PptxGenJS colors

**Never use `#` prefix** — use `"FF0000"` not `"#FF0000"` (causes corruption).

## Script locations

- From repo root: `skills/pptx/scripts/html2pptx.js`, `skills/pptx/scripts/thumbnail.py`, etc.
- OOXML: `skills/pptx/ooxml/scripts/unpack.py`, `pack.py`, `validate.py`
