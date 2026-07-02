---
promptflow_id: special_ops_constant_frame_controlled_kb_integration
class: controlling_process
surface: agent_kb_promptflow
quality: proposed
status: draft
created_at: 2026-05-06
owner: special_ops__prompts_workflows
validator: meta_ops
working_repo: leela-spec/MasterOfArts
target_repo: leela-spec/MasterOfArts
source_repo: leela-spec/MasterOfArts
target_branch: main
target_agent: special_ops__prompts_workflows
target_kb_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/
source_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/
realizes: appendices/APPENDIX_KB_CONSTANT_FAILURE_INTEGRATION_PROCESS.md
---

# Promptflow: Constant Frame Controlled KB Integration

## 1. Purpose

This promptflow operationalizes `appendices/APPENDIX_KB_CONSTANT_FAILURE_INTEGRATION_PROCESS.md`.

It creates a controlled process for turning the `NewResearchBecauseOfConstantFailure/` pack into durable KB artifacts while maintaining constant frame control across every task, file, patch, validation, and promotion decision.

The process has two responsibilities:

1. **Control the frame:** preserve repo boundary, target lane, source authority, artifact sequence, scaffold boundaries, and unresolved questions as explicit state instead of relying on conversational memory.
2. **Produce defining artifacts:** generate the appendices, templates, mistakes, best-practice rules, essence compression, and learning-queue entries needed to make the new failure research usable without promoting unverified claims.

## 2. Source authority

### 2.1 Required local source pack

Use the following source root as the primary new research input:

`OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/`

### 2.2 Required control sources

| Source | Use |
|---|---|
| `appendices/APPENDIX_KB_CONSTANT_FAILURE_INTEGRATION_PROCESS.md` | Ranking, routing, and artifact production intent. |
| `00_SYSTEM_BOOTSTRAP.md` | Execution contract, authority hierarchy, gate protocol, model/config caution. |
| `02_STATE_BLOCK.md` / `04_STATE_BLOCK.md` | Explicit state surface and state-keeper separation. |
| `03_TASK_PAYLOAD.md` | Atomic task payload and no-directory-scan rule. |
| `08_GATE_CHECK.md` | Pre-execution readiness gate. |
| `09_CONTROL_SIGNALS.md` | HALT and CLARIFY control signals. |
| `05_FILE_OUTPUT.md` | Validated file-write schema. |
| `08_TASK_CLOSURE.md` | Closure proof format. |
| `05_SPLIT_SIGNAL.md` / `02_MULTI_FILE_SESSION.md` | Split and multi-file sequencing. |
| `GPT_PATCH_WORKFLOW.md` / `06_DIFF_OUTPUT (1).md` | Patch transport options and failure handling. |
| `ConstantAIFailureAnalysis.md` | Problem framing and externally verified research leads only. |

### 2.3 Existing KB constraints

This promptflow inherits the architecture lock from `PROMPTFLOW_KB_BASE_BUILD.md`:

- F5 scaffold stays compact.
- Appendices hold deep evidence, examples, ranking, and operational protocols.
- `LEARNING_QUEUE.md` remains candidate-only.
- `ESSENCE.md` is updated last.
- No external or cross-lane claim is promoted without validation.

## 3. Constant frame control definition

A frame is the active, machine-checkable context that constrains one task.

A frame is valid only when all of the following remain explicit:

- **Repo frame:** `leela-spec/MasterOfArts` only.
- **Target frame:** `special_ops__prompts_workflows` only.
- **Path frame:** writes only under `OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/`.
- **Source frame:** reads only from listed source files unless the gate expands input refs intentionally.
- **Artifact frame:** one artifact or one closed patch set per task.
- **Promotion frame:** appendices first, scaffold second, essence last, learning queue candidate-only.
- **Authority frame:** local repo source pack and accepted KB constraints outrank chat memory and unverified external claims.
- **Stop frame:** ambiguity, stale state, scope creep, failed validation, wrong repo, or unsupported promotion emits HALT/CLARIFY.

## 4. Frame block schema

Every execution task must start from a frame block equivalent to this schema.

