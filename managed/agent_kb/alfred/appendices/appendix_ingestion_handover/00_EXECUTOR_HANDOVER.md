# Alfred Appendix Ingestion — Executor Handover

## Mission

Create a strict, machine-readable canonical scaffold patch from the Alfred appendices.

This handover does **not** apply the canonical KB edits. It provides per-file unified diff proposals and execution rules for another chat or local executor.

## Source basis

- `managed/agent_kb/alfred/appendices/APPENDIX_ROUTING_MATRIX.md`
- `managed/agent_kb/alfred/appendices/APPENDIX_WORKFLOW_PLAYBOOK.md`
- `managed/agent_kb/alfred/appendices/APPENDIX_PROCESS_HANDOVER_PRIORITY.md`
- `managed/agent_kb/alfred/appendices/APPENDIX_DAILY_COMMAND_BOARD_AND_HANDOFFS.md`
- `managed/agent_kb/alfred/appendices/APPENDIX_SESSION_EXPORT_OPSTATE_AND_TRACKING.md`
- `managed/agent_kb/alfred/appendices/APPENDIX_PATTERN_LEARNING_AND_RHYTHM.md`

## Attached audit basis

- `ANalysis.md`: appendix-to-scaffold ingestion map.
- `KB_SYSTEM_RELIABILITY_AUDIT_V1.txt`: machine-contract requirements.

Key machine-contract constraint: the KB needs a hard machine-executable control layer, not just human-readable doctrine. Critical recommendations must map to file owners, P0/P1 issues must have blocking rules, patch proposals must include exact paths, and prose-only critical rules should be converted into structured contracts.

## Target scaffold files

Apply only to these files:

```text
managed/agent_kb/alfred/ESSENCE.md
managed/agent_kb/alfred/BEST_PRACTICES.md
managed/agent_kb/alfred/MISTAKES.md
managed/agent_kb/alfred/TEMPLATES.md
managed/agent_kb/alfred/LEARNING_QUEUE.md
managed/agent_kb/alfred/SOURCE_MANIFEST.md
managed/agent_kb/alfred/COVERAGE_AUDIT.md
managed/agent_kb/alfred/README.md
```

Do not edit:

```text
managed/agent_kb/alfred/appendices/*.md
managed/agent_kb/alfred/appendices/cleanup_patch_proposals/**
managed/processes/AGENT_HANDOFF_CONTRACTS.md
```

## Apply order

```text
0001_TEMPLATES.diff
0002_LEARNING_QUEUE.diff
0003_MISTAKES.diff
0004_BEST_PRACTICES.diff
0005_ESSENCE.diff
0006_SOURCE_MANIFEST.diff
0007_COVERAGE_AUDIT.diff
0008_README.diff
```

## Machine-readability rules

Every patch must preserve or add:

```yaml
machine_contract:
  exact_target_path: required
  file_owner: required
  authority_status: required
  source_basis: required
  source_status: required
  allowed_writes: explicit
  forbidden_writes: explicit
  stop_conditions: required
  validation_gate: diff_based
  candidate_truth_boundary: explicit
```

## Validation gates

Before applying each file patch:

```powershell
git status --short
git checkout main
git pull origin main
```

After applying each file patch:

```powershell
git diff --check
git diff -- managed/agent_kb/alfred/<TARGET>.md
git add managed/agent_kb/alfred/<TARGET>.md
git commit -m "Ingest Alfred appendix material into <TARGET>"
```

After all patches:

```powershell
git status --short
git log --oneline -8
```

## Stop conditions

Stop immediately if:

- a patch wants to rewrite a full file instead of bounded inserts,
- a target file differs from expected anchors,
- `git diff --check` fails,
- a patch tries to edit appendices as doctrine,
- a patch hardens unread local/manual Leela mechanics,
- a candidate becomes accepted truth without promotion,
- a cleanup/proposal artifact is treated as doctrine,
- a machine-contract field is missing from a new critical section.

## No-patch reasons

- Do not copy whole appendix schemas into `ESSENCE.md`.
- Do not add Daily Board, Session Export, or Pattern Candidate detail to runtime doctrine beyond compact boundaries.
- Do not change process-level handoff authority in `managed/processes/AGENT_HANDOFF_CONTRACTS.md` from this pass.
- Do not delete the appendices in this pass.
- Do not delete `cleanup_patch_proposals/` in this pass.

## Executor note

The diff files in this folder are intended as controlled unified patch proposals. If a hunk does not apply because the target evolved, regenerate the hunk against current `main` rather than manually guessing.
