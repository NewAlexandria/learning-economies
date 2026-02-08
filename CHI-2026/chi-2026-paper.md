# Learning Economies: A Framework for Measuring Cognitive Outcomes in AI-Augmented Learning

**Workshop Paper for CHI 2026 "Tools for Thought with Generative AI"**

---

## Abstract

Generative AI is transforming learning workflows, raising questions about its effects on cognition while also creating opportunities for designing tools for thought (TfT) that protect and augment human thinking. This paper introduces *Learning Economies*, a theoretical framework that provides both a taxonomy for understanding AI-accelerated learning and measurable outcomes for evaluating TfT effectiveness. We identify five fundamental Learning Economies—Breadth, Depth, Subset, Superset, and Network-form—each representing distinct modes of cognitive value creation. Central to this framework is *Resonance*, the transfer mechanism enabling cross-domain knowledge flow. We present operationalizable metrics for each economy, propose a reflective advisor loop—framed as a cybernetic feedback mechanism—where educators serve as navigational guides through dense information spaces, and discuss design implications for GenAI systems. The framework applies across learning levels from early education through vocational and doctoral practice. It offers HCI researchers and practitioners concrete strategies for defining, measuring, and designing cognitive outcomes in AI-augmented learning contexts.

**Keywords:** Tools for thought, generative AI, learning, cognition, measurement, human-AI interaction

---

## 1. Introduction

Generative AI radically expands the scope and capability of automation for work, learning, and creativity. While impactful, it also changes workflows and raises questions about its effects on cognition, including critical thinking and learning [1]. Yet GenAI also offers opportunities for designing "tools for thought" (TfT) that protect and augment cognition—systems that provoke critical thinking, provide personalized tutoring, or enable novel ways of sensemaking, in a lineage extending from Engelbart's vision of augmenting human intellect [4] and Kay's personal dynamic media [5].

A central challenge for TfT research is defining what constitutes a "good" cognitive outcome and how to measure it. Current approaches often focus narrowly on task performance, missing the richer dimensions of understanding, learning mobility, and metacognitive engagement [6]. We need frameworks that capture intermediary outcomes—the artefacts, navigational choices, and reflective processes that scaffold thinking.

This paper introduces *Learning Economies*, a framework previously introduced to understand AI's transformation of human capital [2]. We adapt it here as a measurement framework for TfT outcomes, proposing five distinct economies of cognitive value creation, each with operationalizable metrics. We further propose a *reflective advisor loop* that positions educators and mentors as navigational guides, helping learners interrogate their goals and validate their paths through increasingly dense information spaces.

---

## 2. The Learning Economies Framework

Learning Economies represent distinct modes of value creation through knowledge acquisition and application. Rather than a single axis of "learning more," the framework identifies five qualitatively different cognitive economies.

### 2.1 The Five Economies

**Breadth Economy**: Diversification across multiple domains. Measures parallel intellectual pipelines, the diversity index of fields mastered, and time to proficiency across unrelated subjects. AI enables simultaneous multi-domain competency that was previously sequential.

**Depth Economy**: Acceleration of mastery within fields. Measures time-to-competence, hours to independent problem-solving, and retention rates. AI removes traditional bottlenecks (waiting for lectures, trial-and-error, bureaucratic prerequisites) to compress PhD-level mastery timelines.

**Subset Economy**: Mobility through rapid retraining. Measures career pivot frequency, retraining time to employability, and cross-domain transfer success. This economy captures vocational and cognitive mobility—the ability to move fluidly between domains.

**Superset Economy**: Creative destruction through field-level reinvention. Measures cross-domain synthesis, time from field exposure to field transformation, and the economic impact of innovations that render prior expertise obsolete. Historical examples include the Jacquard loom obsoleting artisanal weaving and GPS replacing celestial navigation.

**Network-form Economy**: Multi-scale knowledge routing. Measures scale traversals navigated, knowledge topology compression, and emergent property discovery. This economy addresses connections across scales—linking molecular insights to ecosystem dynamics, or code optimizations to architectural patterns.

### 2.2 Resonance as Transfer Mechanism

