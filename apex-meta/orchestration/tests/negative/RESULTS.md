# Negative-test results — 2026-07-12

Checker: `scripts/orchestration_check.py` (stdlib-only; exit 0 pass / 1 violation / 2 fail-closed error).
Reproduce: run the commands below from repo root.

| Fixture | Failure class | Command | Expected | Actual |
|---|---|---|---|---|
| `f1-candidate-to-canon.md` | confirmed lifecycle on unreviewed candidate | `packet f1…` | 1 | **1** ✓ |
| `f2-stale-digest.md` | declared digest ≠ recomputed file hash | `canon-write f2…` | 1 | **1** ✓ |
| `f3-missing-evidence.md` | `sources_evidence` key absent (absent key illegal) | `packet f3…` | 1 | **1** ✓ |
| `f4-reviewer-mutation.md` | verdict pass while reviewer confessed artifact mutation | `verdict f4…` | 1 | **1** ✓ |
| `f5-unauthorized-write.md` | canon write without `operator_validation: confirmed` | `canon-write f5…` | 1 | **1** ✓ |
| `p0-positive-control.md` | real authorized US-IDEA-01 G1 conditions | `canon-write p0…` | 0 | **0** ✓ |
| real `00-intake-packet.md` | live packet conforms to schema | `packet …` | 0 | **0** ✓ |
| real v2 digest | live artifact digest recompute | `digest … --expected cd83e576…` | 0 | **0** ✓ |
| nonexistent file | fail-closed on unreadable input | `packet does-not-exist.md` | 2 | **2** ✓ |

All negative fixtures fail closed; positive controls pass; hard errors exit 2 (never silently pass). 9/9.