```yaml
FRAME_BLOCK:
  frame_id: special_ops_constant_frame_controlled_kb_integration
  session_id: YYYY-MM-DD-seq
  active_task_id: TASK-XX
  active_agent_role: planner | executor | verifier | state_keeper
  working_repo: leela-spec/MasterOfArts
  target_repo: leela-spec/MasterOfArts
  target_branch: main
  target_agent: special_ops__prompts_workflows
  target_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/
  source_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/
  immutable_locks:
    - no_cross_repo_targeting
    - no_apex_write_or_runtime_target
    - one_atomic_task_per_call
    - no_implicit_state_inference
    - no_directory_scan_unless_input_refs_authorize_it
    - appendices_before_scaffold
    - scaffold_compact
    - essence_last
    - learning_queue_candidate_only
  active_constraints:
    - output_must_match_task_type
    - scope_must_be_repeated_in_gate_and_closure
    - source_claims_must_have_route_status
    - external_claims_future_research_only_until_verified
    - fetch_back_every_written_file
  allowed_write_roots:
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/
  forbidden_promotions:
    - unverified model/platform claims as accepted doctrine
    - AI routing/runtime config as prompt-workflow governance
    - global KB placement authority
    - QA severity authority
  completed_tasks: []
  open_items:
    - create execution-control appendix
    - create source-notes appendix
    - create patch-transport appendix
    - create regression examples appendix
    - create runtime template catalog appendix
    - update templates with compact pointers
    - update mistakes with compact failure patterns
    - update best practices with compact operating rules
    - update essence last
    - update learning queue with unresolved research candidates
```

## 5. Task payload schema

Every task must be represented as an atomic task payload.

```yaml
TASK_PAYLOAD:
  id: TASK-XX
  type: file_write | file_update | diff_patch | appendix_create | scaffold_update | learning_queue_update | verification
  target_file: relative/path/from/repo/root.md
  scope: one-sentence atomic task with no compound AND/THEN instruction
  output_format: markdown_file | replacement_patch | verification_report | closure_block
  input_refs:
    - exact/source/file.md
  constraints:
    - inherit_from_FRAME_BLOCK
    - no_additions_beyond_scope
    - preserve_existing_valid_doctrine
  forbidden:
    - directory_wide_unspecified_scan
    - unverified_claim_promotion
    - scaffold_density_overload
```

Reject the payload before execution if the scope is compound, the target file is outside the target root, input refs are missing, or the task attempts to promote external/runtime claims into accepted prompt-workflow doctrine.

## 6. Gate-check protocol

Before executing any task, produce and verify a gate check.

```yaml
GATE_CHECK:
  task_id: TASK-XX
  agent_role: planner | executor | verifier | state_keeper
  task_type_understood: file_write | file_update | diff_patch | appendix_create | scaffold_update | learning_queue_update | verification
  scope_understood: repeat task scope verbatim
  target_file: relative/path/from/repo/root.md
  input_refs_confirmed:
    - exact/source/file.md
  active_constraints:
    - inherited constraints from FRAME_BLOCK
  ambiguity_detected: false
  ready_to_execute: true
```

### Gate failure rules

| Condition | Required signal |
|---|---|
| Wrong repo or wrong target root | `HALT: wrong_repo_context` |
| Missing or stale state | `HALT: state_read_failure` |
| Compound task scope | `HALT: split_task_required` |
| Ambiguous target or source authority | `CLARIFY` |
| Scaffold change before appendix support exists | `HALT: promotion_gate_failed` |
| Unverified external model/platform claim promoted as doctrine | `HALT: external_claim_unverified` |
| Patch preimage not found | `HALT: patch_check_fail` |
| Output exceeds safe size | `HALT: split_required` |

## 7. Control signals

Use explicit control signals instead of continuing by interpretation.

```yaml
HALT:
  task_id: TASK-XX
  reason: wrong_repo_context | state_read_failure | split_task_required | promotion_gate_failed | external_claim_unverified | patch_check_fail | scope_exceeded | validation_failed
  detail: one-line machine-readable detail
  safe_state: true | false
  recovery: manual_review_required | retry_with_corrected_payload | split_task | validate_source | create_appendix_first
```

```yaml
CLARIFY:
  task_id: TASK-XX
  question: one blocking question only
  blocking: exact ambiguous field
  options:
    - option_a
    - option_b
```

## 8. Defining artifact production map

The following artifacts define the controlled integration. They must be produced in order.

