# KB_STARTING_SOURCE_MAP

## Purpose

This file defines the starting-source map for seeding, auditing, and routing OpenClaw managed knowledge.

It is a source map. It is not a truth surface, not a promotion ledger, not an agent KB, and not a runtime configuration file.

## Scope

This file covers:

- source classes used during first-wave KB seeding
- authority order for interpreting source material
- final-system surfaces that may receive routed knowledge
- binding lock and decision sources used as architecture inputs
- current seed sources used as implementation evidence
- current governance and process sources used as managed-system evidence
- per-agent KB target mapping
- evidence-only staging and source boundaries
- source-to-target routing rules
- safeguards against accidental canonization

This file does not cover:

- full source dumps
- long research summaries
- full lock-file contents
- full promotion ledger entries
- per-agent rich doctrine
- handoff process schemas
- runtime config changes
- source or staging folder patches

## Source classes

| Source class | Use | Authority posture | Runtime patch target |
|---|---|---|---:|
| `final_system_surface` | Current implementation truth inside `OpenClaw/07_finalopenclawsystem/` | highest implementation evidence for current runtime files | yes, only when the target file itself is in final-system scope |
| `binding_lock_source` | Locked decisions, finality rules, governance specifications, role boundaries, and ambiguity resolutions | authority input for final v1 decisions | no |
| `current_seed_source` | Existing compact agent files under `managed/agents/` | evidence for current activation surfaces and seed rewrite needs | yes, only for the corresponding seed file |
| `current_governance_source` | Existing managed knowledge, rules, rituals, and process files | evidence for current governance/process state | yes, only for the corresponding final-system file |
| `per_agent_kb_target` | Final KB destination under `managed/agent_kb/<agent_id>/` | target for accepted rich doctrine and candidate learning capture | yes, only when creating or updating the KB target through the promotion path |
| `evidence_only_staging_source` | Research, staging, pre-lock, continuation, and source-pack material outside the final runtime boundary | evidence only | no |
| `operator_decision_source` | Explicit human/operator ruling, approval, or rejection | authority input when required by promotion, escalation, or config review | no, unless the ruling authorizes a specific final-system patch |

## Authority order summary

Use this order when source classes appear to conflict:

1. `final_system_surface` for the current state of runtime files.
2. `binding_lock_source` for locked final v1 architecture, governance, scaffold, and boundary decisions.
3. `operator_decision_source` when a human ruling is required or already recorded.
4. `current_governance_source` for current managed-law, ritual, knowledge, and process implementation evidence.
5. `current_seed_source` for current compact activation implementation evidence.
6. `per_agent_kb_target` for accepted per-agent doctrine after creation and promotion.
7. `evidence_only_staging_source` for historical, research, or source-pack support.

Conflict handling:

- **Rule:** Do not average conflicting source classes.
- **Rule:** Do not use a lower-authority source to silently override a higher-authority source.
- **Rule:** Route unresolved authority conflict to the relevant validator, promotion packet, hygiene finding, or operator decision.
- **Rule:** Treat source material as evidence until it is placed in a final-system surface through the governed path.

## Final-system surfaces

Final-system surfaces are the only valid runtime patch targets for this map.

| Surface class | Canonical location | Role |
|---|---|---|
| compact agent seeds | `OpenClaw/07_finalopenclawsystem/managed/agents/` | runtime activation specs and KB pointers |
| per-agent KB roots | `OpenClaw/07_finalopenclawsystem/managed/agent_kb/<agent_id>/` | accepted rich doctrine, practices, mistakes, templates, and candidate queues |
| shared knowledge governance | `OpenClaw/07_finalopenclawsystem/managed/knowledge/` | cross-agent KB governance, source mapping, promotion templates, overlap matrices, and durable manifests |
| managed rules | `OpenClaw/07_finalopenclawsystem/managed/rules/` | operating law, escalation law, promotion law, hygiene law, project-interface law, and swarm-interaction law |
| managed rituals | `OpenClaw/07_finalopenclawsystem/managed/rituals/` | startup, session trace, night planning, heartbeat, and checklist protocols |
| managed processes | `OpenClaw/07_finalopenclawsystem/managed/processes/` | orchestration and handoff process contracts |
| companion docs | `OpenClaw/07_finalopenclawsystem/docs/` | explanatory support only |
| user surfaces | `OpenClaw/07_finalopenclawsystem/user/` | user-owned local truth, identity, override, and memory surfaces |
| runtime config | `OpenClaw/07_finalopenclawsystem/managed/config/openclaw.json` | runtime configuration only; no KB governance doctrine is written here |

