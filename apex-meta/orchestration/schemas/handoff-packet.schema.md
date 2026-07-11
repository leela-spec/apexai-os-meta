---
title: "Handoff Packet Schema"
purpose: >
  The ONE shared schema every packet in the system uses — apex_plan packets, apex-sync
  report headers, apex-session H6 artifacts, specialist/worker returns, Detective inputs.
  Replaces per-packet invented shapes. Built from old Apex v2's handoff-record law
  (the most complete version in scope) + the user-stories artifact-contract requirements.
created: 2026-07-11
source: >
  design-lock-answers.md Q5; v2 canon AGENT_SWARM_INTERACTION_CANON.md L349–376;
  apex-meta/orchestration/user-stories/user-stories.md §7.4.
---

# Handoff Packet Schema

## Law (carried over from v2 canon, verbatim in spirit)

- Silent continuation from an unclear handoff is **invalid**.
- Handoff continuity may **not** depend on hidden reasoning — everything the next role needs is in the packet.
- A packet states who is accountable, what stage the content is at, what surface it targets, and what must happen next.

## Required fields

```yaml
handoff_packet:
  packet_id: string                      # "<workflow>-<story-or-epic-slug>-<NNN>"
  role_accountability: alfred | meta_strategy | meta_ops | meta_detective
                     | knowledge_bank | informatics_design | prompts_workflows
                     | domain_worker | operator
  lifecycle_stage: proposal | computed | confirmed
      # proposal  = semantic choice awaiting validation (apex-plan output, worker returns)
      # computed  = deterministic derivation, reproducible from inputs (apex-sync output)
      # confirmed = operator-gated durable state (apex-session output only)
  status: string                         # H1 status enum value where applicable
  target_surface: string                 # repo-relative path(s) this packet is about / may touch
  next_state: string                     # what the receiving role should leave behind
  prerequisites: [string]                # what must already hold; empty list allowed, absence not
  expected_action: string                # the single thing the receiver is asked to do
  sources_evidence: [string]             # repo-relative refs; every claim traceable
  uncertainties: [string]                # open questions, explicitly kept visible
  unresolved_risk: [string]              # known risks the receiver must not silently absorb
  stop_condition: string                 # when the receiver must stop and hand back
  operator_validation: confirmed | rejected | needs_revision | not_requested
  authority:                             # per schemas/authority-state.schema.md
    state: candidate | verified | invalidated
    basis_digest: null | string
    verification_ref: null | string
```

## Rules

1. **Every** cross-role handoff is a packet with all fields present. `[]`/`null` are legal values; a missing key is not.
2. `lifecycle_stage: confirmed` may be written **only** by the apex-session path with `operator_validation: confirmed`.
3. `lifecycle_stage: computed` packets carry the reproduction command (e.g. the `apex_sync.py` invocation) in `sources_evidence`.
4. A packet whose `expected_action` the receiver cannot perform inside its accountability is **routed back**, not silently reinterpreted (v2: no scope inheritance).
5. Detective verdicts reference packets by `packet_id` + `basis_digest`, never by filename alone.

## Format

Markdown file with the packet as YAML frontmatter (or a fenced `yaml` block inside an existing artifact), body free for human-readable narrative. Location: alongside the work it concerns — epic folders (`apex-meta/epics/<slug>/`), `apex-meta/handoff/`, or the run folder of a simulation.
