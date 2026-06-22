---
class: appendix
role: CONSTANT_FAILURE_SOURCE_NOTES
surface: agent_kb_appendix
quality: proposed
scope: agent
purpose: map every constant-failure research source file to route status, evidence strength, drift risk, verification status, and future integration target
status: created
created_at: 2026-05-06
owner: special_ops__prompts_workflows
validator: meta_ops
task_id: TASK-02
target_agent: special_ops__prompts_workflows
target_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/
source_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/
source_refs:
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/PROMPTFLOW_CONSTANT_FRAME_CONTROLLED_KB_INTEGRATION.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_CONSTANT_FAILURE_INTEGRATION_PROCESS.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/00_SYSTEM_BOOTSTRAP.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/00_PROJECT_BOOTSTRAP.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/01_API_CALL_STRUCTURE.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/02_STATE_BLOCK.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/02_MULTI_FILE_SESSION.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/03_TASK_PAYLOAD.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/03_PROJECT_OPENER.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/04_STATE_BLOCK.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/05_FILE_OUTPUT.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/05_SPLIT_SIGNAL.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/06_DIFF_OUTPUT (1).md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/07_RESEARCH_OUTPUT.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/07_RESEARCH_BLOCK.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/08_GATE_CHECK.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/08_TASK_CLOSURE.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/09_CONTROL_SIGNALS.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/GPT_PATCH_WORKFLOW.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/SOURCE_CONFLICT_REPORT.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/promptworkflowsAPI.py
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/ConstantAIFailureAnalysis.md
---

# APPENDIX_KB_CONSTANT_FAILURE_SOURCE_NOTES

## 1. Purpose

This appendix records source-by-source notes for the `NewResearchBecauseOfConstantFailure/` source pack. It maps each listed source file to evidence strength, impact, actionability, reuse likelihood, fit, drift risk, verification status, route status, and recommended future integration surface.

This file is an appendix-only ledger. It does not mutate `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md`, `TEMPLATES.md`, or `LEARNING_QUEUE.md`.

## 2. TASK-02 gate record

```yaml
GATE_CHECK:
  task_id: TASK-02
  task_type_understood: appendix_create
  scope_understood: Create source notes that map every new research file to route, evidence strength, drift risk, and verification status.
  target_file: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_CONSTANT_FAILURE_SOURCE_NOTES.md
  ambiguity_detected: false
  ready_to_execute: true
```

## 3. Source-root lock

```yaml
source_root_lock:
  working_repo: leela-spec/MasterOfArts
  target_repo: leela-spec/MasterOfArts
  target_branch: main
  target_agent: special_ops__prompts_workflows
  target_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/
  source_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/
  artifact_type: appendix_create
  allowed_write:
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_CONSTANT_FAILURE_SOURCE_NOTES.md
  forbidden_writes:
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/ESSENCE.md
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/BEST_PRACTICES.md
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/MISTAKES.md
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/TEMPLATES.md
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/LEARNING_QUEUE.md
```

## 4. Route-status legend

| Route status | Meaning | Promotion boundary |
|---|---|---|
| `accepted_execution_control` | Source-local execution rule that directly supports constant-frame prompt/workflow control without relying on external platform claims. | May support later compact scaffold rules or templates after promotion gates. |
| `appendix_protocol` | Detailed operating procedure, transport protocol, or long-form schema that should remain in appendix depth. | Scaffold may point to it but should not inline the protocol. |
| `scaffold_candidate` | Compact reusable rule or template candidate, not yet promoted. | Requires later scaffold task and appendix evidence. |
| `adjacent_lane_runtime_claim` | Runtime, API, model-routing, server, token, stream, or response-format claim that may belong to another lane. | Do not promote as prompt/workflow doctrine from this file alone. |
| `future_research` | External model/platform behavior claim or unresolved architecture question requiring verification. | Candidate only until a future verification appendix validates it. |
| `duplicate_or_variant` | Overlapping form of another source already routed through a stronger source. | Retain as variant evidence; avoid duplicate scaffold entries. |
| `rejected_for_promotion` | Missing, unresolved, contradictory, or out-of-scope source material. | Do not promote. |

## 5. Scoring model

