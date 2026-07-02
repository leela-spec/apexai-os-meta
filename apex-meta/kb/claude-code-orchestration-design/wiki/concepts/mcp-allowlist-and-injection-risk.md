---
title: "MCP Allowlist and Injection Risk"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "mcp-allowlist-and-injection-risk"
source_refs:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch02-claude-code-orchestration-surface.md"
    source_hash: "505c6297d2c7198cbf0e77800577ab8e18a25d73"
    source_pointer: "B02-C013; MCP requires explicit trust evaluation and prompt-injection risk handling"
    source_storage_mode: "pointer_only"
  - source_id: "operator-phase1-review-decisions-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/operator-phase1-review-decisions-20260702.md"
    source_hash: "34d9c16967d2f7f49b716d75c8bb1a2a10eb96a7"
    source_pointer: "phase2_implications: MCP server allowlist and committed .mcp.json policy remain boundary/open question"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T14:30:00Z"
updated_at: "2026-07-02T14:30:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "needs_review"
---

# MCP Allowlist and Injection Risk

```yaml
pattern: "Every MCP server candidate needs an allowlist decision and injection-risk review before it becomes trusted infrastructure."
used_when:
  - "A proposed MCP server can read external content, write state, or expose privileged context."
not_used_when:
  - "The server is only being discussed as a deferred concept page."
reads:
  - "server identity"
  - "available tools"
  - "data read/write scope"
  - "external content exposure"
  - "operator trust decision"
writes:
  - "allow, reject, or defer decision candidate"
  - "risk notes"
token_efficiency:
  - "A server-level decision record prevents repeated ad hoc trust analysis."
drift_controls:
  - "External tool output is not accepted as doctrine without source and risk handling."
unresolved_or_deferred:
  - "Concrete allowlist schema."
  - "Injection-risk checklist."
  - "Runtime enforcement mechanism."
```
