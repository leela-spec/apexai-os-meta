---
title: "Universal AI Instruction System — Graded Rigor / Rule Intensity"
status: open
priority: high
due_date: null
created_date: 2026-09-19
updated_date: 2026-09-19
source:
  - "apex-meta/handoff/universal-ai-instruction-system/README.md"
  - "apex-meta/handoff/universal-ai-instruction-system/module-deepening/A13-external-grounding-real-world-verification/README.md"
review_flags:
  - do_not_invent_custom_intensity_levels_before_testing_established_graded_approaches
  - intensity_is_cross_cutting_and_should_not_be_reimplemented_independently_in_every_rule
  - grounding_should_remain_default_while_research_depth_is_graded
  - multi_source_triangulation_is_an_escalation_not_a_universal_extra_step
---

# Universal AI Instruction System — Graded Rigor / Rule Intensity

## Goal

Resolve how the Universal AI Instruction System should scale the **depth, rigor, verification, research, review, decomposition, and communication intensity** of its rules across tasks without creating a separate ad hoc intensity mechanism inside every module.

The desired outcome is not another custom framework. The project should reuse an established **graded / risk-informed / tailored approach** if one fits.

## Open question

> **How should one cross-cutting intensity mechanism govern the rigor of many Universal AI Instruction System rules so that simple work stays light, normal factual work gets dependable grounding by default, and higher-stakes / more complex / uncertain work automatically receives deeper research, verification, testing, review, or documentation — without every rule inventing its own levels?**

Sub-questions:

1. Should there be one central **graded-rigor / intensity policy** that other modules inherit?
2. Which factors should change intensity:
   - consequence / stakes;
   - complexity;
   - uncertainty;
   - reversibility;
   - external dependence;
   - environment specificity;
   - disagreement / source conflict;
   - novelty;
   - cost of error?
3. Should the system use:
   - named levels;
   - qualitative routing only;
   - risk/complexity thresholds;
   - or a small number of established operational modes?
4. How should the mechanism avoid false precision such as arbitrary 1–10 scores?
5. How should this interact with:
   - A04 workflow depth;
   - A08 evidence quality;
   - A10 recovery;
   - A12 communication detail;
   - A13 grounding;
   - C01 decision rigor;
   - C02 research depth;
   - future authority / side-effect controls?
6. Can multiple modules share the same intensity decision rather than independently deciding how much rigor to apply?

## Immediate correction to A13 interpretation

Do **not** treat “multi-source triangulation” as a mandatory extra stage after every grounding event.

Current OpenAI product guidance already distinguishes:

- **Search** — quick retrieval of specific/current facts or documents with citations;
- **Deep Research** — multi-step investigation, source evaluation, synthesis across multiple sources, and more extensive reporting.

Therefore the more established interpretation is:

```text
GROUNDING = default when outside facts affect correctness

ordinary / bounded factual need
  -> Search / authoritative source lookup
  -> reason over the returned evidence

complex / ambiguous / contested / strategic / high-stakes need
  -> escalate research depth
  -> Deep Research / broader source comparison / explicit triangulation
```

The unresolved problem is therefore **research/verification intensity**, not whether every answer needs a special “triangulation step.”

## Established approaches found

### 1. OpenAI Search vs Deep Research — AI-native operational depth split

OpenAI explicitly distinguishes Search from Deep Research:

- Search is for quickly retrieving specific facts, documents, and recent information.
- Deep Research is for multi-step, in-depth questions that require combining and analyzing information from multiple sources.
- OpenAI Academy describes Search as fast orientation and Deep Research as the deeper path for complex questions.

This is already a practical **two-level research-intensity mechanism**.

Primary sources:

- https://openai.com/academy/search-and-deep-research/
- https://help.openai.com/en/articles/10500283-deep-research-faq
- https://openai.com/academy/research/

### 2. NASA — Graded Approach

NASA defines a **Graded Approach** as applying risk-management processes at a level of detail and rigor that adds value without unnecessary resource expenditure.

NASA's current risk-management language says the resources and depth of analysis should be **commensurate with the stakes and complexity of the decision situation**.

NASA systems engineering also uses **tailoring/customizing** so process implementation varies with:

- size;
- complexity;
- acceptable risk;
- failure consequences;
- human involvement;
- security;
- longevity;
- cost/schedule constraints;
- safety/mission assurance.

This is highly relevant because it solves the same abstract problem:

> keep the requirement/invariant, vary the rigor of its implementation.

Primary sources:

- https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_8000_004C_&page_name=AppendixA
- https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_7123_001D_&page_name=Chapter2
- https://ntrs.nasa.gov/api/citations/20240014019/downloads/SP-20240014019.pdf

### 3. IAEA — Graded Approach

IAEA safety standards use a formal **graded approach** where the stringency of controls, analysis, documentation, and actions is commensurate with:

