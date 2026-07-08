<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# create a solid version with all the best pracitce we know by now:

# APEX Step 1 Patch-Pack Builder

## Role

You build a validated patch pack for 22 target files in leela-spec/apexai-os-meta, branch main. Output: one .patch file per target, a manifest, and an apply-handoff file, delivered as a verified downloadable ZIP.

## Step 0 — Access Declaration (mandatory, do this first, do not skip)

Determine and state explicitly, before any other action:

ACCESS_DECLARATION:
live_git_worktree_present: true|false (checked via: pwd; git rev-parse --show-toplevel — run once only)
github_connector_available: true|false (checked via one list_resources call — run once only)
source_plan_readable: true|false (checked via one fetch attempt)
mode_selected: "live_repo" | "api_mirror" | "blocked"

Rules for this step:

- Run each check exactly once. Do not repeat, re-verify, or re-search after a result is obtained. A "not found" result is final and authoritative for this run.
- If live_git_worktree_present is true AND it points to leela-spec/apexai-os-meta: mode_selected = "live_repo".
- Else if github_connector_available is true: mode_selected = "api_mirror".
- Else: mode_selected = "blocked". Stop and report ACCESS_DECLARATION only, with no further action.
- Do not attempt git clone under any circumstance — this environment has no network clone capability.
- Print the ACCESS_DECLARATION block before proceeding to Step 1. This is your one and only environment-discovery phase.


## Step 1 — Read Source Plan

Fetch (via live repo or connector, per mode_selected):
apex-meta/patch-plans/2026-07-07-step1-prompt-blocker-cleanup-plan.okf.md

If unreadable, stop:
SOURCE_ACCESS_FAILED: missing source plan, cannot proceed.

Read section 7 (Per-Target Contracts), section 8 (Cross-File Consistency), section 9 (Forbidden Paths) fully now. Do not re-fetch these sections later — hold them in context for the full run.

## Step 2 — Prepare Working Copy

If mode_selected = "live_repo": use the real checkout directly. Confirm clean state (git status --porcelain prints nothing), then proceed.

If mode_selected = "api_mirror": build a local git repo seeded from real fetched content only.
mkdir -p /home/oai/share/mirror \&\& cd /home/oai/share/mirror \&\& git init -q
For each of the 22 target files below, fetch its real current content via the connector and write it verbatim. If a fetch fails for a file marked create_if_missing in the plan, treat as empty baseline. If a fetch fails for any other file, record it in files_not_fetched and exclude it from this run — do not substitute placeholder text.
git add -A \&\& git commit -q -m "Baseline mirror, fetched \$(date -u +%FT%TZ)"
Record this commit hash as baseline_commit_sha.

## Step 3 — Target List

001 .claude/Claude.md
002 .claude/skills/PrecapNextDay/Skill_precap-next-day.md
003 .claude/skills/PrecapWeek/Skill_Precap-Week.md
004 .claude/skills/PrecapWeek/package-manifest.md
005 .claude/skills/PrecapWeek/references/calendar-planning-guidance.md
006 .claude/skills/PrecapWeek/references/weekly-plan-output-contract.md
007 .claude/skills/PrecapWeek/references/weekly-blueprint-standard.md
008 .claude/skills/PrecapWeek/references/weekly-blueprint-meeting-example.md
009 .claude/skills/PrecapWeek/references/validation-checklist.md
010 .claude/skills/PrecapNextDay/precap-next-day-package-manifest.md
011 .claude/skills/PrecapNextDay/references/operator-output-format-design.md
012 .claude/skills/PrecapNextDay/templates/next-day-plan-operator-template.md
013 .claude/skills/PrecapNextDay/references/prompt-engineering-dependency-contract.md
014 .claude/skills/PrecapNextDay/references/usage-tracking-dependency-contract.md
015 .claude/skills/PrecapNextDay/references/workflow-process-validation-contract.md
016 .claude/skills/ProjectStatus/package-manifest.md
017 .claude/skills/AIRouting/ai-routing-and-usage-tracking-SKILL.md
018 .claude/skills/AIRouting/ai-routing-and-usage-tracking-package-manifest.md
019 .claude/skills/raw-flow-dump-normalize/SKILL.md
020 .claude/skills/status-merge/SKILL.md
021 .claude/skills/project-kb-manager/SKILL.md
022 .claude/skills/model-usage-log/templates/model-usage-delta-template.md

Forbidden — never write to: state/**, .claude/kb/**, source-knowledge/**, ApexDefinition\&OldVersions/**, .github/workflows/**, scripts/**, **/*.py

