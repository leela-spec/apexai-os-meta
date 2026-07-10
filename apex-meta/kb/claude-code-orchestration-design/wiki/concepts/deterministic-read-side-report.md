---
title: "Deterministic Read-Side Report"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "deterministic-read-side-report"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 86-98; deterministic read-side computation"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-process-retrospective-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase1-process-retrospective-20260702.md"
    source_hash: "8b011af3de9d3dc7ef5859964437603717d4b9a7"
    source_pointer: "lines 77-123; Phase 0 source-routed reports"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - "gated-write-side-mutation"
  - "semantic-planning-layer"
related_entities: []
review_flags: []
---

# Deterministic Read-Side Report

## Definition

A deterministic read-side report is a computed artifact that answers the
`project_execution_index` core question **which components may compute
reports** (compile plan, lines 86-98): a component that reads files,
manifests, indexes, or compiled pages and produces derived facts — inventory,
status, lint, profile, or navigation output — without asserting new semantic
doctrine and without mutating canonical project or session state. It sits
between the semantic planning layer and gated write-side mutation in the
`project_execution_index` three-way split
(`semantic_planning_vs_deterministic_read_side_computation_vs_gated_write_side_mutation`,
compile plan line 87).

The concept is reinforced by claim B04-C012 (`phase1-batch04-apex-application-patterns.md`):
the promptflow base-build contract enforces repo boundary, target lock, source
authority, thin-scaffold/deep-appendix structure, index-plausibility checks,
and quality gates *before* scaffold drafting proceeds
(`PROMPTFLOW_KB_BASE_BUILD.md` lines 22-64, 75-117). That quality-gate check is
itself a deterministic read-side report: it inspects existing state and
reports pass/fail or plausibility, and it gates progression to the next
(semantic) stage — it does not itself draft, decide, or mutate.

## Operating Rules

```yaml
rules:
  - "May read files, manifests, indexes, and compiled KB pages."
  - "May not write canonical doctrine, accepted truth, or state mutation records."
  - "Functions as a precondition/quality-gate check (per B04-C012), not as the accepting or mutating action itself."
  - "Output is rebuildable and disposable — it is not source-of-truth data and can be regenerated from the same reads."
  - "Distinct from 'which components may propose state changes' and 'which components may write confirmed mutation records' — those are separate project_execution_index questions answered by other layers."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "Primary framing source — names 'which_components_may_compute_reports' as an explicit project_execution_index core question this concept answers."
    coverage: "project_execution_index question set and the three-layer execution model (planning / read-side computation / write-side mutation)."
  - source_id: "phase1-batch04-apex-application-patterns"
    rationale: "Supplies the concrete instance of a deterministic read-side gate (B04-C012 promptflow quality-gate framing) that this concept generalizes from."
    coverage: "Claim B04-C012 and related concept thin-scaffold-deep-appendices; source-authority-preflight concept."
  - source_id: "phase1-process-retrospective-20260702"
    rationale: "Shows an existing Apex-native instance of the pattern (Phase 0 source-routed reports) predating this KB's Phase 2 synthesis."
    coverage: "Phase 0 navigation/report behavior as a deterministic, non-semantic report layer."
```

## Macro / Meso / Micro

### Macro

The compile plan treats "which components may compute reports" as one of
three load-bearing questions that must be answerable without rereading the
raw corpus (alongside "propose state changes" and "write confirmed mutation
records," compile plan lines 89-91). Deterministic read-side reports are the
answer to that specific slice: a distinct authority band that is allowed to
observe and summarize state but not allowed to originate doctrine or commit
mutations.

### Meso

The pattern recurs across two different source lanes that converge on the
same shape. The `project_execution_index` framing (compile plan) states the
abstract layering. The Apex application-pattern batch (B04-C012) supplies a
concrete precedent: promptflow's quality-gate and index-plausibility checks
run deterministically before scaffold drafting, functioning as a report/gate
rather than a generative or mutating step. Phase 0's own source-routed
reports (`phase1-process-retrospective-20260702.md` lines 77-123) are a
second, Apex-native precedent for the same shape inside this very KB's
lifecycle.

### Micro

- Compile plan, lines 86-98: `project_execution_index` core questions,
  including `which_components_may_compute_reports`.
- B04-C012, `PROMPTFLOW_KB_BASE_BUILD.md` lines 75-117: "ranking model,
  sequence, and quality gates" enforced before scaffold drafting.
- `phase1-process-retrospective-20260702.md` lines 77-123: Phase 0
  source-routed reports as a deterministic, pre-semantic report layer.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: >
      Project execution architecture separates which components may propose
      state changes, which may compute reports, and which may write confirmed
      mutation records, as three distinct project_execution_index questions.
    source_pointer: "phase2-specialized-index-compile-plan-20260702.md lines 89-92"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C002
    claim: >
      The promptflow base-build contract enforces quality gates, including
      index-plausibility checks, before scaffold drafting proceeds — an
      existing pattern for a deterministic read-side check gating downstream
      semantic work.
    source_pointer: "phase1-batch04-apex-application-patterns.md claim B04-C012"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C003
    claim: >
      The deterministic-read-side-report concept is the pattern that answers
      'which components may compute reports' without also answering 'which
      components may write mutation records' — the two are deliberately kept
      separate so report generation never doubles as an implicit mutation.
    source_pointer: "synthesis of compile-plan project_execution_index question set and B04-C012 quality-gate framing"
    confidence: medium
    claim_label: working_hypothesis
```

## Routes Here

```yaml
routes:
  - question: "How does project work move from evidence to a report to a mutation?"
    leads_to: "claude-code-orchestration-design/wiki/summaries/project-execution-state-safety-model.md"
    rationale: "That summary synthesizes the full read/propose/write separation this concept is one layer of."
  - related_page: "claude-code-orchestration-design/wiki/concepts/gated-write-side-mutation.md"
    relation: "Sibling layer — gated-write-side-mutation covers the write-side counterpart to this read-side report layer."
```

## Evidence

```yaml
evidence:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_pointer: "lines 86-98"
    supports: "which_components_may_compute_reports core question and the three-layer execution split"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "claim B04-C012"
    supports: "quality-gate framing of a deterministic check preceding scaffold drafting"
  - source_id: "phase1-process-retrospective-20260702"
    source_pointer: "lines 77-123"
    supports: "Phase 0 source-routed reports as an existing deterministic-report instance"
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: >
      This compile (S6) defines the pattern only; it does not implement or
      validate a deterministic report script or lint tool. S7 is expected to
      validate compiled pages, not S6.
    source_pointer: "phase2-specialized-index-compile-plan-20260702.md section 8, next_action"
    proposed_handling: planning_task_candidate
  - id: U002
    description: >
      External/runtime/platform behavior claims (e.g. what a given script or
      CLI can deterministically compute) default to future-research status
      and should not be silently promoted into this concept's doctrine.
    source_pointer: "phase1-batch04-apex-application-patterns.md claim B04-C015 and tension B04-T004"
    proposed_handling: revisit_source
```
