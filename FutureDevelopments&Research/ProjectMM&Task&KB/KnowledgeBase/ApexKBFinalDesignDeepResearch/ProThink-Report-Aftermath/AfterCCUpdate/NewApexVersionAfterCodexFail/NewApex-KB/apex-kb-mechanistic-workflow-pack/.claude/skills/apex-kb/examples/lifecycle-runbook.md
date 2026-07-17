# Apex KB v2 Operator Runbook

## 1. Start

```text
/apex-kb start
```

Result: fixed welcome plus the exact `run-config.okf.json` shape.

## 2. Save configuration

Save the completed file at the future KB root or another explicit path.

```text
/apex-kb start --config <path-to-run-config.okf.json>
```

Result: schema validation and read-only preflight. A clean run returns a compact `READY_TO_LOCK` readback. No source intake or Phase 0 has run.

## 3. Confirm

Run the exact confirmation command returned in `operator_action`. Do not paraphrase it.

Result: `run-manifest.json`, configuration hash, and `run-state.json`.

## 4. Continue deterministic work

```text
/apex-kb continue --kb-root <kb-root>
```

The command continues until it needs operator input or a semantic executor.

## 5. Execute semantic task

Use the exact trigger returned. The executor reads the batch guide, generated instruction file, stable prompt template, and only the named evidence. After writing the exact outputs, it returns the exact completion response.

## 6. Reconcile

```text
/apex-kb continue --kb-root <kb-root>
```

The control plane validates output. It emits a next batch, Phase 2 task, repair task, acceptance task, postflight, or completion.

## 7. Status or repair

```text
/apex-kb status --kb-root <kb-root>
/apex-kb repair --kb-root <kb-root>
```

Use only the returned exact next action. Existing-KB updates are not part of this runbook.
