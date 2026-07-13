# Orchestration Betterment — Master Plan (v3)

This file has three parts:
- **PART 1 — Preserved Plan v2** (token-efficiency betterment; unchanged, remains the execution
  baseline; on execution it is also persisted into the repo at
  `apex-meta/fable-orchestrator/orchestration-betterment-plan-v2.md` so future sessions can read it).
- **PART 2 — Learnings → KB** (the distilled "what matters most" written as a legal wiki page into
  the claude-code-orchestration-design KB).
- **PART 3 — Deep-dive v3 corrections** (new, deeper findings from the multi-agent audit: handoff
  quality, loop composition, PM alignment, simplicity, drift resistance, composability for future
  systems — adversarially verified, ranked by impact-per-effort).

---

# PART 1 — Preserved Plan v2: Token-Efficient, Resilient, Target-Focused Orchestration

## Context

Two orchestration systems live on `main`: **Fable** (`apex-meta/orchestration/`, general-purpose) and
the **Weekly Orchestrator** (`.claude/skills/weekly-orchestrator/` + `.claude/CLAUDE.md`). A deep
eight-dimension audit found both implement the best-practice KB
(`apex-meta/kb/claude-code-orchestration-design/`) closely at the detail level — but the FIRST pass
missed the macro question: **what does every session pay for before any work starts?**

Measured always-loaded footprint per session in this repo:
- `CLAUDE.md`: 81 lines / ~1,600 tokens — mostly the weekly-loop contract (core_loop, skills table,
  agents table, artifact paths), duplicated inside `weekly-orchestrator/SKILL.md`.
- ~25 project skill descriptions (always injected for triggering) — several at 100–150+ words vs the
  KB's own ≤75-word contract and the external ~100-token guideline.
- 17 agent descriptions (both systems, always advertised).

Authority for the fix — KB (settled, high-confidence) + external verification (2026):
- KB `wiki/concepts/compact-activation-file.md`: activation files carry ONLY trigger metadata, scope
  boundary, next-read pointers; full instructions load on activation; schemas/contracts go to
  referenced files.
- KB `informatics-design-formats-practice-guide.md`: description ≤75 words, starts "Use this skill
  when", names inputs/outputs/does-not-do. `prompt-pack-and-artifact-contract-design.md`: define every
  schema/table ONCE (`canonical_source:` pointers), a real prior defect cost ~800 tokens/load.
- External: CLAUDE.md target 300–600 tokens (>2,000 = storing what doesn't belong; benchmark 3,847→312
  tokens = 91.9% cut, no quality loss); skill idle cost ≈ name+description ≈ 100 tokens each;
  description = trigger, third-person, literal trigger phrases; SKILL.md body <500 lines (all ours
  comply already).

