# Apex KB PowerShell Commands

```powershell
# Repo root
cd C:\GitDev\apexai-os-meta

# Choose one KB root. Do not rely on a silent default.
$KB="apex-meta/kb/<kb-slug>"

# Git Bash is preferred for deterministic redirect/pipe-heavy validation when available.
# PowerShell examples remain supported.
# `--allow-write`, `--json`, `--dry-run`, and `--strict` may be placed before or after the subcommand.

# 0. Author manifests/topic-registry.json first. Then create one controlled run.
$RUN="<stable-run-id>"
python apex-meta/scripts/apex_kb.py --kb-root $KB --allow-write --json control init `
  --run-id $RUN `
  --mode compile `
  --operator-intent "<job to be done>" `
  --kb-identity "<this KB is about X>" `
  --source-locus "<bounded source location>" `
  --source-root "<path\to\bounded-source-root>" `
  --success-definition "<tier-specific success>" `
  --output-tier query_ready `
  --output-tier-rationale "<one line from operator intent>" `
  --execution-route terminal_backed `
  --corpus-breadth narrow `
  --topic-slug "<topic-slug>" `
  --target-repository "leela-spec/apexai-os-meta" `
  --target-commit "<verified-commit-sha>" `
  --title "<Topic Title>"

# 1. Execute the scaffold stage, then the intent-lock stage that writes the compact read-back.
python apex-meta/scripts/apex_kb.py --kb-root $KB --allow-write --json control run
python apex-meta/scripts/apex_kb.py --kb-root $KB --allow-write --json control run
Get-Content -Raw "$KB/log/runs/$RUN/operator-readback.md"

# 2. After the operator confirms that read-back, record the exact affirmative.
python apex-meta/scripts/apex_kb.py --kb-root $KB --allow-write --json control confirm --confirmation-quote "<verbatim affirmative>"

# 3. From here, never choose a low-level mutation command manually.
#    `next` returns one exact PowerShell-safe command or one short packet trigger.
python apex-meta/scripts/apex_kb.py --kb-root $KB --json control next
python apex-meta/scripts/apex_kb.py --kb-root $KB --allow-write --json control run

# 4. Repeat `control run` for deterministic stages. At a semantic stage it renders a packet and
#    returns status needs_semantic_executor. Send only the returned one-line trigger to the semantic
#    executor. After its required read-back/completion response, reconcile repository files.
python apex-meta/scripts/apex_kb.py --kb-root $KB --allow-write --json control reconcile

# 5. Recovery and Git classification are read-only unless input drift is explicitly accepted.
python apex-meta/scripts/apex_kb.py --kb-root $KB --json control status
python apex-meta/scripts/apex_kb.py --kb-root $KB --json control git-state
python apex-meta/scripts/apex_kb.py --kb-root $KB --json control reconcile
# Only after reviewing changed paths:
python apex-meta/scripts/apex_kb.py --kb-root $KB --allow-write --json control reconcile --accept-input-change

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
