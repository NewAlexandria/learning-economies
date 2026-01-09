#!/usr/bin/env python3
"""
Helper script to format and save roadmap content.
This is called after extracting content from browser.
"""

def save_roadmap(slug, title, url, description, content):
    """Save a roadmap to a markdown file."""
    filename = f"{slug}.md"
    filepath = f"/Users/zak/src/projects/learning-economies/research_sources/careers/{filename}"

    # Extract just the roadmap content (remove navigation, footer, etc.)
    lines = content.split('\n')
    roadmap_start = False
    roadmap_lines = []

    for line in lines:
        # Skip header/navigation content
        if any(x in line for x in ['Master SQL', 'START LEARNING', 'Roadmaps', 'AI Tutor', 'Login', 'Sign Up']):
            continue
        if '←  All Roadmaps' in line or 'Schedule Learning Time' in line:
            continue
        if title in line and not roadmap_start:
            roadmap_start = True
            continue
        if roadmap_start:
            if 'Join the Community' in line or 'roadmap.sh is the' in line:
                break
            if line.strip():
                roadmap_lines.append(line.strip())

    # Create markdown content
    md_content = f"""# {title}

**Source:** {url}
**Description:** {description}

---

## Roadmap Content

{chr(10).join(roadmap_lines)}
"""

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(md_content)

    print(f"Saved: {filename}")

if __name__ == "__main__":
    print("This is a helper script for saving roadmaps.")