Scores use a 1-5 scale. Higher is stronger except drift risk, where higher means riskier to promote broadly.

| Score field | 1 | 3 | 5 |
|---|---|---|---|
| Evidence strength (`EVD`) | Not found, indirect, or externally asserted. | Present but partial, variant, or dependent on reconciliation. | Direct source-local control with clear schema or rule. |
| Impact (`IMP`) | Low effect on recurring prompt/workflow failure. | Useful for some workflows. | Directly prevents scope drift, stale state, unsafe continuation, or false closure. |
| Actionability (`ACT`) | Hard to apply without new design work. | Applies with interpretation. | Immediately usable as rule, schema, template, or protocol. |
| Reuse likelihood (`REUSE`) | Narrow one-off utility. | Useful across several tasks. | Reusable across most high-governance prompt/workflow tasks. |
| Fit (`FIT`) | Belongs outside this agent lane. | Shared with adjacent lanes or examples. | Native fit for `special_ops__prompts_workflows`. |
| Drift risk (`RSK`) | Low risk if promoted compactly. | Moderate risk; needs appendix boundary. | High risk; external/runtime/cross-lane claim likely to overreach. |

## 6. Source inventory table

| # | File path | Source function | EVD | IMP | ACT | REUSE | FIT | RSK | Route status | Verification status | Recommended target | Notes |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|---|---|
| 1 | `NewResearchBecauseOfConstantFailure/00_SYSTEM_BOOTSTRAP.md` | Runtime/execution bootstrap, authority hierarchy, gate protocol. | 5 | 5 | 5 | 5 | 5 | 3 | `accepted_execution_control` | fetched | `APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md`; later compact `BEST_PRACTICES.md` and `TEMPLATES.md` pointers | Accept local execution controls; route model pinning, server/API, stream, and temperature claims as adjacent/future only. |
| 2 | `NewResearchBecauseOfConstantFailure/00_PROJECT_BOOTSTRAP.md` | Constrained project/session opener and artifact-output contract. | 4 | 4 | 4 | 4 | 4 | 3 | `scaffold_candidate` | fetched | `APPENDIX_KB_RUNTIME_TEMPLATE_CATALOG.md`; possible compact project opener template | Useful opener, but overlaps with `03_PROJECT_OPENER.md` and generated templates. |
| 3 | `NewResearchBecauseOfConstantFailure/01_API_CALL_STRUCTURE.md` | API call envelope, stateless state/task injection, response-format rules. | 4 | 5 | 4 | 4 | 3 | 5 | `adjacent_lane_runtime_claim` | fetched | `APPENDIX_KB_RUNTIME_TEMPLATE_CATALOG.md`; `APPENDIX_KB_EXTERNAL_CLAIM_VERIFICATION.md` | Statelessness is relevant; concrete runtime/model/JSON enforcement belongs to runtime or AI-handling validation. |
| 4 | `NewResearchBecauseOfConstantFailure/02_STATE_BLOCK.md` | JSON state block replacing implicit chat-history inference. | 5 | 5 | 5 | 5 | 5 | 2 | `accepted_execution_control` | fetched | `APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md`; later compact state template | Strongest canonical state-control source. |
| 5 | `NewResearchBecauseOfConstantFailure/02_MULTI_FILE_SESSION.md` | Manifest-first multi-file choreography and one-file-at-a-time protocol. | 5 | 4 | 5 | 4 | 5 | 3 | `appendix_protocol` | fetched | `APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md`; `TEMPLATES.md` compact pointer candidate | Retain detailed sequencing in appendix; scaffold should keep only atomic artifact rule. |
| 6 | `NewResearchBecauseOfConstantFailure/03_TASK_PAYLOAD.md` | Atomic task payload schema and no-directory-scan rule. | 5 | 5 | 5 | 5 | 5 | 2 | `accepted_execution_control` | fetched | `APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md`; later `TEMPLATES.md` task payload | Directly supports scope and source-authority enforcement. |
| 7 | `NewResearchBecauseOfConstantFailure/03_PROJECT_OPENER.md` | First-message project opener for browser/chat sessions. | 4 | 4 | 4 | 4 | 5 | 3 | `appendix_protocol` | fetched | `APPENDIX_KB_RUNTIME_TEMPLATE_CATALOG.md`; examples appendix | Keep as session-opening protocol; reconcile with `00_PROJECT_BOOTSTRAP.md`. |
| 8 | `NewResearchBecauseOfConstantFailure/04_STATE_BLOCK.md` | Markdown/YAML state block variant for manual session use. | 4 | 4 | 4 | 4 | 5 | 3 | `duplicate_or_variant` | fetched | `APPENDIX_KB_RUNTIME_TEMPLATE_CATALOG.md`; examples appendix | Variant of `02_STATE_BLOCK.md`; useful for browser/manual workflows but not canonical over JSON state block. |
| 9 | `NewResearchBecauseOfConstantFailure/05_FILE_OUTPUT.md` | File-write JSON schema and server write protocol. | 5 | 5 | 5 | 4 | 5 | 3 | `accepted_execution_control` | fetched | `APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md`; later file-output template pointer | Strong validated-output source; server-specific steps remain appendix depth. |
| 10 | `NewResearchBecauseOfConstantFailure/05_SPLIT_SIGNAL.md` | Split-required protocol for long file generation. | 5 | 4 | 5 | 4 | 5 | 3 | `appendix_protocol` | fetched | `APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md`; later compact split template pointer | Prevents summary substitution and output collapse; exact token ceilings must not become global law. |
| 11 | `NewResearchBecauseOfConstantFailure/06_DIFF_OUTPUT (1).md` | Unified-diff output contract for targeted edits. | 4 | 5 | 5 | 5 | 5 | 3 | `appendix_protocol` | fetched | `APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md` | One transport option; must be reconciled with SEARCH/REPLACE workflow rather than treated as universal. |
| 12 | `NewResearchBecauseOfConstantFailure/07_RESEARCH_OUTPUT.md` | JSON research-output schema with scope, sources, and split handling. | 5 | 4 | 4 | 4 | 5 | 3 | `scaffold_candidate` | fetched | `APPENDIX_KB_RUNTIME_TEMPLATE_CATALOG.md`; possible compact research template | Good template candidate after overlap check. |
| 13 | `NewResearchBecauseOfConstantFailure/07_RESEARCH_BLOCK.md` | Markdown research-output block for synthesis tasks. | 4 | 4 | 4 | 4 | 5 | 3 | `duplicate_or_variant` | fetched | `APPENDIX_KB_RUNTIME_TEMPLATE_CATALOG.md`; examples appendix | Human-readable variant of `07_RESEARCH_OUTPUT.md`; retain as output-shape variant. |
| 14 | `NewResearchBecauseOfConstantFailure/08_GATE_CHECK.md` | Pre-execution gate schema and server readiness rules. | 5 | 5 | 5 | 5 | 5 | 2 | `accepted_execution_control` | fetched | `APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md`; later gate template | Directly enforces task type, scope, target, constraints, ambiguity, and readiness. |
| 15 | `NewResearchBecauseOfConstantFailure/08_TASK_CLOSURE.md` | Task-closure proof block. | 5 | 4 | 5 | 5 | 5 | 2 | `accepted_execution_control` | fetched | `APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md`; later closure template | Lightweight proof object; later scaffold should stay compact. |
| 16 | `NewResearchBecauseOfConstantFailure/09_CONTROL_SIGNALS.md` | HALT and CLARIFY signal contracts. | 5 | 5 | 5 | 5 | 5 | 2 | `accepted_execution_control` | fetched | `APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md`; later mistake/best-practice support | Strong stop-discipline source for ambiguity and unsafe continuation. |
| 17 | `NewResearchBecauseOfConstantFailure/GPT_PATCH_WORKFLOW.md` | SEARCH/REPLACE patch transport and dry-run workflow. | 4 | 5 | 5 | 5 | 5 | 3 | `appendix_protocol` | fetched | `APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md` | Conflicts with unified-diff preference unless promoted through a chooser. |
| 18 | `NewResearchBecauseOfConstantFailure/SOURCE_CONFLICT_REPORT.md` | Intended conflict ledger for source contradictions. | 1 | 3 | 1 | 1 | 4 | 5 | `rejected_for_promotion` | not_found_at_listed_path | none until source is restored or path corrected | Listed input ref did not resolve on `main`; no claims promoted from it. |
| 19 | `NewResearchBecauseOfConstantFailure/promptworkflowsAPI.py` | Programmatic generation of template Markdown files. | 4 | 4 | 3 | 4 | 4 | 4 | `appendix_protocol` | fetched | `APPENDIX_KB_RUNTIME_TEMPLATE_CATALOG.md` | Useful generated catalog, but must be reconciled with hand-authored sources before scaffold promotion. |
| 20 | `NewResearchBecauseOfConstantFailure/ConstantAIFailureAnalysis.md` | Failure analysis, external model/platform claims, and browser/API recommendations. | 2 | 4 | 2 | 3 | 3 | 5 | `future_research` | fetched_truncated_but_substantive | `APPENDIX_KB_EXTERNAL_CLAIM_VERIFICATION.md`; candidate-only `LEARNING_QUEUE.md` | Treat as research leads and problem framing; do not promote external claims as accepted doctrine. |