## Step 4 — Per-File Iteration Loop (repeat for each target in order)

1. Read the target file's current real content (already in mirror/worktree from Step 2 — do not re-fetch).
2. Read that file's required_markers / forbidden_markers from source plan section 7 (already in context from Step 1 — do not re-fetch the plan).
3. Apply only the required change to that file.
```
4. Generate patch: `git diff --no-ext-diff -- <file> > patch-packs/<NNN>-<name>.patch`
```

5. Validate: file is non-empty, `grep '^diff --git '` shows exactly one line for this file only.
6. Revert file: `git checkout -- <file>`.
7. Validate patch applies clean: `git apply --check <patch-file>`.
8. Apply and verify:
git apply <patch-file>
grep -q "<required_marker>" <file> (must find each required marker)
grep -L "<forbidden_marker>" <file> (must NOT find any forbidden marker)
git checkout -- <file>
9. Commit patch artifact only:
```
git add patch-packs/<NNN>-<name>.patch
```

git commit -q -m "Add patch <NNN>"
10. Move to next file.

If a step fails for a given file after one retry, record it in files_failed with the reason and move to the next file. Do not stop the whole run for one file's failure. Do not fabricate content to force success — a skipped file is acceptable, a fabricated file is not.

## Step 5 — Cumulative Validation

Apply all generated patches in order against a clean copy; confirm only the intended target files change; run all required/forbidden marker greps from section 7 across the result; revert.

## Step 6 — Manifest and Handoff

Create 000-patch-manifest.md: mode used, baseline_commit_sha (if api_mirror), source plan path, per-patch purpose, validation results, files_not_fetched, files_failed.
Create 999-apply-patches.md: deterministic instructions to apply these patches against the real live repo (checkout main, pull, apply --check each, apply, verify markers, commit, push). If mode_used was api_mirror, this file must state that baseline may have drifted and re-validation against live main is required before applying.

## Step 7 — Package and Verify (mandatory before reporting success)

zip -r step1-prompt-blocker-cleanup-patch-pack.zip <patch-pack-dir>
ls -la step1-prompt-blocker-cleanup-patch-pack.zip
unzip -l step1-prompt-blocker-cleanup-patch-pack.zip
Confirm the listing includes every patch actually created, the manifest, and the handoff file. Do not report success if this listing is empty, missing files, or unverified. Make the ZIP available as a downloadable file in this conversation and confirm it is present in your response.

If mode_used = "live_repo", also attempt commit and push per file; if push fails, fall back to Step 7 packaging instead of claiming success.

## Final Report

Return exactly:

FINAL_REPORT:
mode_used: "live_repo" | "api_mirror"
verdict: PASS | PARTIAL | FAIL
baseline_commit_sha: "<sha-or-NA>"
target_files_total: 22
target_files_patched: <count>
files_not_fetched: []
files_failed: []
each_patch_apply_check: PASS|FAIL
cumulative_marker_validation: PASS|FAIL
forbidden_files_touched: false
zip_created: true|false
zip_contents_verified: true|false
pushed_to_origin: true|false
requires_live_repo_revalidation: true|false

verdict = PASS only if target_files_patched = 22 and all validations pass and (pushed_to_origin = true OR zip fully verified). Otherwise PARTIAL (some files done, honestly reported) or FAIL (nothing usable produced).

Here is the consolidated version — incorporates every fix identified in the gap analysis, keeps the access-declaration and honest-partial-completion mechanics from the prior revision, and closes the four remaining gaps: undefined "clean copy," missing directory creation, undefined patch filenames, and Step 3/2 ordering.[^1][^2]

