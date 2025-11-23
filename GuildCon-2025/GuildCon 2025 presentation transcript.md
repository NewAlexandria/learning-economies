# Introduction

Our collaboration began with some AI work I was doing, followed by the educator work that John has been doing. We called this **learning economies**. You'll see why in a moment. We're trying to picture how AI might reshape education, especially in cybersecurity, and what that could mean for us and our learning.

We also consider how we teach and communicate these ideas, and we hope to impact education more broadly. That's the direction of our thinking - a very current topic: what will AI do to education? This is a first attempt at answering that.

You're probably familiar with NIST 80181, the cyber‑workforce training cycle, which ties into our discussion.

Here's a quick overview for those thinking about the big picture. We'll explore the basis of a learning economy - a term we're coining. We'll discuss the future of things, guides for educators, policy, implementation, and related outcomes.

---

## Origin Story

Presenter: There was a point, as I've been working with LLMs, where I noticed a pattern that was part of an optimization for using LLMs. It stemmed from the actual structure of LLMs themselves and sparked my curiosity about their architecture.

I built an **ontology hydration framework** - a way to gather many bodies of knowledge and unify them. It pulls from documents, extracts their ontologies, or draws from existing frameworks, and then stitches everything together.

If anyone has used Palantir AIP, it aims to support similar functionality. Along the way, I also built a **cyber‑asset categorization system** across OT, IT, and governance, unifying many ontologies to discover assets across logs and other sources.

What I found was that the ontology framework, when applied to LLMs, caused hallucinations - especially around events and net‑flow information that were transient and not true asset representations. The model kept inventing concepts related to net‑flow and other things.

This conflicted with the goal of asset discovery. I realized the LLMs were intrinsically trained on those concepts so closely - via embeddings - that they struggled to differentiate, leading to conflated concepts.

I wanted to build an **asset system**, not a net‑flow system. Instead, I created a kind of 'data sink' - a target resembling a **sacrificial anode or cathode** (if you’re familiar with those concepts). The system kept net‑flow concepts separate, allowing the LLM to add related data only when appropriate, while preserving the distinct assets I was trying to discover.

Working with the LLM architecture in this way yielded higher‑quality output and reduced hallucination.  I was 'going with the grain.'

Along the way, I wondered: **Would this influence how we use LLMs for education, curriculum material, and similar applications?** That question forms the basis of where this project is heading.

---

## Quick slide about LLM architecture

Presenter: For those unfamiliar, you probably won’t dive hyper‑deep, but we’ll cover the large‑level concepts.

LLMs are built around **addressing** - where data is located or referenced within the system. There’s also a **compression** concept, dealing with tokenization and how the model leaps across different addresses to form shorter routes.

All these concepts remain, but you can make foreshortened jumps, plus routing. How are concepts linked based on where you are in the structure? As you go deeper in the chain, are you still close to other concepts?

It’s similar to **web routing**. Imagine every website about dogs; they’d all be close together in the same IP address space. That metaphor illustrates how LLMs route information.

**Temperature** determines whether a lookup can be fuzzy, returning nearby information, or whether it returns only the exact match.

**Stabilization** (a meta‑concept) concerns how, as new data is retrained or filtered into the system, it aligns with existing information.

**Transformers** resemble the compression idea; they let the model jump from one place to many others. There are also **non‑linearities** in structures that fall outside typical tree‑type routing.

These concepts will be unpacked later, but they’re useful to review as we consider what learning economies could achieve.

---

Presenter: And again — we’ll get to what a learning economy is here. At this point we can consider various routings and other aspects, such as the economics and efficiencies of how these models work. I want to highlight a few of those and think about whether they influence education — how we learn and how we teach. That lets us draw parallels to classic education concepts like breadth versus depth, and subsets versus supersets.

Presenter: In terms of breadth, think of parallel domains — getting multiple degrees at the same time. In high school we are forced to learn all domains at a roughly equal level, achieving broad competency across subjects. Undergraduates face similar expectations, though with less pressure. As we progress to master’s and PhD programs we narrow our focus, diving deeper into a specific topic and forgoing breadth because it becomes inefficient.

