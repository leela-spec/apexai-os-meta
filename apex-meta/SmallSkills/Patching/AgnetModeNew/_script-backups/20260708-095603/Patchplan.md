# Handover — Apex KB v3 Repair Patch Plan State and Patch-Pack Process

## 0. Purpose

This handover explains the current Apex KB v3 repair plan, what has already been done, which files are connected, and what the next executor must build.

This is **not** an Agent Mode prompt.

This is **not** a Codex apply prompt.

This is the context handover another AI should read before creating or executing the next patch-pack-builder workflow.

---

## 1. Current state

The Apex KB v3 repair patch-plan package has already landed on `main`.

```yaml
repo: leela-spec/apexai-os-meta
branch: main
landed_commit: eaa03846978e433fe135b317b93f1c08fe3f2022
commit_message: "Add Apex KB v3 repair patch plan package"
```

The commit exists on `main` with the expected message.

The landed package root is:

```text
apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NextFinalization/apex-kb-v3-repair-patch-plan/
```

The package manifest identifies the package as:

```yaml
package_id: apex-kb-v3-repair-patch-plan
version: "0.1"
created_for_repo: leela-spec/apexai-os-meta
branch: main
suspect_commit: 0c747db4
mode: patch_plan_only
```

The manifest also defines the later patch-pack output root:

```text
apex-meta/patches/apex-kb-v3-repair/
```

These values are present in the landed manifest.

---

## 2. What was already done

A previous answer produced the patch-plan as one large monolithic output. That was the wrong artifact shape.

A deterministic local splitter script was then created and used to separate that monolithic output into individual files.

The split files were committed to the repo as the package:

```text
apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NextFinalization/apex-kb-v3-repair-patch-plan/
```

The split package now contains:

```yaml
global_files:
  - 00-global-rules.md
  - 01-read-verification-ledger.md
  - 02-current-state-audit.md
  - 03-target-file-map.md
  - 04-feature-repair-index.md
  - 05-agent-mode-patch-pack-builder-contract.md
  - 06-validation-contract.md
  - 07-codex-applier-contract.md
  - 08-risk-and-rollback-policy.md
  - 09-final-execution-order.md
  - manifest.json

target_plan_files:
  - targets/001-apex-kb-py-pointer-only-phase0.md
  - targets/002-apex-kb-py-quality-coverage.md
  - targets/003-apex-kb-py-query-eval.md
  - targets/004-apex-kb-py-graph-process-flow.md
  - targets/005-apex-kb-py-status-freshness.md
  - targets/006-apex-kb-py-cli-output-json.md
  - targets/007-apex-kb-retrieval-cli-output-json.md
  - targets/008-script-command-contract.md
  - targets/009-kb-contract-doc-alignment.md
  - targets/010-acceptance-tests.md
  - targets/011-phase2-value-contract-alignment.md
  - targets/012-package-manifest-plan-ledger.md
```

The manifest confirms a batch of exactly 12 target plan paths.

The manifest also records that source access, live repo access, file-size, and dependency checks were already performed for the package.

---

## 3. Why this repair exists

A prior Apex KB v3 P0–P2 closure attempt landed useful changes, but the patch process was invalid and several advertised features remained partial or stub-class.

The repair strategy is:

```yaml
repair_strategy:
  decision: targeted_repair_not_default_revert
  reason:
    - useful v3 surfaces already landed
    - full rollback would discard useful work
    - failed patch artifacts must not be reused as implementation authority
    - real behavior must replace stub/marker behavior
```

The repair wave must preserve useful already-landed functionality, especially:

```yaml
preserve:
  - source-payload-manifest core
  - --output-json support
  - CLI compatibility where functional
  - useful status split surfaces
```

The repair wave must replace or complete:

```yaml
repair:
  - pointer_only Phase 0 behavior
  - quality / coverage reporting
  - query-eval pack behavior
  - graph / process-flow extraction
  - status freshness separation
  - documentation overclaims
  - acceptance tests
```

The repair package is explicitly plan-only. It does not contain final patch hunks.

---

## 4. Executor model

The correct execution model has two stages.

```yaml
stage_1_agent_mode:
  role: Git-native patch-pack builder
  input:
    - live terminal Git repository
    - landed repair patch-plan package
  output:
    - validated patch artifacts under apex-meta/patches/apex-kb-v3-repair/
  final_state:
    - patch artifacts committed
    - runtime target files clean/unmodified

stage_2_codex:
  role: deterministic patch applier and verifier
  input:
    - validated patch pack from Agent Mode
  output:
    - runtime/doc repairs applied
    - validation run
    - commit and push to main
```

