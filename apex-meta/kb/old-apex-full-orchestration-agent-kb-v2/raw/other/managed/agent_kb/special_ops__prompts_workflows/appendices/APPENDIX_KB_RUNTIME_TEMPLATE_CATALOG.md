---
class: appendix
role: RUNTIME_TEMPLATE_CATALOG
surface: agent_kb_appendix
quality: proposed
scope: agent
purpose: create a reconciled runtime-template catalog from generated and hand-authored templates without changing accepted scaffold doctrine
status: created
created_at: 2026-05-06
owner: special_ops__prompts_workflows
validator: meta_ops
task_id: TASK-05
target_agent: special_ops__prompts_workflows
target_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/
source_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/
source_refs:
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/PROMPTFLOW_CONSTANT_FRAME_CONTROLLED_KB_INTEGRATION.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_CONSTANT_FAILURE_INTEGRATION_PROCESS.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_CONSTANT_FAILURE_SOURCE_NOTES.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/promptworkflowsAPI.py
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/00_PROJECT_BOOTSTRAP.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/03_PROJECT_OPENER.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/02_STATE_BLOCK.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/04_STATE_BLOCK.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/03_TASK_PAYLOAD.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/08_GATE_CHECK.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/09_CONTROL_SIGNALS.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/05_FILE_OUTPUT.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/05_SPLIT_SIGNAL.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/08_TASK_CLOSURE.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/07_RESEARCH_OUTPUT.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/07_RESEARCH_BLOCK.md
---

# APPENDIX_KB_RUNTIME_TEMPLATE_CATALOG

## 1. Purpose

This appendix reconciles runtime-template material from generated sidecars in `promptworkflowsAPI.py` and hand-authored Markdown templates in `NewResearchBecauseOfConstantFailure/`.

Its purpose is cataloging and routing only. It does not mutate or supersede accepted scaffold doctrine in `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md`, `TEMPLATES.md`, or `LEARNING_QUEUE.md`.

## 2. TASK-05 gate record

```yaml
GATE_CHECK:
  task_id: TASK-05
  task_type_understood: appendix_create
  scope_understood: Create a reconciled runtime-template catalog from generated and hand-authored templates without changing accepted scaffold doctrine.
  target_file: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_RUNTIME_TEMPLATE_CATALOG.md
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
  scope: Create a reconciled runtime-template catalog from generated and hand-authored templates without changing accepted scaffold doctrine.
  allowed_write:
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_RUNTIME_TEMPLATE_CATALOG.md
  forbidden_writes:
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/ESSENCE.md
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/BEST_PRACTICES.md
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/MISTAKES.md
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/TEMPLATES.md
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/LEARNING_QUEUE.md
```

## 4. Source and route-status ledger

| Source | Used for | Route status | Promotion boundary |
|---|---|---|---|
| `PROMPTFLOW_CONSTANT_FRAME_CONTROLLED_KB_INTEGRATION.md` | Task order, appendix-before-scaffold sequence, TASK-05 target, runtime-template catalog requirement, scaffold gates. | `accepted_for_frame_control` | Controls this appendix and later promotion gates. |
| `appendices/APPENDIX_KB_CONSTANT_FAILURE_INTEGRATION_PROCESS.md` | Ranking of template families, route model, generated-template caution, future-research boundaries. | `accepted_for_route_control` | Supports catalog routing; does not authorize scaffold mutation. |
| `appendices/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md` | Accepted state, payload, gate, control-signal, file-output, split, and closure contracts. | `accepted_execution_control` | May support later compact scaffold templates after promotion gate. |
| `appendices/APPENDIX_KB_CONSTANT_FAILURE_SOURCE_NOTES.md` | Source inventory, duplicate handling, canonical/variant notes, missing-source and external-claim cautions. | `accepted_for_source_route_status` | Used to avoid duplicate scaffold promotion. |
| `appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md` | Regression expectations for state drift, compound scope, false completion, split failure, and promotion gate failure. | `accepted_for_regression_context` | Supports later tests; no scaffold mutation here. |
| `NewResearchBecauseOfConstantFailure/promptworkflowsAPI.py` | Generated template registry and generated sidecar names. | `evidence_only_generated_templates` | Generated output is reconciliation evidence, not canonical scaffold doctrine. The file was inspected only and not executed. |
| `NewResearchBecauseOfConstantFailure/00_PROJECT_BOOTSTRAP.md` | Hand-authored project bootstrap template. | `scaffold_candidate` | Candidate-only project opener/bootstrap template after deduplication. |
| `NewResearchBecauseOfConstantFailure/03_PROJECT_OPENER.md` | Hand-authored project opener template. | `appendix_protocol` | Example/variant until reconciled with bootstrap and generated opener. |
| `NewResearchBecauseOfConstantFailure/02_STATE_BLOCK.md` | JSON state block template and state-keeper boundary. | `canonical_template_source` | Strongest state-block evidence; server path claims remain implementation-specific. |
| `NewResearchBecauseOfConstantFailure/04_STATE_BLOCK.md` | Manual/browser Markdown state-block variant. | `duplicate_or_variant` | Retain as variant; do not promote two canonical state schemas. |
| `NewResearchBecauseOfConstantFailure/03_TASK_PAYLOAD.md` | Atomic task payload template. | `canonical_template_source` | Strong candidate for later compact `TEMPLATES.md` entry. |
| `NewResearchBecauseOfConstantFailure/08_GATE_CHECK.md` | Gate-check template. | `canonical_template_source` | Strong candidate for later compact `TEMPLATES.md` entry. |
| `NewResearchBecauseOfConstantFailure/09_CONTROL_SIGNALS.md` | HALT and CLARIFY templates. | `canonical_template_source` | Strong candidate for later compact `TEMPLATES.md` entry. |
| `NewResearchBecauseOfConstantFailure/05_FILE_OUTPUT.md` | Validated file-output schema. | `canonical_template_source` | Strong candidate for later compact file-output pointer; server write details remain appendix-level. |
| `NewResearchBecauseOfConstantFailure/05_SPLIT_SIGNAL.md` | Split-required template. | `appendix_protocol` | Candidate compact pointer only; numeric ceilings remain runtime-dependent. |
| `NewResearchBecauseOfConstantFailure/08_TASK_CLOSURE.md` | Task-closure proof template. | `canonical_template_source` | Strong candidate for later compact closure template. |
| `NewResearchBecauseOfConstantFailure/07_RESEARCH_OUTPUT.md` | JSON research-output template. | `scaffold_candidate` | Candidate research-output template after overlap review. |
| `NewResearchBecauseOfConstantFailure/07_RESEARCH_BLOCK.md` | Markdown research-block template. | `duplicate_or_variant` | Variant/example; avoid duplicate scaffold entry unless JSON and Markdown modes are separated. |