*Resonance* is the universal mechanism enabling flow between economies. It operates through recognition of deep structural similarities that allow knowledge to recombine across domains and scales:

- In **Subset**: Statistical thinking transfers from physics → finance → marketing
- In **Superset**: GPS emerged from synthesizing satellite technology + atomic clocks + relativistic physics + cartography
- In **Network-form**: Molecular biology insights connect to ecosystem dynamics

AI amplifies Resonance by making cross-domain patterns more visible and surfacing non-obvious transfer opportunities.

### 2.3 Link to LLM Architectural Principles

A theoretical mapping connects the five Learning Economies to five core principles of large language model (LLM) architecture: Breadth aligns with *routing* (parallel pathways across domains); Depth with *compression* (efficient representation enabling rapid mastery); Subset with *temperature* (precision and adjacency governing transfer between domains); Superset with *addressing* (re-addressing what knowledge means when fields are reinvented); and Network-form with *transformation* (non-linear mappings across scales). This mapping explains why AI accelerates all five economies simultaneously and motivates TfT design that either mirrors or deliberately compensates for these architectural biases.

---

## 3. The Reflective Advisor Loop

A critical component missing from many TfT designs is the role of human advisors—teachers, mentors, and peers—in navigating learning spaces. We propose that educators function as a *board of advisors*, providing reflective loops for interrogating learner goals and validating direction.

### 3.1 Navigating Dense Information Spaces

AI-accelerated learning creates unprecedented density of available information and potential learning paths. Learners face not just the challenge of *what* to learn, but *how to discover their path* through this space. The reflective advisor loop addresses this through:

1. **Goal Interrogation**: Regular checkpoints where advisors help learners examine and refine their learning objectives
2. **Pattern Validation**: Advisors identify when learning patterns suggest misalignment with stated goals
3. **Direction Confirmation**: Ongoing validation that the learner's trajectory serves their evolving needs

### 3.2 Stabilization Through Human Feedback

Drawing from LLM architecture metaphors, we conceptualize the educator-learner relationship as a *stabilization mechanism*. Just as reinforcement learning from human feedback (RLHF) aligns model outputs with human values, the reflective advisor loop aligns learning trajectories with learner goals and broader educational objectives.

From a cybernetic perspective, the reflective advisor loop functions as a *human-in-the-loop feedback system*: it corrects drift and realigns trajectories with stated goals, contrasting with open-loop AI-only navigation where learners may optimize locally without periodic goal interrogation. This feedback structure—goal interrogation → pattern validation → direction confirmation—provides the closure required for stable, goal-directed learning in dense information spaces.

This produces measurable intermediary artefacts: goal statements, learning path diagrams, reflection journals, and advisor feedback logs—all of which scaffold thinking and can be analyzed for TfT evaluation.

---

## 4. Operationalizing TfT Outcomes

The Learning Economies framework offers concrete metrics aligned with the workshop's call for capturing "the richness of cognition."

### 4.1 Metrics by Economy

| Economy | Primary Metrics | Data Sources |
|---------|-----------------|--------------|
| Breadth | Diversity index, concurrent pipelines | Portfolio analysis, course enrollment |
| Depth | Time-to-competence, velocity curves | Assessment timestamps, milestone logs |
| Subset | Transfer speed, retraining efficiency | Career pivot data, skill assessments |
| Superset | Cross-domain connections, synthesis rate | Artefact analysis, innovation outputs |
| Network-form | Scale traversals, routing efficiency | Query logs, navigation patterns |

### 4.2 Capturing Intermediary Outcomes

Following the workshop's emphasis on "intermediary artefacts that scaffold thinking," we propose tracking:

- **Navigation Artefacts**: Diagrams, notes, and maps learners create while exploring domains
- **Reflective Checkpoints**: Documented goal interrogation sessions with advisors
- **Resonance Traces**: Explicit connections learners draw between domains
- **Scale Movements**: Records of learners moving between micro-details and macro-patterns

### 4.3 Testable Hypotheses

We have developed a set of testable hypotheses aligned with workforce frameworks such as NICE [3], providing concrete intervention designs. *Example*: "Learners using AI-assisted Resonance identification will demonstrate 40% faster Subset economy transitions (career pivots) compared to control groups, as measured by time to first independent contribution in new domains."

