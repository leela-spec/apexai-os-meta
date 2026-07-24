# Apex KB — Knowledge index

Single entry point for future runs/agents. **Start here, then read `PROJECT-STATUS.md`, then the task packets.** Dates and paths are repo-relative to `/…/apexai-os-meta`.

## Future-agent "start here"
1. Read this index → `PROJECT-STATUS.md` (current state + roadmap) → `apex-kb-improvement-tasks.md` (what's done / deferred).
2. To operate the KB, use the **`apex-kb` skill** or spawn the **`apex-kb-operator` agent**; both drive the installed `apex-kb` CLI. **The CLI is the sole lifecycle authority** — never re-implement its logic in a skill/agent.
3. When a run is `query_ready`, call `apex-kb query … --json-output` first (the result carries a `future_agent_contract`); reopen raw sources only when the answer is absent or `source_drift` is not fresh.

## This-session knowledge (2026-07-24)
| Path | Type | Purpose |
|---|---|---|
| `apex-meta/kb/therapy-narm-personal-development/audit/reports/2026-07-24-apex-kb-value-audit.md` | audit report | Three-pillar value audit + unified competitor matrix + **§15 post-Phase-1 re-score**. |
| `apex-meta/kb/therapy-narm-personal-development/audit/handoffs/2026-07-23-apex-kb-value-audit-handover.md` | handover | Original audit brief that scoped the work. |
| `apex-meta/apex-kb-cli/docs/apex-kb-improvement-plan.md` | plan | Full reasoning: realms glossary, semantic-prompt root cause, fixes with value, agent orchestration, scope revisions. |
| `apex-meta/apex-kb-cli/docs/apex-kb-improvement-tasks.md` | task packets | Self-contained packets with Phase-1 status (done) and Phase-2 (deferred/retained). |
| `apex-meta/apex-kb-cli/docs/prompt-design-notes.md` | research | Evidence-based prompt/template patterns (from llm-wiki projects + public best practice). |
| `apex-meta/apex-kb-cli/docs/PROJECT-STATUS.md` | status | Maturity-by-layer, what Phase 1 delivered, roadmap, KB-quality test plan. |

## Runtime artifacts (how to run it)
| Path | Type | Purpose |
|---|---|---|
| `.claude/skills/apex-kb/` | skill | Thin launcher for the CLI; `SKILL.md` lists all 7 commands and the query-first retrieval contract. |
| `.claude/agents/apex-kb-operator.md` | agent | Persistent operator that drives the CLI end-to-end without drift. |
| `apex-meta/apex-kb-cli/` | package | The installed `apex-kb` CLI (`pip install -e ".[test]"`; entry point `apex_kb.cli:main`). |

## CLI reference docs (existing)
| Path | Purpose |
|---|---|
| `apex-meta/apex-kb-cli/README.md` | CLI overview and commands. |
| `apex-meta/apex-kb-cli/docs/ARCHITECTURE.md` | Deterministic lifecycle + semantic-worker architecture. |
| `apex-meta/apex-kb-cli/docs/OPERATOR-GUIDE.md` | Operator-facing usage. |
| `apex-meta/apex-kb-cli/docs/SEMANTIC-WORKER-GUIDE.md` | How a semantic worker executes one packet. |
| `apex-meta/apex-kb-cli/docs/TESTING-AND-CANARY.md` | Test suite + canary evidence. |
| `apex-meta/apex-kb-cli/docs/MIGRATION-AND-LEGACY.md` | Migration from the legacy `apex_kb.py` surface. |
| `apex-meta/apex-kb-cli/docs/IMPLEMENTATION-HANDOVER.md` | Implementation handover notes. |

## Status snapshot
Phase 1 (CLI infrastructure) complete: 54/54 tests green; 13 packets + `pointer_health` probe; commits `30182952 → 99cdde17`. Phase 2 (KB-quality benchmark + richer re-compile) is deferred and retained — see `PROJECT-STATUS.md`.
