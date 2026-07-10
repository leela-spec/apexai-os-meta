# Apex KB Patch Pack v2 Logic Review

```yaml
review_scope:
  repository: leela-spec/apexai-os-meta
  branch: main
  baseline_commit: dbf5bf066cca939abbc1d6a3471cad74c7749db5
  source_patch_directory: apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NewUpgrade10-7/connector-rhythm-orchestration/patch-builder
  output_patch_directory: apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NewUpgrade10-7/connector-rhythm-orchestration/patch-builder-v2
  review_mode: independent_rederivation
  target_files_modified: false
```

## Original pack defects and risks identified

### 1. Patch representation did not match the required consumer format

The first pack used conventional unified-diff headers and numeric hunks. The v2 consumer contract requires anchored `apply_patch` syntax:

```text
*** Begin Patch
*** Update File: <repo-relative path>
@@ <stable symbol or heading>
...
*** End Patch
```

Decision: regenerate every patch in the required format rather than mechanically translating numeric hunks.

### 2. Runtime internal errors were not separated from ordinary blocking failures

The original runtime patch caught retrieval exceptions and stored `status: error`, but the aggregate then collapsed these into the same blocking-failure path used for deterministic validation failures. The declared contract requires:

- planned/pass: exit `0`;
- internal error: exit `1`;
- blocking validation failure: exit `2`.

Decision: add `_postflight_call`, preserve delegate exceptions as `status: internal_error`, aggregate an `internal_error` flag, and update `main` so aggregate internal errors return `1`.

### 3. Delegate return shapes are not uniform

Existing delegates do not all expose identical status fields. In particular, retrieval `cmd_build_index` primarily returns counts and write records, while retrieval `cmd_stale` returns a freshness status.

Decision:

- treat explicit `blocked`, `fail`, `error`, or `internal_error` as failures;
- do not invent success fields for delegates that do not provide them;
- require retrieval freshness from the existing stale result's `status: fresh`;
- preserve complete delegate results under `steps[].result`.

### 4. Internal import failure required explicit handling

The postflight aggregate must delegate retrieval behavior in-process without shelling out. Import failure is an executor/runtime defect, not a quality failure.

Decision: isolate retrieval-module loading in `_postflight_retrieval_module` and convert load failure to an internal error result.

### 5. Dependency skip wording was too broad

The accepted design requires skipping the dependent retrieval stale acceptance check after wiki-index or retrieval-build failure. It does not require skipping lint, quality, audit, or status diagnostics.

Decision: continue lint, quality, audit, and status; skip only retrieval stale after either dependency fails.

### 6. Reason-code synchronization lacked one immutable runtime source

The eleven reason-code strings were duplicated as production literals and separately listed in connector instructions and tests.

Decision: add immutable `QUALITY_REASON_CODES` plus `QUALITY_REASON` references without changing any trigger, threshold, parser, regex, concise-page exception, or repair behavior.

### 7. Documentation needed to match the corrected runtime status model

The original command-contract patch described exit code `1` but did not explain how runtime internal errors are represented.

Decision: document `status: internal_error`, result preservation, and exit code `1` explicitly.

## Preserved behavior

```yaml
preserved:
  - all existing quality thresholds
  - all existing reason triggers
  - entity concise-page exception
  - direct command interfaces
  - global flag normalization behavior
  - output-json behavior
  - retrieval ranking and index design
  - existing lifecycle states
  - semantic acceptance requirement
  - connector completion cap compiled_unvalidated
  - audit nonblocking behavior
```

## Explicit non-goals

```yaml
not_added:
  - workflow engine
  - retries
  - scheduler
  - persisted orchestration state
  - rollback manager
  - dynamic dependency graph
  - semantic grading
  - query evaluation changes
  - retrieval ranking changes
  - general CLI cleanup
  - new lifecycle states
  - new universal quality threshold
```

## Patch-by-patch consistency review

| Patch | Target | Consistency result |
|---|---|---|
| 001 | `.claude/skills/apex-kb/SKILL.md` | Capability router precedes procedure; connector and terminal authorities remain distinct; all eleven reason concepts appear once. |
| 002 | `apex-meta/scripts/apex_kb.py` | Registry and postflight are additive; stage order is fixed; results are preserved; internal errors remain distinct from validation failures. |
| 003 | `script-command-contract.md` | Documents only the runtime introduced by patch 002. |
| 004 | `acceptance-tests.md` | Covers synchronization, dry-run, write mode, failure modes, dependency skipping, schema, result preservation, and exit codes. |
| 005 | `package-manifest.md` | Changes only the two inventory roles required by the authority decision. |
| 006 | `lifecycle-state-machine.md` | Adds only the deprecation banner. |
| 007 | `lifecycle-runbook.md` | Adds the example-only banner and minimally replaces the postflight section. |

## Applicability notes

The patches are anchored to stable symbols or headings from baseline commit `dbf5bf066cca939abbc1d6a3471cad74c7749db5`. They deliberately avoid line-number hunks and large unchanged blocks.

Potential application blockers to check in the later applier:

- target files have drifted from the pinned baseline;
- an anchor heading was renamed;
- the apply-patch implementation requires narrower context around repeated headings;
- current `main` already contains equivalent changes.

These are application-time checks, not reasons to modify target files during patch construction.

## Review verdict

```yaml
verdict: ready_for_apply_patch_validation
functional_intent_preserved: true
original_logic_mechanically_copied: false
runtime_internal_error_contract_corrected: true
one_target_per_patch: true
target_files_modified_on_main: false
```
