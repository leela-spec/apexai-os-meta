---
title: "Scheduler Boundary and Deferment"
page_type: summary
kb_slug: "claude-code-orchestration-design"
summary_slug: "scheduler-boundary-and-deferment"
source_refs:
  - source_id: "phase1-batch03-external-orchestration-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch03-external-orchestration-patterns.md"
    source_hash: "dbe4e500d5c22cc61adc4e1364412da71d3db683"
    source_pointer: "B03-C001; external feature surface mentions scheduled tasks and routines"
    source_storage_mode: "pointer_only"
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "weekly_routine_case_index and project_execution_index; recurring planning loops, state flow, gated mutation"
    source_storage_mode: "pointer_only"
  - source_id: "operator-phase1-review-decisions-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/operator-phase1-review-decisions-20260702.md"
    source_hash: "34d9c16967d2f7f49b716d75c8bb1a2a10eb96a7"
    source_pointer: "avoid_in_phase2: no operational orchestration system built; no runtime hooks/workflows/plugins"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T14:30:00Z"
updated_at: "2026-07-02T14:30:00Z"
confidence: "medium"
claim_label: "source_backed_summary"
status: "needs_review"
---

# Scheduler Boundary and Deferment

```yaml
extension_package: "scheduler_boundary_and_deferment"
pattern: >
  Schedulers belong to runtime orchestration, not to the S6 wiki compile itself.
  The KB can define scheduler boundaries and decision criteria, but must not
  create timers, cron jobs, monitors, hooks, agents, or workflow execution loops.
used_when:
  - "A future Apex workflow asks whether a recurring process should run automatically."
  - "A recurring daily/weekly loop needs a trigger model."
not_used_when:
  - "The current task is semantic wiki compilation or deterministic validation."
reads:
  - "recurrence need"
  - "state read/write contract"
  - "operator gate requirement"
  - "failure and stop conditions"
writes:
  - "scheduler candidate decision"
  - "manual, reminder, condition_watch, or runtime_scheduler recommendation"
  - "no runtime scheduler in S6"
token_efficiency:
  - "Schedulers should point to compact flow packets or state refs, not load raw histories."
drift_controls:
  - "Any scheduled mutation remains operator-gated until a deterministic write contract exists."
unresolved_or_deferred:
  - "Scheduler implementation surface."
  - "Runtime trigger policy."
  - "Failure recovery and duplicate-run prevention."
```
