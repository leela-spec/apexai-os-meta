---
title: "MCP Configuration and Trust Boundary"
page_type: summary
kb_slug: "claude-code-orchestration-design"
summary_slug: "mcp-configuration-and-trust-boundary"
source_refs:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch02-claude-code-orchestration-surface.md"
    source_hash: "505c6297d2c7198cbf0e77800577ab8e18a25d73"
    source_pointer: "claims B02-C012 through B02-C014; MCP connects external tools and requires trust evaluation"
    source_storage_mode: "pointer_only"
  - source_id: "operator-phase1-review-decisions-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/operator-phase1-review-decisions-20260702.md"
    source_hash: "34d9c16967d2f7f49b716d75c8bb1a2a10eb96a7"
    source_pointer: "Q005 MCP policy and phase2_implications lines 49-52, 95-100"
    source_storage_mode: "pointer_only"
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "claude_mechanism_mapping_index core question: when_plugin_or_mcp_is_deferred"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T14:30:00Z"
updated_at: "2026-07-02T14:30:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# MCP Configuration and Trust Boundary

```yaml
extension_package: "mcp_configuration_and_trust_boundary"
pattern: >
  MCP is an external connectivity layer, not a default orchestration layer. Apex
  should treat MCP configuration as deferred until server allowlists, trust
  boundaries, and prompt-injection handling are explicit.
used_when:
  - "A Claude Code process needs controlled access to external tools, databases, APIs, or event channels."
  - "A future implementation must decide whether a server belongs in project, user, or managed scope."
not_used_when:
  - "Compiled KB pages and source refs are sufficient."
  - "A local project skill, deterministic script, or manual operator gate can carry the work."
reads:
  - "MCP server purpose"
  - "trust boundary"
  - "allowlist decision"
  - "data exposure and prompt-injection risk"
writes:
  - "policy candidate or deferred decision record"
  - "no .mcp.json or runtime server config in this S6 extension"
token_efficiency:
  - "Use the compiled MCP entity and decision pages before opening raw MCP docs."
drift_controls:
  - "MCP policy remains deferred unless the operator explicitly approves a concrete server allowlist and config surface."
unresolved_or_deferred:
  - "Committed MCP JSON policy."
  - "Server allowlist."
  - "Trust review procedure."
  - "Injection-risk validation contract."
```

This summary extends the existing `entities/mcp.md` page without editing it.
