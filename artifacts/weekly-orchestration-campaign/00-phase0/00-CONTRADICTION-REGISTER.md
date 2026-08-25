# 00-CONTRADICTION-REGISTER — Weekly Orchestration Campaign Phase 0

> Each entry: competing authorities, exact evidence, resolution, and the
> disambiguation rule the campaign must follow. No entry is closed by edit;
> production files are frozen during evaluation (hard prohibition).

## C-01 · G1–G5 semantic collision (gate semantics, three-way)

**Severity:** CRITICAL (control-plane drift; directly blocks any simulation)

**Competing authorities:**

| System | File | G1–G5 meaning | Evidence (verbatim) |
| :-- | :-- | :-- | :-- |
| Weekly Orchestrator stage gates (**owner**) | `.claude/skills/weekly-orchestrator/SKILL.md` `05e0b3a6` | Loop stage gates: G1 precap_week → G2 precap_next_day → G3 operator_execution → G4 flow_recap → G5 status_merge | `stage_routing:` table lines 30–35; "You dispatch weekly stages, hold G1-G5" |
| Generic milestone blueprint | `apex-meta/orchestration/workflows/WEEKLY_ORCHESTRATION_BLUEPRINT.md` `0d68003e`, last commit `6c8ab225` 2026-08-24 | Portfolio milestone locks: G1 SSoT Lock, G2 Curriculum & Product Lock, G3 Financial Infrastructure Lock, G4 Content & Distribution Lock, G5 Web Integration & Compounding Learnings; verified on Fridays | §2 "Milestone Gates Reference": "**Gate G1 (SSoT Lock):** Single source of truth frozen…" |
| MCDA screening criteria | `apex-meta/orchestration/mcda-evaluation/00-MCDA-CHARTER.md` | Tool-selection criteria: G1 Existing system, G2 Proven use, G3 Repo-native durable state, G4 Cross-agent portability, G5 Human decision gates (+G10) | Criteria table lines 33–42 |

**Collision mechanics:**
- Same token range (`G1`–`G5`) resolves to three disjoint vocabularies depending
  on which file an agent reads first.
- The blueprint was merged into the control-plane directory **after** the live
  skills were authored (2026-08-24 vs 2026-08-17), i.e., the collision is recent.
- `apex-meta/orchestration/README.md` presents the blueprint as a "standardized
  execution blueprint" for the same Monday–Friday cadence the weekly loop runs,
  without noting that its gates are unrelated to the loop's gates.
- Simulation artifacts already inherit both vocabularies:
  `simulations/5-week-progressive-simulation/Week-01/weekly_plan.md` uses
  `exit_gate: G1_SSoT_Lock` while `.claude/skills/weekly-orchestrator/SKILL.md`
  routes `precap_week: {… gate: G1 …}` for the same weekday cadence.
- A control agent resuming "the weekly loop" from disk could read the blueprint's
  Friday "milestone gate verification (G1–G5)" as loop-gate evidence and record a
  false G-passage in a packet — exactly the F10 failure mode.

**Resolution (binding for this campaign):**

1. Owner of loop gate semantics: `.claude/skills/weekly-orchestrator/SKILL.md`.
   Inside the Weekly Orchestrator, "G1" means *weekly planning validated*,
   "G3" means *operator execution evidence returned*, etc.
2. `WEEKLY_ORCHESTRATION_BLUEPRINT.md` is classified as a **foreign milestone
   vocabulary** describing portfolio-level locks. It is not a routing or gate
   authority for the weekly loop. No campaign artifact may cite it as gate law.
3. MCDA charter IDs are rubric labels for tool selection only; renamed here to
   "MCDA-G*" whenever referenced.
4. Any simulation, eval case, or patch produced by this campaign must use
   qualified identifiers: `loop-G1…G5` (or spell out the stage name) when the
   weekly loop is meant; `milestone-lock-G1…G5` if the blueprint is ever meant.

**Operator decision required (recorded, not resolved):** whether the blueprint
should eventually be renamed (e.g., ML1–ML5) or moved out of `workflows/` into
`docs/showcases/`. This is a production mutation → deferred to Phase 8+ with
operator approval. Until then the qualified-identifier rule above governs.

## C-02 · Weekly output contract gap

**Competing authorities:** A3 (`weekly-command-brief-template.md`) names
`.claude/skills/PrecapWeek/references/weekly-plan-output-contract.md` as its
domain contract lineage; the file does not exist on main.

**Evidence:** A3 `template_authority.source_gap`: *"…was referenced by the live
skill but not retrievable from main during research."* Confirmed absent via
filesystem check (Phase 0).

**Resolution:** A2 + A3 together are the complete weekly output authority. The
missing contract file is treated as documentation debt, not a second authority.
No campaign step may invent its content.

## C-03 · Design-lineage refs vs runtime authority

**Competing authorities:** Templates A3/A5/A6/A7 each carry
`source_design_ref` pointers into `apex-meta/operator-output-design/…`; those
design files could be mistaken for overridable authority over the templates.

**Resolution:** Design refs are provenance metadata. Runtime authority for what
an artifact must contain = owning SKILL.md + template. Campaign reviewers
critique the templates themselves; design-lineage files are consulted only as
historical context and never cited as justification to change semantics.

## C-04 · Reviewer independence claim surface

**Competing authorities:** A1 declares two review agents
(apex-review-validity / apex-review-alignment) as "independent Subagents"; the
campaign hard prohibitions require genuinely isolated contexts before any
"reviewer independent" label is used.

**Resolution:** For Phases 4–6, reviewer independence is defined operationally:
separate fresh context per reviewer, identical frozen inputs, no other reviewer
output visible. A reviewer run inside this session's context may not be labeled
"independent" unless it satisfies that definition; results from persona-only
markdown are recorded as non-independent by default.

## C-05 · Seed duplication tension between A2/A3 and daily layer

**Tension (not yet a contradiction):** A3's compact downstream handoff block is
the sole weekly→daily seed (A2 forbids a separate duplicate artifact), while F02
observes weekly/daily information duplication in practice. The templates encode
the right ownership rule; observed outputs violate it. This is a compliance/
design problem for Phase 1–4, NOT an authority contradiction. Recorded so no
reviewer proposes re-architecting authority ownership as a fix for what is an
output-discipline failure.

---

## Register status

| ID | Class | Blocks simulation? | Closed by |
| :-- | :-- | :-- | :-- |
| C-01 | Contradiction | Yes → now resolved by qualified-identifier rule | This register (operator sign-off on rename deferred) |
| C-02 | Gap | No | A2+A3 declared sole authority |
| C-03 | Ambiguity | No | Provenance-metadata ruling |
| C-04 | Methodology guard | No | Operational independence definition |
| C-05 | Tension | No | Deferred to Phase 1 findings |

Gate check (Phase 0 exit): every tested concept now has exactly one owning
authority — control-plane/gate semantics → A1; weekly planning output → A2+A3;
daily planning outputs → A4–A7. Simulation permitted to proceed to Phase 1.
