---
doc_type: research-report
task_id: agent-skill-system-research-run
version: 1
created: 2026-07-11
authority: source_backed_summary
supersedes: none — this is new output, not a state mutation
mode: read-only-research-and-synthesis
---

# SUMMARY (read this first)

**What was read:** Index/wiki/summary-tier files only, from three KB folders under `apex-meta/kb/`:
`operator-research-orchestration-20260711` (has a full compiled wiki — 6 summary pages, all read),
`old-apex-full-orchestration-agent-kb-v2` (no wiki yet — Phase 1 ingest-analysis + Phase 0 nav report read instead),
`apex-plan-sync-session-workflow-v2` (has a full wiki — index, 3 concepts, 3 entities headers, 1 summary; all read except one entity body).
Plus current Anthropic/MCP documentation (fetched live, not from model memory): Building Effective Agents, Agent Skills, Claude Code subagents, Writing Tools for Agents, Effective Context Engineering.

**What was found:** The three KB systems already agree on more than they conflict on. All three independently converge on: a small number of durable roles (not a large permanent roster), explicit artifact contracts instead of conversational memory, a hard split between LLM judgment and deterministic computation, and an operator/validation gate before consequential state changes. The disagreement is not architectural — it's about **which system is the boundary-enforcement layer** (Operator-Research KB's four-role control plane vs. Plan-Sync-Session KB's three-package proposal/compute/mutation split vs. Old-Apex-Full-Orchestration KB's role/state permission model) and **whether "role" or "state" is the unit that grants permission** (Old-Apex-Full-Orchestration KB explicitly says role ≠ permission, state does; Systems 1 and 3 don't make this distinction explicit).

**Top 3 decisions** (full list in `design-lock-qa.md`):
1. Treat Plan-Sync-Session KB's proposal → deterministic-compute → gated-mutation split as the canonical state-mutation boundary for the unified system; fold Operator-Research KB's four-role control plane in as the *who proposes/executes* layer on top of it, not a competing boundary.
2. Adopt Anthropic's skill granularity rule (split when `SKILL.md` gets unwieldy; push detail into referenced files) as the concrete anti-sprawl mechanism for the many skills already listed in `CLAUDE.md`.
3. Make subagents strictly ephemeral/task-scoped (per Claude Code's model), and reserve Old-Apex-Full-Orchestration KB's "named permanent agent" concept only for roles with genuine persistent identity/memory/ownership — not for every recurring task type.

---

# §1 Patterns (from current Anthropic/MCP guidance)

| Pattern | When to use | How | Source |
|---|---|---|---|
| Workflow (predefined code path) vs. Agent (LLM-directed loop) | Workflow when the task is well-defined and repeatable with known steps; agent when the model must make open-ended tool/step decisions | Default to workflow; only promote to an agent loop when a fixed code path can't cover the branching | [Building Effective AI Agents](https://www.anthropic.com/research/building-effective-agents) |
| Prompt chaining | Sequential, decomposable task where each step's output feeds the next | Fixed sequence of LLM calls, each validated before the next runs | Building Effective AI Agents |
| Routing | Heterogeneous inputs that need different handling | Classify the input first, then dispatch to a specialized path/handler | Building Effective AI Agents |
| Parallelization (sectioning / voting) | Independent subtasks, or need for diverse takes on one task | Run subtasks concurrently; aggregate or vote on results | Building Effective AI Agents |
| Orchestrator-workers | Complex task whose decomposition isn't knowable up front | One LLM plans and delegates to specialized workers, synthesizes their output | Building Effective AI Agents |
| Evaluator-optimizer | Output quality benefits from a second critical pass | One LLM generates, a second LLM (or the same one in a different role) critiques and iterates | Building Effective AI Agents |
| Simplicity first | Always — before adding any agentic machinery | Start with the simplest prompt/workflow that could work; add steps only when evaluation shows the simple version fails | Building Effective AI Agents |
| Transparency | Any multi-step agent | Explicitly surface planning/reasoning steps rather than hiding them in opaque chains | Building Effective AI Agents |
| Agent-Computer Interface (ACI) discipline | Any tool-using agent | Treat tool docs/specs with the same rigor as a human-facing API; test and iterate on descriptions | Building Effective AI Agents; [Writing Tools for Agents](https://www.anthropic.com/engineering/writing-tools-for-agents) |
| Skill = directory + `SKILL.md` with required `name`/`description` frontmatter | Any reusable, describable capability | Name/description pre-load into system prompt at startup; full body loads only when relevant (progressive disclosure) | [Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) |
| Progressive disclosure (3 levels: name+description → full SKILL.md → bundled files) | Any skill whose full detail would be wasteful to always load | Keep Level 1 tiny; push rarely-needed detail into separate referenced files loaded on demand | Agent Skills |
| Skill granularity — split when unwieldy | A `SKILL.md` file is growing large or covers multiple rarely-co-occurring contexts | Split into separate files/skills; keep mutually-exclusive contexts in separate paths | Agent Skills |
| Subagent = isolated context + scoped tools + own system prompt | A side task would flood the main conversation, or the same worker type gets spawned repeatedly | Define in `.claude/agents/`; write a precise `description` so the parent knows when to delegate; restrict tool access to what the subagent actually needs | [Claude Code subagents](https://code.claude.com/docs/en/sub-agents) |
| Model tiering via subagents | Cost/latency-sensitive repeated subtask | Route cheap/fast subtasks to a smaller model (e.g. Haiku) via a dedicated subagent | Claude Code subagents |
| Tool selection — fewer, higher-impact tools | Any tool surface design | Don't wrap every API endpoint; consolidate multi-step operations into one tool call | Writing Tools for Agents |
| Tool namespacing | Multiple tools with overlapping domains | Consistent prefixes (`asana_projects_search`) so the agent can disambiguate | Writing Tools for Agents |
| High-signal tool responses | Any tool with a large possible response body | Return semantic names not IDs; support concise vs. detailed response modes; paginate/truncate with sane defaults | Writing Tools for Agents |
| Context budget = scarce resource | All agent/multi-agent design | Curate the smallest high-signal token set per turn rather than maximal recall | [Effective Context Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) |
| Just-in-time retrieval | Large corpora / KBs / file trees | Keep lightweight identifiers (paths, IDs) in context; load full content only when acted on | Effective Context Engineering |
| Compaction | Long-horizon tasks approaching context limits | Summarize history, preserving decisions/open issues/critical details; discard redundant tool output first | Effective Context Engineering |
| Structured external note-taking | Multi-step or multi-session work | Persist progress/decisions to a file (NOTES.md-style) outside context, re-read as needed | Effective Context Engineering |
| Sub-agent context isolation | Deep exploration that would pollute the lead agent's window | Sub-agent does the deep dive, returns a condensed (~1-2k token) summary; lead keeps only the high-level plan | Effective Context Engineering |
| MCP first-class context types: Tool / Resource / Prompt | Any external system integration | Model executable actions as Tools, read-only data as Resources, reusable templates as Prompts | [MCP Specification](https://modelcontextprotocol.io/specification/2025-11-25) |

---

# §2 Mapped onto Apex (per pattern, per system: follows / violates / not addressed)

| Pattern | Operator-Research KB | Old-Apex-Full-Orchestration KB | Plan-Sync-Session KB |
|---|---|---|---|
| Workflow vs. agent distinction | **Follows implicitly** — favors "temporary specialization" over new permanent agents, i.e. workflow-first (`claude-native-apex-orchestration.md` C002) | **Not addressed** — framed entirely as agent roster + state machine, no workflow-vs-agent framing | **Follows** — apex-plan/sync/session are workflow-shaped fixed pipelines, not open agent loops |
| Small stable role set | **Follows** — explicit "four-role control plane," rejects permanent-role proliferation (rank-1 claim C002 in `defining-pattern-and-decision-ranking.md`) | **Violates the spirit / different unit** — nine named agents is already larger than Operator-Research KB's four, and states (BUILD/VERIFY/LOCK) are treated as the real permission layer, not role count | **Follows** — exactly three named packages (`three-package-boundary.md`), each with a hard "must not" list |
| Deterministic vs. semantic split | **Follows** — explicit rank-1 default (`defining-pattern-and-decision-ranking.md` C004): deterministic tooling for exactness, Claude for ambiguity | **Not addressed directly** — closest analog is BUILD/VERIFY/LOCK state permission, which is a workflow-state split, not a compute-mechanism split | **Follows precisely** — `apex-sync` is explicitly the deterministic/read-side layer, `apex-plan` explicitly may not run scripts or compute exact state (`proposal-computation-mutation-split.md`) |
| Independent validation / operator gate | **Follows** — rank-1 default C003, "independent validation gate" concept named directly | **Follows, via states** — VERIFY is a distinct state from BUILD, and self-review/role-conflation is a named failure mode (`phase1-failure-evidence.md` F02) | **Follows, most concretely** — explicit `operator_validation: confirmed` field gates mutation; Phase 2 requires the literal phrase `approve ingest` (`operator-gated-phase-boundary.md`) |
| Explicit structured handoffs | **Follows** — "structured handoff" and workflow records W01/W02 cited as evidence pattern | **Follows, most concretely** — handoff rules require role, state, target surface, next state, prerequisites, expected action, unresolved risk (`phase1-resilient-workflows.md` W01) | **Partially addressed** — `apex-session` owns "H6 handoff artifacts" but the concept page doesn't spell out a handoff schema as detailed as Old-Apex-Full-Orchestration KB's |
| Progressive disclosure / skill granularity | **Not addressed** — this KB is about orchestration architecture, not skill authoring mechanics | **Not addressed** | **Not addressed** — none of the three systems engage with the Anthropic skill-authoring mechanics at all; this is a genuine gap, not a disagreement |
| Subagent = ephemeral, tool-scoped, context-isolated | **Loosely compatible** — "temporary specialization" language is directionally the same idea but not spelled out in Claude Code subagent terms | **Conflicts in framing** — treats agents as named, persistent identities with KB roots and default validators, closer to permanent personas than ephemeral subagents | **Not addressed** — apex-plan/sync/session read as *packages/processes*, not agents in the Claude Code subagent sense; compatible by omission |
| Anti-canonization / candidate-vs-canon separation | **Partially addressed** — via "historical runtime is evidence not target" rule | **Follows, explicitly** — named safeguard: source/candidate/canon/validation/promotion must stay separate (`phase1-failure-evidence.md` F01), and "candidate-to-canonization-leak" is a named failure family | **Follows implicitly** — proposal ≠ computed truth ≠ confirmed mutation is the same shape of rule, just for a different lifecycle stage |
| Just-in-time retrieval / context budget discipline | **Not addressed** | **Not addressed** | **Not addressed** — all three KBs are silent on runtime context-window management; this is inherited from the *apex-kb* skill's retrieval design, not from these three orchestration KBs |

---

# §3 The highest-leverage decisions required to unify the three systems

1. **Pick the state-mutation boundary owner.** Plan-Sync-Session KB's proposal → deterministic-compute → gated-mutation split is the most concrete and directly maps to Anthropic's deterministic-vs-agentic distinction. Adopt it as *the* boundary; treat Operator-Research KB's four-role control plane as roles that sit *on top of* this boundary (who authors proposals, who runs computation, who confirms mutation), not as a parallel/competing boundary. Reconciling this avoids having two different systems both claiming to be "the" gate.

2. **Resolve role vs. state as the unit of permission.** Old-Apex-Full-Orchestration KB explicitly argues role names don't grant permission — operational state (BUILD/VERIFY/LOCK) does. Systems 1 and 3 use role/package boundaries without this state layer. Decide whether the unified system needs an explicit state machine (adds rigor, adds one more concept to track) or whether the three-package boundary (Plan-Sync-Session KB) already provides equivalent protection without it. Given the anti-overengineering constraint on this task, default to *not* adding a new state machine unless a concrete failure is observed that the package boundary doesn't already prevent.

3. **Cap the permanent-role count and force everything else through skills or subagents.** Operator-Research KB's four roles and Plan-Sync-Session KB's three packages both land near "small single digits." Old-Apex-Full-Orchestration KB's nine agents is the outlier. Any unification should treat Old-Apex-Full-Orchestration KB's nine-agent roster as candidate detail to translate into (a) a handful of durable roles/packages plus (b) Claude Code skills and subagents for the rest — not as nine permanent personas to keep.

4. **Adopt Anthropic's skill-granularity rule directly**, since none of the three KBs address it and the live `CLAUDE.md` already lists 10 skills with more implied. Concretely: keep each skill's `SKILL.md` to what's needed to decide *whether* and *how* to start; push procedural detail, templates, and edge cases into referenced files loaded on demand.

5. **Make subagents strictly ephemeral and tool-scoped**, matching the Claude Code model, and reserve "named persistent agent" only where there's a genuine reason (durable memory, durable ownership of an artifact class, cross-session identity) — not simply because a task recurs. This directly resolves the Old-Apex-Full-Orchestration KB vs. Claude Code subagent-model conflict without discarding Old-Apex-Full-Orchestration KB's genuinely useful ideas (delegation-bounds rules, handoff schema).

6. **Standardize one handoff schema across all three systems**, built from Old-Apex-Full-Orchestration KB's most complete version (role, state/status, target surface, next state, prerequisites, expected action, unresolved risk) but generalized to also cover Plan-Sync-Session KB's proposal/compute/mutation lifecycle stage and Operator-Research KB's four-role routing. One handoff schema, reused everywhere, rather than three different "packet" shapes (`weekly_plan_packet`, `flow_recap_packet`, `apex_plan_packet`, etc. as currently enumerated in `CLAUDE.md`).

7. **Decide where operator gates live once, not per-system.** All three systems independently reinvent an operator/human-approval gate (Operator-Research KB's independent-validation-gate, Old-Apex-Full-Orchestration KB's VERIFY/LOCK states, Plan-Sync-Session KB's `operator_validation: confirmed` + `approve ingest` phrase). Consolidate to a single gate primitive (a required field + a required literal phrase, matching Plan-Sync-Session KB's concrete implementation, since it's the only one with an actual mechanism rather than a described concept) and reuse it everywhere consequential mutation happens.

8. **Explicitly rank source authority once, project-wide**, using Operator-Research KB's authority order (Claude-native research > historical Apex/Hermes design evidence > PM/KB/PD options > indexes/rankings) as the template, and apply the same three-tier authority model to Old-Apex-Full-Orchestration KB's much larger and more heterogeneous corpus (mirrored trees, historical logs, MISTAKES files) before any of Old-Apex-Full-Orchestration KB's content is treated as a design decision rather than raw evidence.

---

# DEVIATIONS

- Old-Apex-Full-Orchestration KB (`old-apex-full-orchestration-agent-kb-v2`) has **no `wiki/` directory** — Phase 2 has not been compiled/approved yet. Per the handover's fallback rule, I listed its top-level tree (one level via Glob) and read the 3 available Phase 1 ingest-analysis summary files (`phase1-agent-architecture.md`, `phase1-resilient-workflows.md`, `phase1-failure-evidence.md`) plus `manifests/phase0/phase0-navigation-report.md` as the best available structural description. This is pre-approval analysis, not compiled/approved KB content — treat Old-Apex-Full-Orchestration KB's findings above as lower-confidence than Systems 1 and 3.
- Attempted to read `apex-plan-sync-session-workflow-v2/ingest-analysis/phase1-completion-report.md` (referenced by the wiki index) — the file does not exist at that path in the current repo state; the wiki index's pointer is stale or the file was relocated. Not read; not load-bearing for the conclusions above since the wiki concept pages (which do exist) already carry the equivalent claims.
- Did not open any raw source notes, deep-research prompt bodies, or leaf logs in any of the three KBs — synthesis above is index/wiki-tier only, as scoped.
- Practitioner sources beyond the required Anthropic/MCP set were not separately searched, since the five official sources already supplied concrete, actionable patterns for every category the handover asked for (single/multi-agent selection, subagent scoping, skill structure, context management, failure/observability was covered by context-engineering + KB failure-evidence pages, and anti-patterns were named in each official source).
