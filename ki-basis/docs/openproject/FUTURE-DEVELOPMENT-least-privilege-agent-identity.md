---
okf_version: "0.2"
type: future-development
title: Deferred agent write-safety hardening (OpenProject) — least-privilege identity + write-autonomy policy
description: Two deferred hardening items — (1) replace the broad admin API token with a dedicated non-admin project-scoped identity, and (2) decide the agent write-autonomy policy. Recorded for future realization; both deferred per operator decision 2026-09-28.
tags: [openproject, security, least-privilege, write-autonomy, agent, deferred, future-development]
status: deferred
decided: 2026-09-28
program_ref: apexai-os-meta/apex-meta/orchestration/architecture-improvements/05-program-closeout/PLAN.md (T13, T16)
---

# Deferred agent write-safety hardening (OpenProject)

Two related hardening items are **deferred** by operator decision (2026-09-28): keep things simple and
trust the agents while the setup is single-user, local, and human-supervised. Revisit when agents run
more autonomously or the instance grows in exposure/complexity.

- **Item 1 — least-privilege agent identity** (program T13) — below.
- **Item 2 — write-autonomy policy** (program T16) — at the end of this file.

# Item 1 — least-privilege agent identity for OpenProject

## Operator decision (2026-09-28): **DEFER**
Keep using the current admin API token for now — the operator trusts the agents not to do
something destructive, and the instance is single-user on a local machine (not internet-exposed).
**Revisit when the system grows more complex or agents run more autonomously.** This file records the
idea, the reasoning, and a ready-to-run recipe so it can be picked up later without re-analysis.

## What it is (plain terms)
Agents talk to OpenProject with an **API token** (a "robot password") stored in `~/.config/openproject/op.env`.
Today that token belongs to the **`admin`** user — the master key to the whole instance (read/edit/delete
everything, change settings, manage users). The hardening is to give the agents a **separate non-admin
user** whose token can do day-to-day task work but **cannot** delete projects, change system settings, or
reach anything outside the Leela project tree.

## Why it would matter later (the value)
- **Blast-radius limiting:** an agent bug, a bad instruction, or a hidden prompt-injection can't cause
  instance-wide damage with a limited key — only edit tasks in the allowed projects.
- **Leak containment:** if the token ever leaks (log, screenshot, synced file), the finder gets limited
  task access, not full control.
- **Auditability:** actions show as `leela-agent`, distinct from human `admin` activity.

These benefits scale with autonomy and exposure; at single-user/local/trusted-agent scale the immediate
risk is low, which is why it is deferred.

## Trigger to revisit (do it when ANY of these become true)
- Agents begin making unattended/scheduled writes without a human in the loop.
- The instance becomes reachable beyond the local host, or is shared with other people.
- More than one agent/tool holds the token, or the token must be shared.
- A destructive capability (e.g. `wp.delete`, `project.delete`) is enabled for autonomous use.

## Ready-to-run recipe (for whoever implements this later)
1. **Custom role** (OpenProject UI → Administration → Roles & permissions): create *"Leela Agent
   (least-privilege)"* with only: view work packages, add work packages, edit work packages, add notes
   (comments), manage work package relations, add/edit attachments. **Exclude** delete, admin, member
   management, project settings.
2. **Non-admin user** (UI → Administration → Users): create e.g. `leela-agent`, Administrator **unchecked**.
3. **API token**: log in as `leela-agent` → My account → Access tokens → generate an **API** token.
4. **Scope**: add `leela-agent` as a member of **Leela & Mastery** (and its children — `Leela`,
   `PM Infrastructure`, and any future sub-projects) with the custom role. Membership can be scripted via
   `POST /api/v3/memberships` once the user exists.
5. **Swap the token**: replace `OPENPROJECT_TOKEN` in `~/.config/openproject/op.env` with the new key
   (keep the admin key safe until verified). Never commit the token.
6. **Verify**: `GET /api/v3/users/me` shows `login=leela-agent`, `admin=false`; a create+reread of a test
   work package in a Leela project still succeeds; a write to a non-member project is refused.

# Item 2 — write-autonomy policy (program T16)

## Operator decision (2026-09-28): **DEFER**
Keep the current **safe default**: every mutating operation is blocked until the operator confirms that
specific action (`--confirmed`). No agent write runs unattended yet. Revisit when unattended/scheduled
writes are actually wanted.

## What it is (plain terms)
Right now the skill treats **all writes the same**: preview → wait for operator OK → then write. The
"write-autonomy policy" is the operator's decision about **which kinds of writes an agent may do on its own
without asking each time**, versus which must always stop for confirmation. Today's `write-policy.md` is
marked *provisional* precisely because that decision hasn't been made — deferring simply keeps the
confirm-everything default.

## The decision to make later (per risk class)
Choose an autonomy level for each class (the classes already exist in
`agent-skills/skills/openproject/references/write-policy.md`):

| Class | Examples | Options to pick from |
|---|---|---|
| Read-only | `wp.get`, `project.list` | already automatic |
| Low-impact reversible | `wp.comment`, `wp.attach` | auto **or** confirm-each |
| Workflow / structure | `wp.create`, `wp.update`, `relation.create`, `project.create` | auto in test scope only **or** confirm-each |
| High-impact | `project.update`, close/archive, bulk edits, membership | confirm-each (recommended) |
| Destructive | `project.delete`, `wp.delete`, `relation.delete` | always confirm + recovery expectation |

## Trigger to revisit (do it when ANY becomes true)
- You want an agent to update tasks/status on a schedule or unattended.
- Confirm-each becomes a real friction cost in day-to-day use.
- A dedicated least-privilege identity (Item 1) is in place, making broader autonomy safer.

## When realized
Promote `agent-skills/skills/openproject/references/write-policy.md` from *provisional* to *accepted*, replacing
the "confirm all mutations" default with the chosen per-class policy, and record the decision here + in the
program owner.

## Related
- Operating the instance: [`RUNBOOK-openproject-17.8-operations.md`](RUNBOOK-openproject-17.8-operations.md)
- Pilot execution decisions: [`DECISION-2026-09-28-pilot-execution-reconciliation.md`](DECISION-2026-09-28-pilot-execution-reconciliation.md)
- Skill + write policy: `agent-skills/skills/openproject/references/write-policy.md`
