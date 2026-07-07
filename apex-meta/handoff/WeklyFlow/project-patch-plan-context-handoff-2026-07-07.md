# Project Context Handoff — APEX Step 1 Prompt-Blocker Cleanup Patch Plan

## Purpose of this handoff

This handoff explains the **project context** and **patch plan context** for another AI.

It is not another Agent Mode prompt.
It is not a prompt-reproduction guide.
It is not a generic patching-process document.

It answers:

1. Where is the patch plan?
2. What does the patch plan say?
3. Why does this patch plan exist in the APEX project?
4. Why is Agent Mode needed for this step?
5. What must the next AI understand before creating or executing any patch-pack builder prompt?

## 1. Where the patch plan is

Canonical patch plan path:

```text
apex-meta/patch-plans/2026-07-07-step1-prompt-blocker-cleanup-plan.okf.md
```

Related handoff copy / previous location:

```text
apex-meta/handoff/WeklyFlow/step1_prompt_blocker_cleanup_full_plan.okf.md
```

The canonical patch plan declares itself as:

```yaml
okf_schema: apex.agent_mode.git_native_patch_plan.v1
plan_id: 2026-07-07-step1-prompt-blocker-cleanup-full
status: ready_for_agent_mode_patch_pack_builder
created_for: APEX Step 1 prompt-blocker cleanup before operator-output Deep Research
repo: leela-spec/apexai-os-meta
branch: main
source_of_truth: live terminal Git repository
primary_blocker_source: Blockers.md
process_guide: AgentMode-GitNative-PatchPack-Process.okf.md
future_patch_pack_path: apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/
```

The file explicitly says it is the authoritative semantic source plan for the later Agent Mode patch-pack builder.

## 2. What the patch plan is

The patch plan is a **machine-readable source-grounded patch-pack plan** for cleaning prompt blockers before the next operator-output Deep Research step.

It is not the final implementation itself.
It is not an execution report.
It is not a generated patch pack.

It tells a later Agent Mode run how to create a validated Git-native patch pack containing:

- one patch per target file,
- a patch manifest,
- an apply handoff,
- a validation report,
- no final target-file implementation commit in the builder run.

The patch plan expects Agent Mode to:

1. read the plan,
2. read `Blockers.md`,
3. read the Git-native patch-pack process guide,
4. inspect the live repo files,
5. modify one target file at a time,
6. generate a Git diff patch for that one file,
7. revert the real target file,
8. validate every patch with `git apply --check`,
9. validate the cumulative patch sequence,
10. leave only patch-pack artifacts in the builder final state.

## 3. Why this patch plan exists in the APEX project

The APEX project is building a weekly/daily planning and orchestration loop around packages such as:

- PreCapWeek,
- PreCapNextDay,
- FlowRecap,
- raw-flow-dump-normalize,
- model-usage-log,
- status-merge,
- project-kb-manager,
- ProjectStatus,
- AIRouting.

Before deeper operator-output design work can happen, the project has prompt/blocker hygiene issues that could make a research or implementation agent misread the current architecture.

The patch plan exists because the later Deep Research run for operator-facing output design must not treat these as stable architecture:

- stale path maps,
- fenced skill entrypoints,
- missing support files,
- build residue in live skill files,
- collapsed one-line YAML-like control blocks,
- table-first operator templates without compact success signals,
- package-build completion gates where invocation-level gates are needed.

In other words:

> The patch plan is a cleanup layer before further research/design. It makes the repo readable, path-realistic, and less misleading for future APEX orchestration work.

## 4. What problem the patch plan fixes

The plan names several blocker classes:

### Path and package identity blockers

Some live packages use mixed-case/current paths while manifests or references point to lowercase/future canonical paths.

The cleanup does not normalize or move folders. It adds explicit distinction between:

```yaml
actual_live_path: current path in repo
canonical_target_path: future normalization target
```

This prevents future agents from treating future canonical paths as already existing files.

### Fenced or collapsed prompt files

Some live entrypoints or root control files contain collapsed or fenced blocks that are hard for an agent to read correctly, such as collapsed `core_loop`, `operator_gates`, `artifact_paths`, or skill contract blocks.

