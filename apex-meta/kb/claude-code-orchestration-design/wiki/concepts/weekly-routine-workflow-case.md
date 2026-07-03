---
title: "Weekly Routine Workflow Case"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "weekly-routine-workflow-case"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 99-111; weekly_routine_case_index"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C001 through B04-C005; Apex loop and gates"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "medium"
claim_label: "source_backed_summary"
status: "active"
---

# Weekly Routine Workflow Case

```yaml
pattern: "The weekly routine is a staged workflow case: plan, execute, recap, merge, and seed the next cycle."
used_when:
  - "Demonstrating the general orchestration model on recurring work."
not_used_when:
  - "Building the operational weekly routine runtime."
reads:
  - "weekly direction"
  - "project state"
  - "flow evidence"
writes:
  - "plans, recaps, status deltas, next context"
token_efficiency:
  - "Each stage emits a small artifact instead of preserving raw conversation."
drift_controls:
  - "Stage gates prevent planning, execution, and mutation from collapsing."
unresolved_or_deferred:
  - "Exact workflow implementation remains outside S6."
```
