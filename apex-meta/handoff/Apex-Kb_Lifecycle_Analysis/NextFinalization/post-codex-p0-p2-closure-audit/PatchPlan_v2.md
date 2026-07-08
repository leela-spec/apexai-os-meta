FINAL_REPORT:  
verdict: PASS  
patch_plan_package_root: "apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NextFinalization/apex-kb-v3-repair-patch-plan/"  
files_created:  
- "00-global-rules.md"  
- "01-read-verification-ledger.md"  
- "02-current-state-audit.md"  
- "03-target-file-map.md"  
- "04-feature-repair-index.md"  
- "05-agent-mode-patch-pack-builder-contract.md"  
- "06-validation-contract.md"  
- "07-codex-applier-contract.md"  
- "08-risk-and-rollback-policy.md"  
- "09-final-execution-order.md"  
- "targets/001-apex-kb-py-pointer-only-phase0.md"  
- "targets/002-apex-kb-py-quality-coverage.md"  
- "targets/003-apex-kb-py-query-eval.md"  
- "targets/004-apex-kb-py-graph-process-flow.md"  
- "targets/005-apex-kb-py-status-freshness.md"  
- "targets/006-apex-kb-py-cli-output-json.md"  
- "targets/007-apex-kb-retrieval-cli-output-json.md"  
- "targets/008-script-command-contract.md"  
- "targets/009-kb-contract-doc-alignment.md"  
- "targets/010-acceptance-tests.md"  
- "targets/011-phase2-value-contract-alignment.md"  
- "targets/012-package-manifest-plan-ledger.md"  
- "manifest.json"  
batches:  
- batch: 1  
file_count: 12  
target_features:  
- "pointer_only_phase0"  
- "quality_coverage"  
- "query_eval"  
- "graph_process_flow"  
- "status_freshness_split"  
- "cli_output_json"  
- "retrieval_cli_output_json"  
- "script_command_contract_alignment"  
- "kb_contract_alignment"  
- "acceptance_tests"  
- "phase2_value_contract_alignment"  
- "package_manifest_plan_ledger"  
source_access:  
project_resources_read: true  
live_repo_read: true  
missing_sources: []  
highest_risk_repairs:  
- "graph_process_flow"  
- "pointer_only_phase0"  
- "quality_coverage"  
- "query_eval"  
ready_for_agent_mode_patch_pack_builder: true  
blocker: []

# FILE: `00-global-rules.md`

````markdown
# Apex KB v3 Repair Patch-Plan — Global Rules

## Scope

```yaml
package_id: apex-kb-v3-repair-patch-plan
mode: patch_plan_only
repo: leela-spec/apexai-os-meta
branch: main
canonical_package: .claude/skills/apex-kb/
runtime_scripts:
  lifecycle: apex-meta/scripts/apex_kb.py
  retrieval: apex-meta/scripts/apex_kb_retrieval.py
suspect_commit: 0c747db4
repair_policy: targeted_repair_not_default_revert
````

## Hard constraints

```yaml
must:
  - "Plan only; do not generate patch hunks."
  - "Repair behavior, not markers."
  - "Preserve useful landed behavior: --output-json, CLI compatibility where functional, source-payload-manifest core, useful status split."
  - "Treat apex-meta/patches/apex-kb-v3-p0-p2-closure/*.patch as invalid historical artifacts, not implementation authority."
  - "Use one Git-generated patch per target file in the later builder run."
  - "Validate every later patch with git apply --check individually and cumulatively."
  - "Keep final Agent Mode builder state to patch artifacts only."
must_not:
  - "Do not revert 0c747db4 by default."
  - "Do not manually apply failed patches."
  - "Do not accept PASS_WITH_WORKAROUNDS."
  - "Do not use marker checks as behavior proof."
  - "Do not touch apex-kb2."
  - "Do not rewrite existing KB wiki pages in this repair wave."
  - "Do not mutate Apex Plan, Sync, Session, PreCap, FlowRecap, APSU, or personal orchestration state."
```

## Batch rule

```yaml
batch_size_ceiling: 12
current_batch: 1
target_plan_count: 12
max_plan_file_bytes: 12288
```

````

# FILE: `01-read-verification-ledger.md`

```markdown
# Read Verification Ledger

## 1. Project-source gate

```yaml
source_access_checked: true
source_gate_result: PASS
mandatory_project_sources_readable:
  - "Apex_KB_Project_Resource_Index.machine-readable.yaml.md"
  - "Apex KB v3 Audit.txt"
  - "Apex KB v3 Failure Audit.txt"
  - "Apex KB v3 Patch Plan.txt"
  - "Apex Phase 2 Patch-Pack.txt"
  - "AgentModePatchGuide_v4.md"
  - "Apex KB Patch Pack.txt"
  - "Apex KB v3 Pre-Analysis.txt"
  - "Apex KB Update Plan.txt"
  - "Apex-KB_UpdatePlan.md"
  - "apex-kb-chat-drift-learning.okf.md"
  - "Apex KB Phase 2 Minimal Value Contract — MacroMeso Change Plan.md"
  - "Apex KB Phase 2 Repair.txt"
  - "codex-old-agent-kb-execution-process-audit.md"
  - "Apex KB Lifecycle Execution Audit.md"
missing_required_sources: []
````

## 2. Key source findings

```yaml
source_findings:
  - id: S01
    source: "Apex KB v3 Audit.txt"
    finding: "v3 is near-final but not closed; remaining blockers include CLI resilience, pointer_only Phase 0, quality/coverage, query eval, and freshness separation."
    citation: "turn2file17"
  - id: S02
    source: "Apex KB v3 Audit.txt"
    finding: "Commit 0c747db4 is suspect but repairable; patch pack and patch process are invalid, but useful implementation surfaces landed."
    citation: "turn2file18"
  - id: S03
    source: "Apex KB v3 Audit.txt"
    finding: "quality_report, cmd_query_eval, and process_graph_extract are stub-class surfaces."
    citation: "turn2file18"
  - id: S04
    source: "AgentModePatchGuide_v4.md"
    finding: "Agent Mode must build Git-native patch artifacts only from a live terminal Git worktree; patches must be generated by git diff and validated by git apply --check."
    citation: "turn3file3"
  - id: S05
    source: "Apex KB Phase 2 Minimal Value Contract — MacroMeso Change Plan.md"
    finding: "Phase 2 repair strengthens page value contract without a full lifecycle redesign."
    citation: "turn0file60"
  - id: S06
    source: "codex-old-agent-kb-execution-process-audit.md"
    finding: "Process failures included flag placement, pointer-only Phase 0 limitations, dirty-file policy friction, and shell portability."
    citation: "turn2file6"
```

## 3. Live repo gate

```yaml
live_repo_access_checked: true
live_repo_gate_result: PASS
repo: leela-spec/apexai-os-meta
default_branch: main
permissions_observed: admin_write_available
suspect_commit:
  sha: 0c747db41bc5028d815ae0321f76ace144244738
  in_main_history: true
  evidence: "GitHub commit fetch returned the suspect commit and message."
commits_after_suspect:
  count_observed: 11
  finding: "Later commits add handoff, prompt, audit, log, and process-learning artifacts; they do not repair the runtime target-file stubs."
```

## 4. Live files inspected

```yaml
target_files:
  - path: "apex-meta/scripts/apex_kb.py"
    read_status: read
    evidence:
      - "SOURCE_PAYLOAD_MANIFEST_PATH exists."
      - "normalize_global_flag_placement and --output-json exist."
      - "pointer_only resolved files are counted but not scanned into Phase 0 artifacts."
      - "quality_report returns empty maps/candidates."
      - "cmd_query_eval returns path and empty arrays only."
      - "process_graph_extract returns empty graph arrays only."
  - path: "apex-meta/scripts/apex_kb_retrieval.py"
    read_status: read
    evidence:
      - "normalize_global_flag_placement exists."
      - "--output-json write support exists."
      - "retrieval index behavior itself is outside this repair except status/docs validation."
  - path: ".claude/skills/apex-kb/references/script-command-contract.md"
    read_status: read
    evidence:
      - "Docs overclaim quality, query-eval, graph, and pointer_only behavior."

context_files:
  - ".claude/skills/apex-kb/SKILL.md"
  - ".claude/skills/apex-kb/package-manifest.md"
  - ".claude/skills/apex-kb/references/kb-contract.md"
  - ".claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md"
  - ".claude/skills/apex-kb/templates/wiki-page-templates.md"
  - ".claude/skills/apex-kb/references/acceptance-tests.md"

suspect_artifacts:
  - path: "apex-meta/patches/apex-kb-v3-p0-p2-closure/codex-apply-report.md"
    finding: "git_apply_check: FAIL; workarounds used."
  - path: "apex-meta/patches/apex-kb-v3-p0-p2-closure/PATCH_WORKAROUND_REPORT.md"
    finding: "All eight patch fragments had abbreviated hunk headers; manual equivalent edits were applied."
```

## 5. Verification notes

The live script currently includes source-payload manifest support and v3 lifecycle surfaces, so this plan does not reopen those decisions. The live script also proves the repair target: pointer-only files are resolved separately but not added into the Phase 0 scanned `files` list, while `quality_report`, `cmd_query_eval`, and `process_graph_extract` return empty structures rather than real deterministic results.

Important live evidence:

- `apex_kb.py` defines source-payload constants and Phase 2 value headings in the script header area.
    
- `cmd_phase0` builds artifacts from `iter_source_files(kb_root)` before resolving pointer-only files, then reports pointer-only fields afterward.
    
- `quality_report`, `cmd_query_eval`, and `process_graph_extract` are present but return empty maps, empty arrays, or empty edge categories.
    
- The workaround report says all eight patch fragments used abbreviated hunk headers and equivalent manual changes were applied.
    

````

# FILE: `02-current-state-audit.md`

```markdown
# Current State Audit

## 1. Executive finding

```yaml
current_state_verdict: REPAIR
reason:
  - "0c747db4 is in main history and landed some useful surfaces."
  - "The original patch pack is invalid because git apply check failed."
  - "Manual equivalent edits were applied."
  - "Several advertised features are currently stub-class or partial."
  - "Targeted repair is safer than default full revert."
do_not_revert_by_default: true
````

## 2. What to preserve

```yaml
preserve:
  cli_output_json:
    status: KEEP_REAL
    reason: "Both lifecycle and retrieval scripts have --output-json machinery and path-constrained writes."
  cli_flag_placement:
    status: REPAIR_PARTIAL
    reason: "normalize_global_flag_placement exists and is useful, but docs/parser behavior still needs command-level validation."
  source_payload_manifest:
    status: KEEP_REAL
    reason: "Source-payload manifest generation is implemented and should be smoke-tested, not redesigned."
  status_freshness_split:
    status: REPAIR_PARTIAL
    reason: "wiki_index_status and retrieval_index_status exist, but retrieval_index_status is only present/missing."