Do not skip Stage 1.

Codex should not apply anything until Agent Mode has produced real Git-native `.patch` artifacts that pass `git apply --check` individually and cumulatively.

---

## 5. Source package to read first

The next builder must read the package from the repo, not from chat memory.

Read these files first:

```text
apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NextFinalization/apex-kb-v3-repair-patch-plan/00-global-rules.md
apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NextFinalization/apex-kb-v3-repair-patch-plan/01-read-verification-ledger.md
apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NextFinalization/apex-kb-v3-repair-patch-plan/02-current-state-audit.md
apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NextFinalization/apex-kb-v3-repair-patch-plan/03-target-file-map.md
apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NextFinalization/apex-kb-v3-repair-patch-plan/04-feature-repair-index.md
apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NextFinalization/apex-kb-v3-repair-patch-plan/05-agent-mode-patch-pack-builder-contract.md
apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NextFinalization/apex-kb-v3-repair-patch-plan/06-validation-contract.md
apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NextFinalization/apex-kb-v3-repair-patch-plan/08-risk-and-rollback-policy.md
apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NextFinalization/apex-kb-v3-repair-patch-plan/09-final-execution-order.md
apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NextFinalization/apex-kb-v3-repair-patch-plan/manifest.json
```

Then read all 12 target plan files listed in the manifest batch.

---

## 6. Target file dependency map

### 6.1 Central runtime file: `apex-meta/scripts/apex_kb.py`

This is the main repair target.

It is connected to six target plans:

```yaml
apex-meta/scripts/apex_kb.py:
  target_plans:
    - id: "001"
      file: targets/001-apex-kb-py-pointer-only-phase0.md
      feature: pointer_only_phase0
      repair_class: REPLACE_STUB

    - id: "002"
      file: targets/002-apex-kb-py-quality-coverage.md
      feature: quality_coverage
      repair_class: REPLACE_STUB

    - id: "003"
      file: targets/003-apex-kb-py-query-eval.md
      feature: query_eval
      repair_class: REPLACE_STUB

    - id: "004"
      file: targets/004-apex-kb-py-graph-process-flow.md
      feature: graph_process_flow
      repair_class: REPLACE_STUB

    - id: "005"
      file: targets/005-apex-kb-py-status-freshness.md
      feature: status_freshness_split
      repair_class: REPAIR_PARTIAL

    - id: "006"
      file: targets/006-apex-kb-py-cli-output-json.md
      feature: cli_output_json
      repair_class: KEEP_REAL
```

The manifest confirms these `apex_kb.py` target-plan entries and statuses.

#### Internal dependencies inside `apex_kb.py`

These features are connected and should not be patched as isolated random edits.

```yaml
pointer_only_phase0:
  affects:
    - source manifest interpretation
    - pointer_only source resolution
    - Phase 0 file scanning
    - Phase 0 warning/error reporting
  must_happen_before:
    - quality_coverage validation
    - status/audit assertions involving source coverage

quality_coverage:
  depends_on:
    - source manifest
    - wiki frontmatter source_refs
    - Phase 2 value-contract sections
  produces:
    - source_to_page map
    - page_to_source map
    - shell_page_candidates
    - phase2_repair_candidates
  informs:
    - postflight quality loop
    - acceptance tests
    - docs alignment

query_eval:
  depends_on:
    - query output conventions
    - saved query/eval pack path
    - deterministic JSON/Markdown report behavior
  connects_to:
    - quality_coverage
    - retrieval/query docs
    - acceptance tests

graph_process_flow:
  depends_on:
    - Phase 0 artifact directory
    - Markdown links
    - wikilinks
    - repo path references
    - YAML path references
    - process sequence markers
  risk:
    - highest-complexity deterministic repair
  rule:
    - additive and non-semantic
    - no broad semantic graph inference

status_freshness_split:
  depends_on:
    - wiki index status
    - retrieval index status
    - source-payload manifest status
  purpose:
    - distinguish canonical and derived artifact freshness
    - avoid false all-good status when derived indexes are stale

cli_output_json:
  purpose:
    - preserve existing useful support
    - regression-test it
    - do not redesign unless it conflicts with repair behavior
```