---

## 5. Design Implications for GenAI TfT

### 5.1 Design Strategies by Economy

**For Breadth**: Design parallel learning threads with AI maintaining coherence across domains. Avoid collapsing to single-domain depth prematurely.

**For Depth**: Use AI to identify and remove bottlenecks while preserving desirable friction that supports deep understanding.

**For Subset**: Surface transferable patterns between domains. Make Resonance visible to learners.

**For Superset**: Enable cross-domain synthesis views. Support "what-if" explorations of field reinvention.

**For Network-form**: Provide multi-scale navigation interfaces. Connect granular details to systemic patterns dynamically.

### 5.2 Preserving Cognitive Engagement

TfT design must balance efficiency gains against cognitive engagement. We propose that AI should:

- **Accelerate** navigation but not replace it
- **Suggest** patterns but require learner validation
- **Track** intermediary artefacts rather than skip them
- **Support** the reflective advisor loop rather than substitute for it

### 5.3 Avoiding Cognitive Erosion

The framework highlights risks when AI "short-circuits" valuable cognitive processes:

- Bypassing Resonance development by providing direct answers
- Collapsing multi-scale navigation to single-scale responses
- Eliminating intermediary artefacts that scaffold understanding

---

## 6. Discussion and Future Work

### 6.1 Limitations

The Learning Economies framework requires empirical validation in HCI contexts. We propose the framework and metrics as a basis for such work; we do not yet report controlled studies. Metrics proposed here draw from educational and workforce development applications; adaptation for TfT evaluation may reveal additional dimensions. A comprehensive metrics map and literature-grounded rationale are documented in this repository (metrics-map-learning-economies.md and metrics-literature-sources.md in CHI-2026) for exhaustive search and validation.

### 6.2 Research Agenda

We propose collaborative work on:

1. Empirical studies measuring the five economies in TfT contexts
2. Design patterns for economy-specific TfT interfaces
3. Longitudinal studies of Resonance development with AI assistance
4. Evaluation of reflective advisor loops in AI-augmented learning

### 6.3 Scope and Applicability Across Learning Levels

The five economies apply across learning levels: doctoral and research contexts emphasize Depth, Superset, and Network-form; skilled R&D and vocational practice emphasize Subset and Depth; K–12 and early education emphasize Breadth and Depth with scaffolding. The framework thus offers a lens for the future of learning at all levels. It also reframes what "gifted" education may mean: rather than single-axis depth or speed, giftedness in AI-augmented learning may increasingly denote *multi-economy fluency*—the ability to navigate fluidly across Breadth, Depth, Subset, Superset, and Network-form and to leverage Resonance across domains.

### 6.4 Broader Implications

As AI accelerates all five Learning Economies simultaneously, success depends not on optimizing within any single mode but on fluid navigation across the entire system. The individuals, educators, and institutions that master this unified approach will define the landscape of AI-augmented learning.

---

## 7. Conclusion

We have presented Learning Economies as a framework for defining and measuring cognitive outcomes in AI-augmented learning. The five economies—Breadth, Depth, Subset, Superset, and Network-form—provide distinct, measurable dimensions of TfT effectiveness. The reflective advisor loop positions educators as essential navigational guides. Together, these contributions offer HCI researchers concrete strategies for evaluating and designing GenAI tools for thought.

---

## References

[1] Workshop proposal: "Tools for Thought with Generative AI 2026"

[2] Jones, Z. & Franolich, J. (2025). AI and Learning Economics: Five Economies of Human Capital in the AI Era. GuildCon 2025.

[3] NIST Special Publication 800-181: Workforce Framework for Cybersecurity (NICE Framework)

[4] Engelbart, D. C. (1962). Augmenting Human Intellect: A Conceptual Framework. Stanford Research Institute.

[5] Kay, A., & Goldberg, A. (1977). Personal dynamic media. Computer, 10(3), 31-41.

[6] Azevedo, R., & Aleven, V. (Eds.). (2013). International Handbook of Metacognition and Learning Technologies. Springer.

---

*Word count: ~1,850 (target: ~1,800-2,000 for 4 pages in ACM format)*
