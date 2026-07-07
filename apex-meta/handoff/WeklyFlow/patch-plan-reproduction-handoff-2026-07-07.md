# Handoff — Reproduce the Step 1 Patch Plan / Patch-Pack Builder Instructions Without Drift

## Purpose

This handoff is for another AI that will work from the actual APEX Step 1 Prompt-Blocker Cleanup patch plan and project resources.

The operator clarified that the desired handoff is about the **patch plan**, not merely a prompt-reproduction task.

The task for the next AI is to understand the existing patch plan as the semantic source of truth, then create the minimal Agent Mode execution prompt or patch-pack-builder instructions from it without adding new repo-access, clone, local-path, fallback, or environment logic.

## Critical instruction

Do not invent a new patch plan.
Do not redesign the plan.
Do not create new targets.
Do not remove targets.
Do not add environment acquisition logic.

Use the existing patch plan as the authoritative semantic plan:

```text
apex-meta/patch-plans/2026-07-07-step1-prompt-blocker-cleanup-plan.okf.md
```

The plan already contains the mission, read order, evidence-discovery rules, source inventory, target file map, improvement matrix, per-target contracts, validation matrix, and done criteria.

## Primary repo resources to inspect

Inspect these in this order:

1. `apex-meta/patch-plans/2026-07-07-step1-prompt-blocker-cleanup-plan.okf.md`
   - Role: authoritative semantic patch plan.
   - It declares:
     - repo: `leela-spec/apexai-os-meta`
     - branch: `main`
     - source of truth: live terminal Git repository
     - future patch-pack path: `apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/`

2. `apex-meta/handoff/WeklyFlow/step1_prompt_blocker_cleanup_full_plan.okf.md`
   - Role: handoff copy / earlier location of the same full plan.
   - Use only as a cross-check if the canonical patch-plan path is unavailable or suspected incomplete.

3. `Blockers.md`
   - Role: blocker authority referenced by the plan.
   - Contains PB001-PB009 and fix-first batches B1-B6.
   - If exact root path is unclear, use repo search for `PB001`, `fix-first`, `B1`, `B6`, and `prompt blocker`.

4. `AgentMode-GitNative-PatchPack-Process.okf.md`
   - Role: process doctrine referenced by the plan.
   - If exact root path is unclear, use repo search for `Git-Native Patch-Pack Process`, `git apply --check`, and `patch artifacts only`.

5. The known working prompt example, if provided by the operator.
   - Role: structure/syntax/wording model only.
   - Do not use it as semantic authority for target content.

## What the patch plan already says

The canonical plan frontmatter establishes:

```yaml
okf_schema: apex.agent_mode.git_native_patch_plan.v1
plan_id: 2026-07-07-step1-prompt-blocker-cleanup-full
status: ready_for_agent_mode_patch_pack_builder
repo: leela-spec/apexai-os-meta
branch: main
source_of_truth: live terminal Git repository
primary_blocker_source: Blockers.md
process_guide: AgentMode-GitNative-PatchPack-Process.okf.md
future_patch_pack_path: apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/
```

The plan purpose says Agent Mode should read this plan first, read Blockers.md and the Git-native patch guide, inspect the live repo, then create one Git-generated patch per target file plus manifest and apply handoff.

## Patch-plan sections that must be treated as binding

### Section 1 — Mission Contract

Use this as the task contract:

- Create a validated Git-native patch pack.
- Output patch artifacts only.
- Do not create the implementation commit now.
- Do not create a PR now.
- Final builder state: target files not modified, patch-pack artifacts present, only patch-pack artifacts changed.
- Use `git diff` from live repo modifications.
- Do not hand-write hunks.
- Exactly one patch per target file.
- Every patch and cumulative patch sequence must pass `git apply --check`.
- Do not run PreCapWeek, PreCapNextDay, FlowRecap, raw-flow-dump-normalize, model-usage-log, status-merge, APEX project work, project status merge, calendar writes, schedulers, or state mutation.

### Section 2 — Required Read Order

Use this read order:

1. Git-native patch-pack process guide.
2. `Blockers.md`.
3. This patch plan.
4. Live source files listed in the plan:
   - `.claude/Claude.md`
   - PreCapWeek entrypoint and manifest
   - PreCapNextDay entrypoint and manifest
   - ProjectStatus entrypoint/manifest
   - AIRouting entrypoint/manifest
   - project-kb-manager
   - raw-flow-dump-normalize
   - flow-recap
   - model-usage-log
   - status-merge
   - PreCapNextDay operator templates and dependency contracts
   - project-kb-manager state packet contract/template
5. Read-only recovery sources under `ApexDefinition&OldVersions/...` only if live references are missing or ambiguous. Do not patch old-version paths.

### Section 3 — Evidence-Discovery Plan

Preserve the plan's evidence checks:

