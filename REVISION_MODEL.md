# Model for Revising the Learning Economies Repository

## Purpose

- Capture a concise, actionable model to guide revisions to the Learning Economies repo.
- Organize content around **three main objectives** (engagement, curriculum/platform, epochs/analysis), with a clear documentation story at the root and per pillar.

## Scope

- Focus: repository organization and content needed to support curriculum design, rubrics, and agentic workflows for education and workforce pipelines (K-12 → PhD → vocational).
- Tools: integrate existing assets (NIST/NICE templates, microcredentials, stochastic-context-eval, verne/Jules/agentzero/openclaw).

## Three repository objectives

The repo holds three complementary streams. Naming below is descriptive; exact top-level folder names can follow the **Proposed repository structure** section.

### 1. Engagement and external activity

- Partnerships, conference and workshop participation, community engagement, and related logistics.
- Presentation materials, pitches, and other **business-facing** or stakeholder-facing artifacts (slides, one-pagers, demo scripts).

### 2. Curriculum, standards, and platform

- Curricula, ontologies, standards mappings, and rubrics used for analysis and evaluation.
- Multi-agent models, human user / learner types, prompts and skills, and integration patterns.
- Application or deployed code, connectors, pilots, and experiment protocols.

### 3. Epoch outputs and analysis

- Epoch (or run) outputs: artifacts produced by defined periods or batch processes.
- Data analysis methods and code, analysis outputs (figures, tables, reports), and **schemas** that describe those outputs for reuse and tooling.

## Documentation layout

Use **both** a small root-facing doc set and **per-pillar** entry points so newcomers see the map first, while each tree stays self-explanatory.

### Root

- **`README.md`** — Short orientation: what the repo is, the three objectives, and links into each pillar’s entry doc (and into `docs/` for governance).
- **`REVISION_MODEL.md`** (this file) — Structural intent and checklist; optional to move under `docs/` later if the root should stay minimal.

### Repository-wide `docs/`

- Cross-cutting material only: **CONTRIBUTING**, **DATA-GOVERNANCE** / ethical assessment notes, glossary, architecture or “how the pillars connect,” service-demo pointers.
- Avoid duplicating pillar-specific content here; **link** to the right folder README instead.

### Per pillar (each major folder)

- **`README.md` in that folder** — Default “docs” for that pillar: purpose, layout of subfolders, how to add material, and links to key files.
- **Optional `docs/` inside a pillar** (e.g. `engagement/docs/`) — Use when narrative volume is high (e.g. conference retrospectives, long-form standards commentary) so the pillar root stays scannable. Do not create empty `docs/` stubs “just because.”

**Rule of thumb:** one **README per top-level pillar folder** is required for clarity; root **`docs/`** holds policies and cross-pillar explanations; deeper **`docs/`** subfolders only where they reduce clutter.

## Proposed repository structure

Group top-level folders by the three objectives. Subfolders can evolve; the headings below show intent.

### Pillar 1 — Engagement

- `engagement/` — partnerships, conferences, workshops, pitches, decks, one-pagers, demo scripts, activity notes.

### Pillar 2 — Curriculum and platform

- `curriculum/` — ontologies, course/module templates, canonical learning paths, standards mappings.
- `rubrics/` — rubric templates (Depth, Breadth), example scored rubrics, scoring scripts, JSON schemas for machine scoring where applicable.
- `agents/` — two-level agent layout:
  - **Working agents** — skills, prompts, integration patterns, and conversation-tracking examples (IDs, logging) for task-focused roles (onboarding, curriculum selection, assessment, reflection, etc.).
  - **Board of Advisors** — a critique-oriented agent-team pattern that sits above working agents: reviews and challenges their outputs, resolves conflicts, prioritizes what runs next, and keeps the overall workflow coherent.
- `integrations/` — connectors and instructions for `stochastic-context-eval`, `verne_durand`/Jules, AgentZero/OpenClaw, PDF ingestion.
- `pilots/` — experiment protocols, NIST-800-181 testable templates, pilot data schemas.
- `applications/` *(optional if needed)* — deployed or demo application code; if the footprint is small, keep under `integrations/` or `pilots/` and document in the pillar README.

### Pillar 3 — Epochs and analysis

- `epochs/` *(or `analysis/` if you prefer that name)* — epoch/run outputs, analysis code and notebooks, derived tables and figures, and **schemas** for outputs and metadata.

