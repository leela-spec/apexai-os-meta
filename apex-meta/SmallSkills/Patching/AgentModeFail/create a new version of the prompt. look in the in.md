<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# create a new version of the prompt. look in the intenret for best rpactice for a browser chat gpt. 5.5. agent mode prompt with our specifics. incorporate all your elarnigns but guard against overengineering and creating new failure modes. the agent should focus in the target and the iterative process, not failure modes and failure history or stale info. clearly state if ou can acccess all files and insturctions or if  you need to retreive from drift dangeruous memory

Web research on Agent Mode prompting confirms the direction needed: fewer, sharper sections beat exhaustive ones; state must be verified as an operating rule (not assumed from narrative); and branching logic should be phrased as "if expected state absent, do X" rather than folded into failure-history narration. Applying that, here's a leaner rebuild focused purely on target + iteration, with environment access stated as a mandatory upfront declaration rather than embedded failure lore.[^1]

***

```
# APEX Step 1 Patch-Pack Builder

## Role
You build a validated patch pack for 22 target files in leela-spec/apexai-os-meta, branch main. Output: one .patch file per target, a manifest, and an apply-handoff file, delivered as a verified downloadable ZIP.

## Step 0 — Access Declaration (mandatory, do this first, do not skip)
Determine and state explicitly, before any other action:

ACCESS_DECLARATION:
  live_git_worktree_present: true|false   (checked via: pwd; git rev-parse --show-toplevel — run once only)
  github_connector_available: true|false  (checked via one list_resources call — run once only)
  source_plan_readable: true|false        (checked via one fetch attempt)
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
  mkdir -p /home/oai/share/mirror && cd /home/oai/share/mirror && git init -q
For each of the 22 target files below, fetch its real current content via the connector and write it verbatim. If a fetch fails for a file marked create_if_missing in the plan, treat as empty baseline. If a fetch fails for any other file, record it in files_not_fetched and exclude it from this run — do not substitute placeholder text.
  git add -A && git commit -q -m "Baseline mirror, fetched $(date -u +%FT%TZ)"
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

Forbidden — never write to: state/**, .claude/kb/**, source-knowledge/**, ApexDefinition&OldVersions/**, .github/workflows/**, scripts/**, **/*.py

## Step 4 — Per-File Iteration Loop (repeat for each target in order)
1. Read the target file's current real content (already in mirror/worktree from Step 2 — do not re-fetch).
2. Read that file's required_markers / forbidden_markers from source plan section 7 (already in context from Step 1 — do not re-fetch the plan).
3. Apply only the required change to that file.
4. Generate patch: `git diff --no-ext-diff -- <file> > patch-packs/<NNN>-<name>.patch`
5. Validate: file is non-empty, `grep '^diff --git '` shows exactly one line for this file only.
6. Revert file: `git checkout -- <file>`.
7. Validate patch applies clean: `git apply --check <patch-file>`.
8. Apply, confirm required_markers present and forbidden_markers absent, then revert again.
9. Commit the patch file only (not the target file).
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
```


***

## What's different from PromptClaude.md, and why

| Change | Reasoning |
| :-- | :-- |
| Single upfront `ACCESS_DECLARATION` step instead of scattered preflight checks | Prevents the repeated `find`/`env`/API-recheck loops that burned budget before any real work started — each check runs exactly once, by rule |
| No mention of past failures, fallback archive lore, or synthetic-repo warnings in the body | Per web best practice, agents drift less with fewer, sharper rules — narrating failure history invites the agent to reason about failure instead of the task [^1] |
| Per-file loop explicitly allows partial completion (`files_failed`, `files_not_fetched`) instead of forcing all-or-nothing | Directly closes the loophole that caused full fabrication under perceived time pressure — skipping is now an explicitly sanctioned, honest outcome |
| Plan sections and file content are read once and held in context, not re-fetched per patch | Removes redundant re-fetching seen in the failed transcript |
| Mirror mode formalized as a first-class named mode, not an improvisation | Matches what actually worked in the successful run, without requiring the agent to invent it under pressure |
| Verdict has three tiers (PASS/PARTIAL/FAIL) instead of a misleading PARTIAL_ARTIFACT_EXPORT | Makes partial-but-honest outcomes reportable without pressure to either lie or over-deliver |
| ZIP verification is a hard gate before any success claim | Directly fixes the ZIP-loss failure from the previous run |

This version is shorter than PromptClaude.md by design — per the best-practice guidance found, Agent Mode performs better with fewer, precise constraints than with exhaustive narrated context. It states access status transparently up front rather than assuming or hiding it, and it treats "I can't fetch everything" as a normal, reportable outcome rather than a reason to fabricate.[^1]
<span style="display:none">[^10][^11][^12][^13][^14][^15][^16][^2][^3][^4][^5][^6][^7][^8][^9]</span>

<div align="center">⁂</div>

[^1]: https://www.reddit.com/r/PromptEngineering/comments/1prx3w3/what_prompt_structure_works_best_for_chatgpt/

[^2]: https://www.aiforwardmarketer.com/best-practices-prompting-chatgpt-in-agent-mode/

[^3]: https://blog.postman.com/seven-best-practices-for-writing-high-quality-prompts/

[^4]: https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api

[^5]: https://www.youtube.com/watch?v=VZFYG0tdY8Y

[^6]: https://www.youtube.com/watch?v=k50ZVChTLo8

[^7]: https://shumer.dev/prompting-ai-agents

[^8]: https://www.youtube.com/watch?v=d2QT8eTr9Q8

[^9]: https://developers.openai.com/cookbook/examples/gpt4-1_prompting_guide

[^10]: https://medium.com/@jennette_cajucom/i-used-chatgpt-agent-mode-and-heres-what-i-learned-740926fe24b1

[^11]: https://www.datablist.com/how-to/rules-writing-prompts-ai-agents

[^12]: https://www.kommunicate.io/blog/chatgpt-agent-mode/

[^13]: https://www.youtube.com/watch?v=YXK7YpQamiw

[^14]: https://theproductspace.in/blogs/artificial-intelligence/openai-latest-at-the-2026-ai-summit

[^15]: https://zapier.com/blog/gpt-prompt/

[^16]: PromptClaude.md

