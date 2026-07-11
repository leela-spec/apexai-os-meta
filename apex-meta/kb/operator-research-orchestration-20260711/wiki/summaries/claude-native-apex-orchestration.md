---
title: Claude-Native Apex Orchestration
page_type: summary
kb_slug: operator-research-orchestration-20260711
summary_slug: claude-native-apex-orchestration
source_refs:
  - source_id: dr-apexorchestrationclaude
    source_path: raw/notes/DR_ApexOrchestrationClaude.md
    source_pointer: opening findings; Step-by-Step Build Order; Architecture Validation; Recommended Immediate Actions
  - source_id: prompt-flow-create-claude-native-apex-alfred-orchestration-predefinition-files
    source_path: raw/notes/Prompt Flow_Create Claude-Native Apex Alfred Orchestration Predefinition Files.md
    source_pointer: Translation Rule; Fixed File Sequence; Global Architecture Constraints
  - source_id: apex-hermes-claude-build-pack
    source_path: raw/notes/Apex Hermes Claude Build Pack.md
    source_pointer: 1. 00_SYSTEM_INTENT.md; 3. 02_DECISION_REGISTER.md; 8. Acceptance Checks
created_at: 2026-07-11T10:05:00Z
updated_at: 2026-07-11T10:05:00Z
confidence: high
claim_label: source_backed_summary
status: active
related_concepts: [claude-native-translation, stable-control-plane, contract-before-procedure, independent-validation-gate]
related_entities: [four-role-control-plane]
review_flags: [historical-runtime-evidence-must-not-be-treated-as-target]
---

# Claude-Native Apex Orchestration

## Core Summary

The target is a Claude implementation architecture built from the useful intent of prior Apex material, not a recreation of its historical runtime. The durable design is a small four-role control plane, repository-authored contracts and evidence, narrow repeatable procedures, and independent validation. Historical material is admissible only after translation into a Claude-native decision; it cannot silently prescribe an old runtime, scheduler, or file model.

## What This Adds

```yaml
adds:
  - A single target architecture for interpreting the corpus.
  - A rule that historical runtime language is evidence, never an implementation default.
  - A dependency order: contracts and role boundaries before repeatable procedures and workflow fan-out.
clarifies:
  - Stable roles are control-plane responsibilities, not a license to create a large permanent roster.
  - Durable repository artifacts outrank ephemeral session or runtime state.
limits:
  - This page does not authorize infrastructure, scheduling, or historical runtime implementation.
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: dr-apexorchestrationclaude
    rationale: Most direct source connecting researched Claude behavior to the proposed Apex control plane.
    coverage: Role limits, durable state, build order, validation-first slice, and product-boundary cautions.
  - source_id: prompt-flow-create-claude-native-apex-alfred-orchestration-predefinition-files
    rationale: Explicitly translates inherited terminology and constrains the authoring surface.
    coverage: Claude-native mapping, four roles, output contract, scope firewall, and ordered creation flow.
  - source_id: apex-hermes-claude-build-pack
    rationale: Supplies the reusable macro contracts and closed-loop model underneath the translation.
    coverage: Artifact registry, decision register, acceptance checks, procedure-versus-role boundary, and deprecated-model guard.
```

## Macro / Meso / Micro

### Macro

The corpus converges on a durable control plane that guides work through explicit artifacts rather than depending on a conversation or a runtime's memory. Claude is the target implementation surface. Earlier designs contribute patterns—bounded roles, handoffs, validation, and lifecycle closure—but not executable runtime authority.

### Meso

The control plane divides intake/routing, strategy, operations, and independent validation. Repeated work is encoded as a bounded procedure or workflow; a permanent role is justified only by persistent identity, memory, permissions, or durable ownership. Contracts make handoffs and acceptance criteria inspectable, while a validator can reject completion without owning delivery.

### Micro

The research reference recommends contracts before procedural generation and a validation-first end-to-end slice (`DR_ApexOrchestrationClaude.md`, Step-by-Step Build Order; Recommended Immediate Actions 1–4). The authoring flow forbids drift back into historical runtime implementation (`Prompt Flow...`, Translation Rule) and fixes exactly four permanent roles (`Global Architecture Constraints`). The build pack retains explicit deprecated-process guards and acceptance checks (`Apex Hermes Claude Build Pack.md`, 00_SYSTEM_INTENT.md; Acceptance Checks).

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: Claude is the only implementation target; older architectures are translated evidence rather than runtime specifications.
    source_pointer: "Prompt Flow_Create Claude-Native Apex Alfred Orchestration Predefinition Files.md > Translation Rule"
    confidence: high
    claim_label: source_backed_summary
    used_in_pages: [wiki/concepts/claude-native-translation.md]
  - claim_id: C002
    claim: The durable control plane has four bounded responsibilities, with temporary specialization preferred to permanent role expansion.
    source_pointer: "DR_ApexOrchestrationClaude.md > opening findings; Apex&HermesArchitectrueGuidacne.md > 2. Fixed Profile Architecture"
    confidence: high
    claim_label: source_backed_summary
    used_in_pages: [wiki/concepts/stable-control-plane.md]
  - claim_id: C003
    claim: Contracts, named artifacts, and acceptance checks must precede scalable procedural authoring.
    source_pointer: "Apex Hermes Claude Build Pack.md > 3. 02_DECISION_REGISTER.md; 4. 03_ARTIFACT_CONTRACT_REGISTRY.md; 8. Acceptance Checks"
    confidence: high
    claim_label: source_backed_summary
    used_in_pages: [wiki/concepts/contract-before-procedure.md]
```

## Routes Here

```yaml
routes:
  - question: What is the current architecture being built?
    leads_to: wiki/summaries/claude-native-apex-orchestration.md
    rationale: Establishes target, boundaries, and source interpretation rules.
  - question: Which old ideas should Claude adopt?
    leads_to: wiki/concepts/claude-native-translation.md
    rationale: Separates transferable patterns from historical assumptions.
  - question: Which pattern is most repeatedly supported?
    leads_to: wiki/summaries/core-pattern-convergence.md
    rationale: Provides evidence-weighted overlap across the corpus.
  - related_page: wiki/concepts/stable-control-plane.md
    relation: Defines ownership and anti-proliferation rule.
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: Claude product capabilities and scheduling claims are time-sensitive and must be reopened before implementation decisions depend on them.
    source_pointer: "DR_ApexOrchestrationClaude.md > Validated Source List; opening findings"
    proposed_handling: revisit_source
  - id: U002
    description: A historical source may share role names but imply a different runtime boundary; do not infer compatibility from names alone.
    source_pointer: "Apex Hermes Claude Build Pack.md > 1. 00_SYSTEM_INTENT.md; Prompt Flow... > Translation Rule"
    proposed_handling: revisit_source
```
