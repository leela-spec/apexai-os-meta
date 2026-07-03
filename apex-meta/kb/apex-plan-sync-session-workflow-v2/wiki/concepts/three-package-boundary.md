---
title: "Three Package Boundary"
page_type: "concept"
kb_slug: "apex-plan-sync-session-workflow-v2"
source_refs:
  - source_id: "batch01-workflow-boundary.analysis.md"
    source_path: "apex-meta/kb/apex-plan-sync-session-workflow-v2/ingest-analysis/batch01-workflow-boundary.analysis.md"
    source_hash: "NA"
    source_pointer: "concepts_extracted; entities_or_roles_extracted"
    source_storage_mode: "pointer_only"
created_at: "2026-07-03T12:00:00Z"
updated_at: "2026-07-03T12:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
review_flags: []
---

# Three Package Boundary

## Core summary

The three-package boundary assigns distinct responsibilities to `apex-plan`, `apex-sync`, and `apex-session`. `apex-plan` is the proposal, reasoning, and planning-packet layer. `apex-sync` is the deterministic computation, validation, and script-backed report layer. `apex-session` is the confirmed mutation, session state, and handoff-artifact layer.

## Source-grounded claims

- `apex-plan` owns project capture, decomposition, dependency proposals, priority-policy proposals, urgency rationale, and focus recommendation drafts.
- `apex-sync` owns deterministic read-side reports, dependency eligibility checks, blocker scans, stale detection, registry rebuild previews or the narrow registry exception, drift checks, and score/focus computation.
- `apex-session` owns status mutation records, session progress, state deltas, entity updates, next-session context, planning feed, and H6 handoff artifacts.

## Boundaries

- `apex-plan` must not run scripts, compute exact next tasks, rebuild registries, or mutate state.
- `apex-sync` must not author semantic plans, session narrative, handoff files, or operator validation records.
- `apex-session` must not rank tasks, scan blockers, rebuild registries, compute scores, run scripts, or decompose new work.

## Related pages

- [Workflow Summary](../summaries/apex-plan-sync-session-workflow-summary.md)
- [Proposal Computation Mutation Split](proposal-computation-mutation-split.md)
- [apex-plan](../entities/apex-plan.md)
- [apex-sync](../entities/apex-sync.md)
- [apex-session](../entities/apex-session.md)

## Open questions

- Whether a later pass should add separate pages for H6 artifacts, registry exception, and handoff edges.
