---
title: "Prompt Pack and Artifact Contract Design"
page_type: summary
kb_slug: "claude-code-orchestration-design"
summary_slug: "prompt-pack-and-artifact-contract-design"
source_refs:
  - source_id: "claude-skill-package-bestpractice-handover"
    source_path: "raw/source-groups/claude-skill-design/sources/operator-supplied/notes/Claude_Skill_Package_BestPractice_Handover.md"
    source_hash: "NA"
    source_pointer: "lines 305-336 (reference-file schema ownership rules), 390-408 (single-source-of-truth and no-schema-duplication rules with defect examples)"
    source_storage_mode: "pointer_only"
  - source_id: "prompt-engineering-dependency-contract"
    source_path: "raw/source-groups/prompt-engineer-research-base/raw/refs/current-promptengineer-package/prompt-engineering-dependency-contract.md"
    source_hash: "NA"
    source_pointer: "lines 1-70, owns/must_not_own + upstream_authority/downstream_consumer contract shape"
    source_storage_mode: "pointer_only"
created_at: "2026-07-11T00:00:00Z"
updated_at: "2026-07-11T00:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - "standard-handoff-packet"
  - "yaml-first-artifact-design"
  - "packet-size-budget"
related_entities: []
review_flags: []
---

# Prompt Pack and Artifact Contract Design

## Core Summary

A "prompt pack" or "artifact contract" is a file whose job is to define a schema or interface once and be the single place other files point back to -- not a place to restate logic already owned elsewhere. The corpus's own practitioner guide names the concrete failure mode this design guards against (the same schema defined in three separate files, costing ~800 redundant tokens per load) and the concrete rule that prevents it (exactly one owning file per schema; every other reference writes `canonical_source: the-owning-file-path` instead of re-defining). This KB's own Apex `prompt_engineering_dependency_contract.md` is a real, working instance of that same rule, expressed as explicit `owns` / `must_not_own` lists plus `upstream_authority` / `downstream_consumer` pointers.

## What This Adds

```yaml
adds:
  - "The named failure mode (triple schema definition, ~800 redundant tokens/load) that motivates single-owner contract design."
  - "The concrete rule: canonical_source: the-owning-file-path as the cross-reference mechanism instead of re-defining a schema."
  - "A real Apex example (owns/must_not_own + upstream_authority/downstream_consumer) showing the same rule applied to a live dependency contract between two Apex skills."
clarifies:
  - "A contract file's purpose is interface definition and non-ownership boundaries, not prompt-writing doctrine itself -- the Apex example explicitly states 'This file is an interface contract, not prompt doctrine.'"
limits:
  - "Does not restate Apex's own prompt-engineering or PreCapNextDay skill internals; treat prompt-engineering-dependency-contract.md as the authoritative source for that system, referenced here only as a design-pattern example."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - rank: 1
    source_id: "prompt-engineering-dependency-contract"
    rationale: "Deterministic term-frequency ranking (topic-source-rankings.json, topic prompt-pack-and-artifact-contract-design) placed this file first with 76 keyword hits; it is a complete, real, working artifact contract rather than a description of one."
    coverage: "Full owns/must_not_own declaration, upstream_authority references to the canonical schema-owning files, and downstream_consumer list -- a live interface contract between two Apex skills."
  - rank: 2
    source_id: "claude-skill-package-bestpractice-handover"
    rationale: "Second-ranked (49 keyword hits); an operator-authored, cross-project distillation (P0-P1 tier, claude-skill-design source group) of the general rule this KB's own Apex contract file is an instance of, including a named real defect the rule was written to prevent."
    coverage: "Reference-file structure rules, schema-ownership rule with concrete violation cost, single-source-of-truth pattern for shared lists/values, and context-carry-forward verification steps for sequential generation."
```

## Macro / Meso / Micro

### Macro

The core design problem a prompt pack or artifact contract solves is not "how do I format a prompt" -- it's "how do multiple files/skills that need to agree on the same shape avoid drifting apart." The pattern that recurs across both the general guide and this KB's own Apex system is the same: exactly one file owns a given schema; every other file that needs it references the owner by path instead of copying the shape inline. This is a token-efficiency argument as much as a correctness one -- duplicated schema definition was measured, not assumed, to cost real tokens on every load.

### Meso

