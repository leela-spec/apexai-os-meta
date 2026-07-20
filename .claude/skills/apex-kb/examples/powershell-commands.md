# Apex KB PowerShell Commands

```powershell
# Repository root containing the source corpus.
$REPO="C:\GitDev\leela"
$CONFIG="tmp\apex-kb-start.yaml"

# New KB Setup configuration. Replace every placeholder with operator-approved values.
@"
repository: leela-spec/leela
source_folders:
  - LeelaAppDevelopment
exclusions: []
kb_destination:
  folder: <operator-confirmed-kb-folder>
topics:
  - name: <topic-name>
    phrases:
      - <strong-phrase>
    ambiguous_or_negative_terms: []
    questions:
      - "<target-question>"
run_options:
  source_handling: pointer_only
  semantic_depth: standard
  output: analysis_only
  non_text: inventory_and_report
  ai_help_after_preflight: false
"@ | Set-Content -Encoding UTF8 $CONFIG

# Mandatory preview. This must create no KB destination or KB file.
python apex-meta/scripts/apex_kb.py start --config $CONFIG --repo-root $REPO --json --dry-run

# Only after operator approval of the submitted and derived readback.
python apex-meta/scripts/apex_kb.py start --config $CONFIG --repo-root $REPO --json --allow-write

# For a Setup-only run, stop here before deterministic corpus intelligence.
# The following commands are for a later continuation or an existing controlled KB.
$KB="$REPO\<operator-confirmed-kb-folder>"

# Canonical state derives the next legal action.
python apex-meta/scripts/apex_kb.py --kb-root $KB --json control next
python apex-meta/scripts/apex_kb.py --kb-root $KB --allow-write --json control run

# At a semantic stage, send only the returned packet trigger. Then reconcile files.
python apex-meta/scripts/apex_kb.py --kb-root $KB --allow-write --json control reconcile

# Recovery and Git classification are read-only unless input drift is explicitly accepted.
python apex-meta/scripts/apex_kb.py --kb-root $KB --json control status
python apex-meta/scripts/apex_kb.py --kb-root $KB --json control git-state
python apex-meta/scripts/apex_kb.py --kb-root $KB --json control reconcile
# Only after reviewing changed paths:
python apex-meta/scripts/apex_kb.py --kb-root $KB --allow-write --json control reconcile --accept-input-change

# Index and retrieval after the controlled lifecycle reaches those stages.
python apex-meta/scripts/apex_kb.py --kb-root $KB --allow-write --json index
python apex-meta/scripts/apex_kb_retrieval.py --kb-root $KB --json health
python apex-meta/scripts/apex_kb_retrieval.py --kb-root $KB --allow-write --json build-index
python apex-meta/scripts/apex_kb_retrieval.py --kb-root $KB --json stale
python apex-meta/scripts/apex_kb_retrieval.py --kb-root $KB --allow-write --json query --query "<query>" --limit 8 --save

# Maintenance.
python apex-meta/scripts/apex_kb.py --kb-root $KB --json lint --strict
python apex-meta/scripts/apex_kb.py --kb-root $KB --json audit
python apex-meta/scripts/apex_kb.py --kb-root $KB --json status
python apex-meta/scripts/apex_kb.py --kb-root $KB --json health

# Clear derived search index only.
python apex-meta/scripts/apex_kb_retrieval.py --kb-root $KB --allow-write --json clear-index --confirm-clear-index "clear derived search index"
```
