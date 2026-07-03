---
title: "Apex Plan Sync Session Workflow v2 — Wiki Index"
page_type: "index"
kb_slug: "apex-plan-sync-session-workflow-v2"
source_refs:
  - source_id: "phase1-completion-report.md"
    source_path: "apex-meta/kb/apex-plan-sync-session-workflow-v2/ingest-analysis/phase1-completion-report.md"
    source_hash: "NA"
    source_pointer: "phase1-completion-report.md"
    source_storage_mode: "pointer_only"
  - source_id: "deterministic-after-phase1-report.md"
    source_path: "apex-meta/kb/apex-plan-sync-session-workflow-v2/log/deterministic-after-phase1-report.md"
    source_hash: "NA"
    source_pointer: "deterministic-after-phase1-report.md"
    source_storage_mode: "pointer_only"
created_at: "2026-07-03T12:00:00Z"
updated_at: "2026-07-03T12:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
review_flags: []
---

# Apex Plan Sync Session Workflow v2 — Wiki Index

## Summary pages

- [Apex Plan Sync Session Workflow Summary](summaries/apex-plan-sync-session-workflow-summary.md) — short workflow summary for the plan → sync → session package split.

## Concept pages

- [Three Package Boundary](concepts/three-package-boundary.md) — apex-plan, apex-sync, and apex-session responsibilities.
- [Proposal Computation Mutation Split](concepts/proposal-computation-mutation-split.md) — separation between proposals, deterministic computation, and gated mutation records.
- [Operator-Gated Phase Boundary](concepts/operator-gated-phase-boundary.md) — Phase 1/Phase 2 and status-mutation approval gates.

## Entity pages

- [apex-plan](entities/apex-plan.md) — planning packet creation and proposal ownership.
- [apex-sync](entities/apex-sync.md) — deterministic read-side computation and validation ownership.
- [apex-session](entities/apex-session.md) — H6 handoff artifacts, raw-source preservation, and gated mutation records.

## Source basis

This wiki layer is compiled from the Phase 1 analysis files and the deterministic after-Phase-1 PASS report. It intentionally keeps the wiki minimal and does not create query outputs, deterministic reports, or additional pages.

## Next deterministic step

Run the deterministic index/lint/audit/status checks after Phase 2 wiki compilation.
