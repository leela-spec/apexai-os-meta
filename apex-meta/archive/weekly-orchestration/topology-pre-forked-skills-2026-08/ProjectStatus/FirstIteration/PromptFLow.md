# Prompt Flow — Create `project-status-overview` Claude Skill Package

```yaml
prompt_flow_metadata:
  id: create-project-status-overview-skill-package-v0-1
  target_skill_name: project-status-overview
  target_package_scope: Claude-native skill package
  output_mode: one_file_per_prompt
  operator_copy_mode: true
  file_creation_location: chat_output_only
  purpose: >
    Create the Claude-native skill package that defines and runs the compact
    cross-project Project Status Overview aggregator.

binding_decisions:
  overview_role: >
    The Project Status Overview is a compact cross-project aggregator. It is not
    the detailed project database. Detailed project state lives inside individual
    project realms.
  hierarchy:
    - project
    - task
    - subtask
  forbidden_primary_layers:
    - workstreams
    - project_ids
    - heavy_chunk_ids
    - decision_registry
    - artifact_registry
    - patch_registry
    - detailed_project_state
  allowed_light_layers:
    - blockers_optional
    - archive_optional
    - unassigned_items
    - source_notes_optional
  metric_format:
    syntax: "[priority/urgency/date]"
    priority_range: 1-100
    urgency_range: 1-100
    date_format: "DD-MM or NA"
    example: "[77/30/14-08]"
  ranking_rule:
    primary: deadline_first
    secondary: priority
    tertiary: urgency
    manual_override: always_true
  compact_display_format: |
    Project Name
      - task-label: task-name [prio/urgency/date]
      --- subtask-label: subtask-name [prio/urgency/date]
  canonical_projects_initial:
    - Leela
    - Apex
    - MasterOfArts
    - Investment
    - Others
  unassigned_policy: >
    Unassigned infos, tasks, and project candidates live in a temporary holding
    area. As soon as they are assigned to a project, they are removed from the
    unassigned area.
```

---

# Global rules for every prompt in this flow

```yaml
global_output_contract:
  produce_exactly_one_file_per_prompt: true
  include_file_path_header: true
  no_extra_commentary_outside_required_sections: true

allowed_paths:
  - .claude/skills/project-status-overview/SKILL.md
  - .claude/skills/project-status-overview/references/project-status-overview-contract.md
  - .claude/skills/project-status-overview/templates/current-project-status-overview-template.md
  - .claude/skills/project-status-overview/examples/starter-manual-test-overview.md
  - .claude/skills/project-status-overview/references/ranking-and-validation-rules.md
  - .claude/skills/project-status-overview/package-manifest.md

forbidden_outputs:
  - repo_setup_files
  - CI_or_deployment_files
  - runtime_state_files
  - task_board_files
  - scheduler_files
  - workflow_index
  - additional_permanent_agents
  - project_database_files
  - detailed_project_realm_files

language_rules:
  use_claude_native_language: true
  avoid_legacy_runtime_language: true
  avoid_over_engineering: true
  keep_files_compact: true
  prefer_yaml_and_compact_examples: true
```

---

# Prompt 0 — Package plan validation

````text
We are creating the Claude-native skill package `.claude/skills/project-status-overview/`.

Before creating files, produce the package plan only.

Use these fixed decisions:

- The skill is a compact cross-project aggregator.
- It summarizes project-level tasks and subtasks from deeper individual project realms.
- It does not become the detailed project database.
- The hierarchy is: project → task → subtask.
- Do not use workstreams.
- Do not use project IDs in the human-facing output.
- Do not create heavy chunk IDs.
- Use compact rating syntax: `[priority/urgency/date]`, where priority and urgency are 1-100 and date is `DD-MM` or `NA`.
- Ranking rule: deadline first, then priority, then urgency.
- Manual override is always allowed.
- Unassigned infos/tasks/project candidates live in a temporary unassigned area. Once assigned to a project, remove them from the unassigned area.
- Initial projects: Leela, Apex, MasterOfArts, Investment, Others.

Output exactly:

# Project Status Overview Skill Package — Plan

## 1 Confirmed decisions

## 2 Proposed file list

Use this exact file list unless you find a strong reason to remove a file:

```txt
.claude/skills/project-status-overview/SKILL.md
.claude/skills/project-status-overview/references/project-status-overview-contract.md
.claude/skills/project-status-overview/templates/current-project-status-overview-template.md
.claude/skills/project-status-overview/examples/starter-manual-test-overview.md
.claude/skills/project-status-overview/references/ranking-and-validation-rules.md
.claude/skills/project-status-overview/package-manifest.md
````

## 3 File purpose map

## 4 Boundary map

## 5 Final package creation sequence

## 6 Validation checks

Do not create any final file yet.

````

---

# Prompt 1 — Create `SKILL.md`

```text
Create exactly one file.

# FILE: .claude/skills/project-status-overview/SKILL.md

Requirements:

- Claude-native `SKILL.md`.
- Compact and under 500 lines.
- Frontmatter must include only:
  - name
  - description
