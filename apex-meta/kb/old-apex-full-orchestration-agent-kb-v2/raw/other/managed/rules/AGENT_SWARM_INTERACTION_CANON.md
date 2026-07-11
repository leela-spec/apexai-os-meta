# AGENT_SWARM_INTERACTION_CANON

## Purpose and authority position

This file defines the managed law for role, state, delegation, and handoff behavior across OpenClaw agents.

It exists because role and routing authority may not remain docs-only, while `managed/rules/AGENTS.base.md` must remain compact.

This canon is load-bearing. It governs:

- semantic role meaning
- operational state meaning
- role-state interaction
- delegation boundaries
- handoff minimums
- anti-conflation rules for governed work

This canon does not replace:

- `managed/rules/OPERATING_SPINE_CANON.md` for top-level operating law, authority order, and canonical operating posture
- `managed/rules/ESCALATION_EXCEPTION_BLOCK.md` for stop, hold, exception, and escalation law
- `managed/rules/QA_HYGIENE_PROTOCOL.md` for hygiene findings, severity, and routing consequences
- `managed/rules/PROMOTION_PROTOCOL.md` for packet, approval, and truth-change execution law
- `managed/rules/PROJECT_INTERFACE_CONTRACT.md` for project-interface schema and validation requirements
- file grammar and construction law that belongs in file-format, library, and protocol siblings

## Scope and non-scope

This file governs how agents coordinate work on governed surfaces.

It is in scope for:

- who is accountable for a bounded task
- what an agent is permitted to do right now
- when delegation is valid
- what a receiving agent must be able to see
- when build, review, and promotion must remain distinct
- how compatibility-era human-facing role language maps into managed law

It is out of scope for:

- the full operating cycle
- the full escalation trigger taxonomy
- QA severity definitions
- promotion-packet structure
- project-interface field definitions
- file metadata, bullet grammar, relation grammar, or file-construction syntax

## Default operating stance

The default operating stance is conservative.

- One main active flow is the baseline.
- One main user-facing coordinator remains the default human contact point.
- Delegation is allowed only when the work is bounded, legible, and compatible with the sequential-conservative posture.
- Explicit state and explicit handoff matter more than narrative assumptions about who is “basically in charge.”
- Roles remain the semantic accountability layer.
- Operational states are the real permission layer.
- No role label may be used as compliance theater for permissions the current state does not grant.

## Semantic role layer

OpenClaw uses semantic roles for accountability, planning clarity, and review visibility.

Current managed role taxonomy:

- `PLANNER`
- `STRUCTURER`
- `DRAFTER`
- `VERIFIER`
- `AUDITOR`
- `PROMOTER`

Roles are the accountability layer. They are not the permission layer by themselves.

### PLANNER

`PLANNER` owns session-scope or cycle-scope routing.

Typical responsibility:

- decide what bounded work should happen
- decide in what order it should happen
- decide which role/state posture is required
- assign or sequence work across a session or cycle

Constraints:

- does not directly promote truth by planning it
- does not outrank the operating spine
- does not replace explicit state assignment

### STRUCTURER

`STRUCTURER` owns the internal structure of a bounded task or artifact once the task has already been assigned.

Typical responsibility:

- shape skeleton and segmentation
- determine internal execution order
- define section structure or task-internal orchestration

Constraints:

- does not outrank session-scope planning by `PLANNER`
- does not treat internal structuring decisions as authority to expand scope

### DRAFTER

`DRAFTER` produces candidate content and bounded working outputs.

Typical responsibility:

- create or revise governed artifacts inside the allowed build boundary
- produce bounded candidate deltas
- prepare material for later review or promotion routing

Constraints:

- may not declare its own output verified merely because it is readable
- may not bypass promotion or lock boundaries by virtue of authorship

### VERIFIER

`VERIFIER` checks whether a bounded artifact, delta, or packet is sound enough to advance.

Typical responsibility:

- validate alignment and completeness
- detect contradictions
- reject invalid handoffs
- decide whether a bounded item may move forward, loop back, or escalate

Constraints:

- is review-first, not build-first, on the exact artifact under review
- may not use review posture as cover for silent substantive rewriting

### AUDITOR

`AUDITOR` checks cross-surface integrity, hygiene, and governance-grade reliability.

Typical responsibility:

- detect stale state, trace gaps, dependency drift, truth/state leakage, unresolved holds, and structural inconsistency
- issue findings, holds, or escalation-grade outputs

Constraints:

- does not silently repair governance-critical issues by mutating truth without trace
- does not replace QA/Hygiene protocol definitions with ad hoc practice

### PROMOTER

`PROMOTER` executes an already approved governed transition.

