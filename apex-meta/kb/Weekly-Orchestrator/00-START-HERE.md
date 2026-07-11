---
title: "Weekly Orchestrator — Start Here"
purpose: "Stable entrypoint for humans and AI systems locating the weekly orchestration index, its source material, and the live implementation authority."
status: "live"
created: 2026-07-11
maintenance: "Keep index paths and authority notes synchronized with the repository-wide orchestration systems index."
---

# Weekly Orchestrator — Start Here

Use this file as the stable entrypoint for the repository's weekly orchestration knowledge domain.

## Default retrieval order

```yaml
default_read:
  human_index: indexes/weekly-orchestration-master-index-v3.md
  machine_index: indexes/weekly-orchestration-master-index-v3.yaml
  retrieval_records: indexes/weekly-orchestration-master-index-v3.jsonl

research_sources:
  path: OperatorResearch/
  load_policy: targeted_only

live_implementation:
  root_instruction: ../../../.claude/Claude.md
  skills_root: ../../../.claude/skills/
  operator_output_design: ../../operator-output-design/

index_policy:
  role: navigation_and_retrieval
  authority: non_normative
  note: >
    The index identifies and ranks relevant sources. It does not replace live
    skill contracts, activation records, package manifests, or durable state.
```

## Authority order

When indexed files disagree, use this precedence:

1. Live skill instructions and contracts under `.claude/skills/`.
2. Current activation and validation records.
3. Current template-promotion mappings and package manifests.
4. Production template-system documentation.
5. Earlier design rationale and operator-research sources.
6. Historical or provenance-only material.

## Weekly loop

The current operating loop is:

```text
PrecapWeek
  -> PrecapNextDay
  -> execution and evidence capture
  -> FlowRecap
  -> StatusMerge / Project KB update
  -> ProjectStatus
  -> next planning cycle
```

Load only the index records and source files required for the current task. Do not ingest the entire `OperatorResearch/` folder by default.

## Index package location

All maintained weekly-orchestration index artifacts belong in:

```text
apex-meta/kb/Weekly-Orchestrator/indexes/
```

Expected canonical files:

- `weekly-orchestration-master-index-v3.md`
- `weekly-orchestration-master-index-v3.yaml`
- `weekly-orchestration-master-index-v3.jsonl`

If one or more expected files are absent, treat this entrypoint as valid but the index package as incomplete; use `OperatorResearch/` plus the live skill packages until the missing artifacts are restored.
