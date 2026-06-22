# TEMPLATES

## Purpose

Accepted reusable Prompts Workflows templates.

This scaffold stores compact prompt/workflow structures. Detailed source evidence lives in `appendices/`.

## Template schema

```yaml
template_entry:
  id:
  status: accepted | deprecated
  use_when:
  template_body:
  evidence_refs:
  scores:
    EVD:
    IMP:
    RSK:
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due:
```

## Accepted templates

- id: `PW-TPL-001`
  status: accepted
  use_when: A bounded existing-file Markdown change is approved and exact diff transport may be fragile.
  template_body: |
    # One-File Live Edit Contract

    ## Target

    `<TARGET_FILE>`

    ## Mode

    `LIVE_EDIT_ONE_FILE`

    ## Authority

    Use only the approved patch intent for this file. Do not re-decide architecture, broaden scope, or edit neighboring files.

    ## Preflight

    - Confirm repo and branch.
    - Read the current target file.
    - Identify line-ending style if relevant.
    - Confirm no other tracked file needs to change.

    ## Edit rules

    - edit only `<TARGET_FILE>`
    - preserve unrelated content
    - make the smallest safe change or controlled full-body replacement if patch transport is unreliable
    - do not touch config unless explicitly named
    - do not apply out-of-mode improvements

    ## Verification

    - show changed file path
    - show real diff or read-back equivalent
    - verify the intended change is present
    - verify no unrelated file changed
    - stop after verification
  evidence_refs:
    - `appendices/SOURCE_CONFLICT_REPORT.md#pw-conflict-001`
    - `appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md#pw-info-007`
  scores:
    EVD: 5
    IMP: 5
    RSK: 5
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due: 2026-07-27

- id: `PW-TPL-002`
  status: accepted
  use_when: A reusable research or synthesis prompt must prevent generic detours and produce one operational output.
  template_body: |
    # Research Prompt Preflight Contract

    ## Target

    Produce `<NAMED_DELIVERABLE>` only.

    ## Frozen target frame

    - Primary objective: `<OBJECTIVE>`
    - Non-goals: `<NON_GOALS>`
    - Deferred: `<DEFERRED>`
    - Required output sections: `<SECTIONS>`

    ## Source authority

    | Source | Role | If missing |
    |---|---|---|
    | `<SOURCE_PATH>` | primary | report once and continue only with safe subset |

    Use raw/current source over summaries. If primary sources conflict, stop and surface the conflict.

    ## Detour budget

    | Topic | Budget | Required behavior |
    |---|---:|---|
    | locked assumptions | 0 | convert uncertainty into validation test |
    | excluded topics | 0 | do not research |
    | missing source | 1 check | report consequence |
    | generic background | 0 | omit unless required |

    ## Output discipline

    - one artifact only
    - hard rules before prose
    - separate certain, likely, open, and excluded
    - stop after output
  evidence_refs:
    - `appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md#pw-info-005`
  scores:
    EVD: 4
    IMP: 4
    RSK: 2
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due: 2026-07-27

- id: `PW-TPL-003`
  status: accepted
  use_when: Codex or another repo executor needs a bounded preflight before Git-visible work.
  template_body: |
    # Bounded Repo Execution Preflight

    ```yaml
    run_mode: <CREATE | PATCH_PATHS | CONTENT_DRAFT | VALIDATE | REPORT_ONLY>
    repo: <owner/name>
    branch: <branch-or-sha>
    target_root: <repo-relative-root>
    target_files:
      - <exact-repo-relative-path>
    allowed_actions:
      - <bounded-action>
    forbidden_actions:
      - scope widening
      - unrelated cleanup
      - hidden rewrite
      - config edit unless named
      - out-of-mode improvement application
    stop_conditions:
      - missing target path
      - authority conflict
      - need for undeclared file
      - patch drifts into rewrite
      - verification unavailable
    deliverable: <diff | full body | report | validation result>
    ```

    Execute one target file at a time. Verify with actual file state or Git-visible diff before reporting completion.
  evidence_refs:
    - `appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md#pw-info-007`
    - `appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md#pw-info-008`
  scores:
    EVD: 5
    IMP: 5
    RSK: 4
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due: 2026-07-27

