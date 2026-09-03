# Module 08 — Performance Tuning Deferred by Evidence

## Decision

Do **not** apply the speculative CPU/RAM/worker/database/cache limits from the prior handover now.

They were hypotheses, not measurements from this workload.

## Why

Hard limits and worker reductions can create new failure modes:

- OCR backlog/timeout;
- OpenProject latency;
- OOM kills;
- PostgreSQL query degradation;
- Valkey key eviction affecting Paperless broker state;
- Hermes context/tool failures.

In particular, do not set `maxmemory-policy allkeys-lru` on Valkey merely to cap memory. Valkey is part of Paperless' operational path, not just a disposable browser cache.

## Future trigger

Only open a tuning module after collecting measurements for at least:

- idle stack;
- normal Hermes usage;
- Paperless OCR ingestion;
- OpenProject normal interaction;
- target backup;
- disposable restore.

Capture `docker stats --no-stream` plus any product-specific queue/latency symptoms.

If no concrete bottleneck exists, close the tuning review with `NO_CHANGE_REQUIRED`.

## Current action

Documentation-only. Run the supplied light patch to add this deferred evidence-gated tuning note to `ARCHITEKTUR-BASIS.md`.

```powershell
python .\patches\PATCH-08-performance-tuning-deferred.py C:\GitDev\apexai-os-meta
```

No Compose/service configuration changes in this module.

## Acceptance

Architecture documents preserve the tuning candidate as future work but explicitly forbid speculative limits without measurements.