## 7. Source-by-source notes

### 7.1 `00_SYSTEM_BOOTSTRAP.md`

- **Accepted route:** `accepted_execution_control` for one task per call, no scope expansion, no implicit state inference, authority hierarchy, machine-readable output, and gate protocol.
- **Caution route:** runtime environment, model pinning, temperature, max-token, stream, and model-list claims are `adjacent_lane_runtime_claim` or `future_research` when used outside this appendix.
- **Supports:** execution-control appendix, compact best-practice rule, compact gate/template pointer.
- **Promotion blocker:** cannot be used to create global runtime law for model selection or platform behavior.

### 7.2 `00_PROJECT_BOOTSTRAP.md`

- **Accepted route:** `scaffold_candidate` for constrained opener discipline: one artifact per response, no explanation outside artifact, no scope expansion, and ambiguity stops.
- **Variant risk:** overlaps with `03_PROJECT_OPENER.md` and `promptworkflowsAPI.py` generated opener.
- **Supports:** runtime template catalog and possible compact browser/project opener template.
- **Promotion blocker:** must be deduplicated before insertion into `TEMPLATES.md`.

### 7.3 `01_API_CALL_STRUCTURE.md`

- **Accepted subset:** stateless call principle and explicit order of state block before task payload.
- **Primary route:** `adjacent_lane_runtime_claim` because concrete API fields, response-format enforcement, model selection, and token budgets are runtime/platform assertions.
- **Supports:** runtime template catalog and external-claim verification appendix.
- **Promotion blocker:** cannot be promoted as accepted prompt/workflow doctrine without runtime-lane verification.

