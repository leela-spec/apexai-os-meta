# Handoff — Reproduce the Working Agent Mode Patch-Pack Prompt Without Drift

## Purpose

This handoff is for another AI that will create a new Agent Mode prompt for the APEX Step 1 Prompt-Blocker Cleanup patch-pack task.

The previous assistant repeatedly failed by trying to improve the prompt instead of copying the known working prompt pattern. Do not repeat that.

Your task is not to redesign Agent Mode behavior.
Your task is not to solve repo access creatively.
Your task is not to add new safety architecture.
Your task is to reproduce the working prompt skeleton and change only the task-specific values.

## Primary instruction

Use the working prompt example as the source of truth for structure, repo-handling semantics, fallback semantics, and wording style.

Create the new prompt by copying the working prompt and replacing only the fields listed under "Allowed differences" below.

If a proposed change is not listed under "Allowed differences", do not make it.

## Required inputs

The operator should provide these files to the AI creating the prompt:

1. `WorkingPromptExample.md`
   - This is the known working Agent Mode prompt.
   - Treat it as the locked skeleton.

2. `AgentModePatchGuide_v4.md`
   - Binding process guide.
   - Use only to verify that the copied prompt still follows the required Git-native patch-pack process.
   - Do not use it to invent new sections beyond the working example unless the working example already has the corresponding section shape.

3. Source plan already present in repo:
   - `apex-meta/patch-plans/2026-07-07-step1-prompt-blocker-cleanup-plan.okf.md`
   - This is the semantic authority for patch content.
   - The prompt must tell Agent Mode to read this file first.

4. Optional blocker file if present:
   - `Blockers.md`

## Repository and branch

```yaml
repo: leela-spec/apexai-os-meta
branch: main
patch_pack_path: apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/
primary_source_plan: apex-meta/patch-plans/2026-07-07-step1-prompt-blocker-cleanup-plan.okf.md
```

## Critical lessons from failed attempts

Do not diagnose or solve the environment. Preserve the working prompt's repo handling.

The working prompt did not add:

- `git clone` instructions,
- `C:\GitDev\...` as an Agent Mode runtime requirement,
- `/home/oai/share/...` path logic,
- `git init`,
- substitute repo creation,
- API reconstruction as fallback,
- placeholder target-file generation,
- a new environment-acquisition protocol.

Therefore the new prompt must not add any of those.

## Required repo-handling semantics

Use the working example's Git-native assumption:

```text
Use the live terminal Git repository as the only source of truth for patch generation.
```

The prompt may include the same preflight style as the working prompt:

```bash
git rev-parse --show-toplevel
git rev-parse --is-inside-work-tree
git remote get-url origin
git branch --show-current
git status --porcelain
git ls-remote --heads origin main
```

Do not add clone/open-directory/local-path logic.

If repo preflight fails, stop according to the working prompt pattern. Do not create placeholder artifacts.

## Allowed differences from `WorkingPromptExample.md`

Only these differences are allowed:

| Section / field | Replace with |
|---|---|
| Title | `# Agent Mode Task — APEX Step 1 Prompt-Blocker Cleanup Git-Native Patch-Pack Builder` |
| Role sentence | `You are GPT-5.5 Agent Mode acting as the APEX Step 1 Prompt-Blocker Cleanup Patch-Pack Builder.` |
| Repository | `leela-spec/apexai-os-meta` |
| Branch | `main` |
| Patch-pack path | `apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/` |
| Primary source plan | `apex-meta/patch-plans/2026-07-07-step1-prompt-blocker-cleanup-plan.okf.md` |
| Source-plan fallback search folder | `apex-meta/patch-plans/` |
| Source-plan fallback search terms | `2026-07-07`, `step1`, `prompt-blocker`, `cleanup-plan` |
| Optional read file | `Blockers.md` |
| Target map | The 22 target files listed below |
| Patch map | The 22 patch files listed below |
| Allowed outputs | `000-patch-manifest.md`, 22 patch files, `999-codex-apply-handoff.md`, `validation-report.md` under the patch-pack path |
| Required semantic contract | Use Sections 5, 6, and 7 of the source plan as authority |
| Forbidden mutation paths | Use task-specific forbidden paths listed below |
| Final report schema | May be task-specific, but do not add environment acquisition fields not in the working pattern |

Everything else should remain as close as possible to the working prompt.

## Target file and patch file map

