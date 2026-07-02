---
title: "Weekly Plan Packet"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "weekly-plan-packet"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 99-111; stage reads and writes"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C001, B04-C004, B04-C005"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "medium"
claim_label: "behavioral_inference"
status: "active"
---

# Weekly Plan Packet

```yaml
pattern: "A weekly plan packet carries strategic direction and constraints into daily planning."
used_when:
  - "A recurring routine needs stable weekly priorities before daily execution."
not_used_when:
  - "The task is an isolated one-off request."
reads:
  - "previous status"
  - "operator intent"
writes:
  - "weekly direction"
  - "constraints"
  - "handoff to next-day planning"
token_efficiency:
  - "Daily planning reads a compact weekly packet instead of reconstructing strategy."
drift_controls:
  - "Operator approval separates weekly direction from execution."
unresolved_or_deferred:
  - "This page defines the artifact pattern, not the runtime path."
```
