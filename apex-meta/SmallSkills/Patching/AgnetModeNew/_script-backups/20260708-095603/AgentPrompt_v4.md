# Terminal-Backed Agent / Codex Task — Build Apex KB v3 Repair Patch Pack

You are running inside a **real terminal Git worktree** for:

```yaml
repo: leela-spec/apexai-os-meta
branch: main
```

Your job is to create a validated Git-native patch pack for the landed Apex KB v3 repair plan.

Your job is **not** to apply the final repair to the repo target files.

Final repo state must contain **patch-pack artifacts only** under:

```text
apex-meta/patches/apex-kb-v3-repair/
```

Runtime/docs target files must be clean and unmodified at the end.

This task may be run by Agent Mode, Codex, or a local terminal agent **only if** the real repo checkout is already mounted.

---

## 0. Executor gate — no recovery search

Run exactly:

```bash
git rev-parse --show-toplevel
git rev-parse --is-inside-work-tree
git remote get-url origin
git branch --show-current
```

Required:

```yaml
inside_work_tree: true
origin_contains: "leela-spec/apexai-os-meta"
```

If any check fails, stop immediately:

```yaml
FINAL_REPORT:
  verdict: WRONG_EXECUTOR
  reason: "No live local Git checkout is mounted. Run this in a terminal-backed Agent/Codex/local repo checkout."
  patch_generation_started: false
  pushed: false
```

Do **not** search for the repo.  
Do **not** run `find`.  
Do **not** inspect `/home/oai/share`, `/workspace`, `/mnt/data`, or `/tmp`.  
Do **not** clone.  
Do **not** use GitHub/API snippets as baseline.  
Do **not** create a synthetic repo.

---

## 1. Sync main and dirty-tree policy

```bash
git checkout main
git pull --ff-only origin main
git status --porcelain
```

Dirty tree policy:

```yaml
block_if_dirty_overlaps:
  - "apex-meta/scripts/apex_kb.py"
  - "apex-meta/scripts/apex_kb_retrieval.py"
  - ".claude/skills/apex-kb/"
  - "apex-meta/patches/apex-kb-v3-repair/"
  - ".claude/skills/apex-kb2/"
  - "apex-meta/kb/*/wiki/"
  - "apex-meta/kb/*/ingest-analysis/"
allow_if_dirty_unrelated: true
requirement: "Report unrelated dirty files and leave them untouched."
```

If dirty files overlap blocked paths, stop with:

```yaml
FINAL_REPORT:
  verdict: FAIL
  failed_step: dirty_worktree
  dirty_files:
    - "<path>"
  patch_generation_started: false
  pushed: false
```

---

## 2. Binding source plan

Use this package as the only implementation authority:

```text
apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NextFinalization/apex-kb-v3-repair-patch-plan/
```

Read in this order:

```text
00-global-rules.md
01-read-verification-ledger.md
02-current-state-audit.md
03-target-file-map.md
04-feature-repair-index.md
05-agent-mode-patch-pack-builder-contract.md
06-validation-contract.md
07-codex-applier-contract.md
08-risk-and-rollback-policy.md
09-final-execution-order.md
targets/
manifest.json
```

If any required source-plan file is missing, stop:

```yaml
FINAL_REPORT:
  verdict: FAIL
  failed_step: source_plan_access
  missing_files:
    - "<path>"
  patch_generation_started: false
  pushed: false
```

Do not use:

```text
apex-meta/patches/apex-kb-v3-p0-p2-closure/*.patch
```

Those are invalid historical artifacts, not implementation authority.

---

## 3. Mission lock

Implement the landed repair plan exactly.

The repair is **targeted repair, not rollback**.

Preserve useful landed behavior:

```yaml
preserve:
  - source_payload_manifest core behavior
  - working --output-json support
  - working CLI flag normalization where real
  - useful status freshness split where real
```

Replace stub-class behavior:

```yaml
replace_stubs:
  - pointer_only_phase0
  - quality_coverage
  - query_eval
  - graph_process_flow
```

Repair partial/docs alignment:

```yaml
repair_partial:
  - status_freshness_split
  - cli_output_json regression coverage
  - retrieval_cli_output_json regression coverage
  - script_command_contract_alignment
  - kb_contract_alignment
  - acceptance_tests
  - phase2_value_contract_alignment
  - package_manifest_plan_ledger
```

Do not:

```yaml
must_not:
  - rollback 0c747db4 by default
  - accept PASS_WITH_WORKAROUNDS
  - accept marker checks as behavior proof
  - manually apply failed patches
  - use abbreviated hunk headers
  - rewrite existing KB wiki pages
  - touch .claude/skills/apex-kb2/
  - mutate Plan, Sync, Session, PreCap, FlowRecap, APSU, or personal orchestration state
```

---

## 4. Target-file rule

Use the source-plan target map.

Important: create **one Git-generated patch per repo target path**, not one patch per repair-area file.

Expected patch grouping:

```yaml
patch_groups:
  "001-apex-kb-py-repair.patch":
    target: "apex-meta/scripts/apex_kb.py"
    covers:
      - pointer_only_phase0
      - quality_coverage
      - query_eval
      - graph_process_flow
      - status_freshness_split
      - cli_output_json regression if needed

  "002-apex-kb-retrieval-py-repair.patch":
    target: "apex-meta/scripts/apex_kb_retrieval.py"
    covers:
      - retrieval_cli_output_json regression if needed

  "003-script-command-contract.patch":
    target: ".claude/skills/apex-kb/references/script-command-contract.md"

  "004-kb-contract.patch":
    target: ".claude/skills/apex-kb/references/kb-contract.md"

  "005-acceptance-tests.patch":
    target: ".claude/skills/apex-kb/references/acceptance-tests.md"

  "006-ingest-query-lint-audit-rules.patch":
    target: ".claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md"

  "007-package-manifest.patch":
    target: ".claude/skills/apex-kb/package-manifest.md"
```

Only create a patch if live inspection shows a change is needed.

If the plan requires another target file, add it and explain why in `000-manifest.md`.

---

## 5. Patch generation loop

For each patch group:

### A. Start clean

```bash
git checkout -- <target-file>
git status --porcelain -- <target-file>
```

Status must print nothing.

### B. Edit one target path only

Modify only `<target-file>`.

### C. Generate Git patch

```bash
mkdir -p apex-meta/patches/apex-kb-v3-repair/
git diff --no-ext-diff -- <target-file> > apex-meta/patches/apex-kb-v3-repair/<NNN-name>.patch
```

### D. Validate patch

```bash
test -s apex-meta/patches/apex-kb-v3-repair/<NNN-name>.patch
grep '^diff --git ' apex-meta/patches/apex-kb-v3-repair/<NNN-name>.patch
git checkout -- <target-file>
git apply --check apex-meta/patches/apex-kb-v3-repair/<NNN-name>.patch
git apply apex-meta/patches/apex-kb-v3-repair/<NNN-name>.patch
git diff --name-only
```

`git diff --name-only` may show only `<target-file>`.

### E. Revert target

```bash
git checkout -- <target-file>
git status --porcelain -- <target-file>
```

Status must print nothing.

---

## 6. Patch-pack metadata

Create these files:

```text
apex-meta/patches/apex-kb-v3-repair/000-manifest.md
apex-meta/patches/apex-kb-v3-repair/validation-report.md
apex-meta/patches/apex-kb-v3-repair/patch-plan-source-ledger.md
apex-meta/patches/apex-kb-v3-repair/999-codex-apply-handoff.md
```

`000-manifest.md` must include:

```yaml
source_plan_root: apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NextFinalization/apex-kb-v3-repair-patch-plan/
patch_pack_root: apex-meta/patches/apex-kb-v3-repair/
patch_order:
  - "<patch-file>"
patch_to_target:
  "<patch-file>": "<target-file>"
repair_area_coverage:
  pointer_only_phase0: "<patch-file-or-omitted>"
  quality_coverage: "<patch-file-or-omitted>"
  query_eval: "<patch-file-or-omitted>"
  graph_process_flow: "<patch-file-or-omitted>"
  status_freshness_split: "<patch-file-or-omitted>"
  cli_output_json: "<patch-file-or-omitted>"
  retrieval_cli_output_json: "<patch-file-or-omitted>"
  script_command_contract_alignment: "<patch-file-or-omitted>"
  kb_contract_alignment: "<patch-file-or-omitted>"
  acceptance_tests: "<patch-file-or-omitted>"
  phase2_value_contract_alignment: "<patch-file-or-omitted>"
  package_manifest_plan_ledger: "<patch-file-or-omitted>"
omitted_repairs:
  - repair: "<name>"
    reason: "<reason>"
```

`validation-report.md` must record:

```yaml
per_patch:
  - patch:
    target:
    repair_areas:
      - "<repair_area>"
    git_apply_check:
    single_file_scope:
cumulative:
  git_apply_check_all:
  git_apply_all:
  changed_file_scope:
  py_compile:
  behavior_checks:
final_builder_state:
  target_files_reverted:
  only_patch_pack_artifacts_changed:
```

`999-codex-apply-handoff.md` must contain deterministic apply instructions only:

```yaml
include:
  - repo and branch
  - patch pack root
  - patch order
  - git apply --check commands
  - git apply commands
  - py_compile commands
  - behavior checks from 06-validation-contract.md
  - changed-file scope check
  - commit and push steps
  - final report schema
exclude:
  - branch creation
  - PR creation
  - filesystem search
  - GitHub/API fallback
  - manual workaround path
```

---

## 7. Cumulative validation

From clean `main`:

```bash
git checkout main
git pull --ff-only origin main
git status --porcelain
```

Apply-check all patches in manifest order:

```bash
for p in apex-meta/patches/apex-kb-v3-repair/*.patch; do
  git apply --check "$p"
done
```

Apply all patches:

```bash
for p in apex-meta/patches/apex-kb-v3-repair/*.patch; do
  git apply "$p"
done
```

Verify changed-file scope:

```bash
git diff --name-only
```

Only target files named by `000-manifest.md` may appear.

Run static validation:

```bash
python -m py_compile apex-meta/scripts/apex_kb.py
python -m py_compile apex-meta/scripts/apex_kb_retrieval.py
python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/claude-skill-design --help
python apex-meta/scripts/apex_kb_retrieval.py --kb-root apex-meta/kb/claude-skill-design --help
```

Run behavior checks from:

```text
apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NextFinalization/apex-kb-v3-repair-patch-plan/06-validation-contract.md
```

Behavior checks must prove behavior, not markers.

Then revert all target files:

```bash
git checkout -- apex-meta/scripts/apex_kb.py apex-meta/scripts/apex_kb_retrieval.py .claude/skills/apex-kb/
```

Final changed files may be only under:

```text
apex-meta/patches/apex-kb-v3-repair/
```

---

## 8. Commit patch-pack artifacts only

```bash
git add apex-meta/patches/apex-kb-v3-repair/
git diff --cached --name-only
```

If any staged file is outside `apex-meta/patches/apex-kb-v3-repair/`, stop.

```bash
git commit -m "Add Apex KB v3 repair patch pack"
git push origin main
```

---

## 9. Final report

Return exactly:

```yaml
FINAL_REPORT:
  verdict: PASS | FAIL | WRONG_EXECUTOR
  repo: leela-spec/apexai-os-meta
  branch: main
  repair_plan_root: apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NextFinalization/apex-kb-v3-repair-patch-plan/
  patch_pack_root: apex-meta/patches/apex-kb-v3-repair/

  executor_gate:
    inside_work_tree: true | false
    origin_ok: true | false
    branch_at_start: "<branch-or-NA>"

  repair_area_coverage:
    pointer_only_phase0: PASS | OMITTED | FAIL
    quality_coverage: PASS | OMITTED | FAIL
    query_eval: PASS | OMITTED | FAIL
    graph_process_flow: PASS | OMITTED | FAIL
    status_freshness_split: PASS | OMITTED | FAIL
    cli_output_json: PASS | OMITTED | FAIL
    retrieval_cli_output_json: PASS | OMITTED | FAIL
    script_command_contract_alignment: PASS | OMITTED | FAIL
    kb_contract_alignment: PASS | OMITTED | FAIL
    acceptance_tests: PASS | OMITTED | FAIL
    phase2_value_contract_alignment: PASS | OMITTED | FAIL
    package_manifest_plan_ledger: PASS | OMITTED | FAIL

  patches_created:
    - patch_file: "<path>"
      target_file: "<path>"
      repair_areas:
        - "<repair_area>"
      git_apply_check: PASS | FAIL
      single_file_scope: PASS | FAIL

  omitted_repairs:
    - repair: "<name>"
      reason: "<reason>"

  cumulative_validation:
    git_apply_check_all: PASS | FAIL
    git_apply_all: PASS | FAIL
    changed_file_scope: PASS | FAIL
    py_compile: PASS | FAIL | NA
    behavior_checks: PASS | FAIL | NA

  final_builder_state:
    target_files_reverted: true | false
    only_patch_pack_artifacts_changed: true | false

  committed:
    status: true | false
    sha: "<sha-or-NA>"

  pushed:
    status: true | false

  blockers:
    - "<only if FAIL or WRONG_EXECUTOR>"
```