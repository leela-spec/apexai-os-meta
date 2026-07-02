---
title: "MCP Decision Model"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "mcp-decision-model"
source_refs:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch02-claude-code-orchestration-surface.md"
    source_hash: "505c6297d2c7198cbf0e77800577ab8e18a25d73"
    source_pointer: "B02-C012 through B02-C014; plugins bundle MCP, MCP external connectivity, layered control plane"
    source_storage_mode: "pointer_only"
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "claude_mechanism_mapping_index: when_plugin_or_mcp_is_deferred"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T14:30:00Z"
updated_at: "2026-07-02T14:30:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# MCP Decision Model

```yaml
pattern: "Choose MCP only after simpler local mechanisms are insufficient and external access is explicitly justified."
used_when:
  - "The capability requires live access to an external tool, API, database, repository service, or event channel."
  - "The integration needs a controlled tool interface rather than copied source material."
not_used_when:
  - "A compiled KB page, local file, project skill, deterministic report, or operator-mediated handoff is sufficient."
reads:
  - "capability need"
  - "external system boundary"
  - "data sensitivity"
  - "operator policy"
writes:
  - "decision record: use_local, defer_mcp, or propose_mcp_review"
  - "no runtime config in S6"
token_efficiency:
  - "MCP can reduce copied context but increases trust and policy overhead."
drift_controls:
  - "External content is not promoted into doctrine without source validation and injection-risk review."
unresolved_or_deferred:
  - "Which servers belong in an allowlist."
  - "How server permissions are reviewed."
  - "Whether MCP belongs in project or user scope for Apex."
```
