---
title: "Isolation With Overlap"
page_type: "concept"
kb_slug: "apex-plan-sync-session-workflow-v2"
concept_slug: "isolation-with-overlap"
source_refs:
  - source_id: "apex-plan-skill"
    source_path: "raw/other/SKILL.md"
    source_hash: "a83172f1d3f075273ca05a7e91254ed65ef77294a7519f74e94267c1ff3629cf"
    source_pointer: "lines 24-90"
    source_storage_mode: "copy_into_kb"
  - source_id: "apex-sync-skill"
    source_path: "raw/notes/SKILL.md"
    source_hash: "698848fede4076f10bf3cca2e03d16ffbb9497e9fc9f8d03a851869a54af5b14"
    source_pointer: "lines 45-64, 111-152, 193-208"
    source_storage_mode: "copy_into_kb"
  - source_id: "apex-session-skill"
    source_path: "raw/refs/SKILL.md"
    source_hash: "c45445a3499990275483e0103b7cfc7c1e5b35e7ed0c3ab48d3556fb6902537c"
    source_pointer: "lines 186-208, 248-261"
    source_storage_mode: "copy_into_kb"
created_at: "2026-07-11T10:06:00Z"
updated_at: "2026-07-11T10:06:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - "three-package-boundary.md"
  - "operator-gated-phase-boundary.md"
  - "proposal-computation-mutation-split.md"
related_entities:
  - "../entities/apex-plan.md"
  - "../entities/apex-sync.md"
  - "../entities/apex-session.md"
review_flags: []
---

# Isolation With Overlap

## Definition

This project's resilience strategy is not "keep the three packages as separate as possible."
It is: keep `process_scope` ownership disjoint (isolation), while deliberately repeating three
specific things identically across all three packages (overlap) — a shared status vocabulary,
a mirrored (both-sides-asserted) boundary declaration, and a shared gate discipline. The overlap
is not accidental duplication left over from copy-pasting a template; each repetition serves a
distinct cross-check function that isolation alone cannot provide. This is the concrete mechanism
behind "isolated but redundantly overlapping so the orchestration system stays resilient."

## Operating Rules

```yaml
rules:
  - overlap_1_shared_vocabulary: "The H1 status enum (open, in-progress, blocked, done, deferred) is defined identically in apex-plan (status_enum), apex-sync (H1), and apex-session (allowed_status_values) -- verified character-for-character across all three live SKILL.md files in this KB run."
  - overlap_2_mirrored_boundary: "apex-plan's hands_off_to_apex_sync/hands_off_to_apex_session lists are independently claimed as received territory by apex-sync's Required Outputs and apex-session's routing step -- the same boundary is stated from both the giving and receiving side."
  - overlap_3_shared_gate_discipline: "apex-plan's operator_gate, apex-sync's dry-run default, and apex-session's operator_validation gate are three separately implemented instances of 'nothing consequential happens without an explicit confirming signal.'"
  - overlap_is_cross_check_not_duplication: "Each package validates a shared value (status) or claim (boundary) independently, using its own copy of the rule, rather than deferring to a shared authority -- so a bug or drift in one package's copy does not silently propagate to the others."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "plan-sync-session-interconnection"
    rationale: "Direct topic-registry entry for this concept's subject matter; ranked sources are script-computed from manifests/phase0/topic-source-rankings.json against keywords handoff/boundary/gate/mutate/routing/three-package/operator-gated/proposal."
    coverage: "Full cross-package handoff, boundary, and gate evidence."
  - source_id: "apex-plan-skill"
    rationale: "One side of the mirrored-boundary assertion; source of the hands_off_to_apex_sync/apex_session lists."
    coverage: "Giving-side boundary declaration."
  - source_id: "apex-sync-skill"
    rationale: "Receiving-side confirmation for apex-sync's portion of the handoff triangle, plus the dry-run gate implementation."
    coverage: "Required Outputs list; dry-run default gate."
  - source_id: "apex-session-skill"
    rationale: "Receiving-side confirmation for apex-session's portion of the handoff triangle, plus the operator_validation gate implementation and the unique explicit routing step."
    coverage: "Routing step; operator_validation gate; broadest boundary_validation block."
```

## Macro / Meso / Micro

### Macro

A system built from three packages that only isolate (never overlap) is brittle in a specific way:
if one package's internal declaration of its own boundary silently drifts — say, a future edit to
apex-plan's SKILL.md accidentally widens its `must_not_create` list to permit something it
shouldn't — nothing in a pure-isolation design would catch that, because no other package is
checking apex-plan's boundary against its own. Overlap fixes this by making each boundary claim,
and the shared vocabulary those claims are expressed in, independently verifiable from more than
one place. That is what makes the system "resilient" in the specific sense the operator who
commissioned this KB asked about: not fault-tolerance in a runtime-execution sense (this KB found
no runtime evidence — see Uncertainty below), but drift-tolerance in a documentation/contract
sense.

### Meso