```

## 3. What to repair

```yaml
repair:
  pointer_only_phase0:
    failure_class: REPLACE_STUB
    live_evidence:
      - "cmd_phase0 scans sources/raw files first."
      - "resolve_pointer_only_text_files is called after artifact structures are already built."
      - "pointer_only_warning_count is hardcoded to 0."
      - "pointer_only_unresolved is hardcoded to empty."
    required_repair:
      - "Resolve accessible local text pointers before Phase 0 parse."
      - "Include resolved pointer-only files in Phase 0 scanning."
      - "Report unresolved pointers truthfully."

  quality_coverage:
    failure_class: REPLACE_STUB
    live_evidence:
      - "quality_report creates source_to_page_map and page_to_source_map with empty lists."
      - "phase2_repair_candidates and shell_page_candidates are always empty."
    required_repair:
      - "Compute source/page maps from manifest and wiki frontmatter source_refs."
      - "Detect missing source_refs and missing Phase 2 value sections."
      - "Detect deterministic shell page candidates."

  query_eval:
    failure_class: REPLACE_STUB
    live_evidence:
      - "cmd_query_eval returns path plus empty expected_minimal_pages and raw_source_needed."
      - "It does not read, initialize, write, or validate a pack."
    required_repair:
      - "Read existing query-eval pack."
      - "Initialize minimal pack only with --init and --allow-write."
      - "Validate entries deterministically."

  graph_process_flow:
    failure_class: REPLACE_STUB
    live_evidence:
      - "process_graph_extract returns empty edge_type, yaml_path_reference, and process_sequence arrays."
      - "cmd_graph does not write manifests/phase0 artifacts."
    required_repair:
      - "Extract Markdown links, wikilinks, repo path references, YAML path references, and process sequence markers."
      - "Write deterministic artifacts under manifests/phase0 when --allow-write is used."

  script_command_contract_alignment:
    failure_class: DOCS_ONLY_REPAIR
    live_evidence:
      - "script-command-contract.md claims behavior not currently implemented."
    required_repair:
      - "After script repair, document only implemented behavior."
      - "Label partial or experimental behavior explicitly."
```

## 4. Later commits after 0c747db4

```yaml
later_commit_assessment:
  compare_base: 0c747db4
  compare_head: main
  ahead_by: 11
  target_file_repairs_detected_after_0c747db4: false
  observed_later_file_classes:
    - "handoff/prompt artifacts"
    - "Agent Mode process learning"
    - "post-codex audit JSON logs"
    - "pycache artifacts"
  consequence: "The suspect target-file implementation remains the baseline for repair."
```

## 5. Suspect patch artifacts

```yaml
invalid_patch_artifacts:
  path: "apex-meta/patches/apex-kb-v3-p0-p2-closure/"
  status: "historical_invalid"
  reason:
    - "git_apply_check failed."
    - "abbreviated hunk headers were used."
    - "manual equivalent edits replaced patch application."
  future_use:
    allowed:
      - "forensic evidence"
      - "anti-pattern reference"
    forbidden:
      - "implementation authority"
      - "baseline patch source"
      - "copy-forward into repair pack"
```

## 6. Audit conclusion

The repair pack must be built from live target files on main, not from the failed patch files. It must replace stub behavior with deterministic implementations or explicitly downgrade unsupported docs. It must preserve existing real functionality.

````

# FILE: `03-target-file-map.md`

```markdown
# Target File Map

## 1. Batch map

```yaml
batch:
  id: 1
  file_count: 12
  max_target_plan_files: 12
  patch_pack_root_for_later_builder: apex-meta/patches/apex-kb-v3-repair/
````

## 2. Target plans

|target plan|target repo path|feature|action|
|---|---|---|---|
|`targets/001-apex-kb-py-pointer-only-phase0.md`|`apex-meta/scripts/apex_kb.py`|pointer_only_phase0|replace stub|
|`targets/002-apex-kb-py-quality-coverage.md`|`apex-meta/scripts/apex_kb.py`|quality_coverage|replace stub|
|`targets/003-apex-kb-py-query-eval.md`|`apex-meta/scripts/apex_kb.py`|query_eval|replace stub|
|`targets/004-apex-kb-py-graph-process-flow.md`|`apex-meta/scripts/apex_kb.py`|graph_process_flow|replace stub|
|`targets/005-apex-kb-py-status-freshness.md`|`apex-meta/scripts/apex_kb.py`|status_freshness_split|repair partial|
|`targets/006-apex-kb-py-cli-output-json.md`|`apex-meta/scripts/apex_kb.py`|cli_output_json|keep and regression-test|
|`targets/007-apex-kb-retrieval-cli-output-json.md`|`apex-meta/scripts/apex_kb_retrieval.py`|retrieval_cli_output_json|keep and regression-test|
|`targets/008-script-command-contract.md`|`.claude/skills/apex-kb/references/script-command-contract.md`|script_command_contract_alignment|docs repair|
|`targets/009-kb-contract-doc-alignment.md`|`.claude/skills/apex-kb/references/kb-contract.md`|kb_contract_alignment|docs alignment|
|`targets/010-acceptance-tests.md`|`.claude/skills/apex-kb/references/acceptance-tests.md`|acceptance_tests|add repair tests|
|`targets/011-phase2-value-contract-alignment.md`|`.claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md`|phase2_value_contract_alignment|rules alignment|
|`targets/012-package-manifest-plan-ledger.md`|`.claude/skills/apex-kb/package-manifest.md`|package_manifest_plan_ledger|manifest alignment|

## 3. Multi-feature single-file rule

`apex-meta/scripts/apex_kb.py` appears in multiple target plans because it owns multiple cohesive behavior repairs. The later patch-pack builder may either create one cumulative patch for `apex_kb.py` or one patch per cohesive script feature only if every patch applies cumulatively and all patch files are Git-generated. If the one-patch-per-target-file rule is interpreted strictly by the builder, merge targets 001–006 into a single script patch and keep the target-plan files as implementation subcontracts.

## 4. Forbidden targets

```yaml
forbidden_targets:
  - ".claude/skills/apex-kb2/**"
  - "apex-meta/kb/*/wiki/**"
  - "apex-meta/kb/*/ingest-analysis/**"
  - "apex-meta/patches/apex-kb-v3-p0-p2-closure/*.patch"
  - "Plan/Sync/Session/PreCap/FlowRecap/APSU/personal orchestration files"
```

````

# FILE: `04-feature-repair-index.md`

```markdown
# Feature Repair Index

| feature | status | target plan | evidence basis | repair decision |
|---|---|---|---|---|
| `cli_flag_placement` | REPAIR_PARTIAL | `targets/006`, `targets/007`, `targets/008` | Normalization exists, but must be regression-tested and docs must match actual parser behavior. | Preserve shim; validate before and after subcommand flags. |
| `output_json` | KEEP_REAL | `targets/006`, `targets/007`, `targets/010` | `maybe_write_output_json` exists in both scripts and constrains output path under KB root. | Regression-test with PowerShell-safe path output. |
| `pointer_only_phase0` | REPLACE_STUB | `targets/001` | Pointer-only files are resolved after Phase 0 artifacts are already built; unresolved/warnings are hardcoded. | Include safe resolved text files in scanning or report unresolved. |
| `status_freshness_split` | REPAIR_PARTIAL | `targets/005` | `wiki_index_status` exists; `retrieval_index_status` is present/missing only. | Add freshness comparison to retrieval index metadata if feasible. |
| `quality_coverage` | REPLACE_STUB | `targets/002` | Maps and candidate lists exist but are empty shells. | Compute source/page maps and deterministic repair candidates. |
| `query_eval` | REPLACE_STUB | `targets/003` | Command returns path and empty arrays; no read/init/validate behavior. | Implement deterministic pack read/init/schema validation. |
| `graph_process_flow` | REPLACE_STUB | `targets/004` | Extractor returns empty arrays and writes no artifacts. | Extract deterministic edge families and optionally write JSON artifacts. |
| `script_command_contract_alignment` | DOCS_ONLY_REPAIR | `targets/008` | Contract overclaims current behavior for quality/query-eval/graph/pointer-only. | Rewrite to match repaired behavior only. |
| `kb_contract_alignment` | DOCS_ONLY_REPAIR | `targets/009` | Contract is mostly valid; add/confirm pointer-only and derived-artifact boundaries as needed. | Minimal alignment only. |
| `phase2_value_contract_alignment` | DOCS_ONLY_REPAIR | `targets/011` | Existing value contract is largely correct; quality repair should align lint/reporting language. | Keep contract, align reporting language. |
| `acceptance_tests` | DOCS_ONLY_REPAIR | `targets/010` | Current tests lack explicit pointer-only, quality, query-eval, graph acceptance checks. | Add deterministic smoke checks. |
````

# FILE: `05-agent-mode-patch-pack-builder-contract.md`

````markdown
# Agent Mode Patch-Pack Builder Contract

## 1. Role

```yaml
agent_mode_role:
  role: "Git-native patch-pack builder"
  patch_pack_root: "apex-meta/patches/apex-kb-v3-repair/"
  branch: main
````

## 2. Must

```yaml
must:
  - "operate inside a real terminal Git worktree"
  - "use live main as source of truth"
  - "read target files from the worktree, not from connector reconstruction"
  - "create one Git-generated patch per target file or one cumulative Git-generated patch for apex_kb.py if required for apply stability"
  - "validate every patch with git apply --check"
  - "validate cumulative patch application"
  - "run py_compile on changed Python scripts during temporary cumulative application"
  - "run smoke behavior checks for repaired features during temporary cumulative application"
  - "revert target files after patch generation"
  - "leave final repo state with patch artifacts only"
```

## 3. Must not

```yaml
must_not:
  - "directly apply final target-file changes"
  - "manually apply failed patches"
  - "create synthetic repo files from API snippets"
  - "use abbreviated hunk headers"
  - "hand-edit hunk headers"
  - "self-report pass if git apply --check fails"
  - "use marker-only implementation"
  - "use the invalid apex-kb-v3-p0-p2-closure patch files as implementation source"
```

## 4. Preflight

```yaml
preflight_commands:
  - "git rev-parse --show-toplevel"
  - "git rev-parse --is-inside-work-tree"
  - "git remote get-url origin"
  - "git branch --show-current"
  - "git status --porcelain"
  - "git checkout main"
  - "git pull --ff-only origin main"

hard_stop_if:
  - "not a Git worktree"
  - "target files unreadable"
  - "source plan package unreadable"
  - "git unavailable"
```

## 5. Dirty tree policy

```yaml
dirty_tree_policy:
  block_if_dirty_overlaps:
    - "target files"
    - "apex-meta/patches/apex-kb-v3-repair/"
    - "forbidden paths"
  allow_if_dirty_unrelated: true
  requirement: "report unrelated dirty files and leave them untouched"
```

## 6. Per-target patch loop

```yaml
per_target_loop:
  - "git checkout -- <target-file>"
  - "verify target file clean"
  - "modify only that target file"
  - "git diff --no-ext-diff -- <target-file> > <patch-file>"
  - "test -s <patch-file>"
  - "verify exactly one diff --git header unless cumulative apex_kb.py patch is intentionally one target-file patch"
  - "git checkout -- <target-file>"
  - "git apply --check <patch-file>"
  - "git apply <patch-file>"
  - "verify only intended target file changed"
  - "run relevant smoke checks"
  - "git checkout -- <target-file>"
  - "verify target file clean"
```

## 7. Final artifact set

```yaml
required_artifacts:
  - "000-patch-manifest.md"
  - "NNN-*.patch"
  - "validation-report.md"
  - "999-codex-apply-handoff.md"
  - "patch-plan-source-ledger.md"
```

````

# FILE: `06-validation-contract.md`

```markdown
# Validation Contract

## 1. Patch validity

