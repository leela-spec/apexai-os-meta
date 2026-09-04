---
type: Handover
title: M06 — Decision Elicitation & Trade Studies
description: Bounded research handover for structured operator decisions, grounded options, uncertainty, and transparent trade-offs without pseudo-precision.
status: research_handover
created: 2026-09-04
---

# M06 — Decision Elicitation & Trade Studies

## Purpose

Standardize how an AI helps the operator resolve material choices.

## Operator intent

Useful Q&A should present the exact question, grounded options, practical examples, impact/evidence/risk, a recommendation, and concise rejection notes.

The current `(I/E/R)` formula is a candidate local heuristic, not validated doctrine.

## Existing repo sources

Read only:

- `apex-meta/AI-Snippets/Snippets.md` Q&A and REI sections
- `apex-meta/handoff/universal-ai-instruction-system/01-MODULE-MAP.md`
- `apex-meta/handoff/universal-ai-instruction-system/03-EVALUATION-PLAN.md`

## Research questions

1. Which established approaches best map to the operator need: trade studies, decision analysis, MCDA, weighted decision matrices, ADR/RFC records, or another method?
2. When are numeric scores useful versus misleading?
3. Should impact/evidence/risk remain separate dimensions?
4. If REI remains, how should its formula, anchors, and interpretation change?
5. How should uncertainty and sensitivity to subjective weights be shown?
6. How many options are usually useful before choice overload appears?
7. Which decisions should be elicited from the operator versus inferred from evidence?

## Required outputs

1. Established-concept map.
2. Comparison of 2–5 decision formats.
3. Verdict on REI: retain, revise, rename as local heuristic, or replace.
4. Recommended 1–4 sentence snippet.
5. Trigger/depth rule.
6. Focused decision method.
7. Failure modes: false precision, option spam, weak grounding, hidden value judgments.
8. Simple/medium/complex examples.
9. Evaluation prompts including sensitivity tests.
10. Boundaries with M07 and authorization policy.

## Constraint

Do not present subjective numerical estimates as measured facts. Do not use a matrix when a direct recommendation is sufficient.
