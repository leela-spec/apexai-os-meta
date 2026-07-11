---
class: appendix
role: EXECUTION_CONTROL_CONTRACTS
surface: agent_kb_appendix
quality: proposed
scope: agent
purpose: consolidate execution-control contracts for constant-frame prompt/workflow integration without promoting unverified external or runtime-platform claims
status: created
created_at: 2026-05-06
owner: special_ops__prompts_workflows
validator: meta_ops
target_agent: special_ops__prompts_workflows
target_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/
source_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/
source_refs:
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/PROMPTFLOW_CONSTANT_FRAME_CONTROLLED_KB_INTEGRATION.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_CONSTANT_FAILURE_INTEGRATION_PROCESS.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/00_SYSTEM_BOOTSTRAP.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/02_STATE_BLOCK.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/03_TASK_PAYLOAD.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/08_GATE_CHECK.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/09_CONTROL_SIGNALS.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/05_FILE_OUTPUT.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/05_SPLIT_SIGNAL.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/08_TASK_CLOSURE.md
---

# APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS

## 1. Purpose

This appendix consolidates the execution-control contracts required by the constant-frame controlled KB integration process for `special_ops__prompts_workflows`.

Its purpose is to retain detailed operational schemas in an appendix layer so later scaffold updates can stay compact. It records source-local execution controls as reusable prompt/workflow governance while keeping runtime, model-routing, platform, and externally sourced claims out of accepted doctrine until independently verified.

## 2. Scope and authority lock

```yaml
scope_lock:
  working_repo: leela-spec/MasterOfArts
  target_repo: leela-spec/MasterOfArts
  target_branch: main
  target_agent: special_ops__prompts_workflows
  target_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/
  source_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/
  artifact_class: appendix
  scaffold_files_untouched_by_this_appendix:
    - ESSENCE.md
    - BEST_PRACTICES.md
    - MISTAKES.md
    - TEMPLATES.md
    - LEARNING_QUEUE.md
```

### 2.1 Source usage ledger

| Source | Used for | Route status |
|---|---|---|
| `PROMPTFLOW_CONSTANT_FRAME_CONTROLLED_KB_INTEGRATION.md` | Frame definition, task queue, promotion gates, closure requirements. | `accepted_for_this_appendix` |
| `appendices/APPENDIX_KB_CONSTANT_FAILURE_INTEGRATION_PROCESS.md` | Ranking and route decisions for execution controls. | `accepted_for_this_appendix` |
| `NewResearchBecauseOfConstantFailure/00_SYSTEM_BOOTSTRAP.md` | Execution contract, authority hierarchy, gate protocol, runtime caution surface. | `split: accepted_execution_control + adjacent_lane_runtime_claims` |
| `NewResearchBecauseOfConstantFailure/02_STATE_BLOCK.md` | Explicit state block schema and state-keeper boundary. | `accepted_execution_control` |
| `NewResearchBecauseOfConstantFailure/03_TASK_PAYLOAD.md` | Atomic task payload schema and no-directory-scan rule. | `accepted_execution_control` |
| `NewResearchBecauseOfConstantFailure/08_GATE_CHECK.md` | Pre-execution gate schema and failure routing. | `accepted_execution_control` |
| `NewResearchBecauseOfConstantFailure/09_CONTROL_SIGNALS.md` | HALT and CLARIFY signal schemas. | `accepted_execution_control` |
| `NewResearchBecauseOfConstantFailure/05_FILE_OUTPUT.md` | Validated file-output schema and server write protocol. | `accepted_execution_control` |
| `NewResearchBecauseOfConstantFailure/05_SPLIT_SIGNAL.md` | Split-required protocol for output ceiling risk. | `accepted_execution_control` |
| `NewResearchBecauseOfConstantFailure/08_TASK_CLOSURE.md` | Task closure proof object. | `accepted_execution_control` |

### 2.2 Claim status legend

| Status | Meaning | Promotion boundary |
|---|---|---|
| `accepted_execution_control` | Source-local prompt/workflow rule that can be reused without relying on external platform claims. | May support later compact scaffold rule or template after promotion gate. |
| `appendix_protocol` | Detailed operational procedure retained here because it is too dense for scaffold. | Reference from scaffold; do not inline in full. |
| `adjacent_lane_runtime_claim` | Runtime, server, API, model-routing, token, streaming, or response-format rule that may belong to AI handling/routing or platform implementation. | Do not promote as accepted prompt/workflow doctrine from this appendix alone. |
| `future_research` | External, model-behavior, platform-behavior, or unverifiable claim requiring independent validation. | Candidate only until verified in a future research appendix. |
| `rejected_for_promotion` | Claim conflicts with scope, target root, or authority boundaries. | Do not promote. |