## 5. Canonicality and route-status legend

### 5.1 Canonicality values

| Canonicality | Meaning | Scaffold implication |
|---|---|---|
| `canonical` | Strongest available source-local template for the family. | May become a compact scaffold candidate in a later task. |
| `variant` | Valid alternate form for a different operating mode. | Keep as appendix evidence unless scaffold explicitly needs mode separation. |
| `example` | Useful as an instance, demonstration, or source-local convention. | Do not promote as canonical without normalization. |
| `future_candidate` | Potential template or pointer that needs owner, schema, or overlap review. | Candidate-only. |
| `duplicate_or_rejected` | Duplicate, weaker, conflicting, missing, or unsafe for promotion. | Retain only for reconciliation notes or reject. |

### 5.2 Route-status values

| Route status | Meaning |
|---|---|
| `accepted_execution_control` | Source-local control accepted as appendix evidence for prompt/workflow governance. |
| `canonical_template_source` | Strong hand-authored source that can support a later compact template candidate. |
| `appendix_protocol` | Detailed operating protocol retained in appendix depth. |
| `scaffold_candidate` | Candidate-only scaffold mapping for a later task. |
| `evidence_only_generated_templates` | Generated material from `promptworkflowsAPI.py`; not canonical by default. |
| `duplicate_or_variant` | Overlapping template retained for mode distinction or duplicate analysis. |
| `adjacent_lane_runtime_claim` | Runtime/API/model/platform detail that belongs outside accepted prompt-workflow doctrine until verified. |
| `future_research` | Unverified or cross-lane claim requiring a later verification appendix. |
| `duplicate_or_rejected` | Rejected for scaffold promotion because it is duplicate, weaker, conflicting, or implementation-specific. |

## 6. Generated-vs-hand-authored reconciliation method

```yaml
reconciliation_method:
  step_1_collect_hand_authored_templates:
    sources:
      - 00_PROJECT_BOOTSTRAP.md
      - 03_PROJECT_OPENER.md
      - 02_STATE_BLOCK.md
      - 04_STATE_BLOCK.md
      - 03_TASK_PAYLOAD.md
      - 08_GATE_CHECK.md
      - 09_CONTROL_SIGNALS.md
      - 05_FILE_OUTPUT.md
      - 05_SPLIT_SIGNAL.md
      - 08_TASK_CLOSURE.md
      - 07_RESEARCH_OUTPUT.md
      - 07_RESEARCH_BLOCK.md
  step_2_collect_generated_sidecar_registry:
    source: promptworkflowsAPI.py
    generated_sidecars:
      - output/00_PROJECT_BOOTSTRAP.md
      - output/01_ARTIFACT_SINGLE_FILE.md
      - output/02_MULTI_FILE_SESSION.md
      - output/03_PROJECT_OPENER.md
      - output/04_STATE_BLOCK.md
      - output/05_SPLIT_SIGNAL.md
      - output/06_DIFF_OUTPUT.md
      - output/07_RESEARCH_BLOCK.md
      - output/08_TASK_CLOSURE.md
    execution_status: not_executed_inspected_as_source_only
  step_3_choose_primary_source:
    rule: prefer hand-authored canonical execution-control files over generated sidecars when the hand-authored file is stricter, newer in the integration route, or already accepted by execution-control appendices
  step_4_assign_canonicality:
    rule: canonical | variant | example | future_candidate | duplicate_or_rejected
  step_5_assign_route_status:
    rule: every family and source claim receives explicit route status before later scaffold consideration
  step_6_defer_scaffold_mutation:
    rule: all scaffold targets remain candidate-only until TASK-07 or later scaffold tasks
```

