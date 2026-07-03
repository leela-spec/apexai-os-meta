---
title: "Operator-Gated Phase Boundary"
page_type: "concept"
kb_slug: "apex-plan-sync-session-workflow-v2"
source_refs:
  - source_id: "phase1-completion-report.md"
    source_path: "apex-meta/kb/apex-plan-sync-session-workflow-v2/ingest-analysis/phase1-completion-report.md"
    source_hash: "NA"
    source_pointer: "operator_gate; required_phrase"
    source_storage_mode: "pointer_only"
  - source_id: "deterministic-after-phase1-report.md"
    source_path: "apex-meta/kb/apex-plan-sync-session-workflow-v2/log/deterministic-after-phase1-report.md"
    source_hash: "NA"
    source_pointer: "phase2_gate"
    source_storage_mode: "pointer_only"
created_at: "2026-07-03T12:00:00Z"
updated_at: "2026-07-03T12:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
review_flags: []
---

# Operator-Gated Phase Boundary

## Core summary

The Apex KB lifecycle uses operator gates to prevent uncontrolled phase and status transitions. Phase 1 analysis stops before wiki compilation. Phase 2 requires the explicit phrase `approve ingest`. Status mutation requires explicit operator validation before consequential changes count as confirmed.

## Source-grounded claims

- The Phase 1 completion report recorded `phase2_allowed: false` and required `approve ingest` before wiki synthesis.
- The deterministic after-Phase-1 report passed lint, audit, status, and optional health checks, then kept Phase 2 blocked until operator approval.
- `apex-session` requires confirmed operator validation before consequential mutation records count as confirmed.

## Boundaries

- Phase 2 wiki compilation must not be inferred from Phase 1 completion alone.
- Deterministic PASS does not itself authorize semantic wiki creation.
- Session mutation records are not confirmed without the required validation field.

## Related pages

- [Workflow Summary](../summaries/apex-plan-sync-session-workflow-summary.md)
- [Proposal Computation Mutation Split](proposal-computation-mutation-split.md)
- [apex-session](../entities/apex-session.md)

## Open questions

- Whether later deterministic status reports should store the Phase 2 approval event as a machine-readable lifecycle record.
