---
title: "apex-sync"
page_type: "entity"
kb_slug: "apex-plan-sync-session-workflow-v2"
source_refs:
  - source_id: "batch03-apex-sync.analysis.md"
    source_path: "apex-meta/kb/apex-plan-sync-session-workflow-v2/ingest-analysis/batch03-apex-sync.analysis.md"
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

# apex-sync

## Core summary

`apex-sync` owns deterministic read-side computation and validation. It reads task evidence and produces script-backed reports for next actions, blockers, stale tasks, registry checks, drift, scores, focus candidates, and dependency validation. It does not author semantic plans, session narrative, handoff files, or mutation records.

## Source-grounded claims

- `apex-sync` delegates exact computation to `scripts/apex_sync.py`.
- Its canonical command shape is dry-run-first JSON reporting.
- Its allowed report surface includes next action, blocker, registry, stall, drift, score, focus candidate, and dependency validation reports.
- The only write exception is the narrow registry exception, limited to `apex-meta/registry/index.md` with explicit non-dry-run authorization.

## Boundaries

- No semantic plan authoring.
- No session state mutation.
- No handoff narrative authoring.
- No operator decision validation records.

## Related pages

- [Workflow Summary](../summaries/apex-plan-sync-session-workflow-summary.md)
- [Three Package Boundary](../concepts/three-package-boundary.md)
- [Proposal Computation Mutation Split](../concepts/proposal-computation-mutation-split.md)
- [apex-plan](apex-plan.md)
- [apex-session](apex-session.md)

## Open questions

- Whether `scripts/apex_sync.py` should receive a separate entity page in a later approved expansion.
