---
title: "Evaluation Matrix — Milestone 3"
purpose: >
  Per-dimension comparison of the two systems being merged (old Apex v2's 9-agent
  roster + BUILD/VERIFY/LOCK state machine vs. the current apex-plan/apex-sync/apex-session
  three-package boundary), scored against the resilience dimensions milestone 2 extracted
  from claude-code-orchestration-design. Explicit per-dimension findings with citations,
  not a prose verdict.
created: 2026-07-11
status: "drafted from fan-out research pass — awaiting operator verification (milestone 3 gate)"
---

```okf
document:
  id: fable-orchestrator-evaluation-matrix
  title: Evaluation Matrix
  status: drafted_not_verified
  created_date: 2026-07-11
  repository: leela-spec/apexai-os-meta
  package_path: apex-meta/fable-orchestrator/

scope:
  owns:
    - milestone_2_dimension_definitions_with_citations
    - milestone_3_per_dimension_scoring
    - thin_dimension_flags_for_external_research
  must_not_own:
    - final_architecture_decisions   # those live in design-lock answers (milestone 4)
    - user_stories_content
```

# Evaluation Matrix

## 1. The dimensions (milestone 2 — extracted from `claude-code-orchestration-design`, cited)

Extraction pass run 2026-07-11 over the KB's four load-bearing pages:
`wiki/summaries/minimal-claude-orchestration-architecture.md`,
`wiki/summaries/agent-skill-orchestration-resilient-workflows.md`,
`wiki/summaries/apex-application-orchestration-patterns.md`,
`wiki/summaries/agent-vs-subagent-vs-skill.md`.

### D1 — Mechanism-ladder position

Seven-rung ladder: plain Markdown/YAML artifact → skill → workflow → ephemeral subagent → persistent agent → deterministic script/hook → plugin/MCP. Rule: "start every design question with the smallest mechanism … and move up the ladder only when the current rung provably cannot carry the work safely, auditably, or token-efficiently." "'Minimal' means smallest mechanism sufficient for the task, not fewest total mechanisms ever used."
— `minimal-claude-orchestration-architecture.md` (C001, Macro/Meso; compile plan lines 38–137). Lower-rung criteria (main-conversation vs. skill vs. subagent): `agent-vs-subagent-vs-skill.md` C001–C004. Confidence: high.

### D2 — State-holding location

"Resilience is a property of *where the plan lives*, not of which agent is doing the work." Subagents/skills hold state in Claude's context window (turn restarts on interruption); workflows hold loop+variables in a script (resumable); agent teams coordinate via a shared task list (peers keep running).
— `agent-skill-orchestration-resilient-workflows.md` (C001, C002, Macro; workflows doc lines 21–32). Confidence: high.

### D3 — Adversarial cross-check

"Workflows can apply a repeatable quality pattern that subagent chains cannot on their own: independent agents adversarially reviewing each other's findings … before anything is reported." Explicitly NOT available at the subagent layer alone (C004).
— `agent-skill-orchestration-resilient-workflows.md` (C003, C004). Confidence: high as a claim; **thin as implementable mechanics** (single source line; agent-teams review properties unverified, U001).

### D4 — Role-vs-state permission separation

