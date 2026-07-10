---
title: "Scheduler Boundary and Deferment"
page_type: summary
kb_slug: "claude-code-orchestration-design"
summary_slug: "scheduler-boundary-and-deferment"
source_refs:
  - source_id: "phase1-batch03-external-orchestration-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch03-external-orchestration-patterns.md"
    source_hash: "dbe4e500d5c22cc61adc4e1364412da71d3db683"
    source_pointer: "B03-C001; external feature surface mentions scheduled tasks and routines"
    source_storage_mode: "pointer_only"
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "weekly_routine_case_index and project_execution_index; recurring planning loops, state flow, gated mutation"
    source_storage_mode: "pointer_only"
  - source_id: "operator-phase1-review-decisions-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/operator-phase1-review-decisions-20260702.md"
    source_hash: "34d9c16967d2f7f49b716d75c8bb1a2a10eb96a7"
    source_pointer: "avoid_in_phase2: no operational orchestration system built; no runtime hooks/workflows/plugins"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T14:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "low"
claim_label: "working_hypothesis"
status: "needs_review"
related_concepts:
  - "scheduler-boundary"
  - "scheduler-deferment-rule"
related_entities:
  - "scheduler"
review_flags:
  - "Phase 1 did not deep-dive scheduling infrastructure; this summary compiles a thin evidence base honestly rather than inventing scheduler mechanics"
---

# Scheduler Boundary and Deferment

## Core Summary

**Uncertainty notice, stated up front:** Phase 1 did not conduct a dedicated deep-dive on scheduling or trigger infrastructure. This summary exists to state that plainly, compile the one thin mention that does exist, and record why scheduler design stays deferred rather than becoming Phase 2 doctrine — it is not a synthesis of rich source material.

The only direct evidence is a single row-item mention of "scheduled tasks" and "routines" inside an external repo's comparative feature-surface map (B03-C001, `phase1-batch03-external-orchestration-patterns.md`). No batch04 claim, and no other batch03 claim, describes scheduler mechanism, trigger model, failure handling, or state-mutation authority. Separately, the operator decision log is explicit and high-confidence that Phase 2 must not pretend the operational orchestration system has been built and must not turn deferred implementation work into current doctrine (`operator-phase1-review-decisions-20260702.md`, `phase2_implications.avoid_in_phase2`). Scheduling is a clean case of exactly that kind of deferred implementation work: it was named once, in passing, in a comparative source, and nowhere else — so this summary treats it as a boundary/deferment topic rather than a described feature.

## What This Adds

```yaml
adds:
  - "An explicit statement that scheduling was not deep-dived in Phase 1, so future readers do not mistake this KB's silence for a settled design."
  - "A boundary rule, derived by extension from Apex's general operator-gate doctrine, that any future scheduler should be a trigger layer only, not a state-mutation authority."
clarifies:
  - "Operator decision Q006 (tree-sitter/LSP repo-map deferment) is unrelated to scheduling despite a superficially similar 'defer until later' shape; it concerns code repo maps."
  - "This summary's confidence is deliberately low because it rests on a single passing mention (B03-C001) plus general-doctrine extension, not on scheduler-specific source material."
limits:
  - "No scheduler runtime mechanism, trigger model, deduplication policy, or failure/recovery semantics is described anywhere in this KB."
  - "This page should not be cited as evidence that Apex has designed, or is close to designing, a scheduler."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "operator-phase1-review-decisions-20260702"
    rationale: "Primary, explicit, high-confidence operator policy establishing the general deferment doctrine (avoid turning deferred implementation work into current doctrine, avoid pretending the system is built); ranked first because it is the strongest single piece of grounding on this page, even though it does not name scheduling specifically."
    coverage: "Section 3 phase2_implications.avoid_in_phase2 and phase2_implications.write_as_boundary_or_open_question."
  - source_id: "phase1-batch03-external-orchestration-patterns"
    rationale: "The only source that names scheduling at all; ranked second because its coverage is a single row-item mention with no depth."
    coverage: "B03-C001: 'scheduled tasks' and 'routines' listed as feature-table rows in a comparative external repo README."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "Internal Phase 2 planning note on recurring-loop and state-flow index topics; ranked third and used only for continuity, not as scheduler-mechanism evidence."
    coverage: "weekly_routine_case_index and project_execution_index sections on recurring planning loops and gated state flow in general Apex process terms."
```

## Macro / Meso / Micro

### Macro

Scheduling is named in exactly one place across both Phase 1 batches (a passing mention in a comparative feature table) and is never analyzed as a mechanism. Apex's general operator-review doctrine already tells Phase 2 what to do with topics like this: do not turn them into doctrine, keep them as open boundaries, and do not simulate a build that has not happened. This summary applies that doctrine to scheduling explicitly so the gap is visible rather than silently papered over.

### Meso