Presenter: Depth, exemplified by a PhD, involves rapidly learning at the edge of a domain, discovering new findings, and expanding the field. Subsets correspond to vocational training: a specific cluster of information within a field that is crucial for practice. In vocational settings there are many modules of information that we continually learn and stack together.

Presenter: For those who aren’t familiar with academic structure: undergraduate is broad; degrees become more focused through master’s and PhD programs. For example, cybersecurity at undergrad can be broad, while a PhD will be very specific to a narrow subset of cybersecurity. What we’re getting at is how LLMs inherently lend themselves to multiple domains and parallel learning.

Presenter: Cybersecurity is a useful example because it’s inherently multidisciplinary. It has many specialties and vocational areas, and practitioners often move across those areas as they gain knowledge. It’s a hyper-example of many of these learning economies.

Audience (question): Your question? I’m just trying to understand what you mean by “learning economy.” I’m not sure I’m feeling it.

Presenter: Sure. The reason we call it an economy is that there’s an economics — or efficiencies — to the learning process itself. Are you learning multiple things in parallel and keeping them synthesized because they relate to each other, or are you hyper-focused and blasting into depth as quickly as possible? Those are different learning economies.

Presenter: Similarly, if you’re learning a particular module to practice a trade, you’re refining that trade. The economics here are more like physics of cognition than monetary economics. Think of work roles: malware analyst, network engineer, SOC analyst. If you learn all subjects in parallel, you might not need separate specialists — you could be expert across hosts, networks, crypto, and malware. Is that the kind of question you were asking?

Audience: So the term “learning economy” — is it the four frameworks of how to approach the learning process? Breadth, depth, subset, superset?

Presenter: Yes. Also think of it as a cognitive economy: different neurotypes and learning preferences present different learning economies. Visual learners, auditory learners — these are dimensions, but the model we’re presenting here looks more at parallels between how LLMs work and human education.

Presenter: The presumption is that LLMs present information in ways aligned with their architecture. If we can find cognitive processes that align with that tooling, we can accelerate learning and change industry practices. That raises questions: How will education change with AI tooling? How will the workforce, hiring, and evaluation change if tooling accelerates what learning even means?

Presenter: One speculation is that a breadth-based economy might lead to people learning in parallel — like double majors becoming more common, even triple or quadruple majors. Some people might pursue double master’s-type blends across fields because tooling makes it practical.

Presenter: In cybersecurity research, people already blend fields — they build advanced tools to get analytics and synthesize knowledge across domains. We may see more of that as tooling and capacities expand.

Presenter: Regarding the depth economy: how quickly can someone reach the edge of a field (e.g., PhD-level novelty)? How many papers are required, what is the real innovation, and how fast can you get there? Those questions vary by topic and motivation.

Presenter: Regarding vocational subsets, vocational retraining and workforce development are major priorities — for example, in Pennsylvania there’s a strong focus on workforce development, vocational retraining, and building new infrastructure over the next five-plus years. That raises questions about switching vocational practices and transferring information between domains.

Presenter: Institutions like Arizona State University have been experimenting with modular educational practices that let you assemble modules into degrees or vocational competencies. These examples show that modular, tool-supported learning economies are already emerging.

Audience (interruption): Good question — sorry, I missed it for a second.

Presenter: No worries. The slides are online if you know where to search; we can share them later. Sorry — we didn’t make a QR code. (We don’t trust QR. But we should have.)

Presenter: The superset economy is broad and varied, so we’ll talk about it less. The examples in the slides are intended to illustrate representative ideas. Historically, technological advances — artisanal weaving to looms to automated carbon fiber machinery, or darkroom photography to photolithography for microchips — show how vocational modules migrate between fields. LLMs are particularly good at projecting analogies across fields, which might let people find new industry opportunities and innovations that used to take decades.

Audience: When you say LLMs inherently enhance learning, is that because the data is vectorized?

Presenter: Vectorization is part of it. Vectorization across fields of knowledge enables us to see comparisons and analogies. Open-source science tries to use LLMs to discover new things; the human brain is still crucial, but LLMs add another tool. The superset concept looks for historic economic patterns and how GPT-style transformations might map patterns from one scale to another.

