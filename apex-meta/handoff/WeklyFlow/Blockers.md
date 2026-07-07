# 1. Executive blocker verdict

```yaml
executive_blocker_verdict:
  repo: leela-spec/apexai-os-meta
  branch: main
  inspected_at: 2026-07-07 Europe/Berlin
  overall_prompt_readiness_score_0_100: 58
  deep_research_ready: false
  patch_planning_ready: partially_false
  most_dangerous_blocker: "Path / manifest / entrypoint drift across root, PreCapWeek, PreCapNextDay, ProjectStatus, AIRouting."
  highest_leverage_fix: "Normalize live source authority map and align manifests to actual files before Deep Research."
  top_5_blockers:
    - blocker_id: PB001
      title: "Live skill paths and manifest-declared canonical paths conflict."
      affected_area: "root index, PreCapWeek, PreCapNextDay, ProjectStatus, AIRouting"
      severity_0_100: 96
    - blocker_id: PB002
      title: "PreCapNextDay entrypoint is wrapped in a markdown code fence."
      affected_area: "PreCapNextDay"
      severity_0_100: 94
    - blocker_id: PB003
      title: "PreCapWeek support files are declared but not discoverable in live package."
      affected_area: "PreCapWeek"
      severity_0_100: 92
    - blocker_id: PB004
      title: "Build residue remains in live invocation files."
      affected_area: "AIRouting, raw-flow-dump-normalize, status-merge"
      severity_0_100: 88
    - blocker_id: PB005
      title: "Operator-facing PreCapNextDay template is still table-first and lacks a compact success/result card."
      affected_area: "PreCapNextDay templates"
      severity_0_100: 82
```

**Verdict:** Step 1 is **not done**. Deep Research should not start yet because it would inspect mixed casing, stale manifests, code-fenced entrypoints, missing support files, and table-heavy output artifacts as if they were stable design inputs.

---

# 2. Source inventory

|Area|Actual path|Entrypoint exists|Manifest exists|Main templates exist|Main references exist|Drift|
|---|---|--:|--:|--:|--:|---|
|Root control|`.claude/Claude.md`|n/a|n/a|n/a|n/a|Core loop and artifact paths are collapsed one-line machine blocks.|
|PreCapWeek|`.claude/skills/PrecapWeek/`|yes, `Skill_Precap-Week.md`|yes|no templates declared|declared refs not discoverable|Manifest says canonical `.claude/skills/precap-week/` and `SKILL.md`, but live path/file differ.|
|PreCapNextDay|`.claude/skills/PrecapNextDay/`|yes, `Skill_precap-next-day.md`|yes|yes|yes|Manifest admits actual CamelCase path and future lowercase target.|
|raw-flow-dump-normalize|`.claude/skills/raw-flow-dump-normalize/`|yes|yes|yes|yes|Entry completion gate still validates package-build completion, not run-level output success.|
|flow-recap|`.claude/skills/flow-recap/`|yes|yes|yes|yes|Mostly boundary-safe; manifest still uses build-completion wording.|
|model-usage-log|`.claude/skills/model-usage-log/`|yes|yes|yes|yes|Mostly usable; learning signal exists but could be surfaced more plainly.|
|status-merge|`.claude/skills/status-merge/`|yes|yes|yes|yes|Interface boundary is good, but completion gate includes build-stage checks.|
|project-kb-manager|`.claude/skills/project-kb-manager/`|yes|yes|yes|yes|Manifest exposes state packet, but SKILL supporting files omit it.|
|ProjectStatus|`.claude/skills/ProjectStatus/`|yes, `project-status-overview_SKILL_v3.md`|yes|unclear/live mismatch|references mostly in `FirstIteration`|Manifest declares `.claude/skills/project-status-overview/SKILL.md`, not actual folder/file.|
|AIRouting|`.claude/skills/AIRouting/`|yes|yes|example only|yes but not under declared `references/`|Entrypoint and manifest declare lowercase `ai-routing-and-usage-tracking`; live folder is `AIRouting`.|

