---
title: "Three Package Boundary"
page_type: "concept"
kb_slug: "apex-plan-sync-session-workflow-v2"
concept_slug: "three-package-boundary"
source_refs:
  - source_id: "apex-plan-skill"
    source_path: "raw/other/SKILL.md"
    source_hash: "a83172f1d3f075273ca05a7e91254ed65ef77294a7519f74e94267c1ff3629cf"
    source_pointer: "lines 24-44, 78-90"
    source_storage_mode: "copy_into_kb"
  - source_id: "apex-sync-skill"
    source_path: "raw/notes/SKILL.md"
    source_hash: "698848fede4076f10bf3cca2e03d16ffbb9497e9fc9f8d03a851869a54af5b14"
    source_pointer: "lines 43-64, 111-152"
    source_storage_mode: "copy_into_kb"
  - source_id: "apex-session-skill"
    source_path: "raw/refs/SKILL.md"
    source_hash: "c45445a3499990275483e0103b7cfc7c1e5b35e7ed0c3ab48d3556fb6902537c"
    source_pointer: "lines 27-34, 186-208, 248-261"
    source_storage_mode: "copy_into_kb"
created_at: "2026-07-03T12:00:00Z"
updated_at: "2026-07-11T10:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - "isolation-with-overlap.md"
  - "proposal-computation-mutation-split.md"
related_entities:
  - "../entities/apex-plan.md"
  - "../entities/apex-sync.md"
  - "../entities/apex-session.md"
review_flags: []
---

# Three Package Boundary

## Definition

This project defines "boundary" as a disjoint partition of `process_scope` across three
packages, verified independently in each package's own SKILL.md rather than declared in one
place and trusted elsewhere. apex-plan owns exactly six process items: `PM1_capture_project`,
`PM2_decompose_project`, `PM3_assign_dependency_proposals`, `PD1_priority_policy`,
`PD2_urgency_policy`, `PD4_focus_recommendation_rationale` (SKILL.md lines 25-31). apex-sync
owns eight report types computed by `scripts/apex_sync.py` (SKILL.md lines 45-54). apex-session
owns seven process items: `PM6_update_status`, `KB1_write_session_progress`,
`KB2_extract_state_deltas`, `KB3_maintain_entity_files`, `KB6_produce_next_session_context`,
`PD5_operator_validation_for_mutation`, `PD6_feed_planning_layer` (SKILL.md lines 27-34). No
process-scope item appears as an "owned" item in more than one package's contract — this was
verified directly against all three live SKILL.md files during this KB run, not assumed from the
prior (untrusted) analysis.

## Operating Rules

```yaml
rules:
  - apex_plan_must_not: [run_scripts, compute_exact_next_task, traverse_dependency_graph, scan_blockers, rebuild_registry, mutate_state]
  - apex_sync_must_not: [capture_projects, decompose_work, mutate_task_status, author_handoff_files, validate_operator_decisions, write_session_narrative]
  - apex_session_must_not: [rank_tasks, scan_blockers, rebuild_registries, compute_scores, run_scripts, decompose_new_work]
  - each_package_boundary_is_self_declared: true
  - boundary_verification_method: "cross-read all three SKILL.md files and confirm no owned process_scope item recurs in another package's owns list"
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "plan-sync-session-interconnection"
    rationale: "This concept has a direct topic-registry entry; ranked sources come from manifests/phase0/topic-source-rankings.json's plan-sync-session-interconnection topic (keywords: handoff, boundary, gate, mutate, routing, three-package, operator-gated, proposal)."
    coverage: "Cross-package boundary and handoff evidence, script-ranked by real keyword hit-count."
  - source_id: "apex-hermes-workflow-example-database-master-of-arts-v0-1"
    rationale: "Top-ranked by hit-count (72 hits) for this topic's keywords, despite being from an unrelated research lineage — flagged in Uncertainty below since the ranking is keyword-driven, not relevance-judged."
    coverage: "Incidental keyword overlap (process, workflow terms), not a substantive source for this concept."
  - source_id: "apex-plan-skill"
    rationale: "31 hits — apex-plan's own boundary declaration (hands_off_to lists and must_not_create)."
    coverage: "One side of the three-way boundary assertion."
  - source_id: "apex-session-package-manifest"
    rationale: "31 hits — cross-references apex-session's package inventory against the boundary claims."
    coverage: "Package invariants supporting the boundary claim."
  - source_id: "apex-session-skill"
    rationale: "23 hits — apex-session's boundary_validation block, the most exhaustive of the three."
    coverage: "The routing step and 12-item forbidden-operations list."
```

