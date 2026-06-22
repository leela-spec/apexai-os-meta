---
class: appendix
role: EXTERNAL_CLAIM_VERIFICATION
surface: agent_kb_appendix
quality: proposed
scope: agent
purpose: create a future-research verification ledger for external model and platform behavior claims
status: created
created_at: 2026-05-06
owner: special_ops__prompts_workflows
validator: meta_ops
task_id: TASK-06
target_agent: special_ops__prompts_workflows
target_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/
source_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/
source_refs:
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/PROMPTFLOW_CONSTANT_FRAME_CONTROLLED_KB_INTEGRATION.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_CONSTANT_FAILURE_INTEGRATION_PROCESS.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_CONSTANT_FAILURE_SOURCE_NOTES.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_RUNTIME_TEMPLATE_CATALOG.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/ConstantAIFailureAnalysis.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/00_SYSTEM_BOOTSTRAP.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/01_API_CALL_STRUCTURE.md
---

# APPENDIX_KB_EXTERNAL_CLAIM_VERIFICATION

## 1. Purpose

This appendix is a future-research verification ledger for external model, platform, runtime, browser, API, and provider-behavior claims found in the constant-failure source pack.

It does not verify external claims. It inventories them, assigns verification status, routes them to the correct future or adjacent lane, and defines what evidence would be required before any claim can influence accepted `special_ops__prompts_workflows` doctrine.

This file is appendix-only. It does not mutate `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md`, `TEMPLATES.md`, or `LEARNING_QUEUE.md`.

## 2. TASK-06 gate record

```yaml
GATE_CHECK:
  task_id: TASK-06
  task_type_understood: appendix_create
  scope_understood: Create a future-research verification ledger for external model and platform behavior claims.
  target_file: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_EXTERNAL_CLAIM_VERIFICATION.md
  ambiguity_detected: false
  ready_to_execute: true
```

## 3. Scope lock

```yaml
scope_lock:
  working_repo: leela-spec/MasterOfArts
  target_repo: leela-spec/MasterOfArts
  target_branch: main
  target_agent: special_ops__prompts_workflows
  target_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/
  artifact_type: appendix_create
  scope: Create a future-research verification ledger for external model and platform behavior claims.
  allowed_write:
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_EXTERNAL_CLAIM_VERIFICATION.md
  forbidden_writes:
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/ESSENCE.md
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/BEST_PRACTICES.md
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/MISTAKES.md
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/TEMPLATES.md
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/LEARNING_QUEUE.md
```

## 4. Source and route-status ledger

| Source | Used for | Route status | Evidence status in this appendix | Boundary |
|---|---|---|---|---|
| `PROMPTFLOW_CONSTANT_FRAME_CONTROLLED_KB_INTEGRATION.md` | TASK-06 target, task order, promotion gates, fetch-back requirement, external-claim prohibition. | `accepted_for_frame_control` | `verified_with_source` for local route control only | Controls this appendix; does not verify external claims. |
| `appendices/APPENDIX_KB_CONSTANT_FAILURE_INTEGRATION_PROCESS.md` | Non-promotion warning, ranking of external claims as future research, task dependency map. | `accepted_for_route_control` | `verified_with_source` for local route control only | Confirms external claims must not be promoted as accepted truth. |
| `appendices/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md` | Accepted execution controls and adjacent-lane/runtime caution. | `accepted_for_execution_boundary` | `verified_with_source` for local execution-control boundary only | Source-local controls may support scaffold later; runtime claims remain adjacent/future. |
| `appendices/APPENDIX_KB_CONSTANT_FAILURE_SOURCE_NOTES.md` | Source inventory, route statuses, duplicate handling, external-claim caution. | `accepted_for_source_route_status` | `verified_with_source` for local source-routing only | Provides source map; does not validate external truth. |
| `appendices/APPENDIX_KB_RUNTIME_TEMPLATE_CATALOG.md` | Generated/hand-authored template reconciliation and runtime-template boundaries. | `accepted_for_template_boundary` | `verified_with_source` for local catalog boundary only | Keeps scaffold template recommendations candidate-only. |
| `NewResearchBecauseOfConstantFailure/ConstantAIFailureAnalysis.md` | External model/platform/browser/API claims and failure-cause hypotheses. | `future_research_source_leads` | `unverified` | Treat as claim inventory and problem framing only. External links embedded in the source are not accepted as evidence here. |
| `NewResearchBecauseOfConstantFailure/00_SYSTEM_BOOTSTRAP.md` | Runtime, model pinning, generation-parameter, and execution-control assertions. | `split: source_local_execution_control + adjacent_lane_runtime_claims` | `verified_with_source` for local text presence; external/runtime truth remains unverified | Use local execution controls only; route model/runtime fields to adjacent lane or future tests. |
| `NewResearchBecauseOfConstantFailure/01_API_CALL_STRUCTURE.md` | API payload, stateless call structure, response-format and max-token assertions. | `split: source_local_execution_control + runtime_implementation_claims` | `verified_with_source` for local text presence; API capability truth remains unverified | Use as runtime research input, not accepted platform law. |

