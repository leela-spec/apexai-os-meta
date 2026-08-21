# Installation and Operations Guide: obsidian-wiki

## 1. Machine Installation

### Prerequisites
- Python 3.10+ (tested on Python 3.12.10)
- `pip` package manager

### Installation Command
```bash
python -m pip install -U obsidian-wiki
```

### Windows Encoding Note
On Windows systems, ensure UTF-8 console output is enabled:
```powershell
$env:PYTHONUTF8="1"
```

## 2. Project Setup & Vault Initialization

### Setup Command
Initialize the canonical repository-associated knowledge vault:
```bash
python -m obsidian_wiki setup --vault "knowledge/transcript-wiki" --project . --copy
```

### Vault Verification
Run the system diagnostic suite:
```bash
python -m obsidian_wiki info
python -m obsidian_wiki doctor
```
`doctor` must report `obsidian-wiki doctor: pass` before continuing.

## 3. Daily Operations & Ingestion

### A. Checking Delta / Incremental Ingest
Check which transcript files need processing vs. those already cached:
```bash
python -m obsidian_wiki cache-check "knowledge/transcript-wiki" artifacts/transcript_pipeline_v4/*/transcript.txt --pretty
```

### B. Ingesting Transcripts (Agent-Assisted)
Through your AI coding agent (Claude Code, Antigravity, Codex, etc.), execute:
```
/wiki-ingest artifacts/transcript_pipeline_v4/<source_id>/transcript.txt
```
Or process the transcript directly adhering to the `wiki-ingest` specification:
1. Extract concepts, entities, and claims with provenance markers (`^[inferred]`, `^[ambiguous]`).
2. Write/update category pages in `knowledge/transcript-wiki/` with YAML frontmatter.
3. Update `.manifest.json` with `obsidian-wiki cache-update`:
```bash
python -m obsidian_wiki cache-update "knowledge/transcript-wiki" "artifacts/transcript_pipeline_v4/<source_id>/transcript.txt" --pages "concepts/page1.md" "entities/page2.md"
```
4. Rebuild `index.md`, append to `log.md`, and refresh `hot.md`.

### C. Vault Linting & Health Check
Verify vault link integrity, frontmatter conformance, and trust status:
```bash
python -m obsidian_wiki lint knowledge/transcript-wiki
```

To record reviewed trust levels for new pages:
```bash
python -m obsidian_wiki trust-record --all --reviewed-at "$(Get-Date -Format s)Z" --approved knowledge/transcript-wiki
```

### D. Querying Knowledge
Query the accumulated knowledge graph directly without reloading whole transcripts:
```bash
python -m obsidian_wiki query "What are the four operating features of emotion?" --pretty
```

## 4. Upgrade & Maintenance

### Upgrading the Package
```bash
python -m pip install -U obsidian-wiki
python -m obsidian_wiki doctor
```

### Re-running Unchanged Transcripts
Running an ingest on an unchanged source file will detect identical SHA-256 hashes and skip LLM processing automatically.

### In-Flight Failure Recovery
If an ingest operation is interrupted mid-file, the manifest hash is not updated until completion. Simply re-run the ingest command for that specific source file.
