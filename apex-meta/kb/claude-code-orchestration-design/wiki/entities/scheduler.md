---
title: "Scheduler"
page_type: entity
kb_slug: "claude-code-orchestration-design"
entity_slug: "scheduler"
entity_type: "runtime_trigger_component"
source_refs:
  - source_id: "phase1-batch03-external-orchestration-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch03-external-orchestration-patterns.md"
    source_hash: "dbe4e500d5c22cc61adc4e1364412da71d3db683"
    source_pointer: "B03-C001; scheduled tasks and routines listed in external feature-surface map"
    source_storage_mode: "pointer_only"
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "weekly_routine_case_index and project_execution_index recurring/state-flow questions"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T14:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "low"
claim_label: "working_hypothesis"
status: "needs_review"
related_concepts:
  - "scheduler-boundary"
  - "scheduler-deferment-rule"
related_entities: []
review_flags:
  - "no dedicated scheduler source was ingested in Phase 1 — this entity is an anticipated future orchestration surface, not a described system"
---

# Scheduler

## Identity

```yaml
entity:
  label: "Scheduler"
  type: "runtime_trigger_component"
  aliases:
    - "scheduled tasks"
    - "routines"
```

**Uncertainty notice:** "Scheduler" is not a Claude Code or external-repo entity that was directly ingested and analyzed in Phase 1. It is named here as an anticipated future Apex orchestration surface — something that will eventually need design — not as a system that any ingested source describes in depth. Treat this page's content as a placeholder boundary statement, not a specification.

## Source-Grounded Summary

The only Phase 1 evidence touching "scheduler" at all is a single row in the shanraisshan feature-surface map, which lists "scheduled tasks" and "routines" as named items alongside subagents, commands, skills, workflows, hooks, MCP, plugins, settings, and memory (B03-C001). The batch analysis pointer range for that claim covers only the navigational table listing (`README.md` lines 28-76); it does not describe how scheduling works, how triggers fire, how failures or missed runs are handled, or how a scheduler would interact with Apex's state and gate model. No other Phase 1 source (batch03 or batch04) discusses scheduling. Operator decision Q006 (`operator-phase1-review-decisions-20260702.md`) defers a related-sounding but distinct topic — tree-sitter/LSP repo-map extension — which is about code repo maps, not scheduling, and must not be cited as scheduler evidence.

Given this thin base, this entity page states only a role boundary derived by extension from Apex's general operator-gate and state-discipline doctrine (B04-C005, B04-C011, B04-C017): if a scheduler is built later, it should be a trigger layer, proposing that eligible work run, without carrying authority to accept or mutate state on its own.

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase1-batch03-external-orchestration-patterns"
    rationale: "The only Phase 1 source that names scheduling at all; ranked first because it is the sole direct (if extremely thin) evidentiary anchor."
    coverage: "B03-C001: a single row-item mention of 'scheduled tasks' and 'routines' in a comparative feature-surface table, with no mechanism detail."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "Internal Phase 2 planning note referencing recurring-loop and state-flow index topics in general Apex process terms; used only for continuity, not scheduler-mechanism evidence."
    coverage: "weekly_routine_case_index and project_execution_index sections on recurring planning loops and state flow, not scheduling infrastructure."
