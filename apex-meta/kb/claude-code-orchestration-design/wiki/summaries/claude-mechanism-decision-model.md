---
title: "Claude Mechanism Decision Model"
page_type: summary
kb_slug: "claude-code-orchestration-design"
summary_slug: "claude-mechanism-decision-model"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 112-123; claude_mechanism_mapping_index questions"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch02-claude-code-orchestration-surface.md"
    source_hash: "505c6297d2c7198cbf0e77800577ab8e18a25d73"
    source_pointer: "claims B02-C001 through B02-C016; concepts extracted"
    source_storage_mode: "pointer_only"
  - source_id: "operator-phase1-review-decisions-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/operator-phase1-review-decisions-20260702.md"
    source_hash: "34d9c16967d2f7f49b716d75c8bb1a2a10eb96a7"
    source_pointer: "lines 46-122; operator decisions"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Claude Mechanism Decision Model

```yaml
summary_id: claude_mechanism_decision_model
specialized_indexes:
  - claude_mechanism_mapping_index
pattern: >
  Select the least-powerful Claude Code mechanism that preserves source custody,
  safety, auditability, and token economy.
mechanism_order:
  - "markdown_or_yaml_artifact"
  - "skill"
  - "workflow"
  - "ephemeral_subagent"
  - "persistent_agent"
  - "deterministic_script"
  - "hook"
  - "plugin_or_mcp_later"
used_when:
  - "Choosing between guidance, procedure, delegation, enforcement, packaging, or external connectivity."
not_used_when:
  - "The operator asked only for Phase 2 compiled KB pages."
reads:
  - "official Claude Code surface claims"
  - "operator decisions"
writes:
  - "decision doctrine pages, not runtime files"
token_efficiency:
  - "Start with static artifacts and skills before persistent agents or plugins."
drift_controls:
  - "Soft guidance is not treated as hard enforcement."
  - "Hooks and scripts are reserved for high-risk gates."
unresolved_or_deferred:
  - "MCP allowlist, plugin packaging, and final persistent-agent roster remain later design tasks."
```

The decision model is a boundary map. It does not create hooks, workflows, MCP configuration, plugins, or agent files in S6.
