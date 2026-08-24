# PATCH-001 — Decision Pack Index, D02 Acceptance, D10 Registration

Status: **READY FOR DETERMINISTIC EXACT-MATCH APPLICATION**  
Date: 2026-08-24

Purpose: align existing v2 control files with the operator's accepted D01–D09 decisions, accepted D02 topology, newly explicit D10 safety gate, and the new README/decision-appendix structure.

Apply literal exact-match replacements only. One change per OLD/NEW pair. Abort a block if OLD does not match exactly once.

---

`apex-meta/epics/hermes-multi-repo-orchestration-v2/epic.md`

<OLD>
Status: **RESEARCH VERIFIED / D02 OPERATOR DECISION REMAINS / IMPLEMENTATION NOT AUTHORIZED**  
</OLD>
<NEW>
Status: **ARCHITECTURE DECISIONS D01-D10 RECORDED / IMPLEMENTATION NOT AUTHORIZED**  
</NEW>

---

`apex-meta/epics/hermes-multi-repo-orchestration-v2/epic.md`

<OLD>
      |   +-- SEPARATE repo Kanban boards (recommended D02)
</OLD>
<NEW>
      |   +-- SEPARATE repo Kanban boards (accepted D02)
</NEW>

---

`apex-meta/epics/hermes-multi-repo-orchestration-v2/epic.md`

<OLD>
D02 remains the only primary architecture choice awaiting explicit operator acceptance.
</OLD>
<NEW>
D02 was explicitly accepted by the operator on 2026-08-24. The selected topology is separate repo boards plus asynchronous deterministic read-only Apex rollup.
</NEW>

---

`apex-meta/epics/hermes-multi-repo-orchestration-v2/epic.md`

<OLD>
## Files in this epic

1. `epic.md` — current authority/index.
2. `01-VERIFIED-ARCHITECTURE.md` — concise current architecture/user stories.
3. `02-MASTEROFARTS-SOURCE-MIGRATION-MANIFEST.md` — pilot provenance to preserve/re-home.
</OLD>
<NEW>
## Files in this epic

1. `README.md` — human/agent entrypoint, authority order and complete index.
2. `DECISIONS.md` — compact D01-D10 decision ledger.
3. `decisions/` — one reasoning/risk/forces/shortcomings appendix per decision.
4. `incidents/` — separately maintained upstream/runtime incident evidence linked from decisions.
5. `epic.md` — project overview and architecture summary.
6. `01-VERIFIED-ARCHITECTURE.md` — concise current architecture/user stories.
7. `02-MASTEROFARTS-SOURCE-MIGRATION-MANIFEST.md` — pilot provenance to preserve/re-home.
</NEW>

---

`apex-meta/epics/hermes-multi-repo-orchestration-v2/epic.md`

<OLD>
- **D01 — Apex control plane:** accepted. Apex owns portfolio/orchestration state; project truth stays in source repos.
- **D02 — Kanban topology:** **decision pending**. Current verified recommendation = separate repo boards + asynchronous Apex rollup.
- **D03 — Reusable role profiles:** accepted with constraint: sequential same-profile use until global concurrency is proven safe.
</OLD>
<NEW>
- **D01 — Apex control plane:** accepted. Apex owns portfolio/orchestration state; project truth stays in source repos.
- **D02 — Kanban topology:** accepted 2026-08-24. Separate repo boards + asynchronous deterministic read-only Apex rollup.
- **D03 — Reusable role profiles:** accepted with constraint: sequential same-profile use until global concurrency is proven safe.
</NEW>

---

`apex-meta/epics/hermes-multi-repo-orchestration-v2/epic.md`

<OLD>
- **D09 — External memory:** deferred until a measured cross-profile memory gap exists.

## Current upstream evidence
</OLD>
<NEW>
- **D09 — External memory:** deferred until a measured cross-profile memory gap exists.
- **D10 — Background multi-board autonomy:** deferred safety gate. Do not enable unattended concurrent execution across repo boards until the acceptance tests in `decisions/D10-BACKGROUND-MULTI-BOARD-AUTONOMY.md` pass against the installed Hermes version. Incident evidence: `incidents/INC-001-HERMES-KANBAN-DOCKER-WORKSPACE-CONCURRENCY.md`.

See `DECISIONS.md` for the compact authoritative decision ledger and `decisions/` for the separate reasoning appendices.

## Current upstream evidence
</NEW>

---

`apex-meta/epics/hermes-multi-repo-orchestration-v2/epic.md`

<OLD>
research: substantially complete
D02 human architecture gate: OPEN
runtime migration: NOT AUTHORIZED
</OLD>
<NEW>
research: substantially complete
D01-D10 architecture decisions: RECORDED
runtime migration: NOT AUTHORIZED
</NEW>

---

`apex-meta/epics/hermes-multi-repo-orchestration-v2/01-VERIFIED-ARCHITECTURE.md`

<OLD>
Status: **RESEARCH VERIFIED / D02 OPERATOR DECISION REMAINS / IMPLEMENTATION NOT AUTHORIZED**  
</OLD>
<NEW>
Status: **RESEARCH VERIFIED / D02 ACCEPTED / IMPLEMENTATION NOT AUTHORIZED**  
</NEW>

---

