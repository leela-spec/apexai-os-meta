---
title: "APEX OS Orchestration Systems Index — apexai-os-meta"
purpose: "Canonical map of the two APEX OS orchestration systems, their entrypoints, the shared Plan-Sync-Session Backbone, and supporting design evidence."
created: 2026-07-11
maintenance: "Update this file whenever a live entrypoint, system boundary, backbone package, or authority classification changes."
---

# APEX OS Orchestration Systems Index

APEX OS has exactly two orchestration systems and one shared capability backbone:

```text
APEX OS
├── Weekly Orchestrator
│   └── .claude/skills/weekly-orchestrator/SKILL.md
├── Multi-Agent Orchestration
│   └── apex-meta/orchestration/00-START-HERE.md
└── Plan-Sync-Session Backbone
    ├── .claude/skills/apex-plan/SKILL.md
    ├── .claude/skills/apex-sync/SKILL.md
    └── .claude/skills/apex-session/SKILL.md
```

The backbone is shared infrastructure, not a third orchestration system. Neither orchestration system absorbs or automatically activates the other. Cross-system transfer requires explicit operator instruction, an explicit handoff packet, or a confirmed durable-artifact reference.

The compact APEX OS activation router is `.claude/CLAUDE.md`. Use this index for navigation and classification, not as a substitute for a live entrypoint.

## 1. Knowledge bases (`apex-meta/kb/`)

| KB folder | Status | Purpose | Notes |
|---|---|---|---|
| `claude-code-orchestration-design/` | **live, primary** | The main "how to build Claude Code agent/subagent/skill orchestration systems" KB. Merged from 4 source groups (official Anthropic docs, claude-skill-design, a downloaded practitioner-repo corpus, prompt-engineer-research-base). 106 wiki pages as of 2026-07-10/11. | See `apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/orchestrator-education-targeting-handover.md` for current authoring status and open work. |
| `operator-research-orchestration-20260711/` | **live, compiled** | Research KB answering "what should the Apex Claude-native control-plane architecture look like." Fully compiled wiki (6 summary pages), high confidence. | Synthesized in `apex-meta/handoff/agent-skill-system-research/best-practice-report.md`. |
| `old-apex-full-orchestration-agent-kb-v2/` | **live, Phase 1 + Phase 2 (compilation incomplete)** | Historical Apex/Hermes agent-swarm design (9-agent roster, BUILD/VERIFY/LOCK state machine, handoff rules, failure-mode analysis). Corrected 2026-07-11: a compiled Phase 2 wiki DOES exist — `wiki/index.md` states 17 compiled pages, 19 page files on disk (2 unenumerated, 6 placeholder topics), plus the `ingest-analysis/` Phase 1 files. | Contains `OperatorResearch/ProcessRanking_GPT&MasterOA.md` — the process-taxonomy file behind `apex-meta/fable-orchestrator/`. Treat this KB's agent roster/state-machine as evidence to translate, not a runtime spec to revive (see best-practice-report.md decision 5/8). |
| `old-apex-full-orchestration-agent-kb/` (no `-v2`) | **live, compiled — DO NOT DELETE** | Older (59 commits, since 2026-07-02) than `-v2` (3 commits, all 2026-07-11), but **not a duplicate of it** — distinct subject: old agent-KB architecture, migration/execution-safety doctrine, historical-path-authority patterns. 18 compiled wiki pages. | **Resolved 2026-07-11: keep as-is, do not delete.** Two live skill spec files cite specific pages of this KB as their `source_doctrine`: `.claude/skills/apex-kb/references/historical-path-authority-lint-spec.md` and `.claude/skills/apex-kb/references/repo-execution-router-lint-spec.md`. Deleting this KB would leave those specs pointing at evidence that no longer exists. See `apex-meta/fable-orchestrator/fable-execution-best-practices.md` §7 for the full lesson — always check for `source_doctrine`/citation dependents before deleting any KB, even one that looks old or superseded on the surface. |
| `apex-plan-sync-session-workflow-v2/` | **live, compiled** | Defines the apex-plan / apex-sync / apex-session three-package boundary (proposal vs. deterministic computation vs. gated mutation). Small, high-confidence wiki. | Synthesized in `apex-meta/handoff/agent-skill-system-research/best-practice-report.md`. This is the KB whose boundary model was recommended as the state-mutation backbone for any unified system. |
| `Weekly-Orchestrator/` | **live, domain-specific index and research KB** | Defines and indexes the `PrecapWeek -> PrecapNextDay -> execution -> FlowRecap -> status/update` weekly loop. | Start with `apex-meta/kb/Weekly-Orchestrator/00-START-HERE.md`. Human and machine indexes belong under `indexes/`; load `OperatorResearch/` only when targeted source evidence is needed. |
| `claude-skill-design/` | **superseded / archival** | Original skill-design KB (was 783 files). Its content was copied wholesale into `claude-code-orchestration-design/raw/source-groups/claude-skill-design/`. Only 5 files (a `log/`) remain here. | Do not treat as a live, independent source — read the copy inside `claude-code-orchestration-design/` instead. |
| `_source-acquisitions/skill-best-practices-official-2026-06-23/` | **superseded / archival** | Original official-source acquisition archive (633 files: Anthropic docs, spec, PDF guide, official repos). Copied into `claude-code-orchestration-design/raw/source-groups/_source-acquisitions/`. | Same as above — read the copy inside `claude-code-orchestration-design/`, this is the highest-authority (P0) source tier there. |
| `prompt-engineer-research-base/` | **live, partial** | Prompt/workflow research, supporting material only. Copied into `claude-code-orchestration-design/raw/source-groups/prompt-engineer-research-base/` as a P2 (supporting) source group. | Both the original and the copy exist; treat the copy as the one in active use. |
| `llm-wiki-project-repos/` | **live, unclear maturity** | Appears to hold LLM-authored wiki pages about downloaded project repos. Has both a root `wiki/` (1 file — likely stale/early) and a more developed `KB_v3/` subtree (own `wiki/`, `ingest-analysis/`, `audit/`, `log/`). | **Not yet reviewed in depth.** Possible overlap with `claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/` (both concern downloaded practitioner repos) — check before treating as a separate authority. |

