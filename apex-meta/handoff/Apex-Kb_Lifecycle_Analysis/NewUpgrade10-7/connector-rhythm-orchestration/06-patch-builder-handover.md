# Apex KB Connector Routing and Postflight — Patch Builder Handover

## Role

You are the patch builder for the accepted Apex KB connector-routing and postflight change set.

Your job is to create patch artifacts against current `main`.

Do not apply patches. Do not modify the seven target files directly. Do not reopen research or architecture decisions.

## Repository

```yaml
repository: leela-spec/apexai-os-meta
branch: main
mode: patch_artifact_creation_only
```

Before building patches, record the current `main` commit SHA. Every patch must be generated against that same baseline.

## Governing decisions

The research phase is complete.

1. A connector-only executor performs bounded whole-file semantic authoring and stops at `compiled_unvalidated`.
2. A terminal-backed executor owns deterministic commands, partial edits, manifests, hashes, indexes, lint, quality, status, stale checks, postflight evidence, and terminal validation.
3. `SKILL.md` must route by execution capability before showing terminal-oriented procedure or navigation.
4. The connector checklist mirrors the runtime quality reason-code contract as an authoring precheck. It is not deterministic certification.
5. Add one thin `postflight` command that delegates existing implementations in fixed order. It must not become a workflow engine.
6. `SKILL.md` remains the sole operational lifecycle authority. The lifecycle state machine is deprecated reference material; the runbook is a terminal-backed example.
7. No new lifecycle states are required. Preserve `compiled_unvalidated`, `partial`, and `query_ready`.

## Read first

Read these decision sources before reading target files:

1. `apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NewUpgrade10-7/architecture-analysis-and-connector-rhythm-handover.md`
   - Purpose: governing architecture, connector ownership boundary, and non-targets.

2. `apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NewUpgrade10-7/connector-rhythm-orchestration/00-orchestrator-design-note.md`
   - Purpose: adopted connector rhythm, checklist authority, compile manifest, and truthful completion states.

3. `apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NewUpgrade10-7/connector-rhythm-orchestration/05-r08-capability-routing-report.md`
   - Purpose: exact capability router, connector route, terminal route, and authority-banner decisions.

4. `apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NewUpgrade10-7/connector-rhythm-orchestration/01-research-commission-r06-checklist-equivalence.md`
   - Purpose: scope and output contract for the connector checklist research.
   - Required result to implement: the eleven reason-code concepts listed below.

5. `apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NewUpgrade10-7/connector-rhythm-orchestration/02-research-commission-r07-postflight-aggregation.md`
   - Purpose: scope and output contract for the postflight research.
   - Required result to implement: the fixed seven-stage aggregate described below.

6. `apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NewUpgrade10-7/connector-rhythm-orchestration/04-research-commission-r09-final-minimal-change-plan.md`
   - Purpose: target-file investigation contract. Use this handover as the resolved final plan.

Do not inspect unrelated repository files.

## Exact target files and patch names

Create exactly these seven patch files:

```text
001-apex-kb-skill-capability-routing.patch
002-apex-kb-postflight-runtime.patch
003-apex-kb-postflight-command-contract.patch
004-apex-kb-acceptance-fixtures.patch
005-apex-kb-package-authority-alignment.patch
006-apex-kb-state-machine-deprecation-banner.patch
007-apex-kb-runbook-banner-and-postflight.patch
```

They correspond to:

```text
.claude/skills/apex-kb/SKILL.md
apex-meta/scripts/apex_kb.py
.claude/skills/apex-kb/references/script-command-contract.md
.claude/skills/apex-kb/references/acceptance-tests.md
.claude/skills/apex-kb/package-manifest.md
.claude/skills/apex-kb/references/lifecycle-state-machine.md
.claude/skills/apex-kb/examples/lifecycle-runbook.md
```

Do not add target files unless current-main evidence proves the accepted design cannot be implemented without one. If that occurs, stop and report the blocker instead of expanding scope.

## Required changes

### 1. `SKILL.md`

Create a capability-first router immediately after the title.

Use one routing question:

> Can the executor run repository Python commands in a live worktree and capture the command, exit status, stdout, and stderr?

Route to:

- `terminal_backed`
- `connector_only`
- `unsupported`

