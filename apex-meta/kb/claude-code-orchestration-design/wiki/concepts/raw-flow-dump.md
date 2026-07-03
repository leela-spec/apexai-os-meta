---
title: "Raw Flow Dump"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "raw-flow-dump"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 109-110; raw dumps and context bloat"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C009, B04-C011; evidence and state frames"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "medium"
claim_label: "behavioral_inference"
status: "active"
---

# Raw Flow Dump

```yaml
pattern: "A raw flow dump is temporary execution evidence, not durable project memory."
used_when:
  - "The operator records messy execution output before recap."
not_used_when:
  - "Future sessions need concise accepted state."
reads:
  - "flow packet"
  - "operator execution evidence"
writes:
  - "raw evidence artifact"
token_efficiency:
  - "Raw dumps are consumed into recaps and kept out of routine future context."
drift_controls:
  - "Unprocessed raw evidence is not treated as accepted state."
unresolved_or_deferred:
  - "Retention policy remains outside S6."
```
