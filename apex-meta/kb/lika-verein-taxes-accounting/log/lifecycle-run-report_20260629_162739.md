# Lifecycle Run Report

- Generated at: 2026-06-29T16:32:04Z
- KB root: `apex-meta/kb/lika-verein-taxes-accounting`

## Git state summary

- `git pull --ff-only origin main`: Already up to date from origin/main
- `git status --short` before run: (clean)
- Recent commits: 6eb930ca Add AWV Belegablage PDF conversion; 9997f7a6 Add Lika Verein PDF conversion outputs; 7a15ee22 Add missing Lika Verein source downloads

## Skill/script files loaded

- `.claude/skills/apex-kb/SKILL.md`
- `.claude/skills/apex-kb/package-manifest.md`
- `.claude/skills/apex-kb/references/kb-contract.md`
- `.claude/skills/apex-kb/references/script-command-contract.md`
- `.claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md`
- `.claude/skills/apex-kb/references/lifecycle-state-machine.md`
- `apex-meta/scripts/apex_kb.py --help`
- `apex-meta/scripts/apex_kb_retrieval.py --help`

## KB inventory summary

- Preflight inventory: `log/lifecycle-preflight-inventory_20260629_162739.md`
- Source manifest entries before delta generation: 35
- Raw source candidate scan count: 103

## Source manifest delta summary

- Delta file: `manifests/source-manifest-deltas/source-manifest-delta_20260629_162739.jsonl`
- Delta report: `manifests/source-history/source-manifest-delta-report_20260629_162739.json`
- Delta records created: 60
- Merge dry-run: additions=60, updates=0, unchanged=0, history_records_to_write=0
- Merge apply: additions=60, updates=0, unchanged=0, history_records_to_write=0

## PDF conversion state summary

- Baseline summary preserved: `manifests/pdf-transformations/pdf-transformation-summary_20260629_155320.json`
- Latest summary treated as current state: `manifests/pdf-transformations/pdf-transformation-summary_20260629_160032.json`
- No PDF conversion rerun was performed.

## Table-heavy PDF risk register

- `raw/refs/IHK-Niederbayern_Checkliste-Kleinbetragsrechnungen.md`: low text volume, low heading count, table-heavy conversion warning.
- `raw/refs/LfSt-Bayern_Merkblatt-Festveranstaltungen-2025.md`: table-heavy conversion warning.
- `raw/refs/AWV_Muster-Verfahrensdokumentation-Belegablage.md`: table-heavy conversion warning.

## Web-clutter candidate summary

- Markdown files scanned: 77
- Candidates written: 73
- Candidate JSONL: `audit/web-clutter-candidates_20260629_162739.jsonl`
- Audit report: `log/web-clutter-audit_20260629_162739.md`

## Phase 0 artifacts written

- `manifests/phase0/corpus-profile.md`
- `manifests/phase0/frontmatter-map.json`
- `manifests/phase0/heading-map.json`
- `manifests/phase0/keyword-hits.ndjson`
- `manifests/phase0/markdown-link-map.json`
- `manifests/phase0/phase0-navigation-report.md`
- `manifests/phase0/source-priority-candidates.md`
- `manifests/phase0/topic-file-map.json`

## Index/lint/audit/status results

- `pre-status`: returncode=0 summary=audit_item_count=0, command=status, exists=True, index_status=fresh, kb_root=C:\GitDev\apexai-os-meta\apex-meta\kb\lika-verein-taxes-accounting
- `pre-health`: returncode=0 summary=command=health, network_required=False, optional_modules={'frontmatter': True, 'markdown_it': True, 'yaml': True}, python_version=3.11.9, shell_out_used=False
- `pre-lint`: returncode=0 summary=status=pass
- `pre-audit`: returncode=0 summary=command=audit, groups={}, item_count=0, mutations=False
- `phase0-dry-run`: returncode=2 summary=usage: apex_kb.py [-h] --kb-root KB_ROOT [--json] [--dry-run] [--allow-write]
- `phase0-apply`: returncode=0 summary=artifact_count=8, command=phase0, dry_run=False, phase_boundary=no ingest-analysis, wiki semantic pages, embeddings, or vector stores created, source_file_count=103
- `web-clutter-audit`: returncode=0 summary=candidates=73, files_scanned=77
- `index-dry-run`: returncode=2 summary=usage: apex_kb.py [-h] --kb-root KB_ROOT [--json] [--dry-run] [--allow-write]
- `index-apply`: returncode=0 summary=command=index, dry_run=False, page_count=1, write={'changed': True, 'exists': True, 'path': 'wiki/index.md', 'written': True}
- `post-lint`: returncode=0 summary=status=pass
- `post-audit`: returncode=0 summary=command=audit, groups={}, item_count=0, mutations=False
- `post-status`: returncode=0 summary=audit_item_count=0, command=status, exists=True, index_status=fresh, kb_root=C:\GitDev\apexai-os-meta\apex-meta\kb\lika-verein-taxes-accounting
- `retrieval-health`: returncode=0 summary=command=health, derived_search_dir=C:\GitDev\apexai-os-meta\apex-meta\kb\lika-verein-taxes-accounting\derived\search, kb_root=C:\GitDev\apexai-os-meta\apex-meta\kb\lika-verein-taxes-accounting, kb_root_exists=True, optional_modules={'frontmatter': True, 'markdown_it': True, 'yaml': True}
- `retrieval-stale`: returncode=0 summary=status=fresh
- `phase0-dry-run-valid-order`: returncode=0 summary=artifact_count=8, command=phase0, dry_run=True, phase_boundary=no ingest-analysis, wiki semantic pages, embeddings, or vector stores created, source_file_count=103, source_inventory={'csv_entry_count': 0, 'csv_exists': False, 'csv_path': 'manifests/source-inventory.csv', 'csv_readable': False, 'errors': [], 'json_entry_count': 0, 'json_exists': False, 'json_path': 'manifests/source-inventory.json', 'json_readable': False}
- `index-dry-run-valid-order`: returncode=0 summary=command=index, dry_run=True, page_count=1, write={'changed': True, 'exists': True, 'path': 'wiki/index.md', 'written': False}

## Files intentionally not modified

- `wiki/summaries/*`
- `wiki/concepts/*`
- `wiki/entities/*`
- `outputs/queries/*`
- Apex Plan, Apex Sync, Apex Session, PreCap, FlowRecap, APSU/status-merge, and personal orchestration state.

## Problems found

- Installed phase0 command did not emit a source-inventory* artifact; its JSON output reports source_inventory paths as absent.
- The requested dry-run argument order is rejected by the installed argparse surface; valid installed ordering (--dry-run before subcommand) was rerun successfully.
- Retrieval index generation was not forced because the wiki contains only wiki/index.md and no compiled summaries/concepts/entities yet; retrieval health/stale were run read-only.

## Recommended deterministic script improvements

```yaml
future_script_improvement:
  add command: apex_kb.py web-clutter-audit
  role: detect noisy web captures before semantic ingest
  output: audit/web-clutter-candidates_20260629_162739.jsonl
  non_goal: automatic deletion or semantic cleanup
```

## Stop condition

Stopped before LLM semantic ingest/wiki work. No wiki pages, semantic summaries, concept pages, entity pages, contradiction interpretations, query answers, or semantic audit items from claims were generated.

Deterministic lifecycle preparation complete. The next step is LLM-owned Phase 1 ingest analysis. Phase 2 wiki creation remains blocked until: approve ingest

