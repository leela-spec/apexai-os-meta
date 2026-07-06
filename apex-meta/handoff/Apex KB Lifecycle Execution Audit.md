````
# Apex KB Lifecycle Execution Audit - apex-plan-sync-session-workflow-v2

## Purpose

Audit the Codex execution of the Apex KB lifecycle for:

```yaml
repo: leela-spec/apexai-os-meta
local_repo: C:\GitDev\apexai-os-meta
branch: main
kb_slug: apex-plan-sync-session-workflow-v2
kb_root: apex-meta/kb/apex-plan-sync-session-workflow-v2/
````

This audit should validate whether the lifecycle was executed safely, deterministically, and according to the operator instructions, and identify where instructions, scripts, or process contracts should be patched.

## Execution Summary

Two main lifecycle passes occurred.

### Pass 1: Fresh KB Lifecycle Through Phase 1

Goal:

- Create fresh KB folder.
- Run deterministic Apex KB lifecycle.
- Create Phase 1 ingest-analysis files.
- Stop before Phase 2.
- Commit and push.

Final commit pushed:

```
commit_sha: c9a4dcb92411d52390ed3adca3b9ecc785a115a0
```

Created:

```
kb_root: apex-meta/kb/apex-plan-sync-session-workflow-v2/
phase1_files:
  - ingest-analysis/batch01-workflow-boundary.analysis.md
  - ingest-analysis/batch02-apex-plan.analysis.md
  - ingest-analysis/batch03-apex-sync.analysis.md
  - ingest-analysis/batch04-apex-session.analysis.md
  - ingest-analysis/batch05-handoffs-and-gates.analysis.md
  - ingest-analysis/phase1-completion-report.md
```

Commands completed:

```
commands:
  - scaffold
  - health
  - status
  - source-intake
  - hash
  - preflight
  - phase0
  - lint
  - audit
  - status-final
```

### Pass 2: Deterministic Checks After Phase 1

Goal:

- Verify Phase 1 files.
- Run deterministic lint, audit, status.
- Optionally run health.
- Create continuation report.
- Commit and push.

Final commit pushed:

```
commit_sha: 22362c0786f259b7b0ba4f461c13706a63f7cc31
```

Created logs:

```
logs:
  - log/lint-after-phase1.json
  - log/audit-after-phase1.json
  - log/status-after-phase1.json
  - log/health-after-phase1.json
  - log/deterministic-after-phase1-report.md
```

## Positive Findings

### 1. Branch Safety Was Enforced

Codex checked:

```
git branch --show-current
```

Result:

```
branch: main
```

Execution continued only because branch matched the required branch.

### 2. Existing Unrelated Worktree Changes Were Not Touched

Untracked and deleted files existed outside the KB root, including paths under:

```
FutureDevelopments&Research/...
scripts/extract_pdf_picture_pages.py
apex-meta/handoff/...
```

Codex staged only:

```
apex-meta/kb/apex-plan-sync-session-workflow-v2/
```

and later only:

```
apex-meta/kb/apex-plan-sync-session-workflow-v2/log/
```

This was safe and correctly avoided unrelated user changes.

### 3. Phase 2 Was Not Semantically Run

Codex did not run:

```
ingest-phase2 --allow-write
index --allow-write
```

No Phase 2 wiki synthesis content was authored manually.

Important nuance: the scaffold command itself created empty Phase 2-shaped directories. That is addressed below as a process/script tension.

### 4. Deterministic Checks Passed

Observed deterministic results:

```
lint:
  status: pass
  issue_count: 0

audit:
  item_count: 0
  mutations: false

status:
  source_count: 3
  phase0_artifacts_present: true
  index_status: fresh
  wiki_page_count: 1

health:
  python_version: 3.11.9
  sqlite_fts5_available: true
  tools:
    git: true
    rg: true
```

### 5. Phase 1 Gate Was Preserved

All Phase 1 analysis batches ended with:

```
operator_gate:
  phase2_allowed: false
  required_phrase: approve ingest
  note: "Phase 1 analysis exists for operator review. Wiki synthesis is blocked until explicit approval."