| Order | Artifact | Class | Purpose | Promotion dependency |
|---:|---|---|---|---|
| 0 | `PROMPTFLOW_CONSTANT_FRAME_CONTROLLED_KB_INTEGRATION.md` | controlling promptflow | Defines frame control, task routing, production sequence, and gates. | none |
| 1 | `appendices/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md` | appendix | Consolidates system bootstrap, state block, task payload, gate check, control signals, file output, split, and closure contracts. | prerequisite for template/scaffold updates |
| 2 | `appendices/APPENDIX_KB_CONSTANT_FAILURE_SOURCE_NOTES.md` | appendix | Records source-by-source interpretation, duplicate handling, verification status, and route decisions. | prerequisite for source-authority validation |
| 3 | `appendices/APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md` | appendix | Defines when to use full-body replacement, SEARCH/REPLACE, unified diff, or live-edit instruction. | prerequisite for patch/write template updates |
| 4 | `appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md` | appendix | Provides regression cases for state drift, compound scope, false completion, patch mismatch, split failure, and HALT/CLARIFY. | prerequisite for accepted mistake updates |
| 5 | `appendices/APPENDIX_KB_RUNTIME_TEMPLATE_CATALOG.md` | appendix | Reconciles hand-authored research templates and `promptworkflowsAPI.py` generated templates. | prerequisite for template consolidation |
| 6 | `appendices/APPENDIX_KB_EXTERNAL_CLAIM_VERIFICATION.md` | future/research appendix | Tracks external model/platform claims that need verification before doctrine promotion. | blocks external claim promotion |
| 7 | `TEMPLATES.md` | scaffold | Adds compact frame block, task payload, gate check, control signal, file output, split, and closure templates with appendix pointers. | requires artifacts 1-5 |
| 8 | `MISTAKES.md` | scaffold | Adds failure patterns: implicit state, compound scope, validation bypass, no-op completion, post-HALT continuation, and patch preimage mismatch. | requires artifacts 1, 3, 4 |
| 9 | `BEST_PRACTICES.md` | scaffold | Adds compact rules for explicit frame control, atomic payloads, gate checks, verified output, and deferred research routing. | requires artifacts 1-5 |
| 10 | `ESSENCE.md` | scaffold | Adds one compressed doctrine sentence and appendix pointer only. | last scaffold mutation |
| 11 | `LEARNING_QUEUE.md` | candidate surface | Captures model pinning, API runtime enforcement, state-keeper architecture, and external claim verification as candidates. | after scaffold updates |

## 9. Execution task queue

