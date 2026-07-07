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