### 7.4 `02_STATE_BLOCK.md`

- **Accepted route:** `accepted_execution_control`.
- **Core claim:** state is an explicit input surface; executor must not infer state from chat history or mutate state directly.
- **Supports:** execution-control appendix, regression examples for stale state, and later compact state-block template.
- **Promotion blocker:** any persistent state-store path or server detail must remain implementation-specific unless verified.

### 7.5 `02_MULTI_FILE_SESSION.md`

- **Accepted route:** `appendix_protocol`.
- **Core claim:** multi-file work must start with a manifest and proceed one file at a time.
- **Supports:** regression examples and compact atomic-output rule.
- **Promotion blocker:** full protocol is too dense for scaffold; keep the detailed choreography in appendix depth.

### 7.6 `03_TASK_PAYLOAD.md`

- **Accepted route:** `accepted_execution_control`.
- **Core claim:** task payloads must be atomic, explicit, and bounded by listed input refs.
- **Supports:** execution-control appendix, future `TEMPLATES.md` task payload block, `MISTAKES.md` compound-scope failure pattern.
- **Promotion blocker:** absolute server path requirements should not be generalized to all environments.

### 7.7 `03_PROJECT_OPENER.md`

- **Accepted route:** `appendix_protocol`.
- **Core claim:** new project sessions need explicit project, session, task, output type, constraints, and state ref.
- **Supports:** runtime template catalog and browser/manual workflow examples.
- **Promotion blocker:** deduplicate against `00_PROJECT_BOOTSTRAP.md` before scaffold use.

