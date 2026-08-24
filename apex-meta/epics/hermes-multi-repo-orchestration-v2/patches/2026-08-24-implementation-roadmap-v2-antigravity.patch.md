# Exact-Match Patch Pack — Activate Implementation Roadmap v2 / Antigravity Executor

Status: **READY FOR DETERMINISTIC APPLICATION / NOT APPLIED BY THIS AUTHORING RUN**  
Date: 2026-08-24

Purpose:

- activate `15-IMPLEMENTATION-ROADMAP-v2-ANTIGRAVITY.md` as the implementation execution authority;
- preserve `11-IMPLEMENTATION-ROADMAP.md` as the v1 technical phase catalog;
- record Antigravity as the bounded implementation executor while preserving architecture/client independence;
- keep implementation authorization false;
- make no D01–D10 decision change.

Application law:

1. re-read each live file before application;
2. verify the recorded baseline blob SHA still matches or, if it moved, rebuild the patch from the new live bytes;
3. every `<old>` block must match exactly once;
4. apply only the exact replacement;
5. re-read the changed range and compare the final diff;
6. never substitute whole-file replacement.

---

## PATCH 1 — README authority order

Baseline blob SHA: `e73848d44415557a8da44d701ae4b8c8b503dd28`

<file>
apex-meta/epics/hermes-multi-repo-orchestration-v2/README.md
</file>

<old>
## Authority order

Future agents must read in this order:

1. `README.md` — navigation and authority order.
2. `DECISIONS.md` — compact accepted/deferred decision ledger D01–D10.
3. `state.yaml` — machine-readable current state after the pending patch is applied.
4. `decisions/Dxx-*.md` — decision-specific reasoning/risk appendices.
5. `11-IMPLEMENTATION-ROADMAP.md` — phased implementation plan.
6. `12-RISK-REGISTER.yaml` — machine-readable operational risks.
7. `13-SOURCE-VERIFICATION-MATRIX.md` — claim-to-source verification grades.
8. `incidents/` — upstream/runtime incidents that constrain decisions.
9. `02-MASTEROFARTS-SOURCE-MIGRATION-MANIFEST.md` — pilot provenance that must survive re-homing.
10. `FUTURE-DEVELOPMENT.md` — explicitly deferred capabilities.

Independent pre-implementation validation launcher:

- `14-INDEPENDENT-PREIMPLEMENTATION-VALIDATION-HANDOVER.md` — adversarial handover/prompt for double/triple-checking the accepted architecture, tools, agent orchestration, risks, simulations, and current upstream contracts before implementation authorization.

The D02/D10 decision patch has landed. `README.md` is the current entrypoint and `state.yaml` is the current machine-readable state. Continue to use `patches/` for future edits to existing control files.
</old>

<new>
## Authority order

Future agents must read in this order:

1. `README.md` — navigation and authority order.
2. `DECISIONS.md` — compact accepted/deferred decision ledger D01–D10.
3. `state.yaml` — machine-readable current state after the pending patch is applied.
4. `decisions/Dxx-*.md` — decision-specific reasoning/risk appendices.
5. `15-IMPLEMENTATION-ROADMAP-v2-ANTIGRAVITY.md` — current implementation execution plan; Antigravity is the bounded executor, not an architecture dependency.
6. `11-IMPLEMENTATION-ROADMAP.md` — preserved v1 technical phase catalog; use only where v2 explicitly imports its detail.
7. `12-RISK-REGISTER.yaml` — machine-readable operational risks.
8. `13-SOURCE-VERIFICATION-MATRIX.md` — claim-to-source verification grades.
9. `incidents/` — upstream/runtime incidents that constrain decisions.
10. `02-MASTEROFARTS-SOURCE-MIGRATION-MANIFEST.md` — pilot provenance that must survive re-homing.
11. `FUTURE-DEVELOPMENT.md` — explicitly deferred capabilities.

Independent pre-implementation validation launcher:

- `14-INDEPENDENT-PREIMPLEMENTATION-VALIDATION-HANDOVER.md` — adversarial handover/prompt for double/triple-checking the accepted architecture, tools, agent orchestration, risks, simulations, and current upstream contracts before implementation authorization.
- `validation/independent-preimplementation-review/04-CORRECTION-PLAN.md` — mandatory correction gates incorporated by implementation roadmap v2.

