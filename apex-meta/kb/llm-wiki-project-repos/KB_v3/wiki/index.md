---
title: "KB_v3 Index: Apex KB Lifecycle Improvements"
page_type: index
kb_slug: "llm-wiki-project-repos"
kb_v3_scope: "improvements_failures_patch_ideas"
created_at: "2026-07-06"
status: "active"
confidence: "high"
---

# KB_v3 Index: Apex KB Lifecycle Improvements

## Scope

KB_v3 is a standalone semantic compile under `apex-meta/kb/llm-wiki-project-repos/KB_v3/`. It does not build on earlier `llm-wiki-project-repos` Phase 1/2 outputs. Its source scope is the improvements, failures, and patch ideas in `apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/`.

## Read-First Routes

| Question | Start here | Then read |
|---|---|---|
| What is the overall failure/patch picture? | `wiki/summaries/lifecycle-failure-and-patch-overview.md` | `audit/prioritized-patch-backlog.md` |
| How do we prevent folder/source drift? | `wiki/concepts/target-drift-and-source-authority-gates.md` | `ingest-analysis/phase1-improvements-failures-patch-ideas.analysis.md` |
| What is the strongest source-custody patch? | `wiki/concepts/source-payload-custody-manifest.md` | `wiki/summaries/lifecycle-failure-and-patch-overview.md` |
| How do we stop assistant/process drift? | `wiki/concepts/executor-routing-and-lifecycle-state-lock.md` | `wiki/concepts/cli-contract-and-shell-portability.md` |
| Which deterministic friction points should be patched? | `wiki/concepts/cli-contract-and-shell-portability.md` | `audit/prioritized-patch-backlog.md` |
| What validates Phase 2 usefulness? | `wiki/concepts/postflight-index-retrieval-quality-loop.md` | `log/phase1-phase2-semantic-compile-report.md` |

## Phase 1

- `ingest-analysis/phase1-improvements-failures-patch-ideas.analysis.md` — source-grounded analysis of improvements, failures, tensions, and proposed Phase 2 pages.

## Phase 2 Summary

- `wiki/summaries/lifecycle-failure-and-patch-overview.md` — macro synthesis of Apex KB lifecycle failure modes and patch clusters.

## Phase 2 Concepts

- `wiki/concepts/target-drift-and-source-authority-gates.md` — source access versus source authority; relevance gates.
- `wiki/concepts/source-payload-custody-manifest.md` — deterministic payload manifest patch.
- `wiki/concepts/executor-routing-and-lifecycle-state-lock.md` — state lock, executor selection, one usable artifact.
- `wiki/concepts/cli-contract-and-shell-portability.md` — CLI flag, alias, PowerShell, and ordered execution fixes.
- `wiki/concepts/postflight-index-retrieval-quality-loop.md` — wiki index, retrieval index, lint/audit/status/query eval loop.

## Audit

- `audit/prioritized-patch-backlog.md` — ranked patch backlog consolidated from lifecycle-analysis sources.

## Raw Source Reopen Triggers

- Implementing exact script behavior.
- Writing Codex prompts that mutate repo files.
- Resolving whether a finding should be patch, documentation, or process-only.
- Validating source custody or postflight through actual scripts.