## 3. Authority hierarchy

The source pack defines an authority hierarchy to prevent agent reasoning from overriding explicit system, state, or task constraints. This appendix accepts the pattern as prompt/workflow execution control, not as a global platform implementation requirement.

```yaml
authority_hierarchy_contract:
  L0_system_prompt:
    role: immutable execution policy for the current controlled task
    mutability: none during task execution
    route_status: accepted_execution_control
  L1_state_block:
    role: explicit continuity surface injected for the task
    mutability: read_only_for_executor
    route_status: accepted_execution_control
  L2_task_payload:
    role: atomic instruction object for one task
    mutability: read_only_for_executor
    route_status: accepted_execution_control
  L3_agent_reasoning:
    role: local reasoning only
    mutability: internal
    allowed_to_override_L0_L2: false
    route_status: accepted_execution_control
```

### 3.1 Runtime/model caution

`00_SYSTEM_BOOTSTRAP.md` includes concrete runtime and model-configuration fields. This appendix records them only as adjacent-lane or future-research material:

| Source claim class | Examples from source pack | Route status | Handling rule |
|---|---|---|---|
| Runtime environment | Server-side/API-native execution environment. | `adjacent_lane_runtime_claim` | Keep out of accepted scaffold doctrine unless validated by the owning runtime lane. |
| Model selection | Model pinning and avoiding ambiguous model aliases. | `future_research` / `adjacent_lane_runtime_claim` | Track as candidate for AI handling/routing; do not harden here. |
| Generation parameters | Temperature, max tokens, streaming, response-format settings. | `adjacent_lane_runtime_claim` | May be referenced as runtime implementation question, not prompt/workflow governance law. |
| External model/platform behavior | Claims about model switching, downgrades, token ceilings, or drift mechanisms. | `future_research` | Must be verified before any doctrine promotion. |

## 4. State block contract

The state block replaces implicit reconstruction from chat history. The executor reads it as the active state surface and does not mutate it directly.

```yaml
state_block_contract:
  purpose: replace chat-history inference with explicit task state
  route_status: accepted_execution_control
  required_fields:
    project: string
    session_id: string
    active_agent: executor | planner | verifier | state_keeper
    active_task_id: string
    completed_tasks: list[string]
    last_written_file: string | null
    active_constraints: list[string]
    open_items: list[object]
    repo_path: string
    next_task: string | null
  executor_permissions:
    read_state: true
    infer_missing_state_from_chat_history: false
    mutate_state_directly: false
  state_keeper_permissions:
    update_after_successful_task_closure: true
    update_after_failed_or_ambiguous_task_without_control_signal: false
  failure_behavior:
    state_missing_or_unreadable: HALT
    stale_state_detected: HALT
    contradiction_with_task_payload: HALT_OR_CLARIFY
```

### 4.1 State discipline rules

- **Explicit continuity:** The current task state must be carried in a state block, not inferred from previous chat turns.
- **Executor boundary:** The executor can report task closure but cannot update persistent state directly.
- **State-keeper boundary:** State updates are a separate role action after validated task closure.
- **Stale-state handling:** Missing, stale, contradictory, or unreadable state produces `HALT: state_read_failure` rather than guessed execution.

## 5. Task payload contract

The task payload is the only accepted per-call instruction surface for an execution task. It must be atomic, scoped to one artifact or one closed patch set, and bound to explicit input references.

```yaml
task_payload_contract:
  route_status: accepted_execution_control
  required_fields:
    id: TASK-XX
    type: file_write | file_update | diff_patch | appendix_create | scaffold_update | learning_queue_update | verification
    target_file: relative/path/from/repo/root.md
    scope: one-sentence atomic task
    output_format: markdown_file | replacement_patch | verification_report | closure_block
    input_refs: list[string]
    constraints: list[string]
  validation_rules:
    one_atomic_task_per_call: true
    no_compound_and_then_scope: true
    no_directory_scan_unless_input_refs_authorize_it: true
    target_file_required_for_write_tasks: true
    target_file_must_be_under_target_root: true
    source_refs_must_be_explicit: true
    forbidden_scope_expansion: true
  reject_before_execution_when:
    - scope_is_compound
    - target_file_outside_target_root
    - input_refs_missing
    - task_promotes_unverified_external_or_runtime_claims
    - task_requires_scaffold_update_before_appendix_support
```

