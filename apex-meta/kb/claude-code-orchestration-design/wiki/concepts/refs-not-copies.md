---
title: "Refs Not Copies"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "refs-not-copies"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 124-137; refs_not_copies"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C009, B04-C014; clean handoffs and proof"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "medium"
claim_label: "working_hypothesis"
status: "active"
related_concepts:
  - "packet-size-budget"
  - "compiled-kb-before-raw-source"
  - "yaml-first-artifact-design"
related_entities: []
review_flags: []
---

# Refs Not Copies

## Definition

Refs-not-copies is the rule that artifacts should carry pointers to sources, pages, and files instead of duplicating their full content. It directly answers the `token_economy_and_information_design_index` core question `refs_not_copies`. The concept is grounded most directly in B04-C012 (the promptflow base build contract's requirement for thin scaffolds and deep appendices, pushing dense schemas and examples into referenced files rather than the main activation file), and generalized here to apply to any Apex artifact, not only `SKILL.md`-shaped activation files — a generalization the compile plan's index question invites but that no single B04 claim states for artifacts in general.

## Operating Rules

```yaml
rules:
  - "A page or packet that needs evidence should carry a source pointer (path, anchor, or line range) rather than the full evidence body."
  - "A short quote or exact field value may be inlined when local clarity requires it, but the bulk of supporting material stays in the referenced source."
  - "Activation-level files (skills, scaffolds) stay compact; detailed schemas, examples, and appendices live in separately referenced files."
  - "Future agents follow the reference to verify a claim instead of trusting a copied summary at face value."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase1-batch04-apex-application-patterns"
    rationale: "Primary direct evidence: B04-C012 and the paired contradiction B04-C018/B04-T001 describe the concrete thin-scaffold-deep-appendices practice this concept generalizes into a refs-not-copies rule."
    coverage: "Claims B04-C009 (clean handoffs), B04-C012 (thin scaffold, deep appendices), B04-C014 (fetch-back proof over restated content), B04-C018/B04-T001 (tension between contract completeness and activation-file concision)."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "Names refs_not_copies directly as a token_economy_and_information_design_index core question, the exact framing this page compiles toward."
    coverage: "token_economy_and_information_design_index core_questions, lines 122-134."
```

## Macro / Meso / Micro

### Macro

The token-economy index treats "refs, not copies" as one of the load-bearing techniques for reducing context overload alongside `compiled_kb_pages_vs_raw_sources`, `yaml_first_artifact_design`, and `smallest_useful_file_shape`. The underlying principle recurs across the ingested corpus in a narrower form: keep the thing an agent loads by default small, and let it reach for more detail only when needed.

### Meso

The promptflow base build contract enforces a "thin scaffold, deep appendices" architecture, where activation files stay compact and detailed schemas or evidence live in referenced appendices (B04-C012). This is explicitly identified as a point of tension (B04-C018/B04-T001): Apex needs rich execution contracts, but both the promptflow source and the skill-design source push dense examples and schemas out of the main activation file and into references. Refs-not-copies is the resolution the sources converge on — keep the reference, not the copy, at the activation layer, and let the fetch-back/closure discipline (B04-C014) confirm the referenced content when it actually matters.

### Micro

`PROMPTFLOW_KB_BASE_BUILD.md` lines 54-64 is the direct source for thin-scaffold-deep-appendices (B04-C012). `Apex_Alfred_Skill_Definition_Guide.md` lines 85-93 is the paired source for the same concision pressure at the `SKILL.md` level (B04-C018/B04-T001). The compile plan's token_economy_and_information_design_index (line 129) is where `refs_not_copies` appears as its own named core question, distinct from but adjacent to `compiled_kb_pages_vs_raw_sources` and `smallest_useful_file_shape`.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "The promptflow base build contract enforces repo boundary, target lock, source authority, thin scaffold/deep appendices, index plausibility checks, and quality gates before scaffold drafting."
    source_pointer: "phase1-batch04-apex-application-patterns claim B04-C012"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C002
    claim: "There is a tension between prompt/workflow artifact completeness and SKILL.md concision: Apex needs detailed contracts, but both the promptflow source and skill-design source push dense examples/schemas into appendices or references rather than the main activation file."
    source_pointer: "phase1-batch04-apex-application-patterns claim B04-C018 / contradiction B04-T001"
    confidence: "medium"
    claim_label: "source_backed_summary"
  - claim_id: C003
    claim: "Generalizing thin-scaffold-deep-appendices into an Apex-wide 'refs, not copies' rule for all artifacts (not only SKILL.md-shaped files) is a synthesis driven by the token_economy_and_information_design_index's refs_not_copies question rather than a direct B04 claim about artifacts in general."
    source_pointer: "phase2-specialized-index-compile-plan-20260702 line 129"
    confidence: "medium"
    claim_label: "working_hypothesis"
```

## Routes Here

```yaml
routes:
  - question: "Should a packet copy in the full evidence it depends on, or just point at it?"
    leads_to: "claude-code-orchestration-design/concepts/refs-not-copies.md"
    rationale: "Direct match to the refs_not_copies core question."
  - related_page: "claude-code-orchestration-design/concepts/packet-size-budget.md"
    relation: "Refs-not-copies is the primary mechanism that keeps a packet inside its size budget."
  - related_page: "claude-code-orchestration-design/concepts/compiled-kb-before-raw-source.md"
    relation: "Shared token-economy family: prefer compiled/referenced material over inlined raw content."
```

## Evidence

```yaml
evidence:
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "claim B04-C012"
    supports: "Definition and Meso section: thin scaffold, deep appendices."
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "claim B04-C018 / contradiction B04-T001"
    supports: "Meso section and Key Claim C002: concision-vs-completeness tension."
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "claim B04-C014"
    supports: "Operating Rules: fetch-back verification of referenced content."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_pointer: "token_economy_and_information_design_index core_questions, line 129"
    supports: "Definition and Key Claim C003."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "B04-C012 and B04-C018 ground the pattern specifically at the SKILL.md/scaffold-file level; extending 'refs, not copies' as a rule for all Apex artifacts (packets, pages, entities) is a working hypothesis synthesized from the token_economy index's question framing, not a directly quoted B04 claim about artifacts in general."
    source_pointer: "phase1-batch04-apex-application-patterns claims B04-C012, B04-C018; phase2-specialized-index-compile-plan-20260702 line 129"
    proposed_handling: "revisit_source"
  - id: U002
    description: "Line-accurate source validation (confirming a given ref actually points at the claimed content) is a deterministic postflight concern, not resolved within this compile pass."
    source_pointer: "phase2-specialized-index-compile-plan-20260702 next_action, lines 216-222"
    proposed_handling: "planning_task_candidate"
```