## 5. External-claim handling rule

```yaml
external_claim_handling_rule:
  default_for_external_model_platform_claims: unverified
  default_for_claims_with_external_links_but_no_primary_current_fetch: needs_primary_source
  default_for_browser_or_platform_current_behavior_claims: needs_current_web_check
  default_for_api_or_runtime_capability_claims: needs_runtime_test
  default_for_cross_lane_ownership_claims: adjacent_lane_owner
  source_local_execution_controls:
    allowed_status: verified_with_source
    limitation: verified only as source-local prompt/workflow controls, not as external platform truth
  accepted_doctrine_from_TASK_06: none
  scaffold_recommendations_from_TASK_06: candidate_only
  forbidden:
    - promote unverified model/platform claims as accepted doctrine
    - treat ConstantAIFailureAnalysis.md as verified truth
    - harden runtime/API/model implementation claims inside prompts/workflows without adjacent-lane validation
    - use external blog/community/forum claims as accepted evidence without primary/current verification
```

## 6. Verification-status legend

The only allowed `verification_status` values in this appendix are the following.

| verification_status | Meaning | Allowed current handling |
|---|---|---|
| `unverified` | Claim is present in a source but has not been checked against a current primary source, current web source, or runtime test. | Inventory only; no doctrine promotion. |
| `needs_primary_source` | Claim references provider, model, or platform behavior and needs an official or primary-source confirmation. | Future research queue. |
| `needs_current_web_check` | Claim could change over time and needs a current web check before use. | Future research queue. |
| `needs_runtime_test` | Claim requires direct implementation, API, browser, or tool behavior testing in the active runtime. | Runtime-test candidate only. |
| `adjacent_lane_owner` | Claim belongs to AI handling/routing, platform runtime, server architecture, Knowledge Bank, MetaOps, or another lane. | Route to adjacent owner; do not resolve here. |
| `rejected_for_now` | Claim is too broad, contradictory, missing evidence, or unsafe for promotion in this lane. | Do not promote; revisit only with stronger evidence. |
| `verified_with_source` | Claim is verified only as present in a fetched local source or appendix. For external claims, this status requires cited primary/current evidence, which TASK-06 did not fetch. | Source-local execution controls only in this appendix. |

## 7. Claim inventory table

