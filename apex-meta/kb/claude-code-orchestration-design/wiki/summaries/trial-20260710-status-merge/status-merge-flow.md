---
title: "StatusMerge Flow"
page_type: summary
kb_slug: "claude-code-orchestration-design"
summary_slug: "status-merge-flow"
source_refs:
  - source_id: "status-merge-skill"
    source_path: ".claude/skills/status-merge/SKILL.md"
    source_hash: "228c92fc2db9e8fdf6ac32aece8a741b218e58d6"
    source_pointer: "Purpose, Inputs, Outputs, Procedure, Validation Status Selection, Boundary Rules, and Failure Modes; lines 8-140"
    source_storage_mode: "pointer_only"
  - source_id: "status-merge-packet-contract"
    source_path: ".claude/skills/status-merge/references/status-merge-packet-contract.md"
    source_hash: "d917c130aafcdbea6f4c98d909099c523755f424"
    source_pointer: "Contract Role and status_merge_packet schema; lines 5-73 and 120-253"
    source_storage_mode: "pointer_only"
  - source_id: "next-precap-context-contract"
    source_path: ".claude/skills/status-merge/references/next-precaphandoff-context-contract.md"
    source_hash: "a5551276402f62f14ec8e853660d8015fe7f41d9"
    source_pointer: "Contract Role and next_PreCapNextDay_input_context schema; lines 5-61 and 120-216"
    source_storage_mode: "pointer_only"
created_at: "2026-07-10T14:35:00Z"
updated_at: "2026-07-10T14:35:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "needs_review"
related_concepts:
  - "proposal-only-state-transition"
  - "conflict-before-acceptance"
related_entities:
  - "status-merge"
review_flags:
  - "deterministic_postflight_not_run"
  - "usage_summary_required_optional_mismatch"
---

# StatusMerge Flow

## Core Summary

StatusMerge is the reconciliation layer between validated recap-derived candidates and durable project-state mutation. It does not treat a recap as accepted truth and does not write project records directly. Instead, it compares candidate deltas with previous state references, preserves evidence and confidence, exposes contradictions before acceptance, and creates a proposal packet that an operator and the owning downstream packages can review.

The flow has two outputs with different purposes. The `status_merge_packet` is the review and routing artifact: it records candidate dispositions, conflicts, proposed project-KB changes, and an updated status view that remains explicitly non-durable. The `next_PreCapNextDay_input_context` is a compact downstream seed: it carries current focus, candidate next actions, blockers, unresolved operator decisions, evidence references, and readiness confidence. It is intentionally not a next-day plan. PreCapNextDay still owns plan creation, while `project-kb-manager` retains the durable-write boundary.

This separation prevents three forms of layer collapse: candidate evidence becoming accepted state, a status view being mistaken for a durable record, and a planning seed being mistaken for an executable plan. The package's value is therefore not merely aggregation. It is controlled promotion across ownership boundaries.

## What This Adds

```yaml
adds:
  - "A concrete proposal-before-mutation stage between FlowRecap and project-kb-manager."
  - "A conflict register that is processed before candidate acceptance."
  - "A compact, traceable handoff into PreCapNextDay without generating a plan."
clarifies:
  - "Accepted delta candidates are accepted only into a proposal, not into durable project truth."
  - "ProjectStatus views and proposed project-KB updates are separate from durable owner-controlled writes."
  - "Validation status describes packet readiness, not proof that a write occurred."
limits:
  - "The package does not own upstream FlowRecap schemas."
  - "The package does not own project-KB schemas or direct record mutation."
  - "The package does not create runtime, schedules, calendar writes, or autonomous triggers."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - rank: 1
    source_id: "status-merge-skill"
    rationale: "Primary operational authority for trigger conditions, procedure, failure behavior, and completion boundaries."
    coverage: "Explains when StatusMerge runs, how it classifies candidates, and what it must not do."
  - rank: 2
    source_id: "status-merge-packet-contract"
    rationale: "Primary schema authority for the review packet and durable-write routing boundary."
    coverage: "Defines fields, dispositions, conflicts, downstream consumers, and validation states."
  - rank: 3
    source_id: "next-precap-context-contract"
    rationale: "Primary schema authority for the downstream planning seed."
    coverage: "Defines compact context contents and the boundary between context preparation and plan creation."
```

## Macro / Meso / Micro

### Macro

StatusMerge implements a controlled knowledge-promotion boundary. Information moves from recap-derived candidate evidence toward durable project state only through explicit classification, conflict exposure, operator review, and owner-safe routing. This means the orchestration system can preserve momentum from completed work without allowing the latest recap to overwrite longer-lived project truth automatically.

The macro architecture is a three-stage chain: FlowRecap proposes changes, StatusMerge reconciles and packages them, and downstream owners decide or execute the durable consequences. StatusMerge is therefore neither a recorder nor an executor. It is the semantic decision interface between evidence generation and state mutation.

### Meso