```yaml
TASK_QUEUE:
  - id: TASK-00
    type: verification
    target_file: PROMPTFLOW_CONSTANT_FRAME_CONTROLLED_KB_INTEGRATION.md
    scope: Verify the controlling promptflow exists under the target KB root and inherits the constant-failure integration appendix.
    input_refs:
      - appendices/APPENDIX_KB_CONSTANT_FAILURE_INTEGRATION_PROCESS.md

  - id: TASK-01
    type: appendix_create
    target_file: appendices/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md
    scope: Create the execution-control appendix from the source pack contracts without promoting external model claims.
    input_refs:
      - NewResearchBecauseOfConstantFailure/00_SYSTEM_BOOTSTRAP.md
      - NewResearchBecauseOfConstantFailure/02_STATE_BLOCK.md
      - NewResearchBecauseOfConstantFailure/03_TASK_PAYLOAD.md
      - NewResearchBecauseOfConstantFailure/08_GATE_CHECK.md
      - NewResearchBecauseOfConstantFailure/09_CONTROL_SIGNALS.md
      - NewResearchBecauseOfConstantFailure/05_FILE_OUTPUT.md
      - NewResearchBecauseOfConstantFailure/05_SPLIT_SIGNAL.md
      - NewResearchBecauseOfConstantFailure/08_TASK_CLOSURE.md

  - id: TASK-02
    type: appendix_create
    target_file: appendices/APPENDIX_KB_CONSTANT_FAILURE_SOURCE_NOTES.md
    scope: Create source notes that map every new research file to route, evidence strength, drift risk, and verification status.
    input_refs:
      - NewResearchBecauseOfConstantFailure/*
      - appendices/APPENDIX_KB_CONSTANT_FAILURE_INTEGRATION_PROCESS.md

  - id: TASK-03
    type: appendix_create
    target_file: appendices/APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md
    scope: Create a patch-transport appendix that selects between full-body replacement, SEARCH/REPLACE, unified diff, and live-edit instruction.
    input_refs:
      - NewResearchBecauseOfConstantFailure/GPT_PATCH_WORKFLOW.md
      - NewResearchBecauseOfConstantFailure/06_DIFF_OUTPUT (1).md
      - NewResearchBecauseOfConstantFailure/SOURCE_CONFLICT_REPORT.md

  - id: TASK-04
    type: appendix_create
    target_file: appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md
    scope: Create regression examples that test frame drift, implicit state, compound scope, patch failure, split failure, and false completion.
    input_refs:
      - NewResearchBecauseOfConstantFailure/02_STATE_BLOCK.md
      - NewResearchBecauseOfConstantFailure/03_TASK_PAYLOAD.md
      - NewResearchBecauseOfConstantFailure/08_GATE_CHECK.md
      - NewResearchBecauseOfConstantFailure/09_CONTROL_SIGNALS.md
      - NewResearchBecauseOfConstantFailure/08_TASK_CLOSURE.md

  - id: TASK-05
    type: appendix_create
    target_file: appendices/APPENDIX_KB_RUNTIME_TEMPLATE_CATALOG.md
    scope: Create a reconciled runtime-template catalog from generated and hand-authored templates without changing accepted scaffold doctrine.
    input_refs:
      - NewResearchBecauseOfConstantFailure/promptworkflowsAPI.py
      - NewResearchBecauseOfConstantFailure/07_RESEARCH_OUTPUT.md
      - NewResearchBecauseOfConstantFailure/07_RESEARCH_BLOCK.md

  - id: TASK-06
    type: appendix_create
    target_file: appendices/APPENDIX_KB_EXTERNAL_CLAIM_VERIFICATION.md
    scope: Create a future-research verification ledger for external model and platform behavior claims.
    input_refs:
      - NewResearchBecauseOfConstantFailure/ConstantAIFailureAnalysis.md

  - id: TASK-07
    type: scaffold_update
    target_file: TEMPLATES.md
    scope: Add compact constant-frame-control templates with appendix pointers.
    input_refs:
      - appendices/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md
      - appendices/APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md
      - appendices/APPENDIX_KB_RUNTIME_TEMPLATE_CATALOG.md

  - id: TASK-08
    type: scaffold_update
    target_file: MISTAKES.md
    scope: Add compact failure patterns for implicit state, compound scope, failed validation bypass, false completion, and unsafe continuation.
    input_refs:
      - appendices/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md
      - appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md

  - id: TASK-09
    type: scaffold_update
    target_file: BEST_PRACTICES.md
    scope: Add compact best practices for explicit frame control, atomic execution, gate checks, verified outputs, and research routing.
    input_refs:
      - appendices/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md
      - appendices/APPENDIX_KB_CONSTANT_FAILURE_SOURCE_NOTES.md
      - appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md

  - id: TASK-10
    type: scaffold_update
    target_file: ESSENCE.md
    scope: Add one compressed constant-frame-control doctrine sentence and appendix pointer.
    input_refs:
      - BEST_PRACTICES.md
      - MISTAKES.md
      - TEMPLATES.md
      - appendices/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md

  - id: TASK-11
    type: learning_queue_update
    target_file: LEARNING_QUEUE.md
    scope: Add candidate-only entries for unresolved runtime, state-keeper, model-behavior, and verification research.
    input_refs:
      - appendices/APPENDIX_KB_EXTERNAL_CLAIM_VERIFICATION.md
      - appendices/APPENDIX_KB_RUNTIME_TEMPLATE_CATALOG.md
```

## 10. Promotion gates

### 10.1 Appendix gates

An appendix can be created when:

- source files are listed explicitly;
- route status is declared for every major claim;
- external claims are marked `future_research` unless verified;
- scaffold impact is listed but not applied;
- file is fetched back after write.

### 10.2 Scaffold gates

A scaffold file can be updated only when:

- relevant appendix exists;
- change is compact and navigational;
- no deep source dump enters scaffold;
- no external model/platform claim is accepted as doctrine;
- existing accepted IDs are preserved unless intentionally superseded;
- patch is verified by fetch-back.

