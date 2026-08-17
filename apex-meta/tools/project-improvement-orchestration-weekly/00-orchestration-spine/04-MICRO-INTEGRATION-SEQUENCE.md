# Micro Guidance — Ordered Integration Sequence for Module 00

## Purpose

Give the Master Orchestrator a deterministic **order of operations** for integrating the already validated design into the stale production Weekly Orchestration without drifting into detailed module design.

This is the micro sequence for the **global spine only**. Detailed micro design of the Weekly Command Brief, Next Day Brief, Flow Execution Card, prompt files, recap, etc. remains in Modules 01-08 and their fresh chats.

---

# Phase 0 — Resolve the runtime composition question first

## 0.1 Run the architecture research

Use:

- `01-ARCHITECTURE-RESEARCH-PROMPT.md`

The research must determine whether the current `weekly-orchestrator skill -> custom stage agents -> stage skills` composition is justified or whether some wrapper agents should be removed/thinned.

## 0.2 Record the accepted topology decision

Update project `DECISIONS.md` with:

- accepted composition;
- agents kept;
- agents thinned/removed;
- skills kept/merged if any;
- rejected architecture alternatives;
- reason based on actual requirements.

## 0.3 Do not reorganize for neatness

Only physical/topology changes supported by the research decision enter the production migration.

**Gate 0:** Do not rewrite stage contracts until the Master knows which runtime primitive will own/invoke them.

---

# Phase 1 — Build the authoritative current-to-target map

## 1.1 Read the active global sources

Read:

- `.claude/skills/weekly-orchestrator/SKILL.md`
- `.claude/skills/weekly-orchestrator/references/handoff-schema.md`
- `.claude/skills/weekly-orchestrator/references/review-wiring.md`
- weekly-orchestrator role/doctrine references actually referenced by the entrypoint
- all routed weekly stage-agent files
- the owning stage-skill entrypoints

## 1.2 Read the validated target sources

Read:

- Step 3 operator-output principles
- J1-J3 planning designs
- J4 Flow Execution Card design
- J5 Prompt Files design
- relevant J6-J12 designs/templates when their stage interface is reviewed
- Step 5 promotion map
- Step 6 activation report

## 1.3 Create one transaction table in the working analysis

For each current stage:

`stage -> producer -> inputs -> outputs -> consumer -> operator surface -> machine payload -> persistence -> gate -> state authority -> AI/deterministic/operator`

For every current field/artifact that may survive, also record:

`thing -> named consumer -> concrete value/failure prevented`.

Do not create another permanent registry unless the final Weekly Orchestrator needs this data at runtime. The table is an analysis tool for Module 00.

## 1.4 Mark contradictions

At minimum check for:

- validated human artifact exists but entrypoint does not require it;
- stale schema-first artifact remains primary;
- two files independently define the same rule;
- operator-facing and machine-facing content duplicate each other;
- deterministic data is repeatedly authored by LLM;
- stage/gate exists without a real decision;
- persistent artifact exists with no future consumer;
- stale file is still discoverable as active authority.

**Gate 1:** Master can explain the complete current loop and the intended target loop without relying on chat memory.

---

# Phase 2 — Correct the Weekly Orchestrator spine before module details

## 2.1 Rewrite the central lifecycle contract

Update `.claude/skills/weekly-orchestrator/SKILL.md` so it describes the accepted minimal lifecycle.

The entrypoint must make explicit:

- lifecycle sequence;
- stage owner/invocation mechanism;
- accepted upstream references;
- primary operator artifact per stage where applicable;
- downstream consumer;
- persistence policy;
- state/evidence boundary;
- gate/review trigger;
- degraded/recovery behavior.

Do not include detailed J2/J3/J4 formatting here.

## 2.2 Simplify shared handoff requirements

Audit `.claude/skills/weekly-orchestrator/references/handoff-schema.md` field by field.

For each current field choose:

- `KEEP_REQUIRED`
- `KEEP_CONDITIONAL`
- `DERIVE`
- `MOVE_TO_STAGE_OWNER`
- `ARCHIVE_REMOVE`