### 5.1 Atomicity boundary

A task is atomic when it has exactly one target file or one closed patch set, a single task type, one scope sentence, and a finite list of source refs. Compound tasks are split before execution.

## 6. Gate-check contract

Every task must pass a pre-execution gate before content generation or file mutation. The gate repeats the task scope and confirms target, role, constraints, ambiguity status, and readiness.

```yaml
gate_check_contract:
  route_status: accepted_execution_control
  required_fields:
    task_id: TASK-XX
    agent_role: planner | executor | verifier | state_keeper
    task_type_understood: string
    scope_understood: exact_task_scope
    target_file: relative/path/from/repo/root.md | null
    input_refs_confirmed: list[string]
    active_constraints: list[string]
    ambiguity_detected: false
    ready_to_execute: true
  pass_condition:
    ambiguity_detected: false
    ready_to_execute: true
    target_file_under_target_root: true
    task_type_matches_payload: true
    scope_repeated_verbatim: true
  fail_behavior:
    ambiguity_detected_true: CLARIFY
    ready_to_execute_false: HALT
    wrong_repo_or_root: HALT
    missing_source_authority: HALT_OR_CLARIFY
    unsupported_promotion: HALT
```

### 6.1 TASK-01 gate record

```yaml
GATE_CHECK:
  task_id: TASK-01
  agent_role: executor
  task_type_understood: appendix_create
  scope_understood: Create the execution-control appendix from the source pack contracts without promoting external model claims.
  target_file: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md
  ambiguity_detected: false
  ready_to_execute: true
```

## 7. HALT and CLARIFY control signals

HALT and CLARIFY are stop controls. They replace guessing, scope expansion, unsafe continuation, and silent failure.

### 7.1 HALT contract

```yaml
halt_contract:
  route_status: accepted_execution_control
  signal: HALT
  required_fields:
    task_id: TASK-XX
    reason: wrong_repo_context | state_read_failure | split_task_required | promotion_gate_failed | external_claim_unverified | patch_check_fail | scope_exceeded | validation_failed
    detail: one-line machine-readable detail
    safe_state: true | false
    recovery: manual_review_required | retry_with_corrected_payload | split_task | validate_source | create_appendix_first
  required_behavior:
    stop_downstream_execution: true
    avoid_partial_success_claim: true
    log_or_report_failure: true
```

### 7.2 CLARIFY contract

```yaml
clarify_contract:
  route_status: accepted_execution_control
  signal: CLARIFY
  required_fields:
    task_id: TASK-XX
    question: one_blocking_question_only
    blocking: exact_ambiguous_field
    options: list[string]
  required_behavior:
    pause_task_queue: true
    avoid_guessing: true
    resume_only_after_operator_answer: true
```

### 7.3 Control-signal routing table

| Condition | Signal | Route status |
|---|---|---|
| Wrong repo, wrong target root, or cross-repo target attempt. | `HALT: wrong_repo_context` | `accepted_execution_control` |
| Missing, unreadable, stale, or contradictory state. | `HALT: state_read_failure` | `accepted_execution_control` |
| Compound scope or multiple artifacts in one task. | `HALT: split_task_required` | `accepted_execution_control` |
| Scaffold mutation before appendix evidence exists. | `HALT: promotion_gate_failed` | `accepted_execution_control` |
| External/runtime/platform claim promoted as accepted doctrine without verification. | `HALT: external_claim_unverified` | `accepted_execution_control` |
| Patch preimage or validation check fails. | `HALT: patch_check_fail` or `HALT: validation_failed` | `accepted_execution_control` |
| Ambiguous target, source authority, or operator intent. | `CLARIFY` | `accepted_execution_control` |

## 8. File-output contract

Write tasks must produce a complete, validated file output object or equivalent write operation. The write is valid only when scope is confirmed, content is complete, and validation passes before mutation.