```yaml
patch_validity:
  must:
    - "every .patch has normal diff --git headers"
    - "every hunk has line-range headers"
    - "git apply --check passes individually"
    - "git apply --check passes cumulatively"
    - "no abbreviated hunk headers"
    - "no manual equivalent edits"
````

## 2. Static validation

```yaml
static_validation:
  commands:
    - "python -m py_compile apex-meta/scripts/apex_kb.py"
    - "python -m py_compile apex-meta/scripts/apex_kb_retrieval.py"
    - "python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/claude-skill-design --help"
    - "python apex-meta/scripts/apex_kb_retrieval.py --kb-root apex-meta/kb/claude-skill-design --help"
  required:
    - "help output includes phase0"
    - "help output includes quality"
    - "help output includes coverage"
    - "help output includes query-eval"
    - "help output includes graph or process-graph"
    - "docs mention only implemented behavior"
```

## 3. Behavioral validation

```yaml
behavioral_validation:
  pointer_only_phase0:
    - "create a test KB with source-manifest.json containing pointer_only source_path to a KB-local text file"
    - "run phase0 --allow-write --json"
    - "assert resolved pointer file contributes to heading/link/frontmatter artifacts"
    - "assert pointer_only_scanned_count equals resolved scanned files"
    - "assert unresolved pointer reports in pointer_only_unresolved"

  quality_coverage:
    - "create wiki pages with and without source_refs"
    - "assert source_to_page_map and page_to_source_map are non-empty when source_refs exist"
    - "assert pages_without_source_refs reports missing refs"
    - "assert pages_missing_phase2_value_sections reports missing required sections"
    - "assert phase2_repair_candidates and shell_page_candidates are deterministically populated"

  query_eval:
    - "run query-eval --init without --allow-write and assert planned write only"
    - "run query-eval --init --allow-write and assert outputs/queries/evals/query-eval-pack.json is created"
    - "run query-eval on existing pack and assert status, issue_count, expected_routes, expected_minimal_pages, raw_source_needed"

  graph_process_flow:
    - "create fixture Markdown with markdown links, wikilinks, repo path references, YAML path references, and sequence arrows"
    - "run graph --allow-write --json"
    - "assert deterministic JSON output contains edge categories"
    - "assert artifacts are written under manifests/phase0/"

  output_json:
    - "--output-json writes valid UTF-8 JSON inside kb_root"
    - "outside-kb-root output path is rejected"

  cli_flag_placement:
    - "global flags work before subcommand"
    - "supported global flags work after subcommand"
```

## 4. Final validation

```yaml
final_validation:
  - "git status limited to expected files"
  - "no target files modified in Agent Mode builder final state"
  - "no patch workaround report in new repair patch pack"
  - "no manual equivalent edits"
  - "final report classifies each feature"
  - "invalid old p0-p2 closure patch files remain historical only"
```

````

# FILE: `07-codex-applier-contract.md`

```markdown
# Codex Applier Contract

## 1. Role

```yaml
codex_role:
  role: "deterministic patch applier/verifier"
  branch: main
  patch_pack_root: "apex-meta/patches/apex-kb-v3-repair/"
````

## 2. Must

```yaml
must:
  - "work directly on main"
  - "apply the validated patch pack only"
  - "reject patch files that fail git apply --check"
  - "run py_compile on both scripts"
  - "run command help checks"
  - "run targeted smoke behavior checks for repaired features"
  - "verify changed-file scope"
  - "commit and push only after all validation passes"
```

## 3. Must not

```yaml
must_not:
  - "perform manual equivalent edits after failed patch apply"
  - "accept marker checks as behavior proof"
  - "push PASS_WITH_WORKAROUNDS"
  - "edit target files outside patch application"
  - "repair invalid patches in place and still claim validated-pack apply"
  - "open a PR unless explicitly requested"
