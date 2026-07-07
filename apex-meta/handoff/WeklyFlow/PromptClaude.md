# Agent Mode Task — APEX Step 1 Prompt-Blocker Cleanup Git-Native Patch-Pack Builder

You are GPT-5.5 Agent Mode acting as the APEX Step 1 Prompt-Blocker Cleanup Patch-Pack Builder. Your job is to create a validated, durable patch pack that is either:
1. committed and pushed to the real repository, patch by patch, or
2. exported as a downloadable archive if and only if repository push is unavailable.

Your job is NOT to directly apply the final target-file changes to the repository. The final repo state, after this task, must contain patch artifacts only. The target files must be clean and unmodified in the final commit.

Do not use previous failed Agent Mode output as source material.
Do not read a giant failed transcript.
Do not reconstruct from memory.
Do not create a synthetic repo from copied connector files.
Use the live terminal Git repository as the only source of truth for patch generation.

Repository: leela-spec/apexai-os-meta
Branch: main
Patch-pack path: apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/

Primary source plan to read first:
apex-meta/patch-plans/2026-07-07-step1-prompt-blocker-cleanup-plan.okf.md

If that exact path is not found, search only under apex-meta/patch-plans/ for a filename containing all of:
- 2026-07-07
- step1
- prompt-blocker-cleanup

Also read if available:
Blockers.md (search under apex-meta/ and .claude/ if root location differs)

If the source plan is not readable, stop with:
SOURCE_ACCESS_FAILED:
  missing:
    - "apex-meta/patch-plans/2026-07-07-step1-prompt-blocker-cleanup-plan.okf.md"
  action_needed: "Mount project source or confirm the source-plan path."

Target files for patch generation:
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

Allowed patch-pack outputs:
- apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/000-patch-manifest.md
- apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/001-root-claude-loop-source-authority.patch
- apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/002-precap-next-day-entrypoint-unfence.patch
- apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/003-precap-week-entrypoint-readable.patch
- apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/004-precap-week-manifest-actual-paths.patch
- apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/005-precap-week-calendar-guidance.patch
- apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/006-precap-week-output-contract.patch
- apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/007-precap-week-blueprint-standard.patch
- apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/008-precap-week-meeting-example.patch
- apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/009-precap-week-validation-checklist.patch
- apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/010-precap-next-day-path-policy.patch
- apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/011-operator-output-design-result-card-policy.patch
- apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/012-next-day-plan-result-card.patch
- apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/013-prompt-engineering-path-bridge.patch
- apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/014-usage-tracking-path-bridge.patch
- apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/015-workflow-process-path-bridge.patch
- apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/016-projectstatus-manifest-actual-paths.patch
- apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/017-airouting-entrypoint-residue-removal.patch
- apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/018-airouting-manifest-residue-and-paths.patch
- apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/019-raw-flow-run-completion-gate.patch
- apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/020-status-merge-run-completion-gate.patch
- apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/021-project-kb-manager-state-handoff-exposure.patch
- apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/022-model-usage-learning-card.patch
- apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/999-apply-patches.md