### 7.8 `04_STATE_BLOCK.md`

- **Accepted route:** `duplicate_or_variant`.
- **Core claim:** manual YAML state blocks can preserve continuity in chat/browser contexts.
- **Supports:** examples appendix and runtime template catalog.
- **Promotion blocker:** do not promote two competing canonical state schemas; `02_STATE_BLOCK.md` remains stronger canonical evidence.

### 7.9 `05_FILE_OUTPUT.md`

- **Accepted route:** `accepted_execution_control`.
- **Core claim:** file writes require complete content, scope proof, validation, write, and fetch-back or equivalent verification.
- **Supports:** execution-control appendix and future compact file-output template pointer.
- **Promotion blocker:** exact server write steps stay implementation-specific.

### 7.10 `05_SPLIT_SIGNAL.md`

- **Accepted route:** `appendix_protocol`.
- **Core claim:** long outputs must split at clean logical boundaries and never summarize remaining content.
- **Supports:** regression examples and compact split template pointer.
- **Promotion blocker:** numeric output ceilings are runtime-dependent and should not be accepted as stable doctrine.

### 7.11 `06_DIFF_OUTPUT (1).md`

- **Accepted route:** `appendix_protocol`.
- **Core claim:** targeted edits can use unified diff with limited context and no whole-file rewrite.
- **Supports:** patch transport appendix.
- **Promotion blocker:** conflicts with `GPT_PATCH_WORKFLOW.md` prohibition on unified diffs; requires transport chooser.

### 7.12 `07_RESEARCH_OUTPUT.md`

- **Accepted route:** `scaffold_candidate`.
- **Core claim:** research outputs need explicit topic, format, depth, sources, scope status, and recommendation controls.
- **Supports:** runtime template catalog and possible future research-output template.
- **Promotion blocker:** check existing templates for overlap before scaffold insertion.

### 7.13 `07_RESEARCH_BLOCK.md`

- **Accepted route:** `duplicate_or_variant`.
- **Core claim:** research blocks can use bounded Markdown headers and inline source labels.
- **Supports:** examples appendix and runtime template catalog.
- **Promotion blocker:** avoid duplicate research templates unless the catalog separates JSON and Markdown modes.

### 7.14 `08_GATE_CHECK.md`

- **Accepted route:** `accepted_execution_control`.
- **Core claim:** gate checks occur before execution and explicitly confirm task type, scope, target, constraints, ambiguity, and readiness.
- **Supports:** execution-control appendix, compact gate template, and regression tests.
- **Promotion blocker:** server parsing details remain implementation-specific.

### 7.15 `08_TASK_CLOSURE.md`

- **Accepted route:** `accepted_execution_control`.
- **Core claim:** completed work needs a closure proof with task id, output type, file, scope status, additions beyond scope, and next task.
- **Supports:** execution-control appendix, compact closure template, and false-completion regression tests.
- **Promotion blocker:** do not allow closure text to replace fetch-back validation.

### 7.16 `09_CONTROL_SIGNALS.md`

- **Accepted route:** `accepted_execution_control`.
- **Core claim:** HALT and CLARIFY terminate or pause execution; no downstream execution continues after a HALT.
- **Supports:** execution-control appendix, `MISTAKES.md` unsafe-continuation pattern, and `BEST_PRACTICES.md` stop-discipline rule.
- **Promotion blocker:** log-file locations are runtime-specific.

### 7.17 `GPT_PATCH_WORKFLOW.md`

- **Accepted route:** `appendix_protocol`.
- **Core claim:** SEARCH/REPLACE patches require live-file preimage, exact-once match, dry-run before write, and regeneration on mismatch.
- **Supports:** patch transport appendix.
- **Promotion blocker:** cannot coexist as universal law with unified diff protocol; requires chooser and failure-mode matrix.

### 7.18 `SOURCE_CONFLICT_REPORT.md`

- **Accepted route:** `rejected_for_promotion`.
- **Resolution status:** the exact listed path did not resolve on `main` during TASK-02 fetch-back preparation.
- **Supports:** no scaffold or appendix claim until restored or path-corrected.
- **Promotion blocker:** missing source cannot provide evidence.

