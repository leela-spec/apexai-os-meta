# OKF Adoption Project — Change Log

## 2026-09-01

**Wave 2 / A2 Execution** — Implemented deterministic OKF v0.2 / Apex Profile validator (`apex-meta/scripts/okf_validator.py`) with tri-class diagnostics (`OKF`, `APEX_PROFILE`, `ADVISORY`), created automated RED/GREEN test suite (`apex-meta/scripts/tests/test_okf_validator.py`), established minimal authoring procedure skill (`.claude/skills/informatics-authoring/`), and validated governed bundles.

**Wave 1 / A1 Execution** — Executed Wave 1 / Patch Sequence A1: ratified the canonical informatics package (`apex-meta/informatics/`), surgically updated `AGENTS.md`, `.claude/CLAUDE.md`, and `.github/copilot-instructions.md` via exact-match patch runner, created scoped adapters in `.claude/rules/` and `.github/instructions/`, and verified routing.

**Wave 0 Baseline Recorded** — Generated read-only baseline inventory (`w0-baseline-inventory.md`) and 24-task baseline retrieval benchmark (`w0-retrieval-eval.md`).

**Implementation planning** — Added the approved compatibility-first implementation plan for W0-W2 and the bounded A1/A2 patch sequence. These artifacts define baseline measurement, canonical informatics/routing lock, deterministic validation, minimal authoring support, verification gates, and explicit stop boundaries.

**Creation** — Bundle authored to capture one research round: tooling comparison (home-grown validator vs. `scaccogatto/okf-skills`, with due diligence), a Leela SSOT 0.1→0.2 migration assessment (verified safe but not executed), the resolved location of the prior "Informatics Design Research," an audit finding that apex-meta's existing `.okf.md` files predate real spec-conformance, and a standing next-steps checklist. No production files were changed by this research — see [Next Steps](next-steps.md) for what remains open.