Key architectural verdict (answers the operator's core question): the weekly loop's *skill + stage
subagents* shape is already the right mechanism per the KB's mechanism ladder — it does NOT need to
become something else. The defect is that its full contract also sits in the always-loaded CLAUDE.md.
**Relocate, don't re-architect.** Guard-rail for the whole plan: subtraction and relocation only — no
new engines, hooks, state machines, or ceremony (KB: least-powerful-mechanism; ARCHITECTURE.md §6
deliberate-not-built list stays honored).

All work local-file only; no commit/push unless the operator asks.

---

## Tier 0 — Macro token architecture (highest leverage; pays on EVERY future session)

### 0a. CLAUDE.md → compact activation seed (~1,600 → ~400–500 tokens)
Keep: identity (2–3 lines), the hard global constraints (exclude_from_context, never-write rules,
autonomous-override rule), and one-line pointers: "Weekly loop contract: trigger `run
weekly-orchestrator` → `.claude/skills/weekly-orchestrator/SKILL.md`", "Fable orchestration:
`apex-meta/orchestration/00-START-HERE.md`", "Terms: `apex-meta/GLOSSARY.md`".
Move out (to the weekly-orchestrator skill's references, which already hold most of it): the
core_loop table, full skills table (skills self-describe via frontmatter — the table is duplicate
trigger metadata), agents table (already in SKILL.md contract), artifact_paths, session_startup
procedure. Fix the core_loop's G5/status-merge error (see 1c) in its new single home.
Every table defined once, `canonical_source:` pointer everywhere else.

### 0b. Skill-description diet (~25 skills; est. 1.5–2.5K tokens/session saved)
Rewrite every project skill's `description:` to the KB contract: ≤75 words, "Use this skill when…",
inputs → outputs, one does-not-do clause, literal trigger phrases. Worst offenders first: `apex-kb`,
`deterministic-markdown-patcher`(+2), `AIRouting`, `apex-plan`, `apex-session`, `apex-sync`,
`source-authority-and-verdict-packet`. Body content is untouched — this trims only the always-loaded
tier. (Description-trigger quality is a separate later optimization stage per KB — do not blend
content rewrites in.)

### 0c. Agent-description diet (17 agents)
Same treatment for `.claude/agents/*.md` descriptions: role, when-dispatched, one must-not — cut
narrative. Add a one-word system marker in each description ("Fable"/"Weekly loop") — this doubles as
the cheap namespace fix (replaces the heavier AGENTS-MAP idea; no new file).

### 0d. Compaction-protection note
KB C004: activated content can be silently lost to context compaction. One line in the
weekly-orchestrator SKILL.md contract: "on resume/compaction, re-read this contract before gate
decisions" — resilience for long loop sessions, zero standing cost.

---

## Tier 1 — No-regret correctness & consistency fixes

**1a. Silent preload bug (only finding that can break a live run):** three stage agents' `skills:`
values don't match the target skill's `name:` — `apex-precap-week.md` (`PrecapWeek`→`precap-week`),
`apex-precap-next-day.md` (`PrecapNextDay`→`precap-next-day`), `apex-project-status.md`
(`ProjectStatus`→`project-status-overview`). Verified: flow-recap/status-merge already match,
proving the convention.

**1b. Consumed-recap registry split (real double-merge hazard):** registry exists in BOTH
`state/consumed-recap-registry.md` and `.claude/kb/consumed-recap-registry.md`. Declare `state/`
canonical, migrate entries, point `apex-status-merge.md` at one path only, record in artifact_paths'
new home.

**1c. Loop-contract corrections (applied in its post-0a single home):** add status-merge stage with
G5 (currently the top-level loop omits it and mis-attaches G5 to APSU, contradicting handoff-schema +
every agent); state G3's nature once (currently both "always-required gate" and "capture/none");
unify the APSU artifact name (`updated_all_project_status_packet` / `all_project_status_packet` /
`current_project_status_overview` → one).

**1d. Terminology reconciliation:** one canonical snake_case name per skill across table/dir/`name:`;
System B verdict vocabulary consistent (`revise`↔`needs_revision`, `hold`↔`blocked` drift);
"consequential" defined once in GLOSSARY, referenced by `operator-gate.md`/`detective-review.md`;
invariant-5 wording unified across the three System A files.

**1e. Dead/stale content removal:** strip "# NEXT PROMPT" authoring scaffolding from
`AIRouting/SKILL.md` + `Workflow&Processes/SKILL.md`; weekly-orchestrator SKILL.md reference list —
drop the two never-consumed doctrines (hygiene-clean, informatics-design) or add their consuming
steps, add the two load-bearing ones it omits (meta-strategy-, meta-detective-doctrine); regenerate
`CURRENT-SYSTEM-MANIFEST.yaml` (lists built items as pending, stale HEAD); one "appendices are
historical; CORE.md authoritative" line per Fable doctrine domain with phantom refs.

---

## Tier 2 — Gated / higher effort (after Tier 0+1)

**2a. Decision needed — system relationship:** (a) two separate products, (b) [recommended] Fable =
general engine, Weekly = specialized loop on top sharing the plan/sync/session mutation engine,
(c) merge. Then: one governance story for `apex-plan/sync/session`; resolve `meta-ops.md`
sole-mutation-toucher vs Weekly's single-main-thread-write-path contradiction; two GLOSSARYs → one
canonical + one scoped reference.

**2b. Reconcile Fable safety docs with what was built:** `authority-state.schema.md` forbids the
separate checker that was actually built and passes tests (`scripts/orchestration_check.py
canon-write`) while calling the sanctioned embedded check "pending" — bless the built script (it also
matches KB hard-enforce-via-script doctrine). DL-1: make the authority sidecar the single source of
`authority.state` so verified artifacts stop reading `candidate` in their own frontmatter.

**2c. OPTIONAL (operator activation only, expensive):** live-run one of the five never-executed Fable
stories to populate the new `usage_evidence` telemetry block with real token numbers. Not build work.

---

## Execution order
0a → 0b → 0c → 0d → 1a → 1b → 1c → 1d → 1e (single continuous run, no per-step stops) → report →
2a decision → 2b (→ 2c only on explicit request).

## Verification
- **Token math:** before/after `wc -c` on CLAUDE.md (target ≤ ~2KB chars ≈ 500 tokens); sum of all
  skill+agent description word counts before/after (target ≤75 words each); report estimated
  per-session savings.
- **No-loss check:** every fact removed from CLAUDE.md must exist at its pointer target (grep each
  moved table/constraint in its new single home).
- **Preload:** every stage agent's `skills:` value string-equals the target skill's `name:`.
- **Terminology:** grep for retired names (`PrecapWeek`, `APSU`, `# NEXT PROMPT`,
  `updated_all_project_status_packet`, second registry path) → zero hits outside canonical
  definitions/changelogs.
- **Registry:** exactly one consumed-recap registry referenced anywhere.
- **Fable regression:** `python scripts/orchestration_check.py packet` still parses both simulation
  run folders; negative fixtures still fail closed (9/9).
- **Manifest:** every `CURRENT-SYSTEM-MANIFEST.yaml` path resolves on disk.