The D02/D10 decision patch has landed. `README.md` is the current entrypoint and `state.yaml` is the current machine-readable state. Continue to use `patches/` for future edits to existing control files. Existing control files remain patch-only; new files may be created directly.
</new>

---

## PATCH 2 — state.yaml implementation-plan pointers

Baseline blob SHA: `66ff4c23bd2e1e36f3b987ae5d563d59f926a8d8`

<file>
apex-meta/epics/hermes-multi-repo-orchestration-v2/state.yaml
</file>

<old>
architecture: apex-meta/epics/hermes-multi-repo-orchestration-v2/01-VERIFIED-ARCHITECTURE.md
implementation_roadmap: apex-meta/epics/hermes-multi-repo-orchestration-v2/11-IMPLEMENTATION-ROADMAP.md
risk_register: apex-meta/epics/hermes-multi-repo-orchestration-v2/12-RISK-REGISTER.yaml
verification_matrix: apex-meta/epics/hermes-multi-repo-orchestration-v2/13-SOURCE-VERIFICATION-MATRIX.md
validation_handover: apex-meta/epics/hermes-multi-repo-orchestration-v2/14-INDEPENDENT-PREIMPLEMENTATION-VALIDATION-HANDOVER.md
future_development: apex-meta/epics/hermes-multi-repo-orchestration-v2/FUTURE-DEVELOPMENT.md
</old>

<new>
architecture: apex-meta/epics/hermes-multi-repo-orchestration-v2/01-VERIFIED-ARCHITECTURE.md
implementation_roadmap: apex-meta/epics/hermes-multi-repo-orchestration-v2/15-IMPLEMENTATION-ROADMAP-v2-ANTIGRAVITY.md
implementation_roadmap_v1_reference: apex-meta/epics/hermes-multi-repo-orchestration-v2/11-IMPLEMENTATION-ROADMAP.md
implementation_validation_corrections: apex-meta/epics/hermes-multi-repo-orchestration-v2/validation/independent-preimplementation-review/04-CORRECTION-PLAN.md
risk_register: apex-meta/epics/hermes-multi-repo-orchestration-v2/12-RISK-REGISTER.yaml
verification_matrix: apex-meta/epics/hermes-multi-repo-orchestration-v2/13-SOURCE-VERIFICATION-MATRIX.md
validation_handover: apex-meta/epics/hermes-multi-repo-orchestration-v2/14-INDEPENDENT-PREIMPLEMENTATION-VALIDATION-HANDOVER.md
future_development: apex-meta/epics/hermes-multi-repo-orchestration-v2/FUTURE-DEVELOPMENT.md
</new>

---

## PATCH 3 — state.yaml implementation executor contract

Baseline blob SHA: `66ff4c23bd2e1e36f3b987ae5d563d59f926a8d8`

<file>
apex-meta/epics/hermes-multi-repo-orchestration-v2/state.yaml
</file>

<old>
runtime_target:
  canonical_workspace_root: "~/workspaces"
  canonical_filesystem: WSL2_linux_filesystem
  windows_access: "\\\\wsl.localhost\\Ubuntu\\home\\<operator>\\workspaces"
  one_hermes_installation: true
  one_qmd_installation: true
  docker_execution_boundary: true
  duplicate_live_windows_wsl_checkouts: false
  safe_mode_initial: sequential_single_repo_execution
  autonomous_multi_board_mode: gated_future_option

kanban_recommendation:
</old>

<new>
runtime_target:
  canonical_workspace_root: "~/workspaces"
  canonical_filesystem: WSL2_linux_filesystem
  windows_access: "\\\\wsl.localhost\\Ubuntu\\home\\<operator>\\workspaces"
  one_hermes_installation: true
  one_qmd_installation: true
  docker_execution_boundary: true
  duplicate_live_windows_wsl_checkouts: false
  safe_mode_initial: sequential_single_repo_execution
  autonomous_multi_board_mode: gated_future_option

