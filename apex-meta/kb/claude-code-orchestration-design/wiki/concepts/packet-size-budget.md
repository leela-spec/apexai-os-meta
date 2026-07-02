---
title: "Packet Size Budget"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "packet-size-budget"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 124-137; packet_size_budget"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C007 through B04-C011; bounded artifacts"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "medium"
claim_label: "behavioral_inference"
status: "active"
---

# Packet Size Budget

```yaml
pattern: "Packets should be small enough to route work, not large enough to become a new raw corpus."
used_when:
  - "Designing handoff, task, plan, recap, or query packets."
not_used_when:
  - "The packet is an archive or full evidence bundle by design."
reads:
  - "essential state"
  - "refs"
  - "validation status"
writes:
  - "bounded packet"
token_efficiency:
  - "Include only target, current state, refs, constraints, next action, and stop condition."
drift_controls:
  - "Budget pressure exposes unclear or overloaded tasks."
unresolved_or_deferred:
  - "Exact token or byte limits remain policy work."
```