---

# 3. Prompt-blocker register

## PB001

```yaml
blocker_id: PB001
priority: P0
category:
  - path_and_manifest_drift
affected_files:
  - path: ".claude/Claude.md"
    observed_issue: "Root skill index points to actual mixed-case package paths."
  - path: ".claude/skills/PrecapWeek/package-manifest.md"
    observed_issue: "Manifest declares lowercase package path and SKILL.md, but actual package uses PrecapWeek/Skill_Precap-Week.md."
  - path: ".claude/skills/ProjectStatus/package-manifest.md"
    observed_issue: "Manifest declares project-status-overview/SKILL.md, but actual entrypoint is ProjectStatus/project-status-overview_SKILL_v3.md."
  - path: ".claude/skills/AIRouting/ai-routing-and-usage-tracking-package-manifest.md"
    observed_issue: "Manifest declares ai-routing-and-usage-tracking paths, but actual package is AIRouting."
recommended_fix_type: normalize_path_naming
patch_candidate: true
severity_0_100: 96
confidence_0_100: 98
```

**Evidence:** Root uses `.claude/skills/PrecapNextDay/Skill_precap-next-day.md`, `.claude/skills/PrecapWeek/Skill_Precap-Week.md`, `.claude/skills/ProjectStatus/project-status-overview_SKILL_v3.md`, and `.claude/skills/AIRouting/ai-routing-and-usage-tracking-SKILL.md` as live paths. PreCapWeek manifest instead declares `.claude/skills/precap-week/` and `SKILL.md`. ProjectStatus manifest declares `.claude/skills/project-status-overview/SKILL.md`. AIRouting manifest declares `.claude/skills/ai-routing-and-usage-tracking/SKILL.md`.

**Why it blocks Step 1:** A later research or patch prompt can open the wrong folder, infer a missing package, or edit a non-live target.

---

## PB002

```yaml
blocker_id: PB002
priority: P0
category:
  - machine_readability_issues
  - path_and_manifest_drift
affected_files:
  - path: ".claude/skills/PrecapNextDay/Skill_precap-next-day.md"
    observed_issue: "The whole SKILL file is wrapped as a fenced markdown block; frontmatter is not the first raw file content."
recommended_fix_type: remove_build_residue
patch_candidate: true
severity_0_100: 94
confidence_0_100: 99
```

**Evidence:** The file begins with a literal ```markdown fence before the YAML frontmatter and closes with a final code fence.

**Why it blocks Step 1:** Claude skill routing and repo patch prompts may treat the entrypoint as a quoted artifact instead of a live `SKILL.md`-style file.

---

## PB003

```yaml
blocker_id: PB003
priority: P0
category:
  - path_and_manifest_drift
  - downstream_confusion
affected_files:
  - path: ".claude/skills/PrecapWeek/Skill_Precap-Week.md"
    observed_issue: "Supporting files are declared, but live package references are not discoverable."
  - path: ".claude/skills/PrecapWeek/package-manifest.md"
    observed_issue: "Manifest declares exact reference files that appear absent from the live package."
recommended_fix_type: align_manifest_to_actual_files
patch_candidate: true
severity_0_100: 92
confidence_0_100: 94
```

**Evidence:** PreCapWeek entrypoint lists six support files including `references/calendar-planning-guidance.md` and `references/weekly-plan-output-contract.md`. The manifest declares the same exact reference set. Search for `weekly-plan-output-contract.md` returned the manifest/entrypoint and old-version locations, not a live `.claude/skills/PrecapWeek/references/...` file.

**Why it blocks Step 1:** The weekly-to-daily handoff is not inspectable if the support contracts named by PreCapWeek are missing.

---

## PB004

```yaml
blocker_id: PB004
priority: P0
category:
  - collapsed_or_unreadable_blocks
  - machine_readability_issues
