---
title: Claude Orchestration Implementation Brief
page_type: summary
kb_slug: old-apex-full-orchestration-agent-kb-v2
summary_slug: claude-orchestration-implementation-brief
source_refs:
  - {source_id: source-8c534a90902556f2, source_path: raw/other/managed/agents/AGENT_INDEX.md, source_hash: 9e02b3849e58a9175f7dac4494e26e5a20f22632c65c906db351f252b08365f6, source_pointer: Default routing; Hard overlap reminders, source_storage_mode: copy_into_kb}
  - {source_id: source-05bc8d6b022c9444, source_path: raw/other/managed/rules/AGENT_SWARM_INTERACTION_CANON.md, source_hash: f849f642eecfc16e377e69c92dcf1b3557d058012176f1398255b5b3b054f9fd, source_pointer: Default operating stance; Operational state model; Delegation rules; Handoff rules, source_storage_mode: copy_into_kb}
  - {source_id: source-2ba0a3729386cc27, source_path: raw/other/docs/HermesResearch/hermes-docs/user-guide/features/skills.md, source_hash: 1d4842327849dc40c6af332cb7ddf4698f2672f8b7215f60cd5f07460441bd54, source_pointer: Skills; Supported hub sources; Trust levels, source_storage_mode: copy_into_kb}
created_at: 2026-07-11T10:00:00Z
updated_at: 2026-07-11T10:00:00Z
confidence: mixed
claim_label: source_backed_summary
status: active
related_concepts: [source-authority-routing, macro-meso-micro-synthesis-loop]
related_entities: [meta-ops, meta-detective, special-ops-prompts-workflows]
review_flags: [operator_runtime_target]
---
# Claude Orchestration Implementation Brief

## Purpose and Scope
This page translates source-grounded Old Apex coordination constraints into an implementation brief for the operator-selected Claude runtime. It answers how to preserve role/state boundaries, handoffs, and validation. It does not claim that Hermes is the target runtime: Hermes is historical/reference evidence and, at most, a blueprint containing Hermes logic.

## Decision / Use Guidance
Build Claude orchestration around a small coordinator, explicit task-state records, specialist routes, and independent validation. Keep a direct executor for simple work; introduce the coordinator only when work is bounded, reviewable, and benefits from routing. Treat skills, plugins, and provider tooling as optional capability surfaces, not as authorization or architectural law.

## Adaptive Ranked Source Set
- source_id: source-05bc8d6b022c9444; rationale: highest authority for permission, delegation, and handoff design; coverage: state model and separation constraints.
- source_id: source-8c534a90902556f2; rationale: concrete routing realization; coverage: route selection and ownership boundaries.
- source_id: source-2ba0a3729386cc27; rationale: historical capability reference only; coverage: Hermes skills discovery, provenance, and trust behavior.

## Macro / Meso / Micro
### Macro
The reusable architecture is controlled delegation, not a particular historical runtime: semantic roles make accountability legible; task-scoped states decide permission; independent verification limits self-review. Claude is the implementation target under the operator contract, while the sources describe OpenClaw/old-Apex and Hermes-era evidence.

### Meso
Route ambiguous operator requests through intake, concrete bounded work through a coordinator, option-heavy work through strategy, and high-risk or weak-evidence work through adversarial validation. Put durable knowledge placement and reusable workflow-pattern ownership in their specialist surfaces. The PMKB/PD workflow is therefore operational Meta Ops evidence, not a complete Claude architecture.

### Micro
Persist a handoff record containing role, state, target, next state, prerequisites, action, and risk. Use BUILD for bounded creation, VERIFY for independent review and loop-back decisions, and LOCK for frozen/approval-bound work. A Hermes-style skill catalogue can inspire capability discovery and provenance checks, but it must not be copied as Claude runtime logic.

## Overlap and Evidence
The activation index and interaction canon independently support coordinator routing plus role/state boundaries; both also disallow broad uncontrolled overlap. Hermes skills documentation independently shows a capability catalogue with provenance/trust mechanics, but it is product-specific evidence. The first pair therefore supports the Claude orchestration pattern; the latter only supports the historical-blueprint comparison.

## Alternatives Ranked by Use Case
| Rank | Option | Best use | Evidence and trade-off |
|---|---|---|---|
| 1 | Claude coordinator + explicit state + independent verifier | Multi-step, high-impact, or evidence-sensitive work | Directly fits the two managed Apex sources; adds handoff overhead. |
| 2 | One Claude executor with explicit acceptance checks | Small, local, low-risk task | Fits the canon's "keep work local" guidance; fewer safeguards against self-review. |
| 3 | Hermes-inspired skill registry as a blueprint | Designing capability discovery/provenance | Historical/reference only; its Hermes logic is not Claude target runtime logic. |

## Key Claims
- claim_id: CI01; claim: The managed model makes operational state the permission layer and semantic role the accountability layer.; source_pointer: AGENT_SWARM_INTERACTION_CANON.md#Default-operating-stance; confidence: high; claim_label: source_backed_summary
- claim_id: CI02; claim: Concrete bounded execution starts with Meta Ops, while option uncertainty and high drift risk add Strategy and Detective respectively.; source_pointer: AGENT_INDEX.md#Default-routing; confidence: high; claim_label: source_backed_summary
- claim_id: CI03; claim: Build and review of the same exact change should stay separated where risk or authority matters.; source_pointer: AGENT_SWARM_INTERACTION_CANON.md#Role-switching-and-separation-rules; confidence: high; claim_label: source_backed_summary
- claim_id: CI04; claim: Hermes documents skills as installable capability bundles with source and trust distinctions.; source_pointer: Hermes skills.md#Supported-hub-sources-and-Trust-levels; confidence: medium; claim_label: raw_source

## Routes Here
- question: What should the Claude orchestration runtime preserve from Old Apex?; leads_to: wiki/entities/meta-ops.md; rationale: coordinator boundary and handoff design.
- question: Should Hermes be implemented as the runtime?; leads_to: wiki/concepts/source-authority-routing.md; rationale: distinguish historical/reference evidence from target decisions.
- question: How do we route System 2 questions without a wiki page?; leads_to: ingest-analysis/phase1-agent-architecture.md; rationale: Phase 1 is the required fallback knowledge surface until compiled coverage exists.
- question: Where do PMKB/PD reusable workflows fit?; leads_to: wiki/entities/special-ops-prompts-workflows.md; rationale: reusable workflow ownership is not coordinator authority.

## Uncertainty / Raw Source Reopen Triggers
- id: U-CI01; description: Claude is the operator-selected target, not a historical source claim; reopen the operator handover or future Claude-specific evidence before making runtime-specific assertions.; source_pointer: operator-handover#Claude-target; proposed_handling: ask_operator
- id: U-CI02; description: No compiled System 2 wiki page exists in this KB. For System 2 questions, read ingest-analysis first, especially phase1-*.md, and do not claim compiled coverage.; source_pointer: ingest-analysis/phase1-agent-architecture.md; proposed_handling: revisit_source
- id: U-CI03; description: Hermes capabilities and trust behavior are product-specific; use only as historical/blueprint evidence and reopen the raw Hermes document for any feature-level comparison.; source_pointer: Hermes skills.md#Supported-hub-sources; proposed_handling: revisit_source
