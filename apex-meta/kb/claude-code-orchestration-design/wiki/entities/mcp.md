---
title: "Model Context Protocol"
page_type: entity
kb_slug: "claude-code-orchestration-design"
entity_slug: "mcp"
entity_type: "protocol"
source_refs:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch02-claude-code-orchestration-surface.md"
    source_hash: "505c6297d2c7198cbf0e77800577ab8e18a25d73"
    source_pointer: "claims B02-C013; entities extracted model-context-protocol"
    source_storage_mode: "pointer_only"
  - source_id: "operator-phase1-review-decisions-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/operator-phase1-review-decisions-20260702.md"
    source_hash: "34d9c16967d2f7f49b716d75c8bb1a2a10eb96a7"
    source_pointer: "lines 88-91; MCP later/allowlist decision"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Model Context Protocol

```yaml
role: "External tool and data connectivity layer for Claude Code."
used_when:
  - "A Claude Code process needs controlled access to external systems."
not_used_when:
  - "The KB can answer from compiled pages and source refs."
reads:
  - "server configuration"
  - "trust policy"
writes:
  - "external tool interactions outside S6"
token_efficiency:
  - "MCP can narrow access to tools, but it adds trust and policy cost."
drift_controls:
  - "MCP usage requires explicit allowlist and injection-risk handling."
deferred:
  - "No MCP config is created in S6."
```
