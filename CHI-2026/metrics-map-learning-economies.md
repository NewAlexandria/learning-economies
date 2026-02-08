# Comprehensive Metrics Map for Learning Economies

This document maps **candidate metrics** to each Learning Economy (Breadth, Depth, Subset, Superset, Network-form), with suitability rationale, data sources, and operationalization notes. It references [metrics-literature-sources.md](./metrics-literature-sources.md) for literatures and [2025-09-14-AI-learning-economics.md](../2025-09-14-AI-learning-economics.md) for extended “Metrics to consider.” It also documents **unsuitable metrics** (Annex) with reasons they are germane to the literature but not to Learning Economies.

**Context**: Metric choice is for *evolutionarily advanced* / AI-augmented learning (early education through doctoral/vocational) and for *multi-economy fluency*—the ability to navigate across economies and leverage Resonance—rather than single-axis performance.

---

## Context Statement

The Learning Economies framework evaluates TfT (tools for thought) and AI-augmented learning along five distinct economies of cognitive value creation. Metrics selected here are intended to:

- Support evaluation across **learning levels** (early ed, K–12, vocational, skilled R&D, doctoral) where applicable.
- Capture **which economy** is being exercised (Breadth vs Depth vs Subset etc.) and **cross-domain/scale** dynamics.
- Align with **Resonance** as the transfer mechanism and with **intermediary outcomes** that scaffold thinking (navigation artefacts, reflective checkpoints, resonance traces, scale movements).
- Avoid single-axis or fixed-pathway measures that contradict multi-economy fluency (see Annex: Unsuitable Metrics).

---

## 1. Breadth Economy

**Definition**: Diversification across multiple domains; parallel intellectual pipelines; multi-subject or multi-credential mastery.

### 1.1 Candidate Metrics (with likely literature source)

| Metric | Literature source | Level note |
|--------|-------------------|------------|
| Diversity index of fields mastered | Interdisciplinary / breadth literature; 2025-09-14 | All levels; adapt “fields” to level (e.g. subjects in K–12, credentials in vocational) |
| Number of concurrent/parallel pipelines (domains in progress) | Breadth/portfolio literature; NIST-800-181 (H1) | All levels |
| Number of distinct domains with proficiency ≥ threshold | Assessment literature; NICE-aligned (e.g. ≥3 domains, 80% in 12 weeks) | Vocational/undergrad in NIST; generalize for K–12 |
| Time to proficiency across multiple unrelated subjects | 2025-09-14; learning sciences | All levels |
| Interdisciplinary project count in time frame | Interdisciplinary / CSCL | K–12 through doctoral |
| Number of credentials/degrees completed in parallel | Higher ed; 2025-09-14 | Higher ed / vocational |

### 1.2 Suitability and Rationale

- **Most suitable**: **Diversity index of fields mastered**, **concurrent pipelines**, **number of domains with proficiency ≥ threshold**. They directly capture parallel-domain mastery and breadth rather than depth or subset mobility. Diversity index avoids collapsing to a single score.
- **Suitable with care**: Time to proficiency across subjects (must be clearly “across” subjects to reflect Breadth). Interdisciplinary project count (good proxy if “field” is defined).
- **Data sources / operationalization**: Portfolio analysis, course enrollment, LMS assessments, proctored exams, time logs (see CHI table and NIST H1). For early ed/K–12, “fields” = subjects or activity domains; for vocational, credentials and certifications.

---

## 2. Depth Economy

**Definition**: Acceleration of mastery within a field; time-to-competence; retention of deep knowledge.

### 2.1 Candidate Metrics (with likely literature source)

| Metric | Literature source | Level note |
|--------|-------------------|------------|
| Time-to-competence (e.g. days to 90th percentile) | Expertise/deliberate practice; NIST H3 | All levels; adapt “competence” to level |
| Hours to independent problem-solving | Deliberate practice; 2025-09-14 | Vocational/skilled R&D |
| Retention at 30/90 days (or equivalent) | Cognitive/assessment literature; NIST H3, H4 | All levels |
| Velocity curves (progress over time) | Learning analytics; CHI paper table | All levels |
| Time from novice to professional certification | Vocational/workforce | Vocational |
| Retention rate after accelerated learning | Depth/compression literature; 2025-09-14 | All levels |

### 2.2 Suitability and Rationale

- **Most suitable**: **Time-to-competence** (e.g. to 90th percentile or certification), **retention at 30/90 days**, **velocity curves**. They capture acceleration and sustained mastery without conflating with Breadth or Subset. NIST H3/H4 provide operationalization (guided AI practice, compressed materials, spaced recall).
- **Suitable with care**: Hours to independent problem-solving (domain-specific; define “independent” and “advanced” per level).
- **Data sources / operationalization**: Assessment timestamps, milestone logs, exam records, spaced-recall quizzes, low-stakes quizzes (CHI table; NIST H3, H4).

