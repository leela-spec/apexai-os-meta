# E2E Test Infra: Next-Generation Apex Informatics Architecture

## Test Philosophy
- Opaque-box, requirement-driven testing derived strictly from `ORIGINAL_REQUEST.md`.
- Independent of internal implementation quirks.
- Methodology: Category-Partition + Boundary Value Analysis + Pairwise Combinatorial + Real-World Workload Testing.

## Feature Inventory
| # | Feature | Source (Requirement) | Tier 1 | Tier 2 | Tier 3 |
|---|---------|----------------------|:------:|:------:|:------:|
| 1 | Sub-Bundle Isolation | ORIGINAL_REQUEST §Acceptance Criteria | 5 | 5 | ✓ |
| 2 | Significance & Ranking Architecture (P0–P3) | ORIGINAL_REQUEST R1 | 5 | 5 | ✓ |
| 3 | Uncomputed 3-Metric Raw Estimates `[P<tier> \| I/E/R]` | ORIGINAL_REQUEST R1 | 5 | 5 | ✓ |
| 4 | Top-Loaded Primacy (First ~500 Tokens) | ORIGINAL_REQUEST R1 | 5 | 5 | ✓ |
| 5 | Writing Profile & STE Word Targets | ORIGINAL_REQUEST R2, R4 | 5 | 5 | ✓ |
| 6 | File Architecture & Five-Plane IA | ORIGINAL_REQUEST R4 | 5 | 5 | ✓ |
| 7 | Current-Truth Strict Separation (Zero Inline Changelog) | ORIGINAL_REQUEST R4 | 5 | 5 | ✓ |
| 8 | Execution Adapters (Q&A, Bake-Off, Patch, Handover, MMM) | ORIGINAL_REQUEST R4 | 5 | 5 | ✓ |
| 9 | Operational Lore & Anti-Drift Laws | ORIGINAL_REQUEST R5 | 5 | 5 | ✓ |
| 10 | Task Minimalism & Context Hygiene | ORIGINAL_REQUEST R5 | 5 | 5 | ✓ |
| 11 | Consolidated Router Size & XML IF-Gating | ORIGINAL_REQUEST R2, R3 | 5 | 5 | ✓ |
| 12 | Deterministic OKF Conformance (`okf_validator.py`) | ORIGINAL_REQUEST §Acceptance Criteria | 5 | 5 | ✓ |

## Test Architecture
- Test Runner: Python script at `apex-meta/informatics/tests/test_informatics_e2e.py`.
- Invocation: `python apex-meta/informatics/tests/test_informatics_e2e.py`
- Pass/Fail Semantics: Exits with code 0 on 100% pass, non-zero on any failure.
- Output: Structured JSON/text reporting per-tier pass counts and failure details.

## Real-World Application Scenarios (Tier 4)
| # | Scenario | Features Exercised | Complexity |
|---|----------|--------------------|------------|
| 1 | Agent Pure Writing Task Simulation | Router IF-gate, writing-profile isolation, zero other modules loaded | High |
| 2 | Agent Q&A Decision Matrix Formulation | execution-modes adapter, uncomputed raw (I/E/R) metrics, rejection notes | Medium |
| 3 | Agent Exact-Match Patch Intent Execution | execution-modes patch format, whitespace preservation, anti-hallucination | High |
| 4 | Agent Subsystem Two-Strike Drift Recovery | anti-drift-rules, two-strike rule, operator challenge trigger | Medium |
| 5 | Full Repository OKF & Apex Profile Validation | okf_validator.py execution on apex-meta/informatics, 0 OKF and 0 APEX errors | Critical |

## Coverage Thresholds
- Tier 1: >= 5 test cases per core feature (60+ tests).
- Tier 2: >= 5 test cases per core feature covering boundaries and edge cases (60+ tests).
- Tier 3: >= 12 cross-feature interaction pairwise tests.
- Tier 4: >= 5 real-world application workload scenarios.
- Total Target: ~140+ test assertions.