The package operates through four linked mechanisms. First, it normalizes upstream artifacts as references rather than importing or redefining their schemas. Second, it classifies every candidate delta into accepted-for-proposal, rejected, deferred, duplicate, superseded, insufficiently evidenced, or conflict-noted states. Third, it elevates conflicts ahead of acceptance so competing values, stale evidence, ambiguous ownership, or missing usage information cannot disappear inside a positive merge summary. Fourth, it emits two bounded views: a proposal packet for review and mutation routing, and a compact context seed for later planning.

The validation status reflects the strongest unresolved condition. A packet may be `valid`, `valid_with_warnings`, `operator_review_recommended`, `blocked_by_conflict`, or `blocked_by_missing_state_owner`. These are routing signals. They determine whether downstream consumers can safely proceed, but they do not claim that project-kb-manager has executed a durable update.

### Micro

The packet contract requires traceable source references and at least one previous-state reference. Accepted candidates record a candidate ID, source reference, delta summary, proposed destination, acceptance basis, and operator-confirmation status. Rejected or deferred candidates retain disposition and reason rather than being dropped. Conflict notes identify a conflict type, the conflicting sources, the decision required, and the affected interpretation.

The proposed project-KB update names `project-kb-manager` as durable write owner and carries an operator gate status. The next planning context must point to exactly one source status-merge packet and contains bounded lists for project focus, candidate actions, blockers, unresolved decisions, and evidence. The action statuses explicitly distinguish items ready for PreCap consideration from those blocked by decisions, missing evidence, or conflict review. These fields make the handoff inspectable without turning it into an executable plan.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "StatusMerge reconciles candidate deltas but does not directly mutate durable project state."
    source_pointer: ".claude/skills/status-merge/SKILL.md lines 10-15, 69-83, and 96-112"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages:
      - "wiki/concepts/trial-20260710-status-merge/proposal-only-state-transition.md"
      - "wiki/entities/trial-20260710-status-merge/status-merge.md"
  - claim_id: C002
    claim: "Conflicts are surfaced before candidate acceptance and can block safe downstream routing."
    source_pointer: ".claude/skills/status-merge/SKILL.md lines 75-83 and 114-140; status-merge-packet-contract.md lines 63-72 and 297-314"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages:
      - "wiki/concepts/trial-20260710-status-merge/conflict-before-acceptance.md"
  - claim_id: C003
    claim: "Durable project-KB changes remain operator-gated and owned by project-kb-manager."
    source_pointer: ".claude/skills/status-merge/references/status-merge-packet-contract.md lines 20-41, 63-72, and 214-227"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages:
      - "wiki/concepts/trial-20260710-status-merge/proposal-only-state-transition.md"
  - claim_id: C004
    claim: "The downstream PreCap artifact is a compact planning seed and not a next-day plan or autonomous trigger."
    source_pointer: ".claude/skills/status-merge/references/next-precaphandoff-context-contract.md lines 7-16 and 52-61"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages:
      - "wiki/entities/trial-20260710-status-merge/status-merge.md"
  - claim_id: C005
    claim: "Rejected, deferred, and conflicting candidates remain visible for auditability and later decisions."
    source_pointer: ".claude/skills/status-merge/references/status-merge-packet-contract.md lines 193-212 and 280-314"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages:
      - "wiki/concepts/trial-20260710-status-merge/conflict-before-acceptance.md"
```

## Routes Here

```yaml
routes:
  - question: "How does a FlowRecap candidate become a proposed project-state update?"
    leads_to: "wiki/summaries/trial-20260710-status-merge/status-merge-flow.md"
    rationale: "This page describes the complete reconciliation and routing chain."
  - question: "Why can StatusMerge not write the project KB directly?"
    leads_to: "wiki/concepts/trial-20260710-status-merge/proposal-only-state-transition.md"
    rationale: "The concept page isolates the proposal-versus-durable-state boundary."
  - question: "What happens when recap evidence conflicts with previous state?"
    leads_to: "wiki/concepts/trial-20260710-status-merge/conflict-before-acceptance.md"
    rationale: "The concept page explains conflict ordering, status changes, and operator decisions."
  - question: "What exactly is the StatusMerge package?"
    leads_to: "wiki/entities/trial-20260710-status-merge/status-merge.md"
    rationale: "The entity page describes identity, interfaces, and non-ownership."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: >
      The skill entrypoint lists source usage summaries as optional, while the
      packet contract includes source_usage_summary_refs in the required field set.
    source_pointer: ".claude/skills/status-merge/SKILL.md lines 32-45; status-merge-packet-contract.md lines 43-52 and 123-170"
    proposed_handling: "audit_item"
  - id: U002
    description: >
      This bounded compile does not verify the upstream meaning of a validated
      FlowRecap delta or the downstream execution behavior of project-kb-manager.
    source_pointer: ".claude/skills/status-merge/SKILL.md lines 69-83 and 183-192"
    proposed_handling: "revisit_source"
  - id: U003
    description: >
      A validation status of valid proves packet conformance under this package's
      rules; it does not prove that an operator approved or a durable write completed.
    source_pointer: ".claude/skills/status-merge/SKILL.md lines 85-94; status-merge-packet-contract.md lines 244-252"
    proposed_handling: "leave_as_gap"
```
