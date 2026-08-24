# PATCH-002 — Index Independent Pre-Implementation Validation Handover

Apply by exact literal replacement only. Stop if any `<OLD>` block does not match exactly once.

## 1. README — register the validation launcher and remove stale pending-patch text

/apex-meta/epics/hermes-multi-repo-orchestration-v2/README.md
<OLD>
10. `FUTURE-DEVELOPMENT.md` — explicitly deferred capabilities.

`epic.md` remains the historical project authority/index until the exact-match patch in `patches/` is applied. Do not silently edit existing control files outside the patch process.
</OLD>
<NEW>
10. `FUTURE-DEVELOPMENT.md` — explicitly deferred capabilities.

Independent pre-implementation validation launcher:

- `14-INDEPENDENT-PREIMPLEMENTATION-VALIDATION-HANDOVER.md` — adversarial handover/prompt for double/triple-checking the accepted architecture, tools, agent orchestration, risks, simulations, and current upstream contracts before implementation authorization.

The D02/D10 decision patch has landed. `README.md` is the current entrypoint and `state.yaml` is the current machine-readable state. Continue to use `patches/` for future edits to existing control files.
</NEW>

## 2. state.yaml — register the validation launcher

/apex-meta/epics/hermes-multi-repo-orchestration-v2/state.yaml
<OLD>
verification_matrix: apex-meta/epics/hermes-multi-repo-orchestration-v2/13-SOURCE-VERIFICATION-MATRIX.md
future_development: apex-meta/epics/hermes-multi-repo-orchestration-v2/FUTURE-DEVELOPMENT.md
</OLD>
<NEW>
verification_matrix: apex-meta/epics/hermes-multi-repo-orchestration-v2/13-SOURCE-VERIFICATION-MATRIX.md
validation_handover: apex-meta/epics/hermes-multi-repo-orchestration-v2/14-INDEPENDENT-PREIMPLEMENTATION-VALIDATION-HANDOVER.md
future_development: apex-meta/epics/hermes-multi-repo-orchestration-v2/FUTURE-DEVELOPMENT.md
</NEW>
