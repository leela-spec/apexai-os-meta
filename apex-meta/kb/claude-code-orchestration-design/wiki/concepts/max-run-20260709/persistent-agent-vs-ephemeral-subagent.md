---
title: "Persistent Agent vs Ephemeral Subagent"
page_type: concept
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

# Persistent Agent vs Ephemeral Subagent

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - rank: 1
    source: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-sub-agents.md.md
    rationale: "Primary subagent source."
    coverage: "Subagent context, tool access, scope, built-ins, and custom agents."
```

## Macro / Meso / Micro

### Macro

An ephemeral subagent is a bounded context-isolation tool; a persistent production agent is a promoted runtime component.

### Meso

Use subagents for side research and context savings. Promote persistent agents only after source support, scope, tool limits, and validation are explicit.

### Micro

Do not import large agent libraries as production rosters by default.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Subagents run in separate context windows and return summaries to the main conversation."
    source_pointer: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-sub-agents.md.md
    confidence: high
    claim_label: source_backed_summary
```

## Routes Here

```yaml
routes:
  - question: "Should this be a persistent agent or an ephemeral subagent?"
    leads_to: apex-meta/kb/claude-code-orchestration-design/wiki/concepts/max-run-20260709/persistent-agent-vs-ephemeral-subagent.md
    rationale: "Agent persistence boundary."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Reopen before committing any persistent agent file."
    source_pointer: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-sub-agents.md.md
    proposed_handling: ask_operator
```
