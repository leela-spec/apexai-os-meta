---
title: "Standard Handoff Packet"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "standard-handoff-packet"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 72-85; handoff_contract_index questions"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C004, B04-C009, B04-C011, B04-C014"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Standard Handoff Packet

```yaml
pattern: "A handoff packet is the smallest explicit artifact that lets another role continue without relying on chat memory."
used_when:
  - "Work moves between skills, agents, sessions, or operator review."
not_used_when:
  - "The task is fully completed and no downstream role needs context."
reads:
  - "current state"
  - "target state"
  - "source_refs"
  - "candidate output"
writes:
  - "bounded handoff packet"
token_efficiency:
  - "References replace copied source bodies."
drift_controls:
  - "Authority, claim status, risk, and stop condition must be explicit."
unresolved_or_deferred:
  - "Exact canonical schema can be hardened later as a reusable contract."
```