The main `apex_kb.py` patch can be one cumulative patch for the file if that is safer than multiple overlapping patches. The manifest expresses multiple target-plan features for the same file, so the builder must either produce one file-level patch or clearly document how multiple patches compose.

---

### 6.2 Retrieval runtime file: `apex-meta/scripts/apex_kb_retrieval.py`

This file is connected to one target plan:

```yaml
apex-meta/scripts/apex_kb_retrieval.py:
  target_plan:
    - id: "007"
      file: targets/007-apex-kb-retrieval-cli-output-json.md
      feature: retrieval_cli_output_json
      repair_class: KEEP_REAL
```

The manifest confirms this target path and status.

This is primarily a preservation/regression-test patch:

```yaml
intent:
  - preserve useful output-json behavior
  - ensure CLI/output behavior matches docs
  - do not rewrite retrieval architecture
  - do not broaden into FTS/BM25 redesign
```

---

### 6.3 Documentation and contract files

These docs must be aligned after runtime behavior is repaired.

```yaml
docs_targets:
  - target_file: .claude/skills/apex-kb/references/script-command-contract.md
    target_plan: targets/008-script-command-contract.md
    feature: script_command_contract_alignment
    status: DOCS_ONLY_REPAIR
    depends_on:
      - pointer_only_phase0
      - quality_coverage
      - query_eval
      - graph_process_flow

  - target_file: .claude/skills/apex-kb/references/kb-contract.md
    target_plan: targets/009-kb-contract-doc-alignment.md
    feature: kb_contract_alignment
    status: DOCS_ONLY_REPAIR
    depends_on:
      - pointer_only_phase0

  - target_file: .claude/skills/apex-kb/references/acceptance-tests.md
    target_plan: targets/010-acceptance-tests.md
    feature: acceptance_tests
    status: DOCS_ONLY_REPAIR
    depends_on:
      - pointer_only_phase0
      - quality_coverage
      - query_eval
      - graph_process_flow

  - target_file: .claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md
    target_plan: targets/011-phase2-value-contract-alignment.md
    feature: phase2_value_contract_alignment
    status: DOCS_ONLY_REPAIR
    depends_on:
      - quality_coverage
      - query_eval
      - graph_process_flow

  - target_file: .claude/skills/apex-kb/package-manifest.md
    target_plan: targets/012-package-manifest-plan-ledger.md
    feature: package_manifest_plan_ledger
    status: DOCS_ONLY_REPAIR
```

The manifest confirms these target paths, features, statuses, and dependencies.

The documentation files must not overclaim behavior. They should describe only implemented and validated runtime behavior.

---

## 7. Patch-pack output expected next

The next Agent Mode patch-pack builder should create:

```text
apex-meta/patches/apex-kb-v3-repair/
```

Expected artifacts:

```text
000-patch-manifest.md
001-apex-kb-py-pointer-only-phase0.patch
002-apex-kb-py-quality-coverage.patch
003-apex-kb-py-query-eval.patch
004-apex-kb-py-graph-process-flow.patch
005-apex-kb-py-status-freshness.patch
006-apex-kb-py-cli-output-json.patch
007-apex-kb-retrieval-cli-output-json.patch
008-script-command-contract.patch
009-kb-contract-doc-alignment.patch
010-acceptance-tests.patch
011-phase2-value-contract-alignment.patch
012-package-manifest-plan-ledger.patch
validation-report.md
999-codex-apply-handoff.md
```

If `apex-meta/scripts/apex_kb.py` is patched as one cumulative patch instead of six separate patches, then the patch pack must explicitly document the merge in `000-patch-manifest.md` and still validate every feature acceptance condition.

---

## 8. Required patch-building method

The patch pack must be built Git-natively.

```yaml
method:
  source_of_truth:
    - live terminal Git repository
    - main branch
    - landed split repair plan package
  patch_generation:
    - edit target file in worktree
    - generate patch using git diff
    - save patch under apex-meta/patches/apex-kb-v3-repair/
    - validate patch with git apply --check
    - revert target file before final commit
  validation:
    - every patch applies individually
    - all patches apply cumulatively
    - runtime scripts compile
    - smoke/behavior checks pass
  final_state:
    - patch artifacts only
    - target runtime/doc files clean
```

Do not use:

