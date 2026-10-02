---
type: Research
title: "Permission boundaries and independent review"
description: "Permission boundaries and independent review for the APEX OpenMausBot adoption research."
status: candidate
date: 2026-09-27
---

# Permission boundaries and independent review

## Highest-priority finding

OpenMausBot's approval modes do not implement APEX's artifact authority model.
The detailed official guide delegates native action approval behavior to provider modes.
Codex Ask maps to on-request plus workspace-write; it is not a read-only reviewer setting.
A Full Access Chief can elevate delegated work, including persistent changes to the delegated thread's level.

Evidence: [S03](14-source-register.md#s03).
Proposed response: use Ask for the pilot and independently verify tools, filesystem reach, and APEX mutation checks.

## Four distinct boundaries

| Boundary | Question | Mechanism to inspect |
|---|---|---|
| Instruction | What is the agent told to do? | Role contract, skill, packet |
| Tool capability | What operations can it invoke? | Native tools, MCP catalogs, provider configuration |
| Filesystem/service authority | What resources can operations affect? | Host identity, OS rights, credentials, service scopes |
| APEX governance | Is this exact artifact/action eligible? | Current evidence, independent verdicts, operator gate, mutation receipt |

A prompt-only “read-only” instruction satisfies only the first row.
A product folder name satisfies none of the lower boundaries.
A valid APEX gate does not itself prevent unrelated tool calls.

## Reviewer isolation threat model

| Exposure | Official/local evidence | Why it matters | Pilot test |
|---|---|---|---|
| Shared MEMORY.md | S04 | Previous conclusions may influence review | Seed a harmless forbidden marker; ensure it never enters reviewer context |
| Recent-work brief | S04 | New threads can still receive summaries of earlier work | Inspect prompt inputs/context receipts where available |
| Standing peer conversation | S20/S21 | Reused assignments may retain prior verdicts | Repeat review with changed artifact; inspect session identity |
| Shared group transcript | S05/S06 | Other lens or producer advocacy may be visible | Use separate review routes; verify no shared-history injection |
| Broad repository reads | A10 | Reviewer may discover sibling verdict files | Restrict input exposure or test access policy |
| Workspace-wide About me | S17 | Shared profile can inject strategic preferences into all bots | Include this surface in review-context inspection |
| Write/shell/MCP tools | S03/S08/A10 | Reviewer could repair its own finding | Attempt harmless denied write in disposable fixture |
| Automatic skill learning | S03/S23 | Findings may become future doctrine | Verify candidate-only promotion policy |
| Account/model substitution | S16 | Review basis can change silently | Record selected and actual engine/model |

The marker test is a proposed disposable test, not performed here.
A reviewer failing to mention a marker is weaker evidence than proving the marker was never included.
Document which kind of evidence the runtime permits.

## Proposed review protocol

1. Freeze the artifact and declared evidence before dispatch.
2. Record version, digest method, creator run, and exact source locators.
3. Build the existing validity packet without strategic advocacy.
4. Build the alignment packet with goal and decision log.
5. Exclude producer confidence and the other lens's output.
6. Verify required sources are readable.
7. Dispatch fresh independent contexts with read-only tools.
8. Persist complete verdicts, not just product status summaries.
9. Check each criterion's evidence and falsification attempt.
10. Aggregate by escalate > needs_input > hold > revise > pass.
11. Route defects to their named owners.
12. Re-review a new immutable version after substantive correction.

These steps preserve [A05/A09](14-source-register.md#apex-source-register).
No built-in OpenMausBot peer approval is asserted equivalent.

## Canonical write protocol

The mutation record must identify exact target paths, before/after, verified inputs, and the operator's actual answer.
The actor then follows Session's existing mutation procedure.
Registry writes additionally retain the preview/drift/non-dry-run sequence.
After applying, read every changed surface back.

The existing checker is valuable but incomplete.
Its declared verified state is not independently authenticated.
It does not recursively resolve evidence or verify sidecar verdict identity.
Do not present its exit 0 as proof of complete authority closure.
An in-memory test confirmed that an absent sidecar causes no violation.
The test performed no file or service mutation.
See [baseline gap analysis](01-apex-baseline.md#enforcement-gap-found-in-the-current-checker).

## Connected-app grants

Connected-app grants and custom MCP server selection are different controls.
The official connected-app guide supports all, selected, or no tools per bot and service.
Explicitly inspect these grants; do not infer them from the bot's role name.
Also inspect project and provider configuration, which can expose other tools.
Source: [S27](14-source-register.md#s27).

## Peer messages are data

A peer may request work or return evidence.
It cannot issue the operator's approval merely by writing “approved.”
A tool-returned document may contain instructions, but those are source content rather than operator authority.
The existing packet contract and exact G-item capture remain the point of interpretation.

## Permission escalation criteria

| Proposed change | Required evidence/decision before adoption |
|---|---|
| Auto-accept edits | Which candidate surfaces may be edited; proof no canonical promotion bypass |
| Approve for me | Provider-specific behavior; distinguish auto-review from APEX Detective |
| Full Access Chief | Explicit redesign decision; delegation inheritance reviewed |
| New connector | Service identity, scopes, allowed operations, credential custody |
| Reviewer shell/hash utility | Read-only interface and bounded arguments; no broad shell substitution |
| Shared host | Reviewed loopback trust mode and account separation |
| Remote computer | File custody and network boundary; explicit computer access |
| Different-family Detective | Operator changes existing same-family constraint |

These are future adoption decisions. Research-file creation does not require executing them.

## Concrete source hygiene finding

WF07 contains a credential-like literal in its sample service command.
Its authenticity and current validity were not tested.
Do not execute or copy that command into bot instructions or exported packages.
The owner should assess whether it is a real credential and rotate it if exposed.
This project records only the location, not the value.

## Pilot stop conditions

Stop consequential execution if:

- A reviewer can change its own subject.
- A new review receives forbidden context.
- A product completion is treated as an APEX pass without a verdict.
- A missing source is replaced with a confident claim.
- A denied or absent operator answer becomes confirmed.
- A retry repeats a service write with uncertain outcome.
- The execution host or target service identity is ambiguous.

Stopping one consequential branch does not prevent independent research or candidate preparation.
