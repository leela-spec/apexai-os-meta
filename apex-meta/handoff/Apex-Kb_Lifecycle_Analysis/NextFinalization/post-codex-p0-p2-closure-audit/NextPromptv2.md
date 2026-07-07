# Apex KB v3 P0-P2 Closure Repair Patch-Pack Builder - Agent Mode Prompt v1

You are GPT-5.5 Agent Mode acting as the Apex KB v3 P0-P2 Closure Repair Patch-Pack Builder.

Your job is to create a validated, durable patch pack that is either:

1. committed and pushed to the real repository, patch by patch, or
2. exported as a downloadable archive if and only if repository push is unavailable.

Your job is NOT to directly apply the final target-file changes to the repository.

The final repo state, after this task, must contain patch artifacts only. The target files must be clean and unmodified in the final commit.

Do not use previous failed Agent Mode output as source material.
Do not read a giant failed transcript.
Do not reconstruct from memory.
Do not create a synthetic repo from copied connector files.
Use the live terminal Git repository as the only source of truth for patch generation.

Repository:
leela-spec/apexai-os-meta

Branch:
main

Patch-pack path:
apex-meta/patches/apex-kb-v3-p0-p2-closure-repair/

Primary source reports to read first:

apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NextFinalization/post-codex-p0-p2-closure-audit/connector-detective-audit-and-repair-plan.md

apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NextFinalization/post-codex-p0-p2-closure-audit/local-behavioral-check-report.md

If either source report is not readable, stop with:

SOURCE_ACCESS_FAILED:
  missing:
    - "<missing report path>"
  action_needed: "Pull origin/main or confirm the source-report path."

Target files for patch generation:

001:
  target_file: apex-meta/scripts/apex_kb.py
  patch_file: apex-meta/patches/apex-kb-v3-p0-p2-closure-repair/001-apex-kb-p0-p2-closure-repair.patch

002:
  target_file: .claude/skills/apex-kb/references/script-command-contract.md
  patch_file: apex-meta/patches/apex-kb-v3-p0-p2-closure-repair/002-script-command-contract-align-behavior.patch

003:
  target_file: .claude/skills/apex-kb/references/acceptance-tests.md
  patch_file: apex-meta/patches/apex-kb-v3-p0-p2-closure-repair/003-acceptance-tests-p0-p2-closure-repair.patch

004:
  target_file: .claude/skills/apex-kb/examples/powershell-commands.md
  patch_file: apex-meta/patches/apex-kb-v3-p0-p2-closure-repair/004-powershell-commands-p0-p2-closure-repair.patch

Allowed patch-pack outputs:

- apex-meta/patches/apex-kb-v3-p0-p2-closure-repair/000-patch-manifest.md
- apex-meta/patches/apex-kb-v3-p0-p2-closure-repair/001-apex-kb-p0-p2-closure-repair.patch
- apex-meta/patches/apex-kb-v3-p0-p2-closure-repair/002-script-command-contract-align-behavior.patch
- apex-meta/patches/apex-kb-v3-p0-p2-closure-repair/003-acceptance-tests-p0-p2-closure-repair.patch
- apex-meta/patches/apex-kb-v3-p0-p2-closure-repair/004-powershell-commands-p0-p2-closure-repair.patch
- apex-meta/patches/apex-kb-v3-p0-p2-closure-repair/999-codex-apply-patches.md
- apex-meta/patches/apex-kb-v3-p0-p2-closure-repair/validation-report.md

Hard forbidden files and folders:

- .claude/skills/apex-kb2/
- apex-meta/kb/*/wiki/
- apex-meta/kb/*/ingest-analysis/
- apex-meta/scripts/apex_kb_retrieval.py
- apex-meta/patches/apex-kb-v3-p0-p2-closure/
- derived/
- outputs/
- raw/
- sources/
- tmp/
- old failed patch files

Required repair changes:

1. Preserve existing working behavior:
   - CLI global flag normalization.
   - --output-json support.
   - status freshness split:
     - wiki_index_status
     - retrieval_index_status
     - source_payload_manifest_status.

