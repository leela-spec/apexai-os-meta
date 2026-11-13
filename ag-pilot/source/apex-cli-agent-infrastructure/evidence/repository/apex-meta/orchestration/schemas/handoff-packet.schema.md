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
  sources_excerpt: [object]              # OPTIONAL, see "Source excerpts" below
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

1. **Every** cross-role handoff is a packet with all fields present, except `sources_excerpt` which
   is optional (its absence is legal — not every packet needs it). `[]`/`null` are legal values for
   required fields; a missing required key is not.
2. `lifecycle_stage: confirmed` may be written **only** by the apex-session path with `operator_validation: confirmed`.
3. `lifecycle_stage: computed` packets carry the reproduction command (e.g. the `apex_sync.py` invocation) in `sources_evidence`.
4. A packet whose `expected_action` the receiver cannot perform inside its accountability is **routed back**, not silently reinterpreted (v2: no scope inheritance).
5. Detective verdicts reference packets by `packet_id` + `basis_digest`, never by filename alone.

## Source excerpts (optional field, added for token efficiency — 2026-07-12)

When a receiver (typically a `meta-detective` reviewer) would otherwise re-read a large source file
from scratch just to check a handful of cited lines, the packet author (who already has the file
open) MAY populate `sources_excerpt` with the specific cited ranges:

```yaml
sources_excerpt:
  - path: "apex-meta/kb/.../some-source.md"   # must also appear in sources_evidence
    lines: "L150, L204-207, L470"              # the exact ranges being excerpted
    text: |
      <the actual lines, each still tagged with its line number so anchors stay checkable>
```

Rules for this field:
- **It is required-source material only** — the raw cited text, nothing else. It must never carry
  the producer's rationale, confidence, "why this should pass," or any other-lens verdict; doing so
  would violate the blind-review invariant in `workflows/detective-review.md`.
- **The receiver retains full file access regardless.** An excerpt is a starting point, not a
  restriction — a reviewer verifying anchor fidelity or checking for something outside the excerpted
  range opens the full file exactly as before. Silently trusting an excerpt without the option to
  verify against the real file would itself be an evidence-free pass.
- Every `path` in `sources_excerpt` MUST also appear in `sources_evidence` — the excerpt is a
  convenience copy of cited material, not a replacement for the evidence-reference contract.
- Do **not** use this field to pass a prior verdict, a corrected version's rationale, or any content
  that would let one review lens infer what another lens (or the producer) concluded.

## Format

Markdown file with the packet as YAML frontmatter (or a fenced `yaml` block inside an existing artifact), body free for human-readable narrative. Location: alongside the work it concerns — epic folders (`apex-meta/epics/<slug>/`), `apex-meta/handoff/`, or the run folder of a simulation.