```

## Problems / Friction Points Encountered

## Problem 1: Apex KB CLI Flag Ordering Did Not Match Operator Instructions

The operator gave command shapes like:

```
python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/<slug>/ scaffold --json --allow-write
```

But the script rejected that:

```
error: unrecognized arguments: --json --allow-write
```

Actual working syntax required global flags before the subcommand:

```
python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/<slug>/ --json --allow-write scaffold
```

### Impact

- First scaffold attempt failed.
- Required workaround was discovered and used.
- Final lifecycle succeeded, but `commands_failed` included the initial scaffold flag-order attempt.

### Root Cause

The script uses argparse global options before subcommands, while the operator handover implies flags can appear after subcommands.

### Patch Suggestion: Documentation

Update handover command examples everywhere from:

```
python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/<slug>/ scaffold --json --allow-write
```

to:

```
python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/<slug>/ --json --allow-write scaffold
```

Similarly:

```
python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/<slug>/ --json lint
python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/<slug>/ --json audit
python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/<slug>/ --json status
```

### Patch Suggestion: Script

Make the CLI more forgiving by allowing `--json`, `--allow-write`, and `--dry-run` both before and after subcommands.

Possible implementation direction:

```
# Option A
# Add common flags to each subparser as aliases of global flags.

# Option B
# Preprocess argv and lift known global flags before subcommand parsing.
KNOWN_GLOBAL_FLAGS = {"--json", "--allow-write", "--dry-run", "--strict"}
```

Recommended: Option A, because it keeps argparse behavior explicit and discoverable in `--help`.

## Problem 2: `source-intake` Flag Names Differed From Instructions

Operator suggested:

```
source-intake --source .claude/skills/apex-plan/ --storage-mode pointer_only
```

Script help showed:

```
source-intake --source-path SOURCE_PATH --storage-mode pointer_only
```

Working command:

```
python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/<slug>/ --json --allow-write source-intake --source-path .claude/skills/apex-plan/ --storage-mode pointer_only
```

### Impact

No failed `source-intake` command occurred because Codex checked help first after seeing the earlier CLI mismatch.

### Patch Suggestion: Documentation

Replace `--source` with `--source-path` in lifecycle instructions.

### Patch Suggestion: Script

Add `--source` as an alias for `--source-path`:

```
source_parser.add_argument(
    "--source",
    "--source-path",
    dest="source_path",
    help="Source path to register."
)
```

This would preserve backward compatibility with operator handovers.

## Problem 3: `hash` Flag Name Differed From Instructions

Operator suggested:

```
hash --source .claude/skills/apex-plan/ --json
```

Script help showed:

```
hash --path PATH
```

Working command:

```
python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/<slug>/ --json hash --path .claude/skills/apex-plan/
```

### Patch Suggestion: Documentation

Replace `hash --source` with:

```
hash --path <source_path>
```

### Patch Suggestion: Script

Add `--source` as an alias for `--path` for the `hash` subcommand:

```
hash_parser.add_argument(
    "--path",
    "--source",
    dest="path",
    required=True
)
```

## Problem 4: Scaffold Created Phase 2-Shaped Directories Despite “Do Not Create” Instruction

Operator explicitly said do not create:

```
wiki/summaries/
wiki/concepts/
wiki/entities/
outputs/queries/
audit/resolved/
```

But the scaffold command itself created these directories:

```
wiki/concepts
wiki/entities
wiki/summaries
outputs/queries
audit/resolved
```

### Impact

This creates an apparent instruction violation even though it was caused by the official lifecycle scaffold command, not by semantic Phase 2 execution.

Codex did not author Phase 2 content inside them, but the directories were created.

### Risk

Future audits may incorrectly mark the run as violating the Phase 2 gate because empty scaffold directories exist.

### Patch Suggestion: Instruction

Clarify:

```
phase2_gate:
  do_not_run_phase2_commands: true
  do_not_create_phase2_content: true
  scaffold_may_create_empty_reserved_directories:
    - wiki/summaries/
    - wiki/concepts/
    - wiki/entities/
    - outputs/queries/
    - audit/resolved/
