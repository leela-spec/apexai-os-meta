---
title: "Claude Code Hooks"
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
  - source_path: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-hooks.md.md
---

# Claude Code Hooks

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - rank: 1
    source: primary-code-claude-com-docs-en-hooks.md.md
    rationale: "Primary hooks source."
    coverage: "Hook lifecycle, events, handlers, matchers, decision outputs."
```

## Macro / Meso / Micro

### Macro

Claude Code hooks are event-triggered automation surfaces.

### Meso

Hooks can react to session, turn, tool-call, subagent, task, config, file, worktree, and MCP-related lifecycle events.

### Micro

This KB treats hooks as deterministic enforcement candidates, not general semantic instruction storage.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Hooks run automatically at defined Claude Code lifecycle events."
    source_pointer: primary-code-claude-com-docs-en-hooks.md.md
    confidence: high
    claim_label: source_backed_summary
```

## Routes Here

```yaml
routes:
  - question: "What are Claude Code hooks?"
    leads_to: apex-meta/kb/claude-code-orchestration-design/wiki/entities/max-run-20260709/claude-code-hooks.md
    rationale: "Hook entity route."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Reopen raw docs and run validation before writing hook config."
    source_pointer: primary-code-claude-com-docs-en-hooks.md.md
    proposed_handling: revisit_source
```
