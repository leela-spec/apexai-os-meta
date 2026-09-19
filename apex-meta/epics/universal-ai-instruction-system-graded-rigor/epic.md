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
  - default_grounding_is_not_an_intensity_question
  - baseline_a13_is_normal_web_search_plus_three_verified_quality_sources
  - graded_approach_applies_only_when_more_rigor_is_needed
  - do_not_invent_numeric_intensity_levels_without_evidence
---

# Universal AI Instruction System — Graded Rigor / Rule Intensity

## Goal

Keep one explicit unresolved project-management question:

> **How should the system scale the intensity of multiple rules when ordinary execution is not enough, without each rule inventing its own ad hoc intensity scale?**

This question is **separate from A13's baseline grounding rule**.

## Baseline now fixed for A13

A13 normal behavior is:

```text
actual frame + problem + task + environment
        ↓
normal web search for established best practice
        ↓
>= 3 verified-quality sources
        ↓
congruence check
        ↓
reason from evidence and proceed
```

This is normal grounding, not an elevated research mode.

The exact number three is an operator-selected minimum floor, supported by established multi-source/lateral-verification practice but not claimed to be a universal AI industry standard.

## When intensity becomes an open question

Increase rigor only when ordinary execution exposes a reason:

- materially complex task or environment;
- reliable sources materially disagree;
- local environment contradicts generic guidance;
- high consequence of error;
- unresolved evidence gaps could change the result;
- verification/review requires more effort than the normal baseline.

For A13 specifically:

```text
baseline sources congruent
  -> proceed

sources incongruent / task materially complex
  -> expand research proportionately
  -> surface the disagreement or uncertainty
```

Do **not** equate escalation with a specific product such as Deep Research.

## Established concept retained: graded approach

NASA/IAEA-style **graded approach** remains a useful established concept for the unresolved cross-rule problem:

> keep the requirement in force, but increase the scope/depth/rigor of its application when complexity, uncertainty, risk, or consequences justify it.

For A13, this means:

- the grounding requirement stays in force;
- only the **amount of additional research** changes when baseline evidence is insufficient.

For other modules it could eventually mean:

- A04: more decomposition/review;
- A08: stronger evidence checks;
- A10: stricter recovery safeguards;
- A12: more explicit caveats/decision visibility;
- C01: deeper trade-off analysis;
- C02: more extensive research procedure.

## Open design questions

Do not answer these by inventing a local scale yet:

1. Should one cross-cutting graded-rigor rule govern all modules?
2. Which common factors should increase rigor?
3. Can modules inherit the same escalation decision rather than independently calculating intensity?
4. Should intensity remain qualitative, or are a few named modes useful?
5. What observable stop condition prevents escalation from becoming over-engineering?
6. How should a rule report that it escalated rigor and why?
7. Which behaviors are absolute invariants versus intensity-sensitive implementation details?

## External precedents

### OpenAI

OpenAI guidance supports:
- web research over assumptions;
- citations for web-derived information;
- resolving contradictions;
- ordinary search as normal factual grounding.

Source:
https://developers.openai.com/api/docs/guides/latest-model?model=gpt-5.2

### Google

Gemini's normal grounding flow can execute one or multiple searches and synthesize cited evidence automatically.

Source:
https://ai.google.dev/gemini-api/docs/google-search

### Stanford lateral reading

Stanford teaches verification by checking what multiple trusted sources say and suggests finding four or five other sources.

Source:
https://sml.stanford.edu/digital-strength/digital-strength-tools-training

### CDC

CDC says source selection should fit the actual question/purpose, multiple data sources can increase credibility, and quantity/quality should be sufficient without unnecessary burden.

Source:
https://www.cdc.gov/evaluation/php/evaluation-framework-action-guide/step-4-gather-credible-evidence.html

### NASA / IAEA graded approach

Retain as the primary established precedent for **how rigor increases when baseline practice is insufficient**, not as the baseline research method itself.

## Current hypothesis to test later

```text
BASELINE RULES
stay simple and explicit

IF complexity / disagreement / consequence rises
    ↓
ONE shared graded-approach decision
    ↓
relevant modules increase rigor proportionately
    ↓
stop when evidence/process is sufficient for the task
```

No L1/L2/L3 scheme is authorized yet.

## Preserved original graded-rigor research

Commit `9a165f92f62f4ed18862995652f2cf3ee3d140fb` simplified this epic and removed the detailed comparison material. The current baseline/escalation distinction remains authoritative, but the original research is recoverable exactly from:

```bash
git show 571717fc2933d625d3ec2b8e7976387787d722c5:apex-meta/epics/universal-ai-instruction-system-graded-rigor/epic.md
```

That snapshot preserves the original open questions; OpenAI research-depth comparison; NASA and IAEA Graded Approach research; NIST tier comparison; FDA risk-based assurance evidence; original fit scores; provisional cross-rule synthesis; decisions deliberately left open; and eight acceptance questions.

Treat it as **historical research input**, not as a competing current design.
