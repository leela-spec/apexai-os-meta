# ProjectRepos Target Work

This folder is the usable prework package for scanning and selecting files from
`source-knowledge/ProjectRepos`.

## Primary Files To Read First

1. `llm-routing-packet.md`
2. `candidate-files.md`
3. `scan-run-summary.json`
4. `candidate-files.json`
5. `keyword-hits.ndjson`

Use `corpus-inventory.ndjson` only when you need whole-corpus file coverage.
Use `structure-map.ndjson` when you need headings, frontmatter keys, links,
wikilinks, and code-block spans for ranked candidate files.

## What This Scan Proves

- The full ProjectRepos source root was inventoried.
- The scan found 41,138 files.
- 37,174 files looked textual enough to consider.
- 638 files were binary/assets.
- 2,000 candidate files were selected, read, parsed, and hash-recorded under the
  configured 1 MiB per-file byte limit.
- The largest skipped text files are listed in `scan-run-summary.json`.

## Recommended Next Action

Create a curated allowlist from `candidate-files.md`, starting with:

- `SKILL.md` files with high scores.
- Skill design docs and references.
- Prompt, workflow, agent, MCP/tooling, memory, and evaluation files.
- Package manifests only when they explain package boundaries.

Do not bulk-copy ProjectRepos. Do not import binaries/assets. Do not ingest the
large JSON catalogs directly until a schema-specific extractor is chosen.

## Follow-up Command

For a deeper second pass after reviewing the first 2,000 candidates:

```powershell
python apex-meta/scripts/large_corpus_prework.py `
  --source-root source-knowledge/ProjectRepos `
  --output-root apex-meta/kb/claude-skill-design/manifests/large-corpus-prework-projectrepos-deeper `
  --mode full `
  --profile deep `
  --max-files 0 `
  --max-candidates 5000 `
  --max-bytes-per-file 1048576 `
  --max-structure-lines 8000 `
  --hash-candidates `
  --json
```

Run this only if the current 2,000-candidate report is too narrow.