## 2. Handoff clusters (`apex-meta/handoff/`)

| Folder / file | Contents |
|---|---|
| `agent-skill-system-research/` | `best-practice-report.md` + `design-lock-qa.md` — synthesis of the three orchestration KBs (`operator-research-orchestration-20260711`, `old-apex-full-orchestration-agent-kb-v2`, `apex-plan-sync-session-workflow-v2`) against current Anthropic/MCP best-practice docs, plus an 8-question design-lock Q&A. **Read this first** for the unification decisions already made. |

## 3. Shared backbone and supporting skills (`.claude/skills/`)

| Skill or package | Classification and role |
|---|---|
| `apex-plan`, `apex-sync`, `apex-session` | **Plan-Sync-Session Backbone** — shared capability backbone for proposal/decomposition, deterministic computation, and confirmed mutation/closure. It is not a third orchestration system. |
| `weekly-orchestrator` | Runtime entrypoint for the separate **Weekly Orchestrator** system. |
| `ProjectStatus`, `AIRouting`, `PromptEngineer`, `Workflow&Processes` | Standalone operator-facing capabilities; their presence does not activate either orchestration system. |
| `deterministic-file-promotion`, `deterministic-markdown-patcher`, `deterministic-markdown-patcher2`, `project-kb-manager`, `prompt-engineering-patterns`, `source-authority-and-verdict-packet`, `apex-kb` | Supporting deterministic, authoring, review, or KB-lifecycle capabilities. |

## 4. Other relevant `apex-meta/` locations

| Path | Purpose |
|---|---|
| `orchestration/` | Live **Multi-Agent Orchestration** package, one of the two APEX OS orchestration systems: 00-START-HERE, ARCHITECTURE, GLOSSARY, shared packet/authority/review schemas, orchestrator and Detective workflows, user stories, and simulations. Its seven role definitions live in the shared runtime location `.claude/agents/` but belong to Multi-Agent Orchestration only when an active run adopts or routes them. Start at `apex-meta/orchestration/00-START-HERE.md`. |
| `fable-orchestrator/` | Historical decision-lock and audit-trail folder for the initiative that produced Multi-Agent Orchestration. **Fable Orchestrator is a former working name, not the live system name.** See its own `README.md`. |

## 5. Known overlaps / open questions to resolve before treating any KB as sole authority

1. ~~`old-apex-full-orchestration-agent-kb` vs. `old-apex-full-orchestration-agent-kb-v2` — relationship unconfirmed~~ **Resolved 2026-07-11**: different scope, not a fork/duplicate; non-v2 is older but independently load-bearing (cited as `source_doctrine` by two live skill spec files) — see §1 notes above. Keep both.
2. `llm-wiki-project-repos/` vs. `claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/` — both cover downloaded practitioner repos; possible duplicate corpus.
3. ~~Terminology drift across KBs — no glossary file has been created yet.~~ **Resolved 2026-07-11**: `apex-meta/orchestration/GLOSSARY.md` is the terminology authority (role/state, agent, candidate/verified, packet, workflow/skill, validation/approval, consequential).
