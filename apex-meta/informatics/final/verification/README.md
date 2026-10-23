---
type: Verification
id: VERIF-README-v1.0
title: Apex Informatics Deterministic Verification Suite & Anti-Fake-Test Charter
description: Governance authority, token economics, and defect-prevention rationale for the 338 local deterministic tests.
status: current_truth
tags: [informatics, verification, tests, anti-fake-test, okf-v0.2]
---

# Apex Informatics Deterministic Verification Suite & Anti-Fake-Test Charter

> **Verification Root:** `apex-meta/informatics/final/verification/`  
> **Suite Runtime:** `0.73s` across all 338 tests  
> **AI Token Cost:** `0 tokens` (runs 100% locally on CPU via Python/pytest)  
> **Command:** `python -m pytest "apex-meta/informatics/final/verification/suites"`

---

## 1. The Anti-Fake-Test Law

> [!WARNING]
> **The Problem of AI Self-Verifying Fake Tests:**  
> Autonomous AI coding assistants frequently construct circular, tautological tests. These "fake tests" pass trivial syntax checks, assert mock outputs against mock inputs, and drift away from the actual user-agreed target. They create an illusion of correctness while silently failing operative requirements.

To prevent fake test pollution, every test in this suite is bound to the **Three Anti-Fake-Test Invariants**:
1. **Target Justification (`<target>` & `<new_machinery>`):** No test exists to celebrate boilerplate. Every test must trace to a concrete bug, structural drift defect, or empirical invariant.
2. **Deterministic CPU Execution:** Zero LLM calls in the test loop. Tests run deterministically via regex AST parsing, Byte-Pair Encoding (`tiktoken`), and filesystem assertions.
3. **Auditability via Layered Knowledge Base (`test-kb/`):** Every test suite links directly to its empirical research counterpart in [`final/research/06-layered-rule-kb/`](../research/06-layered-rule-kb/).

---

## 2. Inventory of the 338 Deterministic Tests

The suite comprises **338 tests** distributed across 7 specialized suites in [`suites/`](suites/):

| Suite | Tests | Runtime | What It Prevents (Defect Class Closed) |
|---|---|---|---|
| [`test_canonical_ownership.py`](suites/test_canonical_ownership.py) | **11** | 0.07s | **D1 & D9 Defects:** Duplicate durable IDs (`FA-04`), schema drift, machine-specific `file://` links. |
| [`test_informatics_e2e.py`](suites/test_informatics_e2e.py) | **146** | 0.36s | **STE & Formatting Drift:** Non-flat YAML, multi-line list frontmatter, run-on sentences, missing significance tags. |
| [`test_m3_challenger_tokens.py`](suites/test_m3_challenger_tokens.py) | **56** | 0.21s | **Synthetic Math & Fake Token Counts:** Verifies every claimed BPE token count against `cl100k_base` tiktoken encoding. |
| [`test_m3_rules16_22_links.py`](suites/test_m3_rules16_22_links.py) | **5** | 0.08s | **Broken Reference Drift:** Asserts 100% link resolution and protects live carriers (`AGENTS.md`, etc.) from uncommitted mutations. |
| [`test_m4_audits_coverage.py`](suites/test_m4_audits_coverage.py) | **52** | 0.18s | **Module Blind Spots:** Audits 100% rule inventory coverage across WP (25), FA (13), EM (12), AD (28), and GS (22) rules. |
| [`test_m5_challenger_verification.py`](suites/test_m5_challenger_verification.py) | **29** | 0.18s | **Lossy Compression Drift:** Validates `16-candidate-3A-ultra.md` against `13-candidate-3A-xml.md` and Option B rollups. |
| [`test_tier5_adversarial.py`](suites/test_tier5_adversarial.py) | **39** | 0.10s | **Context Leakage & Ceremony:** Simulates JIT router dispatch, asserts >= 70% token savings over full-stack loading, and bans computed math formulas. |

---

## 3. Token Economics & Resource Efficiency

- **Zero LLM Token Spend:** Traditional "eval agents" consume 10,000–50,000 tokens per verification run. This deterministic suite consumes **0 tokens**.
- **Instant CI/CD Feedback:** Full suite execution takes **< 1.0 second** (typically ~0.73s).
- **Offline / Air-Gapped Resilient:** Requires no internet access, no API keys, and no remote services.

---

## 4. Test Rationale Registry (`test-kb/`)

Detailed architectural rationales connecting each suite to its underlying research are indexed in [`test-kb/`](test-kb/):
- [`01-context-isolation-rationale.md`](test-kb/01-context-isolation-rationale.md) — Rationale for JIT gating and <= 4,000 character ceilings.
- [`02-single-ownership-rationale.md`](test-kb/02-single-ownership-rationale.md) — Rationale for durable IDs and single-file canonical ownership.
- [`03-contract-token-math-rationale.md`](test-kb/03-contract-token-math-rationale.md) — Rationale for BPE token counting and Option B verification.
