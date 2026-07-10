---
title: "Stop Condition as Context Saver"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "stop-condition-as-context-saver"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 124-137; stop_condition_as_context_saver"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C013, B04-C014; stop and closure controls"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - "handoff-stop-conditions"
  - "packet-size-budget"
  - "evd-imp-rsk-thresholds"
related_entities: []
review_flags:
  - "the 'context saver' / token-economy framing extends B04-C013's HALT/CLARIFY claim rather than quoting it directly"
---

# Stop Condition as Context Saver

## Definition

A stop condition is an explicit routing control — HALT or CLARIFY — that ends invalid continuation early rather than guessing, expanding scope, or continuing unsafely. It answers the `token_economy_and_information_design_index` question `how_stop_conditions_save_context_and_reduce_momentum_errors`: stopping early avoids the compounding token cost of continuing on a wrong assumption ("momentum errors"), in addition to the safety benefit Batch 04 already documents (B04-C013).

## Operating Rules

```yaml
rules:
  - "HALT stops execution outright when required evidence, approval, or target clarity is missing."
  - "CLARIFY requests one blocking clarification instead of guessing."
  - "Stop status must be explicit and visible (a field or flag), not implied by prose."
  - "A stop condition must name the single next required action, not a menu of possibilities."
  - "Success/closure must not be claimed until file-output/task-closure requirements are explicitly satisfied (B04-C014)."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase1-batch04-apex-application-patterns"
    rationale: "Directly defines HALT/CLARIFY as routing controls (B04-C013) and the closure discipline that pairs with them (B04-C014)."
    coverage: "HALT and CLARIFY contract definitions; file-output and task-closure validation-status requirements."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "Supplies the token-economy framing that names this concept and connects stop conditions to context cost, not only safety."
    coverage: "token_economy_and_information_design_index question on how stop conditions save context and reduce momentum errors."
```

## Macro / Meso / Micro

### Macro

The `token_economy_and_information_design_index` frames stop conditions as a context-economy device, not merely a safety device: stopping early prevents the compounding token cost of continuing on a wrong assumption across many further turns.

### Meso

B04-C013 defines HALT and CLARIFY as routing controls that stop guessing, scope expansion, unsafe continuation, and silent failure. B04-C014's task-closure contract requires explicit validation status before success is claimed — the complementary "don't claim done" half of the same discipline. B04-C007 and B04-C008 (naming a stop condition before execution begins; preferring bounded, stage-gated execution) supply the upstream requirement that a stop condition exists at all before work starts.

### Micro

The specific "context saver" / token-economy framing of HALT/CLARIFY is index vocabulary from the `token_economy_and_information_design_index`, applied to B04-C013's HALT/CLARIFY claim. Batch 04 itself frames HALT/CLARIFY as safety and routing controls; it does not explicitly frame them as a token-economy mechanism. That connection is this KB's synthesis.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Execution-control contracts define HALT and CLARIFY as routing controls that stop guessing, scope expansion, unsafe continuation, and silent failure."
    source_pointer: "B04-C013 (APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md continuation lines 1-51; BEST_PRACTICES_v_old.md lines 232-242)"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C002
    claim: "File-output and task-closure contracts require complete content, scope proof, target-root validation, fetch-back, and explicit validation status before success is claimed."
    source_pointer: "B04-C014 (APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md continuation lines 52-94, 247-280)"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C003
    claim: "Framing stop conditions explicitly as a token-economy mechanism ('saves context, reduces momentum errors') rather than only a safety mechanism is a Phase 2 synthesis drawn from the token_economy index question, extending B04-C013 rather than quoting it directly."
    source_pointer: "phase2-specialized-index-compile-plan-20260702 lines 124-137"
    confidence: "medium"
    claim_label: "working_hypothesis"
```

## Routes Here

```yaml
routes:
  - question: "How do stop conditions keep an agent from burning context on a wrong path?"
    leads_to: "claude-code-orchestration-design/concepts/packet-size-budget.md"
    rationale: "Packet-size-budget is the companion token-economy constraint that stop conditions protect."
  - related_page: "claude-code-orchestration-design/concepts/handoff-stop-conditions.md"
    relation: "The handoff-packet field where a stop condition is expressed for downstream consumers."
  - related_page: "claude-code-orchestration-design/concepts/evd-imp-rsk-thresholds.md"
    relation: "Risk thresholds that can trigger a HALT or CLARIFY stop condition."
```

## Evidence

```yaml
evidence:
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "B04-C013"
    supports: "HALT/CLARIFY as routing controls against guessing, scope expansion, unsafe continuation, silent failure."
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "B04-C014"
    supports: "Explicit validation status required before closure/success is claimed."
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "B04-C007, B04-C008"
    supports: "Requirement to name a stop condition before execution and prefer bounded, stage-gated execution."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_pointer: "lines 124-137"
    supports: "Token-economy framing of stop conditions as context savers."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "The 'context saver' / token-economy framing of HALT/CLARIFY is Phase 2 index-question synthesis, not verbatim Batch 04 wording."
    source_pointer: "phase2-specialized-index-compile-plan-20260702 lines 124-137"
    proposed_handling: "leave_as_gap"
  - id: U002
    description: "Whether HALT/CLARIFY/closure schemas should become Apex-wide reusable contracts or stay local to the prompt/workflow lane remains open."
    source_pointer: "B04-Q003"
    proposed_handling: "revisit_source"
```
