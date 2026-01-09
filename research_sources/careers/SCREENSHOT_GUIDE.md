# Full-Page Screenshot Guide for Career Roadmaps

This guide explains how to install and use CLI tools to capture full-page screenshots of roadmap.sh pages. Full-page screenshots capture the entire scrollable content of a webpage, not just the visible viewport.

## Recommended Tool: shot-scraper

`shot-scraper` is a command-line tool specifically designed for taking screenshots of web pages. It's built on Playwright and makes full-page screenshots simple.

### Installation

#### macOS (using Homebrew)
```bash
brew install shot-scraper
```

#### macOS/Linux (using pip)
```bash
pip install shot-scraper
```

#### Windows (using pip)
```bash
pip install shot-scraper
```

**Note:** On first run, `shot-scraper` will automatically download the required browser binaries (Chromium).

### Basic Usage

#### Single Page Screenshot
```bash
shot-scraper https://roadmap.sh/cyber-security
```

This creates `cyber-security.png` in the current directory.

#### Full-Page Screenshot (Default Behavior)
By default, `shot-scraper` takes full-page screenshots. To be explicit:
```bash
shot-scraper https://roadmap.sh/cyber-security --full
```

#### Specify Output File
```bash
shot-scraper https://roadmap.sh/cyber-security -o cyber-security-full.png
```

#### Wait for Page to Load
If pages need time to load:
```bash
shot-scraper https://roadmap.sh/cyber-security --wait 2000
```
(waits 2000ms after page load)

### Batch Screenshot Script

Create a script to screenshot all roadmaps in the careers directory:

#### Bash Script (`screenshot_roadmaps.sh`)
```bash
#!/bin/bash

# Create screenshots directory
mkdir -p screenshots

# List of roadmap URLs from the careers directory
roadmaps=(
    "https://roadmap.sh/frontend"
    "https://roadmap.sh/backend"
    "https://roadmap.sh/full-stack"
    "https://roadmap.sh/devops"
    "https://roadmap.sh/devsecops"
    "https://roadmap.sh/data-analyst"
    "https://roadmap.sh/cyber-security"
)

# Screenshot each roadmap
for url in "${roadmaps[@]}"; do
    # Extract slug from URL
    slug=$(echo $url | sed 's|https://roadmap.sh/||')
    echo "Screenshotting: $url"
    shot-scraper "$url" -o "screenshots/${slug}.png" --wait 2000
done

echo "All screenshots saved to screenshots/ directory"
```

#### Python Script (`screenshot_roadmaps.py`)
```python
#!/usr/bin/env python3
"""
Screenshot all roadmap.sh pages from the careers directory.
"""
import subprocess
import os
from pathlib import Path

# Roadmap URLs extracted from the careers directory
ROADMAPS = [
    "https://roadmap.sh/frontend",
    "https://roadmap.sh/backend",
    "https://roadmap.sh/full-stack",
    "https://roadmap.sh/devops",
    "https://roadmap.sh/devsecops",
    "https://roadmap.sh/data-analyst",
    "https://roadmap.sh/cyber-security",
]

def screenshot_roadmap(url, output_dir="screenshots"):
    """Take a full-page screenshot of a roadmap URL."""
    os.makedirs(output_dir, exist_ok=True)

    # Extract slug from URL
    slug = url.replace("https://roadmap.sh/", "")
    output_path = os.path.join(output_dir, f"{slug}.png")

    print(f"Screenshotting: {url}")

    # Run shot-scraper
    result = subprocess.run(
        [
            "shot-scraper",
            url,
            "-o", output_path,
            "--wait", "2000",  # Wait 2 seconds for page to load
        ],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(f"  ✓ Saved to {output_path}")
    else:
        print(f"  ✗ Error: {result.stderr}")

if __name__ == "__main__":
    print("Starting screenshot capture...\n")
    for url in ROADMAPS:
        screenshot_roadmap(url)
    print("\nAll screenshots complete!")
```

### Advanced Options

#### Set Viewport Size
```bash
shot-scraper https://roadmap.sh/cyber-security --width 1920 --height 1080
```

#### Set Quality/Format
```bash
# JPEG with quality setting
shot-scraper https://roadmap.sh/cyber-security -o output.jpg --quality 90

# PNG (default, lossless)
shot-scraper https://roadmap.sh/cyber-security -o output.png
```

#### Delay Before Screenshot
```bash
shot-scraper https://roadmap.sh/cyber-security --delay 3000
```
(waits 3 seconds before taking screenshot)

#### JavaScript Execution Before Screenshot
```bash
shot-scraper https://roadmap.sh/cyber-security --javascript "window.scrollTo(0, document.body.scrollHeight)"
```

---

## Alternative Tool: Playwright (Python)

Playwright is more powerful but requires more setup. It's a good alternative if you need more control.

### Installation

```bash
pip install playwright
playwright install chromium
```

### Python Script Example

```python
from playwright.sync_api import sync_playwright
import os

def screenshot_roadmap(url, output_path):
    """Take full-page screenshot using Playwright."""
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url, wait_until="networkidle")

        # Full-page screenshot
        page.screenshot(path=output_path, full_page=True)

        browser.close()

# Usage
screenshot_roadmap(
    "https://roadmap.sh/cyber-security",
    "screenshots/cyber-security.png"
)
```

---

## Alternative Tool: Puppeteer (Node.js)

If you prefer Node.js:

### Installation

```bash
npm install -g puppeteer
```

### Script Example

```javascript
const puppeteer = require('puppeteer');

async function screenshotRoadmap(url, outputPath) {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto(url, { waitUntil: 'networkidle2' });

    // Full-page screenshot
    await page.screenshot({
        path: outputPath,
        fullPage: true
    });

    await browser.close();
}

// Usage
screenshotRoadmap(
    'https://roadmap.sh/cyber-security',
    'screenshots/cyber-security.png'
);
```

---

## Troubleshooting

### Browser Not Found
If you get errors about missing browsers:
- **shot-scraper**: Run `shot-scraper install` to download browser binaries
- **Playwright**: Run `playwright install chromium`
- **Puppeteer**: Browsers are installed automatically with npm install

### Timeout Issues
If pages take too long to load, increase wait time:
```bash
shot-scraper https://roadmap.sh/cyber-security --wait 5000
```

### Permission Errors
On macOS, you may need to grant Terminal/iTerm permission to take screenshots:
- System Preferences → Security & Privacy → Privacy → Screen Recording

### High Memory Usage
Full-page screenshots of very long pages can use significant memory. If you encounter issues:
- Process one page at a time
- Close browser instances between screenshots
- Consider splitting very long pages

---

## Recommended Workflow

1. **Install shot-scraper** (simplest option):
   ```bash
   pip install shot-scraper
   ```

2. **Create screenshots directory**:
   ```bash
   mkdir -p screenshots
   ```

3. **Run batch screenshot script** (use the Python script above or create your own)

4. **Verify screenshots** are full-page by checking their dimensions

---

## Output Format

Screenshots will be saved as PNG files (or JPEG if specified) with:
- Full page height (captures entire scrollable content)
- Default width: 1280px (or as specified)
- High quality, suitable for documentation or printing

---

## Notes

- Full-page screenshots can be very large files for long pages
- Some pages may have lazy-loaded content; use `--wait` or `--delay` options
- Screenshots are taken in headless browser mode (no visible window)
- All tools support taking screenshots of local HTML files as well
