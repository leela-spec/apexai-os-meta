# Flow Execution Engine — Short Handover

Status: candidate architecture and partial implementation. FEE fills only the
Weekly Orchestrator's step 4 (`operator_execution`). It does not replace the
existing weekly agents or skills, and G3 remains a human gate.

## Start here

1. `00-START-HERE.md` — purpose, boundary, and reading order.
2. `architecture/01-macro-architecture-decision.md` — system shape and trust boundary.
3. `architecture/02-meso-module-design.md` — internal modules M1–M9.
4. `architecture/05-preflight-findings.md` — findings from checking the proposal
   against the live repository and executing laptop.

## Where to record new information

| Information | Record it in |
|---|---|
| Final architecture decision and reversal trigger | `architecture/04-decision-ledger.md` |
| Answer to an unresolved design question | `DESIGN-LOCK-QA.md` |
| New research or evidence that challenges an assumption | `architecture/05-preflight-findings.md` |
| Proposed change to an upstream contract | `architecture/06-gate-batch-draft.md` |
| Implementation mapping, phase status, or verification result | `architecture/03-micro-implementation-map.md` |

Do not silently turn a proposal into a live contract. Draft upstream changes in
`06-gate-batch-draft.md`, obtain the operator gate, then update the owning contract.

## What is implemented

The implementation is under `scripts/fee/`:

- M1 pack compiler and frozen-plan hashing
- M6 append-only execution ledger
- assisted `next` / `capture` loop
- skip-marker emission
- strict artifact reader and path containment
- permanent injection-containment tests

Verified behavior includes a real F1 skip flow and a fixture-based mixed-provider
capture flow. The implementation remains candidate until the upstream gates and
downstream acceptance test are complete.

## Current blocker

Executable flows cannot run because current prompt packs do not provide resolvable
prompt bodies and may still contain `provider_unspecified`. FEE correctly halts
instead of inventing either value.

## Next steps, in order

1. Approve gate-batch item 3: permit FEE to act at Weekly Orchestrator step 4.
2. Approve gate-batch item 1: define and produce prompt bodies at
   `artifacts/flow-packets/<day>/prompt-packs/bodies/<packet_id>.md`.
3. Complete Phase 2: emit `evidence-bundle.md` from captured turns.
4. Run V7: prove `apex-evidence-normalize` accepts that bundle and emits a valid
   `normalized_raw_flow_dump` with sufficient confidence.
5. Only after V7, implement the Windows nightly harness and sanctioned Claude
   auto-lane.

Local-model adjudication (M5), the executor bridge (M7), Perplexity integration,
and dynamic lane-routing feedback remain deliberately deferred.
