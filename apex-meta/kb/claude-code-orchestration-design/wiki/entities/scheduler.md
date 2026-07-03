---
title: "Scheduler"
page_type: entity
kb_slug: "claude-code-orchestration-design"
entity_slug: "scheduler"
entity_type: "runtime_trigger_component"
source_refs:
  - source_id: "phase1-batch03-external-orchestration-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch03-external-orchestration-patterns.md"
    source_hash: "dbe4e500d5c22cc61adc4e1364412da71d3db683"
    source_pointer: "B03-C001; scheduled tasks and routines listed in external feature-surface map"
    source_storage_mode: "pointer_only"
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "weekly_routine_case_index and project_execution_index recurring/state-flow questions"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T14:30:00Z"
updated_at: "2026-07-02T14:30:00Z"
confidence: "medium"
claim_label: "behavioral_inference"
status: "needs_review"
---

# Scheduler

```yaml
role: "Runtime trigger component for recurring or condition-based workflow starts."
used_when:
  - "A mature workflow needs a start signal based on time, recurrence, or condition."
not_used_when:
  - "The workflow lacks state contracts, gates, stop conditions, or validation."
reads:
  - "trigger condition"
  - "workflow reference"
  - "state reference"
  - "operator policy"
writes:
  - "run request or reminder candidate"
  - "execution evidence only, unless another component has write authority"
token_efficiency:
  - "Schedulers should pass compact refs, not raw prior sessions."
drift_controls:
  - "Scheduling is deferred in S6 and must not be confused with implemented runtime behavior."
deferred:
  - "No scheduler implementation is created in S6."
```
