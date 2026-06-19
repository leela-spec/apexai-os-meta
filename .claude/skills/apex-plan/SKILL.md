# Apex Plan Skill

This skill handles planning and decomposition activities for the Apex project. It draws on the CCPM structure pattern and the Backlog task contract to guide creation and refinement of epics and tasks. The skill is **operator‑gated**: any action that creates or modifies files will generate a delta proposal and require the operator to type **CONFIRM** before changes are committed.

## Triggers and Responsibilities

|Trigger phrase|Description|
|---|---|
|**capture project**|Initiate a new project or epic. The skill prompts for a high‑level description, proposes an epic slug and initial task breakdown, and presents a delta proposal for creating `apex-meta/epics/<slug>/` and the corresponding task files. Confirmation required before writing.|
|**decompose**|Break down an existing epic into smaller tasks. The skill examines the current epic structure and proposes new task files with appropriate fields (name, status, priority, effort, due_date, depends_on, etc.). Requires confirmation.|
|**assign dependencies**|Propose or update `depends_on`, `parallel`, and `conflicts_with` relationships between tasks. The skill identifies logical dependencies based on the decomposition and suggests them in a delta proposal. Confirmation required.|
|**score priority**|Evaluate and rank tasks according to H7 priority and urgency. The skill computes scores (high=3, medium=2, low=1; urgency based on due date) and recommends which tasks to focus on next. This operation is read‑only and does not require confirmation.|
|**new epic**|Create a brand‑new epic unrelated to existing ones. The skill asks for a slug and basic metadata, proposes the directory and initial task template, and awaits confirmation before creating files.|
|**focus recommendation**|Provide a recommended focus list of tasks based on priority, urgency and dependency status. This is a computation only and does not modify files.|

### Operator Gate

For any trigger that results in file creation or modification (`capture project`, `decompose`, `assign dependencies`, `new epic`), the skill assembles a **delta proposal** showing the exact file system changes and content additions/edits. The operator must explicitly type **CONFIRM** to apply the changes. Without confirmation, no files are written. This ensures consistency with H1 status enums, the H2 directory structure, and the H3 `depends_on` field, and prevents accidental changes that could interfere with live skills.

### Notes

- **Compliance:** All generated epics and tasks must follow the schema defined in `field-schema.md` (name, status, created, updated, priority, urgency, depends_on, parallel, conflicts_with, effort, epic, due_date, acceptance_criteria, definition_of_done). Status values adhere to the H1 enum—**open**, **in‑progress**, **blocked**, **done**, and **deferred**—exactly as defined in `decisions.md`. Directories and file names follow H2; dependencies use the `depends_on` field (H3).

- **No scripts:** This planning skill performs reasoning and file manipulation directly through the skill interface. It does not invoke any Python scripts.
- **Live skill compatibility:** The skill is designed to coexist with existing live skills (status‑merge, flow‑recap, project‑kb‑manager, PrecapNextDay) by respecting their input expectations and not altering data outside the approved Apex paths.