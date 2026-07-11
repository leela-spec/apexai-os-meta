---
title: "Claude Code Plugins"
page_type: entity
kb_slug: claude-code-orchestration-design
run_id: max-run-20260709
status: needs_review
created_at: "2026-07-09"
updated_at: "2026-07-11"
source_policy: source_preserving
legacy_output_policy: old_pages_for_comparison_only
confidence: high
claim_label: source_backed_summary
source_refs:
  - source_path: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-plugins-reference.md.md
---

# Claude Code Plugins

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - rank: 1
    source: primary-code-claude-com-docs-en-plugins-reference.md.md
    rationale: "Primary plugin reference."
    coverage: "Plugin components, skills, agents, hooks, MCP servers, LSP servers, monitors."
```

## Macro / Meso / Micro

### Macro

Claude Code plugins are bundled distribution units for multiple extension components.

### Meso

Plugins can include skills, agents, hooks, MCP servers, LSP servers, and monitors, so they carry higher packaging and trust implications than a single skill.

### Micro

Use plugin packaging only when distribution or bundled components are required.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "A plugin is a self-contained directory of components that extends Claude Code."
    source_pointer: primary-code-claude-com-docs-en-plugins-reference.md.md
    confidence: high
    claim_label: source_backed_summary
```

## Routes Here

```yaml
routes:
  - question: "What are Claude Code plugins?"
    leads_to: apex-meta/kb/claude-code-orchestration-design/wiki/entities/max-run-20260709/claude-code-plugins.md
    rationale: "Plugin entity route."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Reopen before installing, creating, or distributing plugins."
    source_pointer: primary-code-claude-com-docs-en-plugins-reference.md.md
    proposed_handling: revisit_source
```