## Binding lock and decision sources

Binding lock and decision sources may guide final-system rewrites and KB seeding, but they are not runtime patch targets.

| Source | Source class | Use | Target routing |
|---|---|---|---|
| `OpenClaw/07_finalopenclawsystem/NewFinals/NextLevel2/Executive Final Lock.md` | `binding_lock_source` | top-level final v1 architecture, non-goals, and final target tree | shared governance, seed rewrite boundaries, KB root creation |
| `OpenClaw/07_finalopenclawsystem/NewFinals/NextLevel2/LOCKED_DECISION_REGISTER.md` | `binding_lock_source` | atomic decisions, conflict handling, and required score scale | promotion templates, validation criteria, shared governance |
| `OpenClaw/07_finalopenclawsystem/NewFinals/NextLevel2/GOVERNANCE_AND_INDEX_SPECIFICATIONS.md` | `binding_lock_source` | governance/index surfaces and source-map boundaries | `managed/knowledge/`, `managed/agent_kb/AGENT_KB_INDEX.md` |
| `OpenClaw/07_finalopenclawsystem/NewFinals/NextLevel2/LEARNING_PROMOTION_FINALITY_SPECIFICATION.md` | `binding_lock_source` | KB scaffold, learning lifecycle, finality, and candidate queue rules | per-agent KB scaffold, promotion template, learning queue boundaries |
| `OpenClaw/07_finalopenclawsystem/NewFinals/NextLevel2/ROLE_BOUNDARY_AND_HANDOFF_SPECIFICATION.md` | `binding_lock_source` | role boundaries, validator pairings, and handoff semantics | compact seeds, overlap matrix, handoff process surfaces |
| `OpenClaw/07_finalopenclawsystem/NewFinals/NextLevel2/PRE_LOCK_PACK_AMBIGUITY_RESOLUTION_QA.md` | `binding_lock_source` | ambiguity resolution, approval conditions, schema minimums, and review cadence | governance surfaces and validation criteria |

## Current seed sources

Current seed sources are evidence for compact activation and KB pointer alignment.

| Agent ID | Current seed path | Source class | Primary routing use |
|---|---|---|---|
| `alfred` | `OpenClaw/07_finalopenclawsystem/managed/agents/alfred.md` | `current_seed_source` | activation seed rewrite and `managed/agent_kb/alfred/` seeding |
| `meta_ops` | `OpenClaw/07_finalopenclawsystem/managed/agents/meta_ops.md` | `current_seed_source` | activation seed rewrite and `managed/agent_kb/meta_ops/` seeding |
| `meta_strategy` | `OpenClaw/07_finalopenclawsystem/managed/agents/meta_strategy.md` | `current_seed_source` | activation seed rewrite and `managed/agent_kb/meta_strategy/` seeding |
| `meta_detective` | `OpenClaw/07_finalopenclawsystem/managed/agents/meta_detective.md` | `current_seed_source` | activation seed rewrite and `managed/agent_kb/meta_detective/` seeding |
| `special_ops__knowledge_bank` | `OpenClaw/07_finalopenclawsystem/managed/agents/special_ops__knowledge_bank.md` | `current_seed_source` | activation seed rewrite and `managed/agent_kb/special_ops__knowledge_bank/` seeding |
| `special_ops__informatics_design` | `OpenClaw/07_finalopenclawsystem/managed/agents/special_ops__informatics_design.md` | `current_seed_source` | activation seed rewrite and `managed/agent_kb/special_ops__informatics_design/` seeding |
| `special_ops__prompts_workflows` | `OpenClaw/07_finalopenclawsystem/managed/agents/special_ops__prompts_workflows.md` | `current_seed_source` | activation seed rewrite and `managed/agent_kb/special_ops__prompts_workflows/` seeding |
| `special_ops__ai_handling_routing` | `OpenClaw/07_finalopenclawsystem/managed/agents/special_ops__ai_handling_routing.md` | `current_seed_source` | activation seed rewrite and `managed/agent_kb/special_ops__ai_handling_routing/` seeding |
| `special_ops__hygiene_clean` | `OpenClaw/07_finalopenclawsystem/managed/agents/special_ops__hygiene_clean.md` | `current_seed_source` | activation seed rewrite and `managed/agent_kb/special_ops__hygiene_clean/` seeding |

