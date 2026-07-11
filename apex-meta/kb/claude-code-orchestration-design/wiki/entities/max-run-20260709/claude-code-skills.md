---
title: "Claude Code Skills"
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
  - source_path: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-skills.md.md
---

# Claude Code Skills

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - rank: 1
    source: primary-code-claude-com-docs-en-skills.md.md
    rationale: "Primary Claude Code skills source."
    coverage: "Creation, invocation, scopes, supporting files, dynamic context, frontmatter."
```

## Macro / Meso / Micro

### Macro

Claude Code skills are reusable instruction packages.

### Meso

They can be project, personal, enterprise, nested, or plugin-provided, and their descriptions guide invocation.

### Micro

Use them for repeatable procedures before escalating to hooks, plugins, MCP, or persistent agents.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Skills extend what Claude can do through SKILL.md instructions and optional supporting files."
    source_pointer: primary-code-claude-com-docs-en-skills.md.md
    confidence: high
    claim_label: source_backed_summary
```

## Routes Here

```yaml
routes:
  - question: "What are Claude Code skills?"
    leads_to: apex-meta/kb/claude-code-orchestration-design/wiki/entities/max-run-20260709/claude-code-skills.md
    rationale: "Skill entity route."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Reopen before creating or modifying actual SKILL.md files."
    source_pointer: primary-code-claude-com-docs-en-skills.md.md
    proposed_handling: revisit_source
```
