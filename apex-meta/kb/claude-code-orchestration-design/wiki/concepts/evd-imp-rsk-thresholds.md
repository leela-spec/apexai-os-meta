---
title: "EVD IMP RSK Thresholds"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "evd-imp-rsk-thresholds"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "line 82; EVD_IMP_RSK semantics"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C007, B04-C013, B04-C014; gates and validation"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "medium"
claim_label: "working_hypothesis"
status: "needs_review"
---

# EVD IMP RSK Thresholds

```yaml
pattern: "Evidence, impact, and risk thresholds decide whether a handoff can proceed, needs validation, or must stop."
used_when:
  - "A candidate output may affect state, doctrine, or downstream execution."
not_used_when:
  - "The output is informational and has no downstream consequence."
reads:
  - "evidence quality"
  - "implementation impact"
  - "risk level"
writes:
  - "proceed, validate, clarify, or halt marker"
token_efficiency:
  - "Threshold labels replace long debate in every downstream handoff."
drift_controls:
  - "High-risk or low-evidence claims cannot proceed as accepted truth."
unresolved_or_deferred:
  - "Exact numeric thresholds remain outside S6 and need operator policy."
```