Typical responsibility:

- apply an approved promotion outcome
- update the relevant governed surfaces
- preserve durable trace of what changed and under what approval

Constraints:

- may be a governed mode rather than a permanently separate agent instance
- may not invent its own approval
- may not substitute chat consensus for packetized promotion

## Operational state model

The actual permission layer is the operational state.

OpenClaw uses three operational states:

- `BUILD`
- `VERIFY`
- `LOCK`

State applies to the current bounded task or target surface, not to the agent forever.

### BUILD

`BUILD` is the active creation and substantive revision state.

Permits:

- bounded creation
- bounded structuring
- bounded drafting
- substantive revision inside assigned scope
- production of candidate outputs
- non-truth working updates inside allowed surfaces

Does not permit:

- silent self-verification of the same change
- direct accepted-truth mutation outside the promotion path
- bypass of locked surfaces

### VERIFY

`VERIFY` is the review, validation, reconciliation, and promotion-proposal state.

Permits:

- checking structure, evidence, and consistency
- producing review or audit outputs
- rejecting invalid handoffs or state claims
- proposing advancement, loop-back, hold, or escalation

Does not permit:

- unmarked substantive rewriting of the exact artifact under review as though build and review were the same act
- direct truth mutation by virtue of approval recommendation alone

### LOCK

`LOCK` is the read-only or tightly controlled state used when a surface is frozen by authority, escalation, approval boundary, or governance posture.

Permits:

- reading
- comparing
- referencing
- preparing routing or audit outputs around the locked surface

Does not permit:

- substantive mutation unless the governing protocol explicitly lifts the lock

## State assignment rules

Every material swarm task must identify at least:

- current semantic role
- current operational state
- target surface or bounded object
- intended output surface

Permissions are interpreted from state first, then narrowed by:

- task boundary
- target surface
- protocol constraints
- approval or escalation conditions

The following are invalid:

- inferring permission from role name alone
- inferring permission from file importance alone
- treating a state as global across unrelated workstreams

## State-transition rules

State transitions must be explicit enough that a later agent can reconstruct who was allowed to do what.

### Normal transitions

`BUILD -> VERIFY`

- used when candidate work is ready for review or promotion proposal
- requires a durable candidate artifact or bounded delta

`VERIFY -> BUILD`

- used when review found issues requiring revision
- requires a visible failure reason or loop-back trigger

`VERIFY -> LOCK`

- used when approval, escalation, or governance conditions freeze the workstream
- requires a legible lock reason

`LOCK -> BUILD`

- used only when the lock has been explicitly lifted by the governing authority or protocol event

### Forbidden transitions

The following are forbidden:

- `BUILD` directly treating its own truth change as promotion-complete
- `VERIFY` silently rewriting accepted truth under the guise of review
- overriding `LOCK` through convenience, urgency, or repetition

## Role-state interaction rules

A semantic role is always interpreted through the current state.

The same role behaves differently depending on whether it is in `BUILD`, `VERIFY`, or `LOCK`.

A role change does not erase the current state boundary.

A role may not be assigned a task whose required permissions exceed the current state.

Natural fits exist, but they do not replace explicit assignment:

- `PLANNER`: usually `BUILD`, sometimes `VERIFY`
- `STRUCTURER`: usually `BUILD`
- `DRAFTER`: usually `BUILD`
- `VERIFIER`: usually `VERIFY`
- `AUDITOR`: usually `VERIFY`, sometimes `LOCK`
- `PROMOTER`: enters after successful review and explicit approval under the promotion path

## Delegation rules

Delegation is valid only when:

- the work is clearly bounded
- success criteria are explicit
- required context and source surfaces are identified
- the expected return format is legible
- material constraints are explicit when relevant
- the receiving agent can tell what to do next without reconstructing hidden reasoning from transient chat context

Keep work local when it is:

- simple
- highly personal
- security-sensitive
- approval-bound
- primarily conversational

Delegate when:

- deeper focus is needed
- the work can be bounded cleanly
- the main agent must remain responsive
- the receiving agent can operate with reduced context
- the work can be reviewed against explicit acceptance criteria

Delegation does not transfer authority beyond what the receiving role/state and surface permit.

## Role-switching and separation rules

One agent instance should hold one primary semantic role at a time for one bounded task or bounded object.

If an agent changes semantic role on the same workstream, that shift must be explicit and durable.

Where risk or authority matters, build work and review work on the same exact change should remain separated.

Role-switching may not be used to:

- hide self-review
- bypass independent verification
- evade escalation
- evade the promotion gate

## Handoff rules

A handoff is a governed transfer of bounded work between roles, states, or surfaces.