## Current governance and process sources

Current governance and process sources identify where shared logic already lives and where source evidence should route.

| Source path | Source class | Use | Routing note |
|---|---|---|---|
| `managed/rules/OPERATING_SPINE_CANON.md` | `current_governance_source` | top-level operating law | keep as governing law; do not duplicate into KB map |
| `managed/rules/ESCALATION_EXCEPTION_BLOCK.md` | `current_governance_source` | stop, hold, exception, and escalation law | route stop/hold conflicts here, not into KB entries |
| `managed/rules/PROMOTION_PROTOCOL.md` | `current_governance_source` | truth-change and promotion law | promotion remains separate from this map |
| `managed/rules/QA_HYGIENE_PROTOCOL.md` | `current_governance_source` | hygiene findings, severity, routing, and closure | source-map defects route to QA/Hygiene |
| `managed/rules/PROJECT_INTERFACE_CONTRACT.md` | `current_governance_source` | project interface control law | project-control source claims route here |
| `managed/rules/AGENT_SWARM_INTERACTION_CANON.md` | `current_governance_source` | role, state, delegation, and handoff law | agent coordination claims route here or to process contracts |
| `managed/rituals/BOOTSTRAP.md` | `current_governance_source` | startup ritual | startup-source claims route here only when ritual behavior is affected |
| `managed/rituals/SESSION_EXPORT_PROTOCOL.md` | `current_governance_source` | session trace protocol | trace-source claims route here, not to accepted doctrine directly |
| `managed/rituals/NIGHT_PLANNING_PROTOCOL.md` | `current_governance_source` | cross-session synthesis protocol | night-source claims route here, not to accepted truth directly |
| `managed/rituals/HEARTBEAT.md` | `current_governance_source` | script-first maintenance ritual | continuity signals route onward; heartbeat is not source canon |
| `managed/rituals/CHECKLISTS.md` | `current_governance_source` | lightweight checklist surface | checklist evidence is subordinate to QA/Hygiene |
| `managed/knowledge/AGENT_KB_LANES.md` | `current_governance_source` | KB lane policy | companion governance surface for this file |
| `managed/knowledge/KB_PROMOTION_LEDGER_TEMPLATE.md` | `current_governance_source` | promotion candidate packaging template | use for promotion packets, not source mapping |
| `managed/knowledge/CROSS_REFERENCE_MANIFEST.md` | `current_governance_source` | durable references across surfaces | use for pointer resolution and durable cross-links |
| `managed/knowledge/OVERLAP_VALIDATION_MATRIX.md` | `current_governance_source` | overlap validation across roles and surfaces | use before routing contested material |
| `managed/processes/HOLDING_ORCHESTRATION_FLOW.md` | `current_governance_source` | orchestration process support | keep process evidence in process surface |
| `managed/processes/AGENT_HANDOFF_CONTRACTS.md` | `current_governance_source` | durable handoff contract minimums | handoff details belong here, not in this map |
| `managed/processes/DEEP_RESEARCH_TO_PATCHSPEC_WORKFLOW.md` | `current_governance_source` | research-to-patchspec workflow | use for manufacturing and patchspec process routing |

