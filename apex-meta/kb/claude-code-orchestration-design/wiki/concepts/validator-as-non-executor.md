---
title: "Validator as Non-Executor"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "validator-as-non-executor"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 65-66; build, validation, routing, authority separation"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch03-external-orchestration-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch03-external-orchestration-patterns.md"
    source_hash: "dbe4e500d5c22cc61adc4e1364412da71d3db683"
    source_pointer: "claims B03-C006 through B03-C007; deterministic-then-inference validation"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C013 through B04-C017; verification and gates"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Validator as Non-Executor

```yaml
pattern: "A validator reviews evidence, shape, risk, and completion proof without taking over execution authority."
used_when:
  - "An output needs independent review or risk classification."
not_used_when:
  - "The validator is the only role able to perform the actual task."
reads:
  - "candidate output"
  - "source_refs"
  - "acceptance criteria"
writes:
  - "validation result"
  - "blocker or escalation"
token_efficiency:
  - "Validator reads the smallest candidate/evidence set, not the whole source history."
drift_controls:
  - "Validation cannot silently promote a candidate to accepted truth without the required gate."
unresolved_or_deferred:
  - "Which validation gates become hooks or scripts is deferred beyond S6."
```
