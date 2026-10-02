---
type: Research
title: "Claim verification and unresolved gaps"
description: "Claim verification and unresolved gaps for the APEX OpenMausBot adoption research."
status: candidate
date: 2026-09-27
---

# Claim verification and unresolved gaps

## Evidence contract

Every material recommendation below names the facts that support it and the remaining verification.
“Verified” in this table means source-checked, not APEX authority.state: verified.
All project artifacts remain candidate.

| Claim ID | Claim | Evidence | Classification | Remaining test |
|---|---|---|---|---|
| C01 | APEX is explicitly activated, not always on | A01/A04 | APEX | Preserve activation in pilot |
| C02 | Alfred and Meta Ops share main conversation | A02/A10 | APEX | T03 |
| C03 | Weekly system is separate | A01/A17 | APEX | T25 |
| C04 | Consequence needs review plus operator gate | A05/A06/A08 | APEX | T08–T13 |
| C05 | Existing checker is partial | A15 inspected functions plus missing-sidecar in-memory test | LOCAL | Full-path enforcement implementation/test |
| C06 | Old simulation index disagrees with actual records | A13/A14 and simulations README | LOCAL | No adoption inference from stale index |
| C07 | OpenMausBot 0.1.88 is installed | Executable metadata | LOCAL | Live onboarding/engine check |
| C08 | Downloaded installer matches official asset | S02 API digest + Get-FileHash | LOCAL | No signature/safety claim |
| C09 | Current main is not proven identical to release | Source commit date and release date | LOCAL | Build-specific capability probes |
| C10 | Provider modes determine native approvals | S03 | DOC/SRC | Chosen provider actual behavior |
| C11 | Codex Ask is not read-only | S03 provider mapping | DOC/SRC | Effective sandbox/tool check |
| C12 | Chief Full Access can propagate to delegates | S03 | DOC/SRC | Installed-build inheritance test |
| C13 | Separate threads can share memory | S04/S05 | DOC | T06/T16 |
| C14 | Recent-work brief can reveal other conversation summaries | S04 | DOC/SRC | Actual injected context |
| C15 | Normal coordinate_bots uses standing peer conversation | S20/S21 | SRC | Active tool/profile and history probe |
| C16 | Native subagents support separate contexts/tool restrictions | S19 | Official DOC | Availability inside selected OpenMausBot route |
| C17 | External MCP lacks approval/admin operations listed in S07 | S07 | DOC/SRC | Actual exposed catalog |
| C18 | Product MCP selection does not cover all project/provider config | S08 | DOC/SRC | Effective tool inventory |
| C19 | Team package is not full recovery backup | S09/S12 | DOC | Test export/import scope |
| C20 | Imported teams start conservatively configured | S09 | DOC/SRC | Actual import preview/result |
| C21 | Skill route portability needs explicit testing | S09/S23 discrepancy and APEX dependencies | PROPOSAL | T18 |
| C22 | Local routines need running harness | S10/S11 | DOC | Sleep/restart drill |
| C23 | One scheduler owner avoids duplicate dispatch ownership | WF05 + S10 | PROPOSAL | Chosen ownership and duplicate test |
| C24 | External project directories need separate backup | S12 | DOC | Restore drill |
| C25 | Legacy receipts are bounded and pruned | S22 constants | SRC | Full-return custody test |
| C26 | Later WSL record supersedes assumptions in older dual-engine plans | A18/A19 | APEX recorded conflict | Live host/service validation |
| C27 | WF06 dummy hash does not prove ingestion | WF06 command inspection | LOCAL | Real ingest/retrieve receipt |
| C28 | WF09 help invocation does not prove intake effects | WF09 command inspection | LOCAL | Real staged-intake receipt |
| C29 | WF07 contains credential-like source text | WF07 local inspection | LOCAL | Owner assesses validity/exposure |
| C30 | WF numeric sequence conflicts with explicit program schedule | A18 | LOCAL | Operator/owner resolves ordering |
| C31 | OpenProject taxonomy is not ours to invent | A20 | APEX recorded instruction | Read prior research and operator session |
| C32 | Hermes listed as supported engine does not prove old profile equivalence | S16 + WF profiles | DOC + UNKNOWN | Actual ACP/profile integration |
| C33 | Option A is the lowest-change first experiment | C02/C13/C15/C16 | PROPOSAL | Compare pilot evidence |
| C34 | Native reviewer route is preferable for initial isolation test | C13–C16 + A05 | PROPOSAL | T05–T07 |
| C35 | Same-family review constraint remains baseline | A05/A09 | APEX | Operator decision if changed |
| C36 | Full mechanical enforcement cannot yet be claimed | C05 + broad tool capability | LOCAL/PROPOSAL | Stronger proof than current fixture suite |

## Unresolved contradictions

| Gap ID | Sources in tension | Current treatment |
|---|---|---|
| G01 | APEX architecture says enforcement open; later gate invokes existing checker | Checker exists but implements a narrower guarantee |
| G02 | Simulation index says no runs; idea record says full pass | Use exact dated record and preserve inconsistency |
| G03 | Narrow skill-import comment versus richer team package docs | Route-specific testing; no universal assertion |
| G04 | General approval marketing versus detailed native modes | Use detailed mode documentation |
| G05 | Old two-engine deployment plans versus reported WSL consolidation | Treat infrastructure as changed but not live audited here |
| G06 | Main source and released binary use same version string on different dates | Pin both; test installed behavior |
| G07 | Program says numeric sequence; schedule uses domain ordering | Explicit unresolved workflow decision |
| G08 | Handoff schema permits nested envelope; checker expects top-level frontmatter keys | Use existing fixtures for baseline; decide canonical parser compatibility before adapters |

## Evidence that would change recommendations

- Native project subagents unavailable in the installed product: prefer a tested external controller or approved adapter.
- Product review route proves clean context and enforced access: Option B becomes more attractive.
- Full authority closure implemented and tested elsewhere: update C05/C36 with exact path and receipts.
- Current service topology differs from migration record: revise environment mapping before any domain execution.
- Operator intentionally replaces the existing control contracts: treat that as a new design decision, not a source correction.

## Excluded evidence

No forum post, third-party review, benchmark anecdote, or model recollection is used as product authority.
No sample expected-output text is counted as an executed result.
No local service credentials were validated or copied.
No official product feature is presented as proof of this custom integration working.
