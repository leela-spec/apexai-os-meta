# QA_HYGIENE_PROTOCOL

## Purpose

This file defines the QA/Hygiene control lane for the living OpenClaw system.

It exists because `CHECKLISTS.md` and `HEARTBEAT.md` are not truthful hosts for hygiene findings, severities, required check families, or closure consequences.

This file governs:

- hygiene finding classes
- severity assignments
- required check families
- finding-record minimums
- routing consequences
- closure conditions

QA/Hygiene is a control surface, not a truth surface.

QA/Hygiene is a co-equal control lane with progress and may block progress work when structural reliability is not sufficient.

This file does not replace:

- `OPERATING_SPINE_CANON.md` as top-level operating law
- `ESCALATION_EXCEPTION_BLOCK.md` as stop, hold, degraded-mode, and escalation law
- `PROMOTION_PROTOCOL.md` as truth-change gate
- `PROJECT_INTERFACE_CONTRACT.md` as project-interface schema and validation authority
- `SESSION_EXPORT_PROTOCOL.md` as trace protocol
- `NIGHT_PLANNING_PROTOCOL.md` as synthesis and planning protocol

## Finding classes and severities

Every QA/Hygiene finding must declare at least:

- one finding class
- one severity
- one affected surface or bounded target
- one required action

### Finding classes

#### Interface failure

- **Definition:** required control surfaces are missing, unresolved, stale, malformed, or unreadable enough to break bounded routing.
- **Examples:** missing `ProjCard`; missing `OpState`; broken `SSOT_INDEX` pointer; absent `SigMat`; interface package not usable for bounded entry.

#### State integrity failure

- **Definition:** live operational state is stale, contradictory, or not traceable to bounded trace.
- **Examples:** active work with no recent trace; blocked work still marked active after disposition; pending recommendations applied with no visible trace.

#### Authority leakage

- **Definition:** truth, reasoning, state, or runtime-authority boundaries are mixed or silently crossing.
- **Examples:** `OpState` treated as accepted truth; `BePr_SSOT` treated as accepted truth; `Session Export` carrying truth mutation; docs, rituals, or companion notes behaving as runtime authority hosts.

#### Dependency or pointer failure

- **Definition:** declared dependencies, pointers, queue links, or cross-surface references do not resolve or resolve ambiguously.
- **Examples:** broken packet pointer; stale queue path; unresolved overlay reference; missing subordinate-surface pointer.

#### Trace failure

- **Definition:** required trace artifacts are missing, incomplete, stale, or not linked tightly enough to justify current state.
- **Examples:** no `Session Export` for a material session; no application trace for a packet; no visible trace for an active hold-affecting event.

#### Promotion integrity failure

- **Definition:** truth mutation cannot be traced to one valid packet path, or packet gates were bypassed or obscured.
- **Examples:** accepted truth changed without packet; unresolved disagreement buried in a packet path; truth ownership changed without visible justification.

#### Continuity failure

- **Definition:** bounded operating continuity is degrading in a way that threatens safe orchestration.
- **Examples:** missing Night synthesis for an active cycle; heartbeat lag; queue growth with no bounded routing; memory-write delays that leave active control surfaces stale.

#### Legacy bridge risk

- **Definition:** a bridged legacy artifact remains load-bearing but is too mixed-purpose, stale, or ambiguous to trust safely.
- **Examples:** one legacy file functioning as both `OpState` and SSOT; legacy status labels used as the real trust model; old authority boundaries still driving current work.

#### Overlay compliance failure

- **Definition:** a project-local overlay weakens the managed floor or conflicts ambiguously with it.
- **Examples:** weaker approval posture; weaker escalation posture; hidden local authority rules; local interface bypass.

#### Governance-first substitution

- **Definition:** a run is asked to create or patch a concrete artifact, but instead produces planning, source ledgers, claim caches, acceptance-test scaffolds, broad audit reports, or other control surfaces while the target artifact remains missing, unvalidated, or unusable.
- **Severity:** `P1` when the run is presented as successful or blocks downstream work; `P2` when clearly labeled as a partial diagnostic.
- **Evidence signals:** absent requested file/diff/KB artifact; many control artifacts but no usable target artifact; validation status such as `not_checked` while claiming readiness; continuation steps redesign the process instead of producing the next named artifact; broad all-system audit when a one-agent or one-file target was requested.
- **Required correction:** stop control-first expansion, restate the target artifact, produce it in the next pass, validate the produced artifact, and only then add broader audit, research, or learning documentation.

### Severity model

Findings use four severities:

- `P0`
- `P1`
- `P2`
- `P3`

#### P0 — Critical governance failure

- **Definition:** the operating spine cannot safely trust or continue without explicit disposition.
- **Examples:** direct truth mutation outside promotion; missing required interface package; silent truth/state leakage; untraceable applied packet.
- **Default action:** immediate hold or escalation.

