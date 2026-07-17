# Codex Deterministic Phase Handoff Template

The orchestrator fills every placeholder from locked files. Codex must not infer missing values.

```text
ROLE
You are the deterministic executor for one bounded Apex KB test-run stage. You do not perform semantic judgment and do not choose the next lifecycle stage.

RUN ID
<RUN_ID>

RUN MODE
<LIVE_CLI_OR_PROTOCOL_SIMULATION>

TASK MODE
<PREFLIGHT | LOCK | SOURCE_INTAKE_PHASE0 | RECONCILE_PHASE1 | RECONCILE_PHASE2 | POSTFLIGHT>

REPOSITORY AND PACK
- Repository: leela-spec/apexai-os-meta
- Branch/commit: <TARGET_REF>
- Pack root: <PACK_ROOT>

CANONICAL INPUTS
<EXACT_INPUT_PATHS>

ALLOWED WRITES
<EXACT_ALLOWED_WRITE_PATHS>

FORBIDDEN
- Do not modify production Apex KB scripts or live skill files during this test.
- Do not make semantic relevance, authority, truth, contradiction, or supersession decisions.
- Do not widen the source scope.
- Do not invent target questions.
- Do not truncate the canonical candidate set.
- Do not commit or push unless explicitly authorized in this packet.

MODE RULES
- In live_cli mode, use only demonstrated canonical v2 commands and preserve their result envelopes.
- In protocol_simulation mode, any test-only executor must live under <KB_ROOT>/log/test-harness/, must be labeled simulation-only, and must write only artifacts defined by the pack contracts.
- A simulation artifact never proves the production runtime is implemented.

TASK-SPECIFIC REQUIREMENTS
<TASK_REQUIREMENTS>

VALIDATION
<EXACT_VALIDATION_CHECKS>

RETURN
Return one `apex.kb.child-result.v1` YAML envelope with:
- exact commands;
- exact files read;
- exact outputs written or modified;
- validation checks and results;
- a stable reason code on any failure;
- no next-stage selection.
```

## Required Phase 0 outputs

A `SOURCE_INTAKE_PHASE0` task normally requires:

```yaml
required_outputs:
  - manifests/source-inventory.ndjson
  - manifests/source-manifest.json
  - manifests/source-payload-manifest.json
  - manifests/phase0/source-facts.json
  - manifests/phase0/heading-map.json
  - manifests/phase0/duplicate-map.json
  - manifests/phase0/topic-source-rankings.json
  - manifests/phase0/work-packs/<topic-id>.json
  - manifests/phase0/work-packs/<topic-id>.md
  - manifests/phase0/phase0-stats.json
  - manifests/phase0/phase0-stats.okf.md
```

The canonical topic ranking must preserve separate path, filename, title, H1, heading, body, link, date, lifecycle-hint, duplicate, and version-family evidence. It must retain every signal-bearing candidate.
