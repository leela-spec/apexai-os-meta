---
title: "Claude Code Mechanism Decision Model"
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

# Claude Code Mechanism Decision Model

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - rank: 1
    source: apex-meta/kb/claude-code-orchestration-design/ingest-analysis/max-run-20260709/02-claude-code-mechanisms-and-surfaces.md
    rationale: "Run-specific synthesis of skills, hooks, subagents, plugins, MCP, and .claude scope."
    coverage: "Primary mechanism routing evidence."
  - rank: 2
    source: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-skills.md.md
    rationale: "Skill package and invocation evidence."
    coverage: "Repeatable procedure surface."
  - rank: 3
    source: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-hooks.md.md
    rationale: "Lifecycle event evidence."
    coverage: "Automatic event surface."
```

## Macro / Meso / Micro

### Macro

Choose the smallest Claude Code surface that satisfies the job.

### Meso

Use KB pages for doctrine, skills for repeatable procedures, hooks for lifecycle events, subagents for context isolation, plugins for bundled distribution, and MCP for external tool connection.

### Micro

Queries about which mechanism to use route here before narrower concept pages.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Mechanism choice should follow required repeatability, enforcement, isolation, distribution, or external connectivity."
    source_pointer: apex-meta/kb/claude-code-orchestration-design/ingest-analysis/max-run-20260709/02-claude-code-mechanisms-and-surfaces.md
    confidence: high
    claim_label: source_backed_summary
```

## Routes Here

```yaml
routes:
  - question: "When should Claude Code use skills, hooks, plugins, subagents, or MCP?"
    leads_to: apex-meta/kb/claude-code-orchestration-design/wiki/summaries/max-run-20260709/claude-code-mechanism-decision-model.md
    rationale: "Primary mechanism-selection route."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Reopen raw mechanism docs before writing any runtime configuration."
    source_pointer: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/
    proposed_handling: revisit_source
```