### 7.19 `promptworkflowsAPI.py`

- **Accepted route:** `appendix_protocol`.
- **Core claim:** generated templates mirror several hand-authored Markdown templates and provide a catalog source.
- **Supports:** runtime template catalog.
- **Promotion blocker:** generated output must be compared against hand-authored sources; do not promote generated variants as canonical automatically.

### 7.20 `ConstantAIFailureAnalysis.md`

- **Accepted route:** `future_research`.
- **Core claim handling:** use only as problem framing and research-lead inventory unless each external model/platform claim is independently verified.
- **Supports:** external-claim verification appendix and candidate-only learning queue entries.
- **Promotion blocker:** external claims about model downgrades, model behavior, context windows, output limits, browser limitations, API capability, and vendor behavior remain unaccepted.

## 8. Duplicate and variant handling

| Variant cluster | Primary source | Variant source(s) | Handling |
|---|---|---|---|
| State blocks | `02_STATE_BLOCK.md` | `04_STATE_BLOCK.md` | Use `02_STATE_BLOCK.md` as canonical execution-control source; keep `04_STATE_BLOCK.md` as manual/browser variant. |
| Project/session openers | `00_PROJECT_BOOTSTRAP.md` | `03_PROJECT_OPENER.md`, `promptworkflowsAPI.py` | Reconcile in runtime template catalog before scaffold promotion. |
| Research outputs | `07_RESEARCH_OUTPUT.md` | `07_RESEARCH_BLOCK.md` | Treat JSON and Markdown variants as separate modes only if catalog validates both. |
| Patch transport | none yet | `GPT_PATCH_WORKFLOW.md`, `06_DIFF_OUTPUT (1).md` | Create patch-transport appendix with chooser; do not privilege one transport globally. |
| Split/multi-file output | `05_SPLIT_SIGNAL.md` | `02_MULTI_FILE_SESSION.md` | Use split signal for long single artifacts and manifest protocol for multi-file sessions. |
| Generated templates | hand-authored Markdown files | `promptworkflowsAPI.py` | Generated templates are evidence and reconciliation inputs, not canonical by default. |
| Missing conflict report | none | `SOURCE_CONFLICT_REPORT.md` | Keep rejected until path exists or source is supplied. |

## 9. Scaffold-candidate mapping

| Scaffold surface | Candidate source files | Candidate contribution | Required prerequisite |
|---|---|---|---|
| `BEST_PRACTICES.md` | `00_SYSTEM_BOOTSTRAP.md`, `02_STATE_BLOCK.md`, `03_TASK_PAYLOAD.md`, `08_GATE_CHECK.md`, `09_CONTROL_SIGNALS.md`, `05_FILE_OUTPUT.md` | Compact rule for explicit state, atomic payloads, preflight gates, stop signals, and verified writes. | Appendices 1-4 exist and claim statuses remain explicit. |
| `MISTAKES.md` | `03_TASK_PAYLOAD.md`, `02_STATE_BLOCK.md`, `09_CONTROL_SIGNALS.md`, `08_TASK_CLOSURE.md`, `05_SPLIT_SIGNAL.md` | Failure patterns for compound scope, implicit state, post-HALT continuation, false closure, and summary substitution. | Regression examples appendix. |
| `TEMPLATES.md` | `02_STATE_BLOCK.md`, `03_TASK_PAYLOAD.md`, `08_GATE_CHECK.md`, `09_CONTROL_SIGNALS.md`, `05_FILE_OUTPUT.md`, `08_TASK_CLOSURE.md`, `07_RESEARCH_OUTPUT.md` | Compact template stubs with appendix pointers. | Runtime template catalog and execution-control appendix. |
| `ESSENCE.md` | Execution-control cluster only | One compressed constant-frame-control doctrine sentence and appendix pointer. | Essence last after template, mistake, and best-practice updates. |
| `LEARNING_QUEUE.md` | `01_API_CALL_STRUCTURE.md`, `ConstantAIFailureAnalysis.md`, `promptworkflowsAPI.py` | Candidate-only entries for runtime ownership, external model/platform verification, and template sidecars. | External-claim verification appendix and runtime catalog. |