Do not require operator artifacts to begin with a generic machine envelope unless a retained runtime consumer genuinely requires that physical layout.

If a small machine handoff remains necessary, prefer a compact block/reference rather than a full repeated packet schema.

## 2.3 Reconcile gate logic

Rebuild gate behavior around actual decisions.

Check G1-G5 individually:

- What decision occurs here?
- Who needs to make it?
- What unsafe or costly outcome does the gate prevent?
- Can low-risk progression occur automatically?

Align the result with `review-wiring.md`: independent validity/alignment review is conditional, not routine ceremony.

## 2.4 Reconcile Session / Sync / ProjectStatus

Establish globally:

- apex-session = durable confirmed mutation authority;
- apex-sync = deterministic read-side helper only for retained useful computations;
- ProjectStatus = derived/read projection if retained, never separate truth.

Remove any global requirement to read or produce these components when no downstream capability needs them.

## 2.5 Define artifact persistence classes

For each stage output decide:

- operator durable artifact;
- machine durable artifact with named future consumer;
- ephemeral/generated-on-demand;
- no artifact required.

The default is not "persist because orchestration generated it."

**Gate 2:** corrected central spine is coherent even before detailed output-module refinements.

---

# Phase 3 — Change stage interfaces only as far as needed to remove contradictions

The purpose of Phase 3 is to prevent the central spine from pointing at stale stage behavior. Do not finalize detailed module design here.

## 3.1 PrecapWeek interface correction

Update only enough of PrecapWeek/worker wiring to establish:

- primary operator result = Weekly Command Brief;
- detailed format owned by Module 01;
- downstream daily planning reads approved weekly direction by reference/minimal handoff;
- stale numeric/schema requirements are no longer globally mandatory unless retained consumer analysis proves necessity.

Make the promoted Weekly Command Brief template/design discoverable from the active entrypoint.

If `weekly-plan-output-contract.md` conflicts with this interface, either:

- reduce it to a true machine-only contract with a named consumer; or
- archive it after migrating any real invariant.

## 3.2 PrecapNextDay interface correction

Update only enough to establish:

- primary operator result = PreCap Next Day Brief;
- each full represented flow expands to a Flow Execution Card;
- three sprints remain visible at day level but full detail belongs to Flow Execution Card;
- real prompt files, not large operator-facing prompt packs, are the prompt access mechanism;
- output-module detail remains for Modules 02-04.

Remove the global completion requirement that a flow is "ready" merely because a placeholder/degraded prompt-pack reference exists.

## 3.3 Flow preparation interface correction

Establish the preferred invariant:

- Flow Execution Card is the operator workspace and execution contract;
- a separate machine `flow_packet` survives only if a real downstream consumer cannot use/derive the required information otherwise.

Do not maintain two complete persistent flow representations by default.

## 3.4 Prompt interface correction

Establish:

- PromptEngineer owns actual prompt-body generation;
- AIRouting contributes only needed routing recommendation/reference;
- prompt file must contain an actual body;
- required missing prompt means the flow is not fully ready;
- large repetitive Flow Prompt Pack is not an operator output.

Detailed prompt generation behavior remains Module 04.

## 3.5 Evidence / recap / mutation interfaces

Establish only the global invariants:

- execution evidence is distinct from plan;
- evidence normalization is conditional if that is sufficient for the accepted topology;
- FlowRecap produces actual-result interpretation and candidate changes;
- status merge/review does not become independent truth;
- apex-session applies confirmed durable changes.

Detailed surfaces remain Modules 05-08.

**Gate 3:** no stage interface still requires a downstream artifact that the corrected global lifecycle has removed.

---

# Phase 4 — Remove stale active authority safely

## 4.1 Build an archive candidate list

Include every superseded contract/template/agent instruction that can still mislead a fresh runtime.

Common candidates to inspect:

- old schema-first output contracts;
- obsolete flow-prompt-pack contract;
- obsolete validation/checklist rules tied only to removed schemas;
- duplicate templates superseded by the validated operator template;
- stale role/accountability doctrine not used by retained architecture;
- worker-agent instructions superseded by architecture-research decisions.

