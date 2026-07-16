---
{{RUN_INTENT_JSON}}
---

# Apex KB Run Intent

This file is the operator-owned run configuration. The JSON-compatible YAML frontmatter is canonical. `manifests/run-state.json` is the machine-owned progress record; do not place machine stage progress here.

## Operator readback

A deterministic `control run` at `intent_lock` writes the exact readback to `log/runs/{{RUN_ID}}/operator-readback.md` and records topic-sanity results in this frontmatter. Confirm only after reading that artifact.

## Ownership

- Operator or authorized assistant: intent, scope, output tier, execution route, topic lock, confirmation quote.
- Control plane: validation only; it may record topic-sanity evidence and confirmation metadata, but it does not reinterpret intent.
- Semantic executor: no writes to this file.