## 7. Template-family taxonomy

| Family class | Families | Primary decision |
|---|---|---|
| Session-entry templates | Project bootstrap, project opener. | Reconcile into one compact opener candidate; keep variants as examples. |
| Execution-state templates | JSON state block, manual/browser state block. | JSON state block is canonical; manual block is variant. |
| Atomic-task templates | Task payload, gate check, HALT/CLARIFY. | Canonical execution controls. |
| Output-write templates | File output, split signal, task closure. | Canonical where validated; split remains appendix protocol plus compact pointer candidate. |
| Research-output templates | Research output JSON, research block Markdown. | JSON is candidate canonical for schema-bound research; Markdown is variant/example. |
| Transport/session pointers | Patch chooser pointer, multi-file manifest pointer. | Future candidates because they require chooser or manifest discipline. |
| Generated sidecars | Sidecars emitted by `promptworkflowsAPI.py`. | Evidence only until reconciled with hand-authored templates. |

## 8. Runtime-template catalog table

| Family ID | Template family | Source files | Purpose | Canonicality | Route status | Scaffold target candidate | Appendix pointer | Drift risk | Notes |
|---|---|---|---|---|---|---|---|---|---|
| `RT-01` | Project bootstrap / project opener | `00_PROJECT_BOOTSTRAP.md`; `03_PROJECT_OPENER.md`; `promptworkflowsAPI.py` generated `00_PROJECT_BOOTSTRAP`, `03_PROJECT_OPENER` | Start constrained sessions with project, task, output type, constraints, state reference, and no scope expansion. | `future_candidate` | `scaffold_candidate` | Candidate compact opener in `TEMPLATES.md` only after deduplication. | This appendix §10.1 | Medium | Bootstrap is stronger on constraints; opener is stronger on session fields. Generated sidecars duplicate both. |
| `RT-02` | State block, JSON canonical and manual/browser variant | `02_STATE_BLOCK.md`; `04_STATE_BLOCK.md`; `promptworkflowsAPI.py` generated `04_STATE_BLOCK` | Replace chat-history inference with explicit state. | `canonical` for JSON; `variant` for manual/browser | `canonical_template_source`; `duplicate_or_variant` | Candidate compact state block in `TEMPLATES.md`. | This appendix §10.2 | Low if mode labels remain explicit | JSON source is canonical for controlled execution; manual Markdown is a browser/session variant. |
| `RT-03` | Task payload | `03_TASK_PAYLOAD.md` | Provide one atomic per-call task object with target, scope, constraints, and input refs. | `canonical` | `canonical_template_source` | Candidate compact task payload in `TEMPLATES.md`; mistake support for compound scope. | This appendix §10.3 | Low | Directly supports one atomic task per call and no directory scan without explicit refs. |
| `RT-04` | Gate check | `08_GATE_CHECK.md` | Verify task type, repeated scope, target, constraints, ambiguity, and readiness before execution. | `canonical` | `canonical_template_source` | Candidate compact gate in `TEMPLATES.md`. | This appendix §10.4 | Low | Server-call mechanics are implementation-specific; gate semantics are accepted execution control. |
| `RT-05` | HALT / CLARIFY control signals | `09_CONTROL_SIGNALS.md` | Stop or pause execution when constraints fail or ambiguity exists. | `canonical` | `canonical_template_source` | Candidate compact signal templates in `TEMPLATES.md`; mistake support for unsafe continuation. | This appendix §10.5 | Low | Log paths remain implementation-specific. |
| `RT-06` | File output | `05_FILE_OUTPUT.md`; `promptworkflowsAPI.py` generated `01_ARTIFACT_SINGLE_FILE` | Emit complete file-write content with scope proof and validation contract. | `canonical` for JSON file-output schema; `duplicate_or_rejected` for generated artifact block as canonical write protocol | `canonical_template_source`; `evidence_only_generated_templates` | Candidate compact file-output pointer in `TEMPLATES.md`. | This appendix §10.6 | Medium | Generated artifact block lacks fetch-back and is weaker than validated file-output schema. |
| `RT-07` | Split signal | `05_SPLIT_SIGNAL.md`; `promptworkflowsAPI.py` generated `05_SPLIT_SIGNAL` | Split long outputs at logical boundaries without summary substitution. | `variant` | `appendix_protocol` | Candidate compact split pointer in `TEMPLATES.md`. | This appendix §10.7 | Medium | Numeric token ceilings are runtime-dependent and must not become accepted doctrine. |
| `RT-08` | Task closure | `08_TASK_CLOSURE.md`; `promptworkflowsAPI.py` generated `08_TASK_CLOSURE` | Close a task with proof of output type, target, scope status, additions beyond scope, and next task. | `canonical` | `canonical_template_source` | Candidate compact closure template in `TEMPLATES.md`. | This appendix §10.8 | Low | Later scaffold must require fetch-back before closure is trusted. |
| `RT-09` | Research output JSON | `07_RESEARCH_OUTPUT.md` | Schema-bound research output with topic, format, depth, sources, scope, and recommendation gate. | `future_candidate` | `scaffold_candidate` | Candidate research-output template after overlap review. | This appendix §10.9 | Medium | Good structure, but research output may overlap existing scaffold templates. |
| `RT-10` | Research block Markdown | `07_RESEARCH_BLOCK.md`; `promptworkflowsAPI.py` generated `07_RESEARCH_BLOCK` | Human-readable research block for synthesis tasks. | `variant` | `duplicate_or_variant` | Candidate only if scaffold separates JSON and Markdown modes. | This appendix §10.10 | Medium | Avoid duplicate research templates unless mode distinction is required. |
| `RT-11` | Patch transport chooser pointer | `PROMPTFLOW_CONSTANT_FRAME_CONTROLLED_KB_INTEGRATION.md`; `APPENDIX_KB_CONSTANT_FAILURE_SOURCE_NOTES.md`; `APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md`; `promptworkflowsAPI.py` generated `06_DIFF_OUTPUT` | Point later templates to a chooser across full-body replacement, SEARCH/REPLACE, unified diff, and live edit. | `future_candidate` | `appendix_protocol` | Candidate compact edit-mode chooser pointer in `TEMPLATES.md` after patch appendix dependency. | This appendix §10.11 | High | Diff sidecar is not enough; chooser must prevent transport conflict. |
| `RT-12` | Multi-file session / manifest pointer | `PROMPTFLOW_CONSTANT_FRAME_CONTROLLED_KB_INTEGRATION.md`; `APPENDIX_KB_CONSTANT_FAILURE_SOURCE_NOTES.md`; `APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md`; `promptworkflowsAPI.py` generated `02_MULTI_FILE_SESSION` | Preserve manifest-first sequencing for multi-file work while maintaining one atomic file per execution step. | `future_candidate` | `appendix_protocol` | Candidate compact manifest pointer in `TEMPLATES.md`. | This appendix §10.12 | Medium | Pointer must not weaken one-atomic-task-per-call doctrine. |
| `RT-13` | Generated template sidecars from `promptworkflowsAPI.py` | `promptworkflowsAPI.py` generated sidecars `00` through `08` | Inventory generated runtime templates and compare them to hand-authored files. | `example` | `evidence_only_generated_templates` | No direct scaffold promotion; use as reconciliation evidence only. | This appendix §10.13 | High | The generator was inspected only and not executed. Sidecars are not canonical doctrine. |