## 4.2 Consumer search before archive

For each candidate:

1. search active repo references;
2. identify semantic consumers, not only exact links;
3. migrate any still-valid invariant to the correct owner;
4. update consumers;
5. only then archive.

## 4.3 Archive with provenance

Follow project `ARCHIVE-POLICY.md`.

Archive metadata must identify:

- original active path;
- archive date;
- reason for supersession;
- replacement authority;
- commit/reference where relevant.

## 4.4 Remove active references

Search again after archival.

A migration is incomplete if an active `SKILL.md`, agent, manifest, validator, fixture, or runtime instruction still tells Claude to treat the archived design as current authority.

**Gate 4:** a fresh reader of active `.claude/` paths encounters one coherent generation of runtime rules.

---

# Phase 5 — Replace fake activation with runtime-level validation

## 5.1 Correct validation philosophy

Do not repeat Step 6's failure mode where templates/links/fixtures passed while `entrypoints_changed`, `contracts_changed`, and `runtime_changes` remained zero.

Validation must prove behavior, not package presence.

## 5.2 Static integration checks

Before fresh runtime testing, Master verifies:

- central Weekly Orchestrator references current stage owners;
- stage entrypoints reference current design/template authorities;
- archived contracts have no active authority references;
- downstream interfaces match upstream outputs;
- no removed packet is still required by a completion gate;
- state mutation remains routed through the accepted authority;
- required prompt generation path exists.

## 5.3 Do not test detailed output modules yet

Module 00 is complete when the spine and module interfaces are correct. It does not need to prove the final wording/layout of J2-J11.

Instead, create the bounded Module 01 handover.

**Gate 5:** Master independently concludes the repo is ready for detailed Weekly Command Brief integration without global architectural contradictions.

---

# Phase 6 — Hand off Module 01

Create a bounded handover for `01-weekly-command-brief` containing only:

- accepted production topology from architecture research;
- corrected Weekly Orchestrator interface for weekly planning;
- J2 validated design source;
- current PrecapWeek files;
- stale instructions still needing module-level removal/refinement;
- exact upstream project context contract;
- exact downstream PrecapNextDay consumer contract;
- archive rules;
- fresh-test protocol.

The module chat then performs Q&A with the operator, updates the real production implementation, returns to Master for integration verification, and only after Master pass runs a fresh W34 regression test.

---

# Master anti-drift checklist

At every phase ask:

1. **Is this rule global or module-local?** If module-local, do not solve it in Module 00.
2. **Who consumes this?** If nobody, remove/derive/archive candidate.
3. **Is this information authoritative somewhere else?** Reference it rather than duplicate it.
4. **Does this need persistence?** If it can be derived and has no future consumer, keep it ephemeral.
5. **Does AI need to decide this?** If deterministic, move to deterministic computation where useful.
6. **Does the operator need to see this?** If not, keep it out of the primary surface.
7. **Could a fresh runtime still find the stale rule?** If yes, migration is incomplete.
8. **Are we testing actual runtime behavior or only file existence?** Only runtime behavior proves activation.
9. **Are we creating a new abstraction to solve an abstraction-created problem?** If yes, stop and simplify.

---

# Module 00 definition of done

Module 00 is complete only when all are true:

- architecture research decision is recorded;
- Weekly Orchestrator is the corrected canonical lifecycle authority;
- agent/skill composition matches the accepted simplest native topology;
- shared envelope/gate rules are reduced to demonstrated needs;
- stage interfaces point toward J2-J11 validated operator outputs;
- active entrypoints can discover the validated design they are supposed to execute;
- known conflicting global stale rules are rewritten or archived;
- Session/Sync/ProjectStatus authority boundaries are explicit;
- no removed artifact remains a required downstream dependency;
- validation checks runtime wiring rather than template presence;
- project `CURRENT-STATE.md` and `DECISIONS.md` are updated;
- a bounded Module 01 handover is ready.

After this point, detailed implementation proceeds module by module and is tested through the production path with fresh context and the existing W34 regression data.