Presenter: There could be cybersecurity attack patterns, new instrumentation, or electromagnetic vectors we didn’t think of — crossing domains quickly. For education, LLMs can look across patterns and reveal links that previously took decades to find; we might see similar discoveries happen in a year or two.

Presenter: In a simple example: in incident investigation you have host artifacts and network artifacts with overlap. An LLM aware of those overlaps can teach someone in parallel so they learn faster.

Presenter: The broader point is: if LLM tools have a particular architecture, how can we work with that to accelerate learning? If they conflict with human cognitive patterns, what should we change to avoid degrading human thinking and maintain good cognitive alignment?

Presenter: Beyond education, labor markets will change, people will shift competencies differently, and definitions of human capital will evolve. We might design KPIs around velocity of learning. These are broad policy questions institutions must confront, and educators will need to orchestrate learning processes focused on efficiencies of learning — not monetary economics, but cognitive efficiency.

Presenter: If students approach extreme breadth or depth, it’s unlikely that any single local educator will have all the knowledge they need. So education will become about orchestrating and supporting learners to meet goals and outcomes. That leads into what a training kit for educators could look like.

Presenter: The industry will likely manage AI agents. Just like junior employees, you’ll manage AI agents. Administrators will need to think about supporting educators and their people. This problem scales up, and administrators who know institutional processes will recognize these concepts.

Audience (question): So administrators being managers of AI agents — doesn’t that introduce bias? If educators orchestrate learning, aren’t they pointing AI in certain directions?

Presenter: Yes, that raises ethical concerns. LLMs have biases that influence outcomes. Standards bodies like NIST will likely produce frameworks to guide neutral, unbiased outcomes. Part of classroom practice will be refining learning targets and ensuring tooling and processes support correct goals and measurement standards.

Presenter: At the AI security conference I attended, vendors including Microsoft are building safety tools that include bias considerations. Many big vendors include bias mitigation in their frameworks — they call it “safety.” Safety layers act as guardrails in AI Ops tools (e.g., for auto PR review), with configurability to constrain what an LLM does.

Audience: I’m not a big believer in absolute neutrality. If you claim neutrality, you might be hiding biases. So how do we decide on standards? Who agrees on what neutral is?

Presenter: That question goes to the epistemology of measurement — how do we take measurements and define baselines? The goal is to measure from enough different angles to generate a centroid that works reasonably for stakeholders. Human-in-the-loop bias checks remain essential.

Audience (follow-up): Where does chain of thought and tree-of-thought factor in? Will another agent monitor bias, or will the chain-of-thought be exposed and checked?

Presenter: Chain-of-thought is the notion of exposing reasoning traces so users can see how an LLM arrived at an answer. Chain-of-reasoning and these “chain” concepts are active areas of development for AI–human collaboration. We will inspect chains, inject thoughts, edit them, and record edits like version control. That visibility and editability seems inevitable.

Audience (Annie): I want to add — I don’t think AI can ever be perfect. I can have two SOC teams with similar backgrounds and tooling, and they’ll handle incidents differently; their reports will differ. The challenge is whether you get to the right answer. We don’t expect perfection from humans; why expect it from machines?

Presenter: Exactly. Show your methods and reasoning. Humans still need to evaluate bias and correctness. Critical thinking remains crucial; in my classes I emphasize examining methods and thinking processes. When we interview people, we ask them to show their thinking and action processes — that matters as much as the objective output from tooling.

Presenter: There was a slide about NIST 8018 — the cyber workforce assessment — which breaks down roles and what’s needed for each job. We can use that as part of measurements for the security field in our model.

## Call to Action

Presenter: That builds toward what a training kit could look like for educators. In our discussion, we’ll anchor on cybersecurity because it’s our context, but the model could be general. What could a training kit include? Typical elements: student profiles, attunement processes aligning student goals, class goals, and institutional goals, and evidence of outcomes.

Presenter: Institutions should align to industry so graduates can get jobs. Instructors should show progress, demonstrate that students achieved intended outcomes, and measure and show proof. The training kit would support that, and it should integrate naturally with other tools educators use — research notebooks, LMSs, etc. — so it doesn’t create an exclusive, locked-down domain.