## 9. Canonical / variant decision table

| Decision ID | Competing or related templates | Decision | Reason | Route status |
|---|---|---|---|---|
| `RTD-01` | `00_PROJECT_BOOTSTRAP.md` vs `03_PROJECT_OPENER.md` vs generated opener sidecars | Keep both hand-authored files as opener evidence; defer single scaffold opener until TASK-07. | Bootstrap controls response discipline; opener controls session fields; generated copies duplicate both. | `scaffold_candidate` |
| `RTD-02` | `02_STATE_BLOCK.md` vs `04_STATE_BLOCK.md` vs generated `04_STATE_BLOCK` | Make JSON state block canonical; keep manual Markdown as browser/manual variant. | JSON form is stricter and tied to state-read failure handling; manual variant is useful but weaker. | `canonical_template_source` + `duplicate_or_variant` |
| `RTD-03` | `03_TASK_PAYLOAD.md` vs generated absence | Treat hand-authored task payload as canonical. | It enforces atomic scope, input refs, target, constraints, and no directory scans. | `canonical_template_source` |
| `RTD-04` | `08_GATE_CHECK.md` vs generated absence | Treat hand-authored gate check as canonical. | It explicitly validates readiness and ambiguity before execution. | `canonical_template_source` |
| `RTD-05` | `09_CONTROL_SIGNALS.md` vs generated absence | Treat hand-authored HALT/CLARIFY as canonical. | It defines stop and pause behavior and blocks post-HALT continuation. | `canonical_template_source` |
| `RTD-06` | `05_FILE_OUTPUT.md` vs generated `01_ARTIFACT_SINGLE_FILE` | Use hand-authored file-output JSON as canonical; generated artifact block is duplicate/rejected for canonical file writes. | File-output schema has scope proof, full-path write, validation, and fetch-back concepts; artifact block lacks validation depth. | `canonical_template_source` + `duplicate_or_rejected` |
| `RTD-07` | `05_SPLIT_SIGNAL.md` vs generated `05_SPLIT_SIGNAL` | Treat split signal as appendix protocol and compact pointer candidate only. | The protocol is useful, but numeric limits and continuation mechanics are runtime-sensitive. | `appendix_protocol` |
| `RTD-08` | `08_TASK_CLOSURE.md` vs generated `08_TASK_CLOSURE` | Treat hand-authored closure as canonical but require fetch-back validation from controlling process. | Closure block is lightweight; validation proof must not be replaced by conversational completion. | `canonical_template_source` |
| `RTD-09` | `07_RESEARCH_OUTPUT.md` vs `07_RESEARCH_BLOCK.md` vs generated `07_RESEARCH_BLOCK` | Keep JSON research output as candidate canonical; keep Markdown block as variant/example. | They target different modes; scaffold should avoid duplicate entries unless mode split is explicit. | `scaffold_candidate` + `duplicate_or_variant` |
| `RTD-10` | Generated `06_DIFF_OUTPUT` vs patch transport chooser requirement | Reject generated diff output as standalone canonical transport doctrine; route to patch chooser. | Patch transport conflicts require a chooser and dry-run rules before scaffold use. | `future_candidate` |
| `RTD-11` | Generated `02_MULTI_FILE_SESSION` vs one-atomic-task doctrine | Retain manifest pointer as future candidate; do not promote multi-file execution as one task. | Manifest sequencing is useful only if it preserves one file per execution step. | `future_candidate` |
| `RTD-12` | Generated sidecars as a group vs hand-authored sources | Treat generated sidecars as evidence only. | Generated content may duplicate or weaken hand-authored constraints and was not executed. | `evidence_only_generated_templates` |

