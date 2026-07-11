---
title: Source Authority and Connection Map
page_type: summary
kb_slug: operator-research-orchestration-20260711
summary_slug: source-authority-and-connection-map
source_refs:
  - source_id: dr-apexorchestrationclaude
    source_path: raw/notes/DR_ApexOrchestrationClaude.md
    source_pointer: Validated Source List; Step-by-Step Build Order; Architecture Validation
  - source_id: prompt-flow-create-claude-native-apex-alfred-orchestration-predefinition-files
    source_path: raw/notes/Prompt Flow_Create Claude-Native Apex Alfred Orchestration Predefinition Files.md
    source_pointer: Hard Scope; Translation Rule; Fixed File Sequence
  - source_id: apex-hermes-claude-build-pack
    source_path: raw/notes/Apex Hermes Claude Build Pack.md
    source_pointer: 0. Document Control; 1. 00_SYSTEM_INTENT.md; 8. Acceptance Checks
  - source_id: apex-hermesarchitectrueguidacne
    source_path: raw/notes/Apex&HermesArchitectrueGuidacne.md
    source_pointer: 0. Status; 2. Fixed Profile Architecture; 16. Recommended Evolution Process
  - source_id: apex-hermes-workflow-example-database-master-of-arts-v0-1-1
    source_path: raw/notes/Apex_Hermes_Workflow_Example_Database_Master_of_Arts_v0_1 (1).md
    source_pointer: 1. Source Scan Summary; 6. Workflow Records; 8. Profile Ownership Map
  - source_id: dr-apex-pm-kb-pd-gem
    source_path: raw/notes/DR_APEX_PM_KB_PD_Gem.md
    source_pointer: Phase 2: Process Options and Evaluation; Phase 3: Sub-Skill Grouping Analysis
  - source_id: dr-apex-pm-kb-pd-gpt
    source_path: raw/notes/DR_APEX_PM_KB_PD_GPT.md
    source_pointer: Scope and method; Project/Knowledge/Product management execution options; Final summary table
  - source_id: dr-apex-pm-kb-pd-perp
    source_path: raw/notes/DR_APEX_PM_KB_PD_Perp.md
    source_pointer: 0. Scope status; 2. Per-process options; 4. Processes lacking viable pattern
  - source_id: dr-apex-plan
    source_path: raw/notes/DR_Apex_Plan.md
    source_pointer: Package Summary; Planning Contract; Task Decomposition Rules; Operator Gate
  - source_id: apex-hermes-orchestration-decisions-v0-1
    source_path: raw/notes/apex_hermes_orchestration_decisions_v0_1.md
    source_pointer: whole document
  - source_id: apexagent-workflowsnonaccurate
    source_path: raw/notes/ApexAgent&WorkflowsNonAccurate.md
    source_pointer: Source Scan Summary; Agent Interaction Map; Hermes Translation Map
  - source_id: architecturecheckclaudevshermesvsgpt
    source_path: raw/notes/ArchitectureCheckClaudeVsHermesVsGPT.md
    source_pointer: Full Architecture Analysis; Recommended Default Pattern; Core Design Principle
  - source_id: processranking-gpt-masteroa
    source_path: raw/notes/ProcessRanking_GPT&MasterOA.md
    source_pointer: Selection logic; Top 10 process portfolio; Minimal complete process library
  - source_id: sourceindexprojectgpt
    source_path: raw/notes/SourceIndexProjectGPT.md
    source_pointer: Source Lookup Map; Q&A Decision Flow; Proposed Workflow; Assumptions
  - source_id: sourceindexagentinteraction07oc
    source_path: raw/notes/SourceIndexAgentInteraction07OC.md
    source_pointer: whole document
  - source_id: sourceindexagentinteractionalfred
    source_path: raw/notes/SourceIndexAgentInteractionAlfred.md
    source_pointer: whole document
created_at: 2026-07-11T10:10:00Z
updated_at: 2026-07-11T10:10:00Z
confidence: mixed
claim_label: source_backed_summary
status: active
related_concepts: [source-authority, claude-native-translation, convergence-evidence]
related_entities: []
review_flags: [all-sources-mapped; source-content-depth-varies]
---

# Source Authority and Connection Map

## Core Summary

Use this page before treating any source as an architecture decision. The corpus consists of three different kinds of material: Claude-targeted implementation evidence, historical Apex/Hermes design evidence, and research/index material that helps compare or locate patterns. They do not have equal authority. The first class determines Claude decisions; the second supplies abstractions to translate; the third contributes options, provenance, and gaps.

## What This Adds

