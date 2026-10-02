---
type: Research
title: transcript-to-vault — first live-run trial log (youtube-2-1tGQJa450)
description: Four trials running the transcript-to-vault skill against a real German transcript via Hermes' OpenRouter gateway. Three root causes found and fixed; one is a quota wall, not a bug.
tags: [langextract, hermes, openrouter, transcript-to-vault, incident, rate-limit]
generated: { by: claude/sonnet-5, at: "2026-10-02" }
sources:
  - id: hermes-logs
    resource: docker logs ki-basis-hermes (2026-10-02, session window)
    title: Live Hermes gateway logs during the extraction trials
  - id: openrouter-key-api
    resource: https://openrouter.ai/api/v1/auth/key
    title: OpenRouter key usage/limit introspection endpoint
status: stable
---

# Summary

The pipeline (schema draft → LangExtract → Hermes gateway → grounded Markdown) works.[^hermes-logs]
One real extraction completed and grounded correctly. Three configuration trials failed before
that. Each trial had a distinct, now-fixed root cause. A fourth attempt hit OpenRouter's daily
free-tier quota instead. That quota wall is not a defect; it is a hard limit.[^openrouter-key-api]

# Trial Log

| # | Config changed | Symptom | Root cause | Fix |
|---|---|---|---|---|
| 1 | Default model chain, `max_workers=3`, `max_char_buffer=2000` | 10+ min elapsed, zero chunks completed, repeated `Broken pipe` | `stale_timeout_seconds: 5` (copied verbatim from community's config) is tuned for short chat replies, not extraction-length generation that needs real "thinking" time before the first token.[^hermes-logs] | Raised every model's `timeout_seconds`/`stale_timeout_seconds` to 30 in `config.yaml`. |
| 2 | `max_workers=1`, `batch_length=1`, `max_char_buffer=800` (isolating concurrency as a variable) | Same stale-timeout failures recurred | Confirms trial 1's cause: concurrency was never the lever, the timeout value was. | None needed — trial 1's fix was already sufficient; this trial just isolated the variable. |
| 3 | Explicit `model_id="z-ai/glm-5.2:free"`, `batch_length=3`, `max_workers=2`, `max_char_buffer=1500` | Run completed (exit 0), but 57 of 58 chunks failed JSON parsing; only 1 of 4 extractions grounded | The `model` field in a chat-completions request is **not honored** by Hermes for routing — it always walks its own `config.yaml` chain regardless of what the caller requests. That chain's last entry, `z-ai/glm-5.2:free`, had been deprecated by OpenRouter (`HTTP 404`); Hermes returned that provider's English error string as if it were completion content, and LangExtract correctly failed to parse it as JSON.[^hermes-logs] | Removed the dead `z-ai/glm-5.2:free` entry from both `providers.openrouter.models` and `fallback_providers` in `config.yaml`. |
| 4 | Same as trial 3 minus the dead entry, single diagnostic call | `HTTP 429: Rate limit exceeded: free-models-per-day` | OpenRouter's free tier caps a key without the $10 credit top-up at 50 free-model requests/day. Cumulative diagnostic + extraction calls this session used 73.[^openrouter-key-api] | Not fixable from this side today — see Recommendations. |

# What Worked

One grounded extraction completed end-to-end. It happened before the quota wall hit.

> Class: `gut_clearing_remove_spike`
> Quote: *"und der Verdacht ist hoch dass das eben noch im Darm produziert wird"*

This confirms the full chain — schema drafting via the Hermes gateway, `lx.extract()` against that
same gateway, `char_interval` grounding, exact-substring verification — is architecturally sound.
The remaining issues were all free-tier model reliability, not pipeline design.

# Account State at Time of Writing

Per the OpenRouter key-introspection endpoint:[^openrouter-key-api]

| Field | Value |
|---|---|
| `is_free_tier` | `true` |
| `free_model_daily_requests.used` | 73 |
| `free_model_daily_requests.limit` | 50 |
| `free_model_daily_requests.remaining` | 0 |
| `creator_user_id` | `user_3IKUrCDMQDvOC9nG7crOIbCIKkC` (opaque — not an email) |

The linked account's **email address is not retrievable from this endpoint** — OpenRouter does not
expose it via the API, by design. It was not found in any local repo doc either. The operator
must check the OpenRouter dashboard (openrouter.ai → Settings) directly to top up credit.

# Recommendations

- Check `free_model_daily_requests.remaining` via the key-introspection endpoint before any bulk
  extraction run — a single 80K-character transcript at ~800–1500 char chunks can need 50-100+
  calls, which alone can exhaust the un-topped-up daily cap.
- Treat the `model` field sent to Hermes' gateway as advisory only. The model actually used is
  always whichever `config.yaml`'s `model.default` / `fallback_providers` resolves to that moment.
  To target a specific model, change `config.yaml`, not the request.
- When copying another Hermes instance's free-model list, re-verify every entry against
  OpenRouter's live `GET /api/v1/models` (filter `pricing.prompt == "0"`) before trusting it —
  free-tier model availability churns; `z-ai/glm-5.2:free` was live when community's config was
  written and is gone now.
- `stale_timeout_seconds: 30` worked for this run's chunk sizes but is still a guess, not a
  measured ceiling. If future runs see renewed `Broken pipe`/stale-timeout errors, raise it
  further before re-diagnosing from scratch.

# Related

- [00_README.md](00_README.md) — component status table for this skill.
- [SKILL.md](SKILL.md) — the procedure these trials were exercising.
- [RESEARCH-HANDOVER-adaptive-schema-selection.md](RESEARCH-HANDOVER-adaptive-schema-selection.md) — separate open sub-problem, not implicated here.
- `config.yaml.bak-20261002T111602Z`, `config.yaml.bak-20261002T113415Z` — pre-edit backups on the private Hermes host, in order.

[^hermes-logs]: docker logs ki-basis-hermes, captured live during this session's trials, 2026-10-02.
[^openrouter-key-api]: `GET https://openrouter.ai/api/v1/auth/key`, queried 2026-10-02.
