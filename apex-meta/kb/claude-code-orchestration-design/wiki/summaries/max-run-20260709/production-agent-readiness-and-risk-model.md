---
title: "Production Agent Readiness and Risk Model"
page_type: summary
kb_slug: claude-code-orchestration-design
run_id: max-run-20260709
status: needs_review
created_at: "2026-07-09"
updated_at: "2026-07-11"
source_policy: source_preserving
legacy_output_policy: old_pages_for_comparison_only
confidence: medium
claim_label: source_backed_summary
source_refs:
  - source_path: apex-meta/kb/claude-code-orchestration-design/ingest-analysis/max-run-20260709/03-orchestration-workflows-and-agent-boundaries.md
---

# Production Agent Readiness and Risk Model

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - rank: 1
    source: apex-meta/kb/claude-code-orchestration-design/ingest-analysis/max-run-20260709/03-orchestration-workflows-and-agent-boundaries.md
    rationale: "Run-specific synthesis of agent boundary evidence."
    coverage: "Small curated agent rosters, external-repo caution, source sprawl."
  - rank: 2
    source: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-sub-agents.md.md
    rationale: "Primary subagent source."
    coverage: "Built-in/custom subagent context and scope."
```

## Macro / Meso / Micro

### Macro

Production agents require a stronger gate than draft concepts because they can change execution behavior, context flow, or tool access.

### Meso

Readiness requires a clear task class, source-backed instructions, bounded tools, validation route, rollback/deprecation path, and explicit operator promotion from candidate to runtime component.

### Micro

Most candidate agents should remain examples or concept pages until an operator selects exact files and validation criteria.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Apex should keep production agent rosters small and operator-promoted, not auto-import large collections."
    source_pointer: apex-meta/kb/claude-code-orchestration-design/ingest-analysis/max-run-20260709/03-orchestration-workflows-and-agent-boundaries.md
    confidence: medium
    claim_label: source_backed_summary
```

## Routes Here

```yaml
routes:
  - question: "When is an agent ready for production use?"
    leads_to: apex-meta/kb/claude-code-orchestration-design/wiki/summaries/max-run-20260709/production-agent-readiness-and-risk-model.md
    rationale: "Risk and promotion route."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Reopen before promoting any candidate agent into .claude/agents or plugin distribution."
    source_pointer: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/notes/OrchestrationAgentsInCC_RepoResearch_IT3_GPT.md
    proposed_handling: ask_operator
```
