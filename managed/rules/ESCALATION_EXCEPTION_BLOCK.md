# ESCALATION_EXCEPTION_BLOCK

## Purpose

This file defines the managed stop, hold, exception, and escalation law for the living OpenClaw system.

It exists because the living shell already contains conservative stop/report behavior, but that behavior is fragmented and not yet hosted in a single authoritative runtime file.

This file governs what happens when normal bounded execution is no longer safe. It prefers explicit pause, hold, degraded mode, or routed escalation over silent reconciliation under uncertainty.

This file does not replace:

- `OPERATING_SPINE_CANON.md` as top-level operating law
- `QA_HYGIENE_PROTOCOL.md` as hygiene, finding, and severity authority
- `PROMOTION_PROTOCOL.md` as truth-change gate
- `PROJECT_INTERFACE_CONTRACT.md` as project-interface authority

No agent may continue normal operation after a triggered stop condition unless the condition has been explicitly dispositioned.

## Trigger classes

Escalation uses both escalation level and exception type.

### Escalation levels

- `E0` — local clarification: a bounded issue that can be resolved from currently loaded sources without crossing authority boundaries
- `E1` — local hold: the current bounded task cannot continue safely until a missing prerequisite, boundary, or classification issue is resolved
- `E2` — structured escalation: the issue crosses surfaces, projects, or review boundaries and requires explicit routing
- `E3` — hard stop: the work cannot safely continue without explicit governance or human disposition

### Mandatory trigger classes

#### Authority ambiguity

- Trigger: accepted truth ownership, approval path, or governing surface is unclear
- Action: stop normal progression and route through structured escalation
- Constraint: authority may not be inferred by convenience

#### Truth/state leakage

- Trigger: reasoning, accepted truth, and live state are being mixed or silently redefined
- Action: hard stop or structured escalation depending on severity
- Constraint: do not continue first and repair later

#### Contested promotion

- Trigger: a truth-change candidate has unresolved disagreement, unclear target, or missing approval boundary
- Action: hold packet progression and escalate
- Constraint: contested packets may not advance by silence

#### Severe hygiene finding

- Trigger: a blocking or near-blocking structural failure has been identified, including a `P0` finding or a `P1` finding affecting authority, interface completeness, or traceability
- Action: apply hold or degraded-mode routing according to severity
- Constraint: severe findings may not remain only in backlog

#### Missing required control surface

- Trigger: required project interface surfaces are absent, unresolved, or non-functional
- Action: block normal project participation until mapped, repaired, or explicitly placed in degraded mode
- Constraint: do not compensate by scanning the entire project tree as a normal substitute

#### Missing required trace

- Trigger: a material session, night cycle, or applied change lacks the required durable trace
- Action: escalate according to impact and freeze dependent actions when trace is load-bearing
- Constraint: missing trace is not neutral

#### Unbounded ambiguity

- Trigger: the task can no longer continue from bounded sources without speculative widening
- Action: stop and request routing, research packet, or explicit scope expansion
- Constraint: do not silently widen task scope

#### Approval exception

- Trigger: a required approval or review boundary is missing, bypassed, or only implied
- Action: structured escalation or hard stop depending on impact
- Constraint: local agents may not self-approve around a missing review boundary

### Exception classes

- **Information exception:** required information is missing, stale, or contradictory
- **Authority exception:** truth, control, or approval ownership is unclear or conflicting
- **Integrity exception:** structural reliability is compromised
- **Scope exception:** the current task is no longer bounded enough to continue safely
- **Approval exception:** a required approval or review boundary is missing, contested, or bypassed

These exception classes help classify the issue. They do not weaken the mandatory stop conditions above.

## Hold states

The recognized hold states are:

- `local_hold`
- `project_hold`
- `system_hold`
- `degraded_mode`

Their meanings are:

- `local_hold` freezes one bounded task
- `project_hold` freezes normal progression for one project
- `system_hold` freezes cross-project or governance-critical motion
- `degraded_mode` permits explicitly limited continuation while normal reliability is incomplete

Every hold must state:

- what is held
- why it is held
- which surface or condition triggered it
- what clears it

Holds may not remain implicit in prose, memory, or chat.

### Degraded mode

Degraded mode is allowed only when full stop is unnecessary but normal reliability is not available.

Degraded mode must be:

- explicit
- bounded
- visible in a durable runtime surface
- cleared by an explicit disposition rather than by silence

Degraded mode may not permit:

- hidden truth mutation
- ignored authority ambiguity
- suppressed severe hygiene findings
- silent return to normal operation

Degraded mode is a recorded operating condition, not an informal excuse and not the default posture.

## Routing and response rules

### Local clarification

Route to bounded local clarification only when:

- ambiguity is bounded
- no authority boundary is crossed
- no truth change depends on the answer
- no severe hygiene issue exists

### QA/Hygiene review

Route to `QA_HYGIENE_PROTOCOL.md` when:

- structure, interfaces, pointers, or trace integrity are in question
- stale or contradictory state is suspected
- a hygiene finding may affect authority, traceability, or execution safety
- bridge safety or compatibility safety is in doubt

### Promotion review

Route to `PROMOTION_PROTOCOL.md` when:

- a truth change is proposed
- a packet is contested
- truth ownership or downstream impact is unresolved
- approval or packet trace is missing or compromised

### Night planning

Route to `NIGHT_PLANNING_PROTOCOL.md` only when:

- the issue is mainly prioritization, sequencing, or bounded next-cycle planning
- no immediate hard stop already applies
- the question spans multiple projects or execution surfaces without becoming a governance stop

Night planning may not dissolve an escalation into soft planning language.

### Human review

Route to human review when:

- a governance stop condition exists
- approval is required and unavailable
- authority remains contested after bounded review
- packet trace or applied-truth integrity is compromised
- a `system_hold` is required

### Operational response constraints

- `BUILD` may prepare clarification notes, research packets, or escalation artifacts, but it may not self-resolve authority or approval exceptions by fiat.
- `VERIFY` is the default state for assessing whether an issue is real, bounded, and clearable, but it may not turn contested truth mutation into approved progression.
- `LOCK` applies when a surface or workstream is frozen by escalation, approval boundary, or governance condition and may not be lifted informally.
- Once an `E3` hard stop has triggered, normal progress work must not continue until the hold is dispositioned.
- No startup, maintenance, or execution ritual may silently clear a blocking issue by continuing as if the issue were non-material.

## Required outputs and visibility

Every durable escalation artifact or bounded escalation note must make the following explicit:

- `escalation_level`
- `trigger_class` or `exception_class`
- `trigger_surface` or triggering condition
- `affected_scope`
- `description`
- `evidence_refs` or bounded rationale when evidence is not yet fully assembled
- `current_hold_state`, if any
- `required_disposition`
- `opened_at`

When a dedicated identifier exists, include:

- `escalation_id`

Additional rules:

- Escalations without evidence references are invalid when the evidence is available.
- Escalations must not be phrased only as vague concern.
- Open holds, escalations, and degraded-mode status must remain visible to the relevant runtime surfaces.
- Blocking issues may not be left only in transient chat.
- Continuing normal work after a triggered hard stop is a governance failure.

## Relation to QA, promotion, and bootstrap

`QA_HYGIENE_PROTOCOL.md` defines findings, severities, required check families, and hygiene review logic. This file governs when those findings become holds, degraded-mode conditions, or escalations.

`PROMOTION_PROTOCOL.md` defines how truth-change candidates are reviewed and applied. This file governs what happens when that path is contested, blocked, unclear, or bypassed.

`BOOTSTRAP.md` must respect this block during startup. It may discover or surface a stop condition, but it may not silently clear a blocking issue by continuing as if the issue were non-material.

`HEARTBEAT.md` must route relevant findings into explicit hold, escalation, QA, or promotion surfaces rather than masking them as routine progress.

`NIGHT_PLANNING_PROTOCOL.md` must surface open holds, escalations, and degraded-mode status explicitly rather than dissolving them into general planning.

`SESSION_EXPORT_PROTOCOL.md` remains the trace protocol. Missing or invalid trace may create a hold or degraded mode depending on impact, but this file governs the stop posture rather than the trace schema itself.

## Compatibility notes

This block is intentionally conservative and compatibility-first.

It does not assume:

- external incident-management systems
- automatic recovery behavior
- hidden integration hooks
- full metadata retrofit across all legacy files before escalation law can function

Until every downstream surface has its dedicated final artifact in place, a valid escalation may be expressed through:

- a bounded markdown artifact
- a structured section inside another governed trace surface
- another durable runtime-visible note

That compatibility bridge is valid only when the stop condition, hold state, evidence basis, and required disposition remain explicit.

This file is load-bearing stop law. It should stay narrow: it governs stop, hold, exception, and escalation behavior, while detailed hygiene taxonomy, truth-change procedure, interface schema, and execution ritual detail remain in their sibling managed files.

## Self-check

- **Preserved from the blueprint host:** first-class escalation posture; `E0` to `E3`; mandatory stop conditions; exception-class model; explicit hold states including `degraded_mode`; durable escalation artifact minimums; conservative stop/report posture.
- **Tightened or demoted for DR7 consistency:** removed blueprint frontmatter and `AGENT_INSTRUCTION_BLOCK_vNext.md` naming; folded escalation posture, degraded-mode rules, and operational-state interaction into the DR7 seven-section shape; demoted standalone validation, anti-pattern, and open-question appendices; kept subordinate QA, promotion, interface, session-export, and night-planning detail out of this file.
- **Related subordinate or sibling files:** `OPERATING_SPINE_CANON.md`; `AGENTS.base.md`; `BOOTSTRAP.md`; `HEARTBEAT.md`; `QA_HYGIENE_PROTOCOL.md`; `PROMOTION_PROTOCOL.md`; `PROJECT_INTERFACE_CONTRACT.md`; `SESSION_EXPORT_PROTOCOL.md`; `NIGHT_PLANNING_PROTOCOL.md`.
- **Any unresolved ambiguity:** whether `degraded_mode` eventually needs a stricter standardized metadata flag beyond the current minimum escalation artifact fields; whether every `system_hold` must always produce a distinct named human-disposition artifact or may remain inside another durable governed trace surface.