- Git preflight.
- `git ls-files` inventory checks for each relevant skill/package.
- Searches for build residue such as `NEXT PROMPT`, `VALIDATION`, `package_path_created`, `package_manifest_created`, `files_created`, `SKILL_md_created_with_valid_frontmatter`, `template_created`, `manifest_created`.
- Searches for collapsed/fenced blocks such as `core_loop:  1:`, `operator_gates:  G1:`, `artifact_paths:  apex_project_status:`, `skill_contract:  skill_name:`, `supporting_files:  - path:`, `failure_modes:  missing_required_inputs:`, `completion_gate:  target_path_valid:`, and markdown fences.
- Searches for path drift across lowercase/canonical paths.
- Searches for output design signals like result card, success card, Operator Review First, Route Reuse / Avoid Signal, learning signal, and next_PreCapNextDay_hint.
- Checks missing PreCapWeek references and creates minimal references if live files are missing.

### Section 4 — Source Inventory Expected by Plan

Use this to understand why each package is targeted:

- Root `.claude/Claude.md`: collapsed control blocks and path policy issue.
- PreCapWeek: mixed-case live package, manifest path drift, missing references, collapsed blocks.
- PreCapNextDay: fenced entrypoint, path policy clarity, table-first operator template, dependency path drift.
- ProjectStatus: manifest points to old/lowercase path.
- AIRouting: build-handoff residue and path drift.
- project-kb-manager: state packet contract/template not visible enough from SKILL support map.
- raw-flow-dump-normalize: completion gate checks package creation rather than invocation output.
- status-merge: completion gate includes package-build checks.
- model-usage-log: route signal exists but learning takeaway is not top-level.

### Section 5 — Target File and Patch Map

The plan requires exactly 22 target/patch pairs.

Do not add or remove entries.
Do not merge patches.
Do not split one target into multiple patches.
Do not patch any target outside this list.

```yaml
001:
  target_file: .claude/Claude.md
  patch_file: apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/001-root-claude-loop-source-authority.patch
  patch_type: modify_existing

002:
  target_file: .claude/skills/PrecapNextDay/Skill_precap-next-day.md
  patch_file: apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/002-precap-next-day-entrypoint-unfence.patch
  patch_type: modify_existing

003:
  target_file: .claude/skills/PrecapWeek/Skill_Precap-Week.md
  patch_file: apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/003-precap-week-entrypoint-readable.patch
  patch_type: modify_existing

004:
  target_file: .claude/skills/PrecapWeek/package-manifest.md
  patch_file: apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/004-precap-week-manifest-actual-paths.patch
  patch_type: modify_existing

005:
  target_file: .claude/skills/PrecapWeek/references/calendar-planning-guidance.md
  patch_file: apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/005-precap-week-calendar-guidance.patch
  patch_type: create_if_missing

006:
  target_file: .claude/skills/PrecapWeek/references/weekly-plan-output-contract.md
  patch_file: apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/006-precap-week-output-contract.patch
  patch_type: create_if_missing

007:
  target_file: .claude/skills/PrecapWeek/references/weekly-blueprint-standard.md
  patch_file: apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/007-precap-week-blueprint-standard.patch
  patch_type: create_if_missing

008:
  target_file: .claude/skills/PrecapWeek/references/weekly-blueprint-meeting-example.md
  patch_file: apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/008-precap-week-meeting-example.patch
  patch_type: create_if_missing

009:
  target_file: .claude/skills/PrecapWeek/references/validation-checklist.md
  patch_file: apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/009-precap-week-validation-checklist.patch
  patch_type: create_if_missing

010:
  target_file: .claude/skills/PrecapNextDay/precap-next-day-package-manifest.md
  patch_file: apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/010-precap-next-day-path-policy.patch
  patch_type: modify_existing

011:
  target_file: .claude/skills/PrecapNextDay/references/operator-output-format-design.md
  patch_file: apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/011-operator-output-design-result-card-policy.patch
  patch_type: modify_existing

012:
  target_file: .claude/skills/PrecapNextDay/templates/next-day-plan-operator-template.md
  patch_file: apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/012-next-day-plan-result-card.patch
  patch_type: modify_existing

013:
  target_file: .claude/skills/PrecapNextDay/references/prompt-engineering-dependency-contract.md
  patch_file: apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/013-prompt-engineering-path-bridge.patch
  patch_type: modify_existing

014:
  target_file: .claude/skills/PrecapNextDay/references/usage-tracking-dependency-contract.md
  patch_file: apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/014-usage-tracking-path-bridge.patch
  patch_type: modify_existing

015:
  target_file: .claude/skills/PrecapNextDay/references/workflow-process-validation-contract.md
  patch_file: apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/015-workflow-process-path-bridge.patch
  patch_type: modify_existing

016:
  target_file: .claude/skills/ProjectStatus/package-manifest.md
  patch_file: apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/016-projectstatus-manifest-actual-paths.patch
  patch_type: modify_existing

017:
  target_file: .claude/skills/AIRouting/ai-routing-and-usage-tracking-SKILL.md
  patch_file: apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/017-airouting-entrypoint-residue-removal.patch
  patch_type: modify_existing

018:
  target_file: .claude/skills/AIRouting/ai-routing-and-usage-tracking-package-manifest.md
  patch_file: apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/018-airouting-manifest-residue-and-paths.patch
  patch_type: modify_existing

019:
  target_file: .claude/skills/raw-flow-dump-normalize/SKILL.md
  patch_file: apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/019-raw-flow-run-completion-gate.patch
  patch_type: modify_existing

020:
  target_file: .claude/skills/status-merge/SKILL.md
  patch_file: apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/020-status-merge-run-completion-gate.patch
  patch_type: modify_existing

021:
  target_file: .claude/skills/project-kb-manager/SKILL.md
  patch_file: apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/021-project-kb-manager-state-handoff-exposure.patch
  patch_type: modify_existing

022:
  target_file: .claude/skills/model-usage-log/templates/model-usage-delta-template.md
  patch_file: apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/022-model-usage-learning-card.patch
  patch_type: modify_existing
```

