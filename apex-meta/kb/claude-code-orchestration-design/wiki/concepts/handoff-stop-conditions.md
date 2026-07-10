---
title: "Handoff Stop Conditions"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "handoff-stop-conditions"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 82-85; mandatory stop conditions and refs replacing full context"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C013, B04-C014, B04-C017; stop and closure proof"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - "stop-condition-as-context-saver"
  - "standard-handoff-packet"
  - "evd-imp-rsk-thresholds"
related_entities: []
review_flags: []
---

# Handoff Stop Conditions

## Definition

A handoff stop condition is an explicit, named rule stating exactly when the receiver of a handoff packet must HALT or issue a single blocking CLARIFY question instead of guessing, expanding scope, or silently continuing. It is one of the mandatory fields the `handoff_contract_index` asks every handoff packet to answer (`mandatory_stop_conditions`), and it is directly grounded in the execution-control-contract material ingested in Phase 1 batch 04: HALT and CLARIFY are defined as routing controls, not prose warnings, and they exist specifically to stop guessing, unbounded scope expansion, unsafe continuation, and silent failure (B04-C013).

## Operating Rules

```yaml
rules:
  - "Every handoff-shaped artifact (task packet, flow packet, plan packet) must name the exact condition under which continuation becomes invalid, before work begins."
  - "HALT is used when continuation would require guessing missing source, authority, target, or validation state; it stops all further action."
  - "CLARIFY is used when exactly one blocking question, asked once, would resolve the ambiguity; it is not a substitute for HALT when the gap is structural."
  - "A receiver must not report success or partial success while a stop condition is active."
  - "Stop conditions are routing controls encoded in the artifact, not advisory language buried in prose."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase1-batch04-apex-application-patterns"
    rationale: "Primary source for the HALT/CLARIFY control definitions and the file-output/task-closure contracts that stop conditions feed into."
    coverage: "Claims B04-C013 (HALT/CLARIFY routing controls), B04-C014 (file-output and task-closure contracts), B04-C017 (recommendation to preserve Apex lifecycle safety via explicit gates and HALT/CLARIFY signals)."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "Names `mandatory_stop_conditions` as a required core question of the handoff_contract_index, establishing that stop conditions are an Apex-wide handoff requirement rather than a one-off doctrine note."
    coverage: "handoff_contract_index core_questions, lines 70-83, including `mandatory_stop_conditions` and `how_input_refs_replace_full_context`."
```

## Macro / Meso / Micro

### Macro

Across the ingested corpus, stop conditions are treated as a first-class part of any handoff-shaped contract, not an optional safety note. The compile plan elevates this into a dedicated core question (`mandatory_stop_conditions`) inside the `handoff_contract_index`, meaning every Apex handoff packet design should be checked against whether it states its own stop conditions, alongside authority basis, state, and evidence status.

### Meso

The prompt/workflow execution-control-contract material supplies the concrete mechanism: HALT and CLARIFY are defined as routing controls specifically built to prevent guessing, scope expansion, unsafe continuation, and silent failure (B04-C013). This sits alongside the file-output and task-closure contracts, which require complete content, scope proof, target-root validation, fetch-back, and explicit validation status before success can be claimed (B04-C014) — closure proof and stop conditions are two sides of the same discipline: don't claim done, and don't keep going, unless the packet says it's safe to.

### Micro

`APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md` continuation lines 1-51 define the HALT and CLARIFY contracts directly; `BEST_PRACTICES_v_old.md` lines 232-242 frame this as "routing controls instead of prose warnings," i.e., the stop condition must be a structured field a receiver can check mechanically, not a warning sentence a reader might skim past.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Execution-control contracts define HALT and CLARIFY as routing controls that stop guessing, scope expansion, unsafe continuation, and silent failure."
    source_pointer: "phase1-batch04-apex-application-patterns claim B04-C013"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C002
    claim: "File-output and task-closure contracts require complete content, scope proof, target-root validation, fetch-back, and explicit validation status before success is claimed."
    source_pointer: "phase1-batch04-apex-application-patterns claim B04-C014"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C003
    claim: "The handoff_contract_index treats mandatory stop conditions as a required, generalizable field for every Apex handoff packet, not just prompt/workflow execution."
    source_pointer: "phase2-specialized-index-compile-plan-20260702 lines 70-83"
    confidence: "medium"
    claim_label: "working_hypothesis"
```

## Routes Here

```yaml
routes:
  - question: "What stops a receiving skill or agent from guessing when a handoff is incomplete?"
    leads_to: "claude-code-orchestration-design/concepts/handoff-stop-conditions.md"
    rationale: "Direct match to the mandatory_stop_conditions core question."
  - related_page: "claude-code-orchestration-design/concepts/stop-condition-as-context-saver.md"
    relation: "Sibling concept framing the same HALT/CLARIFY discipline as a token-economy benefit rather than a safety requirement."
  - related_page: "claude-code-orchestration-design/concepts/standard-handoff-packet.md"
    relation: "Stop conditions are one required field inside the standard handoff packet shape."
```

## Evidence

```yaml
evidence:
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "claim B04-C013"
    supports: "Definition and Operating Rules: HALT/CLARIFY as routing controls."
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "claim B04-C014"
    supports: "Meso section: closure proof paired with stop conditions."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_pointer: "handoff_contract_index core_questions, lines 70-83"
    supports: "Macro section and Key Claim C003: generalization to all Apex handoffs."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "The exact machine-readable enum for stop conditions (e.g. a fixed set of HALT/CLARIFY codes) is not specified in Phase 1; B04-Q003 leaves open whether these schemas become reusable Apex-wide contracts or stay local to the prompt/workflow lane."
    source_pointer: "phase1-batch04-apex-application-patterns open question B04-Q003"
    proposed_handling: "planning_task_candidate"
  - id: U002
    description: "Key Claim C003 generalizes stop conditions to every Apex handoff packet based on the compile plan's index framing rather than a direct B04 claim naming 'handoff stop conditions' verbatim; treat the generalization as a working hypothesis until an Apex-wide handoff schema is confirmed."
    source_pointer: "phase2-specialized-index-compile-plan-20260702 lines 70-83"
    proposed_handling: "revisit_source"
```