## Per-agent KB target mapping

Each first-wave agent has one KB root. Each root uses the same five-file scaffold.

| Agent ID | KB root | Accepted doctrine target | Candidate capture target | Default validator |
|---|---|---|---|---|
| `alfred` | `managed/agent_kb/alfred/` | `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md`, `TEMPLATES.md` | `LEARNING_QUEUE.md` | `meta_ops` |
| `meta_ops` | `managed/agent_kb/meta_ops/` | `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md`, `TEMPLATES.md` | `LEARNING_QUEUE.md` | `meta_detective` |
| `meta_strategy` | `managed/agent_kb/meta_strategy/` | `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md`, `TEMPLATES.md` | `LEARNING_QUEUE.md` | `meta_detective` |
| `meta_detective` | `managed/agent_kb/meta_detective/` | `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md`, `TEMPLATES.md` | `LEARNING_QUEUE.md` | `special_ops__hygiene_clean` |
| `special_ops__knowledge_bank` | `managed/agent_kb/special_ops__knowledge_bank/` | `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md`, `TEMPLATES.md` | `LEARNING_QUEUE.md` | `special_ops__informatics_design` |
| `special_ops__informatics_design` | `managed/agent_kb/special_ops__informatics_design/` | `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md`, `TEMPLATES.md` | `LEARNING_QUEUE.md` | `special_ops__hygiene_clean` |
| `special_ops__prompts_workflows` | `managed/agent_kb/special_ops__prompts_workflows/` | `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md`, `TEMPLATES.md` | `LEARNING_QUEUE.md` | `meta_ops` |
| `special_ops__ai_handling_routing` | `managed/agent_kb/special_ops__ai_handling_routing/` | `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md`, `TEMPLATES.md` | `LEARNING_QUEUE.md` | `meta_ops` |
| `special_ops__hygiene_clean` | `managed/agent_kb/special_ops__hygiene_clean/` | `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md`, `TEMPLATES.md` | `LEARNING_QUEUE.md` | `meta_detective` |

## Evidence-only staging and source boundary

Evidence-only staging sources include:

- research reports
- pre-lock packs
- source ledgers
- continuation artifacts
- analysis files
- prompt-flow drafts
- old source maps
- staging folders
- source folders outside the final runtime boundary

Rules:

- **Rule:** Evidence-only staging sources may seed a candidate, a rewrite rationale, or a routing decision.
- **Rule:** Evidence-only staging sources may not become runtime truth by being cited or summarized.
- **Rule:** Evidence-only staging sources are not patched as runtime output.
- **Rule:** Lock files may be architecture authority inputs, but they still remain source inputs rather than runtime patch targets.
- **Rule:** Source paths may be preserved as source references without normalizing them into final-system paths unless a governed final-system target exists.
- **Rule:** If a staging source contradicts a binding lock source or final-system surface, route the contradiction through validation instead of silently choosing the more convenient source.

## Source-to-target routing rules

### Compact activation claims

Route compact activation, role entry, startup pointers, and seed-level boundaries to:

- `managed/agents/<agent_id>.md`
- `managed/agents/AGENT_INDEX.md`

Do not route long doctrine or practice detail into seed files.

### Per-agent rich doctrine

Route accepted role doctrine, repeated practices, known mistakes, and reusable templates to:

- `managed/agent_kb/<agent_id>/ESSENCE.md`
- `managed/agent_kb/<agent_id>/BEST_PRACTICES.md`
- `managed/agent_kb/<agent_id>/MISTAKES.md`
- `managed/agent_kb/<agent_id>/TEMPLATES.md`

Do not route unvalidated source claims directly into accepted KB files.

### Candidate learning

Route unvalidated but useful candidate material to:

- `managed/agent_kb/<agent_id>/LEARNING_QUEUE.md`

