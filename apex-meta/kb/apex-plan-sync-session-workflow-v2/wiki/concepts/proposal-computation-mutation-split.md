---
title: "Proposal Computation Mutation Split"
page_type: "concept"
kb_slug: "apex-plan-sync-session-workflow-v2"
concept_slug: "proposal-computation-mutation-split"
source_refs:
  - source_id: "apex-plan-skill"
    source_path: "raw/other/SKILL.md"
    source_hash: "a83172f1d3f075273ca05a7e91254ed65ef77294a7519f74e94267c1ff3629cf"
    source_pointer: "lines 60-71, 192-249"
    source_storage_mode: "copy_into_kb"
  - source_id: "apex-sync-skill"
    source_path: "raw/notes/SKILL.md"
    source_hash: "698848fede4076f10bf3cca2e03d16ffbb9497e9fc9f8d03a851869a54af5b14"
    source_pointer: "lines 78-109, 153-176"
    source_storage_mode: "copy_into_kb"
  - source_id: "apex-session-skill"
    source_path: "raw/refs/SKILL.md"
    source_hash: "c45445a3499990275483e0103b7cfc7c1e5b35e7ed0c3ab48d3556fb6902537c"
    source_pointer: "lines 45-56, 196-208, 236-246"
    source_storage_mode: "copy_into_kb"
created_at: "2026-07-03T12:00:00Z"
updated_at: "2026-07-11T10:02:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - "three-package-boundary.md"
  - "operator-gated-phase-boundary.md"
related_entities:
  - "../entities/apex-plan.md"
  - "../entities/apex-sync.md"
  - "../entities/apex-session.md"
review_flags: []
---

# Proposal Computation Mutation Split

## Definition

