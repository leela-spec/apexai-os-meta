---
title: "Locked Decisions"
purpose: "The operator's locked architecture/process decisions for this initiative. Current state only."
created: 2026-07-11
---

# Locked Decisions

## D1 — Full final system, no minimal/draft version

**Decision**: this process produces the fully final orchestration system. No draft, no minimal-first-version, no scaffold-to-be-completed-later.

**Rule**: nothing important or already-decided is deferred to a later phase as a v1/v2 excuse.

**Applies to**: every phase in `build-plan.md` and every future Fable session under this initiative.

---

## D2 — Process blueprint: orchestrator-worker fan-out only

**Decision**: the process this build runs on is `PRC-MULTI-001`, orchestrator-worker fan-out/fan-in, as spelled out in `process-blueprint.md`.

**Rule**: heavy guardrails, correction-layers, and validation processes built to prevent a failure routinely introduce a worse one — they crowd out the actual target and produce nothing. Work runs on positive, target-focused, clearly-defined output prompts and mechanisms, not defensive process correcting for things that don't need correcting.

**Applies to**: `process-blueprint.md`, and any future process design under this initiative.

**Not in tension with operator-verification milestones**: the eliminated guardrails were formal AI-run process layers (Kanban graphs, a chain-of-verification step run by an AI, risk frameworks). The operator checking Fable's own understanding/analysis at a milestone (see `target-log.md`) is a human checkpoint, not one of those — it doesn't come back under this elimination.