| claim_id | claim_summary | source_file | claim_type | verification_status | required_evidence | allowed_current_use | forbidden_current_use | candidate_destination | notes |
|---|---|---|---|---|---|---|---|---|---|
| `ECV-001` | GPT model aliases, auto-switching, silent downgrade, or fallback behavior can change model family, context size, or instruction compliance mid-session. | `ConstantAIFailureAnalysis.md`; `00_SYSTEM_BOOTSTRAP.md` | `external_model_platform` | `needs_primary_source` | Current official provider documentation or first-party incident/runtime disclosure; optional controlled model-identity logs. | Future-research lead; warning label only. | Accepted scaffold doctrine; hard requirement to pin a named model in this lane as universal law. | AI Handling/Routing; `LEARNING_QUEUE.md` candidate | Includes alias, auto-routing, downgrade, and load-based fallback claims. |
| `ECV-002` | GPT-4.1, GPT-5, GPT-5.5, or other model families have specific instruction-following degradation or drift characteristics. | `ConstantAIFailureAnalysis.md` | `external_model_platform` | `needs_primary_source` | Current benchmark, provider release notes, reproducible internal evals, or primary research source. | Future-research question; regression-test hypothesis. | Ranking model families in accepted prompt/workflow doctrine without evidence. | AI Handling/Routing; evaluation lane | Treat community/forum claims as leads only. |
| `ECV-003` | Post-training alignment, RLHF, moderation layers, or soft prompt steering cause degraded literal-task compliance. | `ConstantAIFailureAnalysis.md` | `external_model_platform` | `needs_primary_source` | Primary provider explanation, peer-reviewed research, or reproducible eval isolating cause. | Hypothesis for research framing only. | Stating causal mechanism as fact in scaffold. | External-claim research queue | Causal claims require stronger evidence than observed failures. |
| `ECV-004` | Long-session instruction drift grows predictably or exponentially, causing loss of early constraints over many steps. | `ConstantAIFailureAnalysis.md` | `external_model_platform` | `needs_primary_source` | Primary research or internal eval measuring stepwise error compounding for relevant agent tasks. | Use as motivation for atomic-task regression tests only. | Accepted mathematical/empirical law in scaffold. | Regression/evaluation lane; `LEARNING_QUEUE.md` candidate | Source-local response can still use atomic-task control without accepting this causal claim. |
| `ECV-005` | Browser or ChatGPT app output limits cause large file generation to collapse into code blocks, summaries, or incomplete artifacts. | `ConstantAIFailureAnalysis.md`; `05_SPLIT_SIGNAL.md` referenced by appendices | `external_model_platform` | `needs_current_web_check` | Current product documentation and controlled browser tests for output behavior. | Candidate reason for split discipline; runtime-test lead. | Fixed numeric token/output limits as accepted doctrine. | Browser workflow research; runtime test table | Split discipline is safe as source-local control; numeric limits are not. |
| `ECV-006` | API mode supports materially different output-token ceilings or file-generation reliability than browser mode. | `ConstantAIFailureAnalysis.md`; `01_API_CALL_STRUCTURE.md` | `runtime_implementation` | `needs_primary_source` | Current official API model limits, SDK/docs, and runtime tests. | Future research; adjacent-lane implementation question. | Accepted advice to switch to API or specific output budgets as doctrine. | AI Handling/Routing; runtime implementation | Current limits change and must be checked at use time. |
| `ECV-007` | API payloads should enforce `response_format: {type: json_object}` for all structured calls except raw file writes. | `01_API_CALL_STRUCTURE.md` | `runtime_implementation` | `needs_runtime_test` | Runtime contract validation against actual provider API, including failure modes and exceptions. | Candidate runtime template; source-local pattern. | Accepted platform capability or universal requirement. | AI Handling/Routing; runtime template catalog | Belongs partly outside prompts/workflows. |
| `ECV-008` | Streaming should be disabled for structured output integrity. | `00_SYSTEM_BOOTSTRAP.md`; `01_API_CALL_STRUCTURE.md` | `runtime_implementation` | `needs_runtime_test` | Controlled streaming vs non-streaming structured-output tests in target runtime. | Runtime-test candidate only. | Accepted scaffold doctrine that streaming is always unsafe. | AI Handling/Routing; runtime tests | Could become environment-specific guidance after test. |
| `ECV-009` | Temperature should be set to `0.0` for deterministic execution tasks. | `00_SYSTEM_BOOTSTRAP.md`; `01_API_CALL_STRUCTURE.md` | `runtime_implementation` | `needs_runtime_test` | Runtime eval comparing deterministic settings for task closure, diff validity, and schema adherence. | Candidate runtime control. | Universal prompt/workflow law without runtime evidence. | AI Handling/Routing; evaluation lane | May be sensible but still requires owner validation. |
| `ECV-010` | `max_tokens` budgets by task type are appropriate: file write 4096, diff patch 2048, state update 512, research block 8192, gate check 256, clarify 128. | `01_API_CALL_STRUCTURE.md` | `runtime_implementation` | `needs_runtime_test` | Empirical output-size distribution and provider-limit check for each task class. | Runtime-test candidate. | Accepted scaffold numeric budgets. | Runtime implementation; `LEARNING_QUEUE.md` candidate | Numeric ceilings are runtime-sensitive. |
| `ECV-011` | Server-side, Hetzner cloud, API-native execution is the correct architecture for OpenClaw agent tasks. | `00_SYSTEM_BOOTSTRAP.md` | `runtime_implementation` | `adjacent_lane_owner` | Architecture owner decision, deployment design, runtime security review. | Adjacent-lane routing only. | Prompts/workflows doctrine requiring a specific server provider or deployment model. | Platform/runtime architecture lane | Outside TASK-06 and outside this KB lane. |
| `ECV-012` | Each API call should be stateless, with no conversation history injected and state passed only through `STATE_BLOCK`. | `01_API_CALL_STRUCTURE.md`; `02_STATE_BLOCK.md` via appendices | `source_local_execution_control` | `verified_with_source` | Local source and controlling appendices are sufficient for prompt/workflow control; runtime implementation still needs tests. | Accepted source-local execution control; later compact scaffold candidate. | Claiming all provider APIs are stateless or must ignore history by platform law. | `TEMPLATES.md` candidate; execution-control appendix | Safe when framed as a prompt/workflow control, not external behavior. |
| `ECV-013` | Persistent state should exist outside chat history and be read as explicit state, not reconstructed from prior conversation. | `APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md`; `APPENDIX_KB_CONSTANT_FAILURE_SOURCE_NOTES.md` | `source_local_execution_control` | `verified_with_source` | Local source appendix and state-block source are sufficient for source-local control. Persistent storage implementation requires owner decision. | Accepted source-local control; candidate scaffold pointer. | Mandating a specific persistent state-store implementation. | `TEMPLATES.md`; Knowledge Bank / MetaOps if implemented | Separates prompt/workflow principle from implementation. |
| `ECV-014` | `ConstantAIFailureAnalysis.md` identifies five verified causes of failures, including alignment degradation, downgrades, long-session drift, model-family degradation, and app/file boundary failure. | `ConstantAIFailureAnalysis.md` | `future_research` | `unverified` | Claim-by-claim primary-source review and reproducible task evidence. | Research-lead inventory only. | Treating the “verified causes” label as accepted truth. | This appendix; future research queue | The word “verified” in the source is not accepted by this appendix. |
| `ECV-015` | Business/browser ChatGPT Projects, memory, and custom instructions behave as persistent state/gate surfaces suitable for business workflows. | `ConstantAIFailureAnalysis.md` | `external_model_platform` | `needs_current_web_check` | Current official product documentation and browser tests. | Browser-workflow research lead. | Accepted browser-product doctrine in prompts/workflows scaffold. | Browser workflow research; user-facing ops | Product behavior changes over time. |
| `ECV-016` | Direct repo writing, diff application, or connector compliance may be misrepresented by agent tooling. | `ConstantAIFailureAnalysis.md`; patch appendices by route context | `runtime_implementation` | `needs_runtime_test` | Tool-specific audit: requested mode, actual connector operation, changed-file set, and fetch-back comparison. | Runtime-test candidate and validation pattern. | Claiming a specific connector is noncompliant without test evidence. | Hygiene / tooling / AI Handling | Fetch-back validation is safe; tool-behavior accusation is not. |
| `ECV-017` | Some claims belong to AI handling/routing rather than prompts/workflows: model selection, provider routing, runtime parameters, structured-output enforcement, streaming, max-token ceilings. | `APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md`; `APPENDIX_KB_CONSTANT_FAILURE_SOURCE_NOTES.md`; `APPENDIX_KB_RUNTIME_TEMPLATE_CATALOG.md` | `adjacent_lane` | `adjacent_lane_owner` | Adjacent-lane owner review and integration decision. | Route table and candidate handoff. | Solving or canonizing these claims inside this appendix. | AI Handling/Routing; runtime implementation | This appendix may identify owner but not resolve. |
| `ECV-018` | Source-local prompt/workflow controls are safe to use without external verification: explicit state, atomic task payload, gate check, HALT/CLARIFY, validated file output, closure proof, candidate-only scaffold boundaries. | `APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md`; `APPENDIX_KB_CONSTANT_FAILURE_SOURCE_NOTES.md`; `APPENDIX_KB_RUNTIME_TEMPLATE_CATALOG.md` | `source_local_execution_control` | `verified_with_source` | Local source files and appendices; future scaffold task must still stay compact and candidate-bounded. | Later scaffold candidate support. | Using this safe subset to smuggle external model/platform claims into doctrine. | `TEMPLATES.md`; `BEST_PRACTICES.md`; `MISTAKES.md` | Safe only because it does not depend on external model/platform truth. |

