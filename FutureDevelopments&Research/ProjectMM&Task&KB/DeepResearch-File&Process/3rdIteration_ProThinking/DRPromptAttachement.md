# Add This Attachment Block to the Deep Research Prompt

Paste this **above** the “Begin now” line, or directly after the “Binding Phase 7 Decisions” section.

```
# Access-Independent Decision CapsuleUse this capsule as the authoritative fallback if project file access is incomplete, confusing, or inconsistent.Do not ask the operator to re-answer these decisions.## A. Current taskGenerate only the first Claude-native Apex skill package:```txt.claude/skills/apex-plan/
```

This is a package-generation task, not a new research task.

## B. Files expected in project resources

Use these project resources if accessible:

```
Phase-7.txtPhase 7 Package Readiness.txtDeep Research Phase Split.txtApex_Alfred_Skill_Definition_Guide.mdchatgpt_extended_thinking_skill_process_file_flow.mdchatgpt_extended_thinking_skill_process_source_index.mdProThinkingGPT_Harmonization_v1.mdAPEX HARMONIZATION — AGENT MODE INIT DOCUMENT_v2.md
```

If one or more files cannot be accessed, continue using this capsule. Do not stop unless the `apex-plan` package cannot be generated without inventing behavior.

## C. Phase 7 readiness results

```
phase_7_readiness:  apex_plan:    status: READY_FOR_GENERATION    confidence: 88    generate_order: 1    reason: >      A_PLAN has strong basis for project capture, decomposition,      dependency proposals, priority/urgency rationale, and provisional      focus recommendation. PM2 passed Phase 6 using CCPM + Backlog +      CrewAI task.py substitute.    required_label:      - CrewAI_task_py_SUBSTITUTE    boundary:      no_scripts: true      no_state_mutation: true      planning_only: true  apex_session:    status: READY_WITH_CUSTOM_PYTHON_WORK    confidence: 78    generate_order: 2    reason: >      C_SESSION is mostly grounded for handoff, session continuity,      gated mutation, and progress capture. PD3/reverse-unlock support      remains custom or boundary-sensitive.    do_not_generate_now: true  apex_sync:    status: PARTIAL_READY_WITH_GAPS    conditional_status_if_custom_apex_python_accepted: READY_WITH_CUSTOM_PYTHON_WORK    confidence: 62    generate_order: 3    reason: >      B_SYNC has known gaps around blocker scan, stale detection,      registry rebuild, drift detection, exact update-index behavior,      Kanban blocker scripts, OpenClaw TaskFlow, and Hermes governance.    do_not_generate_now: true
```

## D. Locked operator decisions

```
operator_decisions:  accept_CrewAI_task_py_substitute:    decision: true    label_required: CrewAI_task_py_SUBSTITUTE    constraint: >      Use CrewAI task.py only as substitute task-contract evidence.      Do not claim it is the original CrewAI getting-started source.  accept_custom_Apex_Python_for_B_SYNC:    decision: true    constraint: >      Relevant only for future apex-sync generation. Any custom sync      behavior must be labeled as custom Apex Python, not copied source behavior.  canonical_script_root:    decision: scripts/    constraint: >      Preserve H2. Treat apex-meta/scripts as path drift unless H2 is      explicitly amended later.  generate_apex_plan_first:    decision: true  apex_sync_generation_policy:    decision: custom_scope_later    constraint: >      Do not generate apex-sync now. Future apex-sync may be generated only      as READY_WITH_CUSTOM_PYTHON_WORK, not as fully source-backed.
```

## E. Locked H1–H7 project decisions

```
H1_status_enum:  - open  - in-progress  - blocked  - done  - deferredH2_base_path:  state_root: apex-meta/  subdirs:    - apex-meta/harmonization/    - apex-meta/epics/    - apex-meta/handoff/    - apex-meta/registry/  scripts_root: scripts/  skills_root: .claude/skills/H3_dependency_field:  name: depends_on  type: int_array  actionable_rule: all_depends_on_items_must_be_doneH4_script_language: Python onlyH5_clusters:  A_PLAN:    - PM1    - PM2    - PM3    - PD1    - PD2    - PD4  B_SYNC:    - PM4    - PM5    - PM7    - PM8    - KB4    - KB5  C_SESSION:    - PM6    - KB1    - KB2    - KB3    - KB6    - PD3    - PD5    - PD6H6_handoff_format:  files:    - task_plan.md    - findings.md    - progress.md    - next-session.md  next_session_sections:    - Current Step    - Open Items    - Risks    - Decisions Made    - Next ActionsH7_priority_urgency:  priority:    high: 3    medium: 2    low: 1  urgency: due_date_days_until_due_or_999
```

## F. `apex-plan` package boundary

`apex-plan` may:

- capture project/task intent
- clarify operator intent
- decompose work into epics and task candidates
- propose `depends_on` relationships
- propose status labels from H1
- suggest priority and urgency inputs from H7
- prepare operator-gated planning packets
- hand exact computation to `apex-sync`
- hand mutation/session continuity to `apex-session`

`apex-plan` must not:

- run scripts
- mutate repo or project state
- rebuild registries
- compute exact next task
- scan blockers
- perform stale detection
- write handoff files
- own session mutation
- claim missing or substituted sources as direct evidence

## G. Required generated package

Generate exactly:

```
.claude/skills/apex-plan/  SKILL.md  references/    planning-contract.md    task-decomposition-rules.md    dependency-and-priority-rules.md    operator-gate.md    source-basis.md  package-manifest.md
```

Do not generate other files.

## H. Evidence fallback rule

If project files are unavailable or partially unavailable:

1. Continue using this capsule.
2. Mark the source-basis note as `capsule_based`.
3. Do not invent additional evidence.
4. Do not reopen decisions.
5. Do not ask the operator to repeat decisions.
6. Generate the package anyway, as long as the package remains inside the planning-only boundary.

## I. Output discipline

The final answer must be file-ready.

Do not output a research report.

For each file, output:

1. target path
2. complete file content
3. short validation checklist
4. short source-basis note

Inside generated file contents:

- no citation markup
- no research narrative
- no private reasoning
- no broad architecture summary
- no unresolved option discussion

```
---## Simple Best SetupUse the Deep Research prompt like this:```txt1. Main controlled-generation prompt2. Access-Independent Decision Capsule3. Attach these files if the UI allows:   - Phase-7.txt   - Phase 7 Package Readiness.txt   - Apex_Alfred_Skill_Definition_Guide.md   - chatgpt_extended_thinking_skill_process_file_flow.md   - chatgpt_extended_thinking_skill_process_source_index.md
```

The **capsule is more important than the files**. It prevents the model from derailing if file access fails.

## Final Recommendation

Do **not** rely on Deep Research finding the right phase files by itself.

Use this rule:

```
deep_research_execution_rule:  primary_authority: embedded_decision_capsule  secondary_authority: attached_project_files  forbidden_behavior: rediscovering_or_reopening_phase_decisions  required_behavior: generate_file_ready_apex_plan_package
```

That should make the run much safer without over-engineering it.