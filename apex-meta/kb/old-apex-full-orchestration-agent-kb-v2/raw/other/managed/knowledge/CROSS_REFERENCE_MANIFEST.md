# CROSS_REFERENCE_MANIFEST

## Purpose

This file records the durable cross-reference graph for the first-wave holding-orchestration infrastructure.

## Core references

| Source file | Points to | Why |
|---|---|---|
| `managed/rules/AGENTS.base.md` | `managed/agents/AGENT_INDEX.md` | compact startup pointer |
| `managed/agents/AGENT_INDEX.md` | all agent seed files | named-seed entrypoint |
| `managed/agents/AGENT_INDEX.md` | `managed/processes/HOLDING_ORCHESTRATION_FLOW.md` | routing and activation flow |
| `managed/agents/AGENT_INDEX.md` | `managed/processes/AGENT_HANDOFF_CONTRACTS.md` | handoff schema |
| `managed/agents/AGENT_INDEX.md` | `managed/knowledge/OVERLAP_VALIDATION_MATRIX.md` | overlap validation |
| `managed/agents/AGENT_INDEX.md` | `managed/agent_kb/AGENT_KB_INDEX.md` | KB-root index pointer |
| `managed/agent_kb/AGENT_KB_INDEX.md` | first-wave KB roots | durable KB-root map |
| `managed/knowledge/AGENT_KB_LANES.md` | `managed/agent_kb/AGENT_KB_INDEX.md` | lane-to-root boundary |
| `managed/agents/special_ops__knowledge_bank.md` | `managed/knowledge/KB_STARTING_SOURCE_MAP.md` | source seeding |
| `managed/agents/special_ops__knowledge_bank.md` | `managed/knowledge/KB_PROMOTION_LEDGER_TEMPLATE.md` | candidate logging |
| `managed/agents/special_ops__informatics_design.md` | `managed/knowledge/AGENT_KB_LANES.md` | lane boundaries |
| `managed/processes/HOLDING_ORCHESTRATION_FLOW.md` | all relevant seed agents | orchestration entry |
| `managed/processes/AGENT_HANDOFF_CONTRACTS.md` | seed agents and overlap matrix | durable handoff behavior |
| `managed/processes/DEEP_RESEARCH_TO_PATCHSPEC_WORKFLOW.md` | KB source map, ledger template, handoff contracts | implementation workflow |
| `managed/knowledge/KB_STARTING_SOURCE_MAP.md` | first-wave KB roots | source-to-KB seeding route |
| `managed/knowledge/KB_PROMOTION_LEDGER_TEMPLATE.md` | per-agent `LEARNING_QUEUE.md` files | candidate promotion packaging |
| `managed/knowledge/OVERLAP_VALIDATION_MATRIX.md` | seed agents, KB roots, and handoff contracts | boundary validation |
| `docs/ROLE_SYSTEM.md` | `managed/agents/AGENT_INDEX.md` | companion-to-managed named map |
| `docs/PROJECT_ROUTING.md` | `managed/processes/HOLDING_ORCHESTRATION_FLOW.md` | scenario routing guide |
| `docs/LEARNING_SYSTEM.md` | `managed/knowledge/KB_PROMOTION_LEDGER_TEMPLATE.md` | learning-to-candidate pointer |
| `agent_kb_source_indexes/META_HEADS_KB_BASE_BUILD_INDEX.md` | `managed/agent_kb/meta_strategy/` and `managed/agent_kb/meta_detective/` | source index for meta-head KB build/review work |
| `managed/agent_kb/meta_detective/APPENDIX_INTERNAL_MODES.md` | `managed/agent_kb/meta_detective/ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md`, `TEMPLATES.md`, `LEARNING_QUEUE.md` | accepted appendix doctrine for Meta Detective internal validation modes |

## Meta Detective internal-mode working references