```

## Macro / Meso / Micro

### Macro

There is no ingested scheduler system to describe. This page exists so that future Phase 2 readers do not mistake silence for absence of the topic: scheduling was noted once, in passing, in a comparative external feature list, and nothing more.

### Meso

B03-C001's pointer range (README.md lines 28-76) documents a navigational table pattern where a repo maps features to implementation locations; "scheduled tasks" and "routines" are two of many row labels in that table, alongside "dynamic workflows" and "agent teams." None of these row labels were expanded into their own claims in batch03 beyond the initial table-mapping observation. No batch04 claim discusses scheduling at all — batch04 focuses on artifact contracts, operator gates, HALT/CLARIFY, and state discipline, none of which mention a scheduler component by name. The role/boundary content on this page is therefore an extension of that general doctrine to a hypothetical component, clearly labeled as such.

### Micro

- B03-C001: "The `claude-code-best-practice` repository organizes Claude Code concepts as a mapped surface: subagents, commands, skills, workflows, hooks, MCP, plugins, settings, memory, dynamic workflows, agent teams, scheduled tasks, and routines." (`README.md` lines 28-76)
- No batch04 claim mentions scheduling; B04-C005 (operator gates) and B04-C011/B04-C017 (state/verification discipline) are cited here only as the general doctrine this page extends by analogy.

## Key Claims

```yaml
key_claims:
  - claim_id: B03-C001
    claim: "The claude-code-best-practice repository organizes Claude Code concepts as a mapped surface including 'scheduled tasks' and 'routines' as named feature-table rows, with no mechanism, trigger, or failure-handling detail given."
    source_pointer: "phase1-batch03-external-orchestration-patterns.md; README.md lines 28-76"
    confidence: "medium"
    claim_label: "source_backed_summary"
  - claim_id: "SCHED-WH001"
    claim: "If Apex builds a scheduler in the future, it should function as a trigger layer only (propose that eligible work run) and should not carry authority to accept or mutate state on its own; this is an extension of general Apex operator-gate and state-discipline doctrine, not a claim about any described scheduler system."
    source_pointer: "extension of B04-C005, B04-C011, B04-C017; no scheduler-specific source"
    confidence: "low"
    claim_label: "working_hypothesis"
```

## Routes Here

```yaml
routes:
  - question: "Does Apex have a scheduler, and what would it be allowed to do?"
    leads_to: "claude-code-orchestration-design/concepts/scheduler-boundary.md"
    rationale: "Scheduler-boundary states the trigger-layer-only constraint this entity page anticipates; both pages share the same thin evidence base."
  - related_page: "claude-code-orchestration-design/concepts/scheduler-deferment-rule.md"
    relation: "Scheduler-deferment-rule explains why scheduler design (and this entity) stays deferred rather than being compiled as doctrine."
```

## Evidence

```yaml
evidence:
  - source_id: "phase1-batch03-external-orchestration-patterns"
    source_pointer: "README.md lines 28-76 (B03-C001)"
    supports: "Only direct Phase 1 mention of scheduling-adjacent terms"
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_pointer: "weekly_routine_case_index and project_execution_index sections"
    supports: "General recurring-loop/state-flow continuity framing, not scheduler mechanism detail"
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "No dedicated scheduler source was ingested in Phase 1. This entity page is a placeholder for an anticipated future orchestration surface, not a description of an actual system. A dedicated future source ingest on scheduling/trigger infrastructure (cron-like mechanisms, missed-run/deduplication policy, failure recovery, audit logging) is recommended before this page is promoted beyond low confidence."
    source_pointer: "absence noted across phase1-batch03-external-orchestration-patterns.md and phase1-batch04-apex-application-patterns.md"
    proposed_handling: "revisit_source"
  - id: U002
    description: "Operator decision Q006 (tree-sitter/LSP repo-map extension deferment) is superficially similar in shape ('defer until later') but is about code repo maps, not scheduling; it must not be cited as scheduler-specific evidence."
    source_pointer: "apex-meta/kb/claude-code-orchestration-design/log/operator-phase1-review-decisions-20260702.md; Q006_tree_sitter_lsp_repo_maps"
    proposed_handling: "leave_as_gap"
  - id: U003
    description: "Whether 'scheduler' should even be modeled as a single entity, versus multiple distinct trigger mechanisms (time-based, condition-based, manual reminder), is unresolved and should be an explicit operator question before further compile work."
    source_pointer: "n/a — no source distinguishes trigger mechanism types"
    proposed_handling: "ask_operator"
```