```yaml
file_output_contract:
  route_status: accepted_execution_control
  applies_to:
    - file_write
    - file_update
    - appendix_create
  required_fields:
    output_type: file_write | file_update
    task_id: TASK-XX
    filename: string
    repo_path: string
    full_path: string
    scope_confirmed: exact_task_scope
    content: complete_file_content
    line_count: integer
    scope_respected: true
    additions_beyond_scope: null
  server_write_protocol:
    - parse_output
    - validate_scope_respected_true
    - validate_additions_beyond_scope_null
    - validate_target_root
    - write_content
    - fetch_back_written_file
    - verify_content_and_claim_status
  fail_behavior:
    validation_fail: HALT
    incomplete_content: HALT
    target_root_mismatch: HALT
```

### 8.1 File-output boundaries

- **Complete content only:** A file write cannot substitute a summary for the requested artifact.
- **Scope proof required:** The output repeats the task scope and records whether it stayed within scope.
- **Fetch-back required:** A write is not closed until the written path is fetched back and checked.
- **No scaffold side effects:** Appendix creation cannot mutate F5 scaffold files.

## 9. Split-signal contract

The split signal is used only when a file cannot be safely emitted in one response or one write unit. It prevents output collapse, partial artifacts, and summary substitution.

```yaml
split_signal_contract:
  route_status: accepted_execution_control
  trigger: output_exceeds_safe_single_response_or_write_limit
  signal: SPLIT_REQUIRED
  required_fields:
    task_id: TASK-XX
    target_file: string
    estimated_parts: integer
    split_boundary_rule: logical_section_boundary
  continuation_rules:
    part_headers_required: true
    no_preamble_in_continuation: true
    no_summary_substitution: true
    no_new_sections_during_continuation: true
    final_part_has_end_marker: true
  fail_behavior:
    summary_substitution: HALT
    lost_scope: HALT
    missing_part: HALT
```

### 9.1 Split boundary

Split at complete logical sections. Never split inside frontmatter, schemas, tables, or code blocks unless the transport itself guarantees reassembly.

## 10. Task-closure contract

Task closure is a proof object, not a conversational signoff. It records what was produced, whether the original scope was respected, and which task should follow.

```yaml
task_closure_contract:
  route_status: accepted_execution_control
  trigger: after_validated_artifact_write_or_verification
  required_fields:
    task_id: TASK-XX
    output_type: file_write | file_update | diff_patch | verification
    target_file: string
    scope_respected: yes | no
    additions_beyond_scope: none | one-line explanation
    source_refs_used: list[string]
    validation:
      fetch_back: pass | fail
      repo_root: pass | fail
      target_root: pass | fail
      claim_status: pass | fail
      scaffold_untouched: pass | fail
    next_suggested_task: string | none
  forbidden_closure_behavior:
    - claiming_success_without_fetch_back
    - omitting_scope_status
    - hiding_validation_failure
    - adding unrelated recommendations
```

## 11. Frame-control enforcement rules

```yaml
frame_control_enforcement:
  route_status: accepted_execution_control
  repo_boundary:
    expected: leela-spec/MasterOfArts
    on_fail: HALT wrong_repo_context
  target_root_boundary:
    expected_prefix: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/
    on_fail: HALT wrong_target_root
  task_atomicity:
    expected: one artifact or one closed patch set
    on_fail: HALT split_task_required
  source_authority:
    expected: explicit input_refs only
    on_fail: HALT source_authority_missing
  promotion_order:
    expected: appendices_before_scaffold_and_essence_last
    on_fail: HALT promotion_gate_failed
  claim_status:
    expected: every major claim has route status
    allowed_values:
      - accepted_execution_control
      - appendix_protocol
      - adjacent_lane_runtime_claim
      - future_research
      - rejected_for_promotion
    on_fail: HALT claim_status_missing
  external_claims:
    expected: future_research_until_verified
    on_fail: HALT external_claim_unverified
  output_validation:
    expected: fetch_back_or_diff_verified
    on_fail: HALT validation_failed
```

## 12. Scaffold-promotion boundary

This appendix may support later scaffold updates, but it does not itself update scaffold files.

