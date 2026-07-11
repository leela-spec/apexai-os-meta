---
title: "External Research Pack — 2026-07-11"
purpose: >
  Copy-paste prompts for the external models (per fable-execution-best-practices.md §2-3),
  covering the dimensions the reference KB is thin on (evaluation-matrix.md §1) plus one
  repo-grounded verification pass. Operator copies each prompt out, pastes the result back;
  Fable grounds every returned claim against real repo state before acting (§4 verification
  contract) and writes the verified extract to a file immediately (§5).
created: 2026-07-11
status: authored_not_yet_dispatched
routing_note: "One primary objective per prompt. P1/P3 → ChatGPT (deep research / pro thinking). P2/P4 → Gemini (research+write combined in one instruction, per its prompt rule). P5 → Perplexity (GitHub connector required)."
---

# P1 — ChatGPT (deep research): role-vs-state permission separation

Act as an agentic-systems architecture reviewer specializing in multi-agent orchestration governance.

**Task (single objective):** Research how production agent-orchestration systems separate *role-based* permissions (what an agent identity may do) from *state-based* permissions (what the current lifecycle state of an artifact/task permits), and produce a ranked set of concrete, implementable patterns for enforcing "role is accountability, state is permission" in a file-based orchestration system.

**Context you need (we cannot give you repo access — this is the relevant design law, quoted):**
> "Roles remain the semantic accountability layer. Operational states are the real permission layer. No role label may be used as compliance theater for permissions the current state does not grant."

Our system: Claude Code skills/subagents; state lives in Markdown files with YAML frontmatter; the one mutation path is gated by a field `operator_validation: confirmed` plus dry-run-first script writes. Roles: 4 durable accountabilities (intake, strategy, orchestration/integration, independent validation). We do NOT want a full state machine unless evidence demands it.

**Output format:** A ranked table (pattern | what it enforces | enforcement surface (file schema / hook / review step) | failure mode it prevents | adoption cost), max 8 rows, followed by a ≤200-word recommendation for our specific setup. Inline citations/links on every row — uncited claims will be discarded.

---

# P2 — Gemini (deep research, research+write in ONE pass): in-run operator-approval gate patterns

Act as a human-in-the-loop (HITL) workflow-design researcher. Research current (2025–2026) best practice for human-approval checkpoints inside AI agent workflows — approval field conventions, confirmation-phrase patterns, risk-weighted gating (full review only for consequential actions), and gate-bypass failure modes — AND, in the same response, write a concise design note (≤600 words) recommending how a file-based agent-orchestration system should implement ONE reusable gate primitive.

Constraints to design against: the gate is a required YAML field `operator_validation` (values: confirmed / rejected / needs_revision / not_requested) plus a required literal confirmation phrase for phase transitions; gates must be consequential-not-constant (risk-weighted); no global "autonomous mode" toggle. Cite every external claim inline with links. Structure: (1) findings table (pattern | source | relevance), (2) the design note, (3) open risks list.

---

# P3 — ChatGPT (pro thinking): adversarial cross-check wiring mechanics

Act as an LLM-orchestration quality-engineering specialist.

**Task (single objective):** Design the concrete wiring for an independent adversarial-review step in an orchestrator-worker system, given that our reference research established WHAT it is ("independent agents adversarially reviewing each other's findings before anything is reported") but not HOW to wire it.

**Context:** Reviewer role ("Detective") issues criterion-level verdicts (pass / revise / hold / needs_input / escalate), names the owner of each defect, may NOT implement fixes, and corrected work is re-reviewed (the artifact, not the correction claim). Workers are ephemeral, context-isolated, and return structured packets (sources, assumptions, uncertainties, stop conditions). Orchestration runs in Claude Code (skills + ephemeral subagents + file-held state).

**Output format:** (1) a numbered wiring spec (≤10 steps) with explicit inputs/outputs per step; (2) the reviewer's input-packet schema as YAML; (3) a short list of known failure modes of LLM-vs-LLM review (sycophancy, rubber-stamping, shared-blind-spot correlation) with one mitigation each, citing sources inline for every failure-mode claim.

---

# P4 — Gemini (deep research, research+write in ONE pass): persistent-agent escalation criteria

Act as an agentic-systems researcher. Research when multi-agent frameworks and practitioner guidance (2025–2026) justify promoting an ephemeral, per-task subagent into a persistent named agent with durable identity/memory/state — the concrete escalation criteria, the costs (state drift, stale memory, permission creep), and documented cases where persistent agents were the wrong call — AND write, in the same response, a checklist (max 8 items) our team can apply per candidate role to decide "stays ephemeral" vs. "becomes persistent."

Context: our current design keeps 4 durable *accountabilities* as tool-scoped subagent definitions invoked per-run (no standing state beyond files on disk); the open question is what future evidence would justify giving any of them persistent memory. Cite every claim inline. Structure: (1) findings with citations, (2) the checklist, (3) ≤150-word recommendation for our default.

---

# P5 — Perplexity (GitHub connector — repo-grounded verification)

Use your GitHub connector on the repository `leela-spec/apexai-os-meta` (branch: claude/fable-orchestrator-setup-9pc5pu).

Act as an adversarial fact-checker. **Task (single objective):** Verify or refute each factual claim in the file `apex-meta/fable-orchestrator/evaluation-matrix.md`, section "2. Per-dimension scoring", against the actual files it cites — especially:
1. `.claude/skills/apex-plan/SKILL.md`, `.claude/skills/apex-sync/SKILL.md`, `.claude/skills/apex-session/SKILL.md` — do the quoted field names, line ranges, and "must not" boundaries actually appear?
2. `scripts/apex_sync.py` — is it standard-library-only, dry-run-first, with registry as the only write?
3. `apex-meta/kb/old-apex-full-orchestration-agent-kb-v2/raw/other/managed/rules/AGENT_SWARM_INTERACTION_CANON.md` — does the verbatim permission-layer quote appear, and do the cited line ranges match?
4. Does `apex-meta/registry/index.md` exist in the repo or not?
5. Does `apex-meta/kb/old-apex-full-orchestration-agent-kb-v2/wiki/index.md` state "Compiled page count: 17", and how many compiled page files actually exist under that `wiki/`?

**Output format:** A table (claim | verified / refuted / partially | exact evidence: file path + what you found), one row per numbered item plus one row per additional material claim you checked. Do not summarize the matrix — audit it. Flag anything you could not access rather than guessing.
