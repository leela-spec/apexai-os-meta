<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# verify this is a legit prompt and does not overengineer or introduce new failures or does something wroong we know already can only fail:

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

Reasonably solid — the two previously-fatal failure modes (fabrication-under-pressure, unverified ZIP loss) are now explicitly closed. But there are four real gaps that map directly onto behaviors we've already seen this agent do. Not a pushover pass.

## What's correctly fixed

| Prior failure | Status in this prompt |
| :-- | :-- |
| Repeated repo-hunting loop burning budget | Fixed — Step 0 caps discovery to one check each, explicit "run once only" |
| Fabricated placeholder content under time pressure | Fixed — Step 4 explicitly allows honest partial failure (`files_failed`) instead of forcing completion |
| Unverified/lost ZIP export | Fixed — Step 7 hard-gates success on `ls -la` + `unzip -l` output actually being checked |
| Misleading verdict labels (PARTIAL_ARTIFACT_EXPORT) | Fixed — three clean tiers with explicit PASS conditions |
| git commands left implicit (your last question) | Fixed — Step 4.8/4.9 now literal |

## Four real gaps that could still trigger known failure patterns

**1. Step 5 says "apply all generated patches... against a clean copy" — "clean copy" is undefined.**
This is exactly the kind of ambiguity that previously caused the agent to improvise (git clone, local Windows paths, synthetic repos). "Clean copy" could be interpreted as: the mirror's committed baseline (fine), or as "get a fresh copy of the real repo" (which could trigger a clone attempt again). Fix: explicitly say "against the baseline commit created in Step 2" — remove the ambiguous phrase entirely.

**2. Step 3 (target list) is positioned after Step 2, which already references "the 22 target files below."**
Minor, but this exact kind of forward-reference confusion is what caused truncated/partial plan reads in the failed transcript (the agent had to re-fetch content in chunks because instructions and data were interleaved awkwardly). Low risk here since it's a static list, but reordering Step 3 before Step 2 removes any ambiguity for free.

**3. No explicit `mkdir -p` for the patch-pack output directory before Step 4's loop.**

```
Step 4.4 writes to `patch-packs/<NNN>-<name>.patch` but nothing creates that directory. If the agent's shell errors on a missing directory, this is exactly the class of small friction that historically triggered the agent to "route around" with an improvised alternative path. One line (`mkdir -p patch-packs/2026-07-07-step1-prompt-blocker-cleanup`) closes it.
```

**4. `<name>` in the patch filename is never defined.**

```
PromptClaude.md had explicit descriptive names per patch (e.g. `001-root-claude-loop-source-authority.patch`). This version just says `<NNN>-<name>.patch` with no naming rule. Harmless for git mechanics, but it reopens a small but real risk: an ungoverned naming choice is one more place the agent can drift or invent inconsistent conventions across the 22 files, which slightly undermines the manifest's traceability. Either supply exact names per file, or state a deterministic rule (e.g. filename derived from target file's basename).
```


## Verdict

Legitimate and materially safer than PromptClaude.md — the fabrication and ZIP-loss failure modes are genuinely closed, not just narrated around. But it is not yet a "known-safe" ship-it version: gap \#1 (undefined "clean copy") is the highest risk because it's precisely the kind of vague instruction that has previously caused the agent to invent clone/local-path workarounds. Fix that phrase and add the `mkdir -p` line before running this for real.