2. Repair pointer_only Phase 0 behavior in apex-meta/scripts/apex_kb.py:
   - Resolve safe kb-local and repo-local pointer_only text files.
   - Include resolved pointer_only text files in Phase 0 scanning.
   - Truthfully report:
     - pointer_only_sources
     - pointer_only_scanned_count
     - pointer_only_unresolved
     - pointer_only_warning_count
   - Do not silently report pointer_only_unresolved as [] unless there are actually no unresolved pointers.

3. Repair quality / coverage behavior in apex-meta/scripts/apex_kb.py:
   - Read wiki page frontmatter source_refs.
   - Populate page_to_source_map.
   - Populate source_to_page_map.
   - Include manifest sources even when no page references them.
   - Detect shell_page_candidates using:
     - missing source_refs
     - low body density
     - missing Phase 2 value-contract sections.
   - Detect phase2_repair_candidates when pages miss:
     - Adaptive Ranked Source Set
     - Macro / Meso / Micro
     - Key Claims
     - Routes Here
     - Uncertainty / Raw Source Triggers.

4. Repair query-eval behavior in apex-meta/scripts/apex_kb.py:
   - --init without --allow-write reports the planned write only.
   - --init with --allow-write creates:
     outputs/queries/evals/query-eval-pack.json
   - Existing query-eval-pack.json is read and validated.
   - Validate entries for:
     - query
     - expected_routes
     - expected_minimal_pages
     - raw_source_needed
   - Return:
     - status
     - issue_count
     - query-eval-pack.json path
     - expected_minimal_pages
     - raw_source_needed.

5. Repair graph / process-graph behavior in apex-meta/scripts/apex_kb.py:
   - Use deterministic Python stdlib extraction only.
   - Read KB text files only.
   - Extract:
     - markdown_links
     - wikilinks
     - repo_path_references
     - yaml_path_references
     - process_sequence_edges.
   - If --allow-write is present, write graph artifacts under:
     manifests/phase0/
   - Do not crawl the whole repository outside the KB root.

6. Update .claude/skills/apex-kb/references/script-command-contract.md:
   - Update only to match implemented behavior.
   - Remove or soften unsupported claims.
   - Do not document behavior that the script does not implement.

7. Update .claude/skills/apex-kb/references/acceptance-tests.md:
   - Add deterministic acceptance checks for:
     - pointer_only Phase 0
     - quality / coverage maps
     - shell page candidates
     - query-eval --init
     - graph / process-flow extraction.

8. Update .claude/skills/apex-kb/examples/powershell-commands.md:
   - Add PowerShell-safe examples for:
     - status with --output-json
     - quality with --output-json
     - query-eval --init with and without --allow-write
     - graph with --output-json
     - post-repair validation.

Do not add new dependencies.
Do not redesign the lifecycle.
Do not patch retrieval.
Do not rewrite existing generated wiki pages.
Do not create a new KB.

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

mkdir -p apex-meta/patches/apex-kb-v3-p0-p2-closure-repair/

Read first:

- both source reports
- every target file listed above

Before editing, create an internal file-change map for all four patches.
Do not commit this internal map unless summarized inside 000-patch-manifest.md.

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

For each patch 001 through 004, do exactly this sequence.

A. Confirm clean target:

git checkout -- <target-file>
git status --porcelain -- <target-file>

The status command must print nothing.

B. Modify only <target-file> according to the source reports and required repair changes.

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

For 001, also run:

python -m py_compile apex-meta/scripts/apex_kb.py

For 002, 003, and 004, run grep checks relevant to the changed document.

I. Revert target again:

git checkout -- <target-file>
git status --porcelain -- <target-file>

The status command must print nothing.

J. Commit and push this patch artifact only:

git add <patch-file>
git diff --cached --name-only

The staged diff must list only <patch-file>.

Then:

git commit -m "Add Apex KB P0-P2 closure repair patch <NNN>"
git push origin main

If git push fails, stop normal repo mode and go to FALLBACK ARCHIVE MODE.

CUMULATIVE VALIDATION AFTER 001-004 ARE PUSHED

From clean main, run:

git pull --ff-only origin main
git status --porcelain

Then check every patch:

for p in apex-meta/patches/apex-kb-v3-p0-p2-closure-repair/*.patch; do git apply --check "$p" || exit 1; done

Apply all patches in numeric order:

for p in apex-meta/patches/apex-kb-v3-p0-p2-closure-repair/*.patch; do git apply "$p" || exit 1; done

Run compile validation:

python -m py_compile apex-meta/scripts/apex_kb.py

Run command help validation:

python apex-meta/scripts/apex_kb.py --help
python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/claude-skill-design quality --help
python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/claude-skill-design query-eval --help
python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/claude-skill-design graph --help

Run grep validations:

grep -R "pointer_only_scanned_count" -n apex-meta/scripts/apex_kb.py
grep -R "source_to_page_map" -n apex-meta/scripts/apex_kb.py
grep -R "page_to_source_map" -n apex-meta/scripts/apex_kb.py
grep -R "shell_page_candidates" -n apex-meta/scripts/apex_kb.py
grep -R "phase2_repair_candidates" -n apex-meta/scripts/apex_kb.py
grep -R "issue_count" -n apex-meta/scripts/apex_kb.py
grep -R "process_sequence" -n apex-meta/scripts/apex_kb.py

grep -R "Adaptive Ranked Source Set" -n .claude/skills/apex-kb/references/script-command-contract.md .claude/skills/apex-kb/references/acceptance-tests.md
grep -R "Macro / Meso / Micro" -n .claude/skills/apex-kb/references/script-command-contract.md .claude/skills/apex-kb/references/acceptance-tests.md
grep -R "Routes Here" -n .claude/skills/apex-kb/references/script-command-contract.md .claude/skills/apex-kb/references/acceptance-tests.md
grep -R "Uncertainty / Raw Source Triggers" -n .claude/skills/apex-kb/references/script-command-contract.md .claude/skills/apex-kb/references/acceptance-tests.md

Run local behavior checks against claude-skill-design.

Record the JSON outputs in validation-report.md.

Do not fail solely because claude-skill-design has missing lifecycle artifacts.

Fail if:

- a command crashes
- a command returns invalid JSON
- repaired output fields are absent
- quality still lacks source_to_page_map or page_to_source_map fields
- query-eval still lacks status or issue_count fields
- graph still lacks the repaired edge-category fields

Grep validation is supplementary only. It must not replace git apply, compile, and command-output validation.

KB_ROOT="apex-meta/kb/claude-skill-design"
OUT_DIR="log/post-codex-p0-p2-repair-validation"
mkdir -p "$KB_ROOT/$OUT_DIR"

python apex-meta/scripts/apex_kb.py --kb-root "$KB_ROOT" status --json --output-json "$OUT_DIR/status-after-repair.json"
python apex-meta/scripts/apex_kb.py --kb-root "$KB_ROOT" quality --json --output-json "$OUT_DIR/quality-after-repair.json"
python apex-meta/scripts/apex_kb.py --kb-root "$KB_ROOT" query-eval --init --json --output-json "$OUT_DIR/query-eval-after-repair.json"
python apex-meta/scripts/apex_kb.py --kb-root "$KB_ROOT" graph --json --output-json "$OUT_DIR/graph-after-repair.json"

Do not commit these KB log outputs.

Check changed files:

git diff --name-only

The changed files must be only the four target files listed above.
No forbidden files may appear.

Revert cumulative target-file changes:

git checkout -- apex-meta/scripts/apex_kb.py
git checkout -- .claude/skills/apex-kb/references/script-command-contract.md
git checkout -- .claude/skills/apex-kb/references/acceptance-tests.md
git checkout -- .claude/skills/apex-kb/examples/powershell-commands.md

Remove uncommitted validation logs if created:

rm -rf apex-meta/kb/claude-skill-design/log/post-codex-p0-p2-repair-validation

Run:

git status --porcelain

Only patch-pack metadata files that are intentionally being created may remain untracked or modified.

CREATE AND COMMIT MANIFEST

Create:

apex-meta/patches/apex-kb-v3-p0-p2-closure-repair/000-patch-manifest.md

Manifest must include:

- repository and branch
- source reports read
- exact target files read
- exact patch files created
- patch-to-target map
- purpose of each patch
- individual validation command per patch
- cumulative validation commands
- grep validation results
- forbidden files/folders
- statement that target files were reverted and are not modified in the patch-pack commit
- commit SHAs for patch artifact commits if available

Commit and push manifest only:

git add apex-meta/patches/apex-kb-v3-p0-p2-closure-repair/000-patch-manifest.md
git diff --cached --name-only
git commit -m "Add Apex KB P0-P2 closure repair patch manifest"
git push origin main

CREATE AND COMMIT VALIDATION REPORT

Create:

apex-meta/patches/apex-kb-v3-p0-p2-closure-repair/validation-report.md

Validation report must include:

- preflight result
- dirty-file report
- per-patch apply-check result
- cumulative apply-check result
- compile result
- command help result
- behavior-check result
- final target-file cleanliness result

Commit and push validation report only:

git add apex-meta/patches/apex-kb-v3-p0-p2-closure-repair/validation-report.md
git diff --cached --name-only
git commit -m "Add Apex KB P0-P2 closure repair validation report"
git push origin main

CREATE AND COMMIT CODEX APPLY HANDOFF

Create:

apex-meta/patches/apex-kb-v3-p0-p2-closure-repair/999-codex-apply-patches.md

It must be a deterministic command prompt for Codex that says:

- repo: leela-spec/apexai-os-meta
- branch: main
- work directly on main
- do not create branch
- do not open PR
- run git checkout main
- run git pull --ff-only origin main
- run git apply --check for each patch in numeric order
- run git apply for each patch in numeric order
- run compile validation
- run command help validation
- run behavior checks
- verify only the four target files changed
- verify forbidden files were not touched
- commit and push target-file changes

Commit and push handoff only:

git add apex-meta/patches/apex-kb-v3-p0-p2-closure-repair/999-codex-apply-patches.md
git diff --cached --name-only
git commit -m "Add Codex handoff for Apex KB P0-P2 closure repair patches"
git push origin main

FINAL REPO CHECK

Run:

git status --porcelain
git log --oneline -n 15

Final status must be clean except unrelated dirty files that were already present before the task and do not overlap the target, forbidden, or patch-pack paths.

FALLBACK ARCHIVE MODE

Use this only if normal repo mode cannot push to origin or no real origin exists.

Rules:

- Do not claim repo delivery.
- Do not create or use a synthetic repo as if it were the real repo.
- Still generate whatever patch artifacts can be generated from the real local checkout.
- Validate them with git apply --check if possible.
- Create 000-patch-manifest.md, validation-report.md, and 999-codex-apply-patches.md locally.
- Create an archive named apex-kb-v3-p0-p2-closure-repair-patch-pack.zip.

Preferred archive output paths:

1. /mnt/data/apex-kb-v3-p0-p2-closure-repair-patch-pack.zip if /mnt/data exists.
2. ./apex-kb-v3-p0-p2-closure-repair-patch-pack.zip otherwise.

Archive must contain:

- 000-patch-manifest.md
- all generated .patch files
- validation-report.md
- 999-codex-apply-patches.md
- FALLBACK-REPORT.md explaining exactly why repo push was unavailable

In fallback mode final report verdict must be:

PARTIAL_ARTIFACT_EXPORT

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
  patch_pack_path: "apex-meta/patches/apex-kb-v3-p0-p2-closure-repair/"
  patch_files_created:
    - "apex-meta/patches/apex-kb-v3-p0-p2-closure-repair/001-apex-kb-p0-p2-closure-repair.patch"
    - "apex-meta/patches/apex-kb-v3-p0-p2-closure-repair/002-script-command-contract-align-behavior.patch"
    - "apex-meta/patches/apex-kb-v3-p0-p2-closure-repair/003-acceptance-tests-p0-p2-closure-repair.patch"
    - "apex-meta/patches/apex-kb-v3-p0-p2-closure-repair/004-powershell-commands-p0-p2-closure-repair.patch"
  individual_patch_commits:
    "001": "<sha-or-NA>"
    "002": "<sha-or-NA>"
    "003": "<sha-or-NA>"
    "004": "<sha-or-NA>"
  manifest_commit_sha: "<sha-or-NA>"
  validation_report_commit_sha: "<sha-or-NA>"
  handoff_commit_sha: "<sha-or-NA>"
  each_patch_git_apply_check: PASS|FAIL
  cumulative_patch_check: PASS|FAIL
  cumulative_grep_validation: PASS|FAIL
  py_compile: PASS|FAIL
  behavior_validation: PASS|FAIL
  target_files_modified_by_patch_pack_commits: false
  final_repo_status_clean: true|false
  forbidden_files_touched: false
  fallback_archive: "<path-or-NA>"
  failure_reason: "<reason-or-NA>"