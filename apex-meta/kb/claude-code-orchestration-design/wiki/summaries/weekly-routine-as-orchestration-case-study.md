---
title: "Weekly Routine as Orchestration Case Study"
page_type: summary
kb_slug: "claude-code-orchestration-design"
summary_slug: "weekly-routine-as-orchestration-case-study"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 99-111; weekly_routine_case_index questions"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C001 through B04-C019; entities extracted"
    source_storage_mode: "pointer_only"
  - source_id: "operator-phase1-review-decisions-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/operator-phase1-review-decisions-20260702.md"
    source_hash: "34d9c16967d2f7f49b716d75c8bb1a2a10eb96a7"
    source_pointer: "lines 100-122; prompt pack and HALT/CLARIFY decisions"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "medium"
claim_label: "source_backed_summary"
status: "active"
---

# Weekly Routine as Orchestration Case Study

```yaml
summary_id: weekly_routine_as_orchestration_case_study
specialized_indexes:
  - weekly_routine_case_index
  - project_execution_index
pattern: >
  The weekly routine is a case study for staged orchestration: weekly planning,
  next-day planning, human flow execution, flow recap, status merge, and next
  cycle context.
used_when:
  - "Testing whether a general orchestration doctrine handles recurring project work."
  - "Separating plans, prompt packs, raw dumps, recaps, and status packets."
not_used_when:
  - "Treating the weekly routine as the final runtime architecture."
reads:
  - "weekly plan packet"
  - "current project state"
  - "flow packet"
  - "raw flow dump"
  - "flow recap packet"
writes:
  - "next-day plan"
  - "per-flow prompt pack pointer"
  - "flow recap"
  - "status delta"
  - "next-cycle context"
token_efficiency:
  - "Keep raw dumps out of future context after recap."
  - "Use one prompt-pack file per flow as the selected doctrine."
drift_controls:
  - "Operator gates separate planning from execution and status mutation."
  - "HALT/CLARIFY/file-output proof are Apex-wide minimal controls."
unresolved_or_deferred:
  - "Exact runtime paths and process implementation remain outside S6."
```

This is a pattern case, not an instruction to build PreCap, FlowRecap, APSU, or schedulers in this phase.