```yaml
001:
  target_file: .claude/Claude.md
  patch_file: apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/001-root-claude-loop-source-authority.patch

002:
  target_file: .claude/skills/PrecapNextDay/Skill_precap-next-day.md
  patch_file: apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/002-precap-next-day-entrypoint-unfence.patch

003:
  target_file: .claude/skills/PrecapWeek/Skill_Precap-Week.md
  patch_file: apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/003-precap-week-entrypoint-readable.patch

004:
  target_file: .claude/skills/PrecapWeek/package-manifest.md
  patch_file: apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/004-precap-week-manifest-actual-paths.patch

005:
  target_file: .claude/skills/PrecapWeek/references/calendar-planning-guidance.md
  patch_file: apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/005-precap-week-calendar-guidance.patch

006:
  target_file: .claude/skills/PrecapWeek/references/weekly-plan-output-contract.md
  patch_file: apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/006-precap-week-output-contract.patch

007:
  target_file: .claude/skills/PrecapWeek/references/weekly-blueprint-standard.md
  patch_file: apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/007-precap-week-blueprint-standard.patch

008:
  target_file: .claude/skills/PrecapWeek/references/weekly-blueprint-meeting-example.md
  patch_file: apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/008-precap-week-meeting-example.patch

009:
  target_file: .claude/skills/PrecapWeek/references/validation-checklist.md
  patch_file: apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/009-precap-week-validation-checklist.patch

010:
  target_file: .claude/skills/PrecapNextDay/precap-next-day-package-manifest.md
  patch_file: apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/010-precap-next-day-path-policy.patch

011:
  target_file: .claude/skills/PrecapNextDay/references/operator-output-format-design.md
  patch_file: apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/011-operator-output-design-result-card-policy.patch

012:
  target_file: .claude/skills/PrecapNextDay/templates/next-day-plan-operator-template.md
  patch_file: apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/012-next-day-plan-result-card.patch

013:
  target_file: .claude/skills/PrecapNextDay/references/prompt-engineering-dependency-contract.md
  patch_file: apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/013-prompt-engineering-path-bridge.patch

014:
  target_file: .claude/skills/PrecapNextDay/references/usage-tracking-dependency-contract.md
  patch_file: apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/014-usage-tracking-path-bridge.patch

015:
  target_file: .claude/skills/PrecapNextDay/references/workflow-process-validation-contract.md
  patch_file: apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/015-workflow-process-path-bridge.patch

016:
  target_file: .claude/skills/ProjectStatus/package-manifest.md
  patch_file: apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/016-projectstatus-manifest-actual-paths.patch

017:
  target_file: .claude/skills/AIRouting/ai-routing-and-usage-tracking-SKILL.md
  patch_file: apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/017-airouting-entrypoint-residue-removal.patch

018:
  target_file: .claude/skills/AIRouting/ai-routing-and-usage-tracking-package-manifest.md
  patch_file: apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/018-airouting-manifest-residue-and-paths.patch

019:
  target_file: .claude/skills/raw-flow-dump-normalize/SKILL.md
  patch_file: apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/019-raw-flow-run-completion-gate.patch

020:
  target_file: .claude/skills/status-merge/SKILL.md
  patch_file: apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/020-status-merge-run-completion-gate.patch

021:
  target_file: .claude/skills/project-kb-manager/SKILL.md
  patch_file: apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/021-project-kb-manager-state-handoff-exposure.patch

022:
  target_file: .claude/skills/model-usage-log/templates/model-usage-delta-template.md
  patch_file: apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/022-model-usage-learning-card.patch
```

## Required source-plan authority section

The new prompt should include this short bridge because the working example had task-specific required changes inline, while this task stores detailed required changes in the source plan.

```text
PATCHING AUTHORITY FROM SOURCE PLAN

After reading the primary source plan, execute the patch work exactly from these source-plan sections:

1. Section 5 — Target File and Patch Map
- Treat every listed target_file as a required patch target.
- Treat every listed patch_file as the required patch artifact path.
- Create one Git-generated patch per target file.
- Do not skip any target unless the source plan says the file is optional or the file is absent and the plan says create_if_missing.

2. Section 6 — Improvement Matrix
- Use B1 through B6 as the semantic batch plan.
- For each batch, implement the desired_state items.
- Respect every forbidden item.
- Run the high_impact_extra_checks before finalizing each affected patch.

3. Section 7 — Per-Target Contracts
- For each patch ID, apply the required_changes for that exact target file.
- Verify all required_markers for that target.
- Verify all forbidden_markers are absent for that target.
- Use the acceptance field as the semantic done condition.

Do not merely create patch files from the target list.
Each patch must implement the corresponding B1-B6 batch intent and the per-target required_changes from the source plan.
```

Do not expand this into a large new architecture section.

## Forbidden mutation paths

Use these as mutation-forbidden paths. Do not broaden into a new access model.

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

## New-file handling

Patches 005-009 may be create-if-missing files according to the source plan. The prompt may add only the minimal Git-native handling needed for new files:

```bash
git add -N <target-file>
git diff --no-ext-diff -- <target-file> > <patch-file>
git reset -- <target-file>
```

Do not add wider repo or workspace logic because of this.

## Hard prohibitions for the new prompt

The new prompt must not contain any of these strings or behaviors:

```text
git clone
C:\GitDev
/home/oai/share
patchwork
git init
placeholder
synthetic repo
substitute repository
reconstruct files from GitHub API
API snippets as baseline
```

Exception: the prompt may mention `API snippets` only in a negative sentence copied from the working prompt, such as `Do not reconstruct files from API snippets`.

## Fallback rule

Preserve the working prompt's fallback semantics.

Fallback archive mode is only for persistence failure after real Git-native patches were generated from the live terminal Git repository.

Do not let fallback cover:

- missing repo,
- missing origin,
- missing source plan,
- missing target files,
- generated placeholder files,
- API reconstruction,
- synthetic local repo creation.

## Validation required for the produced prompt

Before handing the new prompt back to the operator, produce a drift table:

| Section | Working prompt behavior | New prompt behavior | Allowed difference? |
|---|---|---|---|

The table must prove that every difference is in the allowed-difference list above.

Also produce a forbidden-string check:

```yaml
forbidden_string_check:
  git_clone_present: false
  windows_path_present: false
  slash_home_oai_share_present: false
  patchwork_present: false
  git_init_present: false
  placeholder_present: false
  synthetic_repo_present: false
  api_reconstruction_positive_permission_present: false
```

If the prompt fails this validation, do not deliver it as final.

## Success criteria for the AI creating the prompt

The final answer should include:

1. The full Agent Mode prompt.
2. A short drift table against `WorkingPromptExample.md`.
3. The forbidden-string check.
4. A statement that no clone/local-path/workspace-acquisition logic was added.

## Important note

Do not try to be smarter than the working example.

The correct output is boring: a copied working prompt with the task-specific file map and source-plan path changed.