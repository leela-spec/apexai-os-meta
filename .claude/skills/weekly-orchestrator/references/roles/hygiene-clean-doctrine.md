# Hygiene-clean doctrine (structural QA / repair sweeps)

Purpose: repair and audit discipline for the main thread when it runs structural QA — lint sweeps
(frontmatter lint, path-reference resolution, no-draft-language) and the wave-gated patches that fix
their findings. Source basis: `apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/special_ops__hygiene_clean/`
(cited below as `HC:<file>`). Structural QA here is a deterministic sweep + patch pass, not a standing agent.

## Best practices

- Rule: repair only the damaged span. For a bounded defect (broken fence, dead path, damaged anchor,
  local wording corruption) patch the exact span; whole-file rewrite requires explicit operator
  authorization. [HC:BEST_PRACTICES.md BP-HC-005]
- Rule: patch one drift-sensitive file at a time — apply the patch, inspect the landed diff, verify
  expected anchors and no unintended deletions, then advance to the next file. [HC:BEST_PRACTICES.md BP-HC-004; HC:MISTAKES.md recovery playbook]
- Constraint: lock the sweep before editing — declare target files, allowed actions, forbidden
  actions, stop conditions, and deliverable; stop and re-lock if completing the sweep would require
  actions outside that declaration. [HC:BEST_PRACTICES.md BP-HC-003]
- Rule: closure by evidence only. A lint finding never disappears by silence or later prose cleanup;
  it closes only when the affected surface was rechecked after the fix, or it is explicitly deferred
  or downgraded with a stated reason and follow-up path. [HC:ESSENCE.md core constraints; HC:TEMPLATES.md closure validity checklist]
- Rule: stop conditions outrank completion. If the exact source text, target span, or authority for a
  repair is missing, halt and report — do not guess through it. [HC:MISTAKES.md recovery playbook step 3]

## Known failure modes

- Avoid: repair by interpretation — fixing a dead reference or corrupted span by plausible redesign
  instead of exact minimal correction; semantic drift hides inside cleanup. Choose exact repair or
  stop. [HC:MISTAKES.md M-HC-001]
- Avoid: whole-file rewrite reflex — proposing a full rewrite for a bounded corruption; produces
  unreviewable wording drift. Require exact target spans and diff review. [HC:MISTAKES.md M-HC-003]
- Avoid: mode crossing — a move-only or validate-only pass silently becoming move+edit+scaffolding.
  Declare one mode; halt if completion requires crossing it. [HC:MISTAKES.md M-HC-005]
- Avoid: process-gate bypass — citing a rule (skill contract, patch process, write constraint) while
  proceeding without proving compliance with it; a run must show the gate was actually applied before
  action. [HC:BEST_PRACTICES.md BP-HC-002; HC:MISTAKES.md M-HC-004]
- Avoid: target-topology drift — creating new files or structure during a repair pass before proving
  the existing living files cannot absorb the content (merge-map / no-fit proof first). [HC:MISTAKES.md M-HC-006]
- Avoid: execute-not-explain drift — a bounded repair request turning into process explanation or
  meta-planning; execute the next authorized step, explain only blockers or final verification. [HC:MISTAKES.md M-HC-002]

## Checks worth adding to lint sweeps

- Check: exact-preservation metrics on any move/copy/promotion where content equality matters —
  file count, missing/extra files, bytes, lines, and checksum against the source set. [HC:appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md HC-EVID-017]
- Check: closure trace — every finding from a prior sweep is either fix-verified on its surface or
  carries an explicit deferral/downgrade record; reopen anything that vanished without one. [HC:TEMPLATES.md closure validity checklist]
- Check: scope diff — after a patch wave, the set of changed files equals the declared target set;
  any undeclared file, new file, or extra cleanup is a scope-drift finding. [HC:appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md anti-drift control map, scope drift]

## Templates worth reusing

- Template: execution-mode lock — `{mode, target_files, allowed_actions, forbidden_actions,
  stop_conditions, deliverable, protected_spans, verification_plan}`; fill before any
  drift-sensitive patch wave. [HC:TEMPLATES.md execution_mode_lock]
- Template: severity crib — P0 halt/escalate immediately; P1 remediate before normal progression;
  P2 backlog with bounded follow-up; P3 batch cleanup or explicit deferment. Use to rank sweep
  findings before patching. [HC:TEMPLATES.md severity crib]
- Template: finding record (minimal) — `{finding_id, finding_class, severity, affected_surface,
  required_action, status}`; one row per lint finding so closure stays traceable. [HC:TEMPLATES.md finding_record]
