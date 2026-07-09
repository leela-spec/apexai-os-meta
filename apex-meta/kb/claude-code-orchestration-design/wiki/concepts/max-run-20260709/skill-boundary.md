---
title: "Skill Boundary"
page_type: concept
kb_slug: claude-code-orchestration-design
run_id: max-run-20260709
status: new_parallel_compile
source_policy: source_preserving
legacy_output_policy: old_pages_for_comparison_only
confidence: high
claim_label: source_backed_summary
source_refs:
  - source_path: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-skills.md.md
---

# Skill Boundary

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - rank: 1
    source: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-skills.md.md
    rationale: "Primary Claude Code skills source."
    coverage: "Skill purpose, scope, invocation, supporting files."
```

## Macro / Meso / Micro

### Macro

A skill is a reusable instruction package, not a scheduler, database, or unrestricted autonomous agent.

### Meso

Use a skill when a repeatable procedure or checklist would otherwise be pasted repeatedly or overload CLAUDE.md. Use supporting files for deeper references.

### Micro

A skill can include scripts and references, but its boundary should remain narrow and source-backed.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Skills are the preferred Claude Code mechanism for repeatable procedures with progressive disclosure."
    source_pointer: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-skills.md.md
    confidence: high
    claim_label: source_backed_summary
```

## Routes Here

```yaml
routes:
  - question: "When should something be a skill?"
    leads_to: apex-meta/kb/claude-code-orchestration-design/wiki/concepts/max-run-20260709/skill-boundary.md
    rationale: "Skill-specific boundary."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Reopen if a proposed skill also requires hooks, plugin packaging, or MCP."
    source_pointer: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-skills.md.md
    proposed_handling: revisit_source
```
