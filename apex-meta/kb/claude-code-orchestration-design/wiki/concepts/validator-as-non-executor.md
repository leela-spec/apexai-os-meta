---
title: "Validator as Non-Executor"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "validator-as-non-executor"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 65-66; build, validation, routing, authority separation"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch03-external-orchestration-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch03-external-orchestration-patterns.md"
    source_hash: "dbe4e500d5c22cc61adc4e1364412da71d3db683"
    source_pointer: "claims B03-C006 through B03-C007; deterministic-then-inference validation"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C013 through B04-C017; verification and gates"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "medium"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - "owner-validator-split"
  - "candidate-is-not-accepted-truth"
related_entities:
  - "bmad-method"
review_flags: []
---

# Validator as Non-Executor

## Definition

A validator reviews evidence, structural shape, risk, and completion proof, but is not the actor that performs the underlying task. This narrows the owner/validator split (see related concept) to a specific authority boundary: validation output is a verdict, escalation, or blocker — never a substitute execution of the work being validated. The concept synthesizes BMAD's deterministic-then-inference validation mechanic (B03-C006, B03-C007) with Apex's own HALT/CLARIFY, file-output, and task-closure contracts (B04-C013 through B04-C017), which require verification to happen as a distinct step with its own proof obligations rather than being folded into execution. As with owner-validator-split, the specific framing "validator as non-executor" is an inferential naming step (`working_hypothesis`) built on individually source-backed claims.

## Operating Rules

```yaml
rules:
  - "A validator reviews candidate output, source_refs, and acceptance criteria without taking over execution authority."
  - "Used when an output needs independent review or risk classification."
  - "Not used when the validator is the only role able to perform the actual task (in that case the role is an executor, not a validator)."
  - "Writes: validation result, blocker, or escalation — not new production output."
  - "Validator reads the smallest candidate/evidence set, not the whole source history."
  - "Validation cannot silently promote a candidate to accepted truth without the required gate."
  - "Which validation gates become hooks or scripts remains deferred beyond the current compile cycle."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase1-batch04-apex-application-patterns"
    rationale: "Primary-authority Apex doctrine defining HALT/CLARIFY, file-output proof, and task-closure contracts; ranked highest because it directly grounds the 'non-executor' constraint on validation authority."
    coverage: "B04-C013 (HALT/CLARIFY as routing controls), B04-C014 (file-output and task-closure proof), B04-C015 (external claims require verification), B04-C017 (explicit artifacts/state/gates over conversational continuity)."
  - source_id: "phase1-batch03-external-orchestration-patterns"
    rationale: "Secondary/comparative source supplying the concrete two-pass validation mechanic (deterministic first, inference second); ranked second as non-authoritative external-repo material."
    coverage: "B03-C006 (two-pass validation), B03-C007 (encapsulation checks within the deterministic pass)."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "Internal Phase 2 planning note that first separated build/validation/routing/authority as distinct roles; used for continuity with the compile plan."
    coverage: "Lines 65-66 on separating build, validation, routing, and authority."
```

## Macro / Meso / Micro

### Macro

Validation is treated as a bounded, non-productive role across both the comparative external evidence and Apex's own primary doctrine: a validator's job is to check, classify risk, and gate — not to produce or fix the artifact itself. This keeps the person or process resolving ambiguity in production separate from the person or process certifying the result.

### Meso

BMAD's `skill-validator.md` (B03-C006, B03-C007) frames validation as a check pipeline: deterministic rules run first and inference-level judgment is reserved for what remains, but at no point does the validator itself become the author of the artifact under review. Apex's execution-control doctrine (B04-C013 through B04-C017) reinforces this from the Apex side: HALT and CLARIFY exist specifically to stop guessing, scope expansion, and silent failure rather than to let a reviewing process patch its way to a result; file-output and task-closure contracts require complete content, scope proof, and fetch-back validation before success is claimed, which only makes sense if the checking step is distinct from the producing step.

### Micro