## Macro / Meso / Micro

### Macro

The three-package boundary is what keeps a single conversational request from silently doing more
than the operator asked for. Without it, a system built from one LLM context could blur "I think
this should happen" (planning), "this is exactly true" (computation), and "this has been confirmed
to have happened" (mutation) into one undifferentiated output. The boundary forces those three
epistemic states to stay in three separate packages, each with its own completion gate.

### Meso

The boundary is asserted redundantly, not just once. apex-plan's `hands_off_to_apex_sync` /
`hands_off_to_apex_session` lists (SKILL.md lines 32-44) name what the other two packages are for;
apex-sync's Required Outputs (lines 45-54) and apex-session's routing step (line 188) independently
claim to be the receiving side of those same operations. This means a drift in any one file's
boundary claim — say, if apex-plan's hands-off list silently added an operation apex-sync's
Required Outputs list doesn't also claim — would be visible to a reader diffing the three
contracts against each other, even though no single package's own text would catch its own drift.
That cross-checkability, not the isolation alone, is the actual resilience property (see
Isolation With Overlap for the full argument).

### Micro

Concretely: apex-plan's `boundaries.must_not_create` (11 items, SKILL.md lines 78-90) is exactly
the union of its own two hands-off lists (6 + 5 items, lines 32-44) — verified item-for-item during
this KB run. apex-sync's `boundary_validation`-equivalent is distributed across its Objective
paragraph ("does not capture new projects, decompose work, mutate task status, author handoff
files, validate operator decisions, or create session narrative," SKILL.md lines 22-23) rather than
a single boolean block. apex-session's `boundary_validation` (SKILL.md lines 248-261) is the only
one of the three expressed as 12 explicit `no_*: true` booleans, the most granular of the three
formats.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "No process_scope item is claimed as 'owned' by more than one of apex-plan (6 items), apex-sync (8 report types), and apex-session (7 items) — confirmed by direct cross-read of all three live SKILL.md files during this KB run."
    source_pointer: "raw/other/SKILL.md lines 25-31; raw/notes/SKILL.md lines 45-54; raw/refs/SKILL.md lines 27-34"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C002
    claim: "apex-plan's must_not_create list is exactly the union of its own hands_off_to_apex_sync and hands_off_to_apex_session lists, with no gap and no extra restriction."
    source_pointer: "raw/other/SKILL.md lines 32-44 vs 78-90"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C003
    claim: "Each package's boundary is asserted from both the giving side and the receiving side — apex-plan names what it hands to apex-sync/apex-session, and apex-sync's Required Outputs plus apex-session's routing step independently claim to be the receiving side of those same named operations."
    source_pointer: "raw/other/SKILL.md lines 32-44; raw/notes/SKILL.md lines 45-54; raw/refs/SKILL.md line 188"
    confidence: high
    claim_label: source_backed_summary
```

## Routes Here

```yaml
routes:
  - question: "How does this boundary avoid becoming three isolated silos that silently drift apart?"
    leads_to: "isolation-with-overlap.md"
    rationale: "The redundant two-sided assertion described in Meso is the specific mechanism; Isolation With Overlap develops the full resilience argument."
  - question: "What exactly is apex-plan/apex-sync/apex-session individually responsible for?"
    leads_to: "../entities/apex-plan.md"
    rationale: "Each package's full contract is detailed on its own entity page."
  - related_page: "apex-plan-sync-session-workflow-v2/concepts/proposal-computation-mutation-split.md"
    relation: "This concept describes the WHO (which package owns what); that concept describes the WHAT (proposal vs. computed fact vs. confirmed mutation)."
```

## Evidence

```yaml
evidence:
  - source_id: "apex-plan-skill"
    source_pointer: "lines 25-44, 78-90"
    supports: "C001, C002"
  - source_id: "apex-sync-skill"
    source_pointer: "lines 45-54"
    supports: "C001, C003"
  - source_id: "apex-session-skill"
    source_pointer: "lines 27-34, 188"
    supports: "C001, C003"
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: >
      The plan-sync-session-interconnection topic's script-computed ranking places the
      Master-of-Arts workflow database file above several of apex-plan's/apex-session's own
      reference files, purely because generic keywords like "process" and "routing" appear
      frequently in that large, unrelated document. This is a keyword-frequency artifact, not a
      relevance judgment; flagged so a future reader does not assume the Master-of-Arts file is
      substantively about this concept.
    source_pointer: "manifests/phase0/topic-source-rankings.json, plan-sync-session-interconnection topic, rank 1"
    proposed_handling: leave_as_gap
```
