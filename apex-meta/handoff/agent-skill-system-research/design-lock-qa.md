---
doc_type: design-lock-qa
task_id: agent-skill-system-research-run
version: 1
created: 2026-07-11
authority: decision-forcing-qa
mode: read-only-research-and-synthesis
instructions: >
  Answer by picking or editing an option per question. Every question has a RECOMMENDED
  default so silence is not a blocker, but the operator's actual answer overrides it.
  These decisions gate building — nothing should be scaffolded until this file is answered.
---

# Design Lock Q&A — Unifying the Three Orchestration KBs into One System

## Q1. Topology: single agent, workflow, or multi-agent?
**Options:**
- A. Single Claude session running fixed workflows (skills), no persistent subagents at all.
- B. **RECOMMENDED** — Fixed workflow backbone (the existing PreCap→FlowRecap→APSU loop) with ephemeral, task-scoped subagents spawned only for bounded side-work (research fan-out, deep KB reads, verification passes).
- C. Full multi-agent system with several always-on named agents holding independent state.

**Rationale:** All three KBs and Anthropic's own guidance converge on "small stable core + temporary specialization," not a large persistent roster. Option C is what Old-Apex-Full-Orchestration KB's nine-agent design drifted toward and is explicitly the pattern all three sources warn against.

**Blast radius:** Determines whether "agents" in Apex means Claude Code subagents (ephemeral, per-task) or named personas with persistent memory/state files. Locks the answer to Q5 and Q7 as a consequence.

---

## Q2. How do the three KB systems relate: merge, layer, or one orchestrates the others?
**Options:**
- A. Merge all three into one flattened design doc, discarding system boundaries.
- B. **RECOMMENDED** — Layer them: Plan-Sync-Session KB (apex-plan/sync/session) supplies the state-mutation boundary; Operator-Research KB (four-role control plane) supplies the routing/authorship roles that operate within that boundary; Old-Apex-Full-Orchestration KB supplies translated patterns (handoff schema, anti-canonization rule) but not its literal nine-agent roster or state machine.
- C. Treat one system as authoritative and the other two as fully superseded/discarded.

**Rationale:** §3 decision 1 in the best-practice report — none of the three is wrong, but they answer different questions (who decides vs. who computes vs. who confirms). Discarding any one loses a genuinely load-bearing idea (Old-Apex-Full-Orchestration KB's handoff schema and anti-canonization rule are the most concrete of the three).

**Blast radius:** Determines whether Old-Apex-Full-Orchestration KB needs its own Phase 2 wiki compiled at all, or whether it's mined once for patterns and then left as historical evidence per its own KB's `exclude_from_context`-style treatment.

---

## Q3. Skill granularity: how big can one `SKILL.md` get before it must split?
**Options:**
- A. No fixed rule — split only when the operator notices a problem.
- B. **RECOMMENDED** — Adopt Anthropic's rule directly: keep `SKILL.md` to "decide whether + how to start"; push procedural detail, templates, and edge-case handling into referenced files loaded on demand; split when the file becomes "unwieldy" or covers mutually-exclusive contexts.
- C. Hard numeric line count cap per `SKILL.md`, enforced mechanically.

**Rationale:** This is the one area where none of the three Apex KBs have an opinion — it's a pure gap, not a conflict — so defer to the only source that does (Anthropic's Agent Skills guidance).

**Blast radius:** Governs how the 10 skills already listed in `CLAUDE.md` should be authored/refactored going forward, and whether new skills get one file or a directory with sub-files from day one.

---

## Q4. How are subagents spawned and scoped?
**Options:**
- A. Ad hoc — spawn a general-purpose agent whenever a task feels big.
- B. **RECOMMENDED** — Only define a named subagent when the same worker type is spawned repeatedly with the same instructions (per Claude Code's own guidance); otherwise use a one-off `Agent` call. Every subagent gets an explicit, narrow tool allowlist and a `description` precise enough that the parent never has to guess when to delegate.
- C. One universal "worker" subagent used for everything, with full tool access, to minimize definition overhead.

**Rationale:** Matches Claude Code's documented model exactly (`code.claude.com/docs/en/sub-agents`) and directly resolves the Old-Apex-Full-Orchestration KB vs. Claude Code conflict identified in §2 of the report (Old-Apex-Full-Orchestration KB treats agents as persistent named identities; Claude Code's are ephemeral and task-scoped).

**Blast radius:** Determines whether Old-Apex-Full-Orchestration KB's nine named agents (`alfred`, `meta_ops`, `meta_strategy`, `meta_detective`, `special_ops__*`) get reborn as Claude Code subagent definitions 1:1, or whether most of them collapse into workflow steps / skills with no persistent agent identity at all. Recommendation implies mostly the latter.