### Section 6 — Improvement Matrix

Use the B1-B6 batches as the semantic grouping:

| Batch | Patch IDs | Purpose |
|---|---|---|
| B1 | 001 | Root loop/source authority readability and actual/canonical path policy |
| B2 | 003-009 | PreCapWeek handoff integrity and missing weekly support references |
| B3 | 010, 013-016, 018 | Manifest/path alignment across dependent packages |
| B4 | 017-020 | Remove package-build residue from live invocation surfaces |
| B5 | 011, 012, 022 | Add minimal operator value/success/learning cards before later output-design work |
| B6 | 021 | Expose apex_orchestration_state_packet through project-kb-manager entrypoint |

### Section 7 — Per-Target Contracts

For each patch ID, the prompt-builder/patch-builder must read the exact per-target contract in the source plan and enforce:

- `required_changes`
- `required_markers`
- `forbidden_markers`
- `acceptance`

Do not summarize these away in the actual patch-pack-building work. The source plan is the detailed instruction source.

## Patch-pack artifact contract

The patch pack must contain:

```text
apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/000-patch-manifest.md
apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/001-root-claude-loop-source-authority.patch
...
apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/022-model-usage-learning-card.patch
apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/999-codex-apply-handoff.md
apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/validation-report.md
```

Use `999-codex-apply-handoff.md`, not `999-codex-apply-patches.md`, unless the working prompt reproduction explicitly requires the old name. The current source plan and process guide expect handoff naming.

## Forbidden mutation paths

Do not patch these paths:

```text
state/
.claude/kb/
source-knowledge/
ApexDefinition&OldVersions/
.github/workflows/
scripts/
derived/
outputs/
raw/
sources/
```

`ApexDefinition&OldVersions/` may be read only if the source plan calls for read-only recovery evidence. It must never be patched in this task.

## Environment / repo handling rule

Do not add environment acquisition logic.

Do not add:

- `git clone`,
- `C:\GitDev\...` as an Agent Mode runtime requirement,
- `/home/oai/share/...`,
- `patchwork`,
- `git init`,
- synthetic repo creation,
- placeholder files,
- API reconstruction as source baseline.

The correct patch-plan instruction is:

```text
Use the live terminal Git repository as the only source of truth for patch generation.
Run the Git preflight from the working prompt / process guide.
If the live repo/source plan/target files are not readable, fail.
Do not create substitute artifacts.
```

## New-file handling for create_if_missing targets

Patch IDs 005-009 are `create_if_missing`.

The patch builder may use Git-native intent-to-add for new files:

```bash
git add -N <target-file>
git diff --no-ext-diff -- <target-file> > <patch-file>
git reset -- <target-file>
```

This is the only permitted deviation needed for new-file Git diff generation.

## Output expected from the next AI

The next AI should produce either:

### Option A — Correct Agent Mode patch-pack builder prompt

A prompt copied from the working example shape, but using this patch plan as semantic authority.

It must include:

- repo / branch / patch-pack path,
- source plan path,
- target/patch map,
- B1-B6/Section 5-7 authority bridge,
- forbidden mutation paths,
- Git-native procedure copied from working prompt / process guide,
- no clone/local path/workspace acquisition logic.

### Option B — Correct local/Codex patch-pack build plan

A deterministic local plan for generating the 22 patch files from an already checked-out repo.

It must:

- read the patch plan,
- read Blockers.md,
- read all listed target files,
- generate one Git diff patch per target,
- validate per-patch and cumulative apply,
- write manifest/handoff/validation report,
- keep target files unmodified at final state.

## Validation before delivering any new prompt/plan

Before delivering, the next AI must include:

```yaml
patch_plan_alignment_check:
  canonical_patch_plan_read: true
  source_plan_path: apex-meta/patch-plans/2026-07-07-step1-prompt-blocker-cleanup-plan.okf.md
  target_count: 22
  patch_count: 22
  batches: [B1, B2, B3, B4, B5, B6]
  forbidden_mutation_paths_preserved: true
  clone_logic_added: false
  local_absolute_path_added: false
  patchwork_logic_added: false
  placeholder_file_logic_added: false
  api_reconstruction_added: false
```

If any of the last five fields is true, the output is invalid.

## Final note

The existing patch plan is not the problem. The failure came from attempts to wrap it in new prompt behavior that drifted from the working prompt and from the plan's own live-Git source-of-truth model.

A correct next AI should first understand the patch plan, then produce only a thin execution prompt or local build plan around it.