A valid handoff must make the following explicit:

- current role
- current state
- target surface or bounded object
- intended next role or next state
- required inputs or missing prerequisites
- expected next action
- unresolved risk or blocking ambiguity, when present

A receiving agent must disposition the handoff as:

- accept
- reject
- escalate

Additional rules:

- rejection requires a stated reason
- escalation requires a durable routing output
- silent continuation from an unclear handoff is invalid
- handoff continuity may not depend on hidden reasoning alone

Durable handoff state may live in a governed session trace, plan surface, packet surface, or equivalent governed output, provided the semantics remain explicit.

## Routing boundaries and guardrails

The following routing rules apply:

- Do not begin substantive project work from broad whole-tree traversal when the project interface package can answer the bounded question.
- Do not treat docs examples, persona descriptions, or cost-tiering notes as runtime permission law.
- Do not assume broad multi-agent overlap by default.
- Do not blur build and review into one unmarked continuous act on a load-bearing change.
- Do not substitute chat consensus for packetized promotion.
- Do not continue normal progress work as though major trace gaps, truth/state leakage, or unresolved holds were minor notes.
- Do not use companion-language convenience to override managed law.

## Anti-conflation rules

The following distinctions are mandatory:

- Semantic role is not operational state. Role answers responsibility; state answers permission.
- Planning authority is not truth authority.
- Verification is not promotion execution.
- Candidate output is not accepted truth.
- Project entry surfaces are not a license to assume unrestricted system-wide knowledge.

## Invalid patterns

The following are invalid patterns:

- role name used as the sole permission source
- `BUILD` agent self-promoting its own truth change
- `VERIFY` used as cover for silent substantive rewrite
- `LOCK` bypassed by convenience
- competing orchestration at the same scope with no clear precedence
- handoff accepted without visible target, state, next action, or remaining risk
- promotion executed without durable approval trace
- role-switching used to disguise self-review

## Relationship to sibling and companion files

`managed/rules/AGENTS.base.md` remains the compact base-governance and startup anchor. It should point to this file rather than absorbing its detailed law.

`managed/rules/OPERATING_SPINE_CANON.md` defines top-level operating law, authority order, and the broader control posture this canon must honor.

`managed/rules/ESCALATION_EXCEPTION_BLOCK.md` governs stop, hold, exception, and hard escalation conditions rather than burying them here.

`managed/rules/QA_HYGIENE_PROTOCOL.md` governs hygiene findings, severities, and routing consequences rather than burying them here.

`managed/rules/PROMOTION_PROTOCOL.md` governs the packet and approval path. This file governs how roles and states relate to that path.

`managed/rules/PROJECT_INTERFACE_CONTRACT.md` governs interface-first entry surfaces and schema expectations. This file governs the behavioral obligation to respect that boundary.

`managed/rituals/SESSION_EXPORT_PROTOCOL.md` governs durable session trace expectations often used to support handoffs.

`docs/ROLE_SYSTEM.md` remains companion-only after authority split-out. It should preserve examples, heuristics, cost-tiering notes, and handoff templates.

`docs/PROJECT_ROUTING.md` remains companion-only after authority split-out. It should preserve scenario examples, quick-reference guidance, and delegation checklists.

The following detailed law belongs elsewhere and must not be redefined here:

- `managed/rules/FILE_FORMAT_CANON.md`
- `managed/rules/FILE_TYPE_LIBRARY.md`
- `managed/rules/RELATION_LIBRARY.md`
- `managed/rules/BULLET_LIBRARY.md`
- `managed/rules/ITERATIVE_FILE_PROTOCOL.md`

If a companion file and this canon diverge on a runtime question, this canon governs.

## Compatibility notes

The living shell may still use human-facing language such as:

- main agent
- research specialist
- coding specialist
- persona
- orchestrator

Those terms remain valid as companion examples and advisory mappings.

During the compatibility phase:

- main-agent-first user contact remains the default posture
- human-facing specialist examples remain useful
- the managed semantic runtime taxonomy remains `PLANNER`, `STRUCTURER`, `DRAFTER`, `VERIFIER`, `AUDITOR`, and `PROMOTER`
- the actual permission model remains `BUILD`, `VERIFY`, and `LOCK`

This compatibility posture preserves legibility without allowing docs-only role language to remain the enforcement layer.

## Self-check

### What was preserved from the blueprint host

- The hybrid model of semantic roles plus operational states.
- The full managed role taxonomy: `PLANNER`, `STRUCTURER`, `DRAFTER`, `VERIFIER`, `AUDITOR`, `PROMOTER`.
- The full operational state model: `BUILD`, `VERIFY`, `LOCK`.
- Explicit state-assignment, state-transition, role-state, delegation, handoff, and anti-conflation logic.
- Conservative governance posture: no role-only permissions, no silent self-review, no lock bypass, no chat-only promotion.

