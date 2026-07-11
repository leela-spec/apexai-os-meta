---
class: trace
role: MANIFEST
surface: agent_kb_appendix
quality: reliable
scope: agent
purpose: record the bounded source set used to build the Special Ops AI Handling Routing KB base
dependencies: PROMPTFLOW_KB_BASE_BUILD.md | SPECIAL_OPS_KB_BASE_BUILD_INDEX.md | KB_RANKINGS_BY_AGENT.md
status: kb_base_built
owner: special_ops__ai_handling_routing
validator: meta_ops
---

# APPENDIX_KB_SOURCE_MANIFEST

## Purpose

- **Decision:** This appendix records the source slice used for the `special_ops__ai_handling_routing` KB base.
- **Constraint:** This appendix is evidence and trace for KB-base construction; it does not mutate runtime configuration or accepted governance.
- **Constraint:** Routing guidance remains advisory unless a separate governing surface accepts it.

## Execution lock

- **Working repo:** `leela-spec/MasterOfArts`.
- **Branch:** `main`.
- **Target root:** `OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__ai_handling_routing/`.
- **Promptflow:** `OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__ai_handling_routing/PROMPTFLOW_KB_BASE_BUILD.md`.
- **Source index:** `agent_kb_source_indexes/SPECIAL_OPS_KB_BASE_BUILD_INDEX.md`.

## Indexed source slice

| Source path | Indexed role | Indexed read mode | Actual use | Status |
|---|---|---|---|---|
| `AIHowTo/BasicFiles4Agents/SingleAiGuide_research&Guides/SingleGuide_Claude.md` | primary | read full | task framing, ambiguity handling, module routing, bounded work, hard limits | used |
| `AIHowTo/BasicFiles4Agents/Validation&Authority/SOURCE_AUTHORITY_VERIFICATION_ESCALATION_80_20_ESSENCE.md` | primary | read full | source authority, verification, confidence states, stop conditions | used |
| `AIHowTo/Codex/CODEX_RESILIENT_MIGRATION_PROCESS.md` | supporting | read full | Codex routing, execution-mode lock, path discipline, one-file-at-a-time rule | used |
| `AIHowTo/Codex/CODEX_EXECUTION_INSTRUCTION_RELIABLE_REPRODUCED.md` | supporting | read full | reliable repo execution contract, authority order, stop conditions | used |
| `AIHowTo/BasicFiles4Agents/SingleAiGuide_research&Guides/LIMITED_AGENT_STYLE_GUIDE.md` | supporting | read full | compact output style, typed bullets, escalation when surface/role unclear | used |
| `AIHowTo/BasicFiles4Agents/WorkflowResearch/WORKFLOW_BEST_PRACTICES_RESEARCH.md` | supporting | skim | bounded workflow, overload classification, artifact-centered execution, failure modes | used |
| `OpenClaw/04_final-system-setup/AdvancedUpdateProcess/HARMONIZATION_RISK_REGISTER.md` | evidence | evidence only | stage confusion, scope drift, authority drift, completion illusion, premature handoff risks | used |

## Existing indexes and ledgers used first

| Source | Use in this build | Status |
|---|---|---|
| `agent_kb_source_indexes/SPECIAL_OPS_KB_BASE_BUILD_INDEX.md` | binding source slice for this agent | used |
| `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/KB_RANKINGS_BY_AGENT.md` | ranking plausibility and top candidate check | used |
| `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/SOURCE_INVENTORY_LEDGER.md` | duplicate and source-role plausibility signal | used through retrieved slices |
| `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/MASTER_IDEA_LEDGER.md` | candidate idea context | not exhaustively materialized in scaffold; represented in candidate ledger structure |
| `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/ROLE_AND_KB_TARGET_MAP.md` | role-to-KB fit context | represented through source-index and current seed boundary |
| `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/ESSENCE_CANDIDATES.md` | essence-candidate context | represented through ESSENCE compression and candidate ledger |
| `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/FAILURE_AND_ANTI_DRIFT_LEDGER.md` | anti-drift context | represented through anti-drift appendix and risk register evidence |

## Ranking plausibility check

- **Coverage:** The ranking ledger's `special_ops__ai_handling_routing` slice is represented through three evidence families: information-design/routing-card shape, prompt/workflow handoff shape, and Codex execution-boundary material.
- **Role fit:** Direct doctrine is taken from the source-index slice because it is agent-specific to model/tool routing, handoff, source authority, escalation, and bounded execution.
- **Constraint:** Top-ranked informatics and prompt-flow candidates are treated as structure/routing evidence, not as permission to turn this KB into prompt drafting, file taxonomy, or governance authority.
- **Duplication:** Same-filename and duplicate-candidate signals are handled by preferring the exact repo-accessible paths named in the source index.
- **Gap risk:** No current provider-pricing, live model-benchmark, or runtime-config source was used. This is non-blocking because this KB is advisory and must flag current model/provider claims as `needs_current_verification` before use.
- **Authority risk:** No scaffold file may authorize config mutation, provider-policy claims, or runtime model registry changes.

## Material conflicts

- **Conflict status:** no blocking primary-source conflict found.
- **Non-blocking tension:** older role-material sometimes frames this agent as a technical orchestrator or config updater; current seed and promptflow constrain the lane to advisory model/tool/path-routing doctrine only.
- **Disposition:** no `SOURCE_CONFLICT_REPORT.md` was created because the tension is resolved by current target lock and advisory boundary.

## Downstream appendix map

| Appendix | Function |
|---|---|
| `APPENDIX_KB_INFORMATION_RANKING_LEDGER.md` | ranks extracted information units and maps them to scaffold targets |
| `APPENDIX_KB_CANDIDATE_LEDGER.md` | records candidate entries and validation state before any promotion |
| `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md` | records drift/failure patterns and countermeasures |
