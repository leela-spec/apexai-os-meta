---
title: "Claude Code"
page_type: entity
kb_slug: "claude-code-orchestration-design"
entity_slug: "claude-code"
entity_type: "runtime_surface"
source_refs:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch02-claude-code-orchestration-surface.md"
    source_hash: "505c6297d2c7198cbf0e77800577ab8e18a25d73"
    source_pointer: "source scope and entities extracted"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Claude Code

```yaml
role: "Runtime surface for skills, hooks, subagents, plugins, MCP, settings, rules, and project guidance."
used_when:
  - "Retrieving the overall orchestration surface."
not_used_when:
  - "Treating one component as the whole runtime."
reads:
  - "project guidance and component files"
writes:
  - "runtime outputs only through approved mechanisms, not S6"
token_efficiency:
  - "Use component entity pages to narrow queries."
drift_controls:
  - "Platform behavior claims should be verified when volatile."
deferred:
  - "No Claude Code configuration files are written in S6."
```
