---
title: "Mechanism Ladder"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "mechanism-ladder"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 112-123; mechanism mapping questions"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch02-claude-code-orchestration-surface.md"
    source_hash: "505c6297d2c7198cbf0e77800577ab8e18a25d73"
    source_pointer: "claim B02-C014; layered control plane"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Mechanism Ladder

```yaml
pattern: "Choose the least powerful mechanism that safely satisfies the need."
used_when:
  - "Selecting between artifact, skill, workflow, subagent, agent, script, hook, plugin, or MCP."
not_used_when:
  - "The mechanism has already been mandated by an approved implementation contract."
reads:
  - "task type"
  - "risk level"
  - "repeatability"
writes:
  - "mechanism selection rationale"
token_efficiency:
  - "Static artifacts and skills come before heavier persistent systems."
drift_controls:
  - "Avoids overengineering and role sprawl."
unresolved_or_deferred:
  - "Final implementation surface is decided after KB compile and validation."
```
