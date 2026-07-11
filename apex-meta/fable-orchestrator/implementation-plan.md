---
title: "Meta Implementation Plan — Final Orchestration System (Milestone 5 + 6 map)"
purpose: >
  The macro plan Fable executes to assemble the final orchestration system directly:
  target architecture, final folder layout, component specs, deterministic move map for
  already-existing usable files, build sequence, and verification. Supersedes the
  external-research path — per operator direction 2026-07-11, no external model calls;
  Fable designs and builds, existing mechanisms are reused in place or moved deterministically.
created: 2026-07-11
status: "active — being executed this session"
---

```okf
document:
  id: fable-orchestrator-implementation-plan
  title: Meta Implementation Plan
  status: active_execution
  created_date: 2026-07-11
  repository: leela-spec/apexai-os-meta
  package_path: apex-meta/fable-orchestrator/

scope:
  owns:
    - target_architecture_macro
    - final_folder_layout
    - component_specifications
    - deterministic_move_map
    - build_sequence_and_verification
  must_not_own:
    - user_stories_content
    - per_story_simulation_records   # live in apex-meta/orchestration/simulations/
```

# Meta Implementation Plan

## 0. Standing decisions this plan builds on (all previously evidenced, now operator-directed to execute)

| Source | Decision carried forward |
|---|---|
| `design-lock-answers.md` Q1/Q4 | Workflow backbone; 4 durable accountabilities + 3 specialist lanes as **named, tool-scoped, ephemerally-invoked subagent definitions**; everything else one-off workers with narrow allowlists |
| Q2 | Three-package system (`apex-plan`/`apex-sync`/`apex-session`) is the mutation backbone, **kept in place** under Meta Ops accountability |
| Q3 | Anthropic skill-granularity rule — compact SKILL.md/agent files, detail in references |
| Q5 | **One shared handoff-packet schema** for every packet type |
| Q6 | **One gate primitive**: `operator_validation ∈ {confirmed, rejected, needs_revision, not_requested}` (apex-session's implemented mechanism), applied where consequence lives |
| Q7 + research P1 | Glossary for terminology drift **plus** one minimal `authority.state` field (`candidate | verified | invalidated` + `basis_digest`) for artifact-currency drift — no state machine |
| Q8 + research P2 | Roster translated, not revived. Detective review = **two blind parallel lenses** (validity + strategic alignment), deterministic aggregation, reviewer never fixes its own finding. **Cross-family external judge: dropped** per operator direction (no external calls); residual same-family risk mitigated by the evidence-bearing PASS gate and falsification contract |
| `decisions.md` D1/D2 | This IS the final system (no v1 excuse); no defensive ceremony — only the review step and the gate primitive are added control surfaces |
| `build-plan.md` | Simulation gate: a workflow is adopted only after a real per-story run recorded in `simulations/`; regression = re-run stories on change |

## 1. Target architecture (macro)

One sentence: **a file-backed orchestration package where the operator talks to Alfred, Meta Ops runs the workflow backbone using the three apex skills for plan/compute/mutate, Meta Strategy sets direction, Meta Detective independently reviews consequential artifacts through two blind lenses, and every durable mutation passes the single operator gate carrying the shared handoff schema and the artifact-authority field.**

```
                         OPERATOR
                            │ (intake / decisions / gate confirmations)
                         [Alfred]
                            │
        ┌───────────────────┼──────────────────────┐
   [Meta Strategy]     [Meta Ops] ──────────► [Meta Detective]
   macro direction      meso workflow          independent review
   options/alignment    routing/state          (validity ∥ alignment,
        │                   │                   blind, parallel)
        │        ┌──────────┼───────────┐             │
        │   apex-plan   apex-sync   apex-session      │ verdicts route to
        │   (propose)   (compute)   (gated mutate)    │ named owners only
        │        │          │           │
        │        └── specialist lanes / domain workers (ephemeral, scoped)
        │             Knowledge Bank · Informatics Design · Prompts & Workflows
        │
   all durable artifacts: Markdown+frontmatter, shared handoff-packet schema,
   authority.state on every consequential artifact, operator_validation on every
   consequential mutation, state held in files (never in a context window)
```

Runtime mapping (Claude Code mechanisms, per the mechanism-ladder rule — smallest sufficient rung):
- **Accountabilities/lanes** → `.claude/agents/*.md` subagent definitions (name, description, narrow tool list, role contract). Invoked per-run; no always-on state.
- **Workflow backbone** → Meta Ops orchestration contract (`apex-meta/orchestration/workflows/orchestrator-run.md`) executed by the main conversation or a Workflow script; plan/state always in files.
- **Mutation** → only through apex-session's existing gate; registry writes only through `scripts/apex_sync.py --dry-run false`.
- **Review** → `apex-meta/orchestration/workflows/detective-review.md`, two fresh isolated subagent calls (validity + alignment) with blind packets, deterministic aggregation rule (precedence: escalate > needs_input > hold > revise > pass; single critical non-pass blocks; no majority vote).

## 2. Final folder layout

```
apex-meta/orchestration/                    ← THE final orchestration system package (new)
  00-START-HERE.md                          entry point: what this is, read order, invariants
  ARCHITECTURE.md                           milestone-5 architecture (this plan's §1 expanded + component contracts)
  GLOSSARY.md                               Q7 canonical terms (role/state, agent, candidate/canon, packet, workflow/skill, validation/approval)
  schemas/
    handoff-packet.schema.md                Q5 shared schema (single shape for apex_plan packets, sync reports, H6, worker returns)
    authority-state.schema.md               P1 minimal field + transition rules + enforcement surface
    review-verdict.schema.md                P2 verdict + input-packet schema, Claude-only adaptation
  workflows/
    orchestrator-run.md                     canonical macro→meso→micro run loop (Meta Ops contract)
    detective-review.md                     two-lens blind review wiring, 10 steps, deterministic gate
  user-stories/                             ← moved from fable-orchestrator (regression suite of the system)
    user-stories.md, package-manifest.md, connection-ledger.md
  simulations/                              per-story run records (build-plan gate) — created empty with README

.claude/agents/                             ← new: the 7 named definitions
  alfred.md            meta-strategy.md     meta-ops.md          meta-detective.md
  knowledge-bank.md    informatics-design.md  prompts-workflows.md

(unchanged, referenced in place — deliberately NOT moved:)
.claude/skills/apex-plan|apex-sync|apex-session|apex-kb    the working mutation backbone
.claude/skills/source-authority-and-verdict-packet         Detective's validation skill
scripts/apex_sync.py, scripts/drift_check.py               deterministic compute surface
apex-meta/fable-orchestrator/                              initiative record (how the system was decided) — stays as audit trail
apex-meta/kb/*                                             evidence corpora, per standing do-not-delete resolutions
```

Rationale for the non-moves: the mechanism-ladder and D2 (no ceremony) both say do not relocate working mechanisms for tidiness — `.claude/skills/` and `scripts/` are the *canonical runtime locations* Claude Code reads from; moving them would break the running system to satisfy a folder aesthetic. The orchestration package is the **map and law**; the skills stay the **machinery**.

## 3. Deterministic move map (existing usable files → new folders)

| # | Source (exists today) | Destination | Method | Reference updates required |
|---|---|---|---|---|
| M1 | `apex-meta/fable-orchestrator/APEX_Orchestration_User_Stories/` (4 files) | `apex-meta/orchestration/user-stories/` | `git mv` (history-preserving) | `target-log.md`, `build-plan.md`, `design-lock-answers.md`, `README.md` in fable-orchestrator; any other grep hits for the old path |
| M2 | P1 answer's `authority` YAML + transition rules (`prompts/PromptAnswers/Role-vs-state… (DEEP).md` §4) | `schemas/authority-state.schema.md` | content extraction (copy + adapt; source file stays as research record) | none (new file cites its source) |
| M3 | P2 answer's input-packet + verdict YAML schemas (§2) and 10-step wiring (§1) | `schemas/review-verdict.schema.md` + `workflows/detective-review.md` | content extraction, **adapted Claude-only** (cross-family judge removed per operator direction) | none (new files cite source + record the adaptation) |
| M4 | v2 canon handoff-record law + Q5 field union (`design-lock-answers.md` Q5) | `schemas/handoff-packet.schema.md` | content authoring from decided union | none |
| M5 | §3 shared context of user-stories (accountability/lane/worker contracts) | `.claude/agents/*.md` (7 files) | content extraction into agent frontmatter + contract | none |
| M6 | Drifted-terms list (`ORCHESTRATION-SYSTEMS-INDEX.md` §5.3 + Q7 term list) | `apex-meta/orchestration/GLOSSARY.md` | content authoring | `ORCHESTRATION-SYSTEMS-INDEX.md` §5.3 marked resolved, points at glossary |

Move discipline (per `deterministic-file-promotion` ethos): verify source exists before move, verify destination after, `git status` review before commit, one commit for moves + reference updates so history stays traceable.

## 4. Component specifications

### 4.1 Agent definitions (`.claude/agents/*.md`)
Each file: YAML frontmatter (`name`, `description` triggering correct delegation, `tools` narrow allowlist) + body carrying the accountability contract from user-stories §3 verbatim (accountability, must_not), the handoff obligation (every return is a handoff packet per Q5 schema), and the gate obligation (never treat a mutation as confirmed without `operator_validation: confirmed`).

Tool scoping (smallest sufficient):
| Agent | Tools | Reason |
|---|---|---|
| alfred | Read, Grep, Glob | presents/captures; never executes work |
| meta-strategy | Read, Grep, Glob, WebSearch* | direction needs evidence, never mutation (*only if session policy allows; degrade gracefully) |
| meta-ops | Read, Grep, Glob, Write, Edit, Bash | the only accountability that touches the mutation backbone — and only via the three skills + gate |
| meta-detective | Read, Grep, Glob | read-only by construction (P2: reviewer never fixes) |
| knowledge-bank | Read, Grep, Glob, Write | source custody within KB roots only |
| informatics-design | Read, Grep, Glob, Write | artifact structure/terminology within assigned surface |
| prompts-workflows | Read, Grep, Glob, Write | template authoring within assigned surface |

### 4.2 `handoff-packet.schema.md` (Q5)
Single required field set: `packet_id · role_accountability · lifecycle_stage (proposal|computed|confirmed) · status · target_surface · next_state · prerequisites · expected_action · sources_evidence · uncertainties · unresolved_risk · stop_condition · operator_validation · authority (state, basis_digest, verification_ref)`. Law carried over from v2 canon: silent continuation from an unclear handoff is invalid; continuity may not depend on hidden reasoning.

### 4.3 `authority-state.schema.md` (P1, minimal)
`authority.state ∈ {candidate, verified, invalidated}`; `basis_digest` = sha256 over canonicalized content + declared-evidence hashes; `verification_ref` = path to the independent review artifact. Transitions exactly as ground-checked in `prompts/PromptAnswers/research-integration-note.md`; **one enforcement surface**: the apex-session write path (canon-changing write requires `operator_validation: confirmed` AND every authoritative input `verified` with matching digest). Explicitly NOT a general state machine.

### 4.4 `detective-review.md` + `review-verdict.schema.md` (P2, Claude-only)
Two blind parallel lenses (validity, strategic alignment), both fresh isolated Claude subagent invocations of `meta-detective` with lens-specific packets that withhold author identity/confidence/rationale/prior verdicts. Criterion-level falsification mandatory (strongest-wrong-case + evidence sought + result). Deterministic aggregation, no LLM aggregator, no majority vote; timeout/truncation ⇒ `hold`, never PASS. Reviewer routes defects to named owners; correction ⇒ new artifact version ⇒ re-review of the artifact, not the correction claim. **Recorded limitation:** both lenses are Claude-family — the evidence-bearing PASS gate and falsification contract are the compensating controls; a different-family judge is *out of scope by operator direction* (no external calls).

### 4.5 `orchestrator-run.md`
The canonical loop each user story instantiates: intake (Alfred) → macro framing (Strategy, operator selects) → meso skeleton (Ops via apex-plan, `lifecycle_stage: proposal`) → deterministic checks (apex-sync) → bounded packets to lanes/workers → returns as handoff packets (`authority.state: candidate`) → Detective review for consequential artifacts → operator gate → apex-session confirmed mutation (`lifecycle_stage: confirmed`, inputs `verified`) → state delta + next-session packet. Milestone rule from user-stories §2: full loop only for consequential outputs.

### 4.6 `00-START-HERE.md`, `ARCHITECTURE.md`, `GLOSSARY.md`
Entry point (read order, the five invariants: file-held state, single mutation surface, single gate primitive, independent review before consequence, candidate-never-auto-promotes); architecture doc (§1 expanded, component wiring, runtime mapping table, what was deliberately not built); glossary (Q7 terms, each with the one canonical meaning + the drifted meanings it replaces).

## 5. Build sequence (this session)

1. ✅ This plan.
2. Create `apex-meta/orchestration/` skeleton; execute move M1 (`git mv` user stories) + reference updates.
3. Author schemas (M2–M4): authority-state, review-verdict, handoff-packet.
4. Author workflows: detective-review, orchestrator-run.
5. Author 7 agent definitions (M5).
6. Author 00-START-HERE, ARCHITECTURE, GLOSSARY (M6); `simulations/README.md`.
7. Update `ORCHESTRATION-SYSTEMS-INDEX.md` (new package row, §5.3 resolved), `target-log.md` (milestone 5–6 status + log entry), `build-plan.md` path updates.
8. Structure verification: every cross-reference resolves (grep old paths = 0 hits outside audit-trail records), every planned file exists, `git status` clean review → commit → push.

## 6. Verification & what remains open after this session

- **Structural verification** (this session): all files exist, all references resolve, moves history-preserving.
- **Simulation gate** (next sessions, unchanged from build-plan): the system is *assembled* now but each story workflow is *adopted* only after its real run lands in `simulations/`. First candidate: US-IDEA-01 (smallest durable set: Alfred, Ops, Detective).
- **Enforcement code** for authority-digest checking in the apex-session write path is specified in `authority-state.schema.md` but the script change itself is a Codex execution item per `CODEX_EXECUTION_STANDARD.md` — flagged in ARCHITECTURE.md as the one open build item.
- **Registry materialization** (`apex-meta/registry/index.md` still absent) — first apex-sync rebuild run against the live epic will create it; part of the US-IDEA-01 simulation.
