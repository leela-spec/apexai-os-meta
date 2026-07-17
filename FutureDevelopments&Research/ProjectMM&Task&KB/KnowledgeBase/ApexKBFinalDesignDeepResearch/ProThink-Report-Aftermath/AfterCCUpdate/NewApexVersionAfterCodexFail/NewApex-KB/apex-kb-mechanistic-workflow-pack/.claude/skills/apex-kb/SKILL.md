---
name: apex-kb
description: Manually launch, continue, inspect, or repair the deterministic Apex KB control plane.
disable-model-invocation: true
argument-hint: "start|continue|status|repair [--kb-root <path>] [--config <path>]"
allowed-tools:
  - Bash(python apex-meta/scripts/apex_kb.py *)
---

# Apex KB launcher

Run exactly one control-plane command using the arguments supplied by the operator:

```text
python apex-meta/scripts/apex_kb.py --json control $ARGUMENTS
```

Treat the returned stage-result JSON as authoritative.

1. Display `message` and `operator_action` verbatim.
2. Never invent, rewrite, or paraphrase `next_command`.
3. Never select a lifecycle stage yourself.
4. Never call `scaffold`, `source-intake`, `phase0`, `ingest-phase1`, `ingest-phase2`, `index`, or `postflight` directly.
5. Do not open other Apex KB doctrine before the command runs.
6. If `status` is `blocked`, `failed`, or `needs_operator`, stop after displaying the exact result.
7. If `status` is `needs_semantic_executor`, display the exact packet trigger. Execute the packet only when the operator explicitly selects this session as that bounded semantic executor.
8. Do not infer completion from chat history. Only the returned state and artifacts count.

## TODO — separate existing-KB update lifecycle

Do not use the new-KB build flow to add later content, refresh stale pages, or build another topic against an existing KB. A separate `apex-kb update` lifecycle must be designed with source-diff detection, affected-topic analysis, selective Phase 1/2 refresh, acceptance, and retrieval rebuild.