| Scaffold file | Allowed later use | Boundary |
|---|---|---|
| `TEMPLATES.md` | Compact pointers to state block, task payload, gate check, control signal, file output, split signal, and task closure templates. | Do not inline full appendix schemas. |
| `MISTAKES.md` | Compact failure patterns for implicit state, compound scope, unsafe continuation, failed validation bypass, and false completion. | Do not add source-pack dumps. |
| `BEST_PRACTICES.md` | Compact rules for explicit frame control, atomic payloads, gate checks, verified writes, and deferred external-claim routing. | Do not promote runtime/model claims as accepted doctrine. |
| `ESSENCE.md` | One compressed principle plus appendix pointer after other scaffold files are updated. | Essence last; no operational schemas. |
| `LEARNING_QUEUE.md` | Candidate-only entries for unresolved model, runtime, state-keeper, and external-claim questions. | No accepted doctrine; candidate-only. |

### 12.1 Promotion prerequisites

```yaml
promotion_prerequisites:
  scaffold_update_requires:
    - relevant_appendix_exists
    - compact_change_only
    - no_deep_schema_dump
    - existing_valid_doctrine_preserved
    - external_claims_not_promoted
    - fetch_back_after_write
  essence_update_requires:
    - templates_verified
    - mistakes_verified
    - best_practices_verified
    - one_sentence_only
    - appendix_pointer_only
```

## 13. External-claim handling rule

External model, runtime, platform, API behavior, and provider-behavior claims are not accepted by this appendix unless independently verified in an appropriate future research artifact.

```yaml
external_claim_handling:
  default_status: future_research
  applies_to:
    - model_auto_switching_or_downgrade_claims
    - provider_platform_behavior_claims
    - token_ceiling_claims
    - runtime_parameter_requirements
    - API_response_format_requirements
    - server_architecture_requirements
  allowed_current_handling:
    - record_as_candidate
    - mark_adjacent_lane_runtime_claim
    - route_to_external_claim_verification_appendix
    - route_to_ai_handling_or_runtime_owner
  forbidden_current_handling:
    - accepted_prompt_workflow_doctrine
    - scaffold_rule_without_verification
    - global_runtime_law_from_source_pack_alone
```

## 14. Validation checklist

Use this checklist after every execution-control artifact write or scaffold promotion task.

```yaml
validation_checklist:
  path:
    file_exists: pass_required
    under_target_root: pass_required
    repository: leela-spec/MasterOfArts
    branch: main
  scope:
    task_id_repeated: pass_required
    task_scope_repeated: pass_required
    one_atomic_artifact: pass_required
    no_additions_beyond_scope: pass_required
  source_refs:
    intended_sources_referenced: pass_required
    no_unlisted_source_dependency: pass_required
  claim_status:
    source_claims_have_route_status: pass_required
    external_claims_future_research_or_adjacent_lane: pass_required
    no_unverified_external_claim_promoted: pass_required
  scaffold:
    essence_untouched: pass_required
    best_practices_untouched: pass_required
    mistakes_untouched: pass_required
    templates_untouched: pass_required
    learning_queue_untouched: pass_required
  closure:
    fetch_back_completed: pass_required
    changed_file_set_checked: pass_required
    next_task_identified: pass_required
```

## 15. Next integration dependencies

| Dependency | Next task | Why it follows this appendix |
|---|---|---|
| Source-by-source route ledger | `TASK-02 create APPENDIX_KB_CONSTANT_FAILURE_SOURCE_NOTES.md` | Needed to map every source file to evidence strength, duplicate handling, drift risk, and verification status. |
| Patch transport rules | `TASK-03 create APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md` | Needed before compact edit-mode templates can be safely added to scaffold. |
| Regression examples | `TASK-04 create APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md` | Needed before accepted mistakes are updated with behavioral failure patterns. |
| Runtime template reconciliation | `TASK-05 create APPENDIX_KB_RUNTIME_TEMPLATE_CATALOG.md` | Needed before generated and hand-authored templates are merged or referenced from scaffold. |
| External-claim verification ledger | `TASK-06 create APPENDIX_KB_EXTERNAL_CLAIM_VERIFICATION.md` | Needed before any model/platform/runtime behavior claim can be promoted beyond candidate status. |

## 16. TASK-01 closure scope record

```yaml
task_scope_record:
  task_id: TASK-01
  task_type: appendix_create
  scope: Create the execution-control appendix from the source pack contracts without promoting external model claims.
  target_file: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md
  output_format: markdown_file
  scaffold_mutation: none
  external_claim_promotion: none
```