#### P1 — High-risk integrity failure

- **Definition:** the system may continue only in bounded degraded mode or after prompt remediation.
- **Examples:** stale `OpState` on active work; unresolved authority ownership affecting current routing; missing Night synthesis during active cycle; broken required pointers.
- **Default action:** remediation before normal progression or explicit degraded-mode declaration.

#### P2 — Material hygiene debt

- **Definition:** not immediately blocking, but actively degrading orchestration quality.
- **Examples:** repeated minor staleness; incomplete references; aging queue pointers; bounded cleanup debt with visible risk.
- **Default action:** place in the hygiene backlog with a bounded due path.

#### P3 — Low-risk hygiene issue

- **Definition:** cosmetic or low-risk structural issue that does not materially threaten control quality by itself.
- **Examples:** redundant pointer; minor naming inconsistency; formatting deviation without semantic ambiguity.
- **Default action:** batch cleanup or bounded deferment.

### Severity rules

- Severity must be explicit.
- Findings without severity are invalid.
- `P0` and applicable `P1` findings may not remain only in backlog.
- This protocol uses explicit categorical severity; it does not require a scored numeric model.

## Required check families

QA/Hygiene must be able to perform at least the following check families when they are relevant to the bounded audit target.

### Interface contract check

- **Check:** do required control surfaces exist, resolve, and remain usable for bounded routing?
- **Uses:** `PROJECT_INTERFACE_CONTRACT.md`

### State traceability check

- **Check:** is current `OpState` justified by recent trace or explicit inactivity confirmation?
- **Uses:** `SESSION_EXPORT_PROTOCOL.md`

### Truth/state separation check

- **Check:** are reasoning, accepted truth, and live state still separated correctly?
- **Examples of failure:** `OpState` behaving as SSOT; reasoning treated as truth; hygiene findings treated as truth mutation.

### Promotion traceability check

- **Check:** can every truth mutation be traced to exactly one valid promotion path?
- **Uses:** `PROMOTION_PROTOCOL.md`

### Night continuity check

- **Check:** does the active operating cycle have a valid Night synthesis artifact or explicit degraded-mode record?
- **Uses:** `NIGHT_PLANNING_PROTOCOL.md`

### Pointer and dependency integrity check

- **Check:** do required pointers, references, packet links, queue links, and overlay links resolve cleanly and unambiguously?

### Foundation and startup-safety check

- **Check:** are required governance surfaces and bounded runtime prerequisites present before advanced orchestration is treated as safe?
- **Preserved meaning:** governance presence, runtime base scaffold, validation-lane readiness, migration-awareness, and refusal to treat legacy-root assumptions as canonical by default.

### Environment reliability check

- **Check:** when bounded work depends on environment capability, have those capabilities been verified instead of assumed?
- **Preserved meaning:** fetch/push capability and Python resolution should be verified when relevant, not treated as ambient certainty.
- **Constraint:** this protocol defines the check family, not mandatory tooling choreography.

### Heartbeat continuity-signal check

- **Check:** are heartbeat lag, queue growth, memory-write delays, or unvalidated overlap signaling continuity risk?
- **Preserved meaning:** one active foreground flow remains the default baseline; broader overlap requires validation evidence.

### Legacy bridge safety check

- **Check:** are bridged legacy surfaces still bounded and readable enough to trust temporarily?

### Overlay compliance check

- **Check:** does the local overlay tighten rather than weaken the managed floor?

## Finding record minimums

### Artifact identity target

A QA/Hygiene artifact should identify itself as:

- `class: trace`
- `role: AUDIT`
- `surface: qa_report`
- `quality: reliable`
- `scope: project` or `system`

### Minimum artifact fields

Every QA/Hygiene artifact must include at least:

- `purpose`
- `dependencies`
- `audit_id`
- `target_scope`
- `generated_at`
- `input_window`
- `finding_count`
- `highest_severity`

### Required artifact sections

Every QA/Hygiene artifact must include at least:

1. **Audit header**
   - audit identifier
   - target scope
   - generation time
   - input window
   - overall verdict

2. **Surfaces checked**
   - the exact bounded surfaces that were validated

3. **Findings**
   - all bounded findings

4. **Holds and escalations**
   - required whenever `P0` or applicable `P1` findings exist

5. **Hygiene backlog**
   - required whenever non-blocking issues exist

6. **Verification notes**
   - required when bounded clarification, caveat, or confidence limit matters

### Required per-finding fields

Every finding record must include at least:

- `finding_id`
- `finding_class`
- `severity`
- `affected_surface`
- `description`
- `evidence_refs`
- `required_action`
- `hold_or_escalation_needed`

### Validity rules

A QA/Hygiene artifact is invalid when any of the following are missing or false:

