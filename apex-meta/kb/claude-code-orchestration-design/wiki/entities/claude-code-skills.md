---
title: "Claude Code Skills"
page_type: entity
kb_slug: "claude-code-orchestration-design"
entity_slug: "claude-code-skills"
entity_type: "runtime_component"
source_refs:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch02-claude-code-orchestration-surface.md"
    source_hash: "505c6297d2c7198cbf0e77800577ab8e18a25d73"
    source_pointer: "claims B02-C001 through B02-C004; entities extracted"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Claude Code Skills

```yaml
role: "Repeatable procedure and reference packages invoked directly or automatically in Claude Code."
used_when:
  - "A reusable procedure needs compact activation plus supporting files."
not_used_when:
  - "The need is hard enforcement, external connectivity, or broad distribution."
reads:
  - "description"
  - "SKILL.md body"
  - "supporting files on demand"
writes:
  - "procedure artifacts"
token_efficiency:
  - "Descriptions are always visible; details load only when invoked."
drift_controls:
  - "Boundary and non-purpose keep skill scope narrow."
deferred:
  - "No skill files are created in S6."
```
