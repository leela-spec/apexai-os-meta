---
title: "Flow Recap Packet"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "flow-recap-packet"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 99-111; flow recap stage"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C001, B04-C009, B04-C011"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "medium"
claim_label: "behavioral_inference"
status: "active"
---

# Flow Recap Packet

```yaml
pattern: "A flow recap packet converts raw execution evidence into structured memory and candidate state deltas."
used_when:
  - "A completed or partial flow needs durable interpretation."
not_used_when:
  - "Execution has not happened or evidence is unavailable."
reads:
  - "flow packet"
  - "raw flow dump"
writes:
  - "recap summary"
  - "candidate state delta"
  - "open questions"
token_efficiency:
  - "The recap compresses raw evidence into future-readable fields."
drift_controls:
  - "Recap output remains candidate until accepted by merge or operator gate."
unresolved_or_deferred:
  - "No FlowRecap runtime is created in S6."
```
