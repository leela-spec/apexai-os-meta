# Workflow Efficiency Matrix & Execution Bottleneck Audit

**Document ID:** ALR-001  
**Date:** 2026-09-07  
**Location:** `apex-meta/orchestration/new_final_v4/learnings_and_corrections/`  

---

## 1. Complete Workflow Telemetry Table

| Step | Workflow ID | Domain | Specialist Actor | Executed Engine | Duration | Exit Code | Efficiency Tier |
|---|---|---|---|---|:---:|:---:|---|
| 01 | **WF-01** | Global Health Sweep | `InfraAgent` | PowerShell `wsl.exe` loop + `docker ps` | 19.1s | 0 | Tier B (High) |
| 02 | **WF-05** | IPOS Macro Regime | `IPOSAgent` | Python `.venv` pytest (17 tests) | 9.70s | 0 | Tier B (High) |
| 03 | **WF-06** | Evidence Custody Watchdog | `IPOSAgent` | Python `hashlib` SHA-256 drill | 0.8s | 0 | Tier A (Extreme) |
| 04 | **WF-02** | Creative Writing Synthesis | `ContentAgent` | Hermes (`research-strategist` / OpenRouter) | 1m 30s | 0 | Tier C (Moderate) |
| 05 | **WF-03** | Workshop Curriculum Generator | `ContentAgent` | Hermes (`workshop-designer` / OpenRouter) | **11m 34s** | 0 | Tier D (High Latency) |
| 06 | **WF-04** | MOA Multi-Variant Websites | `ContentAgent` | Python `build_all_websites.py` | 2.20s | 0 | Tier A (Extreme) |
| 07 | **WF-10** | ACIM Corpus Cross-Reference | `ContentAgent` | Hermes (`default` multi-turn tool calling) | 3m 00s | 0 | Tier C (Moderate) |
| 08 | **WF-07** | Coaching Lifecycle Invoicing | `ContentAgent` | Python reportlab + REST API + Celery | 6.2s | 0 | Tier B (High) |
| 09 | **WF-08** | Equinox Pretix Ticketing | `InfraAgent` | Python `verify_fundraiser_stack.py` | 2.07s | 0 | Tier A (Extreme) |
| 10 | **WF-09** | Telegram Bot Offline Intake | `InfraAgent` | Python CLI + Paperless + OpenProject | 5.1s | 0 | Tier B (High) |

---

## 2. Quantitative Insights: The Deterministic vs. Generative Divide

### Observation 1: Deterministic Code is 50x–300x Faster
- The seven deterministic workflows (WF01, WF04, WF05, WF06, WF07, WF08, WF09) required an aggregate total execution time of **~45 seconds combined**.
- They verified 320 sold-out tickets (€11,300), generated and validated 22 static HTML websites, executed 17 quantitative risk tests, and performed PDF invoice generation, OCR ingestion, and bank reconciliation.
- There were zero retries, zero dropped packets, and zero state drift.

### Observation 2: Generative Inference Dominates Execution Time
- The three generative Hermes workflows (WF02, WF03, WF10) consumed **16 minutes and 4 seconds**, representing **95.5% of the total test suite duration**.
- Latency in generative workflows is driven by:
  1. OpenRouter network latency (TLS handshakes + cloud queueing).
  2. Large token output counts (WF03: ~20 KB output).
  3. Multi-turn tool calling roundtrips (WF10: 4 separate roundtrips).
  4. SSE stream drops requiring full re-evaluation.

---

## 3. Structural Action Items

1. **Keep Rule 4 Sacred**: Continue shifting numeric, procedural, and structural tasks into Python scripts and DuckDB queries.
2. **Local Inference for Tier 2**: Transition Hermes from cloud OpenRouter to local Ollama (`qwen3.5:9b`) to eliminate network latency and SSE stream drops.
3. **Stage-Gated Prompting**: Break massive multi-module prompts into isolated single-topic prompts.