---

## 3. Subset Economy

**Definition**: Mobility through rapid retraining; career pivot; cross-domain transfer success; employability in new field.

### 3.1 Candidate Metrics (with likely literature source)

| Metric | Literature source | Level note |
|--------|-------------------|------------|
| Time to employability / time to certification in new field | Vocational/workforce; NIST H5 | Vocational/skilled |
| Transfer speed / time to first independent contribution in new domain | Transfer literature; NIST H5; CHI paper | All levels (adapt “contribution”) |
| Career pivot frequency; number of distinct professional fields | 2025-09-14; workforce | Vocational/career |
| Cross-domain transfer task pass rate (first attempt) | Transfer literature; NIST H2 | All levels |
| Liquidity index / skills convertibility (predicting pivot success) | NIST H6; workforce | Organizational/vocational |
| Retention of core skills after transition | 2025-09-14 | Vocational |

### 3.2 Suitability and Rationale

- **Most suitable**: **Time to employability (or certification) in new field**, **time to first independent contribution**, **transfer task pass rate**. They capture mobility and Resonance-enabled transfer. NIST H5 (resonance-mapped retraining), H2 (resonance prompts), H6 (liquidity) align.
- **Suitable with care**: Career pivot frequency (needs time window and definition of “pivot”); liquidity index (organizational-level but informs Subset design).
- **Data sources / operationalization**: Career pivot data, skill assessments, cert records, PR/task timestamps, HRIS, skills inventory (CHI table; NIST H2, H5, H6).

---

## 4. Superset Economy

**Definition**: Creative destruction through field-level reinvention; cross-domain synthesis; obviation of prior practices.

### 4.1 Candidate Metrics (with likely literature source)

| Metric | Literature source | Level note |
|--------|-------------------|------------|
| Cross-domain synthesis rate; count of “obviating” proposals | NIST H7; innovation/synthesis literature | R&D / doctoral / teams |
| Time from field exposure to field transformation/obviation | 2025-09-14; innovation | Superset-specific |
| Economic impact multiplier (value created/destroyed) | 2025-09-14; economics of innovation | Organizational |
| Number of previously unconnected domains synthesized | 2025-09-14 | R&D / doctoral |
| Downstream adoption of disruptive proposals (e.g. within 12 months) | NIST H7 | Organizational |
| Reduction in legacy-task demand (e.g. % after superset prototype) | NIST H8 | Operational |

### 4.2 Suitability and Rationale

- **Most suitable**: **Count of obviating proposals** (blinded panel), **cross-domain synthesis rate**, **time from exposure to reinvention**, **adoption of disruptive proposals**. They capture field-level reinvention and synthesis rather than single-domain depth or simple transfer. NIST H7, H8 give concrete measures.
- **Suitable with care**: Economic impact multiplier (needs clear definition of value/destroyed); legacy-task reduction (operational proxy for obviation).
- **Data sources / operationalization**: Artefact analysis, innovation outputs, proposal corpus, panel ratings, adoption metrics, time tracking (CHI table; NIST H7, H8).

---

## 5. Network-form Economy

**Definition**: Multi-scale knowledge routing; scale traversals; path length; emergent pattern discovery.

### 5.1 Candidate Metrics (with likely literature source)

| Metric | Literature source | Level note |
|--------|-------------------|------------|
| Scale traversals (micro ↔ macro) per task or per learner | 2025-09-14; CHI table | All levels (adapt scale definitions) |
| Path length (e.g. steps/time from signal to systemic insight) | NIST H9; knowledge graph / LA | Analysts / research |
| Routing efficiency; path length reduction with cross-scale links | 2025-09-14; NIST H10 | Research / learning systems |
| Discovery rate of emergent patterns (with compressed/semantic routing) | NIST H10; 2025-09-14 | Research teams |
| Number of distinct scale traversals navigated in a domain | 2025-09-14 | All levels |
| Percentage of queries benefiting from multi-scale vs single-scale routing | Learning analytics; TfT | TfT / LA contexts |

### 5.2 Suitability and Rationale

- **Most suitable**: **Scale traversals**, **path length (steps/time to systemic insight)**, **routing efficiency / path length reduction**, **emergent pattern discovery rate**. They capture multi-scale navigation and topology rather than single-scale or single-economy outcomes. NIST H9, H10 operationalize (e.g. AI path suggestions micro→macro; compressed knowledge graph vs flat wiki).
- **Suitable with care**: “Queries benefiting from multi-scale” (requires definition of benefit and scale).
- **Data sources / operationalization**: Query logs, navigation patterns, case systems, timestamps, lab notebook mining, citation graphs (CHI table; NIST H9, H10).

