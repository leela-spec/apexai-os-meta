---
title: "APEX Orchestration System — Start Here"
purpose: >
  Entry point to the final orchestration system: what it is, the five invariants,
  the read order, and where everything lives. This package is the MAP AND LAW;
  the machinery it governs stays in its canonical runtime locations
  (.claude/skills/, .claude/agents/, scripts/).
created: 2026-07-11
---

# APEX Orchestration System

The unified orchestration system merging the old Apex agent-swarm doctrine (translated) with the running `apex-plan`/`apex-sync`/`apex-session` mutation backbone (kept in place). Decided through `apex-meta/fable-orchestrator/` (milestones 1–4: discovery, resilience dimensions, evaluation matrix, design-lock answers); assembled per its `implementation-plan.md`.

**One sentence:** the operator talks to Alfred; Meta Ops runs the file-backed workflow using the three apex skills for plan/compute/mutate; Meta Strategy sets direction; Meta Detective independently reviews consequential artifacts through two blind lenses; every durable mutation passes the single operator gate carrying the shared handoff schema and the artifact-authority field.

## The five invariants

1. **State lives in files** — plan, packets, verdicts, deltas on disk before a turn ends; any run resumable from disk alone.
2. **One mutation surface** — durable state only through the apex-session gated path; registry only through `scripts/apex_sync.py --dry-run false` after a drift report.
3. **One gate primitive** — `operator_validation: confirmed`; never implied, never defaulted, applied where consequence lives.
4. **Independent review before consequence** — consequential artifacts reach `authority.state: verified` via the two-lens Detective workflow before feeding a confirmed write.
5. **Candidate never auto-promotes** — learning and doctrine changes stay `candidate` until independently reviewed and operator-accepted.

## Read order

1. This file.
2. `ARCHITECTURE.md` — the full design: topology, runtime mapping, component wiring, what was deliberately not built.
3. `GLOSSARY.md` — canonical terms (role vs. state, candidate vs. verified, validation vs. approval…).
4. `workflows/orchestrator-run.md` — the canonical run loop; then `workflows/detective-review.md`.
5. `schemas/` — handoff-packet, authority-state, review-verdict.
6. `user-stories/user-stories.md` — the seven grounding stories = the system's regression suite.
7. `simulations/` — real per-story run records; a workflow is adopted only after its record passes.

## Where the machinery lives

| Surface | Location |
|---|---|
| Accountabilities & lanes (7 definitions) | `.claude/agents/` — alfred, meta-strategy, meta-ops, meta-detective, knowledge-bank, informatics-design, prompts-workflows |
| Mutation backbone | `.claude/skills/apex-plan`, `apex-sync`, `apex-session` (+ `apex-kb` for KB lifecycle) |
| Deterministic compute | `scripts/apex_sync.py` (stdlib-only, dry-run-first) |
| Detective's validation skill | `.claude/skills/source-authority-and-verdict-packet` |
| How this system was decided (audit trail) | `apex-meta/fable-orchestrator/` |
| Repo-wide map | `apex-meta/ORCHESTRATION-SYSTEMS-INDEX.md` |
