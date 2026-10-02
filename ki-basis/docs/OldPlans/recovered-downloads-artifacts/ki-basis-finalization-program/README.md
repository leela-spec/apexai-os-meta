# ki-basis Finalization Program Bundle

This bundle is designed against `leela-spec/apexai-os-meta` `main` as observed at `b9d7a77c1b84aaed99093e42cea32a7d51c56f26` on 2026-09-03.

## Contents

- `plans/00-START-HERE.md` — program launcher / Antigravity execution law.
- `plans/01-...` through `09-...` — one file per bounded module.
- `plans/05-HERMES-AI-CONTROL-STACK.md` — detailed operator-interactive OpenRouter + Hermes skills implementation.
- `patches/PATCH-06-documentation-truth.py` — narrow documentation/evidence correction.
- `patches/PATCH-08-performance-tuning-deferred.py` — documentation-only deferred tuning note.
- `patches/VERIFY-PATCHES.py` — verifies the two patches landed.
- `HANDOVER-NEXT-CHAT.md` — context handover for a fresh ChatGPT conversation.
- `ANTIGRAVITY-LAUNCHER.md` — copy/paste launcher for the first bounded Antigravity module.

## Patch execution

From a PowerShell or terminal with Python 3:

```powershell
python .\patches\PATCH-06-documentation-truth.py C:\GitDev\apexai-os-meta
python .\patches\PATCH-08-performance-tuning-deferred.py C:\GitDev\apexai-os-meta
python .\patches\VERIFY-PATCHES.py C:\GitDev\apexai-os-meta
```

Review `git diff` before committing. The patch scripts do not commit or push.

## Important

Run Module 01 before using any Paperless credential again. A replacement Paperless token was exposed in the current dossier and must be rotated.
