---
doc_type: design-lock-qa
task_id: agent-skill-system-research-run
created: 2026-07-11
authority: research-questions-for-fable
mode: read-only-research-and-synthesis
instructions: >
  These are open research questions Fable resolves itself, using claude-code-orchestration-design
  (best-practice reference) and the actual intents/contracts of the systems in scope — Fable's
  reasoning tokens are spent clarifying and deciding these, not accepting a pre-picked answer.
  Where the operator gave a starting hypothesis, it's marked as a hypothesis to verify, not a
  locked answer.
scope: >
  In scope: apex-plan / apex-sync / apex-session (the three-package system) and the old Apex
  agent-swarm system (old-apex-full-orchestration-agent-kb + -v2). claude-code-orchestration-design
  is the best-practice reference guiding how to bring them together.
---

# Design Lock Q&A — Core Research Questions for Fable

## Q1. Topology: single agent, workflow, or multi-agent?
**Operator's starting hypothesis (verify, don't assume):** Likely multi-agent, with `apex-plan`/`apex-sync`/`apex-session` integrated underneath a meta-ops-style agent (matching the `meta_ops` role in the old Apex KB).

**Candidate directions to weigh:**
- A. Single Claude session running fixed workflows (skills), no persistent subagents at all.
- B. Fixed workflow backbone with ephemeral, task-scoped subagents spawned only for bounded side-work.
- C. Full multi-agent system with several always-on named agents holding independent state (the operator's hypothesis leans here, but scoped — not the old system's full nine-agent roster; see Q8).

**What Fable needs to check:** `claude-code-orchestration-design`'s agent-subagent-design and workflow-design pages, the actual current `apex-plan`/`apex-sync`/`apex-session` skill contracts, and the old Apex KB's role model.

**Blast radius:** Determines whether "agents" in this build means Claude Code subagents (ephemeral, per-task) or named personas with persistent memory/state files. Coupled with Q4 and Q8.

---

## Q2. How do the systems in scope relate: merge, layer, or one orchestrates the others?
**Operator's starting hypothesis:** Planning/session work likely runs *as* the meta-ops layer — i.e., `apex-plan`/`apex-sync`/`apex-session` isn't a peer system but a component under a meta-ops agent.

**Candidate directions:**
- A. Merge everything into one flattened design, discarding system boundaries.
- B. Layer them: the three-package system supplies the state-mutation boundary; the old Apex KB supplies translated patterns (handoff schema, anti-canonization rule) but not its literal roster/state machine.
- C. Treat one system as authoritative and the other as fully superseded.

**Blast radius:** Determines whether the old Apex KB needs anything built from it directly, or is mined once for patterns and left as historical evidence.

---

## Q3. Skill granularity: how big can one `SKILL.md` get before it must split?
**Candidate directions:**
- A. No fixed rule — split only when a problem is noticed.
- B. Anthropic's own rule: keep `SKILL.md` to "decide whether + how to start," push detail into referenced files, split when unwieldy or covering mutually-exclusive contexts.
- C. Hard numeric line-count cap, enforced mechanically.

**Blast radius:** Governs how every skill in this build gets authored/refactored, and whether new skills get one file or a directory with sub-files from day one.

---

## Q4. How are subagents spawned and scoped?
**Candidate directions:**
- A. Ad hoc — spawn a general-purpose agent whenever a task feels big.
- B. Only define a named subagent when the same worker type is spawned repeatedly with the same instructions; otherwise a one-off call. Explicit, narrow tool allowlist and a precise `description` per subagent.
- C. One universal "worker" subagent used for everything, full tool access.

**What Fable needs to check:** Whether the old Apex KB's named roster (`alfred`, `meta_ops`, `meta_strategy`, `meta_detective`, `special_ops__*`) should become real Claude Code subagent definitions, collapse into workflow steps, or something in between — coupled directly to Q1 and Q8.

---

## Q5. What is the shared context/state model across the unified system?
**Candidate directions:**
- A. Every workflow keeps its own local state file with no shared schema.
- B. One shared handoff/state schema (role/package, status, target surface, next state, prerequisites, expected action, unresolved risk), reused by every in-scope packet type (`apex_plan_packet`, `apex_sync` reports, `apex_session` H6 handoff artifacts) instead of each inventing its own shape.
- C. A single monolithic state file every workflow reads/writes directly.

**Blast radius:** Every skill's output contract changes shape once if B is chosen.

---

## Q6. Where do operator/human-approval gates live?
**Candidate directions:**
- A. Each skill defines and enforces its own gate independently (current de facto state — `apex-kb`'s `approve ingest` phrase and `apex-session`'s `operator_validation: confirmed` field are already separate mechanisms).
- B. One reusable gate primitive — a required `operator_validation` field plus, for phase transitions, a required literal confirmation phrase — reused verbatim by every workflow that mutates durable state.
- C. Remove per-skill gates, replace with a single project-wide "autonomous mode" toggle.

**Blast radius:** Locks the literal field names/phrases used everywhere state mutation is gated, if B is chosen.

---

## Q7. Drift-control mechanism: how is "conceptual drift" (same term, different meaning across systems) prevented going forward?
**Candidate directions:**
- A. No formal mechanism — rely on the operator to notice drift during review.
- B. A single project-level glossary file pinning canonical meaning for terms that have already drifted (e.g. "role" vs. "state" as the unit of permission).
- C. A dedicated drift-detection skill running periodically.

**Blast radius:** Small and reversible regardless of which is chosen.

---

## Q8. What happens to the old Apex KB's nine-agent roster and BUILD/VERIFY/LOCK state machine specifically?
**Candidate directions:**
- A. Implement it as-is: nine persistent named Claude Code subagents, each carrying the BUILD/VERIFY/LOCK state machine.
- B. Translate, don't revive: extract reusable ideas (handoff schema, anti-canonization/candidate-vs-canon separation) into the unified design without reviving the literal roster or state machine.
- C. Discard the old Apex KB entirely as pre-Claude-native legacy design.

**Blast radius:** Whichever way this goes, Q1 and Q4 need to be answered consistently with it — they're coupled, not independent.