This project treats "proposal," "computed fact," and "confirmed mutation" as three distinct
epistemic states that must never collapse into each other silently. A proposal (apex-plan's
output) is a qualitative judgment an operator has not yet reviewed. A computed fact (apex-sync's
output) is an exact, script-derived value that has not been acted upon. A confirmed mutation
(apex-session's output) is a state change an operator has explicitly validated. The same
underlying field can pass through all three states — priority is a clear example: apex-plan
assigns a qualitative `high`/`medium`/`low` value with rationale (SKILL.md lines 60-66), apex-sync
computes the exact numeric ranking from the same weights (`high: 3, medium: 2, low: 1`), and only
apex-session can turn a resulting status change into a confirmed record once
`operator_validation: confirmed` is present.

## Operating Rules

```yaml
rules:
  - proposal_is_not_computed_truth: "apex-plan's dependency_plan and priority_urgency_focus_rationale are explicitly qualitative-only and must not compute exact ranking (apex-plan SKILL.md lines 220-229)."
  - computed_fact_is_not_a_mutation: "apex-sync's 8 reports are read-side outputs; only the single registry write exception may touch disk, and only via an explicit --dry-run false flag (apex-sync SKILL.md lines 95-106)."
  - mutation_requires_confirmation: "A status_mutation_record exists even when operator_validation is missing/rejected/needs_revision, but stays unconfirmed until operator_validation: confirmed (apex-session SKILL.md lines 196-198, 236-240)."
  - same_field_three_ownership_tiers: "priority/urgency fields are proposed qualitatively by apex-plan, computed exactly by apex-sync, and only recorded as a confirmed change by apex-session."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "plan-sync-session-interconnection"
    rationale: "This concept maps directly onto the plan-sync-session-interconnection topic-registry entry; ranked sources come from manifests/phase0/topic-source-rankings.json (script-computed, not hand-picked)."
    coverage: "Cross-package handoff and gate evidence."
  - source_id: "apex-plan-priority-urgency-focus-policy"
    rationale: "71 hits under the apex-plan-contract topic — the canonical source for the qualitative half of the priority/urgency split."
    coverage: "Qualitative priority/urgency/focus rationale rules that apex-plan must stay within."
  - source_id: "apex-sync-scoring-and-focus-rules"
    rationale: "51 hits under the apex-sync-contract topic — the canonical source for the exact-computation half of the same split."
    coverage: "Exact priority/urgency/unlock-depth/focus-candidate computation rules."
  - source_id: "apex-session-mutation-gate-rules"
    rationale: "53 hits under the apex-session-contract topic — the canonical source for the confirmation half of the split."
    coverage: "status_mutation_record and operator_validation_record schemas."
```

## Macro / Meso / Micro

### Macro

This split exists so that an LLM's plausible-sounding proposal, a script's exact computation, and
a human-confirmed fact are never visually or structurally indistinguishable in the system's
output. If they were, an operator skimming output could mistake a qualitative recommendation for
settled truth, or an exact computed report for an already-applied change.

### Meso

Each package enforces the split from its own side rather than relying on a shared arbiter.
apex-plan enforces it by refusing to compute (`do_not_compute_exact_ranking: true`,
`do_not_compute_graph_traversal: true`, SKILL.md lines 224, 229) — it cannot violate the split even
if asked to, because it has no script execution surface at all (`scripts_allowed: false`). apex-sync
enforces it by refusing to author narrative or mutate anything beyond its one write exception —
its outputs are named "reports," never "decisions" or "changes." apex-session enforces it by
gating confirmation behind an explicit four-state `operator_validation` field rather than treating
"a status change was requested" as equivalent to "a status change happened."

### Micro

The clearest concrete instance is the `depends_on` field: apex-plan records it as a proposal
(`integer_array`, "All task IDs listed... must have status done before the task is actionable" is
stated as a *rule apex-plan records but does not enforce*, apex-plan SKILL.md lines 55-58);
apex-sync computes actionability against that exact rule (apex-sync SKILL.md lines 163-167); only
apex-session's mutation records, once confirmed, represent the field having actually changed state
for a real task file. No single package both proposes and confirms the same field.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "apex-plan's priority_urgency_focus_rationale output must be qualitative-only and must explicitly not compute exact ranking or graph traversal."
    source_pointer: "raw/other/SKILL.md lines 220-229"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C002
    claim: "A status_mutation_record and before_after_preview are created for every requested status change in apex-session regardless of validation outcome, but the record counts as confirmed only once operator_validation: confirmed is recorded."
    source_pointer: "raw/refs/SKILL.md lines 196-198, 236-240"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C003
    claim: "The priority_policy weights (high=3, medium=2, low=1) are the same values in both apex-plan's and apex-sync's contracts, with role ownership split explicitly: apex-plan assigns qualitative rationale, apex-sync computes exact ranking from the same weights."
    source_pointer: "raw/other/SKILL.md lines 60-66"
    confidence: high
    claim_label: source_backed_summary
```

## Routes Here

```yaml
routes:
  - question: "If apex-plan records depends_on, why doesn't it check whether the dependency is satisfied?"
    leads_to: "../entities/apex-sync.md"
    rationale: "apex-sync is the package that evaluates actionability against the H1 status enum and depends_on targets."
  - question: "When is a status change actually final?"
    leads_to: "operator-gated-phase-boundary.md"
    rationale: "The operator_validation gate is one specific instance of the broader operator-gating pattern documented there."
  - related_page: "apex-plan-sync-session-workflow-v2/concepts/three-package-boundary.md"
    relation: "That concept documents WHO owns what; this concept documents WHAT KIND of claim each package's output represents."
```

## Evidence

```yaml
evidence:
  - source_id: "apex-plan-skill"
    source_pointer: "lines 60-66, 220-229"
    supports: "C001, C003"
  - source_id: "apex-session-skill"
    source_pointer: "lines 196-198, 236-240"
    supports: "C002"
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: >
      Whether a later KB expansion should split this single concept page into three narrower
      pages (proposal-state, computed-fact-state, confirmed-mutation-state) once more sources
      exist per state remains an open editorial question, not a factual uncertainty about the
      current sources.
    source_pointer: "n/a (editorial scope question)"
    proposed_handling: ask_operator
```