```

or:

```
If scaffold creates empty reserved directories, do not treat that alone as Phase 2 execution.
```

### Patch Suggestion: Script

Add a Phase 1 scaffold mode:

```
python apex-meta/scripts/apex_kb.py --kb-root <root> --json --allow-write scaffold --phase phase1
```

Expected behavior:

- Create raw, ingest-analysis, manifests, log.
- Create only `wiki/index.md`.
- Do not create semantic wiki/output/resolved-audit directories until Phase 2.

Alternative:

```
scaffold --minimal
```

## Problem 5: Phase 0 Reported `source_file_count: 0` Despite Three Pointer Sources

Phase 0 output:

```
source_file_count: 0
source_inventory:
  json_exists: false
  csv_exists: false
```

But source manifest had three pointer-only sources.

### Impact

Phase 0 artifacts were generated but did not inventory files from pointer-only source folders.

### Risk

The KB lifecycle may look internally inconsistent:

```
source_count: 3
phase0_source_file_count: 0
```

This may be expected behavior, but it is not obvious.

### Patch Suggestion: Documentation

Clarify whether Phase 0 reads:

- source manifest entries,
- source inventory files,
- copied raw files only,
- pointer-only paths.

Add explicit note:

```
phase0_pointer_only_behavior:
  pointer_only_sources_registered_in_source_manifest: true
  phase0_file_inventory_requires_source_inventory: true
  source_file_count_may_be_zero_without_inventory_generation: true
```

### Patch Suggestion: Script

Make Phase 0 consume pointer-only source paths from `manifests/source-manifest.json` when accessible.

Expected behavior:

```
source_file_count: count_files_under_pointer_sources
source_inventory_source: source-manifest-pointer-paths
```

Or, if that is intentionally out of scope, emit a clearer warning:

```
{
  "source_file_count": 0,
  "warnings": [
    "pointer_only sources are registered but phase0 did not traverse them because source-inventory.json is absent"
  ]
}
```

## Problem 6: Second Task Required “Run Commands Exactly In This Order,” But Execution Used Parallel Tool Calls

The deterministic after-Phase-1 instructions said:

```
Run these commands exactly in this order:
  1. lint
  2. audit
  3. status
  4. optional health
```

Codex launched lint, audit, status, and health in parallel.

### Impact

All commands succeeded and were read afterward, but strict order was not followed.

### Risk

If future commands depend on outputs from prior commands, parallelization could cause invalid or stale results.

### Process Patch Suggestion

For deterministic lifecycle steps that say “exactly in this order,” prohibit parallel execution:

```
execution_policy:
  ordered_commands:
    parallel_execution_allowed: false
    must_wait_for_each_command: true
```

### Agent Behavior Patch Suggestion

Codex should override its general preference for parallelization when the user says:

```
exactly in this order
```

and run sequentially.

## Problem 7: `previous_commit` Was Initially Missing Locally

The second task specified:

```
previous_commit: b0abb0fc373ad43aa0b24790a01021f8ac6a97cc
```

Initial `git log --oneline -5` did not show it.

A direct check initially failed due to PowerShell/Git quoting issue, then Codex fetched origin and rechecked successfully:

```
previous_commit_exists_after_fetch: true
```

### Impact

No final failure. Report was updated after fetch.

### Patch Suggestion: Instruction

Replace:

```
git log --oneline -5
```

with:

```
git fetch origin
git cat-file -e <sha>^{commit}
```

PowerShell-safe version:

```
git fetch origin
git cat-file -e "<sha>^{commit}"
if ($LASTEXITCODE -ne 0) { throw "previous commit missing" }
```

### Patch Suggestion: Report Template

Add:

```
previous_commit_check:
  method: git_cat_file_after_fetch
  exists: true | false
```

## Problem 8: `git cat-file` Check Had a Quoting/Powershell Issue

Codex attempted:

```
git cat-file -e b0abb0fc373ad43aa0b24790a01021f8ac6a97cc^{commit}
```

PowerShell/Git interaction produced an error:

```
error: unknown switch `n'
```

Later corrected with quoting:

```
git cat-file -e 'b0abb0fc373ad43aa0b24790a01021f8ac6a97cc^{commit}'
```

### Patch Suggestion

All PowerShell examples involving `^{commit}` should quote the full revision:

```
git cat-file -e "<sha>^{commit}"
```

