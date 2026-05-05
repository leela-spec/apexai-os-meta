# Codex Apply Order and Validation — V2

## Scope

This is an execution instruction artifact only. It does not patch scaffold files.

Do not directly edit scaffold files. Codex should apply the V2 diff artifacts one at a time on `main`.

## Already applied

Codex reported that this artifact applied successfully with the approved workaround:

```text
managed/agent_kb/alfred/appendices/appendix_ingestion_handover/final_unified_diffs_v2/0001_ESSENCE__iter01.diff
```

Reported result:

- strict `git apply --check`: failed
- `git apply --check --recount -C0`: passed
- applied with `git apply --recount -C0`
- changed only `managed/agent_kb/alfred/ESSENCE.md`
- 11 insertions

Treat it as usable-with-workaround, not a pristine reusable patch.

## Remaining apply order

Apply and validate one file at a time. Stop on first failure.

```text
managed/agent_kb/alfred/appendices/appendix_ingestion_handover/final_unified_diffs_v2/0002_BEST_PRACTICES__iter01.diff
managed/agent_kb/alfred/appendices/appendix_ingestion_handover/final_unified_diffs_v2/0003_MISTAKES__iter01.diff
managed/agent_kb/alfred/appendices/appendix_ingestion_handover/final_unified_diffs_v2/0004_TEMPLATES_INDEX__iter01.diff
managed/agent_kb/alfred/appendices/appendix_ingestion_handover/final_unified_diffs_v2/0005_LEARNING_QUEUE__iter01.diff
managed/agent_kb/alfred/appendices/appendix_ingestion_handover/final_unified_diffs_v2/0006_SOURCE_MANIFEST__iter01.diff
managed/agent_kb/alfred/appendices/appendix_ingestion_handover/final_unified_diffs_v2/0007_COVERAGE_AUDIT__iter01.diff
managed/agent_kb/alfred/appendices/appendix_ingestion_handover/final_unified_diffs_v2/0008_README__iter01.diff
```

## Per-artifact command

For each artifact:

```bash
git checkout main
git pull

DIFF="<artifact-path>"

if git apply --check "$DIFF"; then
  git apply "$DIFF"
elif git apply --check --recount -C0 "$DIFF"; then
  git apply --recount -C0 "$DIFF"
else
  echo "FAILED: $DIFF"
  exit 1
fi

git diff --name-only
git diff --check
```

## Target lock expectations

Expected target per artifact:

| Artifact | Only allowed changed scaffold target |
|---|---|
| `0002_BEST_PRACTICES__iter01.diff` | `managed/agent_kb/alfred/BEST_PRACTICES.md` |
| `0003_MISTAKES__iter01.diff` | `managed/agent_kb/alfred/MISTAKES.md` |
| `0004_TEMPLATES_INDEX__iter01.diff` | `managed/agent_kb/alfred/TEMPLATES.md` |
| `0005_LEARNING_QUEUE__iter01.diff` | `managed/agent_kb/alfred/LEARNING_QUEUE.md` |
| `0006_SOURCE_MANIFEST__iter01.diff` | `managed/agent_kb/alfred/SOURCE_MANIFEST.md` |
| `0007_COVERAGE_AUDIT__iter01.diff` | `managed/agent_kb/alfred/COVERAGE_AUDIT.md` |
| `0008_README__iter01.diff` | `managed/agent_kb/alfred/README.md` |

If any artifact changes a different scaffold file, stop.

## Required post-apply scans

After all remaining artifacts apply:

```bash
grep -R "ALFRED-BP-" managed/agent_kb/alfred/BEST_PRACTICES.md | sort
grep -R "ALFRED-MF-" managed/agent_kb/alfred/MISTAKES.md | sort
grep -R "ALFRED-LQ-" managed/agent_kb/alfred/LEARNING_QUEUE.md | sort

grep -Rni "value / urgency / leverage / fit\|old metric\|superseded metric\|mapping table" managed/agent_kb/alfred || true

grep -Rni "Weekly Preview\|Monthly Direction Map" managed/agent_kb/alfred/TEMPLATES.md managed/agent_kb/alfred/templates managed/agent_kb/alfred/LEARNING_QUEUE.md || true

grep -Rni "cleanup_patch_proposals\|appendix_ingestion_handover" managed/agent_kb/alfred/README.md managed/agent_kb/alfred/SOURCE_MANIFEST.md managed/agent_kb/alfred/COVERAGE_AUDIT.md || true
```

Expected scan interpretation:

- `ALFRED-BP-024` through `ALFRED-BP-026` appear once in `BEST_PRACTICES.md`.
- `ALFRED-MF-024` through `ALFRED-MF-027` appear once in `MISTAKES.md`.
- `ALFRED-LQ-006` through `ALFRED-LQ-010` appear once in `LEARNING_QUEUE.md`.
- Old metric system language is not reintroduced as accepted doctrine.
- Weekly Preview and Monthly Direction Map are deferred/candidate-only, not operational runtime authority.
- Cleanup-bound folders are not permanent README navigation or doctrine source.

## Report format

```md
## V2 Apply Report

- Applied artifacts:
  - ...
- Workaround used:
  - artifact: yes/no
- Files changed:
  - ...
- Target lock: pass/fail
- Duplicate ID scan: pass/fail
- Metric drift scan: pass/fail
- Deferred item status: pass/fail
- Cleanup-bound reference status: pass/fail
- Remaining issues:
  - none / exact issue
```
