---
type: Research
title: "Operations, observability, and recovery"
description: "Operations, observability, and recovery for the APEX OpenMausBot adoption research."
status: candidate
date: 2026-09-27
---

# Operations, observability, and recovery

## Operating model

The controller should report outcome, evidence location, current phase, pending decision, and next permitted action.
Product status is operational evidence. Repository records remain the APEX continuation basis.

Recommended run receipt fields:

| Field | Purpose |
|---|---|
| run_id / packet_id | Link work across product and repository |
| app_version / engine_version / model / account_alias | Reproduce runtime selection |
| host / resolved working folder / repository revision | Prevent environment ambiguity |
| bot_id / thread_id / assignment_id | Locate execution evidence |
| input paths and digests | Bind work to the intended basis |
| output paths and digests | Recover complete artifacts |
| execution outcome | Distinguish completed, failed, interrupted, waiting |
| review references | Distinguish completion from validation |
| operator decision reference | Distinguish validation from authorization |
| before/after and fetch-back result | Prove applied effect |
| next phase / unresolved risk | Resume without chat memory |

These are receipt metadata, not a competing replacement for the canonical handoff schema.

## Scheduling and the existing portfolio

OpenMausBot routines require its harness to be running.
The official scheduler describes timezone-aware schedules, bounded catch-up, and protection against overlapping runs of the same routine.
Those properties do not establish exactly-once behavior for external service writes.

Choose one scheduler owner per workflow.
WF05 already names Windows Task Scheduler.
Do not add an OpenMausBot schedule for the same computation without defining which owner is authoritative.
Use Europe/Berlin explicitly for local business schedules where appropriate.
Test daylight-saving behavior and restart timing before enabling production recurrence.
Sources: [S10–S11](14-source-register.md#s10), [WF05](../new_final_v4/workflow_plans/WF05_IPOS_WEEKLY_MACRO_REGIME.md).

## Retry and duplication policy

The product can resume or retry work after failures.
The official incident guide describes Chief routing and bounded retries.
That is useful recovery machinery, not permission to repeat an uncertain external effect.

Before retrying a task with possible side effects:

1. Inspect the last durable receipt.
2. Query the target's current state through its approved interface.
3. Determine whether the intended operation already happened.
4. Reuse the established operation identifier where the service supports it.
5. Continue only the unapplied remainder.
6. Record uncertainty if the state cannot be determined.

No generic exactly-once adapter is claimed implemented.
For coordinate_bots, preserve request_key according to the actual tool schema.
For legacy delegation, preserve the returned delegation ID.
Do not mix identifiers or assume one route's limits apply to another.
Sources: [S18](14-source-register.md#s18), [S21–S22](14-source-register.md#s21).

## Receipts are not archival storage

The inspected legacy delegation source bounds its receipt count, retention, and result length.
Therefore copy complete returned artifacts and review verdicts to the run folder promptly.
A short transcript tail or pruned receipt must not be the only evidence.

Capture source and target IDs before closing a conversation.
Keep the original worker return alongside the integrated artifact.
An integration summary is not a substitute for the original evidence.

## Backup scope

Use the app's documented backup mechanism for product state.
Use repository and service-specific backups for external project files and databases.
The official Settings backup excludes external project directories and saved credentials/connections.
A team template export is not a full backup.

Before restore, inspect the documented replacement semantics and paused automation behavior.
Recheck external paths and service identity after moving hosts.
Keep backup passwords separate from archives.
Raw filesystem copies may contain more sensitive material than Settings exports.
Source: [S12](14-source-register.md#s12).

## Recovery drills

| Drill | Required result |
|---|---|
| Quit app during candidate work | Incomplete phase remains visible; no fake completion |
| Restart after queued peer request | Known assignment state; no duplicate dispatch inferred |
| Reviewer times out | hold, not pass |
| Operator absent | Pending gate remains unconfirmed |
| App data restored | Bots and artifacts recover; automations reviewed before restart |
| External repository unavailable | Explicit missing-source state |
| Provider login expires | Human action identified; no credential guessing |
| Source artifact changes after review | Verification invalidated; re-review required |
| Controller chat disappears | H6 and run files locate the next action |
| Service write response lost | Read-before-retry; no speculative repeat |

These are acceptance tests, not claims about tests already passed.

## Cost and workload visibility

Use reported token usage and cost where the provider supplies them.
Do not interpret missing cost as zero.
Account subscriptions and API billing remain provider-specific.
No price or spending forecast is invented in this research.

Measure a small representative run before setting a recurring workload.
Capture number of worker turns, review loops, retries, elapsed time, and operator interruptions.
Compare those to the existing workflow, not to an imagined ideal swarm.
Source: [S06](14-source-register.md#s06), [S16](14-source-register.md#s16).

## Operations division

OpenMausBot may notify and route incidents.
Meta Ops decides how the APEX phase resumes within scope.
The operator supplies missing authority and account actions.
Qualified humans retain financial, legal, and physical-safety decisions.
Existing service skills retain their own identity checks and write contracts.