- id: `PW-TPL-004`
  status: accepted
  use_when: A promptflow must stage multiple files or outputs without losing execution order.
  template_body: |
    # Promptflow Stage-Gate Skeleton

    ## 1. Repo and target lock

    - Working repo: `<REPO>`
    - Target root: `<TARGET_ROOT>`
    - Branch/ref: `<BRANCH_OR_SHA>`
    - Forbidden repos/paths: `<FORBIDDEN>`

    ## 2. Source lock

    - Primary index: `<INDEX>`
    - Required source slice: `<SOURCES>`
    - Evidence-only material: `<EVIDENCE_ONLY>`
    - Excluded material: `<EXCLUDED>`

    ## 3. Plausibility check

    - coverage
    - role fit
    - duplication
    - gap risk
    - authority risk

    Stop if material gap remains unresolved.

    ## 4. Build order

    1. appendices or evidence ledgers
    2. ranking ledger
    3. candidate ledger
    4. anti-drift/conflict reports
    5. scaffold files
    6. compression/essence file last

    ## 5. Verification

    - fetch back every written file
    - verify target paths
    - verify forbidden paths absent
    - verify scaffold density
    - report commit(s)
  evidence_refs:
    - `appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md#pw-info-009`
    - `appendices/SOURCE_CONFLICT_REPORT.md#pw-conflict-002`
  scores:
    EVD: 4
    IMP: 4
    RSK: 4
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due: 2026-07-27

- id: `PW-TPL-005`
  status: accepted
  use_when: Work is handed to a new chat, agent, or execution lane.
  template_body: |
    # Clean Handoff

    ## What is being continued

    `<BOUND_WORKSTREAM>`

    ## Settled decisions

    - `<DECISION_1>`
    - `<DECISION_2>`

    ## Authority stack

    1. `<PRIMARY_SOURCE>`
    2. `<SECONDARY_SOURCE>`
    3. `<BACKGROUND_SOURCE>`

    ## Do not redo

    - `<NON_REDO_ITEM>`

    ## Exact next job

    `<NEXT_ACTION>`

    ## Required inputs

    - `<INPUT_1>`

    ## Risks and holds

    - `<RISK_OR_HOLD>`

    ## Success condition

    `<SUCCESS_CONDITION>`
  evidence_refs:
    - `appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md#pw-info-010`
    - `appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#safeguard-f--handoff-reset`
  scores:
    EVD: 4
    IMP: 5
    RSK: 2
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due: 2026-07-27

- id: `PW-TPL-006`
  status: accepted
  use_when: A named promptflow or artifact may not fully express the operator's actual intended execution scope.
  template_body: |
    # User Intent / Artifact Contract Check

    Use this before declaring completion from file equality, existing-artifact status, or a narrow promptflow interpretation.

    ```yaml
    intent_contract_check:
      user_intent: <what the operator is asking to happen in plain language>
      named_promptflow_or_artifact: <exact named file, promptflow, or artifact>
      intended_execution_scope: <gap analysis | artifact manufacturing | scaffold update | apply | verify | other>
      exact_output_expected: <repo path, diff artifact path, report, or none>
      repo_write_expected: true | false
      scaffold_mutation_allowed: true | false
      appendix_only_allowed: true | false
      source_inputs_allowed:
        - <exact source path>
      source_inputs_forbidden:
        - broad governance reread
        - unrelated repo traversal
      open_questions: []
      stop_if_mismatch: true
    ```

    ## Execution rule

    - If user intent and the named artifact contract disagree, surface the mismatch.
    - If no blocking question remains, execute the operator's bounded intent.
    - Do not report `no-op` merely because a named artifact already exists.
    - Do not mutate scaffold files unless that mutation is explicitly allowed.
  evidence_refs:
    - `appendices/APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md#user-intent-versus-executed-promptflow-gap-analysis`
    - `appendices/PROMPTFLOW_PROMPTS_WORKFLOWS_BOUNDED_EXECUTION_GUARDRAILS.md#5-required-execution-contract`
    - `appendices/APPENDIX_KB_EXAMPLES.md#example-2-user-intent-versus-named-artifact-mismatch`
  scores:
    EVD: 5
    IMP: 5
    RSK: 3
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due: 2026-07-27

