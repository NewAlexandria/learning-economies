#!/usr/bin/env python3
"""
Screenshot all roadmap.sh pages from the careers directory.

This script uses shot-scraper to capture full-page screenshots of all
roadmap pages. Install shot-scraper first:
    pip install shot-scraper

Usage:
    python screenshot_roadmaps.py
"""
import subprocess
import os
import sys
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

def check_shot_scraper():
    """Check if shot-scraper is installed."""
    try:
        subprocess.run(
            ["shot-scraper", "--version"],
            capture_output=True,
            check=True
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def screenshot_roadmap(url, output_dir="screenshots", wait_time=2000):
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
            "--wait", str(wait_time),  # Wait for page to load
            "--full",  # Explicitly request full-page screenshot
        ],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        # Check if file was created
        if os.path.exists(output_path):
            file_size = os.path.getsize(output_path)
            print(f"  ✓ Saved to {output_path} ({file_size:,} bytes)")
            return True
        else:
            print(f"  ✗ Error: File was not created")
            return False
    else:
        print(f"  ✗ Error: {result.stderr}")
        return False

def main():
    """Main function to screenshot all roadmaps."""
    print("=" * 60)
    print("Roadmap.sh Full-Page Screenshot Tool")
    print("=" * 60)
    print()

    # Check if shot-scraper is installed
    if not check_shot_scraper():
        print("ERROR: shot-scraper is not installed.")
        print()
        print("Install it with:")
        print("  pip install shot-scraper")
        print()
        print("Or on macOS with Homebrew:")
        print("  brew install shot-scraper")
        sys.exit(1)

    print(f"Found {len(ROADMAPS)} roadmaps to screenshot")
    print()

    # Screenshot each roadmap
    success_count = 0
    for i, url in enumerate(ROADMAPS, 1):
        print(f"[{i}/{len(ROADMAPS)}] ", end="")
        if screenshot_roadmap(url):
            success_count += 1
        print()

    # Summary
    print("=" * 60)
    print(f"Complete: {success_count}/{len(ROADMAPS)} screenshots saved")
    print(f"Output directory: {os.path.abspath('screenshots')}")
    print("=" * 60)

if __name__ == "__main__":
    main()