---

## 6. Intermediary Outcomes

These scaffold thinking and support TfT evaluation beyond task completion. Keep and extend from CHI paper and workshop emphasis.

| Outcome | Source | Suitability for TfT / multi-economy |
|--------|--------|-------------------------------------|
| **Navigation artefacts** | CHI paper; TfT workshop | High: diagrams, notes, maps while exploring; supports Breadth/Network-form |
| **Reflective checkpoints** | CHI paper; cybernetic/feedback literature | High: goal interrogation with advisors; supports all economies |
| **Resonance traces** | CHI paper; transfer/synthesis literature | High: explicit cross-domain connections; supports Subset/Superset |
| **Scale movements** | CHI paper; Network-form | High: records of micro↔macro movement; supports Network-form |
| **Think-aloud / verbal protocols** | Metacognition/assessment literature | High: process evidence; level-appropriate (e.g. K–12 to doctoral) |
| **Concept maps** | Learning sciences; assessment | High: structure of knowledge; can show breadth, depth, and cross-links |
| **Goal statements; learning path diagrams; reflection journals; advisor feedback logs** | CHI §3.2; reflective advisor loop | High: evidence of reflective loop and direction confirmation |

**Data sources**: LMS exports, advisor logs, learner-produced artefacts, study protocols. Tag by economy where possible (e.g. resonance traces → Subset/Superset; scale movements → Network-form).

---

## 7. References to Existing Repo

- **Primary metrics table**: [chi-2026-paper.md](./chi-2026-paper.md) §4.1 (Economy | Primary Metrics | Data Sources).
- **Extended “Metrics to consider”**: [2025-09-14-AI-learning-economics.md](../2025-09-14-AI-learning-economics.md) per economy.
- **Operational measures and NICE alignment**: [NIST-800-181-testable-templates.md](../NIST-800-181-testable-templates.md) (14 hypotheses with measures, data sources, KSAs).
- **Literatures for exhaustive search**: [metrics-literature-sources.md](./metrics-literature-sources.md).

---

# Annex: Unsuitable Metrics and Rationale

The following metric types are **germane to the literatures** but **unsuitable for Learning Economies** as primary metrics. Documenting them gives reviewers and future work a clear “in scope vs out of scope.”

## A.1 Single-axis performance scores

- **Examples**: Raw GPA, single-domain test score, one subject grade.
- **Why in literature**: Standard in assessment and accountability (breadth of courses, achievement).
- **Why unsuitable**: Do not capture *which* economy (Breadth vs Depth vs Subset etc.) or cross-domain/scale; can contradict multi-economy fluency (e.g. optimizing GPA may favor one economy and obscure others). Do not capture Resonance or scale traversal.

## A.2 Purely task-completion or productivity metrics

- **Examples**: Tasks completed per hour, clicks, completion rate without understanding/transfer.
- **Why in literature**: Common in HCI and productivity research.
- **Why unsuitable**: TfT workshop emphasizes “beyond task performance”; such metrics may miss understanding, transfer, and metacognition. They do not distinguish economies or intermediary outcomes that scaffold thinking.

## A.3 Metrics that assume fixed, linear pathways

- **Examples**: Progress along a single predefined curriculum path; “time to degree” without economy-specific breakdown.
- **Why in literature**: Common in institutional and degree-completion research.
- **Why unsuitable**: Framework emphasizes fluid navigation across economies and Resonance; fixed-path metrics do not capture cross-domain or scale movement and can misrepresent Subset/Superset/Network-form.

## A.4 Metrics that ignore level or modality

- **Examples**: PhD-time-only metrics with no K–12 or vocational variant; single learning modality (e.g. only formal coursework).
- **Why in literature**: Many studies are level- or context-specific.
- **Why unsuitable**: Framework is for evolutionarily advanced learning *across* levels (early ed through doctoral/vocational); metrics that apply only at one level are insufficient for a unified map. Level-agnostic or level-tagged variants are preferred.

## A.5 Metrics that conflate economies without disaggregation

- **Examples**: “Overall learning gain” with no breakdown by Breadth/Depth/Subset/Superset/Network-form; “engagement” as a single composite.
- **Why in literature**: Composite scores are common for parsimony.
- **Why unsuitable**: Learning Economies require distinguishing which economy is being measured so that multi-economy fluency and design implications can be evaluated per economy.

## A.6 Summary

Use the above to exclude or downweight metrics that would undermine the framework’s goals. When citing literature that uses these metrics, note their limitations for Learning Economies and prefer economy-specific, level-aware, and intermediary-outcome-oriented measures where possible.