affected_files:
  - path: ".claude/Claude.md"
    observed_issue: "Core loop, operator gates, and artifact paths are collapsed into one-line YAML-like blocks."
  - path: ".claude/skills/PrecapWeek/Skill_Precap-Week.md"
    observed_issue: "Skill contract, supporting files, failure modes, and completion gate are collapsed into one-line fenced blocks."
recommended_fix_type: split_collapsed_block
patch_candidate: true
severity_0_100: 90
confidence_0_100: 99
```

**Evidence:** Root `core_loop`, `operator_gates`, and `artifact_paths` are single-line blocks. PreCapWeek has collapsed `skill_contract`, `supporting_files`, `failure_modes`, and `completion_gate` blocks.

**Why it blocks Step 1:** Later output-design research needs a human-readable source map; collapsed blocks push research toward schema confusion and parsing mistakes.

---

## PB005

```yaml
blocker_id: PB005
priority: P1
category:
  - build_residue
affected_files:
  - path: ".claude/skills/AIRouting/ai-routing-and-usage-tracking-SKILL.md"
    observed_issue: "Live entrypoint contains VALIDATION file-specific checklist and NEXT PROMPT package-building residue."
  - path: ".claude/skills/AIRouting/ai-routing-and-usage-tracking-package-manifest.md"
    observed_issue: "Manifest contains NEXT PROMPT for building the next package."
  - path: ".claude/skills/raw-flow-dump-normalize/SKILL.md"
    observed_issue: "Completion gate checks package creation, not invocation output success."
  - path: ".claude/skills/status-merge/SKILL.md"
    observed_issue: "Completion gate checks package creation artifacts."
recommended_fix_type: remove_build_residue
patch_candidate: true
severity_0_100: 88
confidence_0_100: 98
```

**Evidence:** AIRouting entrypoint includes `# VALIDATION — FILE-SPECIFIC CHECKS` and `# NEXT PROMPT`. AIRouting manifest also includes `# NEXT PROMPT`. raw-flow-dump-normalize checks `package_path_created`, `raw_flow_dump_contract_created`, and similar build-stage fields. status-merge completion gate checks `package_path_created`, `template_created`, and `manifest_created`.

**Why it blocks Step 1:** Live skill invocation files should tell Claude how to run the skill, not how the package was built.

---

## PB006

```yaml
blocker_id: PB006
priority: P1
category:
  - output_design_confusers
affected_files:
  - path: ".claude/skills/PrecapNextDay/templates/next-day-plan-operator-template.md"
    observed_issue: "Main next_day_plan operator template is table-first and lacks a compact success/result card before details."
recommended_fix_type: add_operator_success_signal_placeholder
patch_candidate: true
severity_0_100: 82
confidence_0_100: 95
```

**Evidence:** The template moves from `Plan Status` directly into wide tables for review items, input context, flow overview, generated file index, capture artifacts, and review flags. The design reference currently legitimizes tables for flow overview, generated file index, input context, operator flags, and workflow blocks.

**Why it blocks Step 1:** A Deep Research prompt about output design may optimize the existing table-first template instead of questioning the interaction model.

---

## PB007

```yaml
blocker_id: PB007
priority: P1
category:
  - boundary_confusion
  - downstream_confusion
affected_files:
  - path: ".claude/skills/project-kb-manager/SKILL.md"
    observed_issue: "The new orchestration state packet is in the manifest but not in the SKILL supporting file map."
recommended_fix_type: add_operator_success_signal_placeholder
patch_candidate: true
severity_0_100: 78
confidence_0_100: 96
```

**Evidence:** project-kb-manager `SKILL.md` supporting files list project schema, domain overlays, milestone logic, write rules, project-record template/example, and manifest, but not the orchestration state packet contract/template. The manifest indexes `references/apex-orchestration-state-packet-contract.md` and `templates/apex-orchestration-state-packet-template.md`.

**Why it blocks Step 1:** The state handoff layer exists, but the live entrypoint does not expose it as an invocation-time support file.

---

## PB008