## 8. Claim-by-claim notes

### `ECV-001` model alias, auto-switch, and downgrade claims

`ConstantAIFailureAnalysis.md` asserts model auto-switching, dynamic downgrades, and context changes under load. These claims are platform behavior claims. They require current primary provider evidence or controlled runtime observation before any scaffold use.

- **Current status:** `needs_primary_source`
- **Allowed:** frame as a risk to verify.
- **Forbidden:** assert as accepted cause of failures.

### `ECV-002` model-family instruction-following claims

Claims about GPT-4.1, GPT-5, GPT-5.5, or any model family being harder to steer belong to model evaluation and routing. They may motivate regression tests, but they do not become accepted prompt/workflow doctrine from the source pack alone.

- **Current status:** `needs_primary_source`
- **Allowed:** route to eval queue.
- **Forbidden:** model ranking or steering advice as doctrine.

### `ECV-003` alignment/RLHF causal claims

The source attributes literal-task failure to post-training alignment, RLHF, moderation, and soft prompt steering. That is a causal model and needs stronger evidence than user observations or community reports.

- **Current status:** `needs_primary_source`
- **Allowed:** research hypothesis.
- **Forbidden:** root-cause assertion in `MISTAKES.md` or `BEST_PRACTICES.md`.

### `ECV-004` long-session drift claims

Long-horizon degradation is plausible as a failure pattern, but empirical rate, mathematical form, and exact cause remain unverified here. The source-local safe control is not the causal claim; it is the execution remedy: one atomic task, explicit state, and closure proof.

- **Current status:** `needs_primary_source`
- **Allowed:** regression-test design input.
- **Forbidden:** accepted quantitative law.

### `ECV-005` browser/chat output limitations

Browser output-collapse claims and numeric output ceilings are current product-behavior claims. They must be checked against current product behavior and controlled browser tests before use beyond candidate language.

- **Current status:** `needs_current_web_check`
- **Allowed:** reason to keep split protocol candidate.
- **Forbidden:** fixed output-token doctrine.

### `ECV-006` API capability and output-limit claims

API capability claims require current official documentation and runtime tests. The prompt/workflow lane can record desired contracts, but cannot guarantee API capabilities or model limits.

- **Current status:** `needs_primary_source`
- **Allowed:** adjacent-lane research task.
- **Forbidden:** accepted API limits in scaffold.