## 10. Source-by-source template notes

### 10.1 Project bootstrap / opener

- **Sources:** `00_PROJECT_BOOTSTRAP.md`, `03_PROJECT_OPENER.md`, generated `00_PROJECT_BOOTSTRAP`, generated `03_PROJECT_OPENER`.
- **Route status:** `scaffold_candidate` with `duplicate_or_variant` evidence.
- **Reconciliation:** Bootstrap contributes execution constraints such as one artifact per response, no scope expansion, and no explanatory text outside the artifact. Opener contributes project/session/task/output/state fields.
- **Decision:** Defer scaffold insertion until TASK-07 can create one compact opener or pointer without duplicating source pack wording.
- **Drift risk:** Medium, because generated text includes strict UI/output phrases that may be transport-specific.

### 10.2 State block

- **Sources:** `02_STATE_BLOCK.md`, `04_STATE_BLOCK.md`, generated `04_STATE_BLOCK`.
- **Route status:** `canonical_template_source` for JSON state; `duplicate_or_variant` for manual Markdown state.
- **Reconciliation:** JSON state block is canonical because it is parseable and tied to state-read failure behavior. Manual Markdown/YAML form is useful for browser/manual contexts only.
- **Decision:** Later `TEMPLATES.md` should include a compact canonical JSON state pointer and mention the manual variant only if scaffold room allows.
- **Drift risk:** Low if canonical/variant labels are preserved.

### 10.3 Task payload

- **Sources:** `03_TASK_PAYLOAD.md`.
- **Route status:** `canonical_template_source`.
- **Reconciliation:** No generated sidecar provides the same atomic payload schema; this hand-authored file controls the family.
- **Decision:** Promote only as compact candidate in TASK-07, with appendix pointer and no full schema dump.
- **Drift risk:** Low.

### 10.4 Gate check

- **Sources:** `08_GATE_CHECK.md`.
- **Route status:** `canonical_template_source`.
- **Reconciliation:** No generated sidecar provides an equivalent gate. The hand-authored source controls the family.
- **Decision:** Later scaffold template should preserve repeated scope, target, ambiguity status, and readiness flags.
- **Drift risk:** Low, except server-call mechanics should remain implementation-specific.

### 10.5 HALT / CLARIFY control signals

- **Sources:** `09_CONTROL_SIGNALS.md`.
- **Route status:** `canonical_template_source`.
- **Reconciliation:** No generated sidecar provides an equivalent stop-signal schema. Hand-authored source controls.
- **Decision:** Later scaffold should include compact HALT and CLARIFY forms and route unsafe continuation to `MISTAKES.md`.
- **Drift risk:** Low.

### 10.6 File output and generated artifact block

- **Sources:** `05_FILE_OUTPUT.md`, generated `01_ARTIFACT_SINGLE_FILE`.
- **Route status:** `canonical_template_source` for file-output; `duplicate_or_rejected` for artifact block as canonical file-write protocol.
- **Reconciliation:** The generated artifact block is useful as an example of single-file output shape, but it lacks the stronger validation and fetch-back boundary required by the integration promptflow.
- **Decision:** Keep generated artifact block as evidence only; later scaffold should prefer validated file-output schema and appendix pointer.
- **Drift risk:** Medium.