### What was tightened or demoted for DR7 consistency

- Demoted blueprint-era direct dependencies on `*_vNext` filenames into final-system sibling paths.
- Replaced `AGENT_INSTRUCTION_BLOCK_vNext.md` dependency logic with the final compact-anchor role of `managed/rules/AGENTS.base.md`.
- Kept project-interface, session-trace, QA, escalation, promotion, and file-grammar matters as outward references rather than duplicating their protocol detail here.
- Removed blueprint sections whose function was advisory, transitional speculation, or checklist-style verification of the canon itself rather than managed law.
- Kept the seed’s lean section structure, but re-expanded it where needed to preserve blueprint-host law for state transitions, role-switching, handoff acceptance, and anti-conflation behavior.

### Which sibling or subordinate files this canon points to

- `managed/rules/AGENTS.base.md`
- `managed/rules/OPERATING_SPINE_CANON.md`
- `managed/rules/ESCALATION_EXCEPTION_BLOCK.md`
- `managed/rules/QA_HYGIENE_PROTOCOL.md`
- `managed/rules/PROMOTION_PROTOCOL.md`
- `managed/rules/PROJECT_INTERFACE_CONTRACT.md`
- `managed/rituals/SESSION_EXPORT_PROTOCOL.md`
- `docs/ROLE_SYSTEM.md`
- `docs/PROJECT_ROUTING.md`
- `managed/rules/FILE_FORMAT_CANON.md`
- `managed/rules/FILE_TYPE_LIBRARY.md`
- `managed/rules/RELATION_LIBRARY.md`
- `managed/rules/BULLET_LIBRARY.md`
- `managed/rules/ITERATIVE_FILE_PROTOCOL.md`

### Any unresolved ambiguity

- The blueprint host is materially broader than the DR7 seed on cross-surface discipline, anti-conflation detail, and transition rules; this draft resolves that by keeping only the parts that directly govern role/state/delegation/handoff behavior and pointing all deeper protocol law outward.
- Long-term taxonomy remains slightly open on whether `PROMOTER` should remain a semantic role or eventually be treated only as a governed mode.
- Long-term taxonomy also remains slightly open on whether `VERIFIER` and `AUDITOR` later merge in some contexts; this draft preserves both because the blueprint host and compatibility posture still distinguish them.

## Named first-iteration seed mapping

The managed seed layer may define named first-iteration agents in `managed/agents/` when those files remain subordinate to this canon.

The default named seed set is:

- `alfred` for operator-facing intake, constraint capture, and bounded routing
- `meta_ops` for orchestration and specialist activation
- `meta_strategy` for option framing and long-range logic
- `meta_detective` for adversarial validation and drift challenge
- `special_ops__knowledge_bank` for KB placement and lifecycle
- `special_ops__informatics_design` for structure, taxonomy, and readability
- `special_ops__prompts_workflows` for reusable prompt and workflow patterns
- `special_ops__ai_handling_routing` for advisory model/tool routing posture
- `special_ops__hygiene_clean` for structural QA, pointer integrity, and closure routing

These names are not a replacement for semantic roles or operational states. They are a managed seed vocabulary for bounded ownership and handoff clarity.

## Overlap-validation companion surfaces

The following companion-managed surfaces may be used to make overlap and handoff behavior durable without replacing this canon:

- `managed/agents/AGENT_INDEX.md`
- `managed/knowledge/OVERLAP_VALIDATION_MATRIX.md`
- `managed/processes/AGENT_HANDOFF_CONTRACTS.md`
- `managed/processes/HOLDING_ORCHESTRATION_FLOW.md`

If any of those surfaces diverge from this canon on a runtime-behavior question, this canon governs.

## First-iteration anti-conflation addendum

The following overlap boundaries are mandatory in the first holding-layer iteration:

- Alfred must not absorb Meta Ops, Strategy, Detective, or runtime law.
- Meta Ops orchestrates; it does not own personal priorities, final strategy, or adversarial validation.
- Knowledge Bank owns placement and lifecycle; Informatics Design owns structure and readability.
- Hygiene audits structural correctness; Detective validates plausibility, authority, and drift.
- Prompts/Workflows owns reusable execution patterns; AI Handling/Routing owns advisory model and tool posture.
- Strategy frames options; Detective challenges; operator approval is required above the relevant threshold band.

Any durable cross-agent change above T0 requires a second verifying role or agent before it is treated as accepted for its target surface.