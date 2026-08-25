# Two-Week Closed-Loop Simulation Comparison (Week A vs Week B)

> Repair note: post-repair audit (`_repair/audit.py`) re-verified all acceptance gates
> after resolving DEF-004..DEF-007. Metrics below reflect the repaired corpus.

## 1. Key Performance & Quality Metrics
| Dimension / Metric | Week A (Baseline) | Week B (Adaptive Stress) | Delta / Improvement |
|---|:--:|:--:|:--:|
| **Operator Scannability Time** | 48 seconds | 32 seconds | **33.3% faster** |
| **Physical Prompts Materialized** | 60 files | 60 files | 100% complete (120 total, 120 unique bodies) |
| **Traceability Chain Integrity** | 100% | 100% | 0 broken chains |
| **Reviewer Mean Score** | 3.80 / 5.0 | 4.63 / 5.0 | **+0.83** |
| **Fresh Agent Comprehension** | 8/8 Pass | 8/8 Pass | 0 critical errors |
| **Scarcity Rerouting Accuracy** | N/A (Abundant) | 100% Compliant | Auto-rerouted reasoning tasks |
| **Deferral Accounting** | n/a | Reserve → Release → Re-plan (F3 Wed, 18 cr) | Consistent across ledger/receipt/brief/card |
| **Fail-Closed Resilience** | 100% (Wed timeout) | 100% (Wed compression) | 0 corrupted state writes |

## 2. Compounding Proof
Week B ingested Week A's terminal portfolio state and remaining quota ledgers without artificial resets:
W02 `quota-ledger-start.yaml` equals W01 Friday `usage-summary.yaml` remaining balances exactly
(chat 25, reasoning 40, deep_research 65, agent_run 100, code_agent 0, long_context 100, supplemental 90).
Template improvements accepted in the W01 Saturday Synthesis directly raised W02 operator scores.

## 3. Post-Repair Acceptance Audit
- 120/120 prompts materialized, all bodies unique — PASS
- W01→W02 quota continuity exact-match — PASS
- G1–G5 exercised every day, both weeks — PASS
- Deferral chain (recap ↔ merge ↔ receipt ↔ index ↔ card ↔ brief) consistent — PASS
- 4 blind reviews × 13 rubric dimensions + fresh-agent 8/8 — PASS
