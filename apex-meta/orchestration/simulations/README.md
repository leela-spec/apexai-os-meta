---
title: "Simulation Records"
purpose: >
  One file per user story: a REAL attempt to satisfy the story with real repo content,
  honestly recorded. A workflow is not adopted until its record here passes.
created: 2026-07-11
---

# Simulation Records

Definition (from `apex-meta/fable-orchestrator/build-plan.md`): a simulation **is** an actual attempt to satisfy the user story using real repo content, with the real result recorded — pass, partial, or fail, honestly. It **is not** a hypothetical walkthrough or a design doc.

Minimum record shape per file:
- the user story being tested (ID + link into `../user-stories/user-stories.md`)
- the actual steps taken (real tool calls, real files read/written)
- the actual result (quote or cite it)
- verdict: pass / partial / fail, with the reason

Naming: `<story-id>-<yyyymmdd>.md` (e.g. `US-IDEA-01-20260712.md`).

Regression rule: re-run affected stories whenever the schemas, workflows, agent definitions, or the three apex skills change.

Status: no story has been run yet. First candidate: **US-IDEA-01** (smallest durable set: Alfred, Meta Ops, Meta Detective; also materializes the registry).