## 10. Appendix-candidate mapping

| Appendix target | Supporting sources | Status after this ledger |
|---|---|---|
| `APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md` | `00_SYSTEM_BOOTSTRAP.md`, `02_STATE_BLOCK.md`, `03_TASK_PAYLOAD.md`, `08_GATE_CHECK.md`, `09_CONTROL_SIGNALS.md`, `05_FILE_OUTPUT.md`, `05_SPLIT_SIGNAL.md`, `08_TASK_CLOSURE.md` | Existing prerequisite, already created before this source-notes appendix. |
| `APPENDIX_KB_CONSTANT_FAILURE_SOURCE_NOTES.md` | All listed `NewResearchBecauseOfConstantFailure/` files plus controlling/integration appendices. | This file. |
| `APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md` | `GPT_PATCH_WORKFLOW.md`, `06_DIFF_OUTPUT (1).md`, missing/possible `SOURCE_CONFLICT_REPORT.md` | Next recommended task; must reconcile conflicting transport instructions. |
| `APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md` | `02_STATE_BLOCK.md`, `03_TASK_PAYLOAD.md`, `08_GATE_CHECK.md`, `09_CONTROL_SIGNALS.md`, `08_TASK_CLOSURE.md`, `05_SPLIT_SIGNAL.md`, `02_MULTI_FILE_SESSION.md` | Needed before mistake updates. |
| `APPENDIX_KB_RUNTIME_TEMPLATE_CATALOG.md` | `promptworkflowsAPI.py`, `00_PROJECT_BOOTSTRAP.md`, `03_PROJECT_OPENER.md`, `04_STATE_BLOCK.md`, `07_RESEARCH_OUTPUT.md`, `07_RESEARCH_BLOCK.md` | Needed before template consolidation. |
| `APPENDIX_KB_EXTERNAL_CLAIM_VERIFICATION.md` | `ConstantAIFailureAnalysis.md`, runtime/model portions of `00_SYSTEM_BOOTSTRAP.md` and `01_API_CALL_STRUCTURE.md` | Future/research appendix before any external claim promotion. |

## 11. Future-research mapping

| Research ID | Source(s) | Route status | Verification question | Candidate destination |
|---|---|---|---|---|
| `PW-CF-RQ-001` | `ConstantAIFailureAnalysis.md` | `future_research` | Which claims about model drift, downgrades, output caps, and browser/API behavior are externally verified and current? | `APPENDIX_KB_EXTERNAL_CLAIM_VERIFICATION.md` |
| `PW-CF-RQ-002` | `01_API_CALL_STRUCTURE.md`, `00_SYSTEM_BOOTSTRAP.md` | `adjacent_lane_runtime_claim` | Which runtime parameters belong to prompts/workflows versus AI handling/routing or platform implementation? | `LEARNING_QUEUE.md` candidate; AI-handling/routing handoff. |
| `PW-CF-RQ-003` | `02_STATE_BLOCK.md`, `04_STATE_BLOCK.md` | `future_research` | Should state keeper be an explicit OpenClaw role or a process label inside this lane? | MetaOps / Knowledge Bank review. |
| `PW-CF-RQ-004` | `GPT_PATCH_WORKFLOW.md`, `06_DIFF_OUTPUT (1).md` | `appendix_protocol` | What chooser decides full-body replacement, SEARCH/REPLACE, unified diff, or live edit? | `APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md` |
| `PW-CF-RQ-005` | `05_SPLIT_SIGNAL.md`, `ConstantAIFailureAnalysis.md` | `future_research` | Which output ceilings are stable for browser, API, and repo-write modes? | `APPENDIX_KB_EXTERNAL_CLAIM_VERIFICATION.md` |
| `PW-CF-RQ-006` | `promptworkflowsAPI.py` | `appendix_protocol` | Should generated template sidecars exist, and what schema owns them? | `APPENDIX_KB_RUNTIME_TEMPLATE_CATALOG.md` |
| `PW-CF-RQ-007` | `SOURCE_CONFLICT_REPORT.md` | `rejected_for_promotion` | Was the conflict report removed, renamed, or never committed to `main`? | Future source repair before use. |

