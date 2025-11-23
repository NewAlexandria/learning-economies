#!/usr/bin/env python3
"""
Pandoc Python filter to conditionally hide slides based on tags/classes.

Usage:
    pandoc input.md -t revealjs --filter=hide-slides-python.py -o output.html

Or with environment variable to control what to hide:
    HIDE_TAGS=optional,appendix pandoc input.md -t revealjs --filter=hide-slides-python.py -o output.html
"""

import os
import sys
import json
from pandocfilters import toJSONFilter, Div, Header

# Configuration: tags/classes that should be hidden
# Can be overridden with HIDE_TAGS environment variable
DEFAULT_HIDE_TAGS = ["optional", "hide", "appendix", "detailed"]

def get_hide_tags():
    """Get list of tags to hide from environment or use defaults."""
    env_tags = os.environ.get("HIDE_TAGS")
    if env_tags:
        return [tag.strip() for tag in env_tags.split(",")]
    return DEFAULT_HIDE_TAGS

def should_hide(elem):
    """Check if an element should be hidden based on its classes."""
    if 'c' in elem and elem['c']:
        classes = elem['c'][0] if isinstance(elem['c'], list) and len(elem['c']) > 0 else []
        if isinstance(classes, list):
            hide_tags = get_hide_tags()
            for class_name in classes:
                if class_name in hide_tags:
                    return True
    return False

def filter_slides(key, value, format, meta):
    """Main filter function."""
    if key == 'Div':
        # Check if div has a class that should be hidden
        if should_hide(value):
            return []  # Remove the div
    elif key == 'Header':
        # Check if header has a class that should be hidden
        if should_hide(value):
            return []  # Remove the header

    return None  # Keep the element

if __name__ == "__main__":
    toJSONFilter(filter_slides)


