# SESSION_EXPORT_PROTOCOL

## 1. Purpose

- **Decision:** This file defines the required trace artifact emitted at the end of each bounded working session inside the OpenClaw operating spine.
- **Decision:** Session Export is the primary durable record of what happened during a session.
- **Decision:** It exists to feed `OpState` updates, Night synthesis, QA/Hygiene review, promotion candidate creation, and later audit.
- **Constraint:** Session Export is trace authority, not accepted truth, and local memory is not a substitute for it.

## 2. When a session export exists

- **Rule:** Every bounded session that changes project motion, produces findings, drafts promotion candidates, performs verification, or creates follow-up work must emit a Session Export.
- **Rule:** Very small no-op or aborted sessions may emit a minimal export that records the abort or no-op condition.
- **Constraint:** Do not assume Session Export artifacts already exist everywhere; the protocol may be present before all projects adopt concrete export files.
- **Constraint:** A session is incomplete for downstream control purposes when material work occurred but no durable export exists.

- ## 3. Required sections and minimum contents
  - `class: trace`
  - `role: LOG`
  - `surface: session_export`
  - `quality: reliable`
  - `scope: session`
- **Decision:** Session Export is reliable enough for planning and review, but not authoritative truth.
- **Keep as compatibility bridge:** legacy LOG or HANDOVER style exports may be mapped temporarily if the mapping is explicit and the authority boundary remains clear.

Every Session Export must answer:

- what session was this?
- what project or bounded task did it serve?
- what was the intended objective?
- what actually happened?
- what changed in operative state?
- what findings or evidence matter downstream?
- what blockers, risks, or disagreements remain?
- what must happen next?
- did this session create promotion candidates?
- did this session create QA/Hygiene findings?

### 3.1 Session header

- **Required metadata:** `project_id`, `session_id`, `session_type`, `started_at`, `ended_at`, `operator_or_executor`, `lane`, `execution_surface`.
- **Decision:** `lane` distinguishes `progress` from `hygiene`.
- **Decision:** `execution_surface` distinguishes `operator` from `cloud`.

### 3.2 Intended objective

- **Purpose:** record what the session was supposed to accomplish.
- **Constraint:** intent is not retrospective justification.

### 3.3 Work performed

- **Must include:** files or surfaces read, files or surfaces written, analyses performed, bounded decisions made, and outputs produced.

### 3.4 Operative delta

- **Must include:** changes to active work, blocked work, next actions, and opened or closed holds.
- **Constraint:** this section informs `OpState`. It does not replace `OpState`.

### 3.5 Findings and evidence

- **Must include:** key findings, evidence references, unresolved uncertainty, and confidence or disagreement markers when relevant.

### 3.6 Promotion candidates

- **Must include:** promotion needed yes/no, candidate target surface(s), packet drafted yes/no, and packet pointer if already created.
- **Constraint:** this section nominates candidates only; it is not a Promotion Packet.

### 3.7 QA/Hygiene findings

- **Must include:** missing required surfaces, stale state, broken links or dependencies, authority leakage, or process violations found during the session.
- **Constraint:** severe findings must be surfaced into explicit QA/Hygiene outputs or escalation, not buried here.

### 3.8 Next actions

- **Must include:** immediate next action(s), owner or expected execution surface if known, and whether the action belongs to operator, cloud, progress, or hygiene.

## 4. Relationship to project state and promotion

- **Decision:** Session Export is the primary trace input for `OpState` updates.
- **Constraint:** projects should not rely on readers reconstructing live state by scanning multiple old Session Exports.
- **Decision:** Project interface surfaces should point to the latest relevant Session Export when it matters for bounded entry.
- **Decision:** Session Export may create promotion candidates when evidence suggests accepted truth should change.
- **Constraint:** Promotion still requires a separate packet under `PROMOTION_PROTOCOL.md`.
- **Decision:** Night planning consumes bounded Session Exports rather than reconstructing sessions from chat history or from local memory files.

## 5. Boundaries and non-substitutions

- **Constraint:** Session Export may not directly redefine `SSOT` or silently embed truth mutation as "what happened."
- **Constraint:** Session Export may not be used as a substitute for `OpState`, `SSOT_INDEX`, a Promotion Packet, or local memory.
- **Constraint:** Local memory files remain companion/local context, not export logs or trace authority.
- **Constraint:** Session Export must remain compact enough for bounded reading by Night, QA/Hygiene, and project-control surfaces.
- **Decision:** Silent truth mutation inside Session Export is a `P0` governance failure.
- **Decision:** Missing operative delta when project motion changed is at least a `P1` hygiene failure.

## 6. Compatibility notes

- **Decision:** Legacy session logs, handovers, or work summaries may be mapped to Session Export during transition when the mapping is explicit and the required questions are still answerable.
- **Constraint:** A legacy artifact that mixes truth mutation, live state, and reasoning without clear boundaries is not a valid mapped export.
- **Decision:** The protocol may exist before every project has concrete export instances.
- **Decision:** Adoption is compatibility-first and does not require retroactive backfill of all old session history.
