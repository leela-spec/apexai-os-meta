# Plan/Sync/Session Engine Feeding the Weekly Orchestrator

## Summary

Use `apex-plan`, `apex-sync`, and `apex-session` as the project-management engine. The Weekly Orchestrator remains a separate operator workflow that consumes confirmed engine outputs and returns execution learning to Session.

The previous integration was directionally useful but incomplete: it exposed Plan and Sync through WeeklyOrchestrator, while the actual missing bridge—Session planning feed and Sync reports into PreCapWeek/PreCapNextDay—was never completed.

Target lifecycle:

```text
Plan proposal
  → Sync deterministic validation/computation
  → operator-approved Session mutation
  → Session planning feed + Sync reports
  → Weekly J1–J5 planning/execution
  → J6–J9 evidence and approved candidate
  → Session mutation
  → J10 mutation receipt
  → J11 confirmed overview
  → next weekly cycle
```

## Architecture and interface changes

### Project-management engine

- Preserve all existing Plan/Sync/Session skill contracts.
- Keep `apex-plan-ops` and `apex-sync-ops` as optional global project-engine agents, not weekly stages.
- Remove their dependency on the weekly handoff schema:
  - Plan worker returns the native `apex_plan_packet` path and compact summary.
  - Sync worker returns native deterministic reports unchanged.
  - Session remains in the operator-facing/main-thread mutation boundary because it requires confirmed approval.
- Preserve the existing native handoffs:
  - Plan requests Sync validation/computation and Session mutation.
  - Sync reads task records and never performs status mutation.
  - Session applies approved mutations and regenerates `planning_feed` and `next-session.md`.

### Engine → Weekly bridge

Extend PreCapWeek and PreCapNextDay accepted inputs with references to:

- confirmed Session `planning_feed`;
- Session `next-session.md`;
- Sync `next_action_report`;
- Sync `blocker_report`;
- optional Sync drift/focus reports when relevant.

Authority order for weekly project context:

1. confirmed Session planning feed and mutation records;
2. current Sync reports derived from those task records;
3. accepted operator intent and weekly recap evidence;
4. Project KB records as optional knowledge/milestone context;
5. degraded assumptions, always flagged.

Project KB is not a mutation authority in this flow and is not required for weekly execution.

### Weekly → Engine bridge

- Change J9/StatusMerge’s durable destination from direct weekly or Project-KB writing to an `apex-session` mutation request containing:
  - approved candidate changes;
  - current accepted values;
  - evidence and recap references;
  - operator decision;
  - unresolved conflicts.
- Session validates and applies the mutation under its existing gate contract.
- Replace J10’s “Project KB Update” meaning with a neutral **Project State Update Receipt** backed by the confirmed Session mutation result.
- J11 may show new truth only when J10 references a confirmed Session result.
- Remove direct writes to `state/apex-project-status.md` and `state/consumed-recap-registry.md` from WeeklyOrchestrator. Keep the empty files explicitly legacy until separately retired.

## Boundary and cleanup changes

- Remove Plan/Sync from WeeklyOrchestrator stage routing and from the weekly G1–G5 packet-type table.
- Keep the global Plan/Sync agents registered in root instructions under a separate “project-management engine” section.
- Update weekly architecture records to describe Plan/Sync/Session as an external upstream/downstream engine, not weekly-owned capabilities.
- Reclassify `project-kb-manager` as an optional knowledge projection and recap/milestone service; do not place it between Session and Weekly.
- Archive the regression-suite Plan packet as historical integration evidence, not a live approved project.
- Correct Fable documents so Weekly and the project engine are reusable inputs to Fable, never proof that Fable itself is complete.
- Reconcile J2, J3, J10, J11, and J12 templates, promotion mapping, manifests, and activation evidence after the J10 ownership change.

## Test plan

- **Engine test:** Plan proposal → Sync dependency/next-action reports → approved Session mutation → refreshed planning feed.
- **Forward bridge:** PreCapWeek and PreCapNextDay consume confirmed Session and Sync references without loading chat history or Project KB.
- **Return bridge:** weekly J7 candidate → J9 approval → Session mutation → J10 receipt → J11 confirmed state.
- **Negative mutation test:** unapproved J9, candidate recap, or failed Sync report cannot update Session or J11.
- **Separation test:** WeeklyOrchestrator contains no Plan/Sync dispatch routes or project-task write commands; Plan/Sync agents remain independently invocable.
- **Degraded test:** missing Session/Sync context yields a low-confidence weekly plan without fabricated state.
- **Token test:** measure direct native handoff sizes and global-agent return sizes; retain wrappers only if their isolation benefit exceeds their context cost.
- **Integrity test:** all live links resolve, YAML parses, and all 13 promoted templates match their declared source hashes.

## Assumptions

- Plan/Sync/Session are the canonical project/task management engine.
- Session owns approved project/task/session mutation and the planning feed.
- Weekly owns planning presentation, execution evidence, recap, and merge recommendation—not project-state mutation.
- Project KB remains available as supplementary knowledge but is outside the critical execution loop.
- Implementation continues on `codex/weekly-boundary-restoration`; no repository files have yet been changed on that branch.
