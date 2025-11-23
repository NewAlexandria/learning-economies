# Slide Optimization Guide

## 1. Keep Title and Columns Together
- **No blank line** between `# Slide Title` and `::::: columns`.
- Place any slide separator (`---`) **after** the closing `:::::`.

## 2. Use Two‑Column Layout Effectively
- Start with `::::: columns` then `::: column` blocks.
- Close each column with `:::` and the layout with `:::::`.
- Keep content concise – short phrases, not full sentences.
- See the `slide-layout-examples.md` for other layoutexamples.

## 3. Move Supporting Details to Notes
- Place **Metrics** or extra info in `::: notes` blocks **outside** the columns.
- Example:
  ```markdown
  # The Breadth Economy: Multi‑Subject / Multi‑Degree Mastery
  ::::: columns
  ::: column
  **Current State:**
  - Broad exposure required (high school)
  - Single‑field depth emphasis (undergrad)
  :::
  ::: column
  **AI‑Accelerated Future:**
  - Double/triple majors → 4‑5 simultaneous
  - LLM routing between domains
  :::
  :::::

  ::: notes
  **Metrics:**
  - Parallel intellectual pipelines sustained
  - Diversity index of fields mastered
  - Time to proficiency across subjects
  :::
  ```
- Use notes for optional or detailed data that the presenter can reference.

## 4. Hide Provisional Slides
- Wrap slides you may skip in `::: {.optional}` to hide them during presentation.

## 5. Consistent Header Formatting
- Merge subtitle into the main `#` header (e.g., `# Breadth Economy: Multi‑Subject / Multi‑Degree Mastery`).
- Avoid separate `##` or bold subtitle lines.

## 6. Minimalist Bullet Points
- Use **bold** for key terms, plain text for supporting phrases.
- Remove filler words (prepositions, articles) where the speaker can fill the gap.

## 7. Technical Metaphor Updates
- Prefer **LLM routing** and **temperature** metaphors over CPU analogies.
- Keep metaphors short and directly tied to AI concepts.

## 8. Consistent Slide Separation
- Use a single `---` line **only** between distinct slides, after the entire slide content.

## 9. Review Rendered Output
- Run `pandoc -t revealjs` locally to verify title + columns stay on one slide.
- Adjust blank lines or separators if the slide splits.

## 10. Checklist Before Export
- [ ] No blank line between title and column block.
- [ ] All metrics moved to `::: notes`.
- [ ] Optional slides wrapped in `{: .optional}`.
- [ ] Bullet points are concise phrases.
- [ ] Metaphors updated to LLM terminology.
- [ ] Slide separators only after closing `:::::`.

---
*This guide captures the best practices discovered while refining the slide decks in this repository.*