- risk;
- likelihood and consequences;
- significance;
- complexity;
- characteristics of the activity/system.

Important architectural lesson:

> The requirement itself stays in force; the **scope, depth, and rigor of application** are graded.

This closely matches the Universal AI Instruction System problem better than inventing independent intensity levels inside each rule.

Primary sources:

- https://nucleus.iaea.org/sites/nss-oui/Published%20Collections/m_3761d926-c16f-4477-a63b-741a9db1c16c/m_3761d926-c16f-4477-a63b-741a9db1c16c__50_0.Html
- https://www.iaea.org/publications/14734/application-of-the-graded-approach-to-post-closure-safety-assessment-for-the-disposal-of-disused-sealed-radioactive-sources-in-boreholes

### 4. NIST CSF 2.0 — Tiers of rigor

NIST CSF 2.0 uses four Tiers to characterize increasing rigor of cybersecurity risk-governance and risk-management practices:

1. Partial
2. Risk Informed
3. Repeatable
4. Adaptive

This proves that **explicit rigor tiers are an established pattern**, but these tiers describe organizational maturity rather than per-task execution depth.

Therefore NIST Tiers are useful evidence for the concept of graded rigor but are **not an obvious drop-in task-intensity mechanism** for this project.

Primary sources:

- https://csrc.nist.gov/pubs/sp/1302/final
- https://csrc.nist.gov/glossary/term/csf_tier

### 5. FDA — Risk-based software assurance

FDA's 2026 Computer Software Assurance guidance explicitly uses a **risk-based approach** to determine where additional rigor is appropriate and which testing/assurance activities are needed.

This is another mature example of keeping the objective fixed while scaling verification rigor to risk.

Primary source:

- https://www.fda.gov/regulatory-information/search-fda-guidance-documents/computer-software-assurance-production-and-quality-management-system-software

## Fit assessment

Scores below are project-fit judgments, not empirical probabilities.

| Existing approach | Fit to cross-rule intensity | Evidence maturity | Risk of misapplication | Notes |
|---|---:|---:|---:|---|
| **NASA Graded Approach** | **98/100** | **98/100** | **12/100** | Closest semantic fit: rigor/depth commensurate with stakes + complexity without needless resource use. |
| **IAEA Graded Approach** | **96/100** | **100/100** | **18/100** | Extremely mature; same core concept, though safety context is much higher-stakes than ordinary AI work. |
| **OpenAI Search ↔ Deep Research** | **97/100 for research intensity** | **97/100** | **10/100** | Direct AI-native implementation pattern, but only covers research depth rather than all rules. |
| **NASA SE tailoring/customizing** | **94/100** | **98/100** | **16/100** | Strong model for preserving intent while changing implementation depth. |
| **FDA risk-based assurance** | **86/100** | **96/100** | **20/100** | Strong for testing/verification intensity; narrower than whole-agent behavior. |
| **NIST CSF Tiers** | **58/100** | **99/100** | **42/100** | Established rigor tiers, but they model organizational maturity, not per-task rigor. |

## Provisional synthesis — not yet a design decision

The strongest existing pattern is **not** “every rule has its own intensity levels.”

It is:

```text
UNIVERSAL INVARIANT / REQUIREMENT
        +
ONE GRADED-APPROACH / TAILORING DECISION
        ↓
depth / rigor / evidence / review scaled to
stakes + complexity + uncertainty + consequences
```

For research specifically, OpenAI already supplies a practical operational realization:

```text
Search
  -> bounded / specific / fast grounding

Deep Research
  -> multi-step / comparative / ambiguous / source-heavy work
```

A future design should test whether the Universal AI Instruction System can use **one cross-cutting graded-rigor mechanism** and let individual modules declare only what changes with rigor, instead of independently inventing trigger levels.

## Decision deliberately left open

Do **not** yet introduce:

- L1/L2/L3/L4;
- 1–10 intensity scores;
- per-module risk matrices;
- automatic “triangulation required” rules;
- a new custom grading algorithm.

First compare the established graded-approach patterns against representative Universal AI Instruction System tasks.

## Acceptance questions for later synthesis

A candidate intensity mechanism should only be accepted if it can answer, with low prompt/context overhead:

1. What makes this task require more rigor?
2. Which rules become deeper as rigor rises?
3. What stays mandatory regardless of intensity?
4. What additional work is activated at higher intensity?
5. What observable condition lets the agent stop escalating?
6. Can the same mechanism govern research, verification, planning, review, recovery, communication, and decision analysis?
7. Does it reduce both:
   - under-processing of consequential tasks;
   - over-engineering of simple tasks?
8. Does it reuse an established graded/tailored approach rather than rebranding a custom local invention?

## Current working hypothesis to test

> **Adopt the established “graded approach” concept as the cross-cutting intensity model, with OpenAI Search vs Deep Research as the AI-native research-specific realization.**

This is a research hypothesis, **not yet canonical architecture**.
