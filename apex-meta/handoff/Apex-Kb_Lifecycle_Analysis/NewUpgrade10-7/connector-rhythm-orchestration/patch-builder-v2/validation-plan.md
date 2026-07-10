# Apex KB Patch Pack v2 Validation Plan

```yaml
repository: leela-spec/apexai-os-meta
branch: main
baseline_commit: dbf5bf066cca939abbc1d6a3471cad74c7749db5
patch_directory: apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NewUpgrade10-7/connector-rhythm-orchestration/patch-builder-v2
patch_format: anchored_apply_patch
```

## Required application order

1. `001-apex-kb-skill-capability-routing.patch`
2. `002-apex-kb-postflight-runtime.patch`
3. `003-apex-kb-postflight-command-contract.patch`
4. `004-apex-kb-acceptance-fixtures.patch`
5. `005-apex-kb-package-authority-alignment.patch`
6. `006-apex-kb-state-machine-deprecation-banner.patch`
7. `007-apex-kb-runbook-banner-and-postflight.patch`

## Pre-application checks

1. Confirm repository is `leela-spec/apexai-os-meta`.
2. Confirm target branch is `main`.
3. Confirm target file contents match commit `dbf5bf066cca939abbc1d6a3471cad74c7749db5` or otherwise inspect anchor drift before application.
4. Confirm each patch contains exactly one `*** Update File:` target matching the manifest.
5. Confirm no patch targets the first patch-pack directory or any file outside the seven targets.

## Individual patch checks

For each patch independently:

1. Restore all seven target files to baseline content in a disposable copy or worktree.
2. Apply the patch with the repository's apply-patch-compatible tool.
3. Confirm every anchored section resolves without fuzzy manual intervention.
4. Confirm only the manifest target file changed.
5. Confirm the resulting file contains no patch markers.
6. Restore baseline content before testing the next patch.

## Cumulative patch check

1. Restore all seven target files to baseline content.
2. Apply all seven patches in manifest order.
3. Confirm exactly these files changed:
   - `.claude/skills/apex-kb/SKILL.md`
   - `apex-meta/scripts/apex_kb.py`
   - `.claude/skills/apex-kb/references/script-command-contract.md`
   - `.claude/skills/apex-kb/references/acceptance-tests.md`
   - `.claude/skills/apex-kb/package-manifest.md`
   - `.claude/skills/apex-kb/references/lifecycle-state-machine.md`
   - `.claude/skills/apex-kb/examples/lifecycle-runbook.md`
4. Confirm no file under `patch-builder/` or `patch-builder-v2/` was modified by patch application.

## Static validation

```text
python -m py_compile apex-meta/scripts/apex_kb.py
python -m py_compile apex-meta/scripts/apex_kb_retrieval.py
python apex-meta/scripts/apex_kb.py --help
python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/apex-kb-smoke postflight --help
```

Pass criteria:

- both Python files compile;
- `postflight` appears in lifecycle help;
- global `--json`, `--dry-run`, `--allow-write`, `--strict`, and `--output-json` placement remains accepted according to the existing normalization contract;
- direct commands remain present.

## Runtime validation

Use the existing acceptance-test fixture KB. Do not invent new production paths.

### Dry-run modes

```text
python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/apex-kb-smoke --json postflight
python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/apex-kb-smoke --allow-write --dry-run --json postflight
```

Required result:

- status `planned`;
- `evidence_complete: false`;
- seven steps in exact order;
- no writes;
- exit code `0`.

### Write mode

```text
python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/apex-kb-smoke --allow-write --json postflight
```

Required result when all blocking delegates pass:

- status `pass`;
- `evidence_complete: true`;
- retrieval stale result is `fresh`;
- exit code `0`.

### Failure modes

Run isolated fixtures for:

- wiki-index failure;
- retrieval-build failure;
- lint strict failure;
- quality strict failure;
- missing retrieval metadata;
- unreadable retrieval metadata;
- internal delegate exception.

Required behavior:

- lint and quality failures do not prevent audit and status diagnostics;
- retrieval stale is skipped after wiki-index or retrieval-build failure;
- audit remains nonblocking;
- blocking failures produce status `fail` and exit code `2`;
- internal delegate exceptions produce status `internal_error` and exit code `1`;
- every delegate result remains under `steps[].result`.

## Reason-code synchronization validation

Compare these three sets:

1. `QUALITY_REASON_CODES` in `apex_kb.py`;
2. `connector_precheck_reason_concepts` in `SKILL.md`;
3. the reason-code list in `acceptance-tests.md`.

They must contain exactly these eleven values and no extras:

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

## Documentation alignment

Confirm:

- `SKILL.md` is the sole operational lifecycle authority;
- the state machine is marked deprecated reference material;
- the runbook is marked terminal-backed example-only;
- the command contract matches runtime stage order, status model, and exit codes;
- the connector checklist is explicitly preventive and does not replace terminal `quality --strict`.