---

## Q5. What is the shared context/state model across the unified system?
**Options:**
- A. Every workflow keeps its own local state file with no shared schema.
- B. **RECOMMENDED** — One shared handoff/state schema (role or package, status, target surface, next state, prerequisites, expected action, unresolved risk — generalized from Old-Apex-Full-Orchestration KB's handoff rule) reused by every workflow's packet type (`weekly_plan_packet`, `flow_recap_packet`, `apex_plan_packet`, etc.), instead of each packet type inventing its own shape.
- C. A single monolithic state file that every workflow reads/writes directly.

**Rationale:** §3 decision 6. Reduces the real risk already visible in `CLAUDE.md`'s artifact_paths table — five+ packet types with no declared common shape — without requiring a new database or runtime.

**Blast radius:** Every skill's output contract changes shape once; this is the highest one-time migration cost of any decision here, but it's a schema change, not an architecture change.

---

## Q6. Where do operator/human-approval gates live?
**Options:**
- A. Each skill defines and enforces its own gate independently (current de facto state — PreCap gates, KB's `approve ingest` phrase, Session's `operator_validation: confirmed` field are all separate mechanisms).
- B. **RECOMMENDED** — One reusable gate primitive: a required `operator_validation` field plus (for phase transitions) a required literal confirmation phrase, matching Plan-Sync-Session KB's already-working KB implementation — reused verbatim by every workflow that mutates durable state, rather than each workflow reinventing its own gate phrase/field.
- C. Remove per-skill gates and replace with a single project-wide "autonomous mode" toggle.

**Rationale:** Plan-Sync-Session KB is the only one of the three KBs with an actual implemented mechanism (not just a described concept) for this — `phase2_allowed: false` + `approve ingest`, and `operator_validation: confirmed`. Reuse what already works rather than inventing a fourth gate design.

**Blast radius:** Locks the literal field names/phrases used everywhere state mutation is gated — a naming decision more than an architectural one, but it needs to be made once and then never re-litigated per skill.

---

## Q7. Drift-control mechanism: how is "conceptual drift" (same term, different meaning across systems) prevented going forward?
**Options:**
- A. No formal mechanism — rely on the operator to notice drift during review.
- B. **RECOMMENDED** — A single project-level glossary file (one page, not a governance framework) that pins the canonical meaning of the handful of terms that have already drifted across these three KBs (e.g., "role" vs. "state" as the unit of permission, "agent" as ephemeral subagent vs. persistent named identity, "handoff packet" shape). Every skill's `SKILL.md` references this glossary instead of redefining terms locally.
- C. A dedicated drift-detection skill that runs periodically to flag terminology mismatches automatically.

**Rationale:** Anti-overengineering constraint rules out C (a new automated governance layer). A is what's currently happening and is exactly how Operator-Research KB/2/3 ended up drifting in the first place (each KB's own `source-authority-and-connection-map.md`-equivalent page independently invented its own authority-ranking language). One glossary page is the smallest concrete fix.

**Blast radius:** Small and reversible — it's a single reference file, not a process. If it's not helping, delete it; if it is, it's the one place future skill authors check before reusing an ambiguous term like "role."

---

## Q8. What happens to Old-Apex-Full-Orchestration KB's nine-agent roster and BUILD/VERIFY/LOCK state machine specifically?
**Options:**
- A. Implement it as-is: nine persistent named Claude Code subagents, each carrying the BUILD/VERIFY/LOCK state machine.
- B. **RECOMMENDED** — Translate, don't revive: extract the two genuinely reusable ideas (the handoff schema in Q5, and the anti-canonization/candidate-vs-canon separation rule) into the unified design; do not create nine persistent agents or a formal state machine. Where a BUILD→VERIFY transition is needed, express it as a workflow step with an explicit validator sub-step, not a named permanent "VERIFY-state agent."
- C. Discard Old-Apex-Full-Orchestration KB entirely as pre-Claude-native legacy design.

**Rationale:** This is Operator-Research KB's own rank-1 rule (`prompt-flow...` Translation Rule) applied consistently: historical runtime language is evidence to translate, never a specification to revive. C throws away real value (Old-Apex-Full-Orchestration KB has the most concrete failure-mode analysis of the three KBs); A recreates exactly the proliferation problem every source warns against.

**Blast radius:** This is the decision most likely to be contested — it directly overrides the most detailed and mechanically-specified of the three systems. If the operator disagrees, everything downstream in Q1/Q4/Q8 needs re-answering together, since they're coupled.
