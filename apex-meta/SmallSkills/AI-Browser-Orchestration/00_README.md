# AI-Browser-Orchestration

Practical, indexed lessons for driving subscription/cloud chat-AI web UIs (ChatGPT, Perplexity, Gemini) via Chrome browser automation — composer quirks, chunked-submission technique, Deep Research workflow, and false-failure patterns to check before retrying or giving up.

This is a **cross-cutting capability skill**, not tied to one initiative. It grew out of the local-orchestration-engine research program's cross-agent research prompts (2026-08-08 through 2026-08-10), but anything that needs to drive these platforms — Weekly Orchestrator, Multi-Agent Orchestration, future initiatives — should read it before running a browser-driven agent session.

## Contents

| File | What it is |
|---|---|
| `Browser-Subscription-AI-Orchestration.okf.md` | The indexed OKF reference: 13 platform-tagged entries (BAO-001 to BAO-013) plus one open, time-stamped verification item. Read the index table first, then only the entries tagged for the platform(s) you're about to drive. |

## Relationship to existing knowledge locations

- Two of this folder's lessons were already recorded as `MK-KB-010` and `MK-KB-011` in `apex-meta/orchestration/agents/knowledge-bank/MISTAKES.md` before this folder existed. This file's `BAO-009`/`BAO-010` entries cross-reference those rather than duplicating them — read the MK-KB entries for the original incident-level detail. That `knowledge-bank/` folder's own `CORE.md` describes its ESSENCE/BEST_PRACTICES/MISTAKES/TEMPLATES set as legacy doctrine superseded by `.claude/agents/knowledge-bank.md` + the `apex-kb` skill for curated external subject-matter KBs — neither of those fits a short operational runbook like this one, which is why this content lives here instead.
- This is a desk synthesis from direct, empirical browser-automation observation this session — not promoted through any formal KB governance/candidate-ledger path. Treat it as a living operational reference: update entries in place as new platform behavior is observed, rather than letting a second, competing copy accumulate elsewhere.

## Status

- **Created**: 2026-08-10
- **Not yet done**: `VERIFY-001` inside the OKF file — Perplexity and Gemini GitHub connectors are operator-reported as newly installed but not yet empirically tested from a live session. Test both before defaulting to this file's chunked-submission (`BAO-003`) or single-shot Deep Research (`BAO-006`) workarounds.
