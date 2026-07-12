# Weekly Orchestrator — Macro Architecture Decision (locked)

Status: final. Decided against `apex-meta/kb/claude-code-orchestration-design/` (primary best-practice KB, per operator priority), `apex-meta/fable-orchestrator/design-lock-answers.md` (Q1–Q8), and the two deep-research verdicts in `apex-meta/fable-orchestrator/prompts/PromptAnswers/`.

## D-M1. Topology: main-thread meta orchestrator + ephemeral stage subagents

Decision: the meta agent is the **main conversation operating under the `weekly-orchestrator` control skill** (accountability: meta_ops). Every loop stage runs as an **ephemeral, context-isolated subagent invoked from a durable definition** under `.claude/agents/`. No always-on agents; no subagent orchestrates other subagents.

Evidence:
- Mechanism ladder (`wiki/summaries/claude-mechanism-decision-model.md`, claim C001): escalate only when the lower rung demonstrably cannot carry the work. Main conversation is the correct rung when phases share context and need operator back-and-forth — gates G1–G5 are operator dialogues, so the gate-holder must live in the main thread.
- Resilience (`wiki/summaries/agent-skill-orchestration-resilient-workflows.md`): resilience is about **where the plan/state lives, not which agent runs it**. The plan lives in files (`CLAUDE.md` core_loop, `state/`, `artifacts/`), so any session can resume the loop from files alone.
- `design-lock-answers.md` Q1-B: fixed workflow backbone + ephemeral task-scoped subagents; durable *accountabilities*, not always-on agents.

## D-M2. Skills do NOT become agents; agents own skills by declaration

Decision: the operator hypothesis "skills become agents with their own isolated skill base" is **partially corrected**. Skills stay skills under `.claude/skills/` (the discovery root). Each stage subagent gets its isolated skill base through the `skills:` frontmatter preload field — full skill content injected into the subagent's fresh context at startup. Ownership is declared in the agent definition, not expressed by moving files.

Evidence:
- Explicit KB verdict (`wiki/summaries/max-run-20260709/skill-hook-plugin-mcp-boundaries.md` C001): "Skill, hook, plugin, and MCP surfaces should not collapse into one generic 'agent' mechanism."
- `wiki/summaries/agent-vs-subagent-vs-skill.md` (claim C003): skill = reusability WITHOUT isolation; subagent = isolation + tool restriction + verbose work returning a short summary. The weekly stages need both → subagent + preloaded skill, not a converted skill.
- Sub-agents doc (`raw/.../primary-code-claude-com-docs-en-sub-agents.md.md` line 277): `skills:` field preloads full skill content; unlisted skills remain invocable via the Skill tool.
- Nested "subskills" are non-canonical; flat sibling skill packages win (`ingest-analysis/.../SubskillsVsAgents_CC.md` §5). Therefore: no folder moves of skill packages; the only required file surgery was canonicalizing six entrypoints to `SKILL.md` with valid frontmatter (without which discovery and preload fail).

## D-M3. Agent ↦ skill ownership matrix

| stage agent (`.claude/agents/`) | accountability | preloaded skills (owned base) | via Skill tool on demand | tools | gate |
|---|---|---|---|---|---|
| apex-precap-week | meta_strategy | PrecapWeek | — | Read, Grep, Glob, Write | G1 |
| apex-precap-next-day | meta_ops | PrecapNextDay | PromptEngineer, AIRouting, Workflow&Processes | Read, Grep, Glob, Write, Skill | G2 |
| apex-evidence-normalize | meta_ops | raw-flow-dump-normalize | — | Read, Grep, Glob, Write | G3 capture |
| apex-flow-recap | meta_ops | flow-recap, model-usage-log | — | Read, Grep, Glob, Write | G4 |
| apex-status-merge | meta_ops | status-merge | — | Read, Grep, Glob, Write | G5 |
| apex-project-status | meta_ops | ProjectStatus | — | Read, Grep, Glob, Write | none |
| apex-review-validity | meta_detective | — (self-contained lens instructions) | — | Read, Grep, Glob | review |
| apex-review-alignment | meta_detective | — (self-contained lens instructions) | — | Read, Grep, Glob | review |
| apex-plan-ops | meta_ops | apex-plan | — | Read, Grep, Glob, Write | operator gate in packet |
| apex-sync-ops | meta_ops | apex-sync | — | Read, Grep, Glob, Bash (apex_sync.py dry-run only) | none |

Alfred (operator-facing accountability) is carried by the main thread itself: it presents packets, holds gates, and records operator decisions. It is not a spawned agent.

The three-package system is integrated per Q2-B (US §3 `meta_ops_support_capabilities`): apex-plan proposes through `apex-plan-ops` (packet-only, writes nothing durable), apex-sync computes through `apex-sync-ops` (dry-run only; the registry non-dry-run write runs in the main thread after operator confirmation of the drift preview), and apex-session's gated-mutation contract is realized by the main-thread single write path itself — status mutation records follow `.claude/skills/apex-session/references/mutation-gate-rules.md`.

## D-M4. Permission model: role + object authority, single write path

Decision: role/tool scoping says who may act; the artifact's `authority.state` (candidate | verified | invalidated) says what may justify action. Stage agents write only their own `artifacts/` family. Canon-changing writes (`state/`, `.claude/kb/`) happen ONLY in the main thread after `operator_validation: confirmed` AND verified-input closure. No BUILD/VERIFY/LOCK state machine.

Evidence: `PromptAnswers/Role-vs-state permission separation_WithRepoAccess.md` §3 (verdict b: minimal authority field, not a full machine; both fields must pass for canon writes); enforcement-boundary doctrine (guidance < settings/hooks; hard-enforce only a short high-risk list — here, the single main-thread write path).

## D-M5. Adversarial review: dual-blind lens pair, deterministic aggregation

Decision: consequential packets (canon-changing, unresolved risk, cross-project conflict, or operator-requested) get two parallel blind reviewers (validity lens, alignment lens) bound to a frozen basis_digest, aggregated by fixed policy — never by an LLM tiebreak. Single-reviewer Detective is rejected as insufficient.

Evidence: `PromptAnswers/Adversarial-review wiring for an orchestrator-worker system (DEEP).md` (decision-change result + steps 1–6); wiring specified in `.claude/skills/weekly-orchestrator/references/review-wiring.md`.

## D-M6. Token efficiency: file format law

Decision: MD-first with one fenced YAML envelope block per packet; snake_case; function-typed labels (Rule/Constraint/Stop/Applies when/Do not); refs-not-copies; compact entrypoints with `read_when`-gated references; stage agents return envelope + ≤12-line summary, never full bodies, so the main thread's context stays flat across the continuous loop.

Evidence: `wiki/summaries/token-efficient-information-design.md` (catalog-first, load-on-demand, B01-C002/C010, B04-C012); `special_ops__informatics_design/` (typed labels, scaffold-vs-appendix split, MD-first with YAML for contract blocks, sidecars only when a consumer needs them).

## Rejected alternatives

- Spawned meta-agent orchestrator: breaks gate dialogues, adds a rung with no demonstrated need, and state already lives in files (D-M1 evidence).
- Moving skill packages into per-agent folders: breaks skill discovery and `skills:` preload; collapses mechanisms the KB says to keep separate (D-M2 evidence).
- Persistent named agents with memory: deferred by the KB's own operator policy (persistent agents small/validated, only for genuine durable identity); no weekly-loop stage needs cross-session agent memory — state is file-held.
- Full lifecycle state machine: disproportionate; the demonstrated gap is covered by the single `authority` object (D-M4 evidence).