```yaml
blocker_id: PB008
priority: P1
category:
  - path_and_manifest_drift
  - downstream_confusion
affected_files:
  - path: ".claude/skills/PrecapNextDay/references/prompt-engineering-dependency-contract.md"
  - path: ".claude/skills/PrecapNextDay/references/usage-tracking-dependency-contract.md"
  - path: ".claude/skills/PrecapNextDay/references/workflow-process-validation-contract.md"
    observed_issue: "Dependency contracts name lowercase upstream package paths that differ from live root skill index paths."
recommended_fix_type: normalize_path_naming
patch_candidate: true
severity_0_100: 76
confidence_0_100: 93
```

**Evidence:** Root index says PromptEngineer lives at `.claude/skills/PromptEngineer/SKILL_prompt-engineering.md`, WorkflowProcesses at `.claude/skills/Workflow&Processes/workflow-process-design-SKILL.md`, and AIRouting at `.claude/skills/AIRouting/ai-routing-and-usage-tracking-SKILL.md`. PreCapNextDay contracts refer to lowercase `.claude/skills/prompt-engineering/`, `.claude/skills/ai-routing-and-usage-tracking/`, and `.claude/skills/workflow-process-design/`.

**Why it blocks Step 1:** Downstream dependency inspection can silently target non-live package paths.

---

## PB009

```yaml
blocker_id: PB009
priority: P2
category:
  - output_design_confusers
  - machine_readability_issues
affected_files:
  - path: ".claude/skills/model-usage-log/templates/model-usage-delta-template.md"
    observed_issue: "Route signal exists, but the operator-facing learning takeaway is not promoted as a plain top-level learning summary."
recommended_fix_type: add_operator_success_signal_placeholder
patch_candidate: true
severity_0_100: 62
confidence_0_100: 84
```

**Evidence:** The template has `Route Reuse / Avoid Signal` and `next_PreCapNextDay_hint`, but it sits as a YAML-oriented section after planned/actual details.

**Why it blocks Step 1:** Future design work may miss that the real output value is the learning signal, not the usage delta schema.

---

# 4. Fix-first batch plan

```yaml
fix_first_batches:
  - batch_id: B1
    title: Root loop and source authority cleanup
    goal: Make `.claude/Claude.md` readable and align the live skill index with actual/canonical path policy.
    files:
      - path: ".claude/Claude.md"
    fixes_blockers:
      - PB001
      - PB004
    risk_level: low
    should_patch_before_deep_research: true
    expected_value: "Deep Research can trust the loop and source map."

  - batch_id: B2
    title: PreCapWeek handoff integrity
    goal: Fix PreCapWeek entrypoint formatting and either create or remove stale declared support-file references.
    files:
      - path: ".claude/skills/PrecapWeek/Skill_Precap-Week.md"
      - path: ".claude/skills/PrecapWeek/package-manifest.md"
      - path: ".claude/skills/PrecapWeek/references/*"
    fixes_blockers:
      - PB003
      - PB004
    risk_level: medium
    should_patch_before_deep_research: true
    expected_value: "Weekly-to-daily seed becomes inspectable."

  - batch_id: B3
    title: Manifest and path alignment
    goal: Normalize or explicitly bridge actual vs canonical paths across PreCapNextDay, ProjectStatus, AIRouting, PromptEngineer, and WorkflowProcesses.
    files:
      - path: ".claude/skills/PrecapNextDay/precap-next-day-package-manifest.md"
      - path: ".claude/skills/ProjectStatus/package-manifest.md"
      - path: ".claude/skills/AIRouting/ai-routing-and-usage-tracking-package-manifest.md"
      - path: ".claude/skills/PrecapNextDay/references/*dependency-contract.md"
    fixes_blockers:
      - PB001
      - PB008
    risk_level: medium
    should_patch_before_deep_research: true
    expected_value: "Patch prompts stop opening wrong files."

  - batch_id: B4
    title: Remove build residue
    goal: Remove `NEXT PROMPT`, validation checklist residue, and package-build completion gates from live invocation files.
    files:
      - path: ".claude/skills/AIRouting/ai-routing-and-usage-tracking-SKILL.md"
      - path: ".claude/skills/AIRouting/ai-routing-and-usage-tracking-package-manifest.md"
      - path: ".claude/skills/raw-flow-dump-normalize/SKILL.md"
      - path: ".claude/skills/status-merge/SKILL.md"
    fixes_blockers:
      - PB005
    risk_level: low
    should_patch_before_deep_research: true
    expected_value: "Live skills no longer look like package-build prompts."

  - batch_id: B5
    title: Output success signal placeholders
    goal: Add minimal operator-facing result/success cards without designing the final template family.
    files:
      - path: ".claude/skills/PrecapNextDay/templates/next-day-plan-operator-template.md"
      - path: ".claude/skills/PrecapNextDay/references/operator-output-format-design.md"
      - path: ".claude/skills/model-usage-log/templates/model-usage-delta-template.md"
    fixes_blockers:
      - PB006
      - PB009
    risk_level: medium
    should_patch_before_deep_research: true
    expected_value: "Deep Research can ask what outputs should feel like, not merely how tables should look."

  - batch_id: B6
    title: State handoff visibility
    goal: Expose apex_orchestration_state_packet through project-kb-manager SKILL.md support map.
    files:
      - path: ".claude/skills/project-kb-manager/SKILL.md"
      - path: ".claude/skills/project-kb-manager/package-manifest.md"
    fixes_blockers:
      - PB007
    risk_level: low
    should_patch_before_deep_research: true
    expected_value: "PreCapWeek and PreCapNextDay have a visible state-source bridge."
```

