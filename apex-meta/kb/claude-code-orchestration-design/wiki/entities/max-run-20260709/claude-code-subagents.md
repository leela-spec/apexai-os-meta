---
title: "Claude Code Subagents"
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
  - source_path: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-sub-agents.md.md
---

# Claude Code Subagents

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - rank: 1
    source: primary-code-claude-com-docs-en-sub-agents.md.md
    rationale: "Primary subagent source."
    coverage: "Custom subagents, built-ins, context windows, tool restrictions, scopes."
```

## Macro / Meso / Micro

### Macro

Claude Code subagents are specialized assistants that run in separate context windows.

### Meso

They are useful for side research, codebase exploration, planning, and complex multi-step tasks where the main conversation should stay focused.

### Micro

This KB treats subagents as bounded routing tools, not automatic persistent runtime truth.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Subagents preserve context by doing side work in their own context and returning summaries."
    source_pointer: primary-code-claude-com-docs-en-sub-agents.md.md
    confidence: high
    claim_label: source_backed_summary
```

## Routes Here

```yaml
routes:
  - question: "What are Claude Code subagents?"
    leads_to: apex-meta/kb/claude-code-orchestration-design/wiki/entities/max-run-20260709/claude-code-subagents.md
    rationale: "Subagent entity route."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Reopen before promoting any subagent template to a persistent project agent."
    source_pointer: primary-code-claude-com-docs-en-sub-agents.md.md
    proposed_handling: ask_operator
```
