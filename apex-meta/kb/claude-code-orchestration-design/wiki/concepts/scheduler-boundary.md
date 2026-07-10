---
title: "Scheduler Boundary"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "scheduler-boundary"
source_refs:
  - source_id: "phase1-batch03-external-orchestration-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch03-external-orchestration-patterns.md"
    source_hash: "dbe4e500d5c22cc61adc4e1364412da71d3db683"
    source_pointer: "B03-C001; scheduled tasks and routines appear in external feature-surface map"
    source_storage_mode: "pointer_only"
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "project_execution_index and weekly_routine_case_index: state flow and recurring loops"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T14:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "medium"
claim_label: "behavioral_inference"
status: "needs_review"
related_concepts:
  - "scheduler-deferment-rule"
  - "gated-write-side-mutation"
related_entities:
  - "scheduler"
review_flags:
  - "no dedicated scheduler source was ingested in Phase 1; this page is a boundary statement, not a mechanism description"
---

# Scheduler Boundary

## Definition

Phase 1 did not deep-dive scheduling infrastructure. The only direct evidence of "scheduling" as a topic is a single mention in the shanraisshan feature-surface map, which lists "scheduled tasks" and "routines" as row items alongside subagents, commands, skills, workflows, hooks, MCP, plugins, settings, and memory (B03-C001), with no depth on mechanism, triggering, or failure handling. Given that thin evidence base, this page defines a boundary rather than a mechanism: whatever a scheduler turns out to be, it is a trigger layer, not an authority layer — it may propose that a workflow run, but it does not itself carry the authority to accept, validate, or mutate state. That boundary rule is derived by extension from Apex's general operator-gate and state-discipline doctrine (B04-C005, B04-C011, B04-C017) applied to an as-yet-unspecified trigger component, not from any scheduler-specific source.

## Operating Rules

```yaml
rules:
  - "A scheduler is a trigger layer, not an authority layer."
  - "Used when a recurring workflow needs a time-based or condition-based start signal."
  - "Not used when the workflow has not defined read/write contracts, stop conditions, and operator gates."
  - "Reads: trigger condition, eligible workflow or packet, state source, stop condition."
  - "Writes: run request or reminder candidate only; no state mutation unless a separate, already-gated write contract allows it."
  - "Scheduler output is execution evidence, not accepted state (mirrors owner/validator separation, not scheduler-specific evidence)."
  - "Runtime scheduler mechanism and deduplication/missed-run policy remain unresolved and out of scope for this compile cycle."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase1-batch03-external-orchestration-patterns"
    rationale: "The only Phase 1 source that names scheduling at all, even briefly; ranked first because every other claim on this page is an extension rather than direct evidence."
    coverage: "B03-C001: a single row-item mention of 'scheduled tasks' and 'routines' inside a comparative external-repo feature map, with no mechanism detail."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "Internal Phase 2 planning note referencing recurring-loop and state-flow index topics; used only as continuity context, not as scheduler-mechanism evidence."
    coverage: "project_execution_index and weekly_routine_case_index sections describing recurring planning loops and state flow in general, not scheduling infrastructure specifically."
```

## Macro / Meso / Micro

### Macro

There is no ingested source that describes scheduler mechanics. What exists is (a) a one-line mention that an external repo's feature map includes "scheduled tasks" and "routines" as named surfaces, and (b) Apex's general doctrine that any write-side or state-changing action needs an operator gate and explicit contracts. This page states the boundary that follows from applying (b) to a hypothetical future scheduler component, while being explicit that (a) does not itself establish how such a component would work.

### Meso

B03-C001 shows that the shanraisshan repo treats "scheduled tasks" and "routines" as first-class named concepts in its navigational table, alongside subagents, commands, skills, workflows, hooks, MCP, plugins, settings, and memory — but the batch analysis pointer range (README.md lines 28-76) covers only the table listing, not an explanation of how scheduling is implemented or gated. No claim in batch03 or batch04 describes trigger mechanisms, cron-like scheduling, missed-run handling, or scheduler-to-workflow contracts. In the absence of that material, the only defensible content for this page is a boundary drawn from adjacent, better-evidenced Apex doctrine: operator gates (B04-C005) and state/verification discipline (B04-C011, B04-C017) should bound any future scheduler so that a trigger firing is never itself treated as an accepted state change.

