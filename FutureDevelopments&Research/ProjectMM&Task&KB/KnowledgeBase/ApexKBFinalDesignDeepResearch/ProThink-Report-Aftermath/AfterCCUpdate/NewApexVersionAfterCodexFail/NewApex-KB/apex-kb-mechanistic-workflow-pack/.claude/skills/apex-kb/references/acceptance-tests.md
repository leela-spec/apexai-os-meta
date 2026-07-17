# Apex KB v2 Acceptance Tests

## Activation

- The skill has `disable-model-invocation: true` and contributes zero description/body context until manual invocation.
- `/apex-kb start` executes the control surface before any doctrine navigation.
- The launcher never constructs or paraphrases a command.

## Configuration and lock

- Start without config renders the fixed welcome and exact JSON template.
- Invalid config reports exact fields and performs no lifecycle mutation.
- Preflight is read-only except its report.
- Source root and KB root recursive overlap is blocked.
- Clean preflight renders one compact confirmation readback.
- Confirmed config produces a reproducible SHA-256 configuration hash.
- Any locked field change blocks execution and identifies the earliest invalidated stage.

## Phase 0

- Inventory totals reconcile with included, excluded, and blocked files.
- Candidates after rank 30 remain in the canonical map.
- Path, filename, title, H1, heading, body, link, date, lifecycle, and duplicate signals remain separate.
- Every candidate has a reason and pointer.
- Dates never produce a semantic authority verdict.
- Phase 0 stats reconcile with rankings and work-pack counts.

## Semantic instructions

- Generated Phase 1/2 instruction files validate against schema.
- Config hash and all input fingerprints are present.
- Phase 1 source batches never exceed configured context budget.
- Locked questions are copied exactly; no AI-generated target question silently appears.
- Semantic output outside the allowlist is rejected.
- Missing/changed input causes no semantic writes.
- Reconcile failures are copied into `prior_validation_feedback` for a bounded repair task.

## Knowledge value

- Every critical/routine question has a direct page route or the run remains partial.
- Dossier Macro/Meso/Micro sections are distinct.
- Source atlas contains every Phase 0 candidate exactly once.
- Unopened sources are never represented as evidence.
- Independent acceptance runs without drafting rationale.
- Query-ready requires semantic pass, deterministic postflight, and fresh retrieval.

## Scope

- The standard new-KB run never auto-adds another topic.
- A request to add new content to an existing KB is blocked with the `APEX_KB_UPDATE_FLOW_NOT_IMPLEMENTED` TODO route.