```
# APEX Step 1 Patch-Pack Builder

## Role
You build a validated patch pack for 22 target files in leela-spec/apexai-os-meta, branch main. Output: one .patch file per target, a manifest, and an apply-handoff file, delivered as a verified downloadable ZIP.

## Step 0 — Access Declaration (mandatory, run first, do not skip or repeat)
Determine and state explicitly, before any other action:

ACCESS_DECLARATION:
  live_git_worktree_present: true|false   (checked via: pwd; git rev-parse --show-toplevel — run once only)
  github_connector_available: true|false  (checked via one list_resources call — run once only)
  source_plan_readable: true|false        (checked via one fetch attempt)
  mode_selected: "live_repo" | "api_mirror" | "blocked"

Rules:
- Run each check exactly once. Do not repeat, re-verify, or re-search after a result is obtained. A "not found" result is final and authoritative for this run.
- If live_git_worktree_present is true AND it points to leela-spec/apexai-os-meta: mode_selected = "live_repo".
- Else if github_connector_available is true: mode_selected = "api_mirror".
- Else: mode_selected = "blocked". Stop and report ACCESS_DECLARATION only, with no further action.
- Do not attempt git clone under any circumstance — this environment has no network clone capability.
- Print the ACCESS_DECLARATION block before proceeding to Step 1.

## Step 1 — Read Source Plan
Fetch (via live repo or connector, per mode_selected):
apex-meta/patch-plans/2026-07-07-step1-prompt-blocker-cleanup-plan.okf.md

If unreadable, stop:
SOURCE_ACCESS_FAILED: missing source plan, cannot proceed.

Read section 7 (Per-Target Contracts), section 8 (Cross-File Consistency), section 9 (Forbidden Paths) fully now. Hold them in context for the full run — do not re-fetch these sections later.

## Step 2 — Target List
001 .claude/Claude.md
002 .claude/skills/PrecapNextDay/Skill_precap-next-day.md
003 .claude/skills/PrecapWeek/Skill_Precap-Week.md
004 .claude/skills/PrecapWeek/package-manifest.md
005 .claude/skills/PrecapWeek/references/calendar-planning-guidance.md
006 .claude/skills/PrecapWeek/references/weekly-plan-output-contract.md
007 .claude/skills/PrecapWeek/references/weekly-blueprint-standard.md
008 .claude/skills/PrecapWeek/references/weekly-blueprint-meeting-example.md
009 .claude/skills/PrecapWeek/references/validation-checklist.md
010 .claude/skills/PrecapNextDay/precap-next-day-package-manifest.md
011 .claude/skills/PrecapNextDay/references/operator-output-format-design.md
012 .claude/skills/PrecapNextDay/templates/next-day-plan-operator-template.md
013 .claude/skills/PrecapNextDay/references/prompt-engineering-dependency-contract.md
014 .claude/skills/PrecapNextDay/references/usage-tracking-dependency-contract.md
015 .claude/skills/PrecapNextDay/references/workflow-process-validation-contract.md
016 .claude/skills/ProjectStatus/package-manifest.md
017 .claude/skills/AIRouting/ai-routing-and-usage-tracking-SKILL.md
018 .claude/skills/AIRouting/ai-routing-and-usage-tracking-package-manifest.md
019 .claude/skills/raw-flow-dump-normalize/SKILL.md
020 .claude/skills/status-merge/SKILL.md
021 .claude/skills/project-kb-manager/SKILL.md
022 .claude/skills/model-usage-log/templates/model-usage-delta-template.md

Patch filename rule (deterministic, no invented naming): <NNN>-<basename-of-target-without-extension>.patch
Example: target .claude/skills/PrecapWeek/package-manifest.md → patch 004-package-manifest.patch

Patch-pack directory (fixed for this run): patch-packs/2026-07-07-step1-prompt-blocker-cleanup/

Forbidden — never write to: state/**, .claude/kb/**, source-knowledge/**, ApexDefinition&OldVersions/**, .github/workflows/**, scripts/**, **/*.py

## Step 3 — Prepare Working Copy
If mode_selected = "live_repo": use the real checkout directly. Confirm clean state (git status --porcelain prints nothing), then proceed.

If mode_selected = "api_mirror": build a local git repo seeded from real fetched content only.
  mkdir -p /home/oai/share/mirror && cd /home/oai/share/mirror && git init -q
For each of the 22 target files listed in Step 2, fetch its real current content via the connector and write it verbatim. If a fetch fails for a file marked create_if_missing in the plan, treat as empty baseline. If a fetch fails for any other file, record it in files_not_fetched and exclude it from this run — do not substitute placeholder text.
  git add -A && git commit -q -m "Baseline mirror, fetched $(date -u +%FT%TZ)"
Record this commit hash as baseline_commit_sha. This commit is the sole reference point for all later validation — there is no other "clean" state in this run.

Create the patch-pack output directory now, before the loop:
  mkdir -p patch-packs/2026-07-07-step1-prompt-blocker-cleanup

## Step 4 — Per-File Iteration Loop (repeat for each target in order)
1. Read the target file's current real content (already present from Step 3 — do not re-fetch).
2. Read that file's required_markers / forbidden_markers from source plan section 7 (already in context from Step 1 — do not re-fetch the plan).
3. Apply only the required change to that file.
4. Generate patch: `git diff --no-ext-diff -- <file> > patch-packs/2026-07-07-step1-prompt-blocker-cleanup/<patch-filename>`
5. Validate: file is non-empty, `grep '^diff --git '` shows exactly one line for this file only.
6. Revert file: `git checkout -- <file>`.
7. Validate patch applies clean against baseline_commit_sha: `git apply --check <patch-file>`.
8. Apply and verify:
   git apply <patch-file>
   grep -q "<required_marker>" <file>   (must find each required marker)
   grep -L "<forbidden_marker>" <file>  (must NOT find any forbidden marker)
   git checkout -- <file>
9. Commit patch artifact only:
   git add patch-packs/2026-07-07-step1-prompt-blocker-cleanup/<patch-filename>
   git commit -q -m "Add patch <NNN>"
10. Move to next file.

If a step fails for a given file after one retry, record it in files_failed with the reason and move to the next file. Do not stop the whole run for one file's failure. Do not fabricate content to force success — a skipped file is acceptable, a fabricated file is never acceptable.

## Step 5 — Cumulative Validation
Reset the working copy to baseline_commit_sha (this is the "clean copy" — the only one that exists in this run). Apply all generated patches in order; confirm only the intended target files change; run all required/forbidden marker greps from source plan section 7 across the result; then reset back to baseline_commit_sha again.

## Step 6 — Manifest and Handoff
Create 000-patch-manifest.md: mode used, baseline_commit_sha, source plan path, per-patch purpose, validation results, files_not_fetched, files_failed.
Create 999-apply-patches.md: deterministic instructions to apply these patches against the real live repo (checkout main, pull, apply --check each, apply, verify markers, commit, push). If mode_used was api_mirror, this file must state that baseline may have drifted and re-validation against live main is required before applying.

## Step 7 — Package and Verify (mandatory before reporting success)
  zip -r step1-prompt-blocker-cleanup-patch-pack.zip patch-packs/2026-07-07-step1-prompt-blocker-cleanup/
  ls -la step1-prompt-blocker-cleanup-patch-pack.zip
  unzip -l step1-prompt-blocker-cleanup-patch-pack.zip
Confirm the listing includes every patch actually created plus the manifest and handoff file. Do not report success if this listing is empty, missing files, or unverified. Make the ZIP available as a downloadable file in this conversation and confirm it is present in your response.

If mode_used = "live_repo", also attempt commit and push per file; if push fails, fall back to this packaging step instead of claiming success.

## Final Report
Return exactly:

FINAL_REPORT:
  mode_used: "live_repo" | "api_mirror"
  verdict: PASS | PARTIAL | FAIL
  baseline_commit_sha: "<sha-or-NA>"
  target_files_total: 22
  target_files_patched: <count>
  files_not_fetched: []
  files_failed: []
  each_patch_apply_check: PASS|FAIL
  cumulative_marker_validation: PASS|FAIL
  forbidden_files_touched: false
  zip_created: true|false
  zip_contents_verified: true|false
  pushed_to_origin: true|false
  requires_live_repo_revalidation: true|false

verdict = PASS only if target_files_patched = 22 and all validations pass and (pushed_to_origin = true OR zip fully verified).
Otherwise verdict = PARTIAL (some files done, honestly reported) or FAIL (nothing usable produced).
```


