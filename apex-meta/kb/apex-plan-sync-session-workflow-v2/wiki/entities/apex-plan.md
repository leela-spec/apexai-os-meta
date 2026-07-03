---
title: "apex-plan"
page_type: "entity"
kb_slug: "apex-plan-sync-session-workflow-v2"
source_refs:
  - source_id: "batch02-apex-plan.analysis.md"
    source_path: "apex-meta/kb/apex-plan-sync-session-workflow-v2/ingest-analysis/batch02-apex-plan.analysis.md"
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

# apex-plan

## Core summary

`apex-plan` owns planning packet creation. It captures project intent, proposes epics/tasks/dependencies/priorities, and produces an operator-reviewed `apex_plan_packet`. It does not run scripts, compute exact rankings, rebuild registries, or mutate state.

## Source-grounded claims

- `apex-plan` creates planning packets for operator review.
- It proposes epics, task drafts, dependency links, qualitative priority, due-date urgency rationale, and provisional focus rationale.
- It hands exact computation, dependency validation, blocker scans, registry rebuild, drift checks, urgency scoring, and focus-candidate computation to `apex-sync`.
- It hands durable updates, status mutation records, entity updates, progress capture, findings capture, and next-session context to `apex-session`.

## Boundaries

- No script execution.
- No state mutation.
- No exact next-task computation or exact sorting.
- No durable session handoff creation.

## Related pages

- [Workflow Summary](../summaries/apex-plan-sync-session-workflow-summary.md)
- [Three Package Boundary](../concepts/three-package-boundary.md)
- [Proposal Computation Mutation Split](../concepts/proposal-computation-mutation-split.md)
- [apex-sync](apex-sync.md)
- [apex-session](apex-session.md)

## Open questions

- Whether the `apex_plan_packet` itself should get a dedicated concept page in a later approved expansion.
