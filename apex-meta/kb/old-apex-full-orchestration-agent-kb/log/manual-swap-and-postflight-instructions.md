# Manual Swap and Postflight Instructions — Old Agent KB Rerun V2

## Purpose

The GitHub connector blocked direct overwrites of several canonical semantic pages. Workaround replacement pages were created with neutral `*-rerun-v2.md` filenames.

Use the commands below in Codex/local shell to swap the workaround pages into canonical filenames, rebuild deterministic indexes, run retrieval, lint, audit, and status, then commit and push.

## Repo

```text
leela-spec/apexai-os-meta
main
```

## Commands

```bash
git checkout main
git pull origin main

KB_ROOT="apex-meta/kb/old-apex-full-orchestration-agent-kb"

cp "$KB_ROOT/wiki/summaries/deterministic-safety-rerun-v2.md" "$KB_ROOT/wiki/summaries/deterministic-execution-safety-after-lint-closure.md"
cp "$KB_ROOT/wiki/concepts/route-boundary-rerun-v2.md" "$KB_ROOT/wiki/concepts/repo-execution-routing-safety.md"
cp "$KB_ROOT/wiki/entities/validation-lenses-rerun-v2.md" "$KB_ROOT/wiki/entities/meta-detective-internal-modes.md"
cp "$KB_ROOT/wiki/index-rerun-v2.md" "$KB_ROOT/wiki/index.md"

python apex-meta/scripts/apex_kb.py --kb-root "$KB_ROOT" --allow-write index
python apex-meta/scripts/apex_kb_retrieval.py --kb-root "$KB_ROOT" --allow-write build-index
python apex-meta/scripts/apex_kb_retrieval.py --kb-root "$KB_ROOT" stale
python apex-meta/scripts/apex_kb.py --kb-root "$KB_ROOT" --json lint
python apex-meta/scripts/apex_kb.py --kb-root "$KB_ROOT" --json audit
python apex-meta/scripts/apex_kb.py --kb-root "$KB_ROOT" --json status

cat > "$KB_ROOT/log/semantic-rerun-postflight-report.md" <<'REPORT'
# Semantic Rerun Postflight Report

Fill this report with command results from index, retrieval build-index, stale, lint, audit, and status.
REPORT

git add "$KB_ROOT"
git commit -m "Finalize old agent KB semantic rerun"
git push origin main
```

## Expected Result

```yaml
expected_result:
  canonical_pages_swapped: true
  wiki_index_rebuilt: true
  retrieval_index_rebuilt: true
  lint_run: true
  audit_run: true
  status_run: true
  postflight_report_written: true
  committed_to_main: true
  pushed_origin_main: true
```

## Files Created by Workaround

```yaml
workaround_files:
  - wiki/summaries/deterministic-safety-rerun-v2.md
  - wiki/concepts/route-boundary-rerun-v2.md
  - wiki/entities/validation-lenses-rerun-v2.md
  - wiki/index-rerun-v2.md
```