### `ECV-007` structured-output and response-format claims

`response_format` enforcement belongs to implementation. It may be a useful runtime template, but it requires direct API tests, exception handling, and owner validation.

- **Current status:** `needs_runtime_test`
- **Allowed:** runtime candidate.
- **Forbidden:** universal platform claim.

### `ECV-008` streaming claims

The source says `STREAM: false` for structured-output integrity. This is a runtime implementation recommendation, not a prompt/workflow doctrine rule.

- **Current status:** `needs_runtime_test`
- **Allowed:** test candidate.
- **Forbidden:** accepted anti-streaming rule.

### `ECV-009` temperature claims

Temperature `0.0` may be appropriate for deterministic execution, but the prompt/workflow lane should not harden it without evaluation and runtime owner acceptance.

- **Current status:** `needs_runtime_test`
- **Allowed:** eval candidate.
- **Forbidden:** global generation-parameter law.

### `ECV-010` max-token budget claims

The exact task-type token budgets in `01_API_CALL_STRUCTURE.md` are implementation hypotheses. They should be tested against actual artifact sizes and current provider limits.

- **Current status:** `needs_runtime_test`
- **Allowed:** runtime sizing experiment.
- **Forbidden:** fixed scaffold budget table.

### `ECV-011` server-side execution assumptions

Provider choice, server/cloud architecture, and API-native execution belong to runtime architecture owners. This appendix cannot select a deployment lane or cloud provider.

- **Current status:** `adjacent_lane_owner`
- **Allowed:** route to runtime owner.
- **Forbidden:** server-provider mandate.

### `ECV-012` stateless call structure

The source-local principle is safe: do not rely on hidden chat history for execution state. The implementation claim that every call is stateless and carries state only in the user message still belongs to runtime validation.

- **Current status:** `verified_with_source` for source-local control.
- **Allowed:** later compact template candidate.
- **Forbidden:** platform/API behavior claim.

### `ECV-013` persistent state-store assumptions

A persistent state surface is a safe prompt/workflow pattern when expressed as an explicit input contract. A concrete store, file path, memory system, or state-keeper service requires adjacent-lane design.

- **Current status:** `verified_with_source` for source-local control.
- **Allowed:** explicit-state doctrine candidate.
- **Forbidden:** storage implementation mandate.

### `ECV-014` promptflow failure-cause claims from `ConstantAIFailureAnalysis.md`

The source labels five causes as verified. This appendix explicitly does not inherit that verification. Each cause must be split into independently testable claims.

- **Current status:** `unverified`
- **Allowed:** claim inventory.
- **Forbidden:** accepting the source label “verified causes.”

### `ECV-015` browser/business account workflow claims

Claims about Projects, memory, custom instructions, and browser behavior require current product checks. They may later support user-facing operating practices, but not this appendix as doctrine.

- **Current status:** `needs_current_web_check`
- **Allowed:** future browser workflow research.
- **Forbidden:** accepted product-behavior guidance.

### `ECV-016` tool/connector compliance claims

Tool behavior must be audited per connector and per write mode. The safe source-local practice is fetch-back validation, not asserting a tool failed unless the changed-file evidence shows it.

- **Current status:** `needs_runtime_test`
- **Allowed:** validation pattern and test candidate.
- **Forbidden:** untested tool accusation.

### `ECV-017` adjacent-lane claims

Model routing, provider selection, API payload enforcement, streaming, token budgets, and server architecture belong to AI Handling/Routing or runtime implementation. This appendix may route, not decide.

- **Current status:** `adjacent_lane_owner`
- **Allowed:** adjacent-lane routing table.
- **Forbidden:** solving adjacent-lane implementation from prompts/workflows.

### `ECV-018` source-local controls safe for later scaffold candidates

Explicit state, atomic task payloads, gate checks, HALT/CLARIFY, verified writes, split discipline, and closure proof are source-local controls. They can support later compact scaffold entries only because they do not rely on external model/platform truth.

- **Current status:** `verified_with_source`
- **Allowed:** compact candidate for later scaffold tasks.
- **Forbidden:** using them to promote external claims by implication.

## 9. Verification plan by claim class

