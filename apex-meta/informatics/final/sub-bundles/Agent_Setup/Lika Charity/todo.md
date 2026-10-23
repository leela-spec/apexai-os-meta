---
type: Plan
title: Lika Charity — Current Work
description: Bounded work packages for proving and implementing the volunteer and event automation workflows.
status: current
---

# Current Work

## Priority queue

| ID | Work package | Status | Depends on | Acceptance |
|---|---|---|---|---|
| LIKA-W01 | Private Telegram supergroup + Topics pilot | READY | D01 | Two authorized volunteers can post in separate topics; Hermes keeps sessions isolated. |
| LIKA-W02 | Volunteer receipt intake proof | READY_AFTER_W01 | LIKA-W01 | One test receipt reaches Paperless and returns an acknowledgement without duplicate ingestion. |
| LIKA-W03 | Treasurer review path + Firefly write-through | BLOCKED_BY_W02 | LIKA-W02 | Ambiguity creates a review task; approved record writes once and links to evidence. |
| LIKA-W04 | Event topic provisioning automation | LATER | LIKA-W01 | Event creation can create/register topics without manual ID copying. |
| LIKA-W05 | pretix proof | READY | D02 | Read event state and safely test event/order/check-in API behavior. |
| LIKA-W06 | Ideation and voting pilot | READY_AFTER_W01 | LIKA-W01 | Ideas become structured OpenProject records and one vote produces a recorded outcome. |
| LIKA-W07 | Governance-method decision | READY | D03 | Define when Telegram poll is advisory and when a formal decision method is required. |
| LIKA-W08 | German accounting profile + ledger proof | READY | D04 | Confirm legal/tax profile, then test one period dataset in ledger finalist(s). |
| LIKA-W09 | End-to-end charity event pilot | BLOCKED | W02,W05,W06,W08 | One event flows from planning through volunteer receipts and tickets to reviewed finance handoff. |

## First executable slice

1. Create one private test supergroup.
2. Enable Topics.
3. Add only two or three test users.
4. Add the Hermes bot with least required permissions.
5. Create `Pilot Event — Receipts`, `Pilot Event — Ideas`, and `Pilot Event — Operations`.
6. Verify allowed users and topic isolation.
7. Post a non-sensitive test receipt.
8. Stop before creating a finance record if extraction is ambiguous.

## Validation ladder

```text
access control
  -> topic routing
    -> source evidence custody
      -> duplicate prevention
        -> exception review
          -> finance write-through
            -> accounting/tax handoff
```