The cleanup expands these into readable YAML-style structures and removes inappropriate wrapper fences.

### Missing PreCapWeek support references

PreCapWeek references support files that are missing or not discoverable. The patch plan creates minimal live reference files for weekly planning, weekly output contract, blueprint examples, calendar proposal boundaries, and validation.

These files are needed so the weekly-to-daily handoff can be inspected instead of inferred.

### Build residue in live skill files

Some live skill files still contain package-construction residue such as `NEXT PROMPT`, package creation validation, or build handoff markers.

The cleanup removes build residue from invocation surfaces while preserving no-runtime, no-calendar, and no-state-overwrite safety boundaries.

### Completion gates at wrong level

Some packages validate whether a package was created instead of validating whether a run produced the right output.

The cleanup changes completion gates from package-build-level to invocation-output-level where needed.

### Operator output signal weakness

Some output templates are table-first and lack compact operator value signals.

The cleanup adds minimal result/learning cards before detailed tables, without doing the full later information-design research.

### State handoff visibility

The project-kb-manager package has state packet contract/template references that need to be more visible from the live SKILL entrypoint.

The cleanup exposes the `apex_orchestration_state_packet` handoff mode while keeping durable writes operator-gated and project-kb-manager-boundary-safe.

## 5. Why Agent Mode is needed

Agent Mode is needed because this is a multi-file, Git-native patch-pack creation task with strict artifact boundaries.

The task is not to directly change the final target files in the repository.

The task is to produce a patch pack that another deterministic applier can apply later.

Agent Mode is appropriate because it can:

- inspect live repo files,
- make temporary edits to one target at a time,
- generate real `git diff` patches,
- revert target files after generating each patch,
- run `git apply --check`,
- validate cumulative patch application,
- write a manifest and handoff,
- keep the final builder commit limited to patch artifacts.

This separation matters because the project wants:

```yaml
builder_run:
  creates: patch-pack artifacts
  does_not_create: final implementation commit

later_applier_run:
  applies: existing patch pack
  validates: target-file changes
  commits: implementation changes separately
```

This reduces the risk of accidentally mutating live skill files, state, calendars, old-version sources, or project KB data during the patch-pack construction phase.

## 6. What Agent Mode must not do

Agent Mode must not:

- run PreCapWeek,
- run PreCapNextDay,
- run FlowRecap,
- run raw-flow-dump-normalize,
- run model-usage-log,
- run status-merge,
- run APEX project work,
- merge canonical project status,
- mutate durable project state,
- edit `.claude/kb` data,
- create calendar events,
- create runtime automation, cron jobs, schedulers, or agents,
- redesign the final operator-facing output template family,
- normalize repository casing by moving folders,
- patch `source-knowledge` or `ApexDefinition&OldVersions`.

Agent Mode is only a patch-pack builder here.

## 7. Required read order from the patch plan

The patch plan defines this read order:

1. `AgentMode-GitNative-PatchPack-Process.okf.md`
   - Process doctrine for Git-native patch-pack creation.

2. `Blockers.md`
   - Primary blocker register with PB001-PB009 and B1-B6 fix-first batches.

3. `apex-meta/patch-plans/2026-07-07-step1-prompt-blocker-cleanup-plan.okf.md`
   - The canonical semantic plan.

4. Live source files, including:
   - `.claude/Claude.md`
   - `.claude/skills/PrecapWeek/Skill_Precap-Week.md`
   - `.claude/skills/PrecapWeek/package-manifest.md`
   - `.claude/skills/PrecapNextDay/Skill_precap-next-day.md`
   - `.claude/skills/PrecapNextDay/precap-next-day-package-manifest.md`
   - `.claude/skills/ProjectStatus/project-status-overview_SKILL_v3.md`
   - `.claude/skills/ProjectStatus/package-manifest.md`
   - `.claude/skills/AIRouting/ai-routing-and-usage-tracking-SKILL.md`
   - `.claude/skills/AIRouting/ai-routing-and-usage-tracking-package-manifest.md`
   - `.claude/skills/project-kb-manager/SKILL.md`
   - `.claude/skills/project-kb-manager/package-manifest.md`
   - `.claude/skills/raw-flow-dump-normalize/SKILL.md`
   - `.claude/skills/flow-recap/SKILL.md`
   - `.claude/skills/model-usage-log/SKILL.md`
   - `.claude/skills/status-merge/SKILL.md`
   - PreCapNextDay operator templates and dependency contracts
   - project-kb-manager state packet contract/template

