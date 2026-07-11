---
title: "Detective Review Workflow (two-lens, blind, parallel)"
purpose: >
  How consequential artifacts get independently reviewed before they can become
  authoritative (authority.state: verified) or feed a confirmed mutation. Translates
  old Apex v2's meta_detective into a concrete workflow step. Claude-only per operator
  direction; schemas in ../schemas/review-verdict.schema.md.
created: 2026-07-11
---

# Detective Review Workflow

**When required:** any artifact whose acceptance triggers durable mutation, public output, spend, safety-relevant instruction, or doctrine change (the user-stories "consequential output" rule). Not required for low-consequence intermediates — the milestone rule applies the full loop only where consequence lives.

## Steps

1. **Freeze the subject** (Meta Ops). Record the artifact's version + sha256 in a lock note; all verdicts bind to the hash. No review against a mutable path.
2. **Build two blind lens packets** (Meta Ops), per `review_input_packet` schema:
   - **validity** packet: artifact + declared sources + criteria. NO macro-goal advocacy, NO worker rationale/confidence, NO prior verdicts.
   - **strategic_alignment** packet: artifact + macro-goal + decision log. NO validity verdict.
3. **Preflight (deterministic, no LLM):** schema-valid packets, hash matches, every required source readable, criterion IDs unique, forbidden context absent. Fail ⇒ `hold`, reviewers never invoked.
4. **Run both lenses in parallel** as fresh isolated `meta-detective` subagent invocations (read-only tools). Each reviewer, per criterion, must first construct the strongest case the artifact is WRONG, then test it against retrieved evidence — falsification before evaluation. Output per `review_verdict` schema. Reviewers may invoke the `source-authority-and-verdict-packet` skill.
5. **Aggregate deterministically** (Meta Ops applies the rule, does not re-judge): precedence `escalate > needs_input > hold > revise > pass`; single critical non-pass blocks; no majority vote; disagreement between lenses ⇒ `hold` or operator escalation.
6. **Route defects to named owners** via a revision-order packet (handoff-packet schema). The reviewer NEVER fixes the artifact — reviewer-repairs-own-finding turns the next review into self-evaluation.
7. **Correction = new immutable version** (vN+1, new hash). "We fixed issue X" is not review evidence.
8. **Re-review the artifact, not the correction claim:** fresh reviewer contexts, prior defect IDs supplied, worker's explanation of why it should now pass withheld. Criterion-scoped re-review only when a deterministic diff proves nothing else changed.
9. **On pass:** Meta Ops sets `authority.state: verified`, `basis_digest`, `verification_ref` on the artifact per `authority-state.schema.md`. Only now may it feed a canon-changing write (which still needs `operator_validation: confirmed`).
10. **Append the audit trail:** verdicts and the lock note stay immutable next to the artifact (epic/run folder).

## Failure handling

Timeout, malformed verdict, missing source, truncation ⇒ `hold`, never PASS. Repeated `hold` on the same artifact ⇒ escalate to operator with the concrete blocker — not another silent retry loop.

## Known limitation (recorded, accepted)

Both lenses are Claude-family; see `../schemas/review-verdict.schema.md` §Recorded limitation. If simulation records show plausible-but-wrong artifacts passing both lenses, the escalation path is a different-family judge — an operator trust-boundary decision, not a default.
