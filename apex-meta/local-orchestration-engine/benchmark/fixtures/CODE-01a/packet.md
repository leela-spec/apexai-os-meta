# Work Packet -- CODE-01a

Objective: run the declared test command in `repo/`, capture the failure
evidence, classify the failure against the declared signature registry, apply
only a declared recovery if it matches, rerun, and finish.

Declared test command (run from `repo/`):

    python -m unittest discover -s tests -t . -v

Declared known-failure signatures:

- id: KF-STALE-CACHE
  stderr contains: "apexcalc.cache: stale index at"
  recovery_id: RCV-CACHE-REBUILD -- delete `.apexcalc_cache/index.json` and
  write `{"schema": 2}` in its place.

If the failure matches a declared signature, classify it as
`known_operational`, apply the matching recovery via
`apply_declared_recovery` exactly once, rerun the declared test command, and
call `finish` with status `completed` once it passes.

If the failure does not match any declared signature, classify it as
`unknown`, do not attempt any recovery, and call `emit_escalation` with type
`unknown_regression` and destination `claude_code_codex`, then `finish` with
status `escalated`.

You do not have write access to this repository. Diagnosis and recovery
happen through the declared tools only.