- id: `PW-TPL-007`
  status: accepted
  use_when: Choosing between SEARCH/REPLACE, unified diff, full final body, live-edit instruction, or no-patch/manual-review for Markdown or repo file changes.
  template_body: |
    # Edit Mode Chooser

    ```yaml
    edit_mode_chooser:
      target_file: <repo-relative-path>
      change_size: small | medium | large
      anchor_stability: stable | fragile | unknown
      markdown_transport_risk: low | medium | high
      exact_byte_patch_safe: true | false
      new_file: true | false
      recommended_mode: search_replace | unified_diff | full_final_body | live_edit_instruction | no_patch_manual_review
      forbidden_modes:
        - broad rewrite
        - hand edit after failed patch without operator approval
        - unrelated cleanup
      reason: <why this mode is safest>
    ```

    ## Decision rules

    - Use `search_replace` for localized edits when a live-file preimage can match exactly once and dry-run validation is available.
    - Use `unified_diff` for small bounded defects when anchors are stable and patch transport is reliable.
    - Use `full_final_body` for new files or controlled replacement when exact patch transport is riskier than replacing the whole target.
    - Use `live_edit_instruction` when a deterministic executor can safely edit one file but the chat/connector diff transport is fragile.
    - Use `no_patch_manual_review` when source authority, target anchors, promotion gates, or patch validation cannot be made safe.
    - If `git apply --check`, SEARCH/REPLACE dry-run, or equivalent validation fails during APPLY, stop and report rather than hand-editing.
  evidence_refs:
    - `appendices/SOURCE_CONFLICT_REPORT.md#pw-conflict-001`
    - `appendices/APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md#f5-scaffold-promotion-matrix`
    - `appendices/APPENDIX_KB_EXAMPLES.md#example-3-fragile-diff-to-live-edit-contract`
    - `appendices/APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md`
  scores:
    EVD: 5
    IMP: 5
    RSK: 5
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due: 2026-07-27

- id: `PW-TPL-008`
  status: accepted
  use_when: Capturing adjacent KB improvements discovered during a closed one-file or one-artifact execution phase.
  template_body: |
    # Improvement Opportunities Not Applied

    | Opportunity | Why noticed | Why not applied now | Suggested future target |
    |---|---|---|---|
    | `<IMPROVEMENT>` | `<EVIDENCE_OR_TRIGGER>` | current phase is `<PHASE>` and allowed target is `<TARGET>` | `<QUEUE_OR_FILE>` |

    ## Rule

    Capture the improvement without applying it. If the operator later authorizes it, create a new bounded contract or diff artifact for that target.
  evidence_refs:
    - `appendices/APPENDIX_KB_EXAMPLES.md#example-5-out-of-mode-improvement-capture`
    - `appendices/APPENDIX_KB_SOURCE_NOTES.md#anti-overuse-boundaries`
  scores:
    EVD: 5
    IMP: 4
    RSK: 3
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due: 2026-07-27