## 12. External-claim caution

External model, runtime, browser, platform, provider, and API behavior claims are not accepted doctrine in this appendix.

```yaml
external_claim_caution:
  default_route_status: future_research
  adjacent_lane_allowed_for_runtime_claims: true
  accepted_doctrine_from_external_claims_in_TASK_02: false
  examples_confined_to_future_or_adjacent:
    - model_auto_switching_or_downgrade_claims
    - context_window_or_output_cap_claims
    - browser_file_write_limit_claims
    - API_response_token_claims
    - model_family_instruction_following_claims
    - provider_load_or_routing_behavior_claims
    - runtime_temperature_stream_response_format_requirements
```

Accepted material from the source pack is limited to source-local execution controls: explicit state, atomic tasks, gate checks, stop signals, verified output, split discipline, closure proof, and patch-transport caution.

## 13. Promotion blockers

| Blocker | Applies to | Required resolution |
|---|---|---|
| Missing source file | `SOURCE_CONFLICT_REPORT.md` | Restore file, correct path, or remove it from future input refs before using its claims. |
| Conflicting patch transport doctrine | `GPT_PATCH_WORKFLOW.md` vs `06_DIFF_OUTPUT (1).md` | Create chooser in `APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md`. |
| Duplicate template surfaces | Project openers, state blocks, research blocks, generated templates | Reconcile in `APPENDIX_KB_RUNTIME_TEMPLATE_CATALOG.md`. |
| External model/platform claims | `ConstantAIFailureAnalysis.md` and runtime portions of bootstrap/API files | Verify in `APPENDIX_KB_EXTERNAL_CLAIM_VERIFICATION.md` before promotion. |
| Scaffold density risk | All template/protocol sources | Keep scaffold compact with appendix pointers only. |
| Essence ordering | Any essence candidate | Update `ESSENCE.md` only after scaffold files are updated and verified. |

## 14. Validation checklist

```yaml
validation_checklist:
  task_id: TASK-02
  scope: Create source notes that map every new research file to route, evidence strength, drift risk, and verification status.
  file_exists_after_write: required
  under_target_root: required
  source_root_referenced: required
  all_listed_new_research_files_have_route_status: required
  evidence_strength_assigned_1_to_5: required
  impact_assigned_1_to_5: required
  actionability_assigned_1_to_5: required
  reuse_likelihood_assigned_1_to_5: required
  fit_assigned_1_to_5: required
  drift_risk_assigned_1_to_5: required
  external_claims_status: future_research_or_adjacent_lane_runtime_claim_only
  scaffold_files_mutated: forbidden
  missing_source_handling: rejected_for_promotion
  fetch_back_required: true
```

## 15. Next integration dependencies

| Next task | Dependency created by this appendix | Reason |
|---|---|---|
| `TASK-03 create APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md` | Patch sources are routed and conflict is identified. | The next safe integration step is to reconcile SEARCH/REPLACE, unified diff, full-body replacement, and live-edit modes. |
| `TASK-04 create APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md` | Regression-supporting sources are mapped. | Mistake updates need examples for stale state, compound scope, split failure, false closure, and unsafe continuation. |
| `TASK-05 create APPENDIX_KB_RUNTIME_TEMPLATE_CATALOG.md` | Template/generator variants are mapped. | Template scaffold updates need a reconciled catalog. |
| `TASK-06 create APPENDIX_KB_EXTERNAL_CLAIM_VERIFICATION.md` | Future-research claims are isolated. | External and runtime/platform claims remain blocked until verified. |

## 16. TASK-02 closure scope record

```yaml
task_scope_record:
  task_id: TASK-02
  task_type: appendix_create
  scope: Create source notes that map every new research file to route, evidence strength, drift risk, and verification status.
  target_file: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_CONSTANT_FAILURE_SOURCE_NOTES.md
  output_format: markdown_file
  scaffold_mutation: none
  external_claim_promotion: none
  missing_input_ref_handling:
    OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/SOURCE_CONFLICT_REPORT.md: rejected_for_promotion
```