### 10.7 Split signal

- **Sources:** `05_SPLIT_SIGNAL.md`, generated `05_SPLIT_SIGNAL`.
- **Route status:** `appendix_protocol`.
- **Reconciliation:** Hand-authored and generated forms are materially aligned, but runtime limits and continuation mechanics are environment-specific.
- **Decision:** Later scaffold may include a compact split pointer. Do not promote specific token ceilings as accepted doctrine.
- **Drift risk:** Medium.

### 10.8 Task closure

- **Sources:** `08_TASK_CLOSURE.md`, generated `08_TASK_CLOSURE`.
- **Route status:** `canonical_template_source`.
- **Reconciliation:** Generated and hand-authored forms align on scope and next-task fields, but controlling promptflow adds stronger fetch-back closure requirements.
- **Decision:** Later scaffold should include closure as proof object and require fetch-back validation before success is claimed.
- **Drift risk:** Low.

### 10.9 Research output JSON

- **Sources:** `07_RESEARCH_OUTPUT.md`.
- **Route status:** `scaffold_candidate`.
- **Reconciliation:** JSON schema is stricter than Markdown research block, with explicit sources and recommendation gate.
- **Decision:** Candidate canonical research-output template after existing template overlap review in TASK-07.
- **Drift risk:** Medium.

### 10.10 Research block Markdown

- **Sources:** `07_RESEARCH_BLOCK.md`, generated `07_RESEARCH_BLOCK`.
- **Route status:** `duplicate_or_variant`.
- **Reconciliation:** Markdown block is useful for human-readable synthesis but duplicates research-output purpose.
- **Decision:** Keep as variant/example unless scaffold explicitly separates JSON and Markdown research modes.
- **Drift risk:** Medium.

### 10.11 Patch transport chooser pointer

- **Sources:** controlling promptflow, source notes, regression appendix, generated `06_DIFF_OUTPUT`.
- **Route status:** `future_candidate` and `appendix_protocol`.
- **Reconciliation:** Generated diff output is a transport example, not a chooser. The integration process requires a separate patch-transport appendix and later compact chooser pointer.
- **Decision:** Later scaffold should point to the patch-transport appendix rather than canonizing generated diff output.
- **Drift risk:** High if unified diff, SEARCH/REPLACE, full-body replacement, and live edit are promoted without a chooser.

### 10.12 Multi-file session / manifest pointer

- **Sources:** controlling promptflow, source notes, regression appendix, generated `02_MULTI_FILE_SESSION`.
- **Route status:** `future_candidate` and `appendix_protocol`.
- **Reconciliation:** Manifest-first sequencing is useful, but one atomic task per call remains the controlling doctrine.
- **Decision:** Later scaffold may include a compact manifest pointer that explicitly preserves one-file-at-a-time execution.
- **Drift risk:** Medium.

### 10.13 Generated template sidecars

- **Sources:** `promptworkflowsAPI.py`.
- **Route status:** `evidence_only_generated_templates`.
- **Generated sidecars inventoried:** `00_PROJECT_BOOTSTRAP`, `01_ARTIFACT_SINGLE_FILE`, `02_MULTI_FILE_SESSION`, `03_PROJECT_OPENER`, `04_STATE_BLOCK`, `05_SPLIT_SIGNAL`, `06_DIFF_OUTPUT`, `07_RESEARCH_BLOCK`, `08_TASK_CLOSURE`.
- **Reconciliation:** Generated sidecars overlap hand-authored files but do not include every canonical family. They omit task payload, gate check, control signal, file-output JSON, and research-output JSON canonical forms.
- **Decision:** Do not execute `promptworkflowsAPI.py`; do not promote generated sidecars as canonical doctrine. Use them as catalog evidence and sidecar-schema research candidates.
- **Drift risk:** High if generated files are treated as authoritative without hand-authored reconciliation.

## 11. Scaffold-candidate template mapping

All scaffold targets in this section are candidate-only. This appendix creates no scaffold mutations.

