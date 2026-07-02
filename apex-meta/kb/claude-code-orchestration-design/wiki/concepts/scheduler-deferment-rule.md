---
title: "Scheduler Deferment Rule"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "scheduler-deferment-rule"
source_refs:
  - source_id: "operator-phase1-review-decisions-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/operator-phase1-review-decisions-20260702.md"
    source_hash: "34d9c16967d2f7f49b716d75c8bb1a2a10eb96a7"
    source_pointer: "avoid_in_phase2: runtime implementation work deferred"
    source_storage_mode: "pointer_only"
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "compile objective: abstract source-grounded orchestration knowledge"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T14:30:00Z"
updated_at: "2026-07-02T14:30:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Scheduler Deferment Rule

```yaml
pattern: "Scheduler design stays deferred until workflow shape, state contract, gate model, and failure model are explicit."
used_when:
  - "A recurring trigger is proposed for an Apex process."
not_used_when:
  - "The proposal is only a semantic KB topic package."
reads:
  - "workflow readiness"
  - "state authority"
  - "operator gate requirement"
  - "failure handling"
writes:
  - "defer_scheduler recommendation"
  - "required_preconditions list"
token_efficiency:
  - "Avoids loading runtime scheduler context into normal KB sessions."
drift_controls:
  - "Recurring trigger behavior is not treated as current system behavior until validated outside S6."
unresolved_or_deferred:
  - "Scheduler runtime surface."
  - "Scheduler audit log shape."
  - "Recovery semantics."
```
