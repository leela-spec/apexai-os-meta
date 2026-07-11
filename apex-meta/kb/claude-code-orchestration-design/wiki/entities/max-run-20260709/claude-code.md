---
title: "Claude Code"
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
  - source_path: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-claude-directory.md.md
---

# Claude Code

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - rank: 1
    source: primary-code-claude-com-docs-en-claude-directory.md.md
    rationale: "Primary source for Claude Code project configuration surfaces."
    coverage: ".claude directory, settings, hooks, skills, commands, subagents, workflows, rules, memory."
```

## Macro / Meso / Micro

### Macro

Claude Code is the local/project execution and configuration environment being modeled by this KB.

### Meso

It exposes multiple orchestration mechanisms: skills, hooks, subagents, plugins, MCP, settings, and project memory.

### Micro

The KB does not write Claude Code runtime config in this phase; it only compiles doctrine.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Claude Code reads project-level configuration and extension surfaces from the .claude directory and related files."
    source_pointer: primary-code-claude-com-docs-en-claude-directory.md.md
    confidence: high
    claim_label: source_backed_summary
```

## Routes Here

```yaml
routes:
  - question: "What is Claude Code in this orchestration KB?"
    leads_to: apex-meta/kb/claude-code-orchestration-design/wiki/entities/max-run-20260709/claude-code.md
    rationale: "Primary product entity."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Reopen current docs before making version-specific product claims."
    source_pointer: primary-code-claude-com-docs-en-claude-directory.md.md
    proposed_handling: revisit_source
```