| Candidate ID | Family ID | Candidate scaffold target | Candidate compact entry shape | Required dependency before use | Status |
|---|---|---|---|---|---|
| `PW-CF-TPL-CAND-001` | `RT-01` | `TEMPLATES.md` | Project opener/bootstrap pointer with project, task, output type, constraints, and state ref. | TASK-07 scaffold update after this appendix is fetched back. | `candidate_only` |
| `PW-CF-TPL-CAND-002` | `RT-02` | `TEMPLATES.md` | Canonical JSON state block pointer; optional manual/browser variant note. | TASK-07; execution-control appendix. | `candidate_only` |
| `PW-CF-TPL-CAND-003` | `RT-03` | `TEMPLATES.md` | Atomic task payload template with scope, target, constraints, input refs. | TASK-07; regression examples for compound scope. | `candidate_only` |
| `PW-CF-TPL-CAND-004` | `RT-04` | `TEMPLATES.md` | Gate-check template with repeated scope, ambiguity, readiness. | TASK-07; execution-control appendix. | `candidate_only` |
| `PW-CF-TPL-CAND-005` | `RT-05` | `TEMPLATES.md` | HALT and CLARIFY compact signal templates. | TASK-07; execution-control appendix. | `candidate_only` |
| `PW-CF-TPL-CAND-006` | `RT-06` | `TEMPLATES.md` | Validated file-output pointer with complete content, scope proof, fetch-back dependency. | TASK-07; no generated artifact-block promotion. | `candidate_only` |
| `PW-CF-TPL-CAND-007` | `RT-07` | `TEMPLATES.md` | Split-required pointer with logical-boundary and no-summary rule. | TASK-07; runtime ceilings left unaccepted. | `candidate_only` |
| `PW-CF-TPL-CAND-008` | `RT-08` | `TEMPLATES.md` | Task-closure proof object pointer. | TASK-07; fetch-back validation retained. | `candidate_only` |
| `PW-CF-TPL-CAND-009` | `RT-09` / `RT-10` | `TEMPLATES.md` | Research-output template; decide JSON-only or JSON + Markdown variant. | TASK-07 overlap review. | `candidate_only` |
| `PW-CF-TPL-CAND-010` | `RT-11` | `TEMPLATES.md` | Patch transport chooser pointer, not standalone diff doctrine. | Patch-transport appendix dependency; TASK-07. | `candidate_only` |
| `PW-CF-TPL-CAND-011` | `RT-12` | `TEMPLATES.md` | Multi-file manifest pointer preserving one file per execution step. | TASK-07; regression examples. | `candidate_only` |
| `PW-CF-TPL-CAND-012` | `RT-13` | `LEARNING_QUEUE.md` | Candidate-only question for generated sidecar schema ownership. | TASK-11 after external/runtime questions are routed. | `candidate_only` |

## 12. Rejected or duplicate template handling

| Item | Handling | Reason | Route status |
|---|---|---|---|
| Generated `01_ARTIFACT_SINGLE_FILE` as canonical file-write template | Reject for canonical promotion; retain as example evidence. | Lacks the stronger validation and fetch-back discipline required by file-output and promptflow closure contracts. | `duplicate_or_rejected` |
| Generated `06_DIFF_OUTPUT` as universal edit protocol | Reject as standalone canonical doctrine; route to patch chooser. | Patch transport needs chooser reconciliation across edit modes. | `future_candidate` |
| Generated `04_STATE_BLOCK` as canonical state block | Keep as manual/browser variant only. | `02_STATE_BLOCK.md` is stricter and parseable as JSON. | `duplicate_or_variant` |
| `07_RESEARCH_BLOCK.md` as sole research template | Do not promote as sole canonical research output. | JSON research-output schema has stronger source and recommendation controls. | `duplicate_or_variant` |
| Dual project opener entries without reconciliation | Do not promote both separately. | Bootstrap and opener overlap; scaffold should stay compact. | `duplicate_or_variant` |
| Generated sidecars as accepted scaffold doctrine | Reject direct promotion. | Generated files are evidence only and were not executed or validated as canonical. | `evidence_only_generated_templates` |
| Runtime/model/platform claims embedded in templates | Do not promote. | Runtime fields, token ceilings, model selection, stream flags, server paths, and log paths are adjacent-lane or future-research claims. | `adjacent_lane_runtime_claim` / `future_research` |

## 13. Future schema and sidecar questions

| Question ID | Question | Source basis | Candidate owner / destination | Status |
|---|---|---|---|---|
| `PW-CF-SIDE-Q-001` | Should runtime templates have machine-readable sidecars, or should Markdown templates remain the only durable source? | `promptworkflowsAPI.py` | Future `LEARNING_QUEUE.md` candidate; possible template-schema appendix. | `future_research` |
| `PW-CF-SIDE-Q-002` | If sidecars exist, what schema distinguishes canonical, variant, example, future candidate, and rejected templates? | This appendix reconciliation method. | `TEMPLATES.md` later compact pointer plus future schema work. | `future_research` |
| `PW-CF-SIDE-Q-003` | Which runtime details belong in prompts/workflows versus AI handling/routing or server implementation? | State/gate/control/file-output source files. | TASK-06 external-claim appendix and adjacent lane review. | `future_research` |
| `PW-CF-SIDE-Q-004` | Can generated templates be validated against hand-authored templates automatically before scaffold promotion? | `promptworkflowsAPI.py` generated registry. | Future validation tooling candidate. | `future_research` |
| `PW-CF-SIDE-Q-005` | Should research-output JSON and Markdown research block remain separate modes? | `07_RESEARCH_OUTPUT.md`; `07_RESEARCH_BLOCK.md`. | TASK-07 overlap review. | `future_research` |
| `PW-CF-SIDE-Q-006` | Should multi-file manifest be a template family or only a pointer to execution-control constraints? | Generated `02_MULTI_FILE_SESSION`; regression examples. | TASK-07 candidate review. | `future_research` |

