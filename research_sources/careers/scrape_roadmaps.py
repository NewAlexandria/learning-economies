#!/usr/bin/env python3
"""
Script to scrape roadmap.sh career roadmaps.
This script provides a list of all roadmaps to scrape.
The actual scraping should be done using browser MCP tools.
"""

ROLE_BASED_ROADMAPS = [
    ("frontend", "Frontend Developer"),
    ("backend", "Backend Developer"),
    ("full-stack", "Full Stack Developer"),
    ("devops", "DevOps Engineer"),
    ("devsecops", "DevSecOps Engineer"),
    ("data-analyst", "Data Analyst"),
    ("ai-engineer", "AI Engineer"),
    ("ai-data-scientist", "AI and Data Scientist"),
    ("data-engineer", "Data Engineer"),
    ("android", "Android Developer"),
    ("machine-learning", "Machine Learning Engineer"),
    ("postgresql-dba", "PostgreSQL DBA"),
    ("ios", "iOS Developer"),
    ("blockchain", "Blockchain Developer"),
    ("qa", "QA Engineer"),
    ("software-architect", "Software Architect"),
    ("cyber-security", "Cyber Security Expert"),
    ("ux-design", "UX Designer"),
    ("technical-writer", "Technical Writer"),
    ("game-developer", "Game Developer"),
    ("server-side-game-developer", "Server Side Game Developer"),
    ("mlops", "MLOps Engineer"),
    ("product-manager", "Product Manager"),
    ("engineering-manager", "Engineering Manager"),
    ("devrel", "Developer Relations"),
    ("bi-analyst", "BI Analyst"),
]

SKILL_BASED_ROADMAPS = [
    ("sql", "SQL"),
    ("computer-science", "Computer Science"),
    ("react", "React"),
    ("vue", "Vue"),
    ("angular", "Angular"),
    ("javascript", "JavaScript"),
    ("typescript", "TypeScript"),
    ("nodejs", "Node.js"),
    ("python", "Python"),
    ("system-design", "System Design"),
    ("java", "Java"),
    ("aspnet-core", "ASP.NET Core"),
    ("api-design", "API Design"),
    ("spring-boot", "Spring Boot"),
    ("flutter", "Flutter"),
    ("cpp", "C++"),
    ("rust", "Rust"),
    ("golang", "Go"),
    ("software-design-architecture", "Design and Architecture"),
    ("graphql", "GraphQL"),
    ("react-native", "React Native"),
    ("design-system", "Design System"),
    ("prompt-engineering", "Prompt Engineering"),
    ("mongodb", "MongoDB"),
    ("linux", "Linux"),
    ("kubernetes", "Kubernetes"),
    ("docker", "Docker"),
    ("aws", "AWS"),
    ("terraform", "Terraform"),
    ("datastructures-and-algorithms", "Data Structures & Algorithms"),
    ("redis", "Redis"),
    ("git-github", "Git and GitHub"),
    ("php", "PHP"),
    ("cloudflare", "Cloudflare"),
    ("ai-red-teaming", "AI Red Teaming"),
    ("ai-agents", "AI Agents"),
    ("nextjs", "Next.js"),
    ("code-review", "Code Review"),
    ("kotlin", "Kotlin"),
    ("html", "HTML"),
    ("css", "CSS"),
    ("swift-ui", "Swift & Swift UI"),
    ("shell-bash", "Shell / Bash"),
    ("laravel", "Laravel"),
    ("elasticsearch", "Elasticsearch"),
    ("wordpress", "WordPress"),
    ("django", "Django"),
]

def get_roadmap_url(slug):
    """Get the full URL for a roadmap slug."""
    return f"https://roadmap.sh/{slug}"

def get_filename(slug):
    """Get the filename for a roadmap slug."""
    return f"{slug}.md"

if __name__ == "__main__":
    print("Role-based Roadmaps:")
    for slug, name in ROLE_BASED_ROADMAPS:
        print(f"  - {name}: {get_roadmap_url(slug)} -> {get_filename(slug)}")

    print(f"\nTotal role-based roadmaps: {len(ROLE_BASED_ROADMAPS)}")
    print(f"Total skill-based roadmaps: {len(SKILL_BASED_ROADMAPS)}")