- B03-C006: "BMAD's validation pattern uses deterministic checks first and inference validation second..." (`skill-validator.md` lines 3-28)
- B04-C013: "Execution-control contracts define HALT and CLARIFY as routing controls that stop guessing, scope expansion, unsafe continuation, and silent failure." (`APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md` continuation lines 1-51)
- B04-C014: "File-output and task-closure contracts require complete content, scope proof, target-root validation, fetch-back, and explicit validation status before success is claimed." (`APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md` continuation lines 52-94, 125-153, 247-280)

## Key Claims

```yaml
key_claims:
  - claim_id: B03-C006
    claim: "BMAD's validation pattern uses deterministic checks first and inference validation second, skipping rules that passed deterministically and reserving LLM judgment for semantic or ambiguous rules."
    source_pointer: "phase1-batch03-external-orchestration-patterns.md; skill-validator.md lines 3-28"
    confidence: "medium"
    claim_label: "source_backed_summary"
  - claim_id: B04-C013
    claim: "Execution-control contracts define HALT and CLARIFY as routing controls that stop guessing, scope expansion, unsafe continuation, and silent failure."
    source_pointer: "phase1-batch04-apex-application-patterns.md; APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md continuation lines 1-51"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: B04-C014
    claim: "File-output and task-closure contracts require complete content, scope proof, target-root validation, fetch-back, and explicit validation status before success is claimed."
    source_pointer: "phase1-batch04-apex-application-patterns.md; APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md continuation lines 52-94, 125-153, 247-280"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: "VNE-WH001"
    claim: "'Validator as non-executor' generalizes BMAD's two-pass check pipeline and Apex's HALT/CLARIFY/closure contracts into a single authority boundary: a validator may block, escalate, or approve, but never substitutes its own execution for the work under review."
    source_pointer: "synthesis of B03-C006, B03-C007, B04-C013, B04-C014, B04-C017"
    confidence: "medium"
    claim_label: "working_hypothesis"
```

## Routes Here

```yaml
routes:
  - question: "Can the reviewer of an artifact also fix or finish it directly?"
    leads_to: "claude-code-orchestration-design/concepts/candidate-is-not-accepted-truth.md"
    rationale: "Candidate-is-not-accepted-truth explains why an unreviewed candidate cannot be treated as final; this page explains why the review step itself must not become production."
  - related_page: "claude-code-orchestration-design/concepts/owner-validator-split.md"
    relation: "Owner-validator-split is the broader role separation; validator-as-non-executor is the specific authority constraint on the validator side of that split."
  - related_page: "claude-code-orchestration-design/entities/bmad-method.md"
    relation: "BMAD-METHOD is the comparative external source for the deterministic-then-inference validation mechanic this concept draws on."
```

## Evidence

```yaml
evidence:
  - source_id: "phase1-batch03-external-orchestration-patterns"
    source_pointer: "skill-validator.md lines 3-28 (B03-C006), lines 119-177 (B03-C007)"
    supports: "Deterministic-then-inference two-pass validation mechanic"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md continuation lines 1-94, 125-153, 247-280 (B04-C013, B04-C014)"
    supports: "HALT/CLARIFY and file-output/task-closure contracts constraining validation authority"
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_pointer: "lines 65-66"
    supports: "Separation of build, validation, routing, and authority as distinct roles"
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Which validation gates become hard-enforced hooks/scripts versus soft-enforced conventions is deferred beyond the current compile cycle."
    source_pointer: "apex-meta/kb/claude-code-orchestration-design/log/operator-phase1-review-decisions-20260702.md; Q002_hook_or_script_enforcement"
    proposed_handling: "planning_task_candidate"
  - id: U002
    description: "BMAD's validator includes BMAD-specific rules not yet filtered for Apex reuse; adopting the two-pass mechanic does not mean adopting BMAD's specific rule set."
    source_pointer: "phase1-batch03-external-orchestration-patterns.md; B03-T002, B03-Q002"
    proposed_handling: "leave_as_gap"
```