Replace the universal procedure with two routes.

The connector route must:

- allow only complete new semantic files or complete rewrites of explicitly owned semantic files;
- prohibit partial edits, appends, machine sections, `wiki/index.md`, manifests, hashes, derived indexes, deterministic commands, and certification;
- use one semantic page per context window;
- require bounded source reading, complete authoring, complete reread, checklist precheck, whole-file write, stored-content readback, and compile-manifest entry;
- create `log/connector-compile-<run-id>.json` as a complete new handoff file;
- stop at `compiled_unvalidated`.

The connector checklist must cover these runtime reason-code concepts exactly once:

```text
missing_source_refs
missing_phase2_value_sections
placeholder_text
no_key_claims
claim_pointer_coverage_below_100_percent
single_claim_summary
single_claim_concept_thin
concept_micro_not_evidenced
thin_macro_meso_micro
summary_source_breadth_below_profile
no_query_routes
```

State clearly that the checklist is preventive only and that terminal `quality --strict` remains authoritative.

The terminal route must reference existing command, retrieval, acceptance-test, and runbook documents instead of duplicating command sequences. Identify `postflight` as the preferred bounded deterministic completion interface once the runtime patch is applied.

Preserve the current lifecycle, output tiers, ownership model, semantic acceptance requirement, and completion labels.

### 2. `apex_kb.py`

Add one immutable registry containing the eleven quality reason-code strings. Replace duplicated production literals with registry references without changing any trigger, threshold, parser, regex, exception, or repair behavior.

Add `postflight` as a thin in-process aggregator. Do not shell out.

Fixed stage order:

1. wiki index
2. retrieval build
3. lint strict
4. quality strict
5. audit
6. status
7. retrieval stale

Required behavior:

- delegate existing functions;
- resolve one KB root and use it for every stage;
- preserve each delegate result under `steps[].result`;
- continue safe diagnostics after lint or quality failure;
- treat audit as nonblocking;
- skip dependent retrieval acceptance checks after index or retrieval-build failure;
- default dry-run returns `planned`, `evidence_complete: false`, and performs no writes;
- `--allow-write --dry-run` remains dry-run;
- `--allow-write` passes only when all blocking stages pass and retrieval is fresh;
- schema: `apex.kb.postflight.v1`;
- exit codes: planned/pass `0`, fail `2`, internal error `1`.

Do not add retries, scheduling, persisted orchestration state, dynamic graphs, rollback logic, semantic review, query evaluation, ranking changes, commit, or push.

### 3. `script-command-contract.md`

Document the implemented `postflight` command only:

- exact seven-stage order;
- blocking and nonblocking behavior;
- dependency skips;
- dry-run as `planned`, never certified pass;
- `--allow-write` behavior;
- schema and exit codes;
- full delegate-result preservation;
- explicit exclusions;
- terminal `quality --strict` authority over the connector checklist.

Do not rewrite the broader lifecycle or individual command contracts.

### 4. `acceptance-tests.md`

Add deterministic fixtures for:

- all eleven reason codes;
- one passing multi-source page;
- the valid concise/narrow-entity exception;
- runtime-registry, checklist, and fixture synchronization;
- postflight dry-run;
- `--allow-write --dry-run`;
- successful write mode;
- lint failure;
- quality failure;
- retrieval-build failure;
- missing or unreadable retrieval metadata;
- shared KB-root propagation;
- path safety;
- direct-command regression;
- JSON schema, stage order, dependency skipping, evidence preservation, status, and exit code.

Do not add LLM grading, subjective prose judgments, external dependencies, or a new universal word threshold.

### 5. `package-manifest.md`

Change only the two inventory roles:

- lifecycle state machine → deprecated historical/reference state model; `SKILL.md` remains operational authority;
- lifecycle runbook → example-only terminal-backed lifecycle sequence.

Leave the existing lifecycle-authority clause and all other package metadata unchanged.

### 6. `lifecycle-state-machine.md`

Add a deprecation banner immediately after the title:

> DEPRECATED REFERENCE — SKILL.md is the sole operational lifecycle authority. This file is retained for historical/reference purposes only. Executors must not derive independent completion states, transitions, or required procedures from it.

Make no other changes.

### 7. `lifecycle-runbook.md`

