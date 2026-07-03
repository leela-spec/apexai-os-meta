---
title: "Operator-Confirmed Mutation"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "operator-confirmed-mutation"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 86-98; confirmed mutation records"
    source_storage_mode: "pointer_only"
  - source_id: "operator-phase1-review-decisions-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/operator-phase1-review-decisions-20260702.md"
    source_hash: "34d9c16967d2f7f49b716d75c8bb1a2a10eb96a7"
    source_pointer: "lines 54-68; hard gates"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C005 and B04-C014; operator gates and closure proof"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Operator-Confirmed Mutation

```yaml
pattern: "A durable mutation becomes accepted only after explicit operator confirmation or an equivalent approved gate."
used_when:
  - "A write changes canonical state, schema, source custody, or execution records."
not_used_when:
  - "The write is a Phase 2 compiled wiki page already authorized by the operator."
reads:
  - "operator decision"
  - "target path"
  - "validation proof"
writes:
  - "confirmed mutation"
  - "audit-visible status"
token_efficiency:
  - "Confirmation records prevent future agents from re-asking why a change happened."
drift_controls:
  - "Prevents generated plans from becoming state without acceptance."
unresolved_or_deferred:
  - "No state mutation outside the KB wiki/log paths occurs in S6."
```