implementation_execution:
  executor: Google_Antigravity
  executor_role: bounded_phase_executor_and_verifier
  architecture_dependency_on_executor: false
  implementation_run_uses_executor: true
  implementation_status: not_authorized
  branch_policy: canonical_branch_only_no_branches_or_PRs
  worktrees: forbidden
  existing_control_file_mutation: exact_match_patch_only
  whole_file_rewrite_existing_control_files: forbidden
  new_files_direct_creation: allowed
  context_policy: one_major_phase_per_Antigravity_context
  evidence_policy: one_compact_phase_evidence_file_plus_implementation_state
  upstream_refresh_before_mutation: required
  D10_enablement: separate_explicit_operator_gate

kanban_recommendation:
</new>

---

## PATCH 4 — state.yaml Antigravity portability clarification

Baseline blob SHA: `66ff4c23bd2e1e36f3b987ae5d563d59f926a8d8`

<file>
apex-meta/epics/hermes-multi-repo-orchestration-v2/state.yaml
</file>

<old>
  hermes: primary_orchestration_runtime
  antigravity:
    permanent_dependency: false
  codex:
</old>

<new>
  hermes: primary_orchestration_runtime
  antigravity:
    permanent_dependency: false
    implementation_executor_for_v2_realization: true
    executor_authority: 15_IMPLEMENTATION_ROADMAP_v2_ANTIGRAVITY
    post_realization_architecture_must_not_require_Antigravity: true
  codex:
</new>

---

## PATCH 5 — state.yaml next action

Baseline blob SHA: `66ff4c23bd2e1e36f3b987ae5d563d59f926a8d8`

<file>
apex-meta/epics/hermes-multi-repo-orchestration-v2/state.yaml
</file>

<old>
next_action:
  owner: human_operator
  gate: implementation_authorization
  instruction: review_README_DECISIONS_appendices_and_authorize_11_IMPLEMENTATION_ROADMAP_only_when_ready
  D10_constraint: background_multi_board_execution_remains_forbidden_until_D10_acceptance_tests_pass
</old>

<new>
next_action:
  owner: human_operator
  gate: implementation_authorization
  instruction: apply_v2_activation_patch_then_authorize_15_IMPLEMENTATION_ROADMAP_v2_ANTIGRAVITY_when_ready
  executor: Google_Antigravity
  implementation_authorized: false
  migration_authorized: false
  D10_constraint: background_multi_board_execution_remains_forbidden_until_D10_acceptance_tests_pass_and_explicit_operator_approval
</new>

---

## PATCH 6 — preserve v1 roadmap but remove execution-authority ambiguity

Baseline blob SHA: `edd3ae40bf67e2457c73f7e83af703c50331366c`

<file>
apex-meta/epics/hermes-multi-repo-orchestration-v2/11-IMPLEMENTATION-ROADMAP.md
</file>

<old>
# 11 — Hermes Multi-Repo v2 Implementation Roadmap

Status: **PLAN COMPLETE / IMPLEMENTATION NOT AUTHORIZED**  
Date: 2026-08-24

## Target outcome
</old>

<new>
# 11 — Hermes Multi-Repo v2 Implementation Roadmap

Status: **V1 TECHNICAL PHASE CATALOG / SUPERSEDED AS EXECUTION AUTHORITY BY `15-IMPLEMENTATION-ROADMAP-v2-ANTIGRAVITY.md` / IMPLEMENTATION NOT AUTHORIZED**  
Date: 2026-08-24

> Preservation rule: keep this file intact as detailed v1 technical planning evidence. The v2 plan imports useful phase detail from this file but governs execution order, Antigravity behavior, validation corrections, and patch-only mutation law.

## Target outcome
</new>

---

## Deterministic application verification

After all six patches are applied:

1. `README.md` names v2 before v1 in authority order.
2. `state.yaml.implementation_roadmap` points to v2.
3. `state.yaml` still has:
   - `implementation_authorized: false`
   - `migration_authorized: false`
   - `background_multi_board_dispatch_authorized: false`
4. `state.yaml.client_portability.antigravity.permanent_dependency` remains `false`.
5. `state.yaml.implementation_execution.executor` is `Google_Antigravity`.
6. v1 roadmap remains present and gains only the supersession/preservation notice.
7. `git diff` contains only the six exact replacements above.
8. no D01–D10 decision appendix changes.
