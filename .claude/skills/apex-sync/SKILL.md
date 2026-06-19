# Apex Sync Skill

This skill orchestrates synchronization and overview operations for the Apex project. It adheres to the CCPM track pattern and is strictly read‑only—no task content is ever modified. All actions respect the H1 status values, H2 path conventions and the H3 `depends_on` field.

## Triggers and Actions

|Trigger phrase|Action|
|---|---|
|**what's next**|Run `scripts/find_next_task.py` to produce a ranked list of actionable tasks.|
|**any blockers**|Run `scripts/show_blocked.py` to list tasks with incomplete dependencies.|
|**stall check**|Run `scripts/stall_detect.py` to detect tasks whose status hasn’t changed across multiple sessions.|
|**rebuild registry**|Run `scripts/update_index.py` to regenerate `apex-meta/registry/index.md`.|
|**sync state**|Run `scripts/update_index.py --dry-run` to preview the registry index without writing.|
|**drift report**|Run `scripts/drift_check.py` to compare the expected registry with the current one and report discrepancies.|

### Notes

- **Script‑first:** Each trigger invokes a deterministic Python script; if the script fails, the skill outputs the error without changing any files.
- **Read‑only:** The skill never writes or edits task files. The only write operation permitted is generating `apex-meta/registry/index.md` when explicitly requested via the _rebuild registry_ trigger. All other operations compute and display information.

- **Compliance:** This skill assumes all task files follow the harmonized schema and path conventions defined in `decisions.md` and `field-schema.md`. In particular, it expects the H1 status enumeration—**open**, **in‑progress**, **blocked**, **done**, and **deferred**—to be used consistently. It does not attempt to alter or correct malformed tasks.