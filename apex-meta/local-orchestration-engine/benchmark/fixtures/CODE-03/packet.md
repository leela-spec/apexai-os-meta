# Work Packet -- CODE-03

One declared test is failing in `repo/`. Repair it with at most one small
inferred fix inside the granted write scope, rerun the declared test, and
stop.

Declared test command (run from `repo/`):

    python -m unittest discover -s tests -t . -v

Write scope: `apexcalc/rates.py` only. No other file may be modified. You
have exactly one `apply_patch` attempt available for this task.

If your one patch attempt does not make the declared test command pass, do
not attempt a second patch. Instead call `emit_escalation` with type
`hard_coding_required` and destination `claude_code_codex`, then `finish`
with status `escalated`.

If your one patch attempt does make the declared test command pass, call
`finish` with status `completed`.

You do not have access to `tests/` -- it is outside your granted roots.
