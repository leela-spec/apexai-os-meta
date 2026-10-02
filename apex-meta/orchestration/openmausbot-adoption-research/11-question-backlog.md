---
type: Research
title: "Operator and technical question backlog"
description: "Operator and technical question backlog for the APEX OpenMausBot adoption research."
status: candidate
date: 2026-09-27
---

# Operator and technical question backlog

## How to use this backlog

Questions are grouped by decision boundary, not as a single questionnaire to answer at once.
P0 questions affect the first pilot or a consequential trust boundary.
P1 questions affect repeatability and operations.
P2 questions affect later expansion.

Open means unanswered in this task.
Existing means a local contract already supplies the baseline; reopen only deliberately.
Verify means collect evidence, not ask the operator to guess a technical fact.
No proposed default below is treated as accepted.

Start with Q01, Q03, Q07, Q13, Q19, Q25, Q37, and Q55.

## A. Objective and baseline

| ID | Priority / status | Question | Why it changes the design |
|---|---|---|---|
| Q01 | P0 / Open | Should the supplied July entrypoint govern the first pilot, with later runtime plans treated as migration inputs? | Selects contract precedence |
| Q02 | P0 / Open | Is OpenMausBot intended as the main operator UI, an execution pool, or a full replacement for the current controller? | Selects A/B/C architecture |
| Q03 | P0 / Open | What single real outcome should the first pilot produce? | Defines measurable scope |
| Q04 | P1 / Open | Which current pain matters most: visibility, handoffs, missed work, context loss, or operator effort? | Sets comparison metrics |
| Q05 | P0 / Existing | Keep Weekly Orchestrator separate with explicit handoffs? | Supplied contracts say yes |
| Q06 | P1 / Open | Is mobile access required in the first deployment? | Adds pairing and remote surface |
| Q07 | P0 / Open | Must work continue while the Windows laptop sleeps? | Determines execution host |
| Q08 | P1 / Open | What evidence would make you reject the pilot even if it produces useful text? | Establishes adoption threshold |

## B. Deployment and paths

| ID | Priority / status | Question | Why it changes the design |
|---|---|---|---|
| Q09 | P0 / Verify | Has the installed 0.1.88 app completed onboarding and engine detection? | Installation alone is insufficient |
| Q10 | P0 / Verify | Which exact release features are present in the installed build versus inspected main? | Prevents version assumptions |
| Q11 | P0 / Open | Should the first controller run on Windows or on the recorded WSL host? | Changes paths and credentials |
| Q12 | P0 / Verify | Which checkout is current authority for each participating repository? | Avoids editing a stale copy |
| Q13 | P0 / Open | Which disposable folder may hold the first pilot's candidate outputs? | Bounds rehearsal writes |
| Q14 | P1 / Verify | Are current service ports and identities consistent with the September 26 migration record? | Old plans may target wrong services |
| Q15 | P1 / Open | Is a local server sufficient, or is a dedicated always-on host required later? | Sets maintenance and backup scope |
| Q16 | P1 / Verify | Does the active engine resolve Windows paths, WSL paths, or container paths? | Prevents false file-access claims |
| Q17 | P1 / Verify | Do required skill-discovery links work without elevation? | Check Developer Mode if needed |
| Q18 | P1 / Open | Who owns app and engine updates, and when are regressions checked? | Prevents untested drift |

## C. Role topology

| ID | Priority / status | Question | Why it changes the design |
|---|---|---|---|
| Q19 | P0 / Open | Start with one APEX controller using native workers, or require visible product peers immediately? | Selects initial complexity |
| Q20 | P0 / Existing | Keep Alfred and Meta Ops in one conversation? | Existing contract requires it |
| Q21 | P1 / Open | Which specialists need persistent product identity beyond a role definition? | Avoids unnecessary bot creation |
| Q22 | P0 / Verify | Can the chosen runtime invoke the exact project agent definitions? | Validates Option A |
| Q23 | P0 / Verify | Does product Chief prompting conflict with native APEX delegation? | Determines whether to assign Chief |
| Q24 | P1 / Open | Which domain workers can remain temporary instead of permanent team members? | Controls context and maintenance |

## D. Detective independence

