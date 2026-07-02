---
title: "Stop Condition as Context Saver"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "stop-condition-as-context-saver"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 124-137; stop_condition_as_context_saver"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C013, B04-C014; stop and closure controls"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Stop Condition as Context Saver

```yaml
pattern: "A clear stop condition saves context by ending invalid continuation early."
used_when:
  - "More work would require missing evidence, approval, or target clarity."
not_used_when:
  - "The next action is fully specified and low risk."
reads:
  - "blocking condition"
  - "required next proof"
writes:
  - "stop status"
  - "one next required action"
token_efficiency:
  - "Stopping prevents speculative expansion and repeated repair passes."
drift_controls:
  - "Stop conditions make uncertainty visible instead of hidden in prose."
unresolved_or_deferred:
  - "Machine-readable stop enum can be standardized later."
```