**Thin in the reference KB.** Coverage is limited to: subagent tool-restriction enforcement (`agent-vs-subagent-vs-skill.md` C002), a generic guidance-vs-enforcement distinction (`minimal-…` — settings/permissions/hooks as the enforcement rung), and named-but-unexplained related concepts (owner-validator-split, role-boundary-and-non-ownership in `apex-application-orchestration-patterns.md`). No page frames role-permission vs. state-mutation-permission as a distinct axis. The in-scope systems themselves (old Apex v2's explicit "role ≠ permission, state does") are ahead of the reference KB here.

### D5 — Context-budget handling

Partial. Token-efficiency is "the test each rung must pass before being adopted" (`minimal-…`, token_economy index, load-every-session vs. only-when-triggered); subagent isolation framed as a context-budget tool (isolate verbose output — `agent-vs-subagent-vs-skill.md` C002); scale limits tied to state location (subagents/skills = a few tasks per turn; workflows = dozens–hundreds, script-held). **No numeric budgets, no compaction/summarization strategy.** (Fable-side handling exists separately in `fable-execution-best-practices.md` §5–6.)

### D6 (adjacent, checked because milestone 4 needs it) — Operator/human gates

**Essentially absent from the reference KB's workflow guidance** — the only gates described are KB-compilation deferral gates (U001–U003 ask_operator flags), not in-run human-approval checkpoints. The in-scope systems (apex-session's `operator_validation: confirmed`, apex-kb's `approve ingest`) are the concrete mechanisms; the reference KB does not adjudicate between them.

### Thin dimensions → routed to external research (per model-routing table)

Per milestone 2's own rule ("where the KB itself is thin on a specific question, produce a prompt for an external model instead of guessing"), these four go to external models — prompts in `prompts/` (authored this session):

1. Role-vs-state permission separation in agent orchestration (D4) — ChatGPT deep research.
2. In-run operator-gate / human-approval checkpoint patterns (D6) — ChatGPT or Gemini.
3. Concrete adversarial cross-check wiring (D3 mechanics) — Gemini deep research.
4. Persistent-agent escalation criteria (ladder rung 5, deferred as U001 in the KB) — ChatGPT pro-thinking.

## 2. Per-dimension scoring (milestone 3)

Two fan-out research passes (2026-07-11), one per system, each grounded in the real files cited below.

### Comparison table

| Dimension | Old Apex v2 (9-agent roster + BUILD/VERIFY/LOCK) | apex-plan / apex-sync / apex-session |
|---|---|---|
| **D1 Mechanism ladder** | Sits high on the persistent-agent/governance rung but is **doc-only**: 9 persistent named agents + written canon, no hooks, no scripts, no MCP; skills/plugins explicitly demoted to "optional capability surfaces, not authorization or architectural law". The BUILD/VERIFY/LOCK machine is documented, never coded. | Uses the **low rungs deliberately**: plain Markdown/YAML contracts + skills + one deterministic stdlib-only script (`scripts/apex_sync.py`, dry-run-first, `--json`). No subagents, hooks, plugins, or MCP. Closer to the reference KB's "smallest sufficient mechanism" rule. |
| **D2 State-holding** | State externalized to durable governed files: every material task must carry role + state + target surface + intended output as an explicit record; "silent continuation from an unclear handoff is invalid"; handoff continuity may not depend on hidden reasoning. Strong on paper, but no runtime ever enforced it. | State fully externalized **and real**: per-task Markdown+frontmatter under `apex-meta/epics/<slug>/NNN.md`, derived registry (`apex-meta/registry/index.md`, script-regenerated), H6 handoff artifacts on disk under `apex-meta/handoff/`. |
| **D3 Adversarial cross-check** | **Strong and structural**: dedicated adversarial agent (`meta_detective` — challenge/contradiction/drift, cannot execute its own findings), plus VERIFIER/AUDITOR roles separated from the BUILD owner, plus "any durable cross-agent change above T0 requires a second verifying role". | **Absent**: grep across all three skills + KB for adversarial/independent-review/cross-check/challenge = zero hits. The script is an independent *recomputation* (determinism check), not a critique. Only challenge points are human operator gates. (`source-authority-and-verdict-packet` exists in the repo but is outside these packages.) |
| **D4 Role-vs-state permission** | **The design's central invariant**: "Roles remain the semantic accountability layer. Operational states are the real permission layer. No role label may be used as compliance theater for permissions the current state does not grant." Deriving permission from a role name is an explicitly invalid pattern. | **Role-based capability partitioning plus a state gate on the single write path**: each skill hard-forbids the others' capabilities; mutation additionally requires `operator_validation: confirmed`, `no_implicit_apply: true`, and registry writes require explicit `--dry-run false` behind a drift-report-first check. Not a general per-state permission model. |
| **D5 Context budget** | Partial, architectural: compact `AGENTS.base.md` anchor ("must remain compact"), per-agent `ESSENCE.md` compact doctrine, index-first canonical read order, built search index. No token accounting. | Partial, **implemented**: compact SKILL.md contracts (~8–11 KB), all detail factored into `references/` behind explicit `read_when` tables, templates loaded on demand, size-tier variants (`.dr.md`/`.pro.md`), exact computation pushed out of context into the script. No token accounting either. |
| **D6 Operator gates** | Implied via VERIFY/LOCK states and escalation verdicts; no concrete field/phrase mechanism. | **The only concrete implemented mechanism in scope**: `operator_validation ∈ {confirmed, rejected, needs_revision, not_requested}`, gate statuses `operator_review_needed / approved_for_handoff / needs_revision`, `requested_operator_action: approve|revise|reject|split|defer`, 3-step confirm chain (approve packet → prepare delta → confirm delta → apply). |

Key evidence anchors — old v2: `raw/other/managed/rules/AGENT_SWARM_INTERACTION_CANON.md` L57–59, L169–252, L349–411, L505–544; `managed/agents/meta_detective.md`; `wiki/concepts/role-state-permission-separation.md` (RS01–RS04); `managed/rules/AGENTS.base.md` L1–39. Three-package: `.claude/skills/apex-plan/SKILL.md` L73–91; `.claude/skills/apex-sync/SKILL.md` L16–23, L78–109, L135–137; `.claude/skills/apex-session/SKILL.md` L27–34, L198, L259; `.claude/skills/apex-session/references/mutation-gate-rules.md` L217–249; `.claude/skills/apex-sync/references/script-command-contract.md` L195–262; `scripts/apex_sync.py` L1–9, L26–27, L84–142, L864–891.

### Verdict shape (per-dimension, not prose-only)

The two systems are **complementary opposites**, which is the strongest possible argument for layering (Q2-B) rather than choosing a winner:

- Old v2 **wins on theory** for D3 (adversarial cross-check) and D4 (role-vs-state invariant) — but nothing was ever mechanized; its whole permission layer is prose law with no enforcement surface.
- The three-package system **wins on mechanism** for D1, D2, D5, D6 — real files, real script, real gate fields — but has no adversarial AI cross-check at all (D3 = absent), the exact failure mode the reference KB names as already-observed ("structurally complete, semantically ungrounded output").
- Neither system does token/context accounting (D5 partial for both); both converge independently on compact-anchor + index-first/read-on-demand retrieval.

Merge implication (feeds milestone 4, not decided here): keep the three-package mechanization as the backbone; translate v2's Detective-style adversarial review into a concrete workflow step; adopt v2's handoff-record fields and its permission invariant as the rule governing any new mutation surface.

### Corrections to prior records made from this pass

1. **`old-apex-full-orchestration-agent-kb-v2` IS Phase-2 compiled** — `wiki/index.md` (auto-generated 2026-07-11T11:42:03Z) states "Compiled page count: 17"; 19 compiled page files exist on disk (index undercounts by 2: `explicit-handoff-continuity.md`, `role-state-permission-separation.md` present but unenumerated; 6 "Untitled topic" placeholders remain). `ORCHESTRATION-SYSTEMS-INDEX.md`'s "Phase 1 only, no Phase 2 wiki" row was stale and has been corrected this session. Discovery-notes §2's discrepancy flag is resolved in favor of "Phase 2 exists, compilation real but incomplete."
2. `apex-meta/registry/index.md` does not currently exist on disk — the derived index has never been materialized; the only live epic data is `apex-meta/epics/narm-support-knowledgebase/` (8 tasks). Relevant to milestone 6 simulation planning.

## 3. Open items for the operator

1. §1 is a research-pass extraction of milestone 2 — verify before treating the dimensions as locked.
2. §2 scoring cites live skill files and the v2 canon — spot-check the load-bearing quotes.
