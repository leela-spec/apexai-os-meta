# Phase 7 Complete — Package Readiness Gate v0.1

## 0. Scope executed

**Executed:** readiness decision for:

```
.claude/skills/apex-plan/.claude/skills/apex-sync/.claude/skills/apex-session/
```

**Not executed:** no package generation, no repo writes, no public web browsing, no architecture redesign.

One important repo-state finding: the three target packages already have current `SKILL.md` entrypoints and manifests in the live repo. I therefore treat this as a **readiness + boundary audit**, not as permission to continue generation blindly.

---

## 1. Inputs reloaded

|Input|Reload result|Relevance|
|---|---|---|
|Phase 4 mechanism ledger|Loaded|Defines COPY / ADAPT / CONCEPT / OMIT mechanisms and unresolved sources.|
|Phase 5 process coverage gate|Loaded|Main readiness basis; verdict was `PHASE_5_PARTIAL_PASS_WITH_B_SYNC_AND_INDEX_BLOCKERS`.|
|Phase 6 PM2 audit|Loaded|PM2 passed against CCPM + Backlog + CrewAI `task.py` substitute.|
|Live repo H1–H7 decisions|Fetched|Confirms status enum, paths, dependency field, Python-only rule, clusters, handoff format, and priority/urgency policy.|
|Live `apex-plan` package|Fetched|Entry point + manifest exist; package is planning-only and no-script.|
|Live `apex-sync` package|Fetched|Entry point + manifest + `apex_sync.py` exist; package is custom deterministic Python.|
|Live `apex-session` package|Fetched|Entry point + manifest exist; package covers gated mutations and handoff/session continuity.|

---

## 2. Readiness criteria

|Status|Meaning|
|---|---|
|`READY_FOR_GENERATION`|Enough grounded evidence exists to generate without inventing missing mechanisms.|
|`READY_WITH_CUSTOM_PYTHON_WORK`|Safe only if missing mechanisms are explicitly labeled as Apex-native Python, not copied source behavior.|
|`PARTIAL_READY_WITH_GAPS`|Useful coverage exists, but important mechanisms are missing, substitute-only, or boundary-unclear.|
|`BLOCKED`|Core package mechanisms depend on unresolved sources and cannot safely be generated.|

---

## 3. Package readiness summary table

|Package|Gate status|Confidence|Main reason|Generation recommendation|
|---|---|---|---|---|
|`apex-plan`|**READY_FOR_GENERATION**|88/100|A_PLAN has strong PM1/PM2/PM3/PD1/PD4 basis; PM2 specifically passed Phase 6.|Generate first, with CrewAI substitute label preserved.|
|`apex-session`|**READY_WITH_CUSTOM_PYTHON_WORK**|78/100|C_SESSION is mostly covered; handoff/session evidence is strong, but PD3/reverse-unlock support remains custom/partial.|Generate second, but keep scope to handoff/session/mutation gates and do not overclaim exact graph logic.|
|`apex-sync`|**PARTIAL_READY_WITH_GAPS**|62/100|B_SYNC carries the known blocker/index/drift gaps; exact `update-index.py` and Kanban scripts remain unresolved.|Do not generate as fully source-backed. Generate only if custom Apex Python is explicitly accepted.|

---

## 4. `apex-plan` readiness

### Verdict

```
apex_plan:  readiness_status: READY_FOR_GENERATION  supporting_processes:    - PM1_capture_project    - PM2_decompose_project    - PM3_assign_dependencies    - PD1_priority_scoring_policy    - PD2_urgency_policy    - PD4_focus_recommendation
```

### Evidence basis

`apex-plan` matches the A_PLAN boundary: it owns project capture, decomposition, dependency proposals, priority/urgency rationale, and provisional focus recommendation, while explicitly handing exact ranking, blocker scans, registry rebuild, and state mutation to other packages.

The package manifest reinforces the same boundary: it must capture goals, define epics, draft task records, propose `depends_on`, explain priority/due-date/focus qualitatively, and must not run scripts or mutate durable files.

Phase 6 gives the strongest readiness support: PM2 passed as a control chain with CCPM as decomposition spine, Backlog as task substrate/parser model, and CrewAI `task.py` as substitute task-contract source.

### Caveats

- CrewAI original getting-started skill remains missing; `task.py` is only a **substitute** for task contract evidence.
- PD2 urgency should be treated as an Apex H7 rule, not as copied Kanban evidence.
- `apex-plan` must remain no-script and operator-gated.

