# ki-basis — CLI Reasoning / Hermes Routing Correction

Baseline reviewed: `origin/main` at `bb9333f70c8c8706bed7861f128cd10813ba5c8c`.

The operator confirmed that **none of the earlier patch bundles have been applied**.

This bundle therefore supersedes all earlier patch bundles from this chat. Do not apply those first.

## Final current logic

```text
heavy-reasoning CLI agent
        ↓
Hermes authenticated local API
        ↓
Hermes provider-backed routing / tools
        ↓
real Hermes skills (supplied later)
        ↓
ki-basis applications
```

- OpenRouter is configured now for Hermes routing/execution.
- The upstream CLI agent can use its own provider for heavy reasoning.
- The CLI agent cannot literally replace Hermes' model/session; Hermes still needs inference.
- Final application skills and `ki-basis-control` are deferred until the real skill set is supplied.
- Direct app APIs remain infrastructure/debug surfaces, not a second permanent agent-control architecture.
- Docker Desktop remains background runtime manager; Dashboard stays closed.

## Apply

```powershell
python .\PATCH-00-single-routing-logic.py C:\GitDev\apexai-os-meta
python .\PATCH-04A-05A-add-current-authority.py C:\GitDev\apexai-os-meta
python .\PATCH-05-mark-real-skills-future.py C:\GitDev\apexai-os-meta
python .\PATCH-HERMES-api-bridge.py C:\GitDev\apexai-os-meta
python .\PATCH-06-runtime-and-research-truth.py C:\GitDev\apexai-os-meta
python .\PATCH-07-bridge-lifecycle.py C:\GitDev\apexai-os-meta
python .\PATCH-09-bridge-phase-audit.py C:\GitDev\apexai-os-meta
python .\PATCH-HANDOVER-single-routing-logic.py C:\GitDev\apexai-os-meta
python .\VERIFY-CLI-HERMES-ROUTING-PATCHES.py C:\GitDev\apexai-os-meta
```

Review `git diff` before committing, then use `ANTIGRAVITY-BRIDGE-LAUNCHER.md`.

The patches are anchor-based and fail instead of broadly rewriting unexpected files.