```yaml
forbidden:
  - manual patch snippets
  - abbreviated hunk headers
  - marker-only checks
  - failed patch files from apex-meta/patches/apex-kb-v3-p0-p2-closure/
  - connector/API snippets as baseline
  - synthetic repo reconstruction
  - PASS_WITH_WORKAROUNDS
```

---

## 9. Validation expectations

A successful patch pack must prove the following before Codex receives it.

```yaml
validation_required:
  git_patch_validity:
    - every patch has valid hunk headers
    - git apply --check passes per patch
    - cumulative git apply --check passes from clean main

  python:
    - python -m py_compile apex-meta/scripts/apex_kb.py
    - python -m py_compile apex-meta/scripts/apex_kb_retrieval.py

  behavior:
    pointer_only_phase0:
      - accessible pointer-only text files are included in Phase 0 artifact scanning
      - unresolved pointer-only files are reported truthfully

    quality_coverage:
      - source_to_page and page_to_source maps are populated where source_refs exist
      - missing source_refs are reported
      - shell/low-value page candidates are detected deterministically

    query_eval:
      - existing query-eval pack can be read
      - pack can be initialized only with explicit write permission
      - invalid entries are reported

    graph_process_flow:
      - Markdown links, wikilinks, repo path references, YAML path references, and process sequence markers are extracted
      - artifacts write under manifests/phase0 only when write permission is explicit

    status_freshness:
      - wiki index status is separate from retrieval index status
      - source-payload manifest status is separate from derived search freshness

    cli_output_json:
      - lifecycle and retrieval output-json behavior still works
      - output paths remain constrained inside the KB root
```

The validation report must include commands, outputs, and pass/fail status.

---

## 10. What must not happen next

Do not let the next AI drift into these tasks:

```yaml
not_next:
  - redesign Apex KB
  - rewrite existing KB wiki pages
  - patch apex-kb2
  - create a new lifecycle architecture
  - debate Phase 0 parser libraries
  - add unrelated retrieval/FTS redesign
  - mutate Plan, Sync, Session, PreCap, FlowRecap, APSU, or personal orchestration files
  - directly apply runtime repairs without creating patch artifacts first
  - create a Codex prompt before the patch pack exists
```

The next stage is specifically:

```yaml
next_stage:
  name: build_repair_patch_pack
  executor: Agent Mode
  input: apex-kb-v3-repair-patch-plan package
  output: validated Git-native patch pack
```

---

## 11. Read order for the next AI

A good next AI should read in this order:

```yaml
read_order:
  1_manifest:
    - apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NextFinalization/apex-kb-v3-repair-patch-plan/manifest.json

  2_global_context:
    - 00-global-rules.md
    - 02-current-state-audit.md
    - 03-target-file-map.md
    - 04-feature-repair-index.md

  3_builder_contract:
    - 05-agent-mode-patch-pack-builder-contract.md
    - 06-validation-contract.md
    - 08-risk-and-rollback-policy.md
    - 09-final-execution-order.md

  4_target_plans:
    - targets/001-apex-kb-py-pointer-only-phase0.md
    - targets/002-apex-kb-py-quality-coverage.md
    - targets/003-apex-kb-py-query-eval.md
    - targets/004-apex-kb-py-graph-process-flow.md
    - targets/005-apex-kb-py-status-freshness.md
    - targets/006-apex-kb-py-cli-output-json.md
    - targets/007-apex-kb-retrieval-cli-output-json.md
    - targets/008-script-command-contract.md
    - targets/009-kb-contract-doc-alignment.md
    - targets/010-acceptance-tests.md
    - targets/011-phase2-value-contract-alignment.md
    - targets/012-package-manifest-plan-ledger.md

  5_live_targets:
    - apex-meta/scripts/apex_kb.py
    - apex-meta/scripts/apex_kb_retrieval.py
    - .claude/skills/apex-kb/references/script-command-contract.md
    - .claude/skills/apex-kb/references/kb-contract.md
    - .claude/skills/apex-kb/references/acceptance-tests.md
    - .claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md
    - .claude/skills/apex-kb/package-manifest.md
```

---

## 12. One-line summary

The monolithic repair plan has already been split and committed as a 23-file patch-plan package on `main`; the next task is to use that package to build a validated Git-native repair patch pack under `apex-meta/patches/apex-kb-v3-repair/`, leaving runtime files clean until Codex applies the patch pack later.