- explicit severity for each finding
- evidence references where evidence is available
- bounded surfaces checked
- highest severity declaration
- explicit holds/escalations when `P0` or applicable `P1` findings exist
- bounded backlog treatment for non-blocking work
- no direct truth mutation embedded in the artifact
- resolving pointers and references

Buried `P0` or applicable `P1` findings are a governance failure.

## Routing and closure rules

### Routing posture

This protocol classifies structural risk and routes consequences.

It does not itself become stop law, promotion law, or planning law.

### Trigger sources

A QA/Hygiene pass may be triggered by:

- scheduled or periodic review
- Night synthesis
- explicit review request
- promotion review need
- observed anomaly
- heartbeat continuity signal
- checklist-driven bounded review

### Routing by finding type

#### Route to escalation law

Route to `ESCALATION_EXCEPTION_BLOCK.md` when:

- a `P0` finding exists
- a `P1` finding requires degraded mode, hold, or escalation
- missing required control surfaces block normal participation
- missing required trace freezes dependent work
- authority leakage threatens safe continuation

#### Route to promotion law

Route to `PROMOTION_PROTOCOL.md` when:

- a promotion integrity failure exists
- truth mutation appears to have occurred without a valid packet path
- truth ownership or packet traceability is contested or unclear

#### Route to Night planning

Route to `NIGHT_PLANNING_PROTOCOL.md` when:

- a non-blocking hygiene backlog must be prioritized
- bounded next-cycle hygiene work must be sequenced
- progress work must be conditioned on visible hygiene prerequisites without becoming a stop-law question

#### Route to state recommendation surfaces

QA/Hygiene may produce bounded recommendations affecting `OpState`, but it does not directly mutate `OpState`.

### Closure rules by severity

#### P0 closure

A `P0` finding closes only when:

- the hold or escalation has an explicit disposition
- the blocking condition is cleared or explicitly reclassified
- the affected surfaces show the required correction or bounded downgrade
- the finding is no longer load-bearing for normal continuation

#### P1 closure

A `P1` finding closes only when:

- remediation is complete, or
- a bounded degraded-mode declaration exists with explicit limits and follow-up path, and
- the affected workstream can continue without hidden authority or trace risk

#### P2 closure

A `P2` finding closes only when:

- the backlog item is completed, or
- a bounded deferment remains explicit and does not conceal a higher-severity dependency

#### P3 closure

A `P3` finding closes only when:

- the issue is cleaned up, or
- a bounded deferment is recorded without causing higher-severity drift

### General closure rules

- Findings may not be closed by silence.
- Findings may not be closed only because later prose stopped mentioning them.
- Governance-first substitution may close only when the concrete target artifact exists and has been checked against its requested format/scope; a better plan, broader ledger, or cleaner audit does not close the finding by itself.
- A finding may not be downgraded without an explicit reason.
- Severe findings may not be rephrased as routine notes to avoid routing consequences.

## Relationship to heartbeat and checklists

### Relationship to `CHECKLISTS.md`

`CHECKLISTS.md` remains a lightweight, operator-facing checklist surface.

It may summarize check families, startup reminders, or compact review prompts.

It does not define:

- severity semantics
- finding classes
- finding-record minimums
- routing consequences
- closure law

`CHECKLISTS.md` is subordinate to this protocol.

### Relationship to `HEARTBEAT.md`

`HEARTBEAT.md` remains a small, script-first maintenance ritual.

It may surface continuity signals such as:

- heartbeat lag
- queue growth
- memory-write delays
- overlap risk before validation

It does not become the authority host for QA/Hygiene law.

When heartbeat surfaces a material issue, the issue must route into explicit QA/Hygiene, escalation, or promotion surfaces rather than remaining masked as routine progress.

### Shared boundary

This protocol preserves:

- the lightweight checklist economy
- the script-first maintenance posture
- the rule that routine ritual surfaces point into managed authority rather than replacing it

## Compatibility notes

This protocol is compatibility-first for the living `07_finalopenclawsystem` shell.

It does not assume:

- external incident-management systems
- automatic remediation behavior
- hidden integration hooks
- full metadata retrofit across all legacy files before QA/Hygiene can function

Legacy audit, hygiene, or health-check artifacts may be mapped temporarily when:

- findings remain bounded
- severity is explicit
- evidence references remain visible
- required actions remain visible
- routing consequences remain explicit

A legacy summary that mixes findings, planning, truth mutation, and unresolved research without clear boundaries is not a valid mapped QA/Hygiene artifact.

Until every downstream surface has its dedicated final artifact in place, a valid QA/Hygiene output may be expressed through:

- a bounded markdown artifact
- a bounded section inside another governed trace surface

That compatibility bridge is valid only when class, severity, evidence, action, and routing consequence remain explicit.

This file stays narrow: it governs hygiene findings, severities, required check families, finding-record minimums, routing, and closure logic. It does not expand into top-level operating law, escalation law, or promotion law.