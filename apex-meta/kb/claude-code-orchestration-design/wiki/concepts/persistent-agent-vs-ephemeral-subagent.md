---
title: "Persistent Agent vs Ephemeral Subagent"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "persistent-agent-vs-ephemeral-subagent"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 57-70; agent_orchestration_index questions"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch02-claude-code-orchestration-surface.md"
    source_hash: "505c6297d2c7198cbf0e77800577ab8e18a25d73"
    source_pointer: "claims B02-C008 through B02-C009; subagent context isolation"
    source_storage_mode: "pointer_only"
  - source_id: "operator-phase1-review-decisions-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/operator-phase1-review-decisions-20260702.md"
    source_hash: "34d9c16967d2f7f49b716d75c8bb1a2a10eb96a7"
    source_pointer: "lines 76-87; persistent vs ephemeral subagent decision"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Persistent Agent vs Ephemeral Subagent

```yaml
pattern: "Persistent agents hold stable repeated roles; ephemeral subagents isolate temporary or exploratory work and return compact results."
used_when:
  - "A domain role repeats and needs stable validation or audit doctrine."
  - "A one-off task needs context isolation without creating permanent coordination overhead."
not_used_when:
  - "A skill or static artifact can carry the procedure."
reads:
  - "routing criteria"
  - "task scope"
  - "source refs"
writes:
  - "summary result or candidate output"
  - "no runtime agent roster in S6"
token_efficiency:
  - "Use ephemeral subagents for bounded exploration instead of polluting main context."
drift_controls:
  - "Persistent only when role, tools, and validation criteria are stable."
unresolved_or_deferred:
  - "Final persistent agent roster remains deferred."
```
