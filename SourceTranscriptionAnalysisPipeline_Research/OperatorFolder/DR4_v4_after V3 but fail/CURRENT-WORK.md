# CURRENT WORK — V3 PRIME IMPLEMENTATION

**Status:** PLAN_READY_FOR_OPERATOR_REVIEW  
**Implementation plan:** `06-PRIME-RECOMMENDATION-IMPLEMENTATION-PLAN.md`  
**Next package after operator approval:** `P00 — Preflight + ruthless reuse audit`

## TARGET

Implement the research report's selected production path directly, starting with the shortest real product vertical slice and adding only selected responsibilities that earn product value.

## Current authority

Read:

1. `../00-CURRENT-AUTHORITY.md`;
2. `00-START-HERE.md`;
3. `06-PRIME-RECOMMENDATION-IMPLEMENTATION-PLAN.md`.

Do not execute V2.1 `S00-S14` or the old V3 `M00-M05` discovery chain.

## Executor

Antigravity CLI directly on `main`.

OpenClaw is not on the implementation critical path. It may later invoke the proven CLI mechanically after the product works.

## Stop-loss

Two corrective iterations on the same subsystem without product advancement => `APPROACH_SUSPECT`; do not perform correction #3.

## Next

No implementation starts from this file until the operator approves the pushed plan. Then set the active work package to `P00` and execute only P00 in a fresh CLI context.
