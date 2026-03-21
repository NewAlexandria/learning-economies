# Model for Revising the Learning Economies Repository

Purpose

- Capture a concise, actionable model to guide revisions to the Learning Economies repo.
- Surface a repo structure, curriculum model, rubric templates, agent engagement patterns, and an implementation checklist.

Scope

- Focus: repository organization and content needed to support curriculum design, rubrics, and agentic workflows for education and workforce pipelines (K-12 → PhD → vocational).
- Tools: integrate existing assets (NIST/NICE templates, microcredentials, stochastic-context-eval, verne/Jules/agentzero/openclaw).

Proposed Repository Structure

- `curriculum/` : curriculum ontologies, course/module templates, canonical learning paths.
- `rubrics/` : rubric templates (Depth, Breadth), example scored rubrics, scoring scripts.
- `agents/` : agent skills, prompts, agent integration patterns, conversation-tracking examples (IDs, logging).
- `integrations/` : connectors and instructions for `stochastic-context-eval`, `verne_durand`/Jules, AgentZero/OpenClaw, PDF ingestion.
- `pilots/` : experiment protocols, NIST-800-181 testable templates, pilot data schemas.
- `docs/` : public README, service-demo, contribution guide, governance for ethical assessments.

Curriculum Model (cleaned and actionable)

- Goal: support two complementary curriculum streams: (A) focused depth tracks that can scale to PhD-level mastery; (B) breadth/portfolio tracks for multi-domain competency.
- Parts:
  - Ontology selection: document which ontologies are in-scope (e.g., NIST/NICE KSA mappings, institution curricula such as Slippery Rock examples, and any Nest-181 style ontologies). Note tradeoffs and mapping guidance.
  - Curriculum templates: module spec (learning objectives, prerequisites, materials, assessments, time estimates, AI-assist hooks).
  - Path recipes: linear, branching, and portfolio templates (single-discipline ladder, multi-degree portfolio, microcredential stacks).

Rubrics (two starter templates)

- Depth Rubric (PhD / mastery-oriented)
  - Criteria: Conceptual rigor, independent problem-solving, original contribution, methodological correctness, literature synthesis.
  - Levels: 1 (intro) → 5 (original contribution/defendable research). Provide scoring anchors and sample evidence per level.
- Breadth Rubric (portfolio / breadth-oriented)
  - Criteria: Domain coverage, integrative projects, transferable skills, collaboration span, applied outcomes.
  - Levels: 1 (exposed) → 5 (multi-domain fluency demonstrated by projects).

Agent Engagement Patterns

- Onboarding agent: collects goals, background, and preferred learning economy (Breadth / Depth / Subset / Superset / Network-form).
- Curriculum-selector agent: maps learner profile → curriculum template + recommended rubrics and pilot hypotheses.
- Reflective-advisor loop (human+agent): schedule checkpoints, capture reflections, prompt redesign of paths, and log advisor IDs for continuity.
- Assessment assistant: auto-score formative tasks, generate evidence bundles for rubric anchors, prepare evaluator review packets.
- Conversation & artifact tracking: persist conversation IDs, activity logs, and artifact references (PDFs, code, notebooks) for reproducibility and follow-up.

Integration & Tools

- PDFs: use `stochastic-context-eval` for parsing and extracting curriculum/references from PDFs. Store transcripts and vector indexes in `integrations/` docs.
- Deep-task queue: document `verne_durand` + Jules CLI usage for long-running reasoning tasks (research threads). Include MCP/CLI setup notes.
- Agent frameworks: provide quick-start examples for AgentZero and OpenClaw; list relevant skill libraries (promptintel, openclaw-shield, molt).

Implementation Checklist (first pass)

1. Create folder skeleton listed above and add README stubs.
2. Move existing curriculum and TRETC/Talk materials into `curriculum/` and `pilots/` with canonical filenames.
3. Add the two rubric templates as editable markdown plus a JSON schema for machine scoring.
4. Add agent skill examples (short scripts + prompt templates) into `agents/` and document runtime requirements.
5. Add `integrations/` guides: `stochastic-context-eval` ingestion example, verne/Jules queue example, and AgentZero/OpenClaw quickstarts.
6. Draft two small pilots: (a) Cybersecurity microcredential using NIST-800-181 testable templates; (b) Breadth portfolio pilot for an interdisciplinary cohort.
7. Add CONTRIBUTING and DATA-GOVERNANCE notes describing ethical review, privacy, and evaluation methods.

Next steps (for me or collaborators)

- I can: (A) scaffold the folders and stubs; (B) migrate selected docs into the new structure; (C) add rubric JSON schemas and a sample agent prompt set.
- Ask: confirm whether you want the new files under the submodule path (recommended) and whether to update `ingest_URLS.md` to link to this model.

References & provenance

- Source: cleaned from `ingest_URLS.md` learning-economies notes and the submodule `submodules/modeling/learning-economies` content.
