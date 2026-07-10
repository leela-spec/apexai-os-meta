---
title: "Claude Code Skills"
page_type: entity
kb_slug: "claude-code-orchestration-design"
entity_slug: "claude-code-skills"
entity_type: "runtime_component"
source_refs:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch02-claude-code-orchestration-surface.md"
    source_hash: "505c6297d2c7198cbf0e77800577ab8e18a25d73"
    source_pointer: "claims B02-C001 through B02-C004; entities extracted"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - "claude-code-orchestration-design/concepts/deterministic-script-boundary.md"
review_flags: []
---

# Claude Code Skills

## Identity

```yaml
entity:
  label: "Claude Code skills"
  type: "runtime_component"
  aliases:
    - "SKILL.md packages"
    - "Agent Skills (Claude Code runtime)"
```

## Source-Grounded Summary

Claude Code now treats custom commands and skills as the same underlying mechanism for new workflows; skills add supporting files, frontmatter controls, and automatic loading when relevant (B02-C001). Skills can live at enterprise, personal, project, nested-project, or plugin levels, and conflict resolution/command naming depends on that location, not solely on frontmatter (B02-C002). Skill content is optimized for progressive loading: descriptions are always visible, full content loads only when invoked, and supporting files stay separate until needed (B02-C003). Claude Code exposes runtime frontmatter controls such as `disable-model-invocation`, `user-invocable`, `allowed-tools`, `disallowed-tools`, `model`, `effort`, `context: fork`, `agent`, `hooks`, `paths`, and `shell` (B02-C004).

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    rationale: "Sole cited source for this page; primary-docs-derived claims covering skill/command convergence, location precedence, progressive loading, and runtime frontmatter controls."
    coverage: "B02-C001 through B02-C004; concepts_extracted skill-command-convergence."
```

## Macro / Meso / Micro

### Macro

Skills are Claude Code's mechanism for repeatable procedures: a compact activation surface (description, always visible) backed by fuller instructions and optional supporting files that load only when the skill is invoked. Because Claude Code has merged custom commands into skills for new work (B02-C001), skills are the default answer to "how do I make this procedure repeatable" in the Claude Code control plane, ahead of subagents, hooks, or plugins.

### Meso

Two structural facts shape how skills should be designed. First, location determines both discovery and precedence — enterprise, personal, project, nested-project, and plugin-level skills can coexist, and conflicts resolve by location rather than by frontmatter alone (B02-C002). Second, skills are built for progressive disclosure: the description is the only thing loaded by default, full `SKILL.md` content loads on invocation, and any supporting files should remain separate so they load only when actually needed (B02-C003). This progressive-loading design is also why skill descriptions function as routing keys rather than documentation.

### Micro

Source pointers: `primary-code-claude-com-docs-en-skills.md.md` lines 7-22 (skills extend Claude Code; commands merged into skills), lines 101-128 (skill locations and precedence), lines 130-168 (live change detection and discovery), lines 170-210 (content types and concision); continuation lines 3-36 (frontmatter fields and runtime controls), lines 37-68 (command-name derivation), lines 87-154 (supporting files, invocation control, post-activation lifecycle); `primary-code-claude-com-docs-en-claude-directory.md.md` lines 25-26.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Claude Code now treats custom commands and skills as the same underlying mechanism for new workflows; skills add supporting files, frontmatter controls, and automatic loading when relevant."
    source_pointer: "B02-C001; primary-code-claude-com-docs-en-skills.md.md lines 11-22"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C002
    claim: "Skills can live at enterprise, personal, project, nested project, or plugin levels; conflict resolution and command naming depend on location, not solely on frontmatter."
    source_pointer: "B02-C002; primary-code-claude-com-docs-en-skills.md.md lines 101-128"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C003
    claim: "Skill content is optimized for progressive loading: descriptions are always visible, full content loads when invoked, and supporting files should remain separate and only load when needed."
    source_pointer: "B02-C003; primary-code-claude-com-docs-en-skills.md.md lines 130-154"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C004
    claim: "Claude Code supports runtime frontmatter controls such as disable-model-invocation, user-invocable, allowed-tools, disallowed-tools, model, effort, context: fork, agent, hooks, paths, and shell."
    source_pointer: "B02-C004; primary-code-claude-com-docs-en-skills.md.md continuation lines 18-36"
    confidence: "high"
    claim_label: "source_backed_summary"
```

## Routes Here

```yaml
routes:
  - question: "What is the smallest Claude Code mechanism for a repeatable procedure?"
    leads_to: "claude-code-orchestration-design/summaries/claude-mechanism-decision-model.md"
    rationale: "Skills sit near the bottom of the mechanism ladder, right after plain markdown/YAML artifacts."
  - related_page: "claude-code-orchestration-design/entities/claude-code-workflows.md"
    relation: "Commands/workflows and skills converge under the same mechanism (B02-C001, B02-C016); the workflows page notes this is not a sharply separated entity."
```

## Evidence

```yaml
evidence:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_pointer: "B02-C001"
    supports: "Skill/command convergence"
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_pointer: "B02-C002"
    supports: "Location-based precedence"
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_pointer: "B02-C003"
    supports: "Progressive disclosure loading model"
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_pointer: "B02-C004"
    supports: "Runtime frontmatter controls"
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Claude Code's integrated command/skill mechanism creates a naming tension for Apex: commands/ files still work, but skills are recommended for new workflows; legacy command patterns should not be treated as first-class long-term architecture unless there is a migration reason (B02-C016, contradiction, medium confidence)."
    source_pointer: "B02-C016"
    proposed_handling: "planning_task_candidate"
  - id: U002
    description: "Which Apex gates require hook-level enforcement rather than skill-prose instruction only? (B02-Q001)"
    source_pointer: "B02-Q001"
    proposed_handling: "revisit_source"
  - id: U003
    description: "Should Apex package reusable orchestration surfaces as plain repo skills, plugins, or both? (B02-Q002)"
    source_pointer: "B02-Q002"
    proposed_handling: "planning_task_candidate"
```