The three overlaps serve three different cross-check purposes. The shared H1 status vocabulary
means any of the three packages could, in principle, validate a status value without needing to
trust another package's validation logic — a shared primitive, not a shared authority. The
mirrored boundary assertion means a reviewer (human or LLM) can catch drift by diffing the three
SKILL.md files against each other, which is exactly what this KB run did (see Key Claims on the
Three Package Boundary concept page) — and confirmed no drift currently exists. The shared gate
discipline means that even though the three gates have different shapes (a required field, a CLI
flag, an enum), an operator learning the system only has to learn one *principle*
("nothing happens by default") to correctly predict how all three packages behave at the moment
of consequential action.

### Micro

The most concrete evidence of deliberate (not accidental) overlap is that the boundary lists are
not merely similar in spirit but are asserted as the literal same operation names across files:
apex-plan's `hands_off_to_apex_sync` names `exact_next_task_computation`,
`dependency_graph_traversal`, `blocker_scan`, `registry_rebuild`, `drift_detection`,
`exact_priority_urgency_unlock_sorting` (SKILL.md lines 33-38); apex-sync's Required Outputs list
independently produces `next_action_report`, `dependency_validation_report`, `blocker_report`,
`registry_report`, `drift_report`, `score_report` (SKILL.md lines 45-54) — six names on one side
matching six report types on the other, verified by direct comparison during this KB run, not
inferred.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "The H1 status enum is defined identically, character-for-character, in all three packages' SKILL.md files, independently verified during this KB run rather than assumed from a shared source file."
    source_pointer: "raw/other/SKILL.md lines 46-53; raw/notes/SKILL.md lines 155-160; raw/refs/SKILL.md lines 45-50"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C002
    claim: "apex-plan's 6 named hands_off_to_apex_sync operations correspond one-to-one with 6 of apex-sync's 8 Required Output report types, verified by direct name comparison."
    source_pointer: "raw/other/SKILL.md lines 33-38; raw/notes/SKILL.md lines 45-54"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C003
    claim: "Three structurally different gate mechanisms (a required packet field, a CLI dry-run default, and a four-state validation enum) implement the same underlying principle -- no consequential action proceeds without an explicit confirming signal -- across the three packages."
    source_pointer: "raw/other/SKILL.md lines 243-249; raw/notes/SKILL.md lines 95-106; raw/refs/SKILL.md lines 52-56, 236-240"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C004
    claim: "This KB run found no drift between the three packages' mirrored boundary claims -- every operation named as handed-off by one package is claimed as received by the corresponding package, with no orphaned or mismatched operation names."
    source_pointer: "cross-comparison of raw/other/SKILL.md, raw/notes/SKILL.md, raw/refs/SKILL.md performed during this KB run"
    confidence: high
    claim_label: source_backed_summary
```

## Routes Here

```yaml
routes:
  - question: "How is 'the system stays resilient because agents are isolated but redundantly overlap' actually implemented, concretely?"
    leads_to: "three-package-boundary.md"
    rationale: "This page is the direct answer; Three Package Boundary supplies the underlying ownership-partition data this page's overlap argument is built on."
  - question: "Does this resilience claim have runtime evidence, or is it contract-level only?"
    leads_to: "../entities/apex-session.md"
    rationale: "apex-session's entity page documents the same runtime-evidence gap (U001) from a different angle -- the routing step is declared in text, not observed in a live transcript."
  - related_page: "apex-plan-sync-session-workflow-v2/concepts/operator-gated-phase-boundary.md"
    relation: "The gate discipline (overlap #3) is fully detailed on that page; this page treats it as one of three overlap mechanisms."
```

## Evidence

```yaml
evidence:
  - source_id: "apex-plan-skill"
    source_pointer: "lines 33-38, 46-53"
    supports: "C001, C002"
  - source_id: "apex-sync-skill"
    source_pointer: "lines 45-54, 95-106, 155-160"
    supports: "C001, C002, C003"
  - source_id: "apex-session-skill"
    source_pointer: "lines 45-50, 52-56, 236-240"
    supports: "C001, C003"
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: >
      This entire concept is documented at the contract level (what the three SKILL.md files
      declare) with no runtime evidence (no session transcript, log, or execution trace showing
      the overlap actually catching a real drift or a real cross-package request being routed
      correctly in practice). The resilience claim is therefore about documentation/contract
      consistency, not observed operational fault-tolerance. This should be revisited if
      transcript or log evidence of live multi-skill sessions becomes available to this KB.
    source_pointer: "no runtime source available to this KB"
    proposed_handling: revisit_source
  - id: U002
    description: >
      The operator's original framing also asked about a macro-to-meso-to-micro-and-back-up
      iterative workflow model. This KB found that structural pattern only at the level of how
      each individual SKILL.md is itself organized (frontmatter macro description -> Skill
      Contract meso detail -> Procedure/Failure Modes micro steps), and in the Master of Arts
      research's PRC-CORE-001 process description (intake -> goal contract -> ... -> revise ->
      learn). No source available to this KB describes a fully worked macro-meso-micro-meso-macro
      loop applied specifically to how apex-plan/apex-sync/apex-session jointly execute a complex
      multi-step goal end-to-end; this is a genuine content gap, not a claim this KB can make on
      current evidence.
    source_pointer: "no direct source found for a full macro-meso-micro-meso-macro worked example across all three packages"
    proposed_handling: leave_as_gap
```