### Root `docs/`

- As in [Documentation layout](#documentation-layout): governance, contributing, cross-pillar architecture—not a fourth “content” pillar.

## Curriculum Model (cleaned and actionable)

### Goal

- Support two complementary curriculum streams: (A) focused depth tracks that can scale to PhD-level mastery; (B) breadth/portfolio tracks for multi-domain competency.

### Ontology selection

- Document which ontologies are in-scope (e.g., NIST/NICE KSA mappings, institution curricula such as Slippery Rock examples, and any Nest-181 style ontologies). Note tradeoffs and mapping guidance.

### Curriculum templates

- Module spec (learning objectives, prerequisites, materials, assessments, time estimates, AI-assist hooks).

### Path recipes

- Linear, branching, and portfolio templates (single-discipline ladder, multi-degree portfolio, microcredential stacks).

## Rubrics (two starter templates)

### Depth Rubric (PhD / mastery-oriented)

- Criteria: Conceptual rigor, independent problem-solving, original contribution, methodological correctness, literature synthesis.
- Levels: 1 (intro) → 5 (original contribution/defendable research). Provide scoring anchors and sample evidence per level.

### Breadth Rubric (portfolio / breadth-oriented)

- Criteria: Domain coverage, integrative projects, transferable skills, collaboration span, applied outcomes.
- Levels: 1 (exposed) → 5 (multi-domain fluency demonstrated by projects).

## Agent Engagement Patterns

- Board of Advisors (meta-layer): critique agent team that organizes all other agent patterns—synthesizes outputs, surfaces disagreements, and steers orchestration so working agents stay aligned with learner goals and rubrics.
- Onboarding agent: collects goals, background, and preferred learning economy (Breadth / Depth / Subset / Superset / Network-form).
- Curriculum-selector agent: maps learner profile → curriculum template + recommended rubrics and pilot hypotheses.
- Reflective-advisor loop (human+agent): schedule checkpoints, capture reflections, prompt redesign of paths, and log advisor IDs for continuity.
- Assessment assistant: auto-score formative tasks, generate evidence bundles for rubric anchors, prepare evaluator review packets.
- Conversation & artifact tracking: persist conversation IDs, activity logs, and artifact references (PDFs, code, notebooks) for reproducibility and follow-up.

## Integration & Tools

- PDFs: use `stochastic-context-eval` for parsing and extracting curriculum/references from PDFs. Store transcripts and vector indexes in `integrations/` docs.
- Deep-task queue: document `verne_durand` + Jules CLI usage for long-running reasoning tasks (research threads). Include MCP/CLI setup notes.
- Agent frameworks: provide quick-start examples for AgentZero and OpenClaw; list relevant skill libraries (promptintel, openclaw-shield, molt).

## Implementation Checklist (first pass)

1. Align folder skeleton with the **three objectives** and add **README.md** for each new or renamed top-level pillar folder.
2. Add or refresh **root `README.md`** and **`docs/`** stubs (CONTRIBUTING, DATA-GOVERNANCE) per [Documentation layout](#documentation-layout).
3. Move existing curriculum and TRETC/Talk materials into the appropriate pillar (`curriculum/`, `pilots/`, `engagement/`, etc.) with canonical filenames.
4. Add the two rubric templates as editable markdown plus a JSON schema for machine scoring.
5. Add agent skill examples (short scripts + prompt templates) into `agents/` and document runtime requirements in that folder’s README.
6. Add `integrations/` guides: `stochastic-context-eval` ingestion example, verne/Jules queue example, and AgentZero/OpenClaw quickstarts.
7. Define **`epochs/`** (or `analysis/`) layout: where raw outputs, code, and schemas live; document in that folder’s README.
8. Draft two small pilots: (a) Cybersecurity microcredential using NIST-800-181 testable templates; (b) Breadth portfolio pilot for an interdisciplinary cohort.

## Next steps (for me or collaborators)

- I can: (A) scaffold folders and README stubs for all three pillars; (B) migrate selected docs into the new structure; (C) add rubric JSON schemas and a sample agent prompt set.
- Ask: confirm whether you want the new files under the submodule path (recommended), preferred name for pillar 3 (`epochs/` vs `analysis/`), and whether to update `ingest_URLS.md` to link to this model.

## References & provenance

- Source: cleaned from `ingest_URLS.md` learning-economies notes and the submodule `submodules/modeling/learning-economies` content.
