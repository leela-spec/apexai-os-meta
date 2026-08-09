---
title: "Local Model Research Attempt (FAILED) — Benchmark Harness — ChatGPT"
doc_type: local_model_research_result
initiative: local-orchestration-engine
prompt: apex-meta/local-orchestration-engine/research-prompts/LOCAL-MODEL-RESEARCH-BENCHMARK-HARNESS-2026-08-08.md
prompt_id: E
agent: chatgpt
agent_model_label: "ChatGPT, reasoning effort: Mittel (Medium, UI default)"
agent_mode: "standard reasoning + web search (Websuche toggle manually enabled)"
account_tier: "subscription (plan tier not disclosed by UI); workspace credit/billing-limit banner recurring throughout this project, never interacted with"
run_id: R1-R3
run_started: "2026-08-09"
run_duration_seconds: null
evidence_date: 2026-08-09
chat_url: null
bundle_sha256: "a1696ab67ccce7b7687b826c1677fec8101d32a2a70a1980880cdb7510279541"
retries: 2
interruptions: []
uncontrolled_variables:
  - "Prompt payload was verified byte-for-byte intact (marker-count check) in every attempt before submission, so this is not a prompt-injection or paste-corruption artifact."
status: "FAILED (superseded) — no usable content produced in these 3 attempts; a 4th attempt (raw-GitHub-URL-fetch via ChatGPT's own browsing tool) also failed, producing only citation chips (see MISTAKES.md MK-KB-010); a 5th attempt via ChatGPT's native GitHub connector succeeded — see the sibling -CHATGPT-RESULT.md file"
---

# Local Model Research Attempt (FAILED) — Benchmark Harness — ChatGPT

## What happened

Research Prompt E (Benchmark Harness Design) was submitted to ChatGPT three times against the same verified-intact bundle (preamble + Operator Decision Lock R3 + Local Model Benchmark Portfolio + Research Prompt E, byte-verified via marker counts before every submission):

1. **Attempt 1** (existing thread): produced only ~346 characters of web-search citation chips (e.g. "Inspect +3", "SweBench +2", "GitHub +1", "arXiv") with zero written prose. Confirmed genuinely idle (not mid-generation) via repeated `stop-button` absence checks over several minutes.
2. **Attempt 2** (same thread, after a one-line nudge message): grew only to ~486 characters, still entirely citation chips, no prose.
3. **Attempt 3** (brand-new chat/thread, to rule out thread-level corruption as the cause): produced ~451 characters, again entirely citation chips, no prose. Genuinely idle, not a rendering or polling false-negative.

All three attempts show the same signature: the model appears to enter a web-search tool-calling loop for this specific prompt and never emits a final written answer, regardless of thread history. This looks like a prompt- or account/session-state-specific failure mode particular to this research prompt on ChatGPT, not a browser-automation defect (insertion integrity was verified correct every time) and not simple mid-generation impatience (idle state was confirmed with margin every time).

## Disposition

No further retries were attempted without operator input, per the standing instruction to check in after a third same-pattern failure rather than keep resubmitting. Perplexity's Bundle E result (see the sibling `-PERPLEXITY-RESULT.md` file) and the existing Prompts A-D results for both agents are what is available for cross-agent synthesis at this time. If the operator wants a fourth attempt (e.g. with Websuche disabled, or the prompt split into smaller pieces), that is a candidate follow-up but was not attempted automatically here.

## Update — superseded 2026-08-09

A 4th attempt asked ChatGPT to fetch the two authority documents and the Research Prompt E file from `raw.githubusercontent.com` directly using its own web-browsing/search tool (link-based, no pasted content). This also failed: the response opened with a packet title but its entire body was web-search citation chips ("GitHub +1", "Inspect +2", "arXiv", etc.) with no synthesized prose, the same signature as attempts 1-3 above. This confirmed, empirically and in this exact project, the operator's assessment that asking an agent to read a GitHub file URL via its own browsing tool is not a reliable mechanism — recorded as `MK-KB-010` in `orchestration/agents/knowledge-bank/MISTAKES.md`.

A 5th attempt used ChatGPT's native, already-connected GitHub connector (Settings → Plugins → GitHub, OAuth-linked, visible as "Verbunden"/Connected, with first-party file-read actions such as "Check repo initialized" and "Compare commits") instead of the browsing tool. ChatGPT visibly invoked the connector ("Drei Rohdateien und Forschungs-Benchmark-Datei abgerufen"), confirmed the fetched prompt file's frontmatter title, and produced a complete, well-formed research packet ending in the required closing YAML block. See `LOCAL-MODEL-RESEARCH-E-BENCHMARK-HARNESS-2026-08-09-CHATGPT-RESULT.md` for the full result. This file is kept as the historical record of what did not work.
