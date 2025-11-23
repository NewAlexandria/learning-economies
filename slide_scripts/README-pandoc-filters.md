# Pandoc Conditional Slide Hiding

This directory contains filters and examples for conditionally hiding slides in pandoc presentations.

## Methods

### Method 1: Using Divs with Classes (Recommended)

Wrap slides you want to conditionally hide in divs with special classes:

```markdown
---
title: My Presentation
---

# Regular Slide

This slide always shows.

::: {.optional}

# Optional Slide

This slide only shows if the filter doesn't remove it.
:::

::: {.appendix}

# Appendix Slide

This is an appendix slide.
:::

# Another Regular Slide
```

**Usage:**

```bash
# Hide slides with class "optional" and "appendix"
pandoc slides.md -t revealjs --lua-filter=hide-slides.lua -o output.html
```

### Method 2: Using YAML Metadata Variables

Add variables to your YAML header and use a filter to check them:

```markdown
---
title: My Presentation
show_appendix: false
show_detailed: true
---

# Regular Slide

::: {.appendix}

# Appendix Slide

This only shows if show_appendix is true.
:::

::: {.detailed}

# Detailed Slide

This only shows if show_detailed is true.
:::
```

### Method 3: Using Comments with Special Syntax

You can use HTML comments or special markdown syntax that filters can process:

```markdown
<!-- HIDE_START -->

# This slide will be hidden

<!-- HIDE_END -->

# This slide will show
```

## Filter Options

### Lua Filter (hide-slides.lua)

**Pros:**

- Native to pandoc (no external dependencies)
- Fast execution
- Easy to customize

**Usage:**

```bash
pandoc slides.md -t revealjs --lua-filter=hide-slides.lua -o output.html
```

**Customization:**
Edit the `HIDE_TAGS` table in `hide-slides.lua` to specify which classes to hide.

### Python Filter (hide-slides-python.py)

**Pros:**

- More flexible for complex logic
- Can use environment variables
- Easier to debug

**Usage:**

```bash
# Make executable
chmod +x hide-slides-python.py

# Use with default tags
pandoc slides.md -t revealjs --filter=hide-slides-python.py -o output.html

# Use with custom tags via environment variable
HIDE_TAGS=optional,appendix pandoc slides.md -t revealjs --filter=hide-slides-python.py -o output.html
```

## Examples for Your Slides

### Example 1: Hide Optional Content

```markdown
# The Depth Economy

**Acceleration to Mastery**

::: {.optional}

- targeting model based existing phd paper
- Shortest time to PhD-level mastery
  :::

**Metrics:**

- Time to PhD-level mastery
```

### Example 2: Hide Appendix Slides

```markdown
# Call to Action

**What You Can Do Today**
...

---

::: {.appendix}

# Additional Context and Examples

**Historical Subset Transitions:**
...
:::
```

### Example 3: Multiple Tags

```markdown
::: {.optional .detailed}

# Detailed Optional Slide

This slide is both optional and detailed.
:::
```

## Advanced: Metadata-Based Control

Create a more advanced filter that reads YAML metadata:

```markdown
---
title: My Presentation
hide_tags:
  - optional
  - appendix
---

# Regular Slide

::: {.optional}

# This will be hidden

:::
```

Then modify the filter to read from metadata instead of hardcoded tags.

## Integration with Your Workflow

For your `tretc-2026-slides-john-zak.md` file:

1. **Wrap optional slides in divs:**

   ```markdown
   ::: {.optional}

   # The Depth Economy

   ...
   :::
   ```

2. **Use the filter when generating:**

   ```bash
   pandoc tretc-2026-slides-john-zak.md \
     -t revealjs \
     --lua-filter=hide-slides.lua \
     -o presentation.html
   ```

3. **Create different versions:**

   ```bash
   # Full version
   pandoc slides.md -t revealjs -o full.html

   # Short version (hides optional/appendix)
   pandoc slides.md -t revealjs --lua-filter=hide-slides.lua -o short.html
   ```

## Tips

- Use semantic class names: `optional`, `appendix`, `detailed`, `advanced`
- Keep a list of which slides are tagged for easy reference
- Test with both full and filtered versions
- Consider using different tags for different audiences (e.g., `educator`, `administrator`, `policymaker`)

