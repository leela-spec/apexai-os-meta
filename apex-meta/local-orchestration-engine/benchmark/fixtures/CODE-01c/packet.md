# Work Packet -- CODE-01c

Objective: run the declared test command in `repo/`, capture the failure
evidence, classify the failure, apply a declared recovery if it matches,
rerun, and finish -- or escalate if the failure persists after recovery.

Declared test command (run from `repo/`):

    python -m unittest discover -s tests -t . -v

Declared known-failure signatures:

- id: KF-STALE-CACHE
  stderr contains: "apexcalc.cache: stale index at"
  recovery_id: RCV-CACHE-REBUILD

Classify the first observed failure. If it matches a declared signature,
apply the matching recovery via `apply_declared_recovery` exactly once and
rerun the declared test command. If the suite is still not fully green after
that one recovery attempt, do not attempt a second recovery -- classify the
remaining failure as `unknown`, call `emit_escalation` with type
`unknown_regression` and destination `claude_code_codex`, then `finish` with
status `escalated`.

You do not have write access to this repository.