5. Read-only recovery sources under `ApexDefinition&OldVersions/...` only if live references are missing or ambiguous.

## 8. The six improvement batches

| Batch | Patch IDs | Purpose |
|---|---|---|
| B1 | 001 | Make root loop/source authority readable and path-realistic. |
| B2 | 003-009 | Make PreCapWeek readable and make weekly-to-daily handoff support files inspectable. |
| B3 | 010, 013-016, 018 | Make actual vs canonical path policy explicit across dependent packages. |
| B4 | 017-020 | Remove package-construction residue from live invocation surfaces. |
| B5 | 011, 012, 022 | Add minimal operator value anchors before later output-design Deep Research. |
| B6 | 021 | Expose `apex_orchestration_state_packet` through project-kb-manager live entrypoint. |

These batches explain the project reason for the 22 individual patches.

## 9. The 22 required patch targets

The patch plan requires exactly 22 target files.

| ID | Target | Patch type | Project reason |
|---|---|---|---|
| 001 | `.claude/Claude.md` | modify | Root loop/source authority readability and actual/canonical path policy. |
| 002 | `.claude/skills/PrecapNextDay/Skill_precap-next-day.md` | modify | Remove wrapper code fence so frontmatter starts correctly. |
| 003 | `.claude/skills/PrecapWeek/Skill_Precap-Week.md` | modify | Expand collapsed contract/support/failure/completion blocks. |
| 004 | `.claude/skills/PrecapWeek/package-manifest.md` | modify | Align manifest with actual live mixed-case path and entrypoint. |
| 005 | `.claude/skills/PrecapWeek/references/calendar-planning-guidance.md` | create if missing | Clarify calendar proposal-only behavior. |
| 006 | `.claude/skills/PrecapWeek/references/weekly-plan-output-contract.md` | create if missing | Define weekly output and first PreCapNextDay seed boundary. |
| 007 | `.claude/skills/PrecapWeek/references/weekly-blueprint-standard.md` | create if missing | Provide minimal weekly blueprint standard. |
| 008 | `.claude/skills/PrecapWeek/references/weekly-blueprint-meeting-example.md` | create if missing | Provide inspectable meeting example for weekly blueprint. |
| 009 | `.claude/skills/PrecapWeek/references/validation-checklist.md` | create if missing | Validate weekly output/seed rather than package creation. |
| 010 | `.claude/skills/PrecapNextDay/precap-next-day-package-manifest.md` | modify | Strengthen actual/canonical path policy. |
| 011 | `.claude/skills/PrecapNextDay/references/operator-output-format-design.md` | modify | Add minimal result-card policy. |
| 012 | `.claude/skills/PrecapNextDay/templates/next-day-plan-operator-template.md` | modify | Add compact Result Card before detail tables. |
| 013 | `.claude/skills/PrecapNextDay/references/prompt-engineering-dependency-contract.md` | modify | Add actual-live/canonical-target path bridge. |
| 014 | `.claude/skills/PrecapNextDay/references/usage-tracking-dependency-contract.md` | modify | Add actual-live/canonical-target path bridge. |
| 015 | `.claude/skills/PrecapNextDay/references/workflow-process-validation-contract.md` | modify | Add actual-live/canonical-target path bridge. |
| 016 | `.claude/skills/ProjectStatus/package-manifest.md` | modify | Align ProjectStatus manifest with actual live path. |
| 017 | `.claude/skills/AIRouting/ai-routing-and-usage-tracking-SKILL.md` | modify | Remove build residue from invocation entrypoint. |
| 018 | `.claude/skills/AIRouting/ai-routing-and-usage-tracking-package-manifest.md` | modify | Remove residue and align path policy. |
| 019 | `.claude/skills/raw-flow-dump-normalize/SKILL.md` | modify | Replace package-build completion gate with run-output completion gate. |
| 020 | `.claude/skills/status-merge/SKILL.md` | modify | Replace package-build completion gate with merge-proposal completion gate. |
| 021 | `.claude/skills/project-kb-manager/SKILL.md` | modify | Expose orchestration state packet handoff mode/support files. |
| 022 | `.claude/skills/model-usage-log/templates/model-usage-delta-template.md` | modify | Add top-level Operator Learning Card. |

