---
title: "Orchestration Systems Index — apexai-os-meta"
purpose: "Single map of every orchestration-relevant KB, handoff cluster, skill, and support folder in this repo, so a new orchestrator run doesn't have to rediscover the repo from scratch."
created: 2026-07-11
maintenance: "Update this file whenever a KB is merged, superseded, or created. Do not let it drift silently — a stale index is worse than no index."
---

# Orchestration Systems Index

Read this before starting any large orchestration-design task in this repo. It tells you what exists, what's live, what's superseded, and where to go for what.

## 1. Knowledge bases (`apex-meta/kb/`)

| KB folder | Status | Purpose | Notes |
|---|---|---|---|
| `claude-code-orchestration-design/` | **live, primary** | The main "how to build Claude Code agent/subagent/skill orchestration systems" KB. Merged from 4 source groups (official Anthropic docs, claude-skill-design, a downloaded practitioner-repo corpus, prompt-engineer-research-base). 106 wiki pages as of 2026-07-10/11. | See `apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/orchestrator-education-targeting-handover.md` for current authoring status and open work. |
| `operator-research-orchestration-20260711/` | **live, compiled** | Research KB answering "what should the Apex Claude-native control-plane architecture look like." Fully compiled wiki (6 summary pages), high confidence. | Synthesized in `apex-meta/handoff/agent-skill-system-research/best-practice-report.md`. |
| `old-apex-full-orchestration-agent-kb-v2/` | **live, Phase 1 only** | Historical Apex/Hermes agent-swarm design (9-agent roster, BUILD/VERIFY/LOCK state machine, handoff rules, failure-mode analysis). No Phase 2 wiki yet — read via `ingest-analysis/` Phase 1 files. | Contains `OperatorResearch/ProcessRanking_GPT&MasterOA.md` — the process-taxonomy file behind `apex-meta/fable-orchestrator/`. Treat this KB's agent roster/state-machine as evidence to translate, not a runtime spec to revive (see best-practice-report.md decision 5/8). |
| `old-apex-full-orchestration-agent-kb/` (no `-v2`) | **live, compiled — DO NOT DELETE** | Older (59 commits, since 2026-07-02) than `-v2` (3 commits, all 2026-07-11), but **not a duplicate of it** — distinct subject: old agent-KB architecture, migration/execution-safety doctrine, historical-path-authority patterns. 18 compiled wiki pages. | **Resolved 2026-07-11: keep as-is, do not delete.** Two live skill spec files cite specific pages of this KB as their `source_doctrine`: `.claude/skills/apex-kb/references/historical-path-authority-lint-spec.md` and `.claude/skills/apex-kb/references/repo-execution-router-lint-spec.md`. Deleting this KB would leave those specs pointing at evidence that no longer exists. See `apex-meta/fable-orchestrator/fable-execution-best-practices.md` §7 for the full lesson — always check for `source_doctrine`/citation dependents before deleting any KB, even one that looks old or superseded on the surface. |
| `apex-plan-sync-session-workflow-v2/` | **live, compiled** | Defines the apex-plan / apex-sync / apex-session three-package boundary (proposal vs. deterministic computation vs. gated mutation). Small, high-confidence wiki. | Synthesized in `apex-meta/handoff/agent-skill-system-research/best-practice-report.md`. This is the KB whose boundary model was recommended as the state-mutation backbone for any unified system. |
| `claude-skill-design/` | **superseded / archival** | Original skill-design KB (was 783 files). Its content was copied wholesale into `claude-code-orchestration-design/raw/source-groups/claude-skill-design/`. Only 5 files (a `log/`) remain here. | Do not treat as a live, independent source — read the copy inside `claude-code-orchestration-design/` instead. |
| `_source-acquisitions/skill-best-practices-official-2026-06-23/` | **superseded / archival** | Original official-source acquisition archive (633 files: Anthropic docs, spec, PDF guide, official repos). Copied into `claude-code-orchestration-design/raw/source-groups/_source-acquisitions/`. | Same as above — read the copy inside `claude-code-orchestration-design/`, this is the highest-authority (P0) source tier there. |
| `prompt-engineer-research-base/` | **live, partial** | Prompt/workflow research, supporting material only. Copied into `claude-code-orchestration-design/raw/source-groups/prompt-engineer-research-base/` as a P2 (supporting) source group. | Both the original and the copy exist; treat the copy as the one in active use. |
| `llm-wiki-project-repos/` | **live, unclear maturity** | Appears to hold LLM-authored wiki pages about downloaded project repos. Has both a root `wiki/` (1 file — likely stale/early) and a more developed `KB_v3/` subtree (own `wiki/`, `ingest-analysis/`, `audit/`, `log/`). | **Not yet reviewed in depth.** Possible overlap with `claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/` (both concern downloaded practitioner repos) — check before treating as a separate authority. |

## 2. Handoff clusters (`apex-meta/handoff/`)

| Folder / file | Contents |
|---|---|
| `agent-skill-system-research/` | `best-practice-report.md` + `design-lock-qa.md` — synthesis of the three orchestration KBs (`operator-research-orchestration-20260711`, `old-apex-full-orchestration-agent-kb-v2`, `apex-plan-sync-session-workflow-v2`) against current Anthropic/MCP best-practice docs, plus an 8-question design-lock Q&A. **Read this first** for the unification decisions already made. |

## 3. Core skills (`.claude/skills/`)

| Skill | Role |
|---|---|
| `apex-plan`, `apex-sync`, `apex-session` | The three-package planning/computation/mutation boundary (see `apex-plan-sync-session-workflow-v2` KB above). |
| `ProjectStatus`, `AIRouting`, `PromptEngineer`, `Workflow&Processes` | Standalone operator-facing skills, no hard gate. |
| `deterministic-file-promotion`, `deterministic-markdown-patcher`, `deterministic-markdown-patcher2`, `project-kb-manager`, `prompt-engineering-patterns`, `source-authority-and-verdict-packet` | Supporting deterministic/authoring tools used by the above. |

## 4. Other relevant `apex-meta/` locations

| Path | Purpose |
|---|---|
| `fable-orchestrator/` | **New** — this initiative's decision-lock folder (process blueprint Q&A, execution best practices for the Fable+external-model orchestration model). See its own `README.md`. |

## 5. Known overlaps / open questions to resolve before treating any KB as sole authority

1. ~~`old-apex-full-orchestration-agent-kb` vs. `old-apex-full-orchestration-agent-kb-v2` — relationship unconfirmed~~ **Resolved 2026-07-11**: different scope, not a fork/duplicate; non-v2 is older but independently load-bearing (cited as `source_doctrine` by two live skill spec files) — see §1 notes above. Keep both.
2. `llm-wiki-project-repos/` vs. `claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/` — both cover downloaded practitioner repos; possible duplicate corpus.
3. Terminology drift across KBs (e.g. "role" vs. "state" as the unit of permission, "agent" as ephemeral subagent vs. persistent identity) — already flagged in `agent-skill-system-research/design-lock-qa.md` Q7; no glossary file has been created yet.
