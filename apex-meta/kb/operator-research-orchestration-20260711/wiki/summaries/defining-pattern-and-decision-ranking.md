---
title: Defining Pattern and Decision Ranking
page_type: summary
kb_slug: operator-research-orchestration-20260711
summary_slug: defining-pattern-and-decision-ranking
source_refs:
  - source_id: dr-apexorchestrationclaude
    source_path: raw/notes/DR_ApexOrchestrationClaude.md
    source_pointer: opening findings; Step-by-Step Build Order; Architecture Validation
  - source_id: prompt-flow-create-claude-native-apex-alfred-orchestration-predefinition-files
    source_path: raw/notes/Prompt Flow_Create Claude-Native Apex Alfred Orchestration Predefinition Files.md
    source_pointer: Translation Rule; Global Architecture Constraints; Global Output Contract
  - source_id: apex-hermes-claude-build-pack
    source_path: raw/notes/Apex Hermes Claude Build Pack.md
    source_pointer: 1. 00_SYSTEM_INTENT.md; 3. 02_DECISION_REGISTER.md; 8. Acceptance Checks
  - source_id: apex-hermes-workflow-example-database-master-of-arts-v0-1-1
    source_path: raw/notes/Apex_Hermes_Workflow_Example_Database_Master_of_Arts_v0_1 (1).md
    source_pointer: Workflow Records W01–W02; Profile Ownership Map; I/O Mechanism Map
  - source_id: dr-apex-pm-kb-pd-gem
    source_path: raw/notes/DR_APEX_PM_KB_PD_Gem.md
    source_pointer: Phase 2–4
created_at: 2026-07-11T10:30:00Z
updated_at: 2026-07-11T10:30:00Z
confidence: high
claim_label: behavioral_inference
status: active
related_concepts: [convergence-evidence, stable-control-plane, deterministic-state-boundary]
related_entities: [four-role-control-plane]
review_flags: [ranking-is-evidence-weighted-not-vote-count]
---

# Defining Pattern and Decision Ranking

## Core Summary

This is the decision hierarchy for retrieval. Rank 1 patterns are defaults because they recur across independent architecture, workflow, and operational evidence and remain compatible with the Claude-only target. Lower ranks are useful constraints or alternatives, not universal defaults.

## What This Adds

```yaml
adds:
  - A compact default order for implementation decisions.
  - A distinction between repeated core patterns and use-case-specific decisions.
clarifies:
  - Repetition is weighted by authority, independence, recency, operational specificity, and contradiction.
limits:
  - Rank is not permission to bypass raw evidence for a concrete implementation.
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: dr-apexorchestrationclaude
    rationale: Claude-targeted decision authority.
    coverage: Target constraints and implementation order.
  - source_id: prompt-flow-create-claude-native-apex-alfred-orchestration-predefinition-files
    rationale: Explicit translation and authoring guardrails.
    coverage: Claude-native output boundary and fixed roles.
  - source_id: apex-hermes-workflow-example-database-master-of-arts-v0-1-1
    rationale: Operational corroboration.
    coverage: Handoffs, ownership, validation, mechanism fit.
  - source_id: dr-apex-pm-kb-pd-gem
    rationale: Mechanism-fit evidence.
    coverage: Deterministic/semantic division and operator gate.
```

## Macro / Meso / Micro

### Macro

Rank 1: Claude-native translation, small stable control plane, explicit artifact contracts, independent validation, and deterministic handling of exact state work. Rank 2: structured handoffs, one-file reviewable authoring, operator gate, and mechanism selection by use case. Rank 3: portfolio/coverage ranking, detailed historical workflow taxonomy, and runtime comparisons—valuable context but not target-defining.

### Meso

The defining roles are Alfred for intake/routing, strategist for prioritization, operations for packaging and workflow execution, and detective for independent verification. The defining workflow is evidence intake → normalization/decomposition → decision or execution package → validation → durable handoff. The defining decision boundary is Claude judgment versus deterministic exactness.

### Micro

The rank-one role limit comes from Claude research and the authoring contract (`DR_ApexOrchestrationClaude.md`, opening findings; `Prompt Flow...`, Global Architecture Constraints). Artifact/acceptance discipline comes from the build pack (`03_ARTIFACT_CONTRACT_REGISTRY`; `Acceptance Checks`). Workflow-level handoff and independent validation are explicit in W01/W02. Deterministic state work is supported by the PM/KB/PD mechanism analysis (`Phase 2–3`).

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: Rank 1 default: translate all historical material into Claude-native decisions and reject direct historical runtime revival.
    source_pointer: "Prompt Flow_Create Claude-Native Apex Alfred Orchestration Predefinition Files.md > Translation Rule"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C002
    claim: Rank 1 default: retain a small stable control plane and use temporary specialization rather than permanent-role proliferation.
    source_pointer: "DR_ApexOrchestrationClaude.md > opening findings; Prompt Flow... > Global Architecture Constraints"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C003
    claim: Rank 1 default: evidence-bearing artifacts and independent validation control durable completion.
    source_pointer: "Apex Hermes Claude Build Pack.md > 03_ARTIFACT_CONTRACT_REGISTRY and Acceptance Checks; Apex_Hermes_Workflow_Example_Database_Master_of_Arts_v0_1 (1).md > W01–W02"
    confidence: high
    claim_label: behavioral_inference
  - claim_id: C004
    claim: Rank 1 default: choose deterministic operations for exact state work and Claude reasoning for semantic judgment.
    source_pointer: "DR_APEX_PM_KB_PD_Gem.md > Phase 2–3"
    confidence: high
    claim_label: source_backed_summary
```

## Routes Here

```yaml
routes:
  - question: What are the strongest defaults for this setup?
    leads_to: wiki/summaries/defining-pattern-and-decision-ranking.md
    rationale: Returns the evidence-weighted hierarchy.
  - question: Why is a pattern ranked highly?
    leads_to: wiki/summaries/core-pattern-convergence.md
    rationale: Shows supporting overlap and limitations.
  - question: Which source can decide a disputed point?
    leads_to: wiki/summaries/source-authority-and-connection-map.md
    rationale: Resolves authority and source scope.
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: A future Claude-targeted source that changes a product boundary can supersede a ranking premise.
    source_pointer: "DR_ApexOrchestrationClaude.md > Validated Source List"
    proposed_handling: revisit_source
```