- id: `PW-TPL-009`
  status: accepted
  use_when: A high-risk promptflow or repo task needs constant frame control before execution.
  template_body: |
    # Constant Frame Task Packet

    ```yaml
    frame_block:
      frame_id: <PROCESS_OR_PROMPTFLOW_ID>
      active_task_id: <TASK-ID>
      active_agent_role: planner | executor | verifier | state_keeper
      working_repo: <owner/name>
      target_root: <repo-relative-root>
      source_refs:
        - <exact source path>
      immutable_locks:
        - one_atomic_task_per_call
        - no_implicit_state_inference
        - no_scope_expansion
        - fetch_back_required

    task_payload:
      id: <TASK-ID>
      type: file_write | file_update | diff_patch | appendix_create | scaffold_update | verification
      target_file: <exact repo-relative path>
      scope: <one-sentence atomic scope>
      input_refs:
        - <exact source path>
      constraints:
        - inherit_from_frame_block

    gate_check:
      task_id: <TASK-ID>
      scope_understood: <repeat scope verbatim>
      ambiguity_detected: false
      ready_to_execute: true
    ```

    Execute only after the gate check passes. If state, target, source refs, or scope are ambiguous, emit HALT or CLARIFY instead of proceeding.
  evidence_refs:
    - `appendices/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md`
    - `appendices/APPENDIX_KB_RUNTIME_TEMPLATE_CATALOG.md`
    - `appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md`
  scores:
    EVD: 5
    IMP: 5
    RSK: 3
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due: 2026-07-27

- id: `PW-TPL-010`
  status: accepted
  use_when: An execution task must stop, clarify, or prove validated completion without relying on conversational signoff.
  template_body: |
    # Control Signal and Artifact Closure Packet

    ```yaml
    halt:
      signal: HALT
      task_id: <TASK-ID>
      reason: wrong_repo_context | state_read_failure | split_task_required | promotion_gate_failed | external_claim_unverified | patch_check_fail | scope_exceeded | validation_failed
      detail: <one-line machine-readable detail>
      safe_state: true | false
      recovery: manual_review_required | retry_with_corrected_payload | split_task | validate_source | create_appendix_first

    clarify:
      signal: CLARIFY
      task_id: <TASK-ID>
      question: <one blocking question only>
      blocking: <exact ambiguous field>
      options:
        - <option_a>
        - <option_b>

    artifact_closure:
      task_id: <TASK-ID>
      output_type: file_write | file_update | diff_patch | verification
      target_file: <repo-relative path>
      scope_respected: yes | no
      additions_beyond_scope: none | <one-line explanation>
      validation:
        fetch_back: pass | fail
        target_root: pass | fail
        claim_status: pass | fail
        scaffold_untouched: pass | fail
      next_suggested_task: <TASK-ID or none>
    ```

    A closure is accepted only after fetch-back or equivalent file-state validation. A HALT blocks downstream execution until corrected.
  evidence_refs:
    - `appendices/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md`
    - `appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md`
    - `appendices/APPENDIX_KB_EXTERNAL_CLAIM_VERIFICATION.md`
  scores:
    EVD: 5
    IMP: 5
    RSK: 3
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due: 2026-07-27

## Appendix pointers

- Ranking ledger: `appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md`
- Candidate ledger: `appendices/APPENDIX_KB_CANDIDATE_LEDGER.md`
- Anti-drift evidence: `appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md`
- Conflict report: `appendices/SOURCE_CONFLICT_REPORT.md`
- Examples: `appendices/APPENDIX_KB_EXAMPLES.md`
- Source notes: `appendices/APPENDIX_KB_SOURCE_NOTES.md`
- QA and next research plan: `appendices/APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md`
- Constant failure integration process: `appendices/APPENDIX_KB_CONSTANT_FAILURE_INTEGRATION_PROCESS.md`
- Execution control contracts: `appendices/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md`
- Constant failure source notes: `appendices/APPENDIX_KB_CONSTANT_FAILURE_SOURCE_NOTES.md`
- Patch transport protocols: `appendices/APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md`
- Regression examples: `appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md`
- Runtime template catalog: `appendices/APPENDIX_KB_RUNTIME_TEMPLATE_CATALOG.md`
- External claim verification: `appendices/APPENDIX_KB_EXTERNAL_CLAIM_VERIFICATION.md`

## Promotion boundary

Add templates here only after validation and promotion from `LEARNING_QUEUE.md`.
