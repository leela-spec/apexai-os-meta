---
title: "apex-session"
page_type: "entity"
kb_slug: "apex-plan-sync-session-workflow-v2"
entity_slug: "apex-session"
entity_type: "tool"
source_refs:
  - source_id: "apex-session-skill"
    source_path: "raw/refs/SKILL.md"
    source_hash: "c45445a3499990275483e0103b7cfc7c1e5b35e7ed0c3ab48d3556fb6902537c"
    source_pointer: "lines 1-319 (full frontmatter, Skill Contract, Accepted Inputs, Final Outputs, Procedure, Validation Rules, Failure Modes, Completion Gate)"
    source_storage_mode: "copy_into_kb"
  - source_id: "apex-session-session-cluster-contract"
    source_path: "raw/refs/session-cluster-contract.md"
    source_hash: "ec87cfeff4df968cebd652706923125d4941d5ea5b250e87526884c30abfb3b0"
    source_pointer: "full file"
    source_storage_mode: "copy_into_kb"
  - source_id: "apex-session-mutation-gate-rules"
    source_path: "raw/refs/mutation-gate-rules.md"
    source_hash: "20d2c9181164788815c4bf92e76491f1240d95b48758b8a028228f14acdbd9ed"
    source_pointer: "full file"
    source_storage_mode: "copy_into_kb"
  - source_id: "apex-session-state-delta-and-entity-rules"
    source_path: "raw/refs/state-delta-and-entity-rules.md"
    source_hash: "6b2101477ec3cd53cb4018007ad0866eec2d39c8a02987746c720b34750662d9"
    source_pointer: "full file"
    source_storage_mode: "copy_into_kb"
  - source_id: "apex-session-handoff-and-next-session-contract"
    source_path: "raw/refs/handoff-and-next-session-contract.md"
    source_hash: "b16dca886f0bb3915e779890e415ed8cc7f6ae03c7e379df96068693090e35d3"
    source_pointer: "full file"
    source_storage_mode: "copy_into_kb"
created_at: "2026-07-03T12:00:00Z"
updated_at: "2026-07-11T09:57:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - "../concepts/three-package-boundary.md"
  - "../concepts/isolation-with-overlap.md"
  - "../concepts/operator-gated-phase-boundary.md"
review_flags: []
---

# apex-session

## Identity

```yaml
entity:
  label: "apex-session"
  type: "tool"
  aliases: ["C_SESSION", "H6 handoff artifact producer"]
  package_path: ".claude/skills/apex-session/"
  cluster: "C_SESSION"
  primary_role: "session_artifact_creation_and_gated_mutation_records"
```

## Source-Grounded Summary

`apex-session` is the confirmed-mutation and session-continuity layer of the three-package
system. It owns seven process items — `PM6_update_status`, `KB1_write_session_progress`,
`KB2_extract_state_deltas`, `KB3_maintain_entity_files`, `KB6_produce_next_session_context`,
`PD5_operator_validation_for_mutation`, and `PD6_feed_planning_layer` (SKILL.md lines 27-34) —
and produces exactly four final handoff files: `task_plan.md`, `findings.md`, `progress.md`, and
`next-session.md` (SKILL.md lines 39-43, 122-127). What this project specifically decides about
"session state" is that nothing consequential is confirmed by default: every status mutation
gets a `status_mutation_record` and a `before_after_preview` regardless of validation state
(SKILL.md lines 196-198), but the record only counts as confirmed once
`operator_validation: confirmed` is present (SKILL.md lines 236-240) — an unconfirmed mutation
stays visible in the record, not silently applied and not silently dropped. apex-session also
carries the strongest raw-source-preservation obligation of the three packages: it must preserve
every available `raw_source_ref`/`raw_source_path` and flag `source_conflict` rather than silently
resolving disagreement between sources (SKILL.md lines 192, 242-246).

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "apex-session-skill"
    rationale: "Top-ranked by Phase0 keyword hit-count (131 hits against session/handoff/mutation/gate/state/delta/entity/progress) — the authoritative contract, and the highest single-file hit count of any of the three skills' own SKILL.md files."
    coverage: "Full skill contract, accepted inputs, final outputs, 11-step procedure, validation rules, failure modes, completion gate."
  - source_id: "apex-session-package-manifest"
    rationale: "119 hits — package inventory, second-highest of any file in the apex-session set."
    coverage: "Final file set validation, source basis, package invariants."
  - source_id: "apex-session-session-cluster-contract"
    rationale: "94 hits — C_SESSION cluster-level boundary and routing rules."
    coverage: "Scope validation, routing apex-plan/apex-sync requests, final acceptance invariants."
  - source_id: "apex-session-state-delta-and-entity-rules"
    rationale: "65 hits — canonical source for state_delta_summary and entity_update_record schemas."
    coverage: "State delta extraction, entity maintenance, raw_source_ref preservation, conflict flagging."
  - source_id: "apex-session-handoff-and-next-session-contract"
    rationale: "56 hits — canonical source for the four H6 handoff artifacts and the planning_feed shape."
    coverage: "task_plan.md/findings.md/progress.md/next-session.md production rules, planning feed."
  - source_id: "apex-session-mutation-gate-rules"
    rationale: "53 hits — canonical source for status_mutation_record and operator_validation_record schemas."
    coverage: "before_after_preview, operator validation gate, status change reason."
