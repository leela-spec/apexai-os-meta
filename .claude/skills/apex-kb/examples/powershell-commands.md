# Apex KB PowerShell Commands

```powershell
# Repo root
cd C:\GitDev\apexai-os-meta

# Choose one KB root. Do not rely on a silent default.
$KB="apex-meta/kb/<kb-slug>"

# Write-enabled commands use `--allow-write` as a global flag before the subcommand.
# Do not put `--allow-write` after the subcommand.

# 1. Scaffold preview, then write.
python apex-meta/scripts/apex_kb.py --kb-root $KB --json scaffold --title "<Topic Title>"
python apex-meta/scripts/apex_kb.py --kb-root $KB --allow-write --json scaffold --title "<Topic Title>"

# 2. Source intake.
python apex-meta/scripts/apex_kb.py --kb-root $KB --json hash --path "path\to\source.md"
python apex-meta/scripts/apex_kb.py --kb-root $KB --allow-write --json source-intake --source-path "path\to\source.md" --source-type note --storage-mode copy_into_kb --source-id "<source-id>"

# 3. Deterministic preflight and Phase 0.
python apex-meta/scripts/apex_kb.py --kb-root $KB --json preflight --source-path "path\to\source.md"
python apex-meta/scripts/apex_kb.py --kb-root $KB --allow-write --json phase0

# 4. Phase 1 shell. LLM fills semantic analysis and stops.
python apex-meta/scripts/apex_kb.py --kb-root $KB --allow-write --json ingest-phase1 --source-path "path\to\source.md" --source-slug "<source-slug>"

# 5. Phase 2 gate validation. Wiki drafting is LLM-owned after approval.
python apex-meta/scripts/apex_kb.py --kb-root $KB --json ingest-phase2 --analysis "<source-slug>.analysis.md" --approval-phrase "approve ingest"

# 6. Index and retrieval.
python apex-meta/scripts/apex_kb.py --kb-root $KB --allow-write --json index
python apex-meta/scripts/apex_kb_retrieval.py --kb-root $KB --json health
python apex-meta/scripts/apex_kb_retrieval.py --kb-root $KB --allow-write --json build-index
python apex-meta/scripts/apex_kb_retrieval.py --kb-root $KB --json stale
python apex-meta/scripts/apex_kb_retrieval.py --kb-root $KB --allow-write --json query --query "<query>" --limit 8 --save

# 7. Maintenance.
python apex-meta/scripts/apex_kb.py --kb-root $KB --json lint --strict
python apex-meta/scripts/apex_kb.py --kb-root $KB --json audit
python apex-meta/scripts/apex_kb.py --kb-root $KB --json status
python apex-meta/scripts/apex_kb.py --kb-root $KB --json health

# 8. Clear derived search index only.
python apex-meta/scripts/apex_kb_retrieval.py --kb-root $KB --allow-write --json clear-index --confirm-clear-index "clear derived search index"
```