## 10. Forbidden paths and mutation guard

The patch plan forbids modifying:

```text
state/**
.claude/kb/**
source-knowledge/**
ApexDefinition&OldVersions/**
.github/workflows/**
scripts/**
**/*.py
**/*.json
**/*.yaml
**/*.yml
```

Allowed new paths are limited to the five PreCapWeek reference files and the patch-pack directory.

This is important because the cleanup must not become a repo-wide rewrite or implementation pass.

## 11. Patch-pack artifact contract

The patch pack must be created under:

```text
apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/
```

Required artifacts:

- `000-patch-manifest.md`
- `001-root-claude-loop-source-authority.patch`
- `002-precap-next-day-entrypoint-unfence.patch`
- `003-precap-week-entrypoint-readable.patch`
- `004-precap-week-manifest-actual-paths.patch`
- `005-precap-week-calendar-guidance.patch`
- `006-precap-week-output-contract.patch`
- `007-precap-week-blueprint-standard.patch`
- `008-precap-week-meeting-example.patch`
- `009-precap-week-validation-checklist.patch`
- `010-precap-next-day-path-policy.patch`
- `011-operator-output-design-result-card-policy.patch`
- `012-next-day-plan-result-card.patch`
- `013-prompt-engineering-path-bridge.patch`
- `014-usage-tracking-path-bridge.patch`
- `015-workflow-process-path-bridge.patch`
- `016-projectstatus-manifest-actual-paths.patch`
- `017-airouting-entrypoint-residue-removal.patch`
- `018-airouting-manifest-residue-and-paths.patch`
- `019-raw-flow-run-completion-gate.patch`
- `020-status-merge-run-completion-gate.patch`
- `021-project-kb-manager-state-handoff-exposure.patch`
- `022-model-usage-learning-card.patch`
- apply handoff file
- validation report

Note: the source plan currently says the apply handoff is `999-apply-patches.md`. Some later prompt variants used `999-codex-apply-handoff.md`. The next AI must resolve this by checking the current source plan and process guide, not by inventing a name.

## 12. Validation expected by the patch plan

Per patch:

- patch file is non-empty,
- patch touches exactly one target file,
- patch applies with `git apply --check` from clean base.

Cumulative:

- all patches pass apply-check in numeric order,
- all patches apply in numeric order,
- changed files equal the 22-target list exactly,
- all required markers from per-target contracts are present,
- all forbidden markers are absent,
- no forbidden path changes.

Done only when:

- all required patch-pack artifacts exist,
- exactly one Git-generated patch per target exists,
- cumulative validation passes,
- target files are reverted,
- patch artifacts only remain in builder final state,
- manifest and apply handoff are complete,
- Deep Research has not been started before the cleanup patch pack exists.

## 13. What the next AI should produce

The next AI should produce a handoff or prompt that clearly states:

1. The project purpose of this cleanup.
2. The canonical patch plan path.
3. The read order.
4. The 22 target files and patch files.
5. The B1-B6 improvement matrix.
6. The no-runtime/no-state/no-calendar/no-folder-normalization boundaries.
7. The Git-native patch-pack artifact contract.
8. The validation and done criteria.
9. Why Agent Mode is used: to create patch artifacts only, not final implementation changes.

The next AI should not focus primarily on debugging prior prompt failures unless explicitly asked.

## 14. One-sentence summary for another AI

The APEX Step 1 patch plan is a repo-local, machine-readable semantic plan at `apex-meta/patch-plans/2026-07-07-step1-prompt-blocker-cleanup-plan.okf.md`; it exists to clean path drift, fenced/collapsed prompt files, missing PreCapWeek references, build residue, weak output success signals, and state-handoff visibility before later operator-output research, using Agent Mode only as a Git-native patch-pack builder that produces validated patch artifacts without directly committing final target-file changes.