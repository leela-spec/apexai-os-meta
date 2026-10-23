---
type: Handover
title: M03 — Context Management
description: Bounded research handover for high-signal, just-in-time context behavior without duplicating Apex Informatics.
status: research_handover
created: 2026-09-04
---

# M03 — Context Management

## Purpose

Standardize how an AI keeps working context small, relevant, and coherent across larger tasks.

## Operator intent

Avoid context bloat. Load only what matters now. Preserve long-horizon coherence through concise durable summaries rather than full-context carryover.

## Existing repo sources

Read only:

- `apex-meta/informatics/standard.md` sections on progressive disclosure and scoping
- `apex-meta/informatics/MMM/working-method.md` context rule
- `apex-meta/handoff/universal-ai-instruction-system/00-ARCHITECTURE-DECISION.md`
- `apex-meta/handoff/universal-ai-instruction-system/01-MODULE-MAP.md`

## Research questions

1. What current context-engineering practices are established across agent systems?
2. Which behaviors belong in universal agent guidance versus Informatics document architecture?
3. When should an AI retrieve JIT, compact, isolate context, or split work?
4. What minimal durable summary should survive between bounded contexts?
5. What failure modes come from over-aggressive compaction or insufficient context?
6. How should agents choose which references not to load?

## Required outputs

1. Established-concept map.
2. Candidate comparison.
3. Recommended 1–4 sentence snippet.
4. Trigger/depth rule.
5. Focused context method referencing, not restating, Informatics.
6. Failure modes.
7. Simple/medium/large examples.
8. Evaluation prompts measuring task quality and context footprint.
9. Boundaries with Informatics, M02, and M04.
10. Integration proposal.

## Constraint

Do not rewrite the five-plane Informatics architecture or create a new memory/state subsystem.