## Problem 9: Final Response From First Run Included `commands_failed` Despite User Template Expecting `[]`

First run final response included:

```
commands_failed:
  - scaffold initial flag-order attempt
```

The requested final format had:

```
commands_failed: []
```

### Analysis

This was honest because the initial scaffold command failed. However, it deviated from the exact output expectation.

### Patch Suggestion

Update final format to distinguish lifecycle failures from corrected attempts:

```
commands_failed: []
corrected_command_attempts:
  - command: scaffold
    reason: global_flags_required_before_subcommand
    recovered: true
```

This avoids hiding a real issue while preserving PASS semantics.

## Problem 10: Previous Commit Provided By User Did Not Match Previously Reported Commit In This Chat

Earlier Codex reported first lifecycle commit as:

```
c9a4dcb92411d52390ed3adca3b9ecc785a115a0
```

Second task provided:

```
previous_commit: b0abb0fc373ad43aa0b24790a01021f8ac6a97cc
```

After fetch, `b0abb0...` existed, but it was not the same as the first commit reported in this chat.

### Risk

This could indicate:

- the user referenced a different upstream commit,
- history advanced outside this chat,
- another chat amended/replayed the same lifecycle,
- commit references are not tightly coupled to the actual run under audit.

### Patch Suggestion

Add ancestry/content validation:

```
git merge-base --is-ancestor b0abb0fc373ad43aa0b24790a01021f8ac6a97cc HEAD
git show --name-only --oneline b0abb0fc373ad43aa0b24790a01021f8ac6a97cc -- apex-meta/kb/apex-plan-sync-session-workflow-v2/
```

Report:

```
previous_commit:
  exists: true
  ancestor_of_head: true | false
  touches_kb_root: true | false
```

## Efficiency Assessment

### Efficient Parts

- Used script help to adapt to actual CLI instead of guessing.
- Read only requested source files for Phase 1, not all references.
- Avoided touching unrelated dirty worktree files.
- Captured deterministic logs into KB log folder.
- Committed narrowly scoped changes.
- Pushed after each committed lifecycle step.

### Inefficient / Risky Parts

- Initial failed scaffold attempt could have been avoided by checking top-level help before first command.
- Some commands were run in parallel despite “exactly in this order.”
- Phase 1 report creation was manual and verbose; could be templated.
- The first direct previous-commit check had a PowerShell quoting issue.
- The lifecycle instruction examples were inconsistent with script syntax, forcing runtime discovery.

### Efficiency Patch Suggestions

1. Add a standard preflight command:

```
python apex-meta/scripts/apex_kb.py --help
python apex-meta/scripts/apex_kb.py --kb-root <root> <subcommand> --help
```

2. Add a machine-readable command contract:

```
python apex-meta/scripts/apex_kb.py command-contract --json
```

Expected output:

```
{
  "global_flags_before_subcommand": true,
  "subcommands": {
    "source-intake": {
      "source_flag": "--source-path"
    },
    "hash": {
      "path_flag": "--path"
    }
  }
}
```

3. Add a script-generated Phase 1 template command:

```
python apex-meta/scripts/apex_kb.py --kb-root <root> --allow-write ingest-phase1-template
```

This could create required headings and gate blocks without doing semantic synthesis.

## Safety Assessment

### Safe Behaviors Observed

- Branch checked before execution.
- Script existence checked.
- KB root existence checked.
- Phase 1 files verified before deterministic after-Phase-1 checks.
- Unrelated changes left unstaged.
- No destructive Git commands used.
- No Phase 2 script commands run.
- Required operator phrase preserved.
- Pushes were explicit and successful.

### Safety Concerns

1. Dirty worktree existed throughout.
    
    - Safe because staging was scoped, but audit should note ambient risk.
2. Scaffold created Phase 2-shaped directories.
    
    - Could be mistaken for Phase 2 work.
3. Parallel execution of ordered checks.
    
    - Safe this time, but not generally safe.
4. Manual Phase 1 content generation can introduce non-deterministic wording.
    
    - Acceptable because task explicitly requested LLM Phase 1 analysis, but should be separated from deterministic phases.

## Concrete Script Patch Suggestions

### Patch A: Global Flag Flexibility

Allow global flags before or after subcommands.

