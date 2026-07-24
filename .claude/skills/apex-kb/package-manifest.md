# Apex KB Package Manifest

```yaml
package_manifest:
  package_name: apex-kb
  package_path: .claude/skills/apex-kb/
  package_role: durable_knowledge_base_compiler
  data_root_template: apex-meta/kb/<kb-slug>/
  installed_cli:
    entry_point: apex-kb            # console script -> apex_kb.cli:main
    package_path: apex-meta/apex-kb-cli
    commands: [start, status, continue, drive, query, doctor, update]
    machine_output: --json-output
  runtime_policy:
    python_version_floor: "3.10"
    dependencies: [click, jsonschema, PyYAML, pypdf]
    network_access: forbidden
    default_mode: read_only
    writes_require: explicit lifecycle action (continue/drive/update) or --yes on update
    writes_outside_run_root: forbidden
```

## Inventory


| Path | Role |
|---|---|
| `SKILL.md` | Skill entrypoint and operating procedure |
| `package-manifest.md` | Package inventory and scope |
| `references/start-input.schema.json` | Compact new-KB Start configuration schema |
| `references/start-workflow.md` | New-KB Setup routing, preview, confirmation, and handoff sequence |
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
| `templates/start-config-template.yaml` | Minimal operator-editable Start configuration |
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
| `../../../apex-meta/apex-kb-cli/` | The installed `apex-kb` CLI package (sole lifecycle authority) |
| `../../../apex-meta/apex-kb-cli/tests/` | CLI unit/integration/contract test suite |

> Note: several `references/*` files (e.g. `script-command-contract.md`, `acceptance-tests.md`) still describe the **superseded** legacy `apex_kb.py control` surface. They are retained only as history; the installed `apex-kb` CLI is authoritative, and independent semantic acceptance is disabled by default.
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

The skill folder is not executable by itself. It is a thin launcher around the **installed `apex-kb` CLI** (`apex-meta/apex-kb-cli`, console entry point `apex_kb.cli:main`). Install with `python -m pip install -e ".\apex-meta\apex-kb-cli[test]"`, then operators invoke the public commands `apex-kb start|status|continue|drive|query|doctor|update`. Deleting this skill must not affect direct CLI operation.

## Lifecycle authority

The **installed `apex-kb` CLI** is the sole lifecycle authority: it derives legal transitions, the next action, stage results, semantic-packet paths, retrieval, recovery, and read-only Git classification. `SKILL.md` is only the operator-behavior launcher; the JSON schemas under `references/` are shape references. The legacy `apex-meta/scripts/apex_kb*.py` surface is superseded and must not be treated as the operator workflow.