### Micro

- B03-C001: "The `claude-code-best-practice` repository organizes Claude Code concepts as a mapped surface: subagents, commands, skills, workflows, hooks, MCP, plugins, settings, memory, dynamic workflows, agent teams, scheduled tasks, and routines." (`README.md` lines 28-76)
- Operator decision Q006 (`operator-phase1-review-decisions-20260702.md`) defers "tree-sitter/LSP repo map" work, which is a repo-map topic, not a scheduling topic — it is explicitly not evidence for scheduler mechanics and should not be conflated with this page's subject.

## Key Claims

```yaml
key_claims:
  - claim_id: B03-C001
    claim: "The claude-code-best-practice repository organizes Claude Code concepts as a mapped surface including scheduled tasks and routines as named feature-table rows, with no mechanism detail given."
    source_pointer: "phase1-batch03-external-orchestration-patterns.md; README.md lines 28-76"
    confidence: "medium"
    claim_label: "source_backed_summary"
  - claim_id: "SB-WH001"
    claim: "A future Apex scheduler should be bounded as a trigger layer only (propose a run), not an authority layer (accept or mutate state), by extension of Apex's operator-gate and state-discipline doctrine rather than by any scheduler-specific source."
    source_pointer: "extension of B04-C005, B04-C011, B04-C017 applied to an unevidenced future component"
    confidence: "low"
    claim_label: "working_hypothesis"
```

## Routes Here

```yaml
routes:
  - question: "If Apex adds a scheduler later, what must it not be allowed to do?"
    leads_to: "claude-code-orchestration-design/concepts/scheduler-deferment-rule.md"
    rationale: "Scheduler-deferment-rule states that scheduler design itself stays deferred until this boundary's preconditions (state contract, gates, failure model) are explicit."
  - related_page: "claude-code-orchestration-design/entities/scheduler.md"
    relation: "The scheduler entity page names the hypothetical component this boundary constrains."
  - related_page: "claude-code-orchestration-design/concepts/gated-write-side-mutation.md"
    relation: "The 'trigger layer, not authority layer' boundary is a specific case of the general gated-write-side-mutation rule."
```

## Evidence

```yaml
evidence:
  - source_id: "phase1-batch03-external-orchestration-patterns"
    source_pointer: "README.md lines 28-76 (B03-C001)"
    supports: "Only direct Phase 1 mention of scheduling-adjacent terms (scheduled tasks, routines)"
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_pointer: "project_execution_index and weekly_routine_case_index sections"
    supports: "General recurring-loop/state-flow framing used for continuity, not scheduler mechanism detail"
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "No Phase 1 source deep-dives scheduler mechanism, triggering model, or failure handling. This page's operating rules are derived by extension from unrelated Apex gate doctrine, not from a dedicated scheduler source."
    source_pointer: "absence noted across phase1-batch03-external-orchestration-patterns.md and phase1-batch04-apex-application-patterns.md"
    proposed_handling: "revisit_source"
  - id: U002
    description: "Operator decision Q006 (defer tree-sitter/LSP repo-map extension) is sometimes mistaken for a scheduler-related deferral; it is about code repo maps, not scheduling, and should not be cited as scheduler evidence."
    source_pointer: "apex-meta/kb/claude-code-orchestration-design/log/operator-phase1-review-decisions-20260702.md; Q006_tree_sitter_lsp_repo_maps"
    proposed_handling: "leave_as_gap"
  - id: U003
    description: "A dedicated future source ingest on scheduling/trigger infrastructure is recommended before this page's rules are promoted beyond a boundary statement."
    source_pointer: "n/a — recommendation based on absence of scheduler-specific sources in batch03/batch04"
    proposed_handling: "planning_task_candidate"
```
