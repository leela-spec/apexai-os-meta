---
title: "Apex Plan Sync Session Workflow Summary"
page_type: "summary"
kb_slug: "apex-plan-sync-session-workflow-v2"
source_refs:
  - source_id: "batch01-workflow-boundary.analysis.md"
    source_path: "apex-meta/kb/apex-plan-sync-session-workflow-v2/ingest-analysis/batch01-workflow-boundary.analysis.md"
    source_hash: "NA"
    source_pointer: "source_grounded_claims"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-completion-report.md"
    source_path: "apex-meta/kb/apex-plan-sync-session-workflow-v2/ingest-analysis/phase1-completion-report.md"
    source_hash: "NA"
    source_pointer: "strongest_patterns"
    source_storage_mode: "pointer_only"
created_at: "2026-07-03T12:00:00Z"
updated_at: "2026-07-03T12:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
review_flags: []
---

# Apex Plan Sync Session Workflow Summary

## Core summary

The workflow separates planning proposals, deterministic computation, and gated session mutation into three packages. `apex-plan` proposes operator-reviewed planning packets. `apex-sync` owns deterministic computation and read-side validation. `apex-session` owns confirmed mutation records, H6 handoff artifacts, state deltas, raw source preservation, and next-session context. The boundary prevents uncontrolled collapse of planning, computation, and mutation.

## Source-grounded claims

- `apex-plan` produces an `apex_plan_packet` for operator review, including project capture, task drafts, dependency proposals, priority rationale, handoff requests, and an operator gate.
- `apex-sync` computes deterministic reports and validates task evidence through script-backed read-side behavior; it remains dry-run-first and has only a narrow registry-write exception.
- `apex-session` converts task/session evidence into H6 handoff artifacts, mutation records, state deltas, entity updates, and next-session context.
- The Phase 2 wiki is based on Phase 1 analysis and does not rerun deterministic scripts or reopen Phase 1.

## Boundaries

- Proposals are not computed truth.
- Computed reports are not session mutations.
- Consequential mutation confirmation requires operator validation.
- This page does not define new commands or create query outputs.

## Related pages

- [Three Package Boundary](../concepts/three-package-boundary.md)
- [Proposal Computation Mutation Split](../concepts/proposal-computation-mutation-split.md)
- [Operator-Gated Phase Boundary](../concepts/operator-gated-phase-boundary.md)
- [apex-plan](../entities/apex-plan.md)
- [apex-sync](../entities/apex-sync.md)
- [apex-session](../entities/apex-session.md)

## Open questions

- Whether supporting reference files add finer-grained boundary detail for a later expansion.
- Whether `scripts/apex_sync.py` should receive a separate entity page in a later approved phase.
