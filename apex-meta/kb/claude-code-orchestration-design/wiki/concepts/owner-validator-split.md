---
title: "Owner Validator Split"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "owner-validator-split"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 72-85; validator or operator review required"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch03-external-orchestration-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch03-external-orchestration-patterns.md"
    source_hash: "dbe4e500d5c22cc61adc4e1364412da71d3db683"
    source_pointer: "claims B03-C006 through B03-C007; validation split"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C004 through B04-C017; operator gates and closure proof"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Owner Validator Split

```yaml
pattern: "The role that owns production is separate from the role that validates acceptance."
used_when:
  - "An artifact may be correct structurally but risky semantically or operationally."
not_used_when:
  - "The operation is read-only and has no downstream commitment."
reads:
  - "owner output"
  - "acceptance criteria"
  - "source_refs"
writes:
  - "validation verdict"
  - "accepted, needs_review, or blocked status"
token_efficiency:
  - "The validator reads the candidate and evidence packet, not the entire source corpus."
drift_controls:
  - "The producer cannot self-promote high-impact work without review."
unresolved_or_deferred:
  - "Exact validator roles are deferred beyond S6."
```
