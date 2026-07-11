---
title: "Deterministic Executor Only Boundary"
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
  - source_path: .claude/skills/apex-kb/SKILL.md
---

# Deterministic Executor Only Boundary

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - rank: 1
    source: .claude/skills/apex-kb/SKILL.md
    rationale: "Defines execution_surface_policy."
    coverage: "External Agent/Codex role and semantic delegation rule."
```

## Macro / Meso / Micro

### Macro

External Agent Mode and Codex are not default semantic owners for Apex KB.

### Meso

They are used by default for live worktree script execution, Git-native patch application, deterministic postflight validation, and commit/push when connector or local git is required.

### Micro

Semantic delegation to those surfaces requires explicit operator override.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "External Agent/Codex role is deterministic_executor_only_by_default."
    source_pointer: .claude/skills/apex-kb/SKILL.md
    confidence: high
    claim_label: source_backed_summary
```

## Routes Here

```yaml
routes:
  - question: "When should Codex or Agent Mode be used?"
    leads_to: apex-meta/kb/claude-code-orchestration-design/wiki/concepts/max-run-20260709/deterministic-executor-only-boundary.md
    rationale: "Boundary for external executors."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Reopen only if operator explicitly changes semantic delegation policy."
    source_pointer: .claude/skills/apex-kb/SKILL.md
    proposed_handling: ask_operator
```
