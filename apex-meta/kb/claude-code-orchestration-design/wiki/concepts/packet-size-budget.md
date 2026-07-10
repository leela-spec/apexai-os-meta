---
title: "Packet Size Budget"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "packet-size-budget"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 124-137; packet_size_budget"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C007 through B04-C011; bounded artifacts"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "medium"
claim_label: "working_hypothesis"
status: "active"
related_concepts:
  - "refs-not-copies"
  - "low-token-handoff-design"
  - "standard-handoff-packet"
related_entities: []
review_flags: []
---

# Packet Size Budget

## Definition

A packet size budget is the discipline of keeping handoff, task, plan, recap, or query packets small enough to route work without becoming a new raw corpus in their own right. It directly answers the `token_economy_and_information_design_index` core question `packet_size_budget`. No B04 claim states a numeric or formal "budget" directly; the concept is synthesized by combining that index question with B04-C011 (atomic task packets carrying explicit state frames instead of chat-history reconstruction) and the prompt/workflow lane's ownership of "bounded execution sequences" (B04-C006), which is the closest direct evidence for a low-token-cost concern in the ingested material.

## Operating Rules

```yaml
rules:
  - "A packet includes only target, current state, refs, constraints, next action, and stop condition — not the full evidence body behind each of those fields."
  - "Bounded, stage-gated, artifact-centered execution is preferred over broad autonomy or giant multi-phase prompts in subscription-chat or handoff contexts."
  - "When a packet strains against its budget, that pressure is itself a signal that the task is unclear or overloaded and should be split."
  - "Archives and full evidence bundles are exempt from the budget by design; the budget applies to routing/working packets, not durable evidence stores."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "Direct source of the packet_size_budget question this page is named after; primary framing source."
    coverage: "token_economy_and_information_design_index core_questions, lines 122-134."
  - source_id: "phase1-batch04-apex-application-patterns"
    rationale: "Supplies the concrete Apex evidence for bounded execution and atomic task packets that the budget concept generalizes from."
    coverage: "Claims B04-C007 (target/source/non-goals/output-contract/stop-condition named before execution), B04-C008 (bounded stage-gated execution preferred over broad autonomy), B04-C011 (atomic task packets over chat-history reconstruction), B04-C006 (prompt/workflow lane owns bounded execution sequences)."
```

## Macro / Meso / Micro

### Macro

Token economy is a cross-cutting concern in this KB's compile plan: file design, packet design, and progressive disclosure all exist to reduce token cost, drift, hallucination, and context overload. A packet size budget is the applied form of that concern at the level of a single handoff or task unit — the smallest useful shape that still carries enough authority and state to be actionable.

### Meso

Bounded, stage-gated, artifact-centered execution is explicitly preferred over broad autonomy or giant multi-phase prompts in subscription-chat or handoff contexts (B04-C008). Atomic task payloads carry explicit target, scope, input references, constraints, and validation conditions rather than open-ended context (B04-C011, and the atomic-task-payload concept in B04's concepts_extracted). The prompt/workflow lane's ownership list includes "bounded execution sequences" and "promptflow skeletons" (B04-C006) — reusable, size-constrained structures rather than open-ended prose — which is the closest direct evidence that budget-consciousness is a lane concern rather than an incidental style choice.

### Micro

`BEST_PRACTICES_v_old.md` lines 74-92 is the direct source for preferring bounded, stage-gated execution over broad autonomy (B04-C008); lines 190-230 are the direct source for explicit state frames and atomic task packets (B04-C011). `ESSENCE.md` lines 11-33 is the direct source for the prompt/workflow lane's ownership boundary, including bounded execution sequences (B04-C006). The compile plan's `token_economy_and_information_design_index` (lines 122-134) is where `packet_size_budget` appears as a named core question alongside `refs_not_copies`, `smallest_useful_file_shape`, and `yaml_first_artifact_design`.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "High-risk execution should carry explicit state frames and atomic task packets rather than relying on chat-history reconstruction."
    source_pointer: "phase1-batch04-apex-application-patterns claim B04-C011"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C002
    claim: "Bounded, stage-gated, artifact-centered execution is preferred over broad autonomy or giant multi-phase prompts in subscription-chat or handoff contexts."
    source_pointer: "phase1-batch04-apex-application-patterns claim B04-C008"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C003
    claim: "The prompt/workflow lane's ownership of 'bounded execution sequences' and 'promptflow skeletons' is the closest direct B04 evidence for a low-token-cost concern; formalizing this into a numeric or structural 'packet size budget' is a synthesis from the token_economy_and_information_design_index question framing rather than a direct B04 claim."
    source_pointer: "phase1-batch04-apex-application-patterns claim B04-C006; phase2-specialized-index-compile-plan-20260702 lines 122-134"
    confidence: "medium"
    claim_label: "working_hypothesis"
```

## Routes Here

```yaml
routes:
  - question: "How small should a handoff or task packet be before it starts becoming a new raw corpus?"
    leads_to: "claude-code-orchestration-design/concepts/packet-size-budget.md"
    rationale: "Direct match to the packet_size_budget core question."
  - related_page: "claude-code-orchestration-design/concepts/refs-not-copies.md"
    relation: "Refs-not-copies is the primary mechanism that keeps a packet inside its size budget."
  - related_page: "claude-code-orchestration-design/concepts/low-token-handoff-design.md"
    relation: "Packet size budget is one operational rule inside the broader low-token handoff design pattern."
```

## Evidence

```yaml
evidence:
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "claim B04-C011"
    supports: "Operating Rules: atomic task packets over chat-history reconstruction."
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "claim B04-C008"
    supports: "Meso section: bounded stage-gated execution preferred over broad autonomy."
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "claim B04-C006"
    supports: "Micro section and Key Claim C003: prompt/workflow lane's bounded-execution-sequence ownership."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_pointer: "token_economy_and_information_design_index core_questions, lines 122-134"
    supports: "Definition and Macro section."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "No B04 claim states an exact token or byte limit; any numeric budget remains policy work rather than an ingested fact."
    source_pointer: "phase2-specialized-index-compile-plan-20260702 lines 122-134"
    proposed_handling: "planning_task_candidate"
  - id: U002
    description: "Key Claim C003 and the overall page confidence are set to medium/working_hypothesis because the 'budget' framing is synthesized from the token_economy_and_information_design_index question rather than quoted directly from a B04 claim naming a size budget."
    source_pointer: "phase1-batch04-apex-application-patterns claim B04-C006"
    proposed_handling: "revisit_source"
```
