---
type: Research
title: "Pilot protocol and acceptance criteria"
description: "Pilot protocol and acceptance criteria for the APEX OpenMausBot adoption research."
status: candidate
date: 2026-09-27
---

# Pilot protocol and acceptance criteria

## Pilot objective

Demonstrate that one real APEX idea workflow can run through OpenMausBot while preserving the existing contracts.
Start with candidate outputs in an isolated workspace.
The pilot passes only on recorded evidence, not on a team diagram or successful app launch.

Suggested first story: US-IDEA-01.
This follows the existing simulation's small role set and source-preserving outcome.
The operator still chooses the real input and any eventual canonical placement.
Evidence: [A12–A13](14-source-register.md#apex-source-register).

## Test stages

### P0 — Readiness and authority

Record app build, engine version, model, account alias, host, project path, and approved pilot scope.
Read the exact project rules used by that runtime.
Prove which APEX role and skill definitions were discovered.
Keep external service writes and scheduled triggers outside this stage.

### P1 — Bounded execution

Run intake, one candidate worker, and controller persistence.
Return a complete packet through the existing schema.
Use actual source files and cite their locators.
Inspect the candidate and the source before marking the stage complete.

### P2 — Independent review

Freeze the artifact.
Run separate validity and alignment lenses.
Demonstrate fresh contexts and read-only behavior.
Inject a deliberate harmless citation error into a disposable test version.
A useful review must detect and route it, rather than merely praise structure.

### P3 — Gate and interruption

Present a real bounded decision.
Verify that no answer leaves the mutation unconfirmed.
Stop and resume the run from disk.
Recompute digests before any later application.

### P4 — Approved mutation rehearsal

Use a clearly labeled disposable target, not canonical project or service state.
Record exact scope and operator confirmation if the rehearsal includes a consequential action.
Read back the result.
Show that stale evidence and missing review block the intended gated path.

### P5 — Adoption decision

Compare the observed result with each acceptance criterion.
Record pass, partial, fail, or not_run per test.
Only accepted scope becomes eligible for a production run.
Keep unrelated workflows and permissions disabled until separately proven.

## Acceptance matrix

| Test | Priority | Evidence required | Failure action |
|---|---|---|---|
| T01 Runtime identity | P0 | Actual app/CLI/model/host receipt | Resolve mismatch |
| T02 Project discovery | P0 | Exact roles and skill reference paths loaded | Fix discovery, not prompt around missing files |
| T03 One controller | P0 | Alfred/Meta Ops phases share gate and run context | Revisit topology |
| T04 Bounded worker | P0 | Packet in, candidate return, stop honored | Narrow routing |
| T05 Read-only Detective | P0 | Harmless write attempt denied; effective tool list | Do not use reviewer for consequence |
| T06 Blind review | P0 | No forbidden context in supported trace plus independent verdicts | Change review route |
| T07 Citation defect detection | P0 | Deliberate defect found with exact source evidence | Review method fails |
| T08 Negative verdict aggregation | P0 | One critical non-pass blocks promotion | Fix aggregation |
| T09 Missing operator decision | P0 | not_requested persists; no write | Gate fails |
| T10 Stale artifact | P0 | Digest mismatch blocks application | Re-review |
| T11 Sidecar/dependency evidence | P0 | Missing or forged authority cannot pass full adopted path | Close current enforcement gap |
| T12 Canonical mutation owner | P0 | No alternate role writes accepted state | Restrict access or revise claims |
| T13 Fetch-back | P0 | Exact post-write state matches approved change | Mark failed/uncertain |
| T14 Disk-only resume | P0 | New conversation resumes from packet/H6 files | Improve continuation |
| T15 Full return custody | P1 | Complete verdict saved despite bounded product receipts | Persist artifact separately |
| T16 Peer-history contamination | P0 for Option B | Repeated assignments prove desired freshness | Avoid persistent peer review |
| T17 Chief delegation level | P0 for Option B | Receiving conversation mode observed | Remove elevation path |
| T18 Skill package assets | P1 | References/scripts/fork semantics survive actual route | Keep canonical native route |
| T19 Connector effective scope | P0 for connectors | Global, project and provider sources accounted for | Hold service access |
| T20 Host path correctness | P0 for WSL | Exact runtime path and repository identity | Correct environment design |
| T21 Duplicate assignment | P1 | Stable request identity, no duplicate effect | Add bounded reconciliation |
| T22 Interrupted side effect | P0 for service writes | Target queried before retry | Hold uncertain operation |
| T23 Scheduled absence | P1 | Sleep/restart/catch-up results recorded | Select correct scheduler host |
| T24 Restore | P1 | App plus external files recover without unwanted replay | Correct backup scope |
| T25 Weekly boundaries | P0 for weekly | G1–G5 and stage forks preserved | Separate weekly pilot |
| T26 Domain portfolio | P2 | One real receipt per selected WF | Keep untested workflows unadopted |

No T01–T26 is marked passed merely because a source describes the feature.
Local executable inspection contributes to T01 readiness only.

## Regression cases from existing APEX

Rerun the existing negative fixtures:

- Candidate promoted as confirmed.
- Stale input digest.
- Missing sources_evidence.
- Reviewer modifying its subject.
- Missing operator confirmation.
- Positive authorized fixture.

These tests are useful baselines.
They do not cover the full authority closure gap identified in this research.
Add no claim of complete enforcement unless the stronger adopted path is tested.

## Evidence folder convention

Proposed future pilot layout:

~~~text
pilot-runs/<run-id>/
  environment.md
  00-intake.md
  01-candidate.v1.md
  02-source-manifest.md
  03-artifact-lock.md
  04-validity-input.md
  05-alignment-input.md
  06-validity-verdict.md
  07-alignment-verdict.md
  08-aggregation.md
  09-gate-presentation.md
  10-mutation-record.md
  task_plan.md
  findings.md
  progress.md
  next-session.md
~~~

This is a proposed file convention, not an executed simulation record.
Use canonical schema fields and the existing H6 section requirements.

## Minimum useful comparison

Compare the same bounded task in the existing APEX route and the pilot.
Measure defect detection, missing-source handling, operator interruption count, and ability to resume.
Record latency and cost only when actually observed.
A prettier UI or larger agent roster is not a success metric by itself.
