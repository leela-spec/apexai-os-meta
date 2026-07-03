---
title: "Proposal Computation Mutation Split"
page_type: "concept"
kb_slug: "apex-plan-sync-session-workflow-v2"
source_refs:
  - source_id: "batch05-handoffs-and-gates.analysis.md"
    source_path: "apex-meta/kb/apex-plan-sync-session-workflow-v2/ingest-analysis/batch05-handoffs-and-gates.analysis.md"
    source_hash: "NA"
    source_pointer: "source_grounded_claims; migration_notes"
    source_storage_mode: "pointer_only"
created_at: "2026-07-03T12:00:00Z"
updated_at: "2026-07-03T12:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
review_flags: []
---

# Proposal Computation Mutation Split

## Core summary

The workflow treats proposal, computation, and mutation as separate epistemic states. Planning proposals are not computed truth. Computed sync outputs are not session mutations. Mutations require operator validation and session handling before they count as confirmed state.

## Source-grounded claims

- `apex-plan` can propose tasks, dependencies, priorities, due-date rationale, and handoff requests, but keeps them inside an operator-reviewed packet.
- `apex-sync` can compute exact reports and validations, but its outputs are reports and not semantic plans or session records.
- `apex-session` can record status changes and next-session context, but consequential status changes require `operator_validation: confirmed` before they are confirmed.

## Boundaries

- Proposal output must not be treated as exact dependency traversal, blocker scan, or task ranking.
- Computation output must not be treated as a status mutation or session narrative.
- Mutation records must preserve before/after evidence and operator validation.

## Related pages

- [Three Package Boundary](three-package-boundary.md)
- [Operator-Gated Phase Boundary](operator-gated-phase-boundary.md)
- [apex-plan](../entities/apex-plan.md)
- [apex-sync](../entities/apex-sync.md)
- [apex-session](../entities/apex-session.md)

## Open questions

- Whether later wiki expansion should split this concept into separate proposal, deterministic report, and mutation-record pages.
