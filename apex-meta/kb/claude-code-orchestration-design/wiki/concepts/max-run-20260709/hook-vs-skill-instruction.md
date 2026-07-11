---
title: "Hook vs Skill Instruction"
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
  - source_path: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-hooks.md.md
  - source_path: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-skills.md.md
---

# Hook vs Skill Instruction

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - rank: 1
    source: primary-code-claude-com-docs-en-hooks.md.md
    rationale: "Defines lifecycle events and hook behavior."
    coverage: "Automatic event-triggered actions."
  - rank: 2
    source: primary-code-claude-com-docs-en-skills.md.md
    rationale: "Defines skill behavior."
    coverage: "User/model-invoked instruction packages."
```

## Macro / Meso / Micro

### Macro

A skill tells Claude how to do a repeatable task; a hook reacts at a lifecycle point.

### Meso

Use a skill when reasoning and instructions are needed. Use a hook when an event should automatically run a bounded check or handler.

### Micro

Do not use a hook merely to smuggle general instructions into every turn.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Skills are instruction packages; hooks are lifecycle event handlers."
    source_pointer: raw Claude Code skills and hooks docs
    confidence: high
    claim_label: source_backed_summary
```

## Routes Here

```yaml
routes:
  - question: "Should this be a hook or a skill?"
    leads_to: apex-meta/kb/claude-code-orchestration-design/wiki/concepts/max-run-20260709/hook-vs-skill-instruction.md
    rationale: "Instruction versus lifecycle boundary."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Reopen before implementing hook config because this page is doctrinal routing only."
    source_pointer: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-hooks.md.md
    proposed_handling: revisit_source
```
