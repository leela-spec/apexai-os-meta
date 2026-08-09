"""lmbench -- APEX local-model benchmark harness. Stdlib only, per D-I2.

Measures whether a model+runtime+harness configuration can safely absorb
approved APEX local-execution work, per
`apex-meta/local-orchestration-engine/LOCAL-MODEL-BENCHMARK-PORTFOLIO-2026-08-08.md`
and the authority envelope in
`apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-08-R3-LOCAL-MODEL.md`.

This is a benchmark harness, not a third APEX orchestration system. It never
runs live Weekly or Multi-Agent work, and its output (`validated_profile_candidate`)
never carries a certification decision -- it only computes which task classes are
*eligible*, per the authority ladder in the decision lock's Section 6. Certification
is the operator's call.
"""

from __future__ import annotations

__all__ = ["__version__"]

__version__ = "0.1.0-candidate"
