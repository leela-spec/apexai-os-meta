# Transcript-to-Knowledge V3 — START HERE

**Status:** AUTHORITATIVE CURRENT ENTRYPOINT  
**Date:** 2026-08-19  
**Repository:** `leela-spec/apexai-os-meta`  
**Branch policy:** `main` only unless the operator explicitly changes it

## Mission

Produce a reliable, source-faithful transcript-to-knowledge pipeline by **running and reusing proven existing systems first**, then adding only the smallest custom integration that real benchmark evidence proves necessary.

V3 exists because V2.1 drifted into a 15-stage custom implementation/orchestration protocol and consumed repeated repair cycles before producing meaningful product output.

## Current authority order

1. current explicit operator instruction;
2. this file;
3. `01-V3-ARCHITECTURE.md`;
4. `02-V3-IMPLEMENTATION-PLAN.md`;
5. exactly one active file under `execution-modules/`;
6. `03-V3-BENCHMARK-AND-TEST-SPEC.yaml` and `04-V3-COMPONENT-REGISTRY.yaml`;
7. `05-V3-OPENCLAW-ANTIGRAVITY-ORCHESTRATION.md` for relay mechanics;
8. `../HANDOVER-2026-08-19-RESET-TO-PROVEN-INFRASTRUCTURE-RESEARCH.md` for failure history and original intent;
9. all V2/V2.1 and V1 material as historical evidence only.

## Superseded execution authority

Do **not** execute the V2.1 `S00-S14` sequence. Do not continue from S01. The following are historical:

- `../v2-reuse-bakeoff/10-V2.1-RECOMMENDED-END-TO-END-ARCHITECTURE.md`
- `../v2-reuse-bakeoff/11-V2.1-STAGE-BY-STAGE-IMPLEMENTATION-PLAN.md`
- `../v2-reuse-bakeoff/execution-modules/`
- `../v2-reuse-bakeoff/06-TRIAL1-TRANSPORT-LOCK.yaml`

Their research observations may be reused, but their orchestration/authority model is not current.

## V3 operating model

```text
ChatGPT architecture/review
        |
        | writes/updates current work package in Git/main
        v
OpenClaw thin relay / process supervisor
        |
        | launches + watches
        v
Antigravity CLI executor
        |
        | research -> run -> inspect -> implement -> test -> repair
        v
Git/main = durable state and handoff
```

OpenClaw is not a planner, semantic reviewer, or architecture authority.

## Anti-drift hard rules

1. **TARGET dominates.** Every action must materially advance the user-facing product or remove a demonstrated blocker.
2. **Reuse before build.** No new abstraction until an existing alternative was actually tried and shown insufficient.
3. **Product before infrastructure.** Before a real vertical slice works, fix only blockers, product corruption, experiment invalidation, or material safety/data-loss risk.
4. **Two-strike rule.** Two corrective iterations on the same subsystem without product advancement => stop repairing it and reconsider/replace the approach.
5. **Orchestration gets only one repair cycle.** If OpenClaw relay itself fails twice before completing a product-advancing task, bypass it and launch Antigravity directly from the same module file.
6. **No sunk-cost authority.** Existing implementation effort gives an approach no preference.
7. **Evidence proportionality.** Do not build more verification machinery than the product risk justifies.
8. **No fake substitutes.** No synthetic audio, historical artifact presented as fresh, heuristic semantic worker, or schema-only PASS.

## Required benchmark corpus

Architecture selection uses **3 primary videos**:

- `P-h5WSQG1Sw` — long English science interview;
- `CygwqaNg2PY` — English technical finance;
- `vFTuLylvYnA` — German finance.

`oZIsMX6WgFs` remains an **optional holdout/regression source**, not a mandatory architecture-selection run.

The previous spec did not require 15-20 videos: it had 4 sources, >=10 representative Map windows, and 40 support pairs. V3 deliberately reduces mandatory evaluation volume while keeping EN/DE, long-source, technical, multi-speaker, and numeric/domain-term coverage.

## Module chain

- `M00` — OpenClaw -> Antigravity relay smoke **while producing one useful research artifact**
- `M01` — proven end-to-end systems landscape + runnable baselines
- `M02` — ASR/transcript layer benchmark **only if still needed**
- `M03` — grounded extraction bake-off **only if still needed**
- `M04` — global synthesis/knowledge-product bake-off **only if still needed**
- `M05` — evaluate and select the smallest proven production composition
- `M06` — integrate only the selected composition
- `M07` — fresh three-source E2E/regression proof

A strong near-complete system discovered in M01 may cause M02-M04 to be skipped. V3 does not force work merely because a module exists.

## Review gates

ChatGPT reviews by default only after:

1. **M01** — choose whether an existing system can be adopted/forked or component composition is necessary;
2. **M05** — freeze the production composition;
3. **M07** — final product/regression acceptance.

Other modules may proceed one at a time through fresh Antigravity contexts under the fixed plan unless they hit `OPERATOR_DECISION`, `APPROACH_SUSPECT`, or a hard blocker.
