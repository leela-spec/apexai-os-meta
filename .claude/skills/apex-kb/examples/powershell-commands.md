# Apex KB PowerShell Commands

```powershell
# Repo root
cd C:\GitDev\apexai-os-meta

# Choose one KB root. Do not rely on a silent default.
$KB="apex-meta/kb/<kb-slug>"

# Git Bash is preferred for deterministic redirect/pipe-heavy validation when available.
# PowerShell examples remain supported.
# `--allow-write`, `--json`, `--dry-run`, and `--strict` may be placed before or after the subcommand.

# 0. Step 0 - Intake and intent lock (see SKILL.md). Do this BEFORE the expensive steps.
#    0a Intake Q&A (chat): operator_intent, kb_identity, source_locus + out-of-scope,
#       success_definition. 0b lock topic-registry.json. Then create the empty skeleton
#       (cheap, registers no sources) so the manifests dir exists:
python apex-meta/scripts/apex_kb.py --kb-root $KB --json scaffold --title "<Topic Title>"
python apex-meta/scripts/apex_kb.py --kb-root $KB --allow-write --json scaffold --title "<Topic Title>"

# 1. 0c Topic-scope validation input - feeds the 0d read-back, not a standalone stop.
python apex-meta/scripts/apex_kb.py --kb-root $KB --json topic-sanity-check --topic-slug "<topic-slug>"

# 2. 0d Read-back + operator confirmation (chat), then record it. The read-back states
#    kb_identity, mode, source_locus/out-of-scope, RECOMMENDED tier/route/breadth (one-line
#    why each), topic_slugs, and the 0c verdict. Only after the operator's explicit "yes",
#    write manifests/run-intent.md with operator_confirmed: true and the verbatim affirmative.
#    NOTHING below runs until manifests/run-intent.md shows operator_confirmed: true.

# 3. Source intake (gated on operator_confirmed: true). Breadth defaults to narrow.
python apex-meta/scripts/apex_kb.py --kb-root $KB --json hash --path "path\to\source.md"
python apex-meta/scripts/apex_kb.py --kb-root $KB --allow-write --json source-intake --source-path "path\to\source.md" --source-type note --storage-mode copy_into_kb --source-id "<source-id>"

# 4. Deterministic preflight, payload manifest, and Phase 0 (gated on operator_confirmed: true).
python apex-meta/scripts/apex_kb.py --kb-root $KB --json preflight --source-path "path\to\source.md"
python apex-meta/scripts/apex_kb.py --kb-root $KB generate-source-payload-manifest --allow-write --json
python apex-meta/scripts/apex_kb.py --kb-root $KB phase0 --allow-write --json
# Phase 0 also writes manifests/phase0/topic-source-rankings.json (exhaustive, tiered, no top-N
# cutoff) and manifests/phase0/work-packs/<topic-slug>.md (the bounded semantic input for that
# topic). Start semantic reading from the work pack, not the full ranking map.

# 5. Phase 1 shell - one file per topic (never per source). LLM fills semantic
# analysis and stops. Run again with a different --source-path/--source-slug
# under the same --topic-slug to append that source's record to the same file.
python apex-meta/scripts/apex_kb.py --kb-root $KB --allow-write --json ingest-phase1 --source-path "path\to\source.md" --topic-slug "<topic-slug>" --source-slug "<source-id>"

# 6. Phase 2 gate validation. Wiki drafting is LLM-owned after approval.
python apex-meta/scripts/apex_kb.py --kb-root $KB --json ingest-phase2 --analysis "<topic-slug>.analysis.md" --approval-phrase "approve ingest"

# 7. Index and retrieval.
python apex-meta/scripts/apex_kb.py --kb-root $KB --allow-write --json index
python apex-meta/scripts/apex_kb_retrieval.py --kb-root $KB --json health
python apex-meta/scripts/apex_kb_retrieval.py --kb-root $KB --allow-write --json build-index
python apex-meta/scripts/apex_kb_retrieval.py --kb-root $KB --json stale
python apex-meta/scripts/apex_kb_retrieval.py --kb-root $KB --allow-write --json query --query "<query>" --limit 8 --save

# 8. Maintenance.
python apex-meta/scripts/apex_kb.py --kb-root $KB --json lint --strict
python apex-meta/scripts/apex_kb.py --kb-root $KB --json audit
python apex-meta/scripts/apex_kb.py --kb-root $KB --json status
python apex-meta/scripts/apex_kb.py --kb-root $KB --json health

# 8. Clear derived search index only.
python apex-meta/scripts/apex_kb_retrieval.py --kb-root $KB --allow-write --json clear-index --confirm-clear-index "clear derived search index"
```