```
def add_common_flags(parser):
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--allow-write", action="store_true")
    parser.add_argument("--strict", action="store_true")
```

Apply to main parser and subparsers, then resolve effective options.

### Patch B: Alias `--source` To `--source-path`

```
source_intake.add_argument(
    "--source-path",
    "--source",
    dest="source_path",
    required=True
)
```

### Patch C: Alias `--source` To `--path` For Hash

```
hash_parser.add_argument(
    "--path",
    "--source",
    dest="path",
    required=True
)
```

### Patch D: Add `scaffold --phase1-only`

```
scaffold --phase1-only
```

Should create:

```
create:
  - raw/
  - ingest-analysis/
  - manifests/
  - manifests/phase0/
  - log/
  - wiki/index.md

skip:
  - wiki/concepts/
  - wiki/entities/
  - wiki/summaries/
  - outputs/queries/
  - audit/resolved/
```

### Patch E: Emit Warning For Pointer-Only Phase 0 With No Inventory

If `source-manifest.json` has pointer-only sources and Phase 0 sees zero files:

```
{
  "warnings": [
    {
      "code": "pointer_only_sources_not_traversed",
      "message": "Pointer-only sources are registered, but phase0 did not traverse them because source inventory is absent."
    }
  ]
}
```

### Patch F: Add `verify-phase1` Command

```
python apex-meta/scripts/apex_kb.py --kb-root <root> --json verify-phase1
```

Expected checks:

```
required_files_present: true
operator_gate_present_in_all_batches: true
phase2_allowed_false: true
required_phrase_exact: approve ingest
wiki_semantic_pages_absent_or_empty: true
```

### Patch G: Add `deterministic-after-phase1` Command

Instead of manually running lint/audit/status/health and writing the report:

```
python apex-meta/scripts/apex_kb.py --kb-root <root> --json --allow-write deterministic-after-phase1
```

Expected writes:

```
log/lint-after-phase1.json
log/audit-after-phase1.json
log/status-after-phase1.json
log/health-after-phase1.json
log/deterministic-after-phase1-report.md
```

## Concrete Instruction Patch Suggestions

### Patch 1: Use Script-Accurate Command Syntax

Replace all examples with global flags before subcommand:

```
python apex-meta/scripts/apex_kb.py --kb-root <root> --json --allow-write scaffold
```

### Patch 2: Clarify Empty Scaffold Directories

Add:

```
empty_reserved_directories_created_by_scaffold_do_not_count_as_phase2:
  - wiki/summaries/
  - wiki/concepts/
  - wiki/entities/
  - outputs/queries/
  - audit/resolved/
```

### Patch 3: For Ordered Commands, Ban Parallel Execution

Add:

```
ordered_execution_required: true
parallel_execution_allowed: false
```

### Patch 4: Add PowerShell-Safe Commit Check

```
git fetch origin
git cat-file -e "<sha>^{commit}"
```

### Patch 5: Split Failed Attempts From Failed Lifecycle Commands

Use:

```
commands_failed: []
corrected_command_attempts:
  - command: scaffold
    failed_attempt_reason: global_flags_after_subcommand_not_supported
    recovered: true
```

### Patch 6: Require Ancestry Validation For Previous Commit

```
git merge-base --is-ancestor "<previous_sha>" HEAD
```

Report:

```
previous_commit:
  exists: true
  ancestor_of_head: true
```

## Overall Verdict

```
process_verdict: PASS_WITH_PROCESS_PATCHES_RECOMMENDED
safety_verdict: SAFE
determinism_verdict: MOSTLY_DETERMINISTIC
phase2_gate_verdict: PRESERVED
main_risks:
  - instruction/script CLI mismatch
  - scaffold creates empty Phase 2-shaped directories
  - ordered deterministic commands were run in parallel
  - pointer-only sources not traversed by phase0
  - previous commit validation needed fetch and better quoting
```

The lifecycle succeeded and was pushed. The process was generally safe because changes were scoped, Phase 2 was not run, and deterministic checks passed. The biggest improvements are to align handover commands with the actual CLI, make the script tolerate common aliases, clarify scaffold directory behavior, and enforce sequential execution when the operator says commands must run in order.