Add an example-only banner immediately after the title:

> EXAMPLE ONLY — This runbook illustrates a terminal-backed execution sequence. It is not the universal Apex KB procedure and does not apply to connector-only semantic authoring. Follow the execution-surface router in SKILL.md first.

Update only the postflight section so that:

- `postflight` is the preferred completion interface;
- default invocation is preview/planned;
- `--allow-write` is required for derived writes and certifying deterministic evidence;
- individual commands remain diagnostic or maintenance interfaces.

Do not otherwise rewrite the runbook.

## Patch artifact location

Create a new artifact directory under:

```text
apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NewUpgrade10-7/connector-rhythm-orchestration/patch-builder/
```

Write:

```text
000-patch-manifest.md
001-apex-kb-skill-capability-routing.patch
002-apex-kb-postflight-runtime.patch
003-apex-kb-postflight-command-contract.patch
004-apex-kb-acceptance-fixtures.patch
005-apex-kb-package-authority-alignment.patch
006-apex-kb-state-machine-deprecation-banner.patch
007-apex-kb-runbook-banner-and-postflight.patch
validation-plan.md
codex-apply-prompt.md
```

## Patch construction rules

- Fetch every target file from the recorded baseline SHA.
- Generate valid unified diffs with repository-relative paths.
- One patch per target file.
- Do not hand-edit target files in the repository.
- Do not apply patches.
- Do not claim `git apply --check`, Python compilation, tests, or runtime validation were executed.
- Inspect each generated patch text for correct source and destination paths, coherent hunks, and target-file scope.
- Keep all seven patches based on the same baseline.

## Manifest requirements

`000-patch-manifest.md` must record:

```yaml
repository: leela-spec/apexai-os-meta
branch: main
baseline_commit: <exact SHA>
mode: patch_artifacts_only
target_files: []
patches_in_order: []
excluded_files: []
known_unvalidated_claims:
  - git apply check not executed by connector
  - Python compilation not executed by connector
  - acceptance tests not executed by connector
  - runtime behavior not certified by connector
```

Also include a concise trace from every patch to R06, R07, or R08.

## Validation plan

`validation-plan.md` must contain the exact terminal order:

1. confirm baseline and target-file contents;
2. run `git apply --check` individually;
3. run cumulative `git apply --check` in manifest order;
4. apply in manifest order;
5. compile `apex_kb.py` and `apex_kb_retrieval.py`;
6. verify `postflight` help and global-flag placement;
7. run direct-command regressions;
8. run reason-code/checklist/fixture synchronization tests;
9. run all quality fixtures;
10. run all postflight dry-run, write-mode, failure, dependency, schema, and exit-code fixtures;
11. inspect documentation/runtime alignment;
12. confirm exactly seven target files changed.

Use exact commands only when they can be derived from current repository contracts. Do not invent test commands. If a command cannot be resolved, state the unresolved command explicitly.

## Codex apply prompt

`codex-apply-prompt.md` must be command-focused and short.

It must instruct Codex to:

- work on `main`;
- fast-forward from origin;
- verify the recorded baseline;
- apply patches in manifest order;
- run the validation plan;
- stop on any patch or required validation failure;
- commit only the seven target files after all checks pass;
- push `main`;
- report starting SHA, patch checks, changed files, validation results, commit SHA, push result, and any workaround.

Do not include branches, pull requests, alternative implementations, or manual equivalent edits.

## Drift to reject

Reject and do not implement:

- lifecycle redesign;
- new lifecycle states;
- quality-threshold or reason-trigger changes;
- retrieval ranking or metadata redesign;
- general CLI cleanup;
- checklist duplication in additional files;
- generated connector checklist tooling;
- new workflow engine, agent, scheduler, retry system, rollback manager, or persisted orchestration state;
- semantic review inside postflight;
- changes to KB corpus files;
- changes outside the seven target files.

## Completion condition

The patch-builder task is complete only when all ten artifact files exist in the patch-builder directory and have been read back from `main`.

Report:

```yaml
patch_builder_result:
  baseline_commit: ""
  artifact_commit: ""
  patch_directory: ""
  patches_created: []
  target_files_modified_directly: false
  patches_applied: false
  terminal_validation_claimed: false
  readback_verified: true|false
  blockers: []
```