### Generation boundary

Safe to generate as a rich package **now**, provided it is labeled:

```
source_backing:  PM2: CCPM + Backlog + CrewAI_task_py_SUBSTITUTE  urgency_policy: Apex_H7_native_rule  exact_scoring: delegated_to_apex_sync  mutations: delegated_to_apex_session
```

---

## 5. `apex-sync` readiness

### Verdict

```
apex_sync:  readiness_status: PARTIAL_READY_WITH_GAPS  conditional_status_if_custom_python_accepted: READY_WITH_CUSTOM_PYTHON_WORK
```

### Evidence basis

The live package defines `apex-sync` as deterministic read-side synchronization, owning PM4, PM5, PM7, PM8, KB4, KB5 plus score/focus-related outputs.

Its manifest already frames `apex_sync.py` as the canonical executable for read-only behavior, registry write behavior, and standard-library implementation. The script itself exists and states that it reads task files, computes reports, and writes only `apex-meta/registry/index.md` when registry is invoked with `--dry-run false`. It also implements H1/H7 constants and task glob assumptions.

### Blockers / source gaps

Phase 5 is decisive here: B_SYNC was **not ready** because PM5, PM7, PM8, KB4, and KB5 are partial or blocked, with exact Kanban blocker/list scripts, exact llm-wiki `update-index.py`, OpenClaw TaskFlow, CrewAI getting-started, and Hermes governance still unresolved.

I also attempted to re-resolve the exact llm-wiki `update-index.py` and Kanban `show_blocked.sh` paths in the live repo; both remained unavailable through the expected paths, so I am carrying them forward as gaps rather than substituting invented evidence.

### Additional boundary issue

There is a **path/boundary drift** to resolve before package generation:

- Current operator lock says `scripts_root: scripts/`.
- Live `apex-sync` points to `apex-meta/scripts/apex_sync.py`.
- Live repo also still contains older root `scripts/find_next_task.py`, which imports `yaml`, meaning it is not standard-library-only.

This does not block the readiness gate, but it **must be normalized before final generation or application**.

### Minimum safe package scope

Safe only as:

```
minimum_safe_apex_sync_scope:  claim_as_source_backed:    - dependency_satisfied_next_action_concept    - script_first_read_side_reports    - H1_status_validation    - H7_priority_urgency_calculation  claim_as_custom_apex_python:    - blocker_scan    - stale_detection    - registry_rebuild    - drift_detection    - unlock_depth  must_not_claim:    - copied_llm_wiki_update_index    - copied_kanban_blocker_scripts    - copied_openclaw_taskflow_state_machine    - Hermes_governance_hardening
```

---

## 6. `apex-session` readiness

### Verdict

```
apex_session:  readiness_status: READY_WITH_CUSTOM_PYTHON_WORK  safe_generation_scope: handoff_session_mutation_gate
```

### Evidence basis

The live `apex-session` package is correctly centered on gated mutations, session progress, state deltas, entity-update proposals, next-session context, planning-layer feed, and operator validation.

Its procedure requires loading session context, drafting mutation proposals, applying a confirmation-token gate, recording progress, extracting deltas, preparing handoff, and validating completion.

The handoff outputs map well to H6: task plan, findings, progress, and next-session context. The manifest also keeps boundaries clean: no scripts, repo writes, next-task ranking, blocker scans, registry rebuilds, scoring, new decomposition, or ungated mutation.

### Caveats

- Phase 5 marked C_SESSION as ready with one custom/partial rule around PD3 reverse-unlock support.
- The current live `apex-sync` claims `PD3_compute_unlock_depth`, while locked H5 places PD3 under C_SESSION.
- This must be resolved as a boundary note before generation: either PD3 remains C_SESSION with a custom helper rule, or operator explicitly changes H5. Under the current instruction, H5 must not be changed.

### Generation boundary

Safe to generate if `apex-session` is scoped to:

```
safe_apex_session_generation_boundary:  owns:    - PM6_status_mutation_proposals    - KB1_progress_capture    - KB2_state_delta_extraction    - KB3_entity_update_proposals    - KB6_next_session_context    - PD5_operator_validation    - PD6_planning_layer_feed  must_treat_as_custom_or_handoff:    - PD3_reverse_unlock_support  must_not_do:    - exact_next_task_ranking    - blocker_scan    - registry_rebuild    - drift_detection    - score_computation
```

---

## 7. Required custom work before generation