| Source file | Points to | Why |
|---|---|---|
| `docs/working/META_DETECTIVE_ORIENTATION_WORKING.md` | five Meta Detective mode working files | working registry for non-agent Detective modes |
| `docs/working/META_DETECTIVE_EVIDENCE_SOURCE_VERIFIER_WORKING.md` | `managed/agent_kb/meta_detective/APPENDIX_INTERNAL_MODES.md`, `BEST_PRACTICES.md`, `TEMPLATES.md`, `MISTAKES.md` | source/trace detail for evidence/source validation mode |
| `docs/working/META_DETECTIVE_CONTRADICTION_LOGIC_AUDITOR_WORKING.md` | `managed/agent_kb/meta_detective/APPENDIX_INTERNAL_MODES.md`, `BEST_PRACTICES.md`, `TEMPLATES.md`, `MISTAKES.md` | source/trace detail for contradiction and logic audit mode |
| `docs/working/META_DETECTIVE_BOUNDARY_AUTHORITY_GUARDIAN_WORKING.md` | `managed/agent_kb/meta_detective/APPENDIX_INTERNAL_MODES.md`, `managed/knowledge/OVERLAP_VALIDATION_MATRIX.md`, `managed/agent_kb/meta_detective/` | source/trace detail for role, authority, config, and promotion boundary checks |
| `docs/working/META_DETECTIVE_RISK_FAILURE_RED_TEAMER_WORKING.md` | `managed/agent_kb/meta_detective/APPENDIX_INTERNAL_MODES.md`, `TEMPLATES.md`, `LEARNING_QUEUE.md` | source/trace detail for failure-mode and red-team pressure |
| `docs/working/META_DETECTIVE_VERDICT_ESCALATION_SYNTHESIZER_WORKING.md` | `managed/agent_kb/meta_detective/APPENDIX_INTERNAL_MODES.md`, `TEMPLATES.md` | source/trace detail for final validation verdict packets |
| `docs/working/META_DETECTIVE_HYGIENE_VALIDATION_REPORT.md` | `managed/agent_kb/meta_detective/APPENDIX_INTERNAL_MODES.md` | structural validation trace for promoted internal mode appendix |
| `managed/agent_kb/meta_detective/LEARNING_QUEUE.md` | `managed/agent_kb/meta_detective/APPENDIX_INTERNAL_MODES.md` and future candidate entries | promoted pack trace plus future candidate capture |

## First-wave seed-to-KB references

| Seed file | KB root | Why |
|---|---|---|
| `managed/agents/alfred.md` | `managed/agent_kb/alfred/` | operator-facing intake boundary depth |
| `managed/agents/meta_ops.md` | `managed/agent_kb/meta_ops/` | orchestration boundary depth |
| `managed/agents/meta_strategy.md` | `managed/agent_kb/meta_strategy/` | options and recommendation boundary depth |
| `managed/agents/meta_detective.md` | `managed/agent_kb/meta_detective/` | adversarial-validation boundary depth |
| `managed/agents/special_ops__knowledge_bank.md` | `managed/agent_kb/special_ops__knowledge_bank/` | KB placement and lifecycle depth |
| `managed/agents/special_ops__informatics_design.md` | `managed/agent_kb/special_ops__informatics_design/` | structure and taxonomy depth |
| `managed/agents/special_ops__prompts_workflows.md` | `managed/agent_kb/special_ops__prompts_workflows/` | reusable prompt/workflow depth |
| `managed/agents/special_ops__ai_handling_routing.md` | `managed/agent_kb/special_ops__ai_handling_routing/` | advisory model/tool routing depth |
| `managed/agents/special_ops__hygiene_clean.md` | `managed/agent_kb/special_ops__hygiene_clean/` | structural QA and hygiene depth |

## KB scaffold references

Each first-wave KB root resolves to the same five-file scaffold:

- `ESSENCE.md`
- `BEST_PRACTICES.md`
- `MISTAKES.md`
- `TEMPLATES.md`
- `LEARNING_QUEUE.md`

`LEARNING_QUEUE.md` files are candidate-only and are not runtime truth.

## Boundary references

- All managed files in this manifest stay within `managed/`, `docs/`, `user/`, and `README-OpenClaw.md`.
- No runtime cross-reference should target `NewFinals/`, `BaselinePatches/`, or `AdvancedUpdateProcess/` as authority.
- `docs/working/` files are working surfaces and not accepted canon by storage alone.

## Maintenance rule

Whenever a new managed seed, lane file, process file, or durable working surface becomes a normal routing dependency, add it here before treating it as a normal routing dependency.
