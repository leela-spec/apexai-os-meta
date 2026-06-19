# Apex Session Skill

This skill manages interactive work sessions for the Apex project, handling status updates, session logging, and handoff preparation. It follows the structure of the planning‑with‑files pattern and enforces an explicit operator confirmation gate (as described in the crewAI design task), ensuring that **every file mutation is preceded by a delta proposal and only applied after the operator types CONFIRM**.

## Triggers and Responsibilities

|Trigger phrase|Description|
|---|---|
|**log session**|Capture a narrative of the current work session into `apex-meta/handoff/progress.md`. The skill summarizes what was done and which tasks were touched, producing a delta proposal for the new session block. Requires operator confirmation before writing.|
|**update status**|Propose status changes to existing tasks or epics (e.g., marking a task as in‑progress or done). The skill gathers the intended updates and presents a delta diff. No changes are written until the operator confirms.|
|**apply deltas**|Apply previously proposed changes (status updates, new tasks, edits) to the repository. This writes to the relevant files under `apex-meta/epics/` and updates timestamps. Requires confirmation.|
|**handoff**|Assemble the end‑of‑session artifacts (`task_plan.md`, `findings.md`, `progress.md`) inside `apex-meta/handoff/`. The skill collates the current state and any findings, then generates a delta proposal for these handoff files. Confirmation required.|
|**next session prep**|Generate `apex-meta/handoff/next-session.md` according to the H6 format: sections for **Current Step**, **Open Items**, **Risks**, **Decisions Made**, and **Next Actions**. A draft is proposed and only written after confirmation.|
|**operator approve**|Final gatekeeper. When invoked, the skill applies all pending deltas that have been presented. If the operator does not issue CONFIRM, no changes are written.|

### Confirmation Gate

For any trigger that would mutate files (log session, update status, apply deltas, handoff, next session prep), the skill generates a **delta proposal** showing the exact changes that would occur. The operator must type **CONFIRM** to apply the changes. Without confirmation, the proposed edits are discarded. This ensures that all writes respect H1 status values, H2 path conventions, and H3 dependency semantics, and prevents inadvertent changes that could break live skills.

### Notes

- **Compliance:** All task updates honour the defined status enumeration (open, in‑progress, blocked, done, deferred), store files under the prescribed `apex-meta/` paths, and use `depends_on` for dependencies.
- **Handoff output:** The generated `next-session.md` file always includes the mandated sections (**Current Step**, **Open Items**, **Risks**, **Decisions Made**, **Next Actions**) as required by H6.
- **Live skills:** This session skill does not override the behaviour of existing skills (e.g., status‑merge, flow‑recap); it writes only to the appropriate Apex project files and maintains compatibility.