- name: project-status-overview
- description must clearly trigger when the operator asks Claude to create, normalize, update, rank, or validate a compact cross-project project status overview.
- The skill must produce a compact project status overview from manual notes, project-specific status summaries, previous overview text, or unassigned incoming items.
- The skill must not create weekly plans, daily plans, execute project work, merge flow recaps as status-merge, or become a detailed project database.
- Use project → task → subtask wording.
- Do not use workstreams.
- Do not require project IDs.
- Do not require heavy task IDs.
- Include the compact output syntax:
  Project Name
    - task-label: task-name [prio/urgency/date]
    --- subtask-label: subtask-name [prio/urgency/date]
- Procedure must include:
  1. Load supplied context.
  2. Separate assigned project material from unassigned material.
  3. Normalize into projects, tasks, subtasks.
  4. Preserve or add metrics in `[prio/urgency/date]`.
  5. Rank tasks deadline-first, then priority, then urgency.
  6. Apply manual override if operator supplied one.
  7. Surface blockers only when present.
  8. Produce unassigned section only for unresolved incoming material.
  9. Validate that no detailed project database was created.
  10. Present final overview for operator review.
- Reference supporting files:
  - `references/project-status-overview-contract.md`
  - `templates/current-project-status-overview-template.md`
  - `references/ranking-and-validation-rules.md`

After file content, output:

---

# VALIDATION CHECKLIST

- [ ] Exactly one file was produced.
- [ ] File path is `.claude/skills/project-status-overview/SKILL.md`.
- [ ] The skill is compact and Claude-native.
- [ ] The skill uses project → task → subtask.
- [ ] The skill does not use workstreams.
- [ ] The skill does not create detailed project-state files.
- [ ] The skill uses `[priority/urgency/date]`.
- [ ] Ranking is deadline-first with manual override.
````

---

# Prompt 2 — Create artifact contract reference

```text
Create exactly one file.

# FILE: .claude/skills/project-status-overview/references/project-status-overview-contract.md

Purpose:
Define the compact artifact contract for `current_project_status_overview`.

Requirements:
- YAML-first.
- No long prose.
- Define the human-readable compact output format:
  Project Name
    - task-label: task-name [prio/urgency/date]
    --- subtask-label: subtask-name [prio/urgency/date]
- Define the internal normalized structure:
  - overview_metadata
  - project_sections
  - ranked_task_view
  - unassigned_items
  - optional_archive
  - validation_record
- Project sections must use project name, not project ID.
- Task fields:
  - task_label
  - task_name
  - rating
  - subtasks optional
  - blocker optional
  - source_note optional
- Subtask fields:
  - subtask_label
  - subtask_name
  - rating
  - blocker optional
- Rating syntax:
  - `[priority/urgency/date]`
  - priority 1-100
  - urgency 1-100
  - date `DD-MM` or `NA`
- Define unassigned item policy:
  - may contain info, task, project_candidate
  - removed when assigned to a project
- Define archive as optional only.
- Define non-goals:
  - no detailed project database
  - no workstreams
  - no status-merge
  - no weekly plan
  - no next-day plan
  - no automatic project execution

After file content, output:

---

# VALIDATION CHECKLIST

- [ ] Exactly one file was produced.
- [ ] Contract uses project → task → subtask.
- [ ] No workstream layer exists.
- [ ] No project IDs are required.
- [ ] Rating format is defined.
- [ ] Unassigned policy is defined.
- [ ] Archive is optional only.
```

---

# Prompt 3 — Create template file

```text
Create exactly one file.

# FILE: .claude/skills/project-status-overview/templates/current-project-status-overview-template.md

Purpose:
Create a reusable blank template for the compact project status overview.

Requirements:
- Include a short YAML metadata block.
- Include compact human-readable project sections.
- Include initial project headings:
  - Leela
  - Apex
  - MasterOfArts
  - Investment
  - Others
- Under each project, include placeholder task lines using:
  - task-label: task-name [prio/urgency/date]
  --- subtask-label: subtask-name [prio/urgency/date]
- Include a `Ranked Task View` section.
- Include an `Unassigned` section.
- Include an optional `Archive` section.
- Include an `Operator Validation` section.
- Keep the template copy-paste friendly.
- Do not include long explanations.

After file content, output:

---

# VALIDATION CHECKLIST

- [ ] Exactly one file was produced.
- [ ] Template contains Leela, Apex, MasterOfArts, Investment, Others.
- [ ] Template uses compact task/subtask syntax.
- [ ] Template includes ranked task view.
- [ ] Template includes unassigned section.
- [ ] Archive is optional.
```

---

# Prompt 4 — Create starter manual test example

