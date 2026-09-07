# OpenRouter Free Model Pool, Cost Cap Defense & Fallback Engine

**Document ID:** ALR-004  
**Date:** 2026-09-07  
**Location:** `apex-meta/orchestration/new_final_v4/learnings_and_corrections/`  
**Target Architecture Level:** Tier 2 LLM Routing  

---

## 1. Context & Operational Requirement

When running autonomous workloads against cloud LLM providers, two risks must be mitigated:
1. **Unintended API Spend**: Autonomous background agents looping on tool calls can consume credits rapidly.
2. **Hard Rate Limit / Quota Halts**: Free model endpoints frequently enforce rate limits (e.g. 20 requests/minute). If a model hits a rate limit (HTTP 429), the entire pipeline must not crash.

---

## 2. Canonical OpenRouter Free Model Pool (`:free`)

OpenRouter hosts designated production-grade models that carry zero inference fees. These are identified by the `:free` suffix:

| Model ID | Context Window | Architecture / Strengths | Recommended Role |
|---|:---:|---|---|
| `meta-llama/llama-3.3-70b-instruct:free` | 128k | State-of-the-art open weights, strong reasoning | Primary Fallback for Strategy & Essay Outlines |
| `google/gemini-2.0-flash-exp:free` | 1M | Ultra-fast token streaming, enormous context | Bulk Text Processing & Curriculum Synthesis |
| `deepseek/deepseek-r1:free` | 64k | Chain-of-thought mathematical reasoning | Quantitative Reasoning & Complex Code Analysis |
| `qwen/qwen-2.5-72b-instruct:free` | 32k | Multi-lingual fluency, precise instruction following | Local Knowledge Extraction & Structured Output |

---

## 3. Resilient Fallback Engine Configuration

In `/root/.hermes/config.yaml`, configure the multi-tiered model pool:

```yaml
model:
  provider: openrouter
  base_url: https://openrouter.ai/api/v1
  default: meta-llama/llama-3.3-70b-instruct:free
  max_tokens: 16384
  
  # Resilient Free Fallback Chain
  fallbacks:
    - google/gemini-2.0-flash-exp:free
    - qwen/qwen-2.5-72b-instruct:free
    - deepseek/deepseek-r1:free

routing_policy:
  retry_on_status: [429, 500, 502, 503, 504]
  max_retries_per_model: 2
  failover_strategy: sequential_round_robin
  rate_limit_backoff_seconds: 5
```

---

## 4. Automatic Quota Cap & Rotation Trigger

To ensure that autonomous pipelines never incur unwanted credit charges:
1. **Zero-Balance Enforced Key**: Use an OpenRouter API key attached to an account with a credit balance of $0.00. OpenRouter will automatically restrict execution to `:free` models.
2. **Quota Exhaustion Rotation**: When Hermes receives an HTTP 429 or cost limit response, the wrapper catches the error, rotates the active model in the profile to the next free endpoint in the pool, and transparently retries the evaluation.
