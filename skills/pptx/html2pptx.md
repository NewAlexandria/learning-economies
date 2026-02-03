# HTML to PowerPoint (html2pptx) — Reference

Full guide: [anthropics/skills/pptx/html2pptx.md](https://github.com/anthropics/skills/blob/main/skills/pptx/html2pptx.md).

## Slide dimensions (HTML body)

- **16:9:** `width: 720pt; height: 405pt`
- **4:3:** `width: 720pt; height: 540pt`

## Critical text rules

- **All text** must be inside `<p>`, `<h1>`–`<h6>`, `<ul>`/`<ol>`, or `<span>`. Text in `<div>` without a text tag is ignored.
- **Never** use manual bullet symbols (•, -, *); use `<ul><li>` or `<ol><li>`.
- **Fonts:** Web-safe only (Arial, Helvetica, Times New Roman, Georgia, Courier New, Verdana, Tahoma, Trebuchet MS, Impact).

## Supported elements

- Text: `<p>`, `<h1>`–`<h6>`, `<ul>`/`<ol>`, `<li>`, `<span>`, `<b>`, `<i>`, `<u>`
- `<div>` with bg/border → shape
- `<img>` for images
- `class="placeholder"` on a div → returns `{ id, x, y, w, h }` for charts/tables

## No CSS gradients

Rasterize gradients and icons to PNG with Sharp first, then reference in HTML.

## API

```javascript
const { slide, placeholders } = await html2pptx(htmlFile, pres, options);
// placeholders = [{ id, x, y, w, h }, ...]
```

- `pres.layout = 'LAYOUT_16x9'` must match HTML dimensions.
- Use PptxGenJS to add charts/tables to `placeholders[i]`.
- **Colors in PptxGenJS:** No `#` prefix — use `"FF0000"`.

## Body styling

- `display: flex` on body to avoid margin collapse.
- Use `margin` for spacing.
