# Transcript Pipeline V2 Reuse Harness

Isolated benchmark and adapter layer for the V2 transcript-to-knowledge reuse bake-off.
This harness interfaces with the locked TTK evidence/custody spine without weakening deterministic invariants.

## Architecture Boundaries
- **TTK Custody & State:** Immutable source SHA custody, segment IDs, processing windows, packet hashes, deterministic validation, resume, verify queue, compiler.
- **Trial 1 Semantic Transport:** Claude Code CLI (`claude`) subscription CLI transport only.
- **Fail-Closed Execution:** Zero heuristic/regex pseudo-semantics in production semantic paths.

## Layout
- `runner.py`: Deterministic control entrypoint for preflight, status, and candidate adapter dispatch.
- `receipt.py`: Atomic JSON receipt logging for all tasks and invocations.
- `schemas/`: Machine-readable JSON Schemas for Map, Reduce, and Verification results.
- `adapters/`: Candidate adapters for Map, Reduce, ASR, and advisory models.
- `tests/`: Deterministic unit tests for harness components, receipts, and schema sync.
