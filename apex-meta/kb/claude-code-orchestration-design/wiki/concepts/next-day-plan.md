---
title: "Next-Day Plan"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "next-day-plan"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 99-111; weekly routine stages"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C001, B04-C004, B04-C005"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "medium"
claim_label: "behavioral_inference"
status: "active"
---

# Next-Day Plan

```yaml
pattern: "A next-day plan translates weekly direction and current state into executable flow packets."
used_when:
  - "A near-term workday needs scoped flows before execution."
not_used_when:
  - "The system is only recording completed execution."
reads:
  - "weekly plan packet"
  - "current project state"
writes:
  - "next-day plan"
  - "flow packet list"
  - "prompt-pack references"
token_efficiency:
  - "Execution reads only selected flow packets."
drift_controls:
  - "Operator approval separates planning from human execution."
unresolved_or_deferred:
  - "Exact daily planner implementation remains outside S6."
```