Presenter: If people learn across many fields simultaneously or go deeply rapidly because tooling enables that, measurement methods need to think beyond NIST 181-type frameworks. We should consider measurement methods relative to the degree of acceleration AI tools afford.

Presenter: There are two camps of instructors: those who avoid AI and those who embrace it. The kit should lower the bar and make facilitation easy, with models trained in the background and integrations to other systems.

Presenter: As a disclaimer: I use AI every day and I think it’s great. But there are concerns about cognitive offloading — the classic calculator argument: people lose certain mental skills. Is that a risk here?

Audience (question): I worry about cognitive offloading. If people use AI for answers instead of engaging sources, where will the balance go?

Presenter: That’s a fair concern. We’re all taking educated guesses — this is new. One approach is to make critical thinking and source-testing explicit learning domains. Teach students to test and validate AI outputs. Making evaluation a taught and assessed skill helps preserve research and synthesis abilities.

Presenter: I studied human-computer interaction and cognitive models of encoding information. There’s an interesting mnemonic concept called the method of loci — the memory palace. It’s about spatial encoding of information; language and spatial cognition are tightly linked. Sherlock Holmes, in Conan Doyle’s stories, used a form of memory palace.

Presenter: My assertion is that language models currently miss an important aspect of the method of loci and spatial cognition. My work on an ontology hydration framework tries to address that gap. Visualization and spatial techniques could help LLMs pack information in a way that aligns with memory palaces in human cognition, supporting agentic learning.

Presenter: The other slides outline what a toolkit might look like and how it supports educators — initial assessment, pilot programs, scaling, success metrics. We have metrics in the repo and will expand them. Are these different economies truly different structures, or are they trade-offs like a capacity principle relative to cognition? We aim to turn those questions into measurable metrics and feed that back into an open-source education process.

Presenter: We have basic warning signs for instructors to identify when a student struggles or excels. The slides list Gen-AI technologies that enable immersive learning and adaptive, personalized education scenarios — not just content consumption but tools adapted to what people actually do.

Presenter: Different students learn differently: some learn by listening, some visually. If there are other educators listening, this is a call to action — we’d love to engage and collaborate, and we plan to take next steps toward formal educator and educational measurement conferences.

Presenter: Any other questions before we wrap?

⸻

## Q&A

(audience questions after the presentation)

Audience: I just got a notification about California trying to implement AI in the mathematics curriculum. Do you have any insight into how they’re doing that?

Presenter: I’m not aware of the specifics, but I’d love to read about it. Sounds like a big change. If anyone has details, please share — I’m surprised and interested.

Audience: What’s your website? Can I look at this material?

Presenter: The materials are on a GitHub repo. My username is new Alexandria — that’s also the guild username and the repo name for learning-economies. You can find me most places under that handle and find the repo there.

Audience (follow-up about California math standards): How will non-deterministic AI interactions affect standardized metrics? If students learn via non-deterministic frameworks, how do we benchmark mastery?

Presenter: Good question. Standardized metrics are already less uniform than they appear. Information can be presented in different ways, but there are local centroids around standardized topics. Models — for example, a RAG (retrieval-augmented generation) system — could ingest canonical curriculum materials so the model is aware of specific content. That lets different students learn via different instructors or books while still measuring against common objectives. We can standardize by ensuring the model and evaluation frameworks align to curricular objectives.

Audience: That’s not how I learned. I’d grab a book and learn independently. LLMs reflect the ways we represent knowledge, not necessarily traditional teaching methods.

Audience: Where do hallucinations factor into time-to-learn? Is there a cognitive penalty when an AI hallucinates and then you correct it?

Presenter: My hope is that, as we build more granular centroids around fields of knowledge — the components that make up a degree program — we’ll see a de-hallucination process similar to what I observed with the ontology hydration framework I built. If you have better-addressing models (the addressing meaning how knowledge items are linked), hallucinations decrease. Smaller edge models tailored for specific outcomes can capture hallucination-prone content and present it as options rather than facts. The remaining knowledge targets remain clearly separated, so you can distinguish between true discoveries and hallucinations. We’ll always push beyond current frameworks, but better tooling and model design can minimize cognitive penalty.