`apex-meta/epics/hermes-multi-repo-orchestration-v2/01-VERIFIED-ARCHITECTURE.md`

<OLD>
|   +-- separate repo Kanban boards (current D02 recommendation)
</OLD>
<NEW>
|   +-- separate repo Kanban boards (accepted D02)
</NEW>

---

`apex-meta/epics/hermes-multi-repo-orchestration-v2/01-VERIFIED-ARCHITECTURE.md`

<OLD>
### V4 — separate repo boards are now recommended
</OLD>
<NEW>
### V4 — separate repo boards are accepted
</NEW>

---

`apex-meta/epics/hermes-multi-repo-orchestration-v2/01-VERIFIED-ARCHITECTURE.md`

<OLD>
Therefore current recommendation:
</OLD>
<NEW>
Therefore accepted D02 topology:
</NEW>

---

`apex-meta/epics/hermes-multi-repo-orchestration-v2/01-VERIFIED-ARCHITECTURE.md`

<OLD>
D02 remains a human gate because this trades native cross-project dependency links for stronger project isolation.
</OLD>
<NEW>
The operator accepted this trade on 2026-08-24: stronger repo/project isolation plus asynchronous Apex references/rollup is preferred over one tenant-shared board.
</NEW>

---

`apex-meta/epics/hermes-multi-repo-orchestration-v2/04-KANBAN-TOPOLOGY-AND-APEX-ROLLUP.md`

<OLD>
Status: **D02 RESEARCH REVISED / RECOMMENDATION READY**  
</OLD>
<NEW>
Status: **D02 ACCEPTED 2026-08-24 / IMPLEMENTATION NOT AUTHORIZED**  
</NEW>

---

`apex-meta/epics/hermes-multi-repo-orchestration-v2/state.yaml`

<OLD>
status: research_verified_D02_operator_gate_remaining
</OLD>
<NEW>
status: architecture_decisions_D01_D10_recorded_implementation_not_authorized
</NEW>

---

`apex-meta/epics/hermes-multi-repo-orchestration-v2/state.yaml`

<OLD>
entrypoint: apex-meta/epics/hermes-multi-repo-orchestration-v2/epic.md
architecture: apex-meta/epics/hermes-multi-repo-orchestration-v2/01-VERIFIED-ARCHITECTURE.md
</OLD>
<NEW>
entrypoint: apex-meta/epics/hermes-multi-repo-orchestration-v2/README.md
decision_ledger: apex-meta/epics/hermes-multi-repo-orchestration-v2/DECISIONS.md
decision_appendices_root: apex-meta/epics/hermes-multi-repo-orchestration-v2/decisions
incidents_root: apex-meta/epics/hermes-multi-repo-orchestration-v2/incidents
architecture: apex-meta/epics/hermes-multi-repo-orchestration-v2/01-VERIFIED-ARCHITECTURE.md
</NEW>

---

`apex-meta/epics/hermes-multi-repo-orchestration-v2/state.yaml`

<OLD>
kanban_recommendation:
  status: operator_decision_required
</OLD>
<NEW>
kanban_recommendation:
  status: accepted_2026_08_24
</NEW>

---

`apex-meta/epics/hermes-multi-repo-orchestration-v2/state.yaml`

<OLD>
  D02_kanban_topology:
    status: operator_decision_required_after_research_revision
    recommendation: separate_repo_boards_plus_async_read_only_Apex_rollup
</OLD>
<NEW>
  D02_kanban_topology:
    status: accepted_2026_08_24
    decision: separate_repo_boards_plus_async_deterministic_read_only_Apex_rollup
</NEW>

---

`apex-meta/epics/hermes-multi-repo-orchestration-v2/state.yaml`

<OLD>
  D09_external_memory:
    status: deferred_accepted_2026_08_24
    decision: no_external_memory_until_measured_gap

next_action:
</OLD>
<NEW>
  D09_external_memory:
    status: deferred_accepted_2026_08_24
    decision: no_external_memory_until_measured_gap
  D10_background_multi_board_autonomy:
    status: deferred_safety_gate_2026_08_24
    decision: no_unattended_concurrent_multi_board_execution_until_installed_version_passes_workspace_persistence_mount_scope_and_profile_concurrency_acceptance
    appendix: apex-meta/epics/hermes-multi-repo-orchestration-v2/decisions/D10-BACKGROUND-MULTI-BOARD-AUTONOMY.md
    incident: apex-meta/epics/hermes-multi-repo-orchestration-v2/incidents/INC-001-HERMES-KANBAN-DOCKER-WORKSPACE-CONCURRENCY.md

next_action:
</NEW>

---

`apex-meta/epics/hermes-multi-repo-orchestration-v2/state.yaml`

<OLD>
next_action:
  owner: human_operator
  gate: D02
  instruction: decide_separate_repo_boards_plus_async_Apex_rollup_before_runtime_reconfiguration
  after_acceptance: execute_11_IMPLEMENTATION_ROADMAP_phase_by_phase
</OLD>
<NEW>
next_action:
  owner: human_operator
  gate: implementation_authorization
  instruction: review_README_DECISIONS_appendices_and_authorize_11_IMPLEMENTATION_ROADMAP_only_when_ready
  D10_constraint: background_multi_board_execution_remains_forbidden_until_D10_acceptance_tests_pass
</NEW>