## 14. External/runtime claim caution

This appendix does not promote runtime, model, provider, platform, token, stream, response-format, server-path, or log-path claims as accepted prompt/workflow doctrine.

```yaml
external_runtime_claim_caution:
  default_route_status: future_research
  adjacent_lane_runtime_claims:
    - model_selection_or_model_pinning_rules
    - temperature_or_sampling_requirements
    - max_token_or_output_ceiling_numbers
    - stream_false_or_response_format_JSON_requirements
    - server_side_parse_write_or_state_paths
    - provider_or_browser_platform_behavior
    - automatic_model_switching_or_downgrade_claims
  accepted_in_this_appendix:
    - template_family_inventory
    - generated_vs_hand_authored_reconciliation
    - canonicality_and_route_status_assignment
    - scaffold_candidate_mapping
  rejected_in_this_appendix:
    - accepted_runtime_law
    - accepted_model_platform_behavior_claim
    - scaffold_mutation
```

## 15. Validation checklist

```yaml
validation_checklist:
  path:
    file_exists: pass_required
    under_target_root: pass_required
    repository: leela-spec/MasterOfArts
    branch: main
  scope:
    task_id_repeated: TASK-05
    task_scope_repeated: Create a reconciled runtime-template catalog from generated and hand-authored templates without changing accepted scaffold doctrine.
    one_atomic_artifact: true
    additions_beyond_scope: none
  source_refs:
    intended_sources_referenced: pass_required
    promptworkflowsAPI_not_executed: pass_required
    generated_sidecars_cataloged_as_evidence_only: pass_required
  template_families:
    project_bootstrap_project_opener: cataloged
    state_block_json_and_manual_variant: cataloged
    task_payload: cataloged
    gate_check: cataloged
    halt_clarify: cataloged
    file_output: cataloged
    split_signal: cataloged
    task_closure: cataloged
    research_output_json: cataloged
    research_block_markdown: cataloged
    patch_transport_chooser_pointer: cataloged
    multi_file_manifest_pointer: cataloged
    generated_sidecars: cataloged
  claim_status:
    every_family_has_route_status: pass_required
    external_runtime_claims_future_or_adjacent_only: pass_required
    no_unverified_external_claim_promoted: pass_required
  scaffold:
    scaffold_candidates_only: pass_required
    essence_untouched: pass_required
    best_practices_untouched: pass_required
    mistakes_untouched: pass_required
    templates_untouched: pass_required
    learning_queue_untouched: pass_required
  closure:
    fetch_back_completed: pass_required
    next_task_identified: TASK-06 create APPENDIX_KB_EXTERNAL_CLAIM_VERIFICATION.md
```

## 16. Integration dependencies for later scaffold updates

| Later artifact | Dependency from this appendix | Allowed later use | Boundary |
|---|---|---|---|
| `TEMPLATES.md` | Runtime-template catalog table and candidate mapping. | Add compact pointers for state, task payload, gate, control signals, file output, split, closure, research output, patch chooser, and manifest pointer. | No generated sidecar direct promotion; no full appendix dump. |
| `BEST_PRACTICES.md` | Candidate-only execution flow implied by canonical families. | Add compact rule for explicit templates, reconciliation before promotion, and candidate-only generated sidecars. | No runtime/model/platform law. |
| `MISTAKES.md` | Duplicate/rejected handling and regression context. | Add compact mistakes for treating generated templates as canonical, duplicate template promotion, and closure without validation. | Do not add long examples; point to appendices. |
| `ESSENCE.md` | One compressed doctrine after scaffold tasks complete. | One sentence only after `TEMPLATES.md`, `MISTAKES.md`, and `BEST_PRACTICES.md` are verified. | Essence last; no schema. |
| `LEARNING_QUEUE.md` | Future sidecar/schema/runtime questions. | Add candidate-only entries for generated sidecars, runtime ownership, and external-claim verification. | Candidate-only; no accepted doctrine. |

## 17. TASK-05 closure scope record

```yaml
task_scope_record:
  task_id: TASK-05
  task_type: appendix_create
  scope: Create a reconciled runtime-template catalog from generated and hand-authored templates without changing accepted scaffold doctrine.
  target_file: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_RUNTIME_TEMPLATE_CATALOG.md
  output_format: markdown_file
  scaffold_mutation: none
  generated_templates_promoted_as_canonical: false
  external_runtime_claim_promotion: none
  next_suggested_task: TASK-06 create APPENDIX_KB_EXTERNAL_CLAIM_VERIFICATION.md
```