| ID | Priority / status | Question | Why it changes the design |
|---|---|---|---|
| Q25 | P0 / Existing | Retain fresh same-family Claude reviewers until explicitly changed? | Preserves current trust decision |
| Q26 | P0 / Verify | Can each lens receive a fresh context without previous verdicts or producer advocacy? | Central review invariant |
| Q27 | P0 / Verify | Which memory, recent-work, recall, group, and project-context inputs reach each reviewer? | Identifies hidden contamination |
| Q28 | P0 / Verify | Can read-only tools be enforced on the actual reviewer execution path? | Prompt text is insufficient |
| Q29 | P0 / Open | Keep the recorded hash-attestation pattern or approve a bounded read-only hash utility? | Resolves known reviewer limitation |
| Q30 | P0 / Verify | Will the review detect a deliberately wrong source locator in a disposable fixture? | Tests useful scrutiny |
| Q31 | P0 / Verify | Does a timeout or malformed verdict produce hold rather than pass? | Prevents silent promotion |
| Q32 | P0 / Verify | Can re-review bind to a new version without receiving the author's persuasive correction narrative? | Preserves independence |
| Q33 | P1 / Open | What observed failure would justify a different-family judge? | Avoids speculative model expansion |
| Q34 | P0 / Verify | Can a reviewer access the other lens's verdict through shared files? | Context isolation is not file isolation |
| Q35 | P1 / Open | How much reviewer trace should be retained for audit without storing unnecessary private content? | Sets custody scope |
| Q36 | P0 / Verify | Is deterministic aggregation actually applied to both complete verdicts? | Prevents majority-vote substitution |

## E. Mutation and approval

| ID | Priority / status | Question | Why it changes the design |
|---|---|---|---|
| Q37 | P0 / Open | Must full authority-closure enforcement be implemented before any production adoption? | Current checker is partial |
| Q38 | P0 / Verify | Which path currently resolves verification_ref and confirms independent passing verdicts? | Not done by inspected canon-write |
| Q39 | P0 / Verify | Can another tool write canonical state without passing the gate? | Distinguishes guidance from enforcement |
| Q40 | P0 / Existing | Preserve operator_validation per exact consequential mutation? | Existing gate primitive |
| Q41 | P0 / Open | Which low-consequence candidate surfaces may be edited without repeated business decisions? | Reduces friction without changing authority |
| Q42 | P0 / Open | Keep all pilot conversations on Ask and prohibit Full Access Chief delegation? | Avoids inherited elevation |
| Q43 | P0 / Verify | What effective permissions apply to existing threads versus bot defaults? | Changing a default may not change old threads |
| Q44 | P0 / Open | How will a product approval be linked to the exact APEX G-item and digest? | Prevents chat-only authorization |
| Q45 | P1 / Open | How should revoke, split, defer, and revise decisions be represented in the operator UI? | Preserves real decision shapes |
| Q46 | P0 / Verify | Does fetch-back prove the intended target changed and nothing else in scope did? | Completes mutation evidence |

## F. Skills, memory, and knowledge

| ID | Priority / status | Question | Why it changes the design |
|---|---|---|---|
| Q47 | P0 / Verify | Do all required native skill references resolve under the chosen working directory? | Procedures are more than SKILL.md |
| Q48 | P0 / Verify | Does context: fork retain its execution meaning through this route? | Weekly stages depend on isolation |
| Q49 | P1 / Open | Should imported skills be deployment copies or should canonical project skills remain primary? | Prevents divergence |
| Q50 | P1 / Verify | Which import route preserves supporting files, and which skips them? | Official surfaces differ |
| Q51 | P0 / Open | What may controller memory contain beyond canonical pointers and preferences? | Avoids shadow authority |
| Q52 | P0 / Existing | Keep learning candidate until review and operator acceptance? | Existing doctrine rule |
| Q53 | P1 / Open | Who reviews changes to standing instructions and enabled skills? | Configuration can change behavior |
| Q54 | P1 / Verify | Can a package export include private starter notes or sensitive copied text? | Requires export review |

## G. Existing workflows and domain services

| ID | Priority / status | Question | Why it changes the design |
|---|---|---|---|
| Q55 | P0 / Open | Is US-IDEA-01 the preferred first real pilot? | Minimal existing end-to-end example |
| Q56 | P1 / Open | Which of the remaining six stories is next after the pilot? | Sets migration order |
| Q57 | P1 / Open | Which WF01–WF10 workflows are actually in regular use today? | Separates active work from plans |
| Q58 | P1 / Open | Does the program's explicit schedule override its contradictory numeric-order sentence? | Needed before portfolio execution |
| Q59 | P0 / Verify | Which WF commands have real execution receipts rather than expected-output examples? | Prevents false readiness |
| Q60 | P0 / Verify | Is the credential-like WF07 literal real and still active? | Owner must assess exposure |
| Q61 | P0 / Existing | Preserve no automated broker execution for IPOS? | Existing domain invariant |
| Q62 | P1 / Open | Should investment monitoring initially return candidates without changing its Watch Register? | Defines consequence boundary |
| Q63 | P1 / Open | Which human reviews physical workshop safety? | AI output cannot replace qualified authority |
| Q64 | P1 / Open | Who authorizes public media and website release? | Separates staging from publication |
| Q65 | P1 / Open | Which financial/legal professional validates invoicing and settlement rules? | Plans' compliance claims are not verified law |
| Q66 | P1 / Verify | Can real custody/retrieval be tested without pretending a dummy SHA-256 command is ingestion? | Repairs WF06 acceptance evidence |
| Q67 | P1 / Verify | Can Telegram intake survive restart without losing or duplicating events? | Help output does not establish this |
| Q68 | P1 / Open | What is the explicit handoff between weekly planning and Multi-Agent work? | Prevents automatic cross-activation |