```yaml
adds:
  - A role and connection for every retained raw source.
  - A practical authority order for conflict resolution.
  - Explicit treatment of indexes and incomplete research as navigation evidence rather than architecture truth.
clarifies:
  - Repeated historical wording is not a Claude implementation decision.
  - A source that says it is incomplete cannot be used as sole authority.
limits:
  - This is a connection map; detailed source analyses remain the evidence layer for individual claims.
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: dr-apexorchestrationclaude
    rationale: Highest Claude-targeted decision relevance.
    coverage: Claude constraints, role model, durable state, validation, build order.
  - source_id: prompt-flow-create-claude-native-apex-alfred-orchestration-predefinition-files
    rationale: Direct Claude-native authoring contract.
    coverage: Translation boundary, scope firewall, ordered artifact creation, role definitions.
  - source_id: apex-hermes-claude-build-pack
    rationale: Strong macro design and artifact contract evidence.
    coverage: Intent, lifecycle, acceptance, excluded/deprecated patterns.
  - source_id: apex-hermes-workflow-example-database-master-of-arts-v0-1-1
    rationale: Strongest operational workflow detail.
    coverage: Workflow records, handoffs, inputs, outputs, mechanism fit, validation.
  - source_id: dr-apex-pm-kb-pd-gem
    rationale: Detailed mechanism alternatives and deterministic/LLM division.
    coverage: PM/KB/PD process grouping, token/cost and implementation modality tradeoffs.
```

## Macro / Meso / Micro

### Macro

Authority order: Claude-targeted research and Claude-native authoring contract; then macro architecture and workflow evidence; then PM/KB/PD options; then indexes, rankings, and partial comparison material. A lower source can reveal a useful pattern, but cannot override a higher Claude-targeted constraint without an explicit decision and evidence.

### Meso

`DR_ApexOrchestrationClaude` and the authoring flow define target and translation. The build pack, architecture guidance, decisions file, workflow database, and agent catalog form one historical design cluster: use them to extract role boundaries, lifecycle, handoffs, and validation—not runtime mechanics. PM/KB/PD Gem, GPT, and Perplexity form an options cluster: use them to choose implementation modality by process. `DR_Apex_Plan` is a focused planning-contract candidate. Process ranking and source indexes are discovery/navigation inputs, not canonical decisions.

### Micro

`ArchitectureCheckClaudeVsHermesVsGPT` is a historical comparison and must route only to translation/review, not target selection. `ApexAgent&WorkflowsNonAccurate` self-identifies uncertainty and is candidate-only. `DR_APEX_PM_KB_PD_Perp` explicitly limits its evidence to two sources, so it can corroborate but not settle an option. `SourceIndexProjectGPT` contains a rich question flow and source lookup map but is an index; claims must reopen the linked raw material. The two smaller SourceIndexAgentInteraction files are locator aids until their referenced content is verified.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: Claude-targeted research and the Claude-native authoring contract are the decision authority for the target architecture.
    source_pointer: "DR_ApexOrchestrationClaude.md > opening findings; Prompt Flow... > Translation Rule and Hard Scope"
    confidence: high
    claim_label: source_backed_summary
    used_in_pages: [wiki/summaries/claude-native-apex-orchestration.md]
  - claim_id: C002
    claim: Historical Apex/Hermes documents form an evidence cluster for abstract patterns, not a target runtime specification.
    source_pointer: "Apex Hermes Claude Build Pack.md > 0. Document Control; Apex&HermesArchitectrueGuidacne.md > 0. Status; Prompt Flow... > Translation Rule"
    confidence: high
    claim_label: source_backed_summary
    used_in_pages: [wiki/summaries/core-pattern-convergence.md]
  - claim_id: C003
    claim: PM/KB/PD reports are decision-option evidence whose strength varies by report scope and source coverage.
    source_pointer: "DR_APEX_PM_KB_PD_Gem.md > Phase 1–4; DR_APEX_PM_KB_PD_GPT.md > Scope and method; DR_APEX_PM_KB_PD_Perp.md > 0. Scope status"
    confidence: high
    claim_label: source_backed_summary
    used_in_pages: [wiki/summaries/orchestration-alternatives-by-use-case.md]
  - claim_id: C004
    claim: Source indexes and process rankings improve navigation but cannot independently establish implementation truth.
    source_pointer: "SourceIndexProjectGPT.md > Source Lookup Map; ProcessRanking_GPT&MasterOA.md > Selection logic"
    confidence: high
    claim_label: source_backed_summary
    used_in_pages: [wiki/summaries/core-pattern-convergence.md]
```

## Routes Here

```yaml
routes:
  - question: Which source should decide this architecture question?
    leads_to: wiki/summaries/source-authority-and-connection-map.md
    rationale: Establishes authority and source scope.
  - question: Is this a repeated core pattern or a historical proposal?
    leads_to: wiki/summaries/core-pattern-convergence.md
    rationale: Applies the overlap/evidence model.
  - question: Which mechanism fits a PM, KB, or PD process?
    leads_to: wiki/summaries/orchestration-alternatives-by-use-case.md
    rationale: Routes to option ranking.
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: The exact lineage among historical design documents is not yet proven; they may not be independent evidence.
    source_pointer: "Apex Hermes Claude Build Pack.md > Source grounding; SourceIndexProjectGPT.md > Source Inventory"
    proposed_handling: revisit_source
  - id: U002
    description: Smaller index files can point to missing or external material; do not elevate their summaries to source truth.
    source_pointer: "SourceIndexAgentInteraction07OC.md > whole document; SourceIndexAgentInteractionAlfred.md > whole document"
    proposed_handling: revisit_source
```
