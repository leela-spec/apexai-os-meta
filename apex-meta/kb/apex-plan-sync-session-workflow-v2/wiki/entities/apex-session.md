---
title: "apex-session"
page_type: "entity"
kb_slug: "apex-plan-sync-session-workflow-v2"
source_refs:
  - source_id: "batch04-apex-session.analysis.md"
    source_path: "apex-meta/kb/apex-plan-sync-session-workflow-v2/ingest-analysis/batch04-apex-session.analysis.md"
    source_hash: "NA"
    source_pointer: "source_grounded_claims"
    source_storage_mode: "pointer_only"
created_at: "2026-07-03T12:00:00Z"
updated_at: "2026-07-03T12:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
review_flags: []
---

# apex-session

## Core summary

`apex-session` owns H6 handoff artifacts, gated status-change records, state deltas, entity updates, evidence references, and next-session context. It records confirmed session continuity after operator validation and does not perform ranking or deterministic sync computation.

## Source-grounded claims

- `apex-session` creates `task_plan.md`, `findings.md`, `progress.md`, and `next-session.md`.
- It preserves evidence references and unresolved context.
- It validates status changes before they are treated as confirmed.
- It feeds the planning layer with session context, but does not compute exact focus or ranking.

## Boundaries

- No task ranking.
- No blocker scans or registry rebuilds.
- No score or focus-candidate computation.
- No new work decomposition.

## Related pages

- [Workflow Summary](../summaries/apex-plan-sync-session-workflow-summary.md)
- [Three Package Boundary](../concepts/three-package-boundary.md)
- [Proposal Computation Mutation Split](../concepts/proposal-computation-mutation-split.md)
- [Operator-Gated Phase Boundary](../concepts/operator-gated-phase-boundary.md)
- [apex-plan](apex-plan.md)
- [apex-sync](apex-sync.md)

## Open questions

- Whether H6 handoff artifacts should receive a dedicated concept page in a later approved expansion.
