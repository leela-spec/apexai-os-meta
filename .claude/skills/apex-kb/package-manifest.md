# Apex KB Package Manifest

```yaml
package_manifest:
  package_name: apex-kb
  package_path: .claude/skills/apex-kb/
  package_role: durable_knowledge_base_compiler
  data_root_template: apex-meta/kb/<kb-slug>/
  script_paths:
    lifecycle: apex-meta/scripts/apex_kb.py
    retrieval: apex-meta/scripts/apex_kb_retrieval.py
  runtime_policy:
    python_version_floor: "3.10"
    required_dependency: Python standard library
    network_access: forbidden
    shell_out: forbidden
    default_mode: dry_run
    writes_require: --allow-write
    writes_outside_kb_root: forbidden
```

## Inventory


| Path | Role |
|---|---|
| `SKILL.md` | Skill entrypoint and operating procedure |
| `package-manifest.md` | Package inventory and scope |
| `references/semantic-value-contract.md` | Completion target, registry v2, ledger, traceability, and acceptance contract |
| `references/browser-git-connector-semantic-runbook.md` | Connector-only compilation and clean-context evaluator workflow |
| `references/topic-registry-v2.schema.json` | Topic target-query schema |
| `references/semantic-run-ledger.schema.json` | Per-topic semantic progress/source-use schema |
| `references/semantic-acceptance.schema.json` | Independent semantic acceptance schema |
| `references/query-eval-pack-v2.schema.json` | Query-eval v2 schema |
| `assets/repository-semantic-contract/` | Repository-local semantic authority copied by scaffold |
| `references/kb-contract.md` | KB data, source, page, and boundary contract |
| `references/script-command-contract.md` | Deterministic script command contract |
| `references/ingest-query-lint-audit-rules.md` | Operational rules for ingest/query/lint/audit |
| `references/retrieval-contract.md` | Retrieval, index, stale, and query-output contract |
| `references/lifecycle-state-machine.md` | Deprecated historical reference; never operational authority |
| `references/acceptance-tests.md` | Local command-level and semantic-wiring fixtures |
| `references/knowledge-promotion-rules.md` | Source/candidate/doctrine/runtime promotion gate rules |
| `references/repo-execution-router-lint-spec.md` | Repo execution route lint spec |
| `references/historical-path-authority-lint-spec.md` | Legacy path/current authority lint spec |
| `templates/ingest-analysis-template.md` | Phase 1 query-linked analysis template |
| `templates/wiki-page-templates.md` | Phase 2 v2 answer-bearing page templates |
| `templates/query-output-template.md` | Query packet template |
| `templates/kb-schema-template.md` | Starter `kb-schema.md` |
| `templates/source-manifest-template.json` | Starter source manifest |
| `examples/powershell-commands.md` | PowerShell local commands |
| `examples/lifecycle-runbook.md` | Example-only terminal-backed lifecycle sequence |
## Canonical runtime KB paths

```yaml
required_runtime_paths:
  - README.md
  - kb-schema.md
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

The skill folder is not executable by itself. It requires the repo-level scripts at `apex-meta/scripts/apex_kb.py` and `apex-meta/scripts/apex_kb_retrieval.py` for deterministic lifecycle, validation, and retrieval operations.

## Lifecycle authority

`SKILL.md` is the single operational lifecycle authority. `references/lifecycle-state-machine.md` is retained only as deprecated historical/reference material and must not introduce independent completion states or transitions. Runtime command behavior remains authoritative in the scripts and command contract.

