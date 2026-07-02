---
title: "Scheduler Boundary"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "scheduler-boundary"
source_refs:
  - source_id: "phase1-batch03-external-orchestration-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch03-external-orchestration-patterns.md"
    source_hash: "dbe4e500d5c22cc61adc4e1364412da71d3db683"
    source_pointer: "B03-C001; scheduled tasks and routines appear in external feature-surface map"
    source_storage_mode: "pointer_only"
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "project_execution_index and weekly_routine_case_index: state flow and recurring loops"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T14:30:00Z"
updated_at: "2026-07-02T14:30:00Z"
confidence: "medium"
claim_label: "behavioral_inference"
status: "needs_review"
---

# Scheduler Boundary

```yaml
pattern: "A scheduler is a trigger layer, not an authority layer."
used_when:
  - "A recurring workflow needs a time-based or condition-based start signal."
not_used_when:
  - "The workflow has not defined read/write contracts, stop conditions, and operator gates."
reads:
  - "trigger condition"
  - "eligible workflow or packet"
  - "state source"
  - "stop condition"
writes:
  - "run request or reminder candidate"
  - "no state mutation unless a separate write contract allows it"
token_efficiency:
  - "A scheduler should pass refs and trigger metadata, not full chat histories."
drift_controls:
  - "Scheduler output is execution evidence, not accepted state."
unresolved_or_deferred:
  - "Runtime scheduler mechanism."
  - "Deduplication and missed-run policy."
```
