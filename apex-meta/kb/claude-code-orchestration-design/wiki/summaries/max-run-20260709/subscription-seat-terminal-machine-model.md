---
title: "Subscription, Seat, Terminal, and Machine Model"
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
  - source_path: apex-meta/kb/claude-code-orchestration-design/ingest-analysis/max-run-20260709/04-subscription-seat-terminal-and-machine-models.md
---

# Subscription, Seat, Terminal, and Machine Model

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - rank: 1
    source: apex-meta/kb/claude-code-orchestration-design/ingest-analysis/max-run-20260709/04-subscription-seat-terminal-and-machine-models.md
    rationale: "Run-specific scope analysis."
    coverage: "Project, personal, plugin, machine, and session boundaries."
  - rank: 2
    source: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-skills.md.md
    rationale: "Skill location/scope source."
    coverage: "Enterprise, personal, project, plugin skill placement."
```

## Macro / Meso / Micro

### Macro

Do not assume every Claude Code mechanism is equally portable across machines, users, workspaces, and organizations.

### Meso

Skills, settings, subagents, and plugin components have scope and trust boundaries. KB pages should document scope without making plan, price, or availability claims.

### Micro

Use this page when a query involves personal versus project scope, local settings, terminal execution, workspace trust, or whether a claim may depend on current product/version details.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Scope-sensitive Claude Code features require current verification before being treated as universal."
    source_pointer: apex-meta/kb/claude-code-orchestration-design/ingest-analysis/max-run-20260709/04-subscription-seat-terminal-and-machine-models.md
    confidence: medium
    claim_label: source_backed_summary
```

## Routes Here

```yaml
routes:
  - question: "Which Claude Code orchestration features depend on project, user, machine, or trust scope?"
    leads_to: apex-meta/kb/claude-code-orchestration-design/wiki/summaries/max-run-20260709/subscription-seat-terminal-machine-model.md
    rationale: "Scope and portability route."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Reopen official docs before making subscription, pricing, or availability claims."
    source_pointer: raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/
    proposed_handling: revisit_source
```
