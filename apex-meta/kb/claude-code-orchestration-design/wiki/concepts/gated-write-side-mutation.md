---
title: "Gated Write-Side Mutation"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "gated-write-side-mutation"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 86-98; gated write-side mutation"
    source_storage_mode: "pointer_only"
  - source_id: "operator-phase1-review-decisions-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/operator-phase1-review-decisions-20260702.md"
    source_hash: "34d9c16967d2f7f49b716d75c8bb1a2a10eb96a7"
    source_pointer: "lines 54-68; hard-enforce high-risk gates"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C005, B04-C014, B04-C017"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Gated Write-Side Mutation

```yaml
pattern: "State-changing writes require an explicit gate, proof of target, and validation before being accepted."
used_when:
  - "A task changes durable project, KB, or execution state."
not_used_when:
  - "The output is a read-only report or candidate page."
reads:
  - "approved target"
  - "current state"
  - "validation criteria"
writes:
  - "confirmed mutation record"
  - "updated canonical file only after approval"
token_efficiency:
  - "Mutation packets store deltas rather than full histories."
drift_controls:
  - "No write-side mutation proceeds from prose instruction alone."
unresolved_or_deferred:
  - "S6 compiles the rule; it does not create enforcement hooks."
```