### 10.3 Essence gate

`ESSENCE.md` can be updated only after `TEMPLATES.md`, `MISTAKES.md`, and `BEST_PRACTICES.md` have been updated and verified.

`ESSENCE.md` receives only:

- one compressed principle;
- one appendix pointer;
- no operational schema;
- no unverified external claim.

## 11. Constant-frame drift detector

Run this detector before and after every task.

```yaml
FRAME_DRIFT_DETECTOR:
  check_repo:
    expected: leela-spec/MasterOfArts
    on_fail: HALT wrong_repo_context
  check_target_root:
    expected_prefix: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/
    on_fail: HALT wrong_target_root
  check_task_atomicity:
    expected: one artifact or one closed patch set
    on_fail: HALT split_task_required
  check_source_refs:
    expected: explicit input_refs only
    on_fail: HALT source_authority_missing
  check_promotion_order:
    expected: appendices_before_scaffold_and_essence_last
    on_fail: HALT promotion_gate_failed
  check_claim_status:
    expected: accepted | candidate | future_research | evidence_only | rejected
    on_fail: HALT claim_status_missing
  check_external_claims:
    expected: future_research_until_verified
    on_fail: HALT external_claim_unverified
  check_output_validation:
    expected: fetch_back_or_diff_verified
    on_fail: HALT validation_failed
```

## 12. File output contract

Every artifact write must provide this closure metadata in the execution log or completion response.

```yaml
ARTIFACT_CLOSURE:
  task_id: TASK-XX
  output_type: file_write | file_update | diff_patch | verification
  target_file: relative/path/from/repo/root.md
  scope_respected: yes | no
  additions_beyond_scope: none | one-line explanation
  source_refs_used:
    - exact/source/file.md
  validation:
    fetch_back: pass | fail
    repo_root: pass | fail
    target_root: pass | fail
    claim_status: pass | fail
    promotion_gate: pass | fail
  next_suggested_task: TASK-XX or none
```

## 13. Verification pass

After each write or patch:

1. Fetch back the written file from `main` or the active branch.
2. Confirm it lives under the target KB root.
3. Confirm it references the intended source files.
4. Confirm it did not mutate unrelated governance or cross-lane doctrine.
5. Confirm external claims are not marked accepted unless separately verified.
6. Confirm the task closure matches the original scope.
7. Update the frame state through the state-keeper role only.

## 14. State-keeper rule

The executor never mutates the frame directly.

After a successful task closure, the state-keeper role appends a frame update:

```yaml
FRAME_STATE_UPDATE:
  completed_task: TASK-XX
  written_or_updated_file: relative/path/from/repo/root.md
  validation_status: pass | fail
  next_task: TASK-YY | none
  open_items_delta:
    remove:
      - completed item
    add:
      - newly discovered candidate or blocker
  halt_log_delta: none | halt_id
```

If state cannot be updated safely, the next task must not start.

## 15. Completion condition

This promptflow is complete only when:

- all required appendices are created or explicitly deferred;
- scaffold updates have appendix evidence and pass promotion gates;
- `ESSENCE.md` is updated last, if updated at all;
- `LEARNING_QUEUE.md` contains unresolved cross-lane and external-claim research as candidates only;
- every touched file has been fetched back;
- no write occurred outside the target KB root;
- final closure reports all artifacts, statuses, and remaining future-research items.

## 16. Machine-readable execution lock

```yaml
accepted_target:
  promptflow_id: special_ops_constant_frame_controlled_kb_integration
  working_repo: leela-spec/MasterOfArts
  target_repo: leela-spec/MasterOfArts
  source_repo: leela-spec/MasterOfArts
  branch: main
  target_agent: special_ops__prompts_workflows
  target_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/
  source_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/
  realizes: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_CONSTANT_FAILURE_INTEGRATION_PROCESS.md
forbidden_targets:
  - leela-spec/apexai-os-meta
  - global governance files outside this KB lane
  - runtime model routing files outside this KB lane
execution_contract:
  one_task_per_call: true
  explicit_frame_required: true
  gate_check_required: true
  halt_or_clarify_on_ambiguity: true
  fetch_back_required: true
  scaffold_density_limit: compact_only
  essence_last: true
```
