---
title: "Multi-Agent Orchestration — Start Here"
purpose: >
  Entry point to Multi-Agent Orchestration inside APEX OS: activation boundary,
  invariants, read order, and runtime locations. This package is the system map
  and law; its machinery stays in the canonical .claude/skills/, .claude/agents/,
  scripts/, and apex-meta/orchestration/ locations.
created: 2026-07-11
---

# Multi-Agent Orchestration

Multi-Agent Orchestration is one of two orchestration systems inside APEX OS. It is the live package developed under the former working name Fable Orchestrator. Activate it only when the operator explicitly requests a Multi-Agent Orchestration run or explicitly routes a bounded problem into this system.

It does not include or replace the Weekly Orchestrator. A Weekly Orchestrator run does not activate this system, and this system does not absorb the weekly loop. Cross-system input is accepted only through explicit operator instruction, an explicit handoff packet, or a confirmed durable-artifact reference.

The system translates the old Apex agent-swarm doctrine without reviving an always-on swarm. It uses the shared Plan-Sync-Session Backbone in place: `apex-plan` proposes, `apex-sync` computes, and `apex-session` applies confirmed mutations and closes the run.

**One sentence:** in an explicitly started Multi-Agent Orchestration run, the operator talks to Alfred; Meta Ops runs the file-backed workflow through the shared backbone; Meta Strategy sets direction; Meta Detective independently reviews consequential artifacts through two blind lenses; and every durable mutation passes the operator gate with the shared handoff schema and artifact-authority fields.

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
| APEX OS activation router | `.claude/CLAUDE.md` |
| Multi-Agent accountabilities & lanes (7 definitions) | `.claude/agents/` — alfred, meta-strategy, meta-ops, meta-detective, knowledge-bank, informatics-design, prompts-workflows |
| Shared Plan-Sync-Session Backbone | `.claude/skills/apex-plan`, `.claude/skills/apex-sync`, `.claude/skills/apex-session` |
| Supporting KB lifecycle capability | `.claude/skills/apex-kb` |
| Deterministic compute | `scripts/apex_sync.py` (stdlib-only, dry-run-first) |
| Detective's validation skill | `.claude/skills/source-authority-and-verdict-packet` |
| Separate Weekly Orchestrator entrypoint | `.claude/skills/weekly-orchestrator/SKILL.md` |
| Historical design audit trail | `apex-meta/fable-orchestrator/` |
| Repo-wide map | `apex-meta/ORCHESTRATION-SYSTEMS-INDEX.md` |