```text
Create exactly one file.

# FILE: .claude/skills/project-status-overview/examples/starter-manual-test-overview.md

Purpose:
Create a filled example for the first manual test run of the Project Status Overview.

Use this seed state:

Apex:
- Highest current priority.
- Current focus: define project status overview / aggregation format and skill package.
- Next: define output documents for the file system.
- Later: implement Claude-side automation.
- Later: supplement for Hermes.

Leela:
- Core priority: spatial design system.
- Subtasks:
  - research Flutter best practices for spatial design possibilities
  - create/formalize spatial design aspects
  - fill with content
- Overlap with MasterOfArts content.

MasterOfArts:
- First: website skeleton content.
- Then: actual website execution.
- Business plan is also a priority.

Investment:
- Active but paused.

Others:
- Inbox/candidate container.

Requirements:
- Use compact output syntax:
  Project Name
    - task-label: task-name [prio/urgency/date]
    --- subtask-label: subtask-name [prio/urgency/date]
- Invent reasonable starter ratings for test purposes, but mark them as operator-review-needed.
- Use deadline `NA` unless a real date is known.
- Include a ranked task view using deadline-first, then priority, then urgency.
- Include manual override field as empty.
- Include an unassigned section.
- Do not create workstreams.
- Do not create a detailed project database.

After file content, output:

---

# VALIDATION CHECKLIST

- [ ] Exactly one file was produced.
- [ ] Example uses all five initial projects.
- [ ] Example uses `[prio/urgency/date]`.
- [ ] Example has ranked task view.
- [ ] Example marks starter ratings as review-needed.
- [ ] Example does not use workstreams.
```

---

# Prompt 5 — Create ranking and validation rules

```text
Create exactly one file.

# FILE: .claude/skills/project-status-overview/references/ranking-and-validation-rules.md

Purpose:
Define the ranking, validation, and failure rules for the compact project status overview.

Requirements:
- YAML-first.
- Define rating parser:
  - priority 1-100
  - urgency 1-100
  - date `DD-MM` or `NA`
- Define ranking rule:
  1. Manual override/pinned order if present.
  2. Deadline-first.
  3. Priority second.
  4. Urgency third.
- Define deadline pressure:
  - real date beats `NA` when date is soon
  - overdue/near deadline rises highest
  - `NA` does not mean unimportant
- Define manual override:
  - operator may pin, demote, promote, or freeze tasks
  - manual override beats automatic ranking
- Define validation checks:
  - every rating must match `[number/number/date-or-NA]`
  - priority and urgency must be 1-100
  - every task must belong to a project or unassigned
  - unassigned item must be removed once assigned
  - no workstream section
  - no detailed project-state expansion
  - blockers only appear when present
- Define failure modes:
  - missing metrics
  - invalid date
  - over-detailed project expansion
  - unassigned item duplicated after assignment
  - ranking conflict between deadline and manual override
- Define correction behavior:
  - preserve operator override
  - ask for review only when needed
  - mark uncertain ratings as operator-review-needed

After file content, output:

---

# VALIDATION CHECKLIST

- [ ] Exactly one file was produced.
- [ ] Ranking rule is deadline-first with manual override.
- [ ] Validation checks match the compact model.
- [ ] Failure modes prevent over-engineering.
```

---

# Prompt 6 — Create package manifest

```text
Create exactly one file.

# FILE: .claude/skills/project-status-overview/package-manifest.md

Purpose:
Create the package manifest for the `project-status-overview` Claude skill package.

Requirements:
- List every package file:
  - `.claude/skills/project-status-overview/SKILL.md`
  - `.claude/skills/project-status-overview/references/project-status-overview-contract.md`
  - `.claude/skills/project-status-overview/templates/current-project-status-overview-template.md`
  - `.claude/skills/project-status-overview/examples/starter-manual-test-overview.md`
  - `.claude/skills/project-status-overview/references/ranking-and-validation-rules.md`
  - `.claude/skills/project-status-overview/package-manifest.md`
- For each file, include:
  - purpose
  - when Claude should read it
  - validation role
- Include package-level boundaries:
  - compact aggregator only
  - no workstreams
  - no detailed project database
  - no weekly plan
  - no next-day plan
  - no status-merge
- Include package-level acceptance checks.
- Include first manual test instruction:
  - Run the skill using the starter example.
  - Ask it to produce a compact current project status overview.
  - Check that output uses project → task → subtask.
  - Check ranked task view.
  - Check unassigned section.
  - Check that no workstream layer appears.

After file content, output:

---

# VALIDATION CHECKLIST

- [ ] Exactly one file was produced.
- [ ] Manifest lists all package files.
- [ ] Manifest defines package boundaries.
- [ ] Manifest includes first manual test instruction.
```

---

# Final package acceptance criteria

```yaml
package_acceptance:
  required_files:
    - .claude/skills/project-status-overview/SKILL.md
    - .claude/skills/project-status-overview/references/project-status-overview-contract.md
    - .claude/skills/project-status-overview/templates/current-project-status-overview-template.md
    - .claude/skills/project-status-overview/examples/starter-manual-test-overview.md
    - .claude/skills/project-status-overview/references/ranking-and-validation-rules.md
    - .claude/skills/project-status-overview/package-manifest.md

  must_pass:
    - skill_is_compact_aggregator
    - hierarchy_is_project_task_subtask
    - no_workstreams
    - no_project_id_requirement
    - no_heavy_chunk_id_requirement
    - rating_format_is_priority_urgency_date
    - ranking_is_deadline_first_priority_second_urgency_third
    - manual_override_always_true
    - unassigned_items_removed_when_assigned
    - detailed_project_state_lives_elsewhere
```