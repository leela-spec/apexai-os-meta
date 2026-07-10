---
title: "Proposal-Only State Transition"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "proposal-only-state-transition"
source_refs:
  - source_id: "status-merge-skill"
    source_path: ".claude/skills/status-merge/SKILL.md"
    source_hash: "228c92fc2db9e8fdf6ac32aece8a741b218e58d6"
    source_pointer: "Purpose, Procedure, Boundary Rules, and Failure Modes; lines 8-15, 69-83, 96-140"
    source_storage_mode: "pointer_only"
  - source_id: "status-merge-packet-contract"
    source_path: ".claude/skills/status-merge/references/status-merge-packet-contract.md"
    source_hash: "d917c130aafcdbea6f4c98d909099c523755f424"
    source_pointer: "Ownership, global rules, accepted candidates, proposed project-KB update, and status view; lines 20-72 and 193-227"
    source_storage_mode: "pointer_only"
created_at: "2026-07-10T14:40:00Z"
updated_at: "2026-07-10T14:40:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "needs_review"
related_concepts:
  - "conflict-before-acceptance"
related_entities:
  - "status-merge"
review_flags:
  - "deterministic_postflight_not_run"
---

# Proposal-Only State Transition

## Definition

A proposal-only state transition is a controlled intermediate state in which evidence has been interpreted and candidate changes have been classified, but no durable project record has yet been mutated. The proposal may be complete enough for review, routing, and downstream planning context, while still remaining explicitly separate from accepted runtime or project truth.

Within StatusMerge, this distinction is structural rather than rhetorical. Accepted delta candidates are accepted into the merge proposal, not automatically into the project KB. The package can describe a proposed update and an updated status view, but both artifacts retain an owner route and operator gate. The durable change remains the responsibility of `project-kb-manager`.

## Operating Rules

```yaml
rules:
  - "Candidate evidence must remain traceable to source refs."
  - "Acceptance inside the merge packet means proposal acceptance, not durable-state acceptance."
  - "Every proposed durable change must identify its destination and write owner."
  - "Operator confirmation status must remain visible when required."
  - "A status view must not be represented as the project database or current durable record."
  - "Validation status must not be used as proof that a downstream write occurred."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - rank: 1
    source_id: "status-merge-packet-contract"
    rationale: "Defines the formal distinction between proposal ownership and durable write ownership."
    coverage: "Accepted candidates, proposed update object, status view, operator gate, and project-kb-manager route."
  - rank: 2
    source_id: "status-merge-skill"
    rationale: "Defines the operational procedure and failure corrections that preserve the distinction."
    coverage: "Proposal-only drafting, owner-safe routing, forbidden direct mutation, and completion checks."
```

## Macro / Meso / Micro

### Macro

Proposal-only transitions solve a common orchestration problem: semantic work often needs to move faster than durable-state mutation. A recap or reviewer may identify a likely change, but the system still needs a stable place to preserve that conclusion before an authorized owner writes it. The proposal layer allows the system to retain useful interpretation without confusing recency with authority.

This is a promotion boundary. Evidence becomes a candidate; a candidate becomes an accepted proposal; only a separate owner and gate can turn that proposal into durable truth. By naming each stage, the system prevents hidden writes and makes rejected or unconfirmed interpretations recoverable.

### Meso

The StatusMerge packet expresses the boundary through field-level obligations. An accepted candidate carries its source, proposed destination, acceptance basis, and confirmation status. The proposed project-KB update names the durable write owner and records whether it is ready for review, confirmed for routing, or blocked. The updated status packet is explicitly described as a view/proposal, so it cannot quietly replace the `ProjectStatus` or project-KB schema.

This pattern also separates semantic validity from execution status. A merge packet can be internally valid while the durable update remains unapproved. Conversely, a conflict or missing owner can block routing even when the underlying candidate is well supported. The packet therefore records what is known, what is proposed, and what has actually been authorized as distinct facts.

### Micro

The contract requires `accepted_delta_candidates` to include `candidate_id`, `source_ref`, `delta_summary`, `proposed_destination`, `acceptance_basis`, and `operator_confirmation_status`. Allowed destinations distinguish project-KB update proposals, ProjectStatus view proposals, PreCap context seeds, and consumed-recap views. The `proposed_project_kb_update` object fixes `durable_write_owner` to `project-kb-manager` and includes an `operator_gate_status` that may remain blocked.

The status view retains `source_status_merge_packet_ref`, accepted candidate views, consumed recap candidates, unresolved conflicts, and a project-status summary. Those fields preserve traceability while the contract explicitly states that the view is not durable project state. This combination is what makes the transition proposal-only in a verifiable way.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "StatusMerge may prepare a proposed project-KB update but cannot execute the durable write itself."
    source_pointer: ".claude/skills/status-merge/SKILL.md lines 75-83 and 96-112; status-merge-packet-contract.md lines 214-220"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C002
    claim: "An accepted delta candidate remains a proposal until operator or owner confirmation."
    source_pointer: ".claude/skills/status-merge/references/status-merge-packet-contract.md lines 63-72 and 193-199"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C003
    claim: "The updated all-project status artifact is a proposal/view and not the authoritative current project state."
    source_pointer: ".claude/skills/status-merge/SKILL.md lines 47-67 and 133-140; status-merge-packet-contract.md lines 222-227 and 335-344"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C004
    claim: "Packet validity and durable-write completion are separate lifecycle facts."
    source_pointer: ".claude/skills/status-merge/SKILL.md lines 85-94; status-merge-packet-contract.md lines 244-252 and 316-333"
    confidence: "medium"
    claim_label: "behavioral_inference"
```

## Routes Here

```yaml
routes:
  - question: "Why does StatusMerge produce proposals instead of updating the project KB?"
    leads_to: "wiki/concepts/trial-20260710-status-merge/proposal-only-state-transition.md"
    rationale: "Explains the ownership and promotion boundary."
  - question: "When is a recap-derived change considered durable truth?"
    leads_to: "wiki/concepts/trial-20260710-status-merge/proposal-only-state-transition.md"
    rationale: "Separates candidate, proposal, operator confirmation, and owner execution."
  - related_page: "wiki/summaries/trial-20260710-status-merge/status-merge-flow.md"
    relation: "Places the concept inside the full reconciliation flow."
  - related_page: "wiki/concepts/trial-20260710-status-merge/conflict-before-acceptance.md"
    relation: "Explains one of the principal conditions that blocks promotion."
```

## Evidence

```yaml
evidence:
  - source_id: "status-merge-skill"
    source_pointer: "lines 75-83 and 96-140"
    supports: "Proposal-only drafting, owner routing, forbidden direct mutation, and correction of implied writes."
  - source_id: "status-merge-packet-contract"
    source_pointer: "lines 193-227 and 316-344"
    supports: "Accepted-proposal semantics, durable-write owner, operator gate, and non-durable status view."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "The contract defines confirmation states but this bounded source set does not define the exact operator interaction that changes them."
    source_pointer: "status-merge-packet-contract.md lines 258-278 and 316-333"
    proposed_handling: "revisit_source"
  - id: U002
    description: "The term accepted can be misread as durable acceptance unless every consumer preserves the proposal-only qualifier."
    source_pointer: "status-merge-packet-contract.md lines 193-199"
    proposed_handling: "audit_item"
```