## H. OpenProject and multi-account scope

| ID | Priority / status | Question | Why it changes the design |
|---|---|---|---|
| Q69 | P1 / Existing | Keep Lika excluded from the current personal/professional OpenProject initiative? | Later handover records exclusion |
| Q70 | P1 / Existing | Design the Mastery of Arts taxonomy with the operator rather than infer it? | Explicit existing preference |
| Q71 | P0 for PM / Verify | Has the existing OpenProject research and skill authority been read before integration? | Mandatory dependency in handover |
| Q72 | P0 for PM / Open | Which system owns each status field: APEX, Leela's SSOT, or OpenProject? | Prevents competing state |
| Q73 | P1 / Verify | Which of the stated two Claude, two Codex, and one Antigravity accounts actually work now? | Fleet statement is not readiness |
| Q74 | P1 / Open | Which account is assigned to each workload and why? | Capacity and data boundary |
| Q75 | P1 / Verify | Does each account discover the same accepted service skill and target the same instance? | Cross-account consistency |
| Q76 | P1 / Verify | Does Hermes ACP preserve the needed existing profile behavior? | Engine support is not profile equivalence |

## I. Connectors and remote access

| ID | Priority / status | Question | Why it changes the design |
|---|---|---|---|
| Q77 | P0 for connectors / Open | Which specific services are necessary for the first accepted workflow? | Minimizes irrelevant connections |
| Q78 | P0 for connectors / Verify | What effective tools arrive from app config, project config, and provider user config? | Avoids hidden tool inheritance |
| Q79 | P0 for connectors / Verify | Are service credentials scoped to the intended private or community instance? | Prevents cross-instance writes |
| Q80 | P1 / Open | Is external MCP orchestration needed, or can the pilot stay inside the app? | Determines pairing/token work |
| Q81 | P0 for shared host / Verify | Is loopback treated as owner or service, and can agent shells reach it? | Critical self-hosted boundary |
| Q82 | P1 / Open | Is remote desktop/computer control needed at all for document workflows? | Avoids unnecessary computer access |
| Q83 | P1 / Open | Who can pair remote devices, and how are lost devices revoked? | Defines remote administration |
| Q84 | P1 / Verify | Does a disabled product MCP selection leave provider-local tools available? | Product UI is not full enforcement |

## J. Reliability and acceptance

| ID | Priority / status | Question | Why it changes the design |
|---|---|---|---|
| Q85 | P1 / Open | Which scheduler owns each recurring workflow? | Avoids double dispatch |
| Q86 | P1 / Open | What catch-up behavior is acceptable after sleep or downtime? | Prevents stale surprise execution |
| Q87 | P0 for service writes / Verify | How is an uncertain external effect reconciled before retry? | Prevents duplicates |
| Q88 | P1 / Open | What run evidence must survive product receipt pruning? | Defines durable custody |
| Q89 | P1 / Open | What recovery time and acceptable data-loss window are required? | Sets backup frequency |
| Q90 | P1 / Verify | Can app state and external repositories both be restored successfully? | Backup existence is insufficient |
| Q91 | P1 / Open | What spend or subscription-usage ceiling should the pilot respect? | Bounds actual trial |
| Q92 | P1 / Open | Which failures should notify immediately versus wait for a digest? | Sets interruption policy |
| Q93 | P0 / Open | Who accepts the final pilot evidence and decides production adoption? | Prevents self-approval |
| Q94 | P1 / Open | Which changes require rerunning the pilot suite: app, model, tools, role, or host? | Defines regression boundary |
| Q95 | P1 / Verify | Can an independent session resume from the saved files without this conversation? | Tests the foundational invariant |
| Q96 | P2 / Open | After adoption, should an exportable team package be maintained as a versioned deployment artifact? | Enables repeatable expansion |

## Resolution rule

Record answers in [the decision log](12-decision-log.md).
Link each accepted decision to the operator's exact answer or existing authoritative record.
Close technical questions only with receipts.
Do not replace unknowns with the research author's confidence.
