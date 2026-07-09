---
title: "Skill, Hook, Plugin, and MCP Boundaries"
page_type: summary
kb_slug: claude-code-orchestration-design
run_id: max-run-20260709
status: new_parallel_compile
source_policy: source_preserving
legacy_output_policy: old_pages_for_comparison_only
confidence: high
claim_label: source_backed_summary
source_refs:
  - source_path: apex-meta/kb/claude-code-orchestration-design/ingest-analysis/max-run-20260709/02-claude-code-mechanisms-and-surfaces.md
---

# Skill, Hook, Plugin, and MCP Boundaries

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - rank: 1
    source: apex-meta/kb/claude-code-orchestration-design/ingest-analysis/max-run-20260709/02-claude-code-mechanisms-and-surfaces.md
    rationale: "Batch analysis maps all mechanism surfaces."
    coverage: "Skills, hooks, plugins, MCP, subagents, .claude directory."
  - rank: 2
    source: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-plugins-reference.md.md
    rationale: "Plugin component source."
    coverage: "Plugin-bundled skills, agents, hooks, MCP servers, LSP servers, monitors."
```

## Macro / Meso / Micro

### Macro

The boundary is role-based: skills guide, hooks trigger, plugins bundle, MCP connects.

### Meso

Use skills for procedural knowledge; use hooks for automatic event reactions; use plugins only when multiple components should be distributed together; use MCP when the KB needs external system access.

### Micro

This page should not be used as permission to create any runtime file. It is a routing summary for mechanism comparison.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Skill, hook, plugin, and MCP surfaces should not collapse into one generic 'agent' mechanism."
    source_pointer: apex-meta/kb/claude-code-orchestration-design/ingest-analysis/max-run-20260709/02-claude-code-mechanisms-and-surfaces.md
    confidence: high
    claim_label: source_backed_summary
```

## Routes Here

```yaml
routes:
  - question: "What is the difference between skills, hooks, plugins, and MCP?"
    leads_to: apex-meta/kb/claude-code-orchestration-design/wiki/summaries/max-run-20260709/skill-hook-plugin-mcp-boundaries.md
    rationale: "Boundary overview."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Reopen raw docs before implementing any mechanism."
    source_pointer: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/
    proposed_handling: revisit_source
```