The general guide states the rule directly: "Each schema is defined in EXACTLY ONE file. No other file may redefine it. Other files that need to reference a schema write: canonical_source: references/filename.md" (lines 320-325), and grounds it in a real observed defect: "Triple definition was found in the v1 contract file — same schema in artifact_contract, Normalized Structure, and Section Contracts. Cost: ~800 redundant tokens per load" (lines 325-327). The same guide extends this beyond schemas to shared values: "The canonical project list is defined once in binding_decisions. No per-file content hardcodes the project list... defect_found: The project list was hardcoded in 4 separate per-prompt requirement blocks, creating drift risk" (lines 396-403). This KB's own Apex dependency contract applies exactly this discipline structurally: its frontmatter-equivalent YAML block declares `owns:` (a list of ten things this file is the canonical source for) and `must_not_own:` (an explicit list of eleven adjacent schemas it must not redefine, e.g. `prompt_packet_schema`, `provider_specific_prompting_rules`, `routing_decision_schema`), then names `upstream_authority` (the actual owning files for each of those excluded schemas) and `downstream_consumer` (which skill and which of its outputs depend on this contract) (prompt-engineering-dependency-contract.md lines 5-49).

### Micro

The general guide additionally specifies enforcement-adjacent constraints that keep this pattern maintainable at scale: contract files should target "under 100 lines," manifest files "under 60 lines" (lines 333-335), and when generating a sequence of files that must stay mutually consistent, "load all previously generated files before writing the next one. Verify: (a) no schema you are about to write is already owned by a prior file, (b) all key names match prior files" (lines 405-408) -- an explicit anti-drift check rather than an assumption that consistency will hold. The Apex contract's own `must_not_own` list is the same idea applied preemptively at design time rather than caught after the fact: it names `prompt_packet_schema`, `prompt_sequence_schema`, `final_copy_paste_prompt_schema`, `provider_specific_prompting_rules`, `prompt_task_taxonomy`, `iteration_loop_patterns`, `routing_decision_schema`, `workflow_stage_taxonomy`, `process_stage_taxonomy`, `flow_prompt_pack_schema`, and `daily_plan_schema` as schemas this file must never redefine, each with a named `upstream_authority` file that actually owns it (prompt-engineering-dependency-contract.md lines 18-29, 33-42).

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Each schema must be defined in exactly one file; every other file that needs it should write canonical_source: the-owning-file-path rather than redefining the schema, because a real prior defect (the same schema tripled across three sections of one contract file) cost roughly 800 redundant tokens per load."
    source_pointer: "Claude_Skill_Package_BestPractice_Handover.md lines 320-327"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages: []
  - claim_id: C002
    claim: "Shared values (not just schemas) should also have exactly one canonical source; a real prior defect hardcoded the same project list in four separate per-prompt requirement blocks, creating drift risk."
    source_pointer: "Claude_Skill_Package_BestPractice_Handover.md lines 396-403"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages: []
  - claim_id: C003
    claim: "This KB's own Apex prompt_engineering_dependency_contract explicitly declares both an owns list (ten items it is the canonical source for) and a must_not_own list (eleven adjacent schemas it must never redefine), each mapped to an upstream_authority file that actually owns it."
    source_pointer: "prompt-engineering-dependency-contract.md lines 5-49"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages: []
  - claim_id: C004
    claim: "The guide recommends target length ceilings for contract files (under 100 lines) and manifest files (under 60 lines), plus an explicit verification step before writing each new file in a generated sequence: confirm no schema about to be written is already owned by a prior file, and that key names match prior files."
    source_pointer: "Claude_Skill_Package_BestPractice_Handover.md lines 333-335, 405-408"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages: []
```

## Routes Here

```yaml
routes:
  - question: "How should I structure a schema/contract file so it doesn't drift from other files that depend on it?"
    leads_to: "wiki/summaries/prompt-pack-and-artifact-contract-design.md"
    rationale: "Direct single-schema-owner rule with a named real-world defect it prevents."
  - question: "Is there a real example of an owns/must_not_own artifact contract in this system?"
    leads_to: "wiki/summaries/prompt-pack-and-artifact-contract-design.md"
    rationale: "Cites this KB's own live Apex dependency contract as a concrete instance of the general pattern."
  - related_page: "wiki/concepts/standard-handoff-packet.md"
    relation: "Companion concept on handoff-packet shape; this page focuses on the schema-ownership rule that keeps such packets non-duplicative."
  - related_page: "wiki/concepts/yaml-first-artifact-design.md"
    relation: "Companion concept on why these contracts are written YAML-first; this page covers what content they should and should not own."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "This page treats the Apex prompt_engineering_dependency_contract.md purely as a design-pattern example, per operator instruction to cross-reference rather than duplicate Apex's own artifact-contract work; it does not attempt to verify whether PreCapNextDay or the prompt-engineering skill currently comply with every owns/must_not_own boundary declared in that file."
    proposed_handling: "leave_as_gap"
  - id: U002
    description: "The ~800-redundant-token-per-load figure and the four-per-prompt-block hardcoding defect are both retrospective incident reports from the source guide's own project history, not independently re-measured for this KB."
    source_pointer: "Claude_Skill_Package_BestPractice_Handover.md lines 325-327, 400-403"
    proposed_handling: "leave_as_gap"
```
