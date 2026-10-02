---
type: Research
title: "Decision record and proposed choices"
description: "Decision record and proposed choices for the APEX OpenMausBot adoption research."
status: candidate
date: 2026-09-27
---

# Decision record and proposed choices

## Status definitions

- EXISTING: recorded in the supplied canonical APEX contracts or later local handover.
- OBSERVED: read-only evidence collected during this research.
- PROPOSED: recommendation awaiting an operator choice or pilot evidence.
- OPEN: competing choices not resolved.
- ACCEPTED: reserved for an explicit new operator decision; none is fabricated here.

Research-file creation was explicitly requested. That authorizes this bundle, not runtime adoption or changed canonical doctrine.

## Decision ledger

| ID | Status | Decision or proposition | Basis | Consequence / reopen condition |
|---|---|---|---|---|
| D01 | EXISTING | Multi-Agent runs require explicit activation | A01/A04 | No always-on swarm by default |
| D02 | EXISTING | Weekly Orchestrator is separate | A01/A17 | Explicit cross-system handoffs |
| D03 | EXISTING | Alfred and Meta Ops share the main conversation | A02/A10 | Do not split into autonomous peer bots by naming convention |
| D04 | PROPOSED | Pilot Option A before product-native team adoption | A02 + S19/S24 | Depends on native skill/agent discovery test |
| D05 | PROPOSED | Do not assign product Chief in Option A's first test | S20/S21 | Avoid conflicting product/native routing; reassess after evidence |
| D06 | EXISTING | Preserve fresh blind Detective lenses | A05/A09 | Persistent history requires isolation proof |
| D07 | EXISTING | Retain Claude-family review baseline | A05/A09 | Different family requires deliberate policy change |
| D08 | PROPOSED | Keep pilot conversations on Ask | S03 | Effective tools still need separate verification |
| D09 | PROPOSED | Exclude Full Access Chief delegation from initial adoption | S03 | Requires redesigned gate/elevation controls if reopened |
| D10 | EXISTING | Files own accepted APEX state | A01/A03 | Product memory is not authoritative |
| D11 | PROPOSED | Keep canonical native skills as initial procedure source | A11 + S08/S23 | Import portability can be evaluated later |
| D12 | OBSERVED | App 0.1.88 is installed; installer matches official digest | S02 + local inspection | No reinstall claimed necessary |
| D13 | OPEN | Select Windows pilot host versus WSL/server execution | A19 + S14/S15 | Resolve working-folder and account custody |
| D14 | OPEN | Confirm July contract baseline versus later runtime scope | A01/A18/A19 | Async question asked; no assumed acceptance |
| D15 | PROPOSED | Start with US-IDEA-01 candidate rehearsal | A12/A13 | Operator chooses actual input |
| D16 | OBSERVED | Existing authority checker implements only part of schema | A08/A15 | Do not claim complete mechanical enforcement |
| D17 | OPEN | Define and prove missing authority-closure enforcement before production writes | A08/A15 | Requires implementation task, not this research |
| D18 | EXISTING | Candidate learning does not auto-promote | A01/A05 | Product learning convenience cannot bypass review |
| D19 | PROPOSED | One scheduler owner per workflow | WF05 + S10 | Avoid parallel Task Scheduler and product triggers |
| D20 | PROPOSED | App backup plus separate external repository/service backup | S12 | Team export alone is insufficient |
| D21 | OPEN | Decide need for external MCP controller | S07 + A02 | New trust boundary and paired credential custody |
| D22 | EXISTING | Current OpenProject initiative excludes Lika | A20 | Adoption does not reopen scope |
| D23 | EXISTING | OpenProject taxonomy requires operator collaboration | A20 | No automatic project hierarchy creation |
| D24 | OPEN | Assign authoritative status fields across APEX, Leela, OpenProject | A20 | Prevent bidirectional conflict |
| D25 | OBSERVED | September 26 record reports consolidated WSL stacks | A19 | Old dual-engine plans require reconciliation; not live reverified |
| D26 | PROPOSED | Preserve domain workflow outcomes; reverify runtime commands | A18/A19 | No blind execution of old examples |
| D27 | OBSERVED | WF07 includes a credential-like literal | WF07 local read | Value excluded; owner assessment needed |
| D28 | PROPOSED | Versioned team package only after pilot acceptance | S09 | Package is deployment input, not authority |
| D29 | OPEN | Define pilot budget, notification policy, and success threshold | Q04/Q08/Q91/Q92 | No invented pricing or workload target |
| D30 | OBSERVED | Source main was read at a later commit than release publication | S02/S26 | Same version string does not prove shipped parity |

## Detailed rationale for the priority choices

### D04 — Minimal semantic change

Option A retains the supplied controller/worker topology.
Option B adds persistent peer memory and product-generated coordination instructions.
Option C retains the controller but introduces a new MCP boundary.
The first test should answer whether the simpler native route is available and faithful.
If it fails, the evidence determines the next option.

### D09 — Approval inheritance

The official detailed guide explicitly documents delegated Full Access from a Chief.
APEX's existing rules require exact mutation confirmation and independent verified inputs.
The product feature is not defective; it serves a different approval model.
Adoption must reconcile the models rather than assume the APEX gate survives unchanged.

### D17 — Enforcement completion

The inspected code checks declared input state and digest.
It does not resolve verification sidecars or prove the full dependency closure.
Existing negative fixtures remain useful.
Passing them does not establish the stronger schema guarantee.
A production decision must explicitly address this difference.

### D26 — Preserve outcomes, revalidate execution

The later migration record changes infrastructure assumptions.
Some WF acceptance commands exercise only a small part of the claimed workflow.
For example, a dummy hash proves hashing, not custody ingestion.
Therefore each migrated workflow needs a real receipt matched to its intended outcome.

## New decision entry template

~~~text
Decision ID:
Question IDs:
Status:
Operator answer, verbatim:
Answer date and channel/reference:
Options considered:
Accepted scope:
Excluded scope:
Evidence and version:
Consequences:
Acceptance test:
Reopen trigger:
~~~

Do not write ACCEPTED solely because the research recommends an option.