---

# 5. Deep Research readiness checklist

```yaml
deep_research_readiness_checklist:
  source_authority_clear:
    status: fail
    blockers:
      - PB001
      - PB004

  skill_inventory_reliable:
    status: fail
    blockers:
      - PB001
      - PB002
      - PB003
      - PB008

  PreCapWeek_to_PreCapNextDay_handoff_reliable:
    status: fail
    blockers:
      - PB003
      - PB007

  output_artifact_names_stable:
    status: partial
    blockers:
      - PB001
      - PB008

  stale_build_residue_removed_or_marked:
    status: fail
    blockers:
      - PB005

  operator_success_signal_placeholders_present:
    status: fail
    blockers:
      - PB006
      - PB009

  final_verdict:
    ready_for_deep_research: false
    minimum_required_fixes_before_research:
      - batch_id: B1
      - batch_id: B2
      - batch_id: B3
      - batch_id: B4
      - batch_id: B5
      - batch_id: B6
```

---

# 6. Patch protocol note

```yaml
patch_protocol:
  required:
    - use_real_local_clone
    - start_from_current_main
    - edit_real_files
    - generate_patch_with_git_diff
    - validate_with_git_apply_check
    - run_disposable_apply_validation
    - report_exact_files_changed
  forbidden:
    - patch_from_memory
    - patch_from_connector_excerpt_only
    - claim_validation_without_git
    - mutate_state_or_run_APEX_work
```

---

# 7. Final recommendation

```yaml
final_step_1_recommendation:
  should_fix_before_deep_research: true
  minimum_fix_batches:
    - batch_id: B1
    - batch_id: B2
    - batch_id: B3
    - batch_id: B4
    - batch_id: B5
    - batch_id: B6
  can_deep_research_start_if_unfixed: false
  reason: >
    The later Deep Research run would otherwise inspect a repo with collapsed
    root loop blocks, missing PreCapWeek support files, code-fenced PreCapNextDay
    entrypoint content, path/casing drift across live packages, live build
    residue, and table-first operator templates without success-signal anchors.
  next_prompt_to_run_after_step_1:
    - "APEX Operator Output Design Deep Research Prompt"
```

**Bottom line:** fix Step 1 first. The repo is architecturally close, but not yet prompt-safe enough for output-design Deep Research.