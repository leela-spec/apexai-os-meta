---
type: Plan
title: Master of Arts Business — Current Work
description: Bounded work packages for proving and implementing the business automation workflows.
status: current
---

# Current Work

## Priority queue

| ID | Work package | Status | Depends on | Acceptance |
|---|---|---|---|---|
| MOA-W01 | Telegram supergroup + forum-topic Hermes pilot | READY | D01 | Authorized team member posts image in one topic; Hermes receives it in the correct isolated session. |
| MOA-W02 | Receipt intake proof | READY_AFTER_W01 | MOA-W01 | One real test receipt reaches Paperless, produces OCR, and creates no duplicate on replay. |
| MOA-W03 | Expense classification + Firefly write-through | BLOCKED_BY_W02 | MOA-W02 | High-confidence record writes once; ambiguous record creates an OpenProject review item. |
| MOA-W04 | Event-topic setup automation | LATER | MOA-W01 | Event setup returns and records Telegram thread IDs without manual retyping. |
| MOA-W05 | pretix API proof | READY | D02 | Read one event; create a sandbox/test event or equivalent safe fixture; read order/check-in state. |
| MOA-W06 | tixlr API evidence check | BLOCKED_EXTERNAL | None | Obtain official API documentation or vendor credentials. |
| MOA-W07 | Ideation-to-programme pilot | READY_AFTER_W01 | MOA-W01 | Ideas become OpenProject records; one vote produces a recorded outcome and next work. |
| MOA-W08 | German ledger bake-off | READY | D03 | Same small reconciled dataset imports into each finalist and produces a usable adviser/tax handoff. |
| MOA-W09 | End-to-end event pilot | BLOCKED | W02,W05,W07,W08 | One event flows from planning through receipts/ticket state to reconciled handoff. |

## First executable slice

1. Create one private test supergroup.
2. Enable Topics.
3. Add the Hermes Telegram bot with least required permissions.
4. Allowlist only test users and the test chat.
5. Create `Test Event — Receipts` and `Test Event — Ideas` topics.
6. Bind or prompt the receipt topic for receipt intake.
7. Post one non-sensitive test receipt image.
8. Verify topic isolation before any finance mutation.

## Verification order

```text
Telegram delivery
  -> Hermes topic isolation
    -> Paperless evidence custody
      -> extraction validation
        -> OpenProject exception path
          -> Firefly write-through
            -> tax-ledger handoff
```
