# Apex KB Script Command Contract v2

## Public operator surface

The operator uses four stable actions. Both terminal use and `/apex-kb` route to the same control plane.

```text
/apex-kb start [--kb-root <path>] [--config <run-config.okf.json>]
/apex-kb continue --kb-root <path>
/apex-kb status --kb-root <path>
/apex-kb repair --kb-root <path>
```

Canonical implementation form:

```text
python apex-meta/scripts/apex_kb.py --json control <action> [flags]
```

| Action | Behavior |
|---|---|
| `start` | With no config: return fixed welcome. With config: validate and run read-only preflight. |
| `continue` | Execute contiguous deterministic stages until operator input or a semantic executor is required. |
| `status` | Read-only state, hash, artifact, and exact-next-action report. |
| `repair` | Reconcile changed inputs or failed outputs; emit reason-coded repair instructions. |

## Internal actions

| Internal action | Writes | Purpose |
|---|---:|---|
| `preflight-config` | preflight report only | Validate schema, paths, overlap, runtime capabilities, and topic vocabulary. |
| `confirm-config` | yes | Compile and lock `run-manifest.json`; initialize `run-state.json`. |
| `render-semantic-instructions` | yes | Generate Phase 1/2 instruction files and handoff packet. |
| `reconcile` | yes | Validate exact outputs, writes, fingerprints, question coverage, and acceptance. |
| `doctor` | no | Validate schemas, templates, command dispatch, and package consistency. |

## Direct-command policy

For new v2 runs, direct mutation commands are prohibited even before run state exists. Legacy behavior requires an explicit `--legacy-direct` opt-out and must never be selected automatically.

## Standard result

Every action returns `apex.kb.stage-result.v2`. The JSON must contain the configuration hash, stage, status, reason code, human message, consumed/created artifacts, exact next command, operator action, semantic task references, and structured errors.

## Validation presentation

- Schema and preflight always execute.
- A clean pass returns one compact `READY_TO_LOCK` readback.
- Detailed successful checks are written to the preflight artifact but hidden from the default human message.
- Warnings and failures include exact field/path, reason code, and operator action.

## Write policy

- Deterministic scripts may write only within the selected KB root, except repository-owned skill/package files during explicit implementation work.
- Semantic executors may write only allowlisted packet outputs.
- Git operations are read-only classification unless the operator invokes a separate Git workflow.
- No stage infers a command from chat or prose.

## Exit codes

```yaml
exit_codes:
  0: success_or_expected_gate
  1: internal_script_error
  2: blocked_validation_or_contract_failure
```