Hard forbidden files and folders:
- state/**
- .claude/kb/**
- source-knowledge/**
- ApexDefinition&OldVersions/**
- .github/workflows/**
- scripts/**
- **/*.py
- **/*.json
- **/*.yaml
- **/*.yml

Required changes per target (read from source plan — do not derive from memory):
Read section 7 "Per-Target Contracts" of the source plan for per-file required_markers and forbidden_markers.
Read section 8 "Cross-File Consistency Requirements" for boundary rules.
Read section 9 "Forbidden Paths and Mutation Guard" for additional guards.

PRE-FLIGHT: repository and persistence checks

Run:
  git rev-parse --show-toplevel
  git rev-parse --is-inside-work-tree
  git remote get-url origin
  git branch --show-current
  git status --porcelain

Then run:
  git ls-remote --heads origin main

Rules:
1. If this is not a Git worktree, stop.
2. If origin is missing, stop normal repo mode. Do not create a synthetic repo. Go to FALLBACK ARCHIVE MODE.
3. If origin does not point to leela-spec/apexai-os-meta, stop.
4. If the current branch is not main, run git checkout main.
5. Run git pull --ff-only origin main.
6. If git pull fails, stop normal repo mode. Go to FALLBACK ARCHIVE MODE only if the local checkout is otherwise readable.
7. If unrelated dirty files overlap target files, forbidden paths, or the patch-pack path, stop.
8. If unrelated dirty files exist elsewhere, report them but continue only if they do not overlap the task.

Create the patch-pack directory:
  mkdir -p apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup

Read first:
- the source plan (apex-meta/patch-plans/2026-07-07-step1-prompt-blocker-cleanup-plan.okf.md)
- every target file listed above

Before editing, create an internal file-change map for all 22 patches. Do not commit this internal map unless summarized inside 000-patch-manifest.md.

PATCH GENERATION DOCTRINE
- Generate patches with git diff only.
- Do not hand-write unified diff hunks.
- Do not manually edit hunk headers.
- Do not use zero-context diffs.
- Do not normalize line endings across whole files.
- Do not run formatters.
- Do not rewrite unrelated sections.
- Generate one patch file per target file.
- Each patch file must touch exactly one target file.
- After each patch file is generated, immediately revert the real target file.
- After each patch file validates, commit and push that patch file only before moving to the next patch.
- If push fails, do not claim success. Go to FALLBACK ARCHIVE MODE.

PER-PATCH CHECKPOINT PROCEDURE

For each patch 001 through 022, do exactly this sequence.

A. Confirm clean target:
  git checkout -- <target-file>
  git status --porcelain -- <target-file>
  The status command must print nothing.

B. Modify only <target-file> according to the source plan per-target contract for that file.

C. Generate the patch:
  git diff --no-ext-diff -- <target-file> > <patch-file>

D. Validate patch file existence:
  test -s <patch-file>

E. Validate single-file scope:
  grep '^diff --git ' <patch-file>
  This must print exactly one line, and that line must reference only <target-file>.

F. Revert the real target file before apply-check:
  git checkout -- <target-file>
  git status --porcelain -- <target-file>
  The status command must print nothing.

G. Validate that the patch applies to clean main:
  git apply --check <patch-file>

H. Temporarily apply the patch and run patch-specific sanity checks:
  git apply <patch-file>
  git diff --name-only
  The diff must contain only <target-file>.
  Then verify required_markers exist and forbidden_markers are absent per source plan section 7.

I. Revert target again:
  git checkout -- <target-file>
  git status --porcelain -- <target-file>
  The status command must print nothing.

J. Commit and push this patch artifact only:
  git add <patch-file>
  git diff --cached --name-only
  The staged diff must list only <patch-file>.
  Then:
  git commit -m "Add step1 blocker cleanup patch <NNN>"
  git push origin main
  If git push fails, stop normal repo mode and go to FALLBACK ARCHIVE MODE.

CUMULATIVE VALIDATION AFTER 001-022 ARE PUSHED

From clean main, run:
  git pull --ff-only origin main
  git status --porcelain

Then check every patch:
  for p in apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/*.patch; do
    git apply --check "$p" || exit 1
  done

Apply all patches in numeric order:
  for p in apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/*.patch; do
    git apply "$p" || exit 1
  done

Run required marker validations (from source plan section 7):
  grep -R "path_policy:" .claude/Claude.md
  grep -R "actual_live_path" .claude/Claude.md
  grep -R "canonical_target_path" .claude/Claude.md
  grep -R "core_loop:" .claude/Claude.md
  grep -R "raw_flow_dump_output_completion_gate:" .claude/skills/raw-flow-dump-normalize/SKILL.md
  grep -R "status_merge_output_completion_gate:" .claude/skills/status-merge/SKILL.md
  grep -R "handoff_mode" .claude/skills/project-kb-manager/SKILL.md
  grep -R "operator_learning_card:" .claude/skills/model-usage-log/templates/model-usage-delta-template.md
  grep -R "result_card_policy:" .claude/skills/PrecapNextDay/references/operator-output-format-design.md

Run forbidden marker checks (from source plan section 7) — these must return no matches:
  grep -R "core_loop:  1:" .claude/Claude.md && exit 1 || true
  grep -R "package_path_created: true" .claude/skills/raw-flow-dump-normalize/SKILL.md && exit 1 || true
  grep -R "package_path_created: true" .claude/skills/status-merge/SKILL.md && exit 1 || true
  grep -R "# NEXT PROMPT" .claude/skills/AIRouting/ && exit 1 || true
  grep -R "# VALIDATION" .claude/skills/AIRouting/ && exit 1 || true

Check changed files:
  git diff --name-only
  The changed files must be exactly the 22 target files listed above.
  No forbidden files may appear.

Revert cumulative target-file changes:
  git checkout -- .claude/
  git status --porcelain -- .claude/
  This must print nothing.

CREATE AND COMMIT MANIFEST

Create: apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/000-patch-manifest.md

Manifest must include:
- repository and branch
- source plan file read
- Blockers.md read status
- exact target files read
- exact patch files created
- patch-to-target map
- purpose of each patch (from source plan section 5 and 7)
- individual validation command per patch
- cumulative validation commands
- required marker validation results
- forbidden marker validation results
- forbidden files/folders
- statement that target files were reverted and are not modified in the patch-pack commit
- commit SHAs for patch artifact commits if available

Commit and push manifest only:
  git add apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/000-patch-manifest.md
  git diff --cached --name-only
  git commit -m "Add step1 blocker cleanup patch manifest"
  git push origin main

CREATE AND COMMIT APPLY HANDOFF

Create: apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/999-apply-patches.md

It must be a deterministic command prompt that says:
- repo: leela-spec/apexai-os-meta
- branch: main
- work directly on main
- do not create branch
- do not open PR
- run git checkout main
- run git pull --ff-only origin main
- run git apply --check for each patch in numeric order
- run git apply for each patch in numeric order
- verify only the 22 target files changed
- verify forbidden files were not touched
- verify required markers
- verify forbidden markers absent
- commit and push target-file changes

Commit and push handoff only:
  git add apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/999-apply-patches.md
  git diff --cached --name-only
  git commit -m "Add apply handoff for step1 blocker cleanup patches"
  git push origin main

FINAL REPO CHECK

Run:
  git status --porcelain
  git log --oneline -n 15

Final status must be clean.

FALLBACK ARCHIVE MODE

Use this only if normal repo mode cannot push to origin or no real origin exists.

Rules:
- Do not claim repo delivery.
- Do not create or use a synthetic repo as if it were the real repo.
- Still generate whatever patch artifacts can be generated from the real local checkout.
- Validate them with git apply --check if possible.
- Create 000-patch-manifest.md and 999-apply-patches.md locally.
- Create an archive named step1-prompt-blocker-cleanup-patch-pack.zip.

Preferred archive output paths:
1. /mnt/data/step1-prompt-blocker-cleanup-patch-pack.zip if /mnt/data exists.
2. ./step1-prompt-blocker-cleanup-patch-pack.zip otherwise.

Archive must contain:
- 000-patch-manifest.md
- all generated .patch files
- 999-apply-patches.md
- FALLBACK-REPORT.md explaining exactly why repo push was unavailable

In fallback mode final report verdict must be: PARTIAL_ARTIFACT_EXPORT
Do not report pushed: true in fallback mode.

FINAL REPORT FORMAT

Return exactly:

FINAL_REPORT:
  verdict: PASS|PARTIAL_ARTIFACT_EXPORT|FAIL
  repo: leela-spec/apexai-os-meta
  branch: main
  normal_repo_mode_used: true|false
  origin_verified: true|false
  pushed_patch_artifacts_to_main: true|false
  patch_pack_path: "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/"
  patch_files_created:
    - "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/001-root-claude-loop-source-authority.patch"
    - "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/002-precap-next-day-entrypoint-unfence.patch"
    - "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/003-precap-week-entrypoint-readable.patch"
    - "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/004-precap-week-manifest-actual-paths.patch"
    - "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/005-precap-week-calendar-guidance.patch"
    - "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/006-precap-week-output-contract.patch"
    - "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/007-precap-week-blueprint-standard.patch"
    - "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/008-precap-week-meeting-example.patch"
    - "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/009-precap-week-validation-checklist.patch"
    - "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/010-precap-next-day-path-policy.patch"
    - "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/011-operator-output-design-result-card-policy.patch"
    - "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/012-next-day-plan-result-card.patch"
    - "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/013-prompt-engineering-path-bridge.patch"
    - "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/014-usage-tracking-path-bridge.patch"
    - "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/015-workflow-process-path-bridge.patch"
    - "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/016-projectstatus-manifest-actual-paths.patch"
    - "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/017-airouting-entrypoint-residue-removal.patch"
    - "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/018-airouting-manifest-residue-and-paths.patch"
    - "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/019-raw-flow-run-completion-gate.patch"
    - "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/020-status-merge-run-completion-gate.patch"
    - "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/021-project-kb-manager-state-handoff-exposure.patch"
    - "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/022-model-usage-learning-card.patch"
  individual_patch_commits:
    "001": "<sha-or-NA>"
    "002": "<sha-or-NA>"
    "003": "<sha-or-NA>"
    "004": "<sha-or-NA>"
    "005": "<sha-or-NA>"
    "006": "<sha-or-NA>"
    "007": "<sha-or-NA>"
    "008": "<sha-or-NA>"
    "009": "<sha-or-NA>"
    "010": "<sha-or-NA>"
    "011": "<sha-or-NA>"
    "012": "<sha-or-NA>"
    "013": "<sha-or-NA>"
    "014": "<sha-or-NA>"
    "015": "<sha-or-NA>"
    "016": "<sha-or-NA>"
    "017": "<sha-or-NA>"
    "018": "<sha-or-NA>"
    "019": "<sha-or-NA>"
    "020": "<sha-or-NA>"
    "021": "<sha-or-NA>"
    "022": "<sha-or-NA>"
  manifest_commit_sha: "<sha-or-NA>"
  handoff_commit_sha: "<sha-or-NA>"
  each_patch_git_apply_check: PASS|FAIL
  cumulative_patch_check: PASS|FAIL
  cumulative_marker_validation: PASS|FAIL
  target_files_modified_by_patch_pack_commits: false
  final_repo_status_clean: true|false
  forbidden_files_touched: false
  fallback_archive: "<path-or-NA>"
  failure_reason: "<reason-or-NA>"