|Required work|Applies to|Reason|
|---|---|---|
|Label CrewAI `task.py` as substitute evidence|`apex-plan`|PM2 is strong, but not from original CrewAI getting-started skill.|
|Decide script root|`apex-sync`|Current instruction says `scripts/`; live package uses `apex-meta/scripts/`.|
|Accept or reject custom Apex Python for B_SYNC|`apex-sync`|Missing exact llm-wiki/Kanban/OpenClaw sources mean B_SYNC cannot be represented as copied source logic.|
|Define custom index-rebuild behavior|`apex-sync`|KB4 remains blocked without exact `update-index.py`.|
|Define custom blocker/stale/drift behavior|`apex-sync`|PM5/PM7/KB5 are not fully source-backed.|
|Resolve PD3 package ownership|`apex-session` / `apex-sync`|H5 puts PD3 in C_SESSION; current live `apex-sync` claims unlock-depth computation.|
|Keep Hermes governance as later hardening|all packages|Hermes governance source remains missing; do not claim final governance hardening.|

---

## 8. Recommended generation order

```
recommended_generation_order:  1:    package: apex-plan    reason: strongest evidence, PM2 passed, least custom mechanism risk    status: generate_first_if_operator_confirms  2:    package: apex-session    reason: session/handoff/mutation gate is mostly grounded    condition: resolve_PD3_boundary_or_label_PD3_as_custom_support  3:    package: apex-sync    reason: highest utility but largest source gaps    condition: generate_only_as_custom_Apex_Python_scope_or_delay
```

**Recommendation:** generate `apex-plan` first, then `apex-session`, and delay or custom-scope `apex-sync`.

---

## 9. Operator decisions needed

1. **Accept CrewAI `task.py` substitute?**  
    Recommended: **yes**, but label it explicitly as `SUBSTITUTE`, not original skill-source evidence.
2. **Accept custom Apex Python for B_SYNC?**  
    Recommended: **yes only if labeled clearly**. Otherwise delay `apex-sync`.
3. **Which script root is canonical now: `scripts/` or `apex-meta/scripts/`?**  
    Recommended under current instruction: keep `scripts/` unless you explicitly amend H2.
4. **Generate `apex-plan` first?**  
    Recommended: **yes**.
5. **Keep `apex-sync` partial or delay?**  
    Recommended: generate only a **custom-scoped** version, or delay until missing sources are resolved.

---

## 10. Gate verdict YAML

```
phase_7_package_readiness_gate:  version: "0.1"  status: COMPLETE  repo_writes_performed: false  package_generation_performed: false  public_web_used: false  readiness:    apex_plan:      status: READY_FOR_GENERATION      confidence: 88      evidence_basis:        - Phase_5_A_PLAN_mostly_ready        - Phase_6_PM2_control_chain_pass        - live_repo_package_entrypoint_and_manifest_present      caveats:        - CrewAI_task_py_is_substitute        - urgency_policy_is_Apex_H7_native_rule      recommendation: generate_first    apex_session:      status: READY_WITH_CUSTOM_PYTHON_WORK      confidence: 78      evidence_basis:        - Phase_5_C_SESSION_ready_with_one_custom_rule        - planning_with_files_handoff_pattern        - live_repo_package_entrypoint_and_manifest_present      caveats:        - PD3_reverse_unlock_support_partial        - current_live_apex_sync_claims_PD3_despite_H5_C_SESSION_lock      recommendation: generate_second_after_PD3_boundary_note    apex_sync:      status: PARTIAL_READY_WITH_GAPS      conditional_status_if_operator_accepts_custom_python: READY_WITH_CUSTOM_PYTHON_WORK      confidence: 62      evidence_basis:        - Phase_5_B_SYNC_not_ready        - live_repo_apex_sync_package_and_apex_sync_py_present      blockers:        - exact_llm_wiki_update_index_py_missing        - Kanban_blocker_list_scripts_unresolved        - OpenClaw_TaskFlow_missing        - Hermes_governance_missing      recommendation: delay_or_generate_only_as_custom_Apex_Python  generation_order:    - apex-plan    - apex-session    - apex-sync_custom_or_deferred  operator_decisions_required:    - accept_CrewAI_task_py_substitute_for_PM2    - accept_custom_Apex_Python_for_B_SYNC    - confirm_script_root_scripts_vs_apex_meta_scripts    - confirm_apex_plan_first    - decide_apex_sync_custom_scope_or_delay
```