## What changed from the version I flagged, and why

| Fix | Location | Closes |
| :-- | :-- | :-- |
| "Against a clean copy" replaced with explicit `baseline_commit_sha` reset | Step 5 | Removes the exact ambiguity that historically caused improvised clone/local-path detours [^1] |
| `mkdir -p` for the patch-pack directory added before the loop starts | Step 3 (end) | Prevents shell errors from an undeclared directory, which previously caused route-around improvisation [^1] |
| Deterministic patch filename rule stated explicitly | Step 2 | Removes ungoverned naming, keeps manifest traceability consistent across all 22 files [^1] |
| Target list moved before working-copy setup | Step 2 → Step 3 reordered | Removes forward-reference ambiguity ("the 22 target files below" appearing before the list existed) [^1] |
| Git commands in apply/commit steps kept fully literal | Step 4.8–4.9 | Confirmed present per your direct check — retained as-is [^3] |

This version has no known-open gaps against the failure history reviewed so far. It cannot be verified as "will succeed" until run — that depends on real Agent Mode container behavior — but every previously identified failure mechanism (repeated discovery loops, fabricated placeholders, unverified ZIP, ambiguous "clean" state, undeclared directories, ungoverned naming) now has an explicit, closed rule against it.

<div align="center">⁂</div>

[^1]: verify-this-is-a-legit-prompt-and-does-not-overeng.md

[^2]: create-a-new-version-of-the-prompt.-look-in-the-in-2.md

[^3]: is-that-puprompt-really-using-git-to-create-the-ac-3.md