```

## Macro / Meso / Micro

### Macro

apex-session is where the system's memory lives. apex-plan proposes and forgets (each packet is a
fresh proposal); apex-sync computes and reports (each report is a fresh snapshot); apex-session is
the only package whose output is meant to persist and accumulate across sessions — the four H6
files are explicitly refreshed, not recreated from nothing, and next-session.md exists specifically
to carry context forward to a future invocation of the whole system.

### Meso

apex-session's 11-step procedure (SKILL.md lines 186-208) opens with an explicit routing step that
has no equivalent in apex-plan's or apex-sync's own procedures: "If the request asks for new
decomposition, route to apex-plan. If it asks for ranking, blocker scan, registry rebuild, drift
detection, stale detection, or score computation, route to apex-sync" (line 188). This makes
apex-session's procedure the one place in the system where a single incoming request is expected
to be actively triaged across all three packages before any package does its own work — apex-plan
and apex-sync each declare what they refuse, but neither's procedure text contains an explicit
dispatch-to-a-named-sibling-package step the way apex-session's does. The `boundary_validation`
block (SKILL.md lines 248-261) is the largest explicit forbidden-operations list of the three
skills: 12 named booleans, effectively a superset covering both apex-plan's forbidden
decomposition and apex-sync's forbidden scoring/registry/drift/stale operations in one place.

### Micro

`next-session.md` has an exact, non-negotiable structure: precisely five sections — Current Step,
Open Items, Risks, Decisions Made, Next Actions (SKILL.md lines 229-234) — not a suggested outline
but a `next_session_sections_exact: true` validation rule (line 313). The
`operator_validation_values` enum (`confirmed`, `rejected`, `needs_revision`, `not_requested`,
SKILL.md lines 52-56) is a four-state gate, richer than a simple boolean confirm/reject — 
`needs_revision` and `not_requested` both keep a mutation record open rather than forcing an
immediate accept/deny decision.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "apex-session's step-1 procedure explicitly routes new-decomposition requests to apex-plan and ranking/blocker/registry/drift/stale/score requests to apex-sync, before doing any apex-session-specific work."
    source_pointer: "raw/refs/SKILL.md line 188"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C002
    claim: "apex-session must produce exactly four H6 handoff files (task_plan.md, findings.md, progress.md, next-session.md), and next-session.md must contain exactly five sections: Current Step, Open Items, Risks, Decisions Made, Next Actions."
    source_pointer: "raw/refs/SKILL.md lines 39-43, 122-127, 223-234, 313"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C003
    claim: "A status mutation record is created for every requested status change regardless of validation state, but only counts as confirmed once operator_validation: confirmed is present; needs_revision and not_requested both keep it open rather than accepted or rejected outright."
    source_pointer: "raw/refs/SKILL.md lines 52-56, 196-198, 236-240"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C004
    claim: "apex-session's boundary_validation block lists 12 distinct forbidden operations, the largest explicit boundary list of the three skills, spanning both apex-plan's and apex-sync's forbidden territory."
    source_pointer: "raw/refs/SKILL.md lines 248-261"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C005
    claim: "apex-session must preserve raw_source_ref and raw_source_path and flag source_conflict rather than silently resolving disagreement between sources or filling gaps from memory."
    source_pointer: "raw/refs/SKILL.md lines 190-192, 242-246, 276-278"
    confidence: high
    claim_label: source_backed_summary
```

## Routes Here

```yaml
routes:
  - question: "Which package decides where a mixed request should go?"
    leads_to: "../concepts/isolation-with-overlap.md"
    rationale: "C001 documents apex-session's unique explicit dispatch step, central to how the handoff triangle self-corrects."
  - question: "When does a status change actually count as final?"
    leads_to: "../concepts/proposal-computation-mutation-split.md"
    rationale: "C003's operator_validation gate is the specific mechanism that separates a recorded mutation from a confirmed one."
  - related_page: "apex-plan-sync-session-workflow-v2/entities/apex-plan.md"
    relation: "apex-plan hands off status mutation, entity updates, session progress logging, and next-session context to apex-session."
  - related_page: "apex-plan-sync-session-workflow-v2/concepts/operator-gated-phase-boundary.md"
    relation: "apex-session's operator_validation gate is one of three independent gate implementations this concept documents."
```

## Evidence

```yaml
evidence:
  - source_id: "apex-session-skill"
    source_pointer: "line 188"
    supports: "C001"
  - source_id: "apex-session-skill"
    source_pointer: "lines 39-43, 122-127, 223-234"
    supports: "C002"
  - source_id: "apex-session-skill"
    source_pointer: "lines 52-56, 196-198, 236-240"
    supports: "C003"
  - source_id: "apex-session-skill"
    source_pointer: "lines 248-261"
    supports: "C004"
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: >
      C001 and C004's characterization of apex-session as the system's "dispatcher" and having
      the broadest boundary list is a structural observation from static text comparison across
      the three SKILL.md files, not confirmed against a runtime trace of an actual mixed request
      being split three ways. Flagged for revisit if session-transcript evidence becomes
      available.
    source_pointer: "raw/refs/SKILL.md line 188, lines 248-261"
    proposed_handling: revisit_source
```