B03-C001 documents that the shanraisshan `claude-code-best-practice` README organizes Claude Code concepts into a navigational table that includes "scheduled tasks" and "routines" as row labels, alongside subagents, commands, skills, workflows, hooks, MCP, plugins, settings, and memory. The batch03 analysis pointer range for this claim (lines 28-76) covers only the table listing itself. Separately, the operator decision log's `phase2_implications.avoid_in_phase2` list explicitly names "pretending the operational orchestration system has been built" and "turning deferred implementation work into current doctrine" as things to avoid; while scheduling is not named in that list, it fits the pattern of a topic that has surface-level mention but no reviewed depth. The `scheduler-boundary` concept page derives a trigger-layer-only constraint from Apex's general operator-gate doctrine (B04-C005, B04-C011, B04-C017) by extension, and the `scheduler-deferment-rule` concept page states why that design work stays deferred. This summary exists to tie those two thin, honestly-labeled concept pages together with the scheduler entity page into one topic view.

### Micro

- B03-C001: "The `claude-code-best-practice` repository organizes Claude Code concepts as a mapped surface: subagents, commands, skills, workflows, hooks, MCP, plugins, settings, memory, dynamic workflows, agent teams, scheduled tasks, and routines." (`README.md` lines 28-76)
- Operator decision log: "pretending the operational orchestration system has been built"; "turning deferred implementation work into current doctrine." (`operator-phase1-review-decisions-20260702.md`, `phase2_implications.avoid_in_phase2`)
- Operator decision log Q006: `defer_phase0_v1_5_code_repo_map_extension` — about tree-sitter/LSP code repo maps, not scheduling; cited here only to explicitly rule it out as scheduler evidence.

## Key Claims

```yaml
key_claims:
  - claim_id: B03-C001
    claim: "The claude-code-best-practice repository organizes Claude Code concepts as a mapped surface including 'scheduled tasks' and 'routines' as named feature-table rows, with no mechanism, trigger, or failure-handling detail given."
    source_pointer: "phase1-batch03-external-orchestration-patterns.md; README.md lines 28-76"
    confidence: "medium"
    claim_label: "source_backed_summary"
    used_in_pages:
      - "claude-code-orchestration-design/concepts/scheduler-boundary.md"
      - "claude-code-orchestration-design/entities/scheduler.md"
  - claim_id: "OPD-C001"
    claim: "Phase 2 must avoid turning deferred implementation work into current doctrine and must not present the operational orchestration system as already built."
    source_pointer: "operator-phase1-review-decisions-20260702.md; phase2_implications.avoid_in_phase2"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages:
      - "claude-code-orchestration-design/concepts/scheduler-deferment-rule.md"
  - claim_id: "SBD-WH001"
    claim: "Scheduling should be treated as deferred implementation work rather than compiled doctrine, on the same logic the operator applied to named deferred items (e.g. the tree-sitter/LSP repo-map extension), even though scheduling itself was never named as an explicit operator decision point."
    source_pointer: "extension of operator-phase1-review-decisions-20260702.md deferment pattern; no scheduler-specific source"
    confidence: "low"
    claim_label: "working_hypothesis"
    used_in_pages:
      - "claude-code-orchestration-design/concepts/scheduler-boundary.md"
      - "claude-code-orchestration-design/concepts/scheduler-deferment-rule.md"
      - "claude-code-orchestration-design/entities/scheduler.md"
```

## Routes Here

```yaml
routes:
  - question: "Does this KB have anything to say about how Apex schedules recurring work?"
    leads_to: "claude-code-orchestration-design/summaries/scheduler-boundary-and-deferment.md"
    rationale: "This is the single compiled entry point for the (thin) scheduler topic, linking the boundary concept, the deferment-rule concept, and the scheduler entity page."
  - related_page: "claude-code-orchestration-design/concepts/scheduler-boundary.md"
    relation: "States the trigger-layer-only constraint this summary compiles."
  - related_page: "claude-code-orchestration-design/concepts/scheduler-deferment-rule.md"
    relation: "States why scheduler design work stays deferred rather than becoming doctrine."
  - related_page: "claude-code-orchestration-design/entities/scheduler.md"
    relation: "Names the hypothetical component these boundary and deferment rules apply to."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "No Phase 1 source deep-dives scheduler mechanism, trigger model, deduplication/missed-run policy, or failure recovery. This summary and its linked concept/entity pages are boundary statements built on a single passing mention plus general-doctrine extension, not a synthesis of rich scheduler-specific material."
    source_pointer: "absence noted across phase1-batch03-external-orchestration-patterns.md and phase1-batch04-apex-application-patterns.md"
    proposed_handling: "revisit_source"
  - id: U002
    description: "A dedicated future source ingest on scheduling/trigger infrastructure (e.g. reading a scheduler-focused external repo or Claude Code's own scheduled-task/routine feature documentation in depth) is recommended before this topic is promoted beyond low confidence."
    source_pointer: "n/a — recommendation based on absence of scheduler-specific sources in batch03/batch04"
    proposed_handling: "planning_task_candidate"
  - id: U003
    description: "Operator decision Q006 (tree-sitter/LSP repo-map deferment) is superficially similar in shape to a scheduler deferment but is about code repo maps, not scheduling; conflating the two would misattribute operator intent."
    source_pointer: "apex-meta/kb/claude-code-orchestration-design/log/operator-phase1-review-decisions-20260702.md; Q006_tree_sitter_lsp_repo_maps"
    proposed_handling: "leave_as_gap"
```