| Claim class | Includes | Required verification path | Default status until done | Owner route |
|---|---|---|---|---|
| Model alias / auto-switch / downgrade | Alias routing, fallback models, context-window changes, load-based switching. | Primary provider source plus runtime logs or UI/API evidence. | `needs_primary_source` | AI Handling/Routing |
| Model-family instruction following | Model-specific drift, steerability, compliance degradation. | Current evals, reproducible internal regression tests, primary model documentation. | `needs_primary_source` | Evaluation + AI Handling/Routing |
| Output-token / response-length | Browser and API output ceilings; large artifact collapse. | Current product/API documentation plus controlled output-size tests. | `needs_current_web_check` or `needs_runtime_test` | Runtime + browser workflow research |
| Browser/chat limitations | Projects, memory, custom instructions, file generation, code-block behavior. | Current product documentation plus browser test protocol. | `needs_current_web_check` | Browser workflow research |
| API capability | `response_format`, model limits, tool calling, file write behavior. | Official API documentation plus runtime tests. | `needs_primary_source` | AI Handling/Routing |
| Streaming / response-format / structured output | Stream false, JSON mode, schema adherence, raw file exceptions. | Controlled runtime tests across output modes. | `needs_runtime_test` | Runtime implementation |
| Temperature / generation parameters | Temperature zero, deterministic settings, task-specific budgets. | Eval on diff validity, file completeness, schema compliance. | `needs_runtime_test` | Evaluation + runtime implementation |
| Server-side execution assumptions | Hetzner/API-native execution, server ownership, toolchain. | Architecture review and owner decision. | `adjacent_lane_owner` | Runtime architecture |
| Persistent state-store assumptions | STATE_BLOCK, state keeper, memory/store, no chat-history inference. | Source-local prompt validation plus architecture owner decision for storage. | `verified_with_source` for prompt control; `adjacent_lane_owner` for storage | Prompts/workflows + MetaOps/Knowledge Bank |
| Promptflow failure-cause claims | Causes from `ConstantAIFailureAnalysis.md`. | Split into atomic claims, then primary/current/runtime verification. | `unverified` | Future research |
| AI handling/routing claims | Model pinning, route selection, fallbacks, provider-specific configuration. | Adjacent-lane design and runtime tests. | `adjacent_lane_owner` | AI Handling/Routing |
| Source-local controls | Atomic tasks, explicit state, gate, HALT/CLARIFY, fetch-back, closure proof. | Local source appendices and later scaffold promotion gate. | `verified_with_source` | Prompts/workflows |

## 10. Adjacent-lane routing table

| Routing ID | Claim area | Why outside this appendix | Adjacent owner candidate | Handoff artifact candidate | Current status |
|---|---|---|---|---|---|
| `ALR-001` | Model pinning, aliases, auto-switching, downgrade avoidance. | Requires provider/runtime routing authority. | `special_ops__ai_handling_routing` | `LEARNING_QUEUE.md` candidate; future AI-routing appendix | `adjacent_lane_owner` |
| `ALR-002` | API payload fields, JSON mode, structured outputs, tool behavior. | Requires implementation and current API documentation. | Runtime implementation + AI Handling/Routing | Runtime-test report | `adjacent_lane_owner` |
| `ALR-003` | Streaming and generation parameters. | Requires model/runtime evals. | Evaluation + runtime implementation | Parameter test matrix | `adjacent_lane_owner` |
| `ALR-004` | Server-side execution environment and cloud provider. | Deployment architecture decision. | Platform/runtime architecture | Architecture decision record | `adjacent_lane_owner` |
| `ALR-005` | Persistent state-store and state-keeper service. | Could imply new OpenClaw role or storage architecture. | MetaOps + Knowledge Bank + runtime implementation | State-keeper design note | `adjacent_lane_owner` |
| `ALR-006` | Connector/diff/file-write compliance. | Requires tool-specific audit. | Hygiene + tooling + runtime implementation | Tool compliance audit | `adjacent_lane_owner` |
| `ALR-007` | Browser Projects, memory, custom instructions, and business-account workflow. | Product behavior changes and needs current web/product check. | User-facing ops / browser workflow research | Browser workflow best-practice appendix | `adjacent_lane_owner` |

## 11. Runtime-test candidate table

| Test ID | Claim IDs | Test objective | Minimum procedure | Pass evidence | Candidate owner | Status |
|---|---|---|---|---|---|---|
| `RTT-001` | `ECV-007` | Verify structured-output behavior with `response_format`. | Run representative gate, file-output, and closure tasks with and without structured response settings. | Captured requests, responses, schema-validity report, error modes. | AI Handling/Routing | `needs_runtime_test` |
| `RTT-002` | `ECV-008` | Compare streaming vs non-streaming structured-output integrity. | Execute identical structured-output tasks in stream and non-stream modes. | Validity rate, truncation rate, partial-object evidence. | Runtime implementation | `needs_runtime_test` |
| `RTT-003` | `ECV-009` | Evaluate temperature effects on deterministic repo-task outputs. | Run repeated atomic tasks at `0.0` and comparison settings. | Diff validity, scope creep, schema adherence, completion stability. | Evaluation lane | `needs_runtime_test` |
| `RTT-004` | `ECV-010` | Validate task-type token budgets. | Generate representative artifacts for each task type and measure required output length. | Output distribution, truncation rate, recommended budget. | Runtime implementation | `needs_runtime_test` |
| `RTT-005` | `ECV-005`; `ECV-006` | Measure browser vs API artifact output behavior. | Produce comparable Markdown artifacts in browser and API contexts. | Completeness, formatting, truncation, code-block/file-write behavior. | Browser workflow + runtime | `needs_runtime_test` |
| `RTT-006` | `ECV-016` | Audit connector write-mode compliance. | Request diff/full-file/write-mode tasks, then compare actual changed-file set and commit diff. | Requested mode, actual mode, fetch-back proof, changed-file evidence. | Hygiene + tooling | `needs_runtime_test` |
| `RTT-007` | `ECV-001`; `ECV-002` | Detect model identity/routing drift where observable. | Capture model selection metadata where available across long and high-load tasks. | Metadata logs or documented absence of visibility. | AI Handling/Routing | `needs_runtime_test` |
| `RTT-008` | `ECV-012`; `ECV-013` | Validate explicit-state execution discipline. | Run controlled tasks with state block, stale state, missing state, and chat-history-only state. | HALT rate for bad state; correct execution for valid state. | Prompts/workflows + MetaOps | `needs_runtime_test` |

