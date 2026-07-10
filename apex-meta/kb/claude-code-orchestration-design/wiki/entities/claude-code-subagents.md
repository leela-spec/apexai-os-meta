---
title: "Claude Code Subagents"
page_type: entity
kb_slug: "claude-code-orchestration-design"
entity_slug: "claude-code-subagents"
entity_type: "runtime_component"
source_refs:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch02-claude-code-orchestration-surface.md"
    source_hash: "505c6297d2c7198cbf0e77800577ab8e18a25d73"
    source_pointer: "claims B02-C008 through B02-C009; entities extracted"
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

# Claude Code Subagents

## Identity

```yaml
entity:
  label: "Claude Code subagents"
  type: "runtime_component"
  aliases:
    - "Task subagents"
    - "sub-agents"
    - "context-isolated agents"
```

## Source-Grounded Summary

Subagents isolate exploratory or specialized work in separate context windows and return summaries to the main conversation, preserving main-thread context and enabling tool/model specialization (B02-C008). Claude Code ships built-in Explore and Plan subagents that are read-only/research-oriented and deliberately keep exploration results out of the main context, while general-purpose subagents can perform complex multi-step operations with broader tool access (B02-C009). Subagents are also a named entity in the Claude Code orchestration surface with a defined role — "context-isolated worker sessions with custom prompts, tools, models, and permissions" — extracted directly from the primary subagents documentation (B02 entities_extracted, `claude-code-subagents`). Subagent scope, discovery, and definition source are not uniform: they may be defined as persistent project/user files, or as ephemeral CLI/session definitions, and plugin-shipped agents carry additional restrictions relative to project/user-defined subagents (B02 source pointers, sub-agents.md.md lines 150-190 and 230-234; B02-T003).

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    rationale: "Sole cited source for this page; carries the primary-docs claims on subagent purpose, built-in types, discovery scope, and the plugin-agent restriction contradiction that most directly define this entity."
    coverage: "B02-C008 context isolation and delegation; B02-C009 built-in Explore/Plan/general-purpose types; B02-T003 plugin agent restrictions; B02-Q003 open question on subagent persistence; concepts_extracted subagent-context-isolation."
```

## Macro / Meso / Micro

### Macro

Subagents are Claude Code's delegation and context-isolation mechanism: a way to run specialized or exploratory work in a separate context window so the main conversation's context budget is preserved and so the subtask can carry different tools, permissions, or a different model than the main thread (B02-C008). In the layered control-plane model, subagents sit above skills — they are used when a task needs its own bounded context and possibly different capabilities, not merely a repeatable procedure that can run inline. This makes subagents the primary mechanism for "context isolation," distinct from hooks (enforcement), skills (repeatable procedure), and plugins (distribution).

### Meso

Claude Code differentiates subagent types by capability and risk profile. Built-in Explore and Plan subagents are read-only/research-oriented and are specifically designed to keep exploration results out of the main context — they return findings, not raw transcripts (B02-C009). General-purpose subagents, by contrast, can perform complex multi-step operations with broader tool access, trading some of that isolation-safety for capability (B02-C009). Subagent definitions are not all equal in provenance either: they can be scoped as project files, user files, plugin-shipped bundles, or ephemeral CLI/session definitions (sub-agents.md.md lines 150-190), and Claude Code enforces uniqueness/discovery rules across those scopes. Critically, plugin-shipped subagents are a restricted subset — they carry security restrictions and do not support every frontmatter field available to project- or user-defined subagents (B02-T003, sub-agents.md.md lines 230-234). This means "is this subagent trustworthy and fully-featured" depends on where it was defined, not just on its prompt.

### Micro

Source pointers: `primary-code-claude-com-docs-en-sub-agents.md.md` lines 7-14 (subagent definition and isolated context), lines 19-29 (benefits and delegation descriptions), lines 31-86 (built-in subagent types and restrictions), lines 88-148 (custom subagent quickstart), lines 150-190 (scope, discovery, uniqueness, plugin/CLI definitions), lines 230-234 (file-based frontmatter and plugin subagent caveat).

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Subagents isolate exploratory or specialized work in separate context windows and return summaries to the main conversation, preserving main-thread context and enabling tool/model specialization."
    source_pointer: "B02-C008; primary-code-claude-com-docs-en-sub-agents.md.md lines 7-14, 19-29"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C002
    claim: "Built-in Explore and Plan subagents are read-only/research-oriented and keep exploration results out of the main context, while general-purpose subagents can perform complex multi-step operations with broader tools."
    source_pointer: "B02-C009; primary-code-claude-com-docs-en-sub-agents.md.md lines 31-86"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C003
    claim: "Subagent definitions can be scoped as persistent project/user files, plugin-shipped bundles, or ephemeral CLI/session definitions, with discovery and uniqueness rules across those scopes."
    source_pointer: "sub-agents.md.md lines 150-190"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C004
    claim: "Plugin-shipped agents carry security restrictions and do not support every frontmatter field available to project/user subagents, so plugin subagents are a constrained subset rather than a full equivalent."
    source_pointer: "B02-T003; sub-agents.md.md lines 230-237; primary-code-claude-com-docs-en-plugins-reference.md.md lines 51-83"
    confidence: "medium"
    claim_label: "source_backed_summary"
```

## Routes Here

```yaml
routes:
  - question: "When should a task be delegated to a subagent instead of handled inline by a skill?"
    leads_to: "claude-code-orchestration-design/summaries/claude-mechanism-decision-model.md"
    rationale: "Subagents occupy the context-isolation rung of the mechanism ladder, between workflows and persistent agents/hooks."
  - related_page: "claude-code-orchestration-design/entities/claude-code-plugins.md"
    relation: "Plugin-shipped subagents are a restricted variant of project/user subagents (B02-T003); the plugins page covers the packaging side of the same tension."
```

## Evidence

```yaml
evidence:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_pointer: "B02-C008"
    supports: "Context isolation and delegation definition"
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_pointer: "B02-C009"
    supports: "Built-in Explore/Plan vs general-purpose subagent distinction"
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_pointer: "sub-agents.md.md lines 150-190"
    supports: "Persistence/scope and discovery model"
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_pointer: "B02-T003"
    supports: "Plugin subagent restriction"
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Which Apex subagent definitions should be persistent project files, and which should remain ephemeral CLI/session definitions? (B02-Q003, open question)"
    source_pointer: "B02-Q003"
    proposed_handling: "planning_task_candidate"
  - id: U002
    description: "Plugin-shipped subagents have security restrictions and an incomplete frontmatter surface relative to project/user subagents; any Apex design that assumes parity between plugin and project subagents should reopen this source (B02-T003)."
    source_pointer: "B02-T003"
    proposed_handling: "revisit_source"
  - id: U003
    description: "Operator Phase 1 review decided persistent subagents should be kept small and validated, reserved for repeated domain roles, stable validation/audit roles, or security-sensitive repo executors with explicit constraints; ephemeral subagents are for one-off scouting, comparison reading, or broad exploration. This decision is doctrine-adjacent but not yet implemented as an actual subagent roster."
    source_pointer: "operator-phase1-review-decisions-20260702.md Q004 (lines 74-84)"
    proposed_handling: "planning_task_candidate"
```