```

## 4. Required command shape

```bash
git checkout main
git pull --ff-only origin main
git apply --check apex-meta/patches/apex-kb-v3-repair/*.patch
git apply apex-meta/patches/apex-kb-v3-repair/*.patch
python -m py_compile apex-meta/scripts/apex_kb.py
python -m py_compile apex-meta/scripts/apex_kb_retrieval.py
python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/claude-skill-design --help
python apex-meta/scripts/apex_kb_retrieval.py --kb-root apex-meta/kb/claude-skill-design --help
```

## 5. Final report requirements

```yaml
final_report_required_fields:
  - verdict
  - patch_pack_root
  - git_apply_check_all
  - py_compile_apex_kb
  - py_compile_retrieval
  - behavior_checks
  - changed_file_scope
  - commit_sha
  - pushed_to_origin_main
  - workarounds_used
```

`workarounds_used` must be `false` for PASS.

````

# FILE: `08-risk-and-rollback-policy.md`

```markdown
# Risk and Rollback Policy

## 1. Risk posture

```yaml
overall_risk: medium_high
recovery_mode: targeted_repair
do_not_revert_by_default: true
````

## 2. Highest-risk repairs

```yaml
highest_risk:
  graph_process_flow:
    risk: high
    reason:
      - "Correct extraction must include YAML/path/process/contract edges, not just Markdown links."
      - "Risk of creating noisy or misleading graph artifacts."
    mitigation:
      - "Keep deterministic and additive."
      - "Use simple Python stdlib extraction."
      - "Keep graph non-blocking."
      - "Write artifacts under manifests/phase0 only."

  pointer_only_phase0:
    risk: medium_high
    reason:
      - "Path resolution can accidentally escape KB root if not constrained."
      - "Repo-local pointers must be allowed safely without network fetch."
    mitigation:
      - "Allow only kb-root-relative or repo-local text files."
      - "Reject network URLs."
      - "Report unresolved paths instead of guessing."
      - "Never count a pointer file as scanned unless parsed."

  quality_coverage:
    risk: medium
    reason:
      - "May drift into subjective grading."
    mitigation:
      - "Use structural heuristics only."
      - "No LLM grading."
      - "No page_value_score."
      - "Report-only unless strict mode is explicitly selected."

  query_eval:
    risk: medium
    reason:
      - "Could become semantic grading."
    mitigation:
      - "Validate schema only."
      - "Do not judge answer quality."
      - "Do not run LLM evals."
```

## 3. Rollback policy

```yaml
rollback_policy:
  if_patch_pack_invalid:
    action: "reject patch pack before application"
    revert_needed: false
  if_codex_apply_fails_git_apply_check:
    action: "stop without manual edits"
    revert_needed: false
  if_static_validation_fails_after_apply:
    action: "git reset --hard HEAD before commit"
    report: "FAIL"
  if_behavior_validation_fails_after_apply:
    action: "git reset --hard HEAD before commit"
    report: "FAIL_WITH_BEHAVIOR_REGRESSION"
  if_bad_commit_pushed:
    preferred: "targeted repair follow-up"
    fallback: "git revert <bad-commit> only if runtime behavior is worse than pre-repair"
```

## 4. Revert threshold

```yaml
revert_only_if:
  - "repair corrupts source-payload manifest behavior"
  - "repair breaks scaffold/source-intake/phase0/index/lint/status baseline"
  - "repair creates writes outside kb_root"
  - "repair mutates non-Apex-KB systems"
  - "repair cannot be isolated by targeted follow-up"
```

````

# FILE: `09-final-execution-order.md`

```markdown
# Final Execution Order

## 1. Planning package order

```yaml
read_order:
  - "00-global-rules.md"
  - "01-read-verification-ledger.md"
  - "02-current-state-audit.md"
  - "03-target-file-map.md"
  - "04-feature-repair-index.md"
  - "05-agent-mode-patch-pack-builder-contract.md"
  - "06-validation-contract.md"
  - "07-codex-applier-contract.md"
  - "08-risk-and-rollback-policy.md"
````

## 2. Agent Mode builder execution order

```yaml
agent_mode_builder_order:
  - step: 1
    action: "repo preflight on live terminal Git worktree"
  - step: 2
    action: "read all target files from live main"
  - step: 3
    action: "repair apex-meta/scripts/apex_kb.py behaviors"
    features:
      - pointer_only_phase0
      - quality_coverage
      - query_eval
      - graph_process_flow
      - status_freshness_split
      - cli_output_json_regression
  - step: 4
    action: "repair apex-meta/scripts/apex_kb_retrieval.py only if output-json or flag placement validation fails"
  - step: 5
    action: "repair docs/contracts to match implemented behavior"
  - step: 6
    action: "add acceptance tests"
  - step: 7
    action: "validate patches individually and cumulatively"
  - step: 8
    action: "revert target files and leave patch artifacts only"
```

## 3. Codex applier execution order

```yaml
codex_applier_order:
  - step: 1
    action: "git checkout main && git pull --ff-only origin main"
  - step: 2
    action: "git apply --check repair patch pack"
  - step: 3
    action: "git apply repair patch pack"
  - step: 4
    action: "py_compile both scripts"
  - step: 5
    action: "run help checks"
  - step: 6
    action: "run targeted behavior fixture checks"
  - step: 7
    action: "verify docs match behavior"
  - step: 8
    action: "commit and push main only if all checks pass"
```

## 4. Feature order

```yaml
feature_order:
  1: pointer_only_phase0
  2: quality_coverage
  3: query_eval
  4: graph_process_flow
  5: status_freshness_split
  6: cli_output_json_regression
  7: retrieval_cli_output_json_regression
  8: docs_alignment
  9: acceptance_tests
```

````

# FILE: `targets/001-apex-kb-py-pointer-only-phase0.md`

```markdown
# Target Plan — 001 pointer-only-phase0

## 1. Target file

```text
apex-meta/scripts/apex_kb.py
````

## 2. Current verified behavior

```yaml
current_behavior:
  verified_from_live_repo: true
  source_files_read:
    - "Apex KB v3 Audit.txt"
    - "Apex KB v3 Failure Audit.txt"
    - "Apex KB v3 Patch Plan.txt"
    - "Apex KB Lifecycle Execution Audit.md"
    - "codex-old-agent-kb-execution-process-audit.md"
  live_repo_files_inspected:
    - "apex-meta/scripts/apex_kb.py"
    - ".claude/skills/apex-kb/references/kb-contract.md"
    - ".claude/skills/apex-kb/references/script-command-contract.md"
  evidence:
    - "cmd_phase0 builds files = iter_source_files(kb_root) and structures before pointer_only resolution."
    - "resolve_pointer_only_text_files returns string paths but those files are not added to the structures parsed for Phase 0 artifacts."
    - "pointer_only_warning_count is hardcoded to 0."
    - "pointer_only_unresolved is hardcoded to []."
```

## 3. Failure class

```yaml
failure_class:
  status: REPLACE_STUB
  reason: "The surface reports pointer_only fields but does not include resolved pointer-only files in Phase 0 artifact generation and does not report unresolved pointers truthfully."
  user_value_problem: "Pointer-only repo/local sources can be recorded in custody but then disappear from deterministic navigation, causing later LLM ingest to miss source material."
```

## 4. Required repair behavior

```yaml
required_behavior:
  must:
    - "detect pointer_only sources from source-manifest.json"
    - "support repo-local and kb-root-relative local text pointers"
    - "include accessible pointer-only text files in Phase 0 scanning or emit explicit unresolved status"
    - "avoid network fetches"
    - "report pointer_only_source_status with resolved/unresolved entries"
    - "report pointer_only_scanned_count accurately"
    - "report pointer_only_warning_count accurately"
    - "report pointer_only_unresolved accurately"
  must_not:
    - "hardcode warning_count: 0"
    - "hardcode unresolved: []"
    - "count resolved pointer files without scanning them"
    - "fetch network URLs"
    - "scan binary files"
  deterministic_only: true
  llm_owned: false
```

## 5. Implementation intent

Repair the `pointer_only_manifest_sources`, `resolve_pointer_only_text_files`, and `cmd_phase0` flow.

Implementation intent:

- Normalize manifest source storage mode lookup to support both `source_storage_mode` and legacy `storage_mode`.
    
- Read pointer path from `source_path`, `pointer`, or equivalent existing manifest field.
    
- Reject URLs and unsupported schemes as unresolved with a reason.
    
- Resolve relative pointers first against `kb_root`, then against repository root if the script can infer it safely from the current working tree or parent directories.
    
- Only allow files with text extensions already accepted by Phase 0.
    
- Produce structured status entries with `source_id`, `pointer`, `status`, `resolved_path`, and `reason`.
    
- Add resolved pointer files to the Phase 0 file list before `parse_markdown_structure`.
    
- Deduplicate files by resolved path so copied and pointer sources do not double-count.
    
- Count `pointer_only_scanned_count` from pointer files actually included in structures.
    
- Count `pointer_only_warning_count` from unresolved or unsupported pointer entries.
    
- Populate `pointer_only_unresolved` with unresolved status entries.
    

Do not change semantic ingest behavior. Do not create wiki pages. Do not perform network access.

## 6. Acceptance tests

```yaml
acceptance_tests:
  static:
    - "grep for pointer_only_warning_count and verify it is not hardcoded to 0."
    - "grep for pointer_only_unresolved and verify it is derived from status entries."
  behavioral:
    - "Create KB-local file raw/pointer-source.md and a source-manifest pointer_only entry pointing to it."
    - "Run phase0 --allow-write --json."
    - "Verify heading-map.json contains raw/pointer-source.md."
    - "Verify pointer_only_scanned_count is 1."
    - "Create one missing pointer_only entry and verify pointer_only_unresolved contains it."
  regression:
    - "Existing copied raw/ sources still scan normally."
    - "Phase 0 still writes only manifests/phase0 artifacts."
    - "No network URL is fetched."
```

## 7. Agent Mode patch-pack instructions

```yaml
agent_mode_builder_notes:
  patch_file_name: "001-apex-kb-py-pointer-only-phase0.patch"
  one_target_file_only: true
  validate_with:
    - "git apply --check apex-meta/patches/apex-kb-v3-repair/001-apex-kb-py-pointer-only-phase0.patch"
    - "python -m py_compile apex-meta/scripts/apex_kb.py"
  forbidden:
    - "manual equivalent edits"
    - "abbreviated hunk headers"
    - "marker-only implementation"
```

## 8. Codex applier notes

```yaml
codex_notes:
  apply_order: 1
  post_apply_checks:
    - "python -m py_compile apex-meta/scripts/apex_kb.py"
    - "run pointer_only Phase 0 fixture"
```

````

# FILE: `targets/002-apex-kb-py-quality-coverage.md`

```markdown
# Target Plan — 002 quality-coverage

## 1. Target file

```text
apex-meta/scripts/apex_kb.py
````

## 2. Current verified behavior

```yaml
current_behavior:
  verified_from_live_repo: true
  source_files_read:
    - "Apex KB v3 Pre-Analysis.txt"
    - "Apex KB v3 Audit.txt"
    - "Apex KB v3 Failure Audit.txt"
    - "Apex KB Phase 2 Minimal Value Contract — MacroMeso Change Plan.md"
  live_repo_files_inspected:
    - "apex-meta/scripts/apex_kb.py"
    - ".claude/skills/apex-kb/templates/wiki-page-templates.md"
    - ".claude/skills/apex-kb/references/kb-contract.md"
  evidence:
    - "quality_report returns source_to_page_map and page_to_source_map, but every list is empty."
    - "phase2_repair_candidates is always empty."
    - "shell_page_candidates is always empty."
    - "Current lint checks missing Phase 2 value headings, but quality command does not expose coverage meaningfully."
```

## 3. Failure class

```yaml
failure_class:
  status: REPLACE_STUB
  reason: "The quality command exposes expected keys but performs no real source/page coverage or shell-page analysis."
  user_value_problem: "Apex KB can pass structural checks while still producing low-value pages with weak source routing."
```

## 4. Required repair behavior

```yaml
required_behavior:
  must:
    - "compute source_to_page_map from wiki page frontmatter source_refs and/or structured source pointers"
    - "compute page_to_source_map"
    - "report pages_without_source_refs"
    - "report pages_missing_phase2_value_sections"
    - "report phase2_repair_candidates"
    - "detect shell/low-value pages using minimal structural heuristics"
    - "remain deterministic and non-semantic"
  must_not:
    - "return only empty maps"
    - "perform LLM grading"
    - "create a subjective page_value_score"
    - "hard fail by default"
  deterministic_only: true
  llm_owned: false
```

## 5. Implementation intent

Repair `quality_report(kb_root)` and `cmd_quality`.

Implementation intent:

- Load `source-manifest.json`.
    
- Build canonical source identifiers from `source_id`, `id`, `source_path`, and pointer fields.
    
- Iterate `wiki_pages(kb_root)`.
    
- Parse frontmatter and body.
    
- Extract `source_refs` from frontmatter:
    
    - list of strings
        
    - list of objects with `source_id`, `source_path`, `source_pointer`
        
    - scalar fallback
        
- Build `page_to_source_map` as page path -> list of source identifiers/pointers.
    
- Build `source_to_page_map` as manifest source -> pages that reference it.
    
- Add source IDs found in pages but not manifest under `unmanifested_source_refs`.
    
- Add manifest sources not used by any page under `manifest_sources_without_pages`.
    
- Add pages with no usable source refs under `pages_without_source_refs`.
    
- Detect missing Phase 2 value sections using `PHASE2_VALUE_HEADINGS`.
    
- Detect shell page candidates with structural heuristics:
    
    - missing source refs
        
    - low body density after frontmatter
        
    - no Key Claims section
        
    - no Macro/Meso/Micro section
        
    - only YAML blocks and minimal narrative
        
- Populate `phase2_repair_candidates` when summary/concept/entity pages miss required value headings or source routing.
    
- Keep `--strict` behavior optional and deterministic; strict can return fail status if candidates exist, but default should report only.
    

Do not score semantic quality. Do not rewrite pages.

## 6. Acceptance tests

```yaml
acceptance_tests:
  static:
    - "quality_report must populate maps from parsed wiki page source_refs."
    - "phase2_repair_candidates must be derived from actual page checks."
  behavioral:
    - "Create one page with source_refs and one page without source_refs."
    - "Run quality --json."
    - "Verify page_to_source_map includes the referenced source."
    - "Verify source_to_page_map maps the source to the page."
    - "Verify pages_without_source_refs includes the unreferenced page."
    - "Verify pages_missing_phase2_value_sections reports missing headings."
  regression:
    - "quality command remains read-only."
    - "coverage alias returns the same structure."
    - "No LLM calls, network calls, or outside-kb writes occur."
```

## 7. Agent Mode patch-pack instructions

```yaml
agent_mode_builder_notes:
  patch_file_name: "002-apex-kb-py-quality-coverage.patch"
  one_target_file_only: true
  validate_with:
    - "git apply --check apex-meta/patches/apex-kb-v3-repair/002-apex-kb-py-quality-coverage.patch"
    - "python -m py_compile apex-meta/scripts/apex_kb.py"
  forbidden:
    - "manual equivalent edits"
    - "abbreviated hunk headers"
    - "marker-only implementation"
```

## 8. Codex applier notes

```yaml
codex_notes:
  apply_order: 2
  post_apply_checks:
    - "python apex-meta/scripts/apex_kb.py --kb-root <fixture-kb> quality --json"
    - "python apex-meta/scripts/apex_kb.py --kb-root <fixture-kb> coverage --json"
```

````

# FILE: `targets/003-apex-kb-py-query-eval.md`

```markdown
# Target Plan — 003 query-eval

## 1. Target file

```text
apex-meta/scripts/apex_kb.py
````

## 2. Current verified behavior

```yaml
current_behavior:
  verified_from_live_repo: true
  source_files_read:
    - "Apex KB v3 Audit.txt"
    - "Apex KB v3 Failure Audit.txt"
    - "Apex KB v3 Patch Plan.txt"
    - "DR_Apex KB QueryRetrieval Integration_Final Patch Pack.md"
  live_repo_files_inspected:
    - "apex-meta/scripts/apex_kb.py"
    - ".claude/skills/apex-kb/references/script-command-contract.md"
  evidence:
    - "query_eval_pack_path returns outputs/queries/evals/query-eval-pack.json."
    - "cmd_query_eval returns a path plus expected_minimal_pages: [] and raw_source_needed: []."
    - "It does not read an existing pack."
    - "It does not initialize a pack."
    - "It does not validate pack schema."
```

## 3. Failure class

```yaml
failure_class:
  status: REPLACE_STUB
  reason: "The command only returns a path and empty arrays while docs claim read/init/validate behavior."
  user_value_problem: "Apex KB cannot evaluate query-routing coverage deterministically, so retrieval usefulness remains untested."
```

## 4. Required repair behavior

```yaml
required_behavior:
  must:
    - "read existing outputs/queries/evals/query-eval-pack.json if present"
    - "initialize a minimal valid pack when --init and --allow-write are provided"
    - "validate schema deterministically"
    - "report expected_routes, expected_minimal_pages, raw_source_needed"
    - "avoid semantic LLM grading"
  must_not:
    - "only return a path"
    - "hardcode empty arrays without reading the pack"
    - "judge answer quality semantically"
  deterministic_only: true
  llm_owned: false
```

## 5. Implementation intent

Repair `cmd_query_eval` and related parser flags.

Implementation intent:

- Keep pack path at `outputs/queries/evals/query-eval-pack.json`.
    
- Add parser support for:
    
    - `--init`
        
    - `--json`
        
    - `--allow-write` via normalized global flag
        
- Define minimal pack schema:
    
    - `schema: apex.query_eval_pack.v1`
        
    - `kb_slug`
        
    - `queries`
        
    - each query has `query`, `expected_routes`, `expected_minimal_pages`, `raw_source_needed`
        
- If pack exists:
    
    - read JSON
        
    - validate object structure
        
    - validate every query entry
        
    - return `status`, `issue_count`, `issues`, `query_count`, `expected_routes`, `expected_minimal_pages`, `raw_source_needed`
        
- If pack missing and `--init` without effective write:
    
    - return `status: planned`
        
    - include planned write path
        
    - do not write
        
- If pack missing and `--init --allow-write`:
    
    - create parent directory
        
    - write minimal valid pack
        
    - return `status: initialized`
        
- If pack missing and no `--init`:
    
    - return `status: missing`
        
    - do not fail unless strict is later added.
        
- No LLM grading, no query execution, no web/network access.
    

## 6. Acceptance tests

```yaml
acceptance_tests:
  static:
    - "cmd_query_eval must read or initialize query-eval-pack.json."
    - "result must include status and issue_count."
  behavioral:
    - "Run query-eval --init without --allow-write; verify no file created and planned status returned."
    - "Run query-eval --init --allow-write; verify valid JSON file created."
    - "Run query-eval on valid pack; verify issue_count 0."
    - "Run query-eval on invalid pack; verify deterministic issues."
  regression:
    - "No LLM grading occurs."
    - "outputs are valid JSON with --output-json."
```

## 7. Agent Mode patch-pack instructions

```yaml
agent_mode_builder_notes:
  patch_file_name: "003-apex-kb-py-query-eval.patch"
  one_target_file_only: true
  validate_with:
    - "git apply --check apex-meta/patches/apex-kb-v3-repair/003-apex-kb-py-query-eval.patch"
    - "python -m py_compile apex-meta/scripts/apex_kb.py"
  forbidden:
    - "manual equivalent edits"
    - "abbreviated hunk headers"
    - "marker-only implementation"
```

## 8. Codex applier notes

```yaml
codex_notes:
  apply_order: 3
  post_apply_checks:
    - "python apex-meta/scripts/apex_kb.py --kb-root <fixture-kb> query-eval --init --json"
    - "python apex-meta/scripts/apex_kb.py --kb-root <fixture-kb> --allow-write query-eval --init --json"
    - "python apex-meta/scripts/apex_kb.py --kb-root <fixture-kb> query-eval --json"
```

````

# FILE: `targets/004-apex-kb-py-graph-process-flow.md`

```markdown
# Target Plan — 004 graph-process-flow

## 1. Target file

```text
apex-meta/scripts/apex_kb.py
````

## 2. Current verified behavior

```yaml
current_behavior:
  verified_from_live_repo: true
  source_files_read:
    - "Apex KB v3 Audit.txt"
    - "Apex KB v3 Failure Audit.txt"
    - "process-flow-graph-audit.md"
    - "graph-summary.md"
    - "link-graph.sample.json"
    - "Apex Phase 0 Corpus Intelligence Implementation Decision.md"
  live_repo_files_inspected:
    - "apex-meta/scripts/apex_kb.py"
    - ".claude/skills/apex-kb/references/script-command-contract.md"
  evidence:
    - "process_graph_extract returns edge_type: [], yaml_path_reference: [], process_sequence: []."
    - "cmd_graph wraps the empty result."
    - "No artifacts are written under manifests/phase0."
    - "Docs claim graph artifacts and multiple edge types."
```

## 3. Failure class

```yaml
failure_class:
  status: REPLACE_STUB
  reason: "The command exists but extracts no graph/process-flow information and writes no artifacts."
  user_value_problem: "Apex KB loses deterministic navigation value for process and file-reference relationships."
```

## 4. Required repair behavior

```yaml
required_behavior:
  must:
    - "extract deterministic graph/process-flow edges from markdown links, wikilinks, explicit repo path references, YAML path references, and process sequence markers"
    - "write or plan artifacts under manifests/phase0/ if --allow-write is used"
    - "produce deterministic JSON output"
    - "avoid Obsidian dependency"
    - "avoid Node/remark dependency for V1"
  must_not:
    - "return empty arrays only"
    - "pretend a pure Markdown-link graph is sufficient"
    - "crawl the entire repo outside the KB root"
    - "perform semantic graph inference"
  deterministic_only: true
  llm_owned: false
```

## 5. Implementation intent

Repair `process_graph_extract` and `cmd_graph`.

Implementation intent:

- Iterate KB-local text files only:
    
    - `raw/`
        
    - `sources/` if present
        
    - `ingest-analysis/`
        
    - `wiki/`
        
    - `kb-schema.md`
        
    - `README.md`
        
    - exclude `derived/`, `outputs/`, binary files, and large generated logs unless explicitly safe.
        
- Extract edge records with stable fields:
    
    - `source_path`
        
    - `target`
        
    - `edge_type`
        
    - `line`
        
    - `raw`
        
    - `confidence: deterministic`
        
- Edge families:
    
    - `markdown_link`
        
    - `wikilink`
        
    - `repo_path_reference`
        
    - `yaml_path_reference`
        
    - `process_sequence`
        
- Markdown links and wikilinks may reuse existing regex logic.
    
- Repo path references should detect Apex repo path-like strings such as `.claude/...`, `apex-meta/...`, `wiki/...`, `raw/...`, `manifests/...`.
    
- YAML path references should detect lines where key names contain `path`, `file`, `root`, `source`, `target`, or `output`, and values look path-like.
    
- Process sequence markers should detect arrows like `A -> B`, `A → B`, ordered stage labels, and explicit `hands_off_to`/`depends_on`-style fields where deterministic.
    
- Deduplicate edges deterministically.
    
- Return:
    
    - `edge_count`
        
    - `edges_by_type`
        
    - `artifacts`
        
    - `deterministic_only`
        
- With `--allow-write`, write:
    
    - `manifests/phase0/process-flow-graph.json`
        
    - optionally `manifests/phase0/process-flow-graph-summary.md`
        
- Without write, report planned artifacts only.
    

Do not require Obsidian, Node, remark, network, or LLM calls.

## 6. Acceptance tests

```yaml
acceptance_tests:
  static:
    - "process_graph_extract must not return only hardcoded empty arrays."
    - "cmd_graph must plan or write manifests/phase0 artifacts."
  behavioral:
    - "Create fixture file containing a Markdown link, wikilink, repo path reference, YAML path reference, and A -> B sequence."
    - "Run graph --json."
    - "Verify edge_count > 0."
    - "Verify edges_by_type includes markdown_link, wikilink, repo_path_reference, yaml_path_reference, and process_sequence."
    - "Run graph --allow-write --json and verify process-flow-graph.json exists under manifests/phase0."
  regression:
    - "No network fetch."
    - "No outside-kb crawl."
    - "No graph command hard failure for empty KB; it should return zero edges truthfully."
```

## 7. Agent Mode patch-pack instructions

```yaml
agent_mode_builder_notes:
  patch_file_name: "004-apex-kb-py-graph-process-flow.patch"
  one_target_file_only: true
  validate_with:
    - "git apply --check apex-meta/patches/apex-kb-v3-repair/004-apex-kb-py-graph-process-flow.patch"
    - "python -m py_compile apex-meta/scripts/apex_kb.py"
  forbidden:
    - "manual equivalent edits"
    - "abbreviated hunk headers"
    - "marker-only implementation"
```

## 8. Codex applier notes

```yaml
codex_notes:
  apply_order: 4
  post_apply_checks:
    - "python apex-meta/scripts/apex_kb.py --kb-root <fixture-kb> graph --json"
    - "python apex-meta/scripts/apex_kb.py --kb-root <fixture-kb> graph --allow-write --json"
```

````

# FILE: `targets/005-apex-kb-py-status-freshness.md`

```markdown
# Target Plan — 005 status-freshness

## 1. Target file

```text
apex-meta/scripts/apex_kb.py
````

## 2. Current verified behavior

```yaml
current_behavior:
  verified_from_live_repo: true
  source_files_read:
    - "Apex KB v3 Audit.txt"
    - "Apex KB v3 Patch Plan.txt"
    - "codex-old-agent-kb-execution-process-audit.md"
  live_repo_files_inspected:
    - "apex-meta/scripts/apex_kb.py"
    - "apex-meta/scripts/apex_kb_retrieval.py"
    - ".claude/skills/apex-kb/references/script-command-contract.md"
  evidence:
    - "cmd_status returns wiki_index_status and retrieval_index_status."
    - "retrieval_index_status only returns present or missing based on derived/search/index-meta.json."
    - "It does not compare retrieval metadata to current wiki pages."
```

## 3. Failure class

```yaml
failure_class:
  status: REPAIR_PARTIAL
  reason: "The split exists and is useful, but retrieval freshness is only presence detection."
  user_value_problem: "Operators can mistake a present retrieval index for a fresh retrieval index."
```

## 4. Required repair behavior

```yaml
required_behavior:
  must:
    - "preserve wiki_index_status"
    - "preserve retrieval_index_status"
    - "report retrieval index missing, fresh, stale, or unknown"
    - "avoid importing or shelling into retrieval script if a simple metadata check is sufficient"
    - "remain read-only"
  must_not:
    - "collapse wiki and retrieval freshness into one status field"
    - "claim fresh when only metadata is present"
  deterministic_only: true
  llm_owned: false
```

## 5. Implementation intent

Repair `retrieval_index_status(kb_root)`.

Implementation intent:

- Keep `wiki_index_status` as `stale_index_status(kb_root)`.
    
- For retrieval:
    
    - If `derived/search/index-meta.json` is missing, return `missing`.
        
    - If metadata cannot be read, return `unknown` or `unreadable`.
        
    - If metadata includes indexed wiki file hashes, compare them to current wiki page hashes.
        
    - If any current page hash differs, any indexed page is missing, or any current wiki page is absent from metadata, return `stale`.
        
    - If metadata shape is older and cannot prove freshness, return `present_unknown_freshness` or `unknown` instead of `fresh`.
        
- Do not run `apex_kb_retrieval.py` from inside `apex_kb.py`.
    
- Do not write.
    

## 6. Acceptance tests

```yaml
acceptance_tests:
  static:
    - "retrieval_index_status must not return present merely because index-meta.json exists."
  behavioral:
    - "No index-meta.json -> retrieval_index_status: missing."
    - "Unreadable/legacy metadata -> unknown or present_unknown_freshness."
    - "Fresh metadata matching wiki hashes -> fresh."
    - "Modify a wiki page after metadata -> stale."
  regression:
    - "status command remains read-only."
    - "source_payload_manifest_status remains unchanged."
```

## 7. Agent Mode patch-pack instructions

```yaml
agent_mode_builder_notes:
  patch_file_name: "005-apex-kb-py-status-freshness.patch"
  one_target_file_only: true
  validate_with:
    - "git apply --check apex-meta/patches/apex-kb-v3-repair/005-apex-kb-py-status-freshness.patch"
    - "python -m py_compile apex-meta/scripts/apex_kb.py"
  forbidden:
    - "manual equivalent edits"
    - "abbreviated hunk headers"
    - "marker-only implementation"
```

## 8. Codex applier notes

```yaml
codex_notes:
  apply_order: 5
  post_apply_checks:
    - "python apex-meta/scripts/apex_kb.py --kb-root <fixture-kb> status --json"
```

````

# FILE: `targets/006-apex-kb-py-cli-output-json.md`

```markdown
# Target Plan — 006 cli-output-json

## 1. Target file

```text
apex-meta/scripts/apex_kb.py
````

## 2. Current verified behavior

```yaml
current_behavior:
  verified_from_live_repo: true
  source_files_read:
    - "Apex KB v3 Audit.txt"
    - "codex-old-agent-kb-execution-process-audit.md"
    - "AgentModePatchGuide_v4.md"
  live_repo_files_inspected:
    - "apex-meta/scripts/apex_kb.py"
    - ".claude/skills/apex-kb/references/script-command-contract.md"
  evidence:
    - "normalize_global_flag_placement exists and moves selected post-subcommand global flags before the subcommand."
    - "maybe_write_output_json exists and writes under kb_root."
    - "Parser has --output-json as global flag."
```

## 3. Failure class

```yaml
failure_class:
  status: KEEP_REAL
  reason: "The feature is real enough to preserve, but it needs regression tests because it came from the suspect workaround commit."
  user_value_problem: "PowerShell-safe JSON output and flexible flag placement prevent repeat execution friction."
```

## 4. Required repair behavior

```yaml
required_behavior:
  must:
    - "preserve --output-json support"
    - "preserve path safety under kb_root"
    - "preserve global flag normalization where functional"
    - "ensure post-subcommand placement works for documented global flags"
    - "produce valid UTF-8 JSON"
  must_not:
    - "weaken path safety"
    - "allow output-json outside kb_root"
    - "rewrite the entire parser"
  deterministic_only: true
  llm_owned: false
```

## 5. Implementation intent

Do not redesign the parser. Validate and minimally harden the existing shim.

Implementation intent:

- Keep `normalize_global_flag_placement`.
    
- Confirm command set includes every lifecycle helper subcommand.
    
- Confirm global bool flags include `--json`, `--dry-run`, `--allow-write`, `--strict`.
    
- Confirm value flags include `--output-json`.
    
- Confirm parser-level `--output-json` remains a global option.
    
- Confirm `maybe_write_output_json` handles relative paths under KB root and rejects outside paths through `ensure_inside`.
    
- If any repaired commands add subcommand-specific flags, ensure normalization does not steal legitimate command-local flags.
    
- Add or update acceptance tests in target 010 rather than adding marker-only logic.
    

## 6. Acceptance tests

```yaml
acceptance_tests:
  static:
    - "normalize_global_flag_placement includes all current commands."
    - "maybe_write_output_json calls ensure_inside."
  behavioral:
    - "status --json works with --json before subcommand."
    - "status --json works with --json after subcommand."
    - "status --output-json log/status.json writes valid JSON."
    - "outside-kb-root --output-json path is rejected."
  regression:
    - "source-payload-manifest still supports --allow-write before and after subcommand."
```

## 7. Agent Mode patch-pack instructions

```yaml
agent_mode_builder_notes:
  patch_file_name: "006-apex-kb-py-cli-output-json.patch"
  one_target_file_only: true
  validate_with:
    - "git apply --check apex-meta/patches/apex-kb-v3-repair/006-apex-kb-py-cli-output-json.patch"
    - "python -m py_compile apex-meta/scripts/apex_kb.py"
  forbidden:
    - "manual equivalent edits"
    - "abbreviated hunk headers"
    - "marker-only implementation"
```

## 8. Codex applier notes

```yaml
codex_notes:
  apply_order: 6
  post_apply_checks:
    - "python apex-meta/scripts/apex_kb.py --kb-root <fixture-kb> status --output-json log/status.json"
    - "python - <<'PY' parse the JSON file and assert command == status PY"
```

````

# FILE: `targets/007-apex-kb-retrieval-cli-output-json.md`

```markdown
# Target Plan — 007 retrieval-cli-output-json

## 1. Target file

```text
apex-meta/scripts/apex_kb_retrieval.py
````

## 2. Current verified behavior

```yaml
current_behavior:
  verified_from_live_repo: true
  source_files_read:
    - "Apex KB v3 Audit.txt"
    - "DR_Apex KB QueryRetrieval Integration_Final Patch Pack.md"
    - "codex-old-agent-kb-execution-process-audit.md"
  live_repo_files_inspected:
    - "apex-meta/scripts/apex_kb_retrieval.py"
    - ".claude/skills/apex-kb/references/script-command-contract.md"
  evidence:
    - "normalize_global_flag_placement exists in retrieval script."
    - "maybe_write_output_json exists and writes JSON under kb_root."
    - "Script policy restricts writes to derived/search and outputs/queries."
```

## 3. Failure class

```yaml
failure_class:
  status: KEEP_REAL
  reason: "Retrieval CLI output-json and flag normalization are real enough to preserve and regression-test."
  user_value_problem: "Retrieval postflight should produce parseable UTF-8 JSON without PowerShell redirection problems."
```

## 4. Required repair behavior

```yaml
required_behavior:
  must:
    - "preserve --output-json support"
    - "preserve path safety under kb_root"
    - "preserve retrieval command flag normalization"
    - "write valid JSON for health, stale, query, export, build-index, and clear-index where applicable"
  must_not:
    - "patch retrieval ranking semantics in this repair wave"
    - "weaken derived-path restrictions"
    - "allow output outside kb_root"
  deterministic_only: true
  llm_owned: false
```

## 5. Implementation intent

This target is primarily regression validation. Patch only if live validation shows defects.

Implementation intent:

- Keep `normalize_global_flag_placement` in retrieval script.
    
- Confirm command set includes `health`, `build-index`, `stale`, `query`, `export`, `clear-index`.
    
- Confirm value flag normalization handles `--output-json <path>`.
    
- Confirm `maybe_write_output_json` resolves relative paths under KB root and enforces `ensure_inside`.
    
- Do not change ranking, indexing, chunking, FTS5, query-packet semantics, or clear-index confirmation behavior unless needed to keep output-json safe.
    

## 6. Acceptance tests

```yaml
acceptance_tests:
  static:
    - "normalize_global_flag_placement includes all retrieval commands."
    - "maybe_write_output_json calls ensure_inside."
  behavioral:
    - "health --output-json log/retrieval-health.json writes valid JSON."
    - "stale --output-json log/retrieval-stale.json writes valid JSON."
    - "post-subcommand --json works for health and stale."
  regression:
    - "build-index still writes only under derived/search."
    - "query --save still writes only under outputs/queries."
```

## 7. Agent Mode patch-pack instructions

```yaml
agent_mode_builder_notes:
  patch_file_name: "007-apex-kb-retrieval-cli-output-json.patch"
  one_target_file_only: true
  validate_with:
    - "git apply --check apex-meta/patches/apex-kb-v3-repair/007-apex-kb-retrieval-cli-output-json.patch"
    - "python -m py_compile apex-meta/scripts/apex_kb_retrieval.py"
  forbidden:
    - "manual equivalent edits"
    - "abbreviated hunk headers"
    - "marker-only implementation"
```

## 8. Codex applier notes

```yaml
codex_notes:
  apply_order: 7
  post_apply_checks:
    - "python apex-meta/scripts/apex_kb_retrieval.py --kb-root <fixture-kb> health --output-json log/retrieval-health.json"
    - "python apex-meta/scripts/apex_kb_retrieval.py --kb-root <fixture-kb> stale --json"
```

````

# FILE: `targets/008-script-command-contract.md`

```markdown
# Target Plan — 008 script-command-contract

## 1. Target file

```text
.claude/skills/apex-kb/references/script-command-contract.md
````

## 2. Current verified behavior

```yaml
current_behavior:
  verified_from_live_repo: true
  source_files_read:
    - "Apex KB v3 Audit.txt"
    - "Apex KB v3 Failure Audit.txt"
    - "AgentModePatchGuide_v4.md"
  live_repo_files_inspected:
    - ".claude/skills/apex-kb/references/script-command-contract.md"
    - "apex-meta/scripts/apex_kb.py"
    - "apex-meta/scripts/apex_kb_retrieval.py"
  evidence:
    - "Contract claims quality/coverage computes maps and candidates."
    - "Contract claims query-eval validates or initializes a pack."
    - "Contract claims graph generates deterministic artifacts under manifests/phase0."
    - "Contract claims pointer_only Phase 0 resolves repo-local pointers and reports unresolved/warnings."
    - "Live code does not yet implement those claims fully."
```

## 3. Failure class

```yaml
failure_class:
  status: DOCS_ONLY_REPAIR
  reason: "The contract overclaims behavior that is currently partial or stub-class."
  user_value_problem: "Future agents and Codex prompts trust docs that do not match implementation, recreating PASS_WITH_WORKAROUNDS risk."
```

## 4. Required repair behavior

```yaml
required_behavior:
  must:
    - "script-command-contract.md must describe only implemented behavior"
    - "any experimental or partial command must be labeled partial or planned"
    - "PowerShell-safe --output-json examples must match parser behavior"
    - "global flag placement docs must match actual parser behavior"
  must_not:
    - "claim graph artifacts are generated if graph command only returns data"
    - "claim query-eval initializes packs if it does not"
    - "claim quality computes maps if maps remain empty"
    - "claim pointer-only scanned files if they are only counted"
  deterministic_only: false
  llm_owned: false
```

## 5. Implementation intent

Patch the contract after script behavior is repaired.

Implementation intent:

- Keep the shared policy and command tables.
    
- Update `v3 closure additions` so each command reflects implemented behavior after targets 001–007.
    
- If the builder fails to implement any script behavior, label that behavior `partial` or `planned`, not complete.
    
- Add exact examples:
    
    - before-subcommand global flags
        
    - after-subcommand global flags only where supported
        
    - `--output-json` writing inside KB root
        
- State that old p0-p2 closure patches are historical invalid artifacts and not command authority only if this belongs in contract; otherwise keep that in patch-pack manifest.
    
- Do not introduce a new lifecycle model.
    
- Do not claim behavior proven only by marker grep.
    

## 6. Acceptance tests

```yaml
acceptance_tests:
  static:
    - "No unsupported claim remains for quality/coverage."
    - "No unsupported claim remains for query-eval init/validate."
    - "No unsupported claim remains for graph artifact writing."
    - "No unsupported claim remains for pointer-only scanning."
  behavioral:
    - "Each documented command has a matching parser command."
    - "Each documented --output-json example executes in smoke tests."
  regression:
    - "Docs keep Python standard-library/no-network/no-shell-out policy."
    - "Docs keep writes-inside-kb-root policy."
```

## 7. Agent Mode patch-pack instructions

```yaml
agent_mode_builder_notes:
  patch_file_name: "008-script-command-contract.patch"
  one_target_file_only: true
  validate_with:
    - "git apply --check apex-meta/patches/apex-kb-v3-repair/008-script-command-contract.patch"
  forbidden:
    - "manual equivalent edits"
    - "abbreviated hunk headers"
    - "marker-only documentation"
```

## 8. Codex applier notes

```yaml
codex_notes:
  apply_order: 8
  post_apply_checks:
    - "grep documented command names and verify parser has matching subcommands"
    - "grep for unsupported overclaim phrases"
```

````

# FILE: `targets/009-kb-contract-doc-alignment.md`

```markdown
# Target Plan — 009 kb-contract-doc-alignment

## 1. Target file

```text
.claude/skills/apex-kb/references/kb-contract.md
````

## 2. Current verified behavior

```yaml
current_behavior:
  verified_from_live_repo: true
  source_files_read:
    - "Apex KB Phase 2 Minimal Value Contract — MacroMeso Change Plan.md"
    - "Apex-KB_UpdatePlan.md"
    - "Apex KB v3 Audit.txt"
  live_repo_files_inspected:
    - ".claude/skills/apex-kb/references/kb-contract.md"
    - ".claude/skills/apex-kb/SKILL.md"
    - "apex-meta/scripts/apex_kb.py"
  evidence:
    - "kb-contract.md already defines canonical versus derived paths."
    - "source-payload-manifest is included as canonical."
    - "Phase 2 page value contract is included and mostly aligned."
    - "Source custody says pointer_only requires source_path/source_hash/source_storage_mode, but live pointer_only may have no hash with no_hash_reason."
```

## 3. Failure class

```yaml
failure_class:
  status: DOCS_ONLY_REPAIR
  reason: "The contract is largely valid but may need minimal alignment with repaired pointer-only and payload-manifest behavior."
  user_value_problem: "Source custody rules must not force impossible hashes for pointer-only local paths when no_hash_reason is the correct durable record."
```

## 4. Required repair behavior

```yaml
required_behavior:
  must:
    - "preserve canonical/derived split"
    - "preserve source-payload-manifest role"
    - "align pointer_only source fields with actual manifest behavior"
    - "state that pointer_only Phase 0 scans only safe local text pointers or reports unresolved"
    - "keep no external BagIt dependency rule"
  must_not:
    - "reopen source-payload manifest architecture"
    - "weaken source custody"
    - "turn source-payload-manifest into replacement for source-manifest.json"
  deterministic_only: false
  llm_owned: false
```

## 5. Implementation intent

Patch only the source custody section if needed.

Implementation intent:

- Keep existing data root, canonical/derived, root shape, page contract, and boundary contract.
    
- In `source_storage_modes.pointer_only`, allow:
    
    - `source_path`
        
    - `source_storage_mode`
        
    - `source_hash` when available
        
    - `no_hash_reason` when not hashable
        
- Add a concise line that Phase 0 may use safe resolved pointer-only local text files for deterministic navigation, and must report unresolved pointers.
    
- Do not add new schema bureaucracy.
    

## 6. Acceptance tests

```yaml
acceptance_tests:
  static:
    - "pointer_only contract mentions source_hash when available or no_hash_reason when unavailable."
    - "contract says source-payload-manifest does not replace source-manifest.json."
  behavioral:
    - "N/A documentation alignment only."
  regression:
    - "canonical/derived paths remain unchanged."
    - "boundary contract remains unchanged."
```

## 7. Agent Mode patch-pack instructions

```yaml
agent_mode_builder_notes:
  patch_file_name: "009-kb-contract-doc-alignment.patch"
  one_target_file_only: true
  validate_with:
    - "git apply --check apex-meta/patches/apex-kb-v3-repair/009-kb-contract-doc-alignment.patch"
  forbidden:
    - "manual equivalent edits"
    - "abbreviated hunk headers"
    - "broad lifecycle rewrite"
```

## 8. Codex applier notes

```yaml
codex_notes:
  apply_order: 9
  post_apply_checks:
    - "grep source-payload-manifest references"
    - "grep pointer_only source_storage_modes"
```

````

# FILE: `targets/010-acceptance-tests.md`

```markdown
# Target Plan — 010 acceptance-tests

## 1. Target file

```text
.claude/skills/apex-kb/references/acceptance-tests.md
````

## 2. Current verified behavior

```yaml
current_behavior:
  verified_from_live_repo: true
  source_files_read:
    - "Apex KB v3 Audit.txt"
    - "Apex KB v3 Failure Audit.txt"
    - "AgentModePatchGuide_v4.md"
    - "Apex KB Lifecycle Execution Audit.md"
  live_repo_files_inspected:
    - ".claude/skills/apex-kb/references/acceptance-tests.md"
    - "apex-meta/scripts/apex_kb.py"
    - "apex-meta/scripts/apex_kb_retrieval.py"
  evidence:
    - "Acceptance tests cover scaffold, source intake, source-payload manifest, Phase 0, gate, wiki/index/retrieval, lint/audit."
    - "Acceptance tests do not yet explicitly validate repaired pointer-only Phase 0."
    - "Acceptance tests do not yet explicitly validate quality maps/candidates."
    - "Acceptance tests do not yet explicitly validate query-eval init/read/schema."
    - "Acceptance tests do not yet explicitly validate graph/process-flow extraction."
```

## 3. Failure class

```yaml
failure_class:
  status: DOCS_ONLY_REPAIR
  reason: "Acceptance tests do not yet prevent stub-class surfaces from passing."
  user_value_problem: "Marker-only or empty-output implementations can pass unless behavior fixtures are required."
```

## 4. Required repair behavior

```yaml
required_behavior:
  must:
    - "add deterministic acceptance checks for pointer_only Phase 0"
    - "add deterministic acceptance checks for quality/coverage maps"
    - "add deterministic acceptance checks for shell page candidates"
    - "add deterministic acceptance checks for query-eval --init"
    - "add deterministic acceptance checks for graph/process-flow extraction"
    - "add --output-json checks"
  must_not:
    - "replace compile and behavior checks with grep-only checks"
    - "require external dependencies"
    - "require network access"
  deterministic_only: true
  llm_owned: false
```

## 5. Implementation intent

Append a v3 repair acceptance section.

Implementation intent:

- Add fixture setup commands that create a small KB with:
    
    - one copied raw note
        
    - one pointer-only local text source
        
    - one missing pointer-only source
        
    - one good wiki concept page with source_refs and Phase 2 value headings
        
    - one shell page missing source_refs/value headings
        
    - one file with link/wikilink/path/YAML/sequence graph cues
        
- Add commands:
    
    - `phase0 --allow-write --json`
        
    - `quality --json`
        
    - `coverage --json`
        
    - `query-eval --init` dry-run
        
    - `query-eval --init --allow-write`
        
    - `graph --allow-write --json`
        
    - `status --output-json log/status.json`
        
    - retrieval `health --output-json log/retrieval-health.json`
        
- Add pass criteria checking behavior, not only markers.
    
- Keep examples shell-neutral where possible; include PowerShell-safe and Git Bash variants only if concise.
    

## 6. Acceptance tests

```yaml
acceptance_tests:
  static:
    - "File includes pointer_only Phase 0 repair fixture."
    - "File includes quality/coverage repair fixture."
    - "File includes query-eval repair fixture."
    - "File includes graph/process-flow repair fixture."
  behavioral:
    - "Commands are runnable from repo root."
    - "Pass criteria assert non-empty or accurately unresolved outputs where expected."
  regression:
    - "Existing scaffold/source-intake/retrieval tests remain."
    - "No dependency beyond Python stdlib."
```

## 7. Agent Mode patch-pack instructions

```yaml
agent_mode_builder_notes:
  patch_file_name: "010-acceptance-tests.patch"
  one_target_file_only: true
  validate_with:
    - "git apply --check apex-meta/patches/apex-kb-v3-repair/010-acceptance-tests.patch"
  forbidden:
    - "manual equivalent edits"
    - "abbreviated hunk headers"
    - "grep-only acceptance criteria"
```

## 8. Codex applier notes

```yaml
codex_notes:
  apply_order: 10
  post_apply_checks:
    - "read acceptance tests and run the new v3 repair fixture subset"
```

````

# FILE: `targets/011-phase2-value-contract-alignment.md`

```markdown
# Target Plan — 011 phase2-value-contract-alignment

## 1. Target file

```text
.claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md
````

## 2. Current verified behavior

```yaml
current_behavior:
  verified_from_live_repo: true
  source_files_read:
    - "Apex KB Phase 2 Minimal Value Contract — MacroMeso Change Plan.md"
    - "Apex KB Phase 2 Repair.txt"
    - "Apex KB v3 Pre-Analysis.txt"
    - "Apex KB v3 Audit.txt"
  live_repo_files_inspected:
    - ".claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md"
    - ".claude/skills/apex-kb/templates/wiki-page-templates.md"
    - ".claude/skills/apex-kb/references/kb-contract.md"
  evidence:
    - "Rules already define Phase 2 page value sections."
    - "Lint rules mention stale retrieval index, but current status/quality behavior needs clearer alignment."
    - "Query rules mention index-first retrieval, but query-eval pack behavior is not described."
```

## 3. Failure class

```yaml
failure_class:
  status: DOCS_ONLY_REPAIR
  reason: "Rules are mostly valid but should align with repaired quality/coverage and query-eval behavior."
  user_value_problem: "Future agents need one operational rule page that explains how quality, query-eval, and lint/reporting interact without turning them into semantic grading."
```

## 4. Required repair behavior

```yaml
required_behavior:
  must:
    - "preserve Phase 2 value contract"
    - "define quality/coverage as deterministic structural reporting"
    - "define query-eval as deterministic route/schema pack validation, not LLM grading"
    - "define graph/process-flow as deterministic Phase 0 navigation artifact"
    - "distinguish report-only findings from blocking lint failures"
  must_not:
    - "weaken source grounding"
    - "add page_value_score"
    - "require fixed source count"
    - "make graph extraction a semantic inference task"
  deterministic_only: false
  llm_owned: false
```

## 5. Implementation intent

Add a concise v3 repair subsection.

Implementation intent:

- Under Query rules, add query-eval pack rule:
    
    - queries define expected routes/pages/raw-source-needed
        
    - script validates schema only
        
    - no answer grading
        
- Under Lint rules or new Quality rules, describe:
    
    - `quality` and `coverage` report source/page maps
        
    - pages missing source refs
        
    - pages missing Phase 2 value sections
        
    - repair candidates
        
    - shell candidates
        
    - report-only by default
        
- Under Phase 0, mention graph/process-flow artifacts if implemented:
    
    - extracted deterministically
        
    - written under `manifests/phase0`
        
    - no Obsidian/Node dependency
        
- Keep current Phase 1/Phase 2 boundaries.
    

## 6. Acceptance tests

```yaml
acceptance_tests:
  static:
    - "Rules explicitly say quality/coverage is deterministic and non-semantic."
    - "Rules explicitly say query-eval is not LLM grading."
    - "Rules explicitly say graph/process-flow is deterministic."
  behavioral:
    - "N/A documentation alignment only."
  regression:
    - "Phase 0 must_not_create list remains."
    - "Query remains read-only for Plan/Sync/Session."
```

## 7. Agent Mode patch-pack instructions

```yaml
agent_mode_builder_notes:
  patch_file_name: "011-phase2-value-contract-alignment.patch"
  one_target_file_only: true
  validate_with:
    - "git apply --check apex-meta/patches/apex-kb-v3-repair/011-phase2-value-contract-alignment.patch"
  forbidden:
    - "manual equivalent edits"
    - "abbreviated hunk headers"
    - "new semantic grading system"
```

## 8. Codex applier notes

```yaml
codex_notes:
  apply_order: 11
  post_apply_checks:
    - "grep for query-eval non-grading rule"
    - "grep for quality/coverage deterministic reporting rule"
```

````

# FILE: `targets/012-package-manifest-plan-ledger.md`

```markdown
# Target Plan — 012 package-manifest-plan-ledger

## 1. Target file

```text
.claude/skills/apex-kb/package-manifest.md
````

## 2. Current verified behavior

```yaml
current_behavior:
  verified_from_live_repo: true
  source_files_read:
    - "Apex KB v3 Audit.txt"
    - "Apex KB v3 Patch Plan.txt"
    - "AgentModePatchGuide_v4.md"
  live_repo_files_inspected:
    - ".claude/skills/apex-kb/package-manifest.md"
    - ".claude/skills/apex-kb/SKILL.md"
    - ".claude/skills/apex-kb/references/script-command-contract.md"
  evidence:
    - "Package manifest lists package path, script paths, runtime policy, inventory, canonical paths, derived paths, and scope exclusions."
    - "It does not need broad repair."
    - "It may need minor alignment if new or repaired docs are added."
```

## 3. Failure class

```yaml
failure_class:
  status: DOCS_ONLY_REPAIR
  reason: "The manifest is mostly correct; update only if the repair pack changes package file inventory or adds new reference/example files."
  user_value_problem: "Package manifests are used for future navigation and should not go stale after repair."
```

## 4. Required repair behavior

```yaml
required_behavior:
  must:
    - "preserve package_name apex-kb"
    - "preserve package_path .claude/skills/apex-kb/"
    - "preserve runtime script paths"
    - "ensure repaired reference files remain listed"
    - "ensure canonical/derived path lists remain accurate"
  must_not:
    - "rename package"
    - "touch apex-kb2"
    - "add patch-plan files as runtime package files"
    - "claim the skill folder is executable by itself"
  deterministic_only: false
  llm_owned: false
```

## 5. Implementation intent

Patch only if necessary.

Implementation intent:

- If target files remain the existing package files, leave package manifest unchanged.
    
- If builder adds any new package reference file, add it to Inventory.
    
- Do not list `apex-meta/handoff/.../apex-kb-v3-repair-patch-plan/` as a package runtime file.
    
- Do not list `apex-meta/patches/apex-kb-v3-repair/` as a package runtime file; it is patch artifact history.
    
- Keep executability note.
    

## 6. Acceptance tests

```yaml
acceptance_tests:
  static:
    - "package_name remains apex-kb."
    - "script paths remain apex-meta/scripts/apex_kb.py and apex-meta/scripts/apex_kb_retrieval.py."
    - "canonical and derived paths match SKILL.md and kb-contract.md."
  behavioral:
    - "N/A documentation alignment only."
  regression:
    - "No apex-kb2 references introduced."
    - "No patch-pack artifact path listed as runtime package file."
```

## 7. Agent Mode patch-pack instructions

```yaml
agent_mode_builder_notes:
  patch_file_name: "012-package-manifest-plan-ledger.patch"
  one_target_file_only: true
  validate_with:
    - "git apply --check apex-meta/patches/apex-kb-v3-repair/012-package-manifest-plan-ledger.patch"
  forbidden:
    - "manual equivalent edits"
    - "abbreviated hunk headers"
    - "package rename"
```

## 8. Codex applier notes

```yaml
codex_notes:
  apply_order: 12
  post_apply_checks:
    - "grep package_name"
    - "grep script_paths"
    - "grep canonical_paths"
```

````

# FILE: `manifest.json`

```json
{
  "package_id": "apex-kb-v3-repair-patch-plan",
  "version": "0.1",
  "created_for_repo": "leela-spec/apexai-os-meta",
  "branch": "main",
  "suspect_commit": "0c747db4",
  "mode": "patch_plan_only",
  "package_root": "apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NextFinalization/apex-kb-v3-repair-patch-plan/",
  "patch_pack_root_for_later_builder": "apex-meta/patches/apex-kb-v3-repair/",
  "max_plan_file_bytes": 12288,
  "batch_size_ceiling": 12,
  "global_rules_file": "00-global-rules.md",
  "files": [
    {
      "path": "00-global-rules.md",
      "target_repo_path": null,
      "feature": "global_rules",
      "status": "PLAN_ONLY",
      "batch": 0,
      "depends_on": [],
      "byte_estimate": 1800,
      "source_evidence": [
        "S01",
        "S02",
        "S04"
      ]
    },
    {
      "path": "01-read-verification-ledger.md",
      "target_repo_path": null,
      "feature": "read_verification",
      "status": "PLAN_ONLY",
      "batch": 0,
      "depends_on": [],
      "byte_estimate": 4300,
      "source_evidence": [
        "S01",
        "S02",
        "S03",
        "S04",
        "S05",
        "S06"
      ]
    },
    {
      "path": "02-current-state-audit.md",
      "target_repo_path": null,
      "feature": "current_state_audit",
      "status": "PLAN_ONLY",
      "batch": 0,
      "depends_on": [
        "01-read-verification-ledger.md"
      ],
      "byte_estimate": 3600,
      "source_evidence": [
        "S01",
        "S02",
        "S03"
      ]
    },
    {
      "path": "03-target-file-map.md",
      "target_repo_path": null,
      "feature": "target_file_map",
      "status": "PLAN_ONLY",
      "batch": 0,
      "depends_on": [
        "02-current-state-audit.md"
      ],
      "byte_estimate": 2600,
      "source_evidence": [
        "S02",
        "S04"
      ]
    },
    {
      "path": "04-feature-repair-index.md",
      "target_repo_path": null,
      "feature": "feature_repair_index",
      "status": "PLAN_ONLY",
      "batch": 0,
      "depends_on": [
        "02-current-state-audit.md"
      ],
      "byte_estimate": 2300,
      "source_evidence": [
        "S01",
        "S03"
      ]
    },
    {
      "path": "05-agent-mode-patch-pack-builder-contract.md",
      "target_repo_path": null,
      "feature": "agent_mode_builder_contract",
      "status": "PLAN_ONLY",
      "batch": 0,
      "depends_on": [
        "00-global-rules.md"
      ],
      "byte_estimate": 3200,
      "source_evidence": [
        "S04"
      ]
    },
    {
      "path": "06-validation-contract.md",
      "target_repo_path": null,
      "feature": "validation_contract",
      "status": "PLAN_ONLY",
      "batch": 0,
      "depends_on": [
        "04-feature-repair-index.md"
      ],
      "byte_estimate": 3300,
      "source_evidence": [
        "S03",
        "S04"
      ]
    },
    {
      "path": "07-codex-applier-contract.md",
      "target_repo_path": null,
      "feature": "codex_applier_contract",
      "status": "PLAN_ONLY",
      "batch": 0,
      "depends_on": [
        "06-validation-contract.md"
      ],
      "byte_estimate": 2200,
      "source_evidence": [
        "S04",
        "S06"
      ]
    },
    {
      "path": "08-risk-and-rollback-policy.md",
      "target_repo_path": null,
      "feature": "risk_rollback",
      "status": "PLAN_ONLY",
      "batch": 0,
      "depends_on": [
        "02-current-state-audit.md"
      ],
      "byte_estimate": 2600,
      "source_evidence": [
        "S02",
        "S03"
      ]
    },
    {
      "path": "09-final-execution-order.md",
      "target_repo_path": null,
      "feature": "execution_order",
      "status": "PLAN_ONLY",
      "batch": 0,
      "depends_on": [
        "03-target-file-map.md",
        "06-validation-contract.md"
      ],
      "byte_estimate": 1800,
      "source_evidence": [
        "S04"
      ]
    },
    {
      "path": "targets/001-apex-kb-py-pointer-only-phase0.md",
      "target_repo_path": "apex-meta/scripts/apex_kb.py",
      "feature": "pointer_only_phase0",
      "status": "REPLACE_STUB",
      "batch": 1,
      "depends_on": [],
      "byte_estimate": 4700,
      "source_evidence": [
        "S01",
        "S02",
        "S03",
        "S06"
      ]
    },
    {
      "path": "targets/002-apex-kb-py-quality-coverage.md",
      "target_repo_path": "apex-meta/scripts/apex_kb.py",
      "feature": "quality_coverage",
      "status": "REPLACE_STUB",
      "batch": 1,
      "depends_on": [],
      "byte_estimate": 4600,
      "source_evidence": [
        "S01",
        "S03",
        "S05"
      ]
    },
    {
      "path": "targets/003-apex-kb-py-query-eval.md",
      "target_repo_path": "apex-meta/scripts/apex_kb.py",
      "feature": "query_eval",
      "status": "REPLACE_STUB",
      "batch": 1,
      "depends_on": [],
      "byte_estimate": 4100,
      "source_evidence": [
        "S01",
        "S03"
      ]
    },
    {
      "path": "targets/004-apex-kb-py-graph-process-flow.md",
      "target_repo_path": "apex-meta/scripts/apex_kb.py",
      "feature": "graph_process_flow",
      "status": "REPLACE_STUB",
      "batch": 1,
      "depends_on": [],
      "byte_estimate": 5000,
      "source_evidence": [
        "S01",
        "S03"
      ]
    },
    {
      "path": "targets/005-apex-kb-py-status-freshness.md",
      "target_repo_path": "apex-meta/scripts/apex_kb.py",
      "feature": "status_freshness_split",
      "status": "REPAIR_PARTIAL",
      "batch": 1,
      "depends_on": [],
      "byte_estimate": 3200,
      "source_evidence": [
        "S01",
        "S06"
      ]
    },
    {
      "path": "targets/006-apex-kb-py-cli-output-json.md",
      "target_repo_path": "apex-meta/scripts/apex_kb.py",
      "feature": "cli_output_json",
      "status": "KEEP_REAL",
      "batch": 1,
      "depends_on": [],
      "byte_estimate": 3000,
      "source_evidence": [
        "S01",
        "S06"
      ]
    },
    {
      "path": "targets/007-apex-kb-retrieval-cli-output-json.md",
      "target_repo_path": "apex-meta/scripts/apex_kb_retrieval.py",
      "feature": "retrieval_cli_output_json",
      "status": "KEEP_REAL",
      "batch": 1,
      "depends_on": [],
      "byte_estimate": 3000,
      "source_evidence": [
        "S01",
        "S06"
      ]
    },
    {
      "path": "targets/008-script-command-contract.md",
      "target_repo_path": ".claude/skills/apex-kb/references/script-command-contract.md",
      "feature": "script_command_contract_alignment",
      "status": "DOCS_ONLY_REPAIR",
      "batch": 1,
      "depends_on": [
        "targets/001-apex-kb-py-pointer-only-phase0.md",
        "targets/002-apex-kb-py-quality-coverage.md",
        "targets/003-apex-kb-py-query-eval.md",
        "targets/004-apex-kb-py-graph-process-flow.md"
      ],
      "byte_estimate": 3300,
      "source_evidence": [
        "S02",
        "S03"
      ]
    },
    {
      "path": "targets/009-kb-contract-doc-alignment.md",
      "target_repo_path": ".claude/skills/apex-kb/references/kb-contract.md",
      "feature": "kb_contract_alignment",
      "status": "DOCS_ONLY_REPAIR",
      "batch": 1,
      "depends_on": [
        "targets/001-apex-kb-py-pointer-only-phase0.md"
      ],
      "byte_estimate": 2800,
      "source_evidence": [
        "S05"
      ]
    },
    {
      "path": "targets/010-acceptance-tests.md",
      "target_repo_path": ".claude/skills/apex-kb/references/acceptance-tests.md",
      "feature": "acceptance_tests",
      "status": "DOCS_ONLY_REPAIR",
      "batch": 1,
      "depends_on": [
        "targets/001-apex-kb-py-pointer-only-phase0.md",
        "targets/002-apex-kb-py-quality-coverage.md",
        "targets/003-apex-kb-py-query-eval.md",
        "targets/004-apex-kb-py-graph-process-flow.md"
      ],
      "byte_estimate": 3300,
      "source_evidence": [
        "S03",
        "S04"
      ]
    },
    {
      "path": "targets/011-phase2-value-contract-alignment.md",
      "target_repo_path": ".claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md",
      "feature": "phase2_value_contract_alignment",
      "status": "DOCS_ONLY_REPAIR",
      "batch": 1,
      "depends_on": [
        "targets/002-apex-kb-py-quality-coverage.md",
        "targets/003-apex-kb-py-query-eval.md",
        "targets/004-apex-kb-py-graph-process-flow.md"
      ],
      "byte_estimate": 3000,
      "source_evidence": [
        "S05"
      ]
    },
    {
      "path": "targets/012-package-manifest-plan-ledger.md",
      "target_repo_path": ".claude/skills/apex-kb/package-manifest.md",
      "feature": "package_manifest_plan_ledger",
      "status": "DOCS_ONLY_REPAIR",
      "batch": 1,
      "depends_on": [],
      "byte_estimate": 2600,
      "source_evidence": [
        "S04"
      ]
    }
  ],
  "batches": [
    {
      "batch": 1,
      "file_count": 12,
      "paths": [
        "targets/001-apex-kb-py-pointer-only-phase0.md",
        "targets/002-apex-kb-py-quality-coverage.md",
        "targets/003-apex-kb-py-query-eval.md",
        "targets/004-apex-kb-py-graph-process-flow.md",
        "targets/005-apex-kb-py-status-freshness.md",
        "targets/006-apex-kb-py-cli-output-json.md",
        "targets/007-apex-kb-retrieval-cli-output-json.md",
        "targets/008-script-command-contract.md",
        "targets/009-kb-contract-doc-alignment.md",
        "targets/010-acceptance-tests.md",
        "targets/011-phase2-value-contract-alignment.md",
        "targets/012-package-manifest-plan-ledger.md"
      ]
    }
  ],
  "verification": {
    "source_access_checked": true,
    "live_repo_access_checked": true,
    "no_file_over_size_ceiling": true,
    "no_cross_file_narrative_dependencies": true,
    "no_live_splitting_used": true
  }
}
````