## 12. Future-research queue

| Research ID | Claim IDs | Research item | Priority | Required evidence | Candidate destination | Blocking condition |
|---|---|---|---|---|---|---|
| `ECV-RQ-001` | `ECV-001` | Verify whether model aliases, auto-switching, or downgrades occur in target environments and whether they affect context or instruction compliance. | P1 | Primary provider source and runtime observability. | `LEARNING_QUEUE.md` candidate; AI Handling/Routing handoff | No scaffold promotion until sourced. |
| `ECV-RQ-002` | `ECV-002`; `ECV-003`; `ECV-004` | Separate observed agent failures from causal claims about model family, post-training, and long-session drift. | P1 | Eval protocol, primary research, controlled regressions. | Future evaluation appendix | Causes remain unverified. |
| `ECV-RQ-003` | `ECV-005`; `ECV-015` | Current browser/business workflow behavior: Projects, memory, custom instructions, file output, and output truncation. | P1 | Current product documentation and browser tests. | Browser-workflow appendix candidate | Product behavior is time-sensitive. |
| `ECV-RQ-004` | `ECV-006`; `ECV-007`; `ECV-008`; `ECV-009`; `ECV-010` | API/runtime capability matrix for structured output, streaming, temperature, and token budgets. | P1 | Official API docs and runtime tests. | Runtime implementation handoff | API claims cannot enter scaffold as doctrine. |
| `ECV-RQ-005` | `ECV-011`; `ECV-013`; `ECV-017` | Determine owner and architecture for server-side execution and persistent state. | P1 | Architecture decision record and owner approval. | MetaOps / Knowledge Bank / runtime architecture | Prompt/workflow lane cannot decide deployment. |
| `ECV-RQ-006` | `ECV-016` | Build connector compliance audit for diff, full-file, and write-mode behavior. | P1 | Changed-file evidence and fetch-back comparison. | Hygiene/tooling appendix | Tool claims require test evidence. |
| `ECV-RQ-007` | `ECV-018` | Convert source-local controls into compact scaffold entries only after dependency appendices are complete. | P2 | Appendix support and compact patch task. | TASK-07 to TASK-11 | Candidate-only until scaffold task executes. |

## 13. Forbidden-promotion list

The following are forbidden for current scaffold promotion from TASK-06:

1. **Model alias / auto-switch / downgrade claims:** No accepted doctrine without current primary evidence.
2. **Model-family degradation claims:** No model ranking, degradation assertion, or steerability claim without eval evidence.
3. **RLHF/alignment causal claims:** No causal root-cause doctrine from `ConstantAIFailureAnalysis.md`.
4. **Numeric output/token ceilings:** No fixed browser or API limits as accepted prompt/workflow law.
5. **Browser product behavior claims:** No current Projects, memory, custom-instruction, or file-output behavior claims without current product check.
6. **API capability claims:** No `response_format`, structured-output, streaming, or max-token capability claim without API docs and runtime tests.
7. **Generation-parameter law:** No universal temperature or streaming rule without runtime owner validation.
8. **Server/cloud architecture:** No Hetzner, API-native, or server-side architecture mandate from this lane.
9. **Persistent state-store implementation:** No concrete store, service, or state-keeper architecture mandate.
10. **Tool noncompliance accusations:** No assertion that a connector misrepresents compliance without changed-file and fetch-back proof.
11. **“Verified causes” label from source:** The label is not inherited; each cause remains independently unverified.
12. **Scaffold mutation:** No mutation to `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md`, `TEMPLATES.md`, or `LEARNING_QUEUE.md` in TASK-06.

## 14. Scaffold impact boundary

All scaffold impacts below are candidate-only. This appendix creates no scaffold mutations.

| Scaffold file | Candidate-only impact | Required dependency before mutation | Forbidden in later scaffold |
|---|---|---|---|
| `TEMPLATES.md` | Compact state block, task payload, gate check, HALT/CLARIFY, file-output, split, closure, and patch-chooser pointers. | TASK-07 plus appendix evidence and fetch-back. | Full schema dump; runtime/API/model claims. |
| `MISTAKES.md` | Compact failure patterns: implicit state, compound scope, unsafe continuation, false closure, validation bypass. | TASK-08 plus regression appendix. | External model/platform root-cause assertions. |
| `BEST_PRACTICES.md` | Compact practice: explicit state, atomic tasks, gate before execution, verified output, external claims routed to research. | TASK-09 plus source notes and execution-control appendices. | Model-family or browser/API behavior claims as doctrine. |
| `ESSENCE.md` | One compressed principle after scaffold updates. | TASK-10, essence last. | Any external/runtime/platform claim. |
| `LEARNING_QUEUE.md` | Candidate-only entries for external verification, runtime/API tests, AI-routing owner review, state-store architecture, browser workflow checks. | TASK-11 after this appendix exists. | Marking unresolved claims as accepted doctrine. |

## 15. Integration dependencies for later `LEARNING_QUEUE.md` and scaffold updates

```yaml
later_integration_dependencies:
  TASK_07_TEMPLATES:
    may_use:
      - ECV-012 source-local stateless/external-state control
      - ECV-013 explicit state-store principle without implementation
      - ECV-018 safe source-local controls
    must_not_use:
      - ECV-001 through ECV-011 as accepted platform/runtime doctrine
      - ECV-014 through ECV-017 as resolved claims
    condition: compact pointers only; scaffold candidates only until written and fetched back
  TASK_08_MISTAKES:
    may_use:
      - source-local failure patterns from execution-control and regression appendices
    must_not_use:
      - RLHF, model downgrade, browser limit, or API capability claims as root causes
  TASK_09_BEST_PRACTICES:
    may_use:
      - explicit frame control and verification routing rule
    must_not_use:
      - model-family guidance, browser business-account guidance, or generation-parameter requirements as accepted doctrine
  TASK_10_ESSENCE:
    may_use:
      - one compressed source-local principle only
    must_not_use:
      - any external claim, API claim, browser claim, or runtime architecture claim
  TASK_11_LEARNING_QUEUE:
    may_use:
      - ECV-RQ-001 through ECV-RQ-007 as candidate-only entries
    must_not_use:
      - accepted status for unresolved model/platform/runtime claims
```

## 16. Validation checklist

```yaml
validation_checklist:
  path:
    file_exists: pass_required
    under_target_root: pass_required
    repository: leela-spec/MasterOfArts
    branch: main
  scope:
    task_id_repeated: TASK-06
    task_scope_repeated: Create a future-research verification ledger for external model and platform behavior claims.
    one_atomic_artifact: true
    scaffold_mutation: none
  source_refs:
    intended_source_files_referenced:
      - PROMPTFLOW_CONSTANT_FRAME_CONTROLLED_KB_INTEGRATION.md
      - APPENDIX_KB_CONSTANT_FAILURE_INTEGRATION_PROCESS.md
      - APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md
      - APPENDIX_KB_CONSTANT_FAILURE_SOURCE_NOTES.md
      - APPENDIX_KB_RUNTIME_TEMPLATE_CATALOG.md
      - ConstantAIFailureAnalysis.md
      - 00_SYSTEM_BOOTSTRAP.md
      - 01_API_CALL_STRUCTURE.md
  claim_status:
    every_claim_has_verification_status: true
    allowed_status_values_only: true
    external_claims_verified_without_evidence: false
    unverified_external_claims_marked_unverified_or_evidence_needed: true
    runtime_model_api_claims_routed_adjacent_or_future: true
  required_claim_classes:
    model_alias_auto_switch_downgrade_claims: inventoried
    model_family_instruction_following_claims: inventoried
    output_token_or_response_length_claims: inventoried
    browser_chat_limitations: inventoried
    api_capability_claims: inventoried
    streaming_response_format_structured_output_claims: inventoried
    temperature_generation_parameter_claims: inventoried
    server_side_execution_assumptions: inventoried
    persistent_state_store_assumptions: inventoried
    promptflow_failure_cause_claims: inventoried
    ai_handling_routing_claims: inventoried
    source_local_prompt_workflow_controls: inventoried
  scaffold:
    candidate_only: true
    essence_untouched: pass_required
    best_practices_untouched: pass_required
    mistakes_untouched: pass_required
    templates_untouched: pass_required
    learning_queue_untouched: pass_required
```

## 17. TASK-06 closure scope record

```yaml
task_scope_record:
  task_id: TASK-06
  task_type: appendix_create
  scope: Create a future-research verification ledger for external model and platform behavior claims.
  target_file: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_EXTERNAL_CLAIM_VERIFICATION.md
  output_format: markdown_file
  scaffold_mutation: none
  external_claim_promotion: none
  external_verification_performed: none
  scaffold_recommendations: candidate_only
```
