---
title: "Flow Packet"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "flow-packet"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 99-111; each stage reads and writes"
    source_storage_mode: "pointer_only"
  - source_id: "operator-phase1-review-decisions-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/operator-phase1-review-decisions-20260702.md"
    source_hash: "34d9c16967d2f7f49b716d75c8bb1a2a10eb96a7"
    source_pointer: "lines 100-107; flow packet points to prompt pack"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "medium"
claim_label: "source_backed_summary"
status: "active"
---

# Flow Packet

```yaml
pattern: "A flow packet scopes one execution unit and points to its prompt pack instead of embedding every prompt."
used_when:
  - "A daily plan needs separable executable work units."
not_used_when:
  - "The artifact is a general strategy note or final status summary."
reads:
  - "next-day plan"
  - "current scope"
writes:
  - "flow objective"
  - "input refs"
  - "prompt-pack pointer"
token_efficiency:
  - "The flow packet stays compact by referencing the prompt pack file."
drift_controls:
  - "Execution is scoped to one flow and explicit input refs."
unresolved_or_deferred:
  - "Exact file path convention remains outside S6."
```