`LEARNING_QUEUE.md` entries are candidate-only. They are not runtime truth, not accepted doctrine, and not proof of promotion.

### Shared KB governance

Route cross-agent KB placement, source-class rules, promotion packaging, overlap validation, durable reference mapping, and KB lane policy to:

- `managed/knowledge/AGENT_KB_LANES.md`
- `managed/knowledge/KB_STARTING_SOURCE_MAP.md`
- `managed/knowledge/KB_PROMOTION_LEDGER_TEMPLATE.md`
- `managed/knowledge/CROSS_REFERENCE_MANIFEST.md`
- `managed/knowledge/OVERLAP_VALIDATION_MATRIX.md`

Do not place per-agent rich doctrine in shared governance files.

### Process contracts and handoffs

Route orchestration process, handoff schema, and research-to-patchspec workflow claims to:

- `managed/processes/HOLDING_ORCHESTRATION_FLOW.md`
- `managed/processes/AGENT_HANDOFF_CONTRACTS.md`
- `managed/processes/DEEP_RESEARCH_TO_PATCHSPEC_WORKFLOW.md`

Do not embed full handoff schemas in this source map.

### Managed law and ritual claims

Route operating law, escalation law, promotion law, hygiene law, project-interface law, role/state law, startup ritual, session trace, night planning, heartbeat, and checklists to their existing managed rule or ritual files.

Do not duplicate managed law inside this file.

### Runtime config claims

Route runtime configuration questions to operator review for:

- `managed/config/openclaw.json`

Do not write config doctrine or schema changes into this source map.

## Anti-canonization safeguards

- **Source is not canon:** a source can support a candidate without becoming accepted truth.
- **Candidate is not canon:** a candidate in `LEARNING_QUEUE.md` is not runtime truth.
- **Map is not promotion:** this file guides routing and provenance; it does not approve content.
- **Validation is required:** promotion still requires the normal validation path and the assigned validator.
- **No self-promotion:** the source writer, KB owner, or drafting agent may not promote its own candidate without validation.
- **No source/staging patches:** source and staging folders remain evidence-only unless separately reclassified by a governed final-system decision.
- **No config mutation:** `openclaw.json` remains outside this file's change scope.
- **No doctrine dumping:** raw research, long source excerpts, and full lock contents stay out of shared governance files.
- **No path laundering:** do not make a staging path appear final merely by copying the string into a final-system file.
- **No silent conflict resolution:** unresolved conflicts require validator review, hygiene finding, promotion packet, escalation, or operator decision.

## Acceptance criteria

This file is valid when all checks pass:

| Check | Pass condition |
|---|---|
| final role preserved | file remains a durable starting-source map for seeding and auditing KB knowledge |
| source classes present | source classes distinguish final-system, lock, seed, governance/process, KB target, staging, and operator-decision sources |
| authority order explicit | conflicts can be resolved without guessing or averaging |
| final-system surfaces mapped | seeds, KB roots, shared governance, rules, rituals, processes, docs, user surfaces, and config boundaries are visible |
| binding lock sources bounded | lock files guide decisions but are not runtime patch targets |
| current seed sources mapped | all nine first-wave agents have current seed paths |
| governance/process sources mapped | managed rules, rituals, knowledge, and process surfaces are routed without duplicating their schemas |
| per-agent KB targets mapped | all nine first-wave KB roots are present with the five-file scaffold boundary |
| learning queue boundary preserved | `LEARNING_QUEUE.md` is candidate-only and never runtime truth |
| source/staging boundary preserved | staging and source material remain evidence-only |
| source-to-target routing clear | source material can be routed to the correct final-system surface |
| anti-canonization safeguards present | source, candidate, canon, validation, and promotion remain separate |
| config changes excluded | no `openclaw.json` changes are proposed |
| no rich doctrine dump | shared governance does not absorb per-agent rich doctrine |
| no handoff schema dump | process contract schemas remain outside this source map |
