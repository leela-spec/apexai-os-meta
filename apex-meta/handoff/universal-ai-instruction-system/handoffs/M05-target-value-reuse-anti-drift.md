---
type: Handover
title: M05 — Target, Value, Reuse & Anti-Drift
description: Bounded research handover for keeping execution tied to the requested outcome while preferring proven reuse before custom invention.
status: research_handover
created: 2026-09-04
---

# M05 — Target, Value, Reuse & Anti-Drift

## Purpose

Standardize outcome-focused behavior that resists process drift, unnecessary infrastructure, and unsupported custom invention.

## Operator intent

The agent should pursue the shortest credible path to the actual user-facing target. Existing proven systems should be tried before new abstractions are invented. Corrections should be challenged when they are not required to test or safely deliver the real target.

## Existing repo sources

Read only:

- `apex-meta/AI-Snippets/Snippets.md` anti-drift/minimalism sections
- `apex-meta/handoff/universal-ai-instruction-system/00-ARCHITECTURE-DECISION.md`
- `apex-meta/handoff/universal-ai-instruction-system/01-MODULE-MAP.md`

The referenced `SnippetDocs/AnitOverEng.md` was not found on `main` during the orchestrator run. Do not invent its contents.

## Research questions

1. Which established concepts best express the operator's need: YAGNI, KISS, Lean waste/value, vertical slices, walking skeletons, tracer bullets, Theory of Constraints, risk-based assurance, or another method?
2. How should `reuse before build` be stated without forbidding justified custom integration?
3. When should an AI stop repairing a failing subsystem and reconsider it?
4. How should the operator challenge rule be phrased without suppressing necessary safety or architecture work?
5. Which rules are universal versus software/product-building specific?
6. How do we distinguish useful simplification from harmful underengineering?

## Required outputs

1. Established-concept map.
2. Candidate comparison.
3. Recommended 1–4 sentence snippet.
4. Trigger/depth rule.
5. Focused method for target/reuse/drift decisions.
6. Failure modes: overengineering, overcorrection, underengineering, premature simplification, sunk-cost behavior.
7. Examples across product, research, and ordinary tasks.
8. Evaluation prompts.
9. Boundaries with M04 and existing safety/authorization rules.
10. Integration proposal.

## Constraint

Do not turn `shortest path` into `fewest steps at any cost`. Value, correctness, material risk, and required evidence remain part of the target.
