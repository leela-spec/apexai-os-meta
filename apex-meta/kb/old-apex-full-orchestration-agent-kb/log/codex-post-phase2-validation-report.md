# Codex Post-Phase-2 Validation Report - old-apex-full-orchestration-agent-kb

```yaml
verdict: PASS
kb_root: apex-meta/kb/old-apex-full-orchestration-agent-kb/
branch: main
created_at: "2026-07-03T11:15:40Z"
phase2_report_present: true
phase2_report_pass: true
wiki_index_present: true
all_indexed_pages_present: true
scripts_discovered:
  apex_kb_py: true
  apex_kb_retrieval_py: true
commands_run:
  - "git fetch --all --prune"
  - "git checkout origin/main -- apex-meta/kb/old-apex-full-orchestration-agent-kb"
  - "python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/old-apex-full-orchestration-agent-kb status"
  - "python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/old-apex-full-orchestration-agent-kb health"
  - "python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/old-apex-full-orchestration-agent-kb lint"
  - "python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/old-apex-full-orchestration-agent-kb audit"
  - "python apex-meta/scripts/apex_kb_retrieval.py --kb-root apex-meta/kb/old-apex-full-orchestration-agent-kb --allow-write build-index"
  - "python apex-meta/scripts/apex_kb_retrieval.py --kb-root apex-meta/kb/old-apex-full-orchestration-agent-kb stale"
  - "python apex-meta/scripts/apex_kb_retrieval.py --kb-root apex-meta/kb/old-apex-full-orchestration-agent-kb query --query \"validator executor separation\" --limit 3"
  - "python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/old-apex-full-orchestration-agent-kb --allow-write index"
  - "python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/old-apex-full-orchestration-agent-kb lint"
  - "python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/old-apex-full-orchestration-agent-kb status"
files_changed:
  - "apex-meta/kb/old-apex-full-orchestration-agent-kb/audit/semantic-open-questions.md"
  - "apex-meta/kb/old-apex-full-orchestration-agent-kb/derived/search/index-meta.json"
  - "apex-meta/kb/old-apex-full-orchestration-agent-kb/derived/search/index.sqlite"
  - "apex-meta/kb/old-apex-full-orchestration-agent-kb/derived/search/search-index.json"
  - "apex-meta/kb/old-apex-full-orchestration-agent-kb/derived/search/search-index.ndjson"
  - "apex-meta/kb/old-apex-full-orchestration-agent-kb/ingest-analysis/batch01-agent-kb-architecture.analysis.md"
  - "apex-meta/kb/old-apex-full-orchestration-agent-kb/ingest-analysis/batch02-agent-roles-and-doctrine.analysis.md"
  - "apex-meta/kb/old-apex-full-orchestration-agent-kb/ingest-analysis/batch03-handoffs-validation-and-risk.analysis.md"
  - "apex-meta/kb/old-apex-full-orchestration-agent-kb/ingest-analysis/batch04-reusable-patterns-and-migration.analysis.md"
  - "apex-meta/kb/old-apex-full-orchestration-agent-kb/ingest-analysis/phase1-completion-report.md"
  - "apex-meta/kb/old-apex-full-orchestration-agent-kb/log/codex-post-phase2-validation-report.md"
  - "apex-meta/kb/old-apex-full-orchestration-agent-kb/log/phase2-wiki-compile-report.md"
  - "apex-meta/kb/old-apex-full-orchestration-agent-kb/wiki/index.md"
  - "apex-meta/kb/old-apex-full-orchestration-agent-kb/wiki/concepts/agent-doctrine-and-promotion-patterns.md"
  - "apex-meta/kb/old-apex-full-orchestration-agent-kb/wiki/concepts/migration-safety-patterns.md"
  - "apex-meta/kb/old-apex-full-orchestration-agent-kb/wiki/concepts/validation-and-routing-guardrails.md"
  - "apex-meta/kb/old-apex-full-orchestration-agent-kb/wiki/entities/meta-detective-internal-modes.md"
  - "apex-meta/kb/old-apex-full-orchestration-agent-kb/wiki/entities/old-agent-roles.md"
  - "apex-meta/kb/old-apex-full-orchestration-agent-kb/wiki/entities/reusable-artifact-families.md"
  - "apex-meta/kb/old-apex-full-orchestration-agent-kb/wiki/summaries/handoff-validation-and-risk-doctrine.md"
  - "apex-meta/kb/old-apex-full-orchestration-agent-kb/wiki/summaries/migration-to-claude-native-orchestration.md"
  - "apex-meta/kb/old-apex-full-orchestration-agent-kb/wiki/summaries/old-agent-kb-architecture.md"
  - "apex-meta/kb/old-apex-full-orchestration-agent-kb/wiki/summaries/old-agent-role-system.md"
  - "apex-meta/kb/old-apex-full-orchestration-agent-kb/wiki/summaries/reusable-old-agent-kb-patterns.md"
warnings:
  - "Local main had diverged from origin/main, so only the target KB root was restored from origin/main instead of merging unrelated remote history."
  - "Initial retrieval query invocation without --query failed with argparse usage error, then succeeded with the documented --query flag."
failures: []
```

## Command Results

### Preflight

```text
branch: main
kb_root_exists: true
phase2_report_present: true
wiki_index_present: true
phase2_report markers:
  verdict: PASS
  approval_received: true
required wiki/audit files: all present
```

### Validation

```text
apex_kb status before rebuild:
  source_count: 2
  wiki_page_count: 12
  audit_item_count: 1
  index_status: stale
  phase0_artifacts_present: true
  search_index_present: false

apex_kb health:
  git: true
  rg: true
  sqlite fts5_available: true
  optional modules frontmatter/markdown_it/yaml: true

apex_kb lint before rebuild:
  status: warn
  issues: index stale

apex_kb audit:
  item_count: 1
  semantic-open-questions.md status: unknown
  mutations: false

apex_kb index:
  wiki/index.md written
  page_count: 12

apex_kb lint after rebuild:
  status: pass
  issue_count: 0

apex_kb status after rebuild:
  source_count: 2
  wiki_page_count: 12
  audit_item_count: 1
  index_status: fresh
  phase0_artifacts_present: true
  search_index_present: true
```

### Retrieval

```text
apex_kb_retrieval build-index:
  page_count: 11
  chunk_count: 66
  wrote:
    derived/search/search-index.json
    derived/search/search-index.ndjson
    derived/search/index-meta.json
    derived/search/index.sqlite
  sqlite fts5_available: true

apex_kb_retrieval stale:
  status: fresh
  added: []
  deleted: []
  modified: []

apex_kb_retrieval query --query "validator executor separation" --limit 3:
  backend: sqlite_fts5_bm25
  result_count: 3
  top_result: wiki/concepts/validation-and-routing-guardrails.md / Relationships
  fallback_error: None
```

## Final Status

Phase 2 report and compiled wiki pages are present on main after restoring the target KB root from origin/main. Deterministic lifecycle validation passes, the wiki index is fresh, retrieval artifacts were rebuilt, retrieval stale check is fresh, and the smoke query returned results.
