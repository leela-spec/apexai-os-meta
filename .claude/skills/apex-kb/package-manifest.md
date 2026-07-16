# Apex KB Package Manifest

```yaml
package_manifest:
  package_name: apex-kb
  package_path: .claude/skills/apex-kb/
  package_role: durable_knowledge_base_compiler
  data_root_template: apex-meta/kb/<kb-slug>/
  script_paths:
    lifecycle: apex-meta/scripts/apex_kb.py
    control_plane: apex-meta/scripts/apex_kb_control.py
    retrieval: apex-meta/scripts/apex_kb_retrieval.py
  runtime_policy:
    python_version_floor: "3.10"
    required_dependency: Python standard library
    network_access: forbidden
    shell_out:
      default: forbidden
      read_only_exceptions: [phase0_git_history, control_git_status_classification]
    default_mode: dry_run
    writes_require: --allow-write
    writes_outside_kb_root: forbidden
```

## Inventory


| Path | Role |
|---|---|
| `SKILL.md` | Skill entrypoint and operating procedure |
| `package-manifest.md` | Package inventory and scope |
| `references/run-intent.schema.json` | Operator-owned compact run configuration and confirmation schema |
| `references/run-state.schema.json` | Machine-owned lifecycle state, transition, blocker, artifact, and fingerprint schema |
| `references/stage-result.schema.json` | Compact result schema for every control action/stage |
| `references/semantic-handoff-packet.schema.json` | Exact semantic input/output/write/readback packet schema |
| `references/git-state.schema.json` | Read-only Git/worktree classification schema |
| `references/semantic-value-contract.md` | Completion target, registry v2, ledger, traceability, and acceptance contract |
| `references/browser-git-connector-semantic-runbook.md` | Connector-only compilation and clean-context evaluator workflow |
| `references/topic-registry-v2.schema.json` | Topic target-query and vocabulary schema |
| `references/semantic-run-ledger.schema.json` | Per-topic semantic progress/source-use schema |
| `references/semantic-acceptance.schema.json` | Independent semantic acceptance schema |
| `references/query-eval-pack-v2.schema.json` | Query-eval v2 schema |
| `references/analysis-config.schema.json` | Optional per-KB Phase 0 signal activation (`auto\|on\|off`) |
| `references/topic-source-rankings.schema.json` | Exhaustive, tiered, field-separated Phase 0 ranking schema |
| `references/topic-work-pack.schema.json` | Bounded per-topic semantic-input (work pack) schema |
| `assets/repository-semantic-contract/` | Repository-local semantic authority copied by scaffold |
| `references/kb-contract.md` | KB data, source, page, and boundary contract |
| `references/script-command-contract.md` | Deterministic script command contract |
| `references/ingest-query-lint-audit-rules.md` | Operational rules for ingest/query/lint/audit |
| `references/retrieval-contract.md` | Retrieval, index, stale, and query-output contract |
| `references/acceptance-tests.md` | Local command-level and semantic-wiring fixtures |
| `references/knowledge-promotion-rules.md` | Source/candidate/doctrine/runtime promotion gate rules |
| `templates/run-intent-template.md` | Human projection for JSON-compatible run-intent frontmatter |
| `templates/semantic-handoff-packet-template.md` | Human projection for run-specific semantic packets |
| `templates/ingest-analysis-template.md` | Phase 1 query-linked analysis template |
| `templates/wiki-page-templates.md` | Phase 2 v2 answer-bearing page templates |
| `templates/query-output-template.md` | Query packet template |
| `templates/topic-work-pack-template.md` | Topic work pack (bounded L3 semantic input) shape |
| `templates/kb-schema-template.md` | Starter `kb-schema.md` |
| `templates/source-manifest-template.json` | Starter source manifest |
| `examples/powershell-commands.md` | PowerShell-first control-plane commands |
| `examples/lifecycle-runbook.md` | Operator lifecycle, semantic handoff, recovery, and postflight sequence |
| `../../../apex-meta/scripts/apex_kb_control.py` | Delegated control implementation loaded by the existing lifecycle CLI |
| `../../../apex-meta/scripts/tests/test_apex_kb_control.py` | Unit and synthetic lifecycle/recovery fixtures |
| `../../../apex-meta/scripts/tests/test_apex_kb_control_integration.py` | Existing-CLI delegation and direct-command compatibility fixtures |
## Canonical runtime KB paths

```yaml
required_runtime_paths:
  - README.md
  - kb-schema.md
  - manifests/run-intent.md
  - manifests/run-state.json
  - manifests/topic-registry.json
  - log/runs/<run-id>/packets/
  - log/runs/<run-id>/stage-results/
  - raw/articles/
  - raw/papers/
  - raw/notes/
  - raw/refs/
  - raw/other/
  - ingest-analysis/
  - wiki/index.md
  - wiki/concepts/
  - wiki/entities/
  - wiki/summaries/
  - manifests/source-manifest.json
  - manifests/phase0/
  - derived/search/
  - audit/resolved/
  - outputs/queries/
  - log/
```

## Canonical versus derived KB paths

```yaml
canonical_paths:
  - raw/
  - kb-schema.md
  - manifests/run-intent.md
  - manifests/run-state.json
  - manifests/topic-registry.json
  - manifests/source-manifest.json
  - manifests/source-payload-manifest.json
  - ingest-analysis/
  - wiki/
  - audit/
  - log/

derived_rebuildable_paths:
  - manifests/phase0/
  - derived/search/
  - outputs/queries/
```

## Scope exclusions

Apex KB does not own project planning, task status mutation, exact next-task ranking, dependency graph traversal, blocker scanning, task registry rebuilds, session handoff authoring outside the KB root, external contact, hosted retrieval, or public web research without operator request.

## Executability note

The skill folder is not executable by itself. It requires the repo-level scripts at `apex-meta/scripts/apex_kb.py`, `apex-meta/scripts/apex_kb_control.py`, and `apex-meta/scripts/apex_kb_retrieval.py`. Operators invoke only `apex_kb.py`; it delegates control state/transitions to `apex_kb_control.py` and retrieval to the existing retrieval engine.

## Lifecycle authority

`SKILL.md` is the operator behavior and semantic-ownership authority. The JSON schemas are the machine-shape authorities. `apex_kb_control.py` is the executable owner of legal transitions, next-command derivation, stage results, semantic packet paths, recovery, and read-only Git classification; `apex_kb.py` and `apex_kb_retrieval.py` remain the existing domain/runtime owners. The deprecated `references/lifecycle-state-machine.md` and the two unexecuted lint-spec files remain removed; this design does not recreate a competing prose state machine.

