# PROMOTION_PROTOCOL

## 1. Purpose

- **Decision:** This file defines the only valid path for changing accepted truth inside the OpenClaw operating spine.
- **Decision:** Promotion is the governed conversion of evidence and reasoning into accepted truth.
- **Decision:** Promotion is packetized.
- **Decision:** Promotion is explicit, reviewable, and auditable.
- **Constraint:** Learning, repeated successful use, session outputs, Night outputs, QA/Hygiene findings, and experiments may generate candidates, but they are not promotions by themselves.

## 2. Promotion-eligible artifact classes

Promotion may govern:

- creation of a new truth surface
- modification of an existing truth surface
- deprecation or replacement of accepted truth
- remapping of truth ownership or `SSOT_INDEX` authority notes

### 2.1 Introduce truth

- create a new truth-bearing surface or a newly governed truth domain

### 2.2 Modify truth

- change accepted content inside an existing truth boundary

### 2.3 Deprecate or replace truth

- retire an obsolete truth surface or declare its successor

### 2.4 Remap truth boundaries

- change which surface owns a domain or authority boundary

- **Constraint:** Every promotion target must have a clear bounded scope.

## 3. Required promotion packet contents

Every promotion must be represented by a packet.

- `packet_id`
- `promotion_class`
- `target_surface`
- `target_scope`
- `change_summary`
- `evidence_links`
- `source_reasoning_links`
- `impact_summary`
- `risk_summary`
- `disagreement_summary`
- `approval_required`
- `proposed_by`
- `verified_by` or `pending`
- `status`
- `created_at`
- `last_updated`

- **Decision:** `status` is the packet lifecycle state, not the truth status of the target surface.
- **Allowed statuses:** `drafted`, `under_verification`, `awaiting_approval`, `approved`, `rejected`, `applied`, `superseded`.
- **Constraint:** A packet without reference-backed evidence or a clearly named target is invalid.

## 4. Review chain and approval gates

### 4.1 Trigger and drafting

- **Allowed triggers:** session findings, research findings, QA/Hygiene findings, Night synthesis recommendations, or explicit operator request.
- **State:** `BUILD` for packet drafting.
- **Constraint:** Drafting may summarize evidence but may not rewrite truth.

### 4.2 Verification

- **Checks:** evidence sufficiency, authority clarity, target boundary clarity, downstream impact, and disagreement visibility.
- **State:** `VERIFY` for packet review.
- **Constraint:** Unresolved ambiguity routes to escalation rather than quiet progression.

### 4.3 Approval gates

- **Gate:** evidence
- **Gate:** authority
- **Gate:** boundary
- **Gate:** impact
- **Gate:** disagreement
- **Gate:** approval
- **Decision:** operator approval is required by default in the first rewrite round.
- **Constraint:** approval may not be inferred from silence or repeated use.

## 5. Apply and trace rules

- **Action:** Apply an approved change to the target truth surface and update `SSOT_INDEX` when truth ownership or pointers change.
- **State:** the authoritative target is treated as `LOCK` during application.
- **Action:** Record application trace that points back to the exact approved packet.
- **Constraint:** Every applied truth change must be traceable to one approved packet.
- **Decision:** Session and Night protocols may emit candidates and packet drafts, but they may not directly mutate accepted truth.
- **Decision:** `OpState` may reference approved truth changes only after packet application.
- **Decision:** Rejected or superseded packets remain in trace history with explicit reason.
- **Constraint:** If an applied change later proves wrong, correction requires a new packet or another explicit governed path; this protocol does not invent automatic rollback machinery.

## 6. Prohibitions and non-auto-promotion boundary

### BUILD

- **Allowed:** draft packet, assemble evidence, summarize proposed change.
- **Forbidden:** apply truth mutation.

### VERIFY

- **Constraint:** No automatic truth mutation.
- **Constraint:** No bypass of user-owned truth boundaries.
- **Constraint:** No self-approval around a missing approval boundary.
- **Constraint:** No chat consensus, repeated success, or memory write-down is equivalent to promotion.
- **Constraint:** `LEARNING_SYSTEM.md` remains a companion explainer; learning is not auto-promotion.
- **Constraint:** Route materially insufficient evidence, contested authority, unresolved disagreement, mixed target boundaries, or broken application trace into escalation.

## 7. Compatibility notes

- **Decision:** Packet structure may be adopted before every project retrofits a full promotion queue.
- **Decision:** Legacy evidence and reasoning surfaces may be referenced when the bounded target and trace chain are explicit.
- **Decision:** Adoption is compatibility-first and does not require immediate retroactive rollout across older files.

## 8. Knowledge-artifact promotion classes

The first holding-layer iteration adds explicit candidate classes for managed KB governance. These classes do not bypass the existing packet requirement.

Allowed candidate classes:

- `candidate`
- `strong_candidate`
- `essence_candidate`
- `best_practice_candidate`
- `project_card_candidate`
- `archive_candidate`

These classes describe the intended destination of a governed change. They do not, by themselves, change accepted truth.

## 9. KB promotion routing

When a durable learning or research artifact is routed through managed KB lanes, the minimum promotion flow is:

1. place or log the item as a candidate in the correct KB lane
2. attach source references, evidence summary, and intended destination class
3. verify with the required partner for that lane or artifact class
4. escalate to operator approval when the threshold band or target surface requires it
5. apply only through the valid packet path if the target is accepted truth, managed law, project-interface authority, or runtime/config behavior

## 10. Required verification by artifact class

- `essence_candidate`: domain or function owner plus `meta_detective`
- `best_practice_candidate`: domain or function owner plus `meta_ops`
- `project_card_candidate`: `meta_ops` plus the relevant project-interface owner
- `archive_candidate`: lane owner plus `special_ops__hygiene_clean`; operator approval if not clearly reversible and low impact

Lane-specific companion ledgers or templates may help package these changes, but they remain subordinate to this protocol.

## 11. Threshold guard

Any T3/T4 candidate touching managed law, accepted truth, project-interface surfaces, or config remains operator-approved by default.
