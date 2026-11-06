---
okf_version: "0.2"
type: decision-support-and-verification-board
durable_id: M01-QA-20261106
title: "Module 01 — Matrix 1 / Matrix 2 High-Impact Operator Q&A"
description: "Fourteen source-grounded decisions for the non-temporal project matrix and temporal allocation matrix."
status: PROPOSED_DEFAULTS_NOT_APPROVED
baseline_repo: leela-spec/apexai-os-meta
baseline_main_sha: 7e4ed05cb51532fa058d76bc26560a5a6e496b4f
date: 2026-11-06
matrix_1: ORCHESTRATOR-MATRIX-1-DESIGN-HANDOVER-20261106.okf.md
matrix_2: ORCHESTRATOR-MATRIX-2-DESIGN-HANDOVER-20261106.okf.md
decision_status: pending_operator
write_authorization: false
---

# Module 01 — Orchestrator Question and Decision Board

## Decision method

Impact I: value, effectiveness and target achievement. Evidence E: source support and strength of verification. Risk R: potential misjudgment, complexity, collateral effects and future consequences. All 1-100, **estimated rather than measured**. These decision-support ratings are NOT the obsolete mandatory per-project scoring gate and NOT a synthetic composite priority score. State estimates separately from live evidence.

- **L0** low impact and reversible: decide and state.
- **L1** medium impact: option/recommendation/grounding/notes.
- **L2** I >= 80: each option needs realistic worked example, named source evidence, reversal cost, change-of-mind condition.
- **L3** I >= 80 AND (R >= 50 OR E <= 60), or irreversible, or cross-feature: L2 plus two user stories/personas **per option**, a simulation **per option** using a labeled fixture, a comprehension-check round first, letters-reply sheet, independent verification.
- Operator override "Q07 L2" changes level without changing underlying evidence.
- An unanswered question retains its **recommended default as a discussion hypothesis**, NOT an accepted operator decision. **Never** interpret silence as approval for OpenProject writes, calendar writes, scope expansion or repository mutation.
- All L3 simulations below use *W45 committed draft as illustrative fixture*, not verified current work packages or a live calendar. They are design thought experiments, not execution evidence.
- Where a task reference appears as WP-MA-03, it is W45's provisional **local label**, not a real numeric OpenProject ID.
- Decisions already accepted by the operator (D012 forked skill, embedded YAML handoff, no mandatory numeric task gates) remain baseline. The questions below resolve unaccepted consequences and contradictions.

## Comprehension check (before choosing L3 options)

Check C1: OpenProject says "invoice engine in progress", while a Git commit and passing tests prove the PDF code is working. Which describes the *work commitment*; which describes *implementation/verification*? They answer different questions.
Check C2: In W45, "Seq 1" labels both the Master of Arts project in the template and the 09:00-11:00 **Apex OS** time slot in the draft. Are project identity and daily block identity the same concept? Proposed answer: no.
Check C3: W45 says 38 focus hours, but the visible four work windows total 7h/day or 35h in a five-day unconstrained week. Can an AI treat the 38h as confirmed? Proposed answer: no.
Check C4: If the Wednesday meeting disappears after Sunday planning, which worker should refine Wednesday's execution cards? Proposed answer: PrecapNextDay, under the accepted ownership boundary.
Check C5: Does a saved [OP-OFFLINE] tag prove OpenProject is unreachable **today**? No; only an actual current health check can establish that.
Check C6: Does answering this Q&A authorize live status updates or calendar event creation? No.

The operator may correct any comprehension check before choosing letters. The questions are grouped: Round A (Q01-Q05, authority and project truth), B (Q06-Q10, scheduling), C (Q11-Q14, integration and verification).

## Round A — Truth, project development and portfolio scope

### Q01 — L3 (I98/E88/R85): Who owns each kind of state when OpenProject and Git disagree?

**Question:** When a WP's completion status conflicts with source-repo implementation evidence, which system owns what, and which view may change it?

**Options:**
- **A — Single OpenProject source for everything (I70/E30/R85).** Read WP status as proof both that the work is done and that the code exists. Example: OP says "Closed" for invoice export, so Matrix 1 displays it as implemented without reading tests. Grounding: proposed global language in current PrecapWeek skill, broader than actual migration verification.
  - Stories: Operator sees an apparently finished invoice export while code does not run; executor skips a real missing test because "done" came from PM.
  - W45 fixture simulation: local [WP-MA-05] marked closed -> all invoice successor tasks considered ready, despite zero test evidence. **Failure:** conflates commitment and realization.
  - Reverse: high; must audit all displayed claims and work closures. Changes recommendation only if OP actually includes independently verified build/test provenance sufficient for every claim.
- **B — Ownership by question, reconcile conflicts (I98/E88/R24).** OP owns enrolled-project commitments, WP status and dependency metadata; Git/accepted decisions/code/tests own implementation and verification; calendar owns observed meetings. Example: invoice export may be "Open" in OP but code passes: display both and propose a status update, not silently rewrite either.
  - Stories: Operator sees exactly what remains administratively open; executor knows whether software is tested and can attach evidence before requesting WP closure.
  - W45 fixture simulation: [WP-MA-05] OP status OPEN / Git test PASS -> Matrix 1 flags "reconcile PM state" rather than "not implemented" or "fully closed".
  - Reverse: moderate; per-fact source tags can be simplified later. Changes recommendation if a deliberately accepted single authoritative platform includes all evidence and explicit migration approval.
- **C — Git-first for all projects (I66/E60/R68).** Infer active tasks and completion only from repos. Example: a client-approved invoice request exists only as OP work package; weekly precap omits it.
  - Stories: Operator loses PM commitments; executor may finish code that no one currently prioritized.
  - W45 simulation: a new OP invoice deadline absent from repo is invisible. Reverse: moderate-high; must restore enrollment and status mapping.

**Recommendation:** B.
**Reasoning:** 2026-11-06 decision candidate explicitly separates PM work commitments from code/build/product facts; mixed project enrollment remains unverified. This reduces duplicate state and preserves auditability without discarding OP.
**Notes:** A — status is not proof of implemented features. C — repo-only view misses enrolled current commitments.
**Evidence:** Nov 6 authority decision 01 and conflict log C01-C10 (repository, VERIFIED_REPO); live OP not queried (UNKNOWN). **Independent check:** reviewer compares a live WP and matching repo commit/test evidence; intentional disagreement remains visible.

### Q02 — L3 (I97/E55/R80): What happens when the private OpenProject client cannot be reached?

**Question:** How do we continue the Sunday precap without hallucinating identifiers, falsely declaring service outage, or losing known work?

**Options:**
- **A — Stop planning until OP works (I45/E80/R55).** All tasks become blocked from weekly planning. Example: WSL cold boot prevents reaching port 8083, so no W45 strategy can be drafted.
  - Stories: Operator loses the only Sunday planning slot; executor starts Monday without selected work.
  - W45 fixture simulation: no local API -> no Matrix 1 shortlist -> Matrix 2 empty. Reverse: low once OP recovers. Changes recommendation if legally/operationally forbidden to plan without live PM.
- **B — Fail-closed on identity, degrade the plan (I96/E83/R24).** Try root, whoami, project.list, doctor and paginated WP reads via canonical skill. If unreachable *in this run*, display OP-UNRESOLVED with a stable provenance-labelled local ref (e.g., W45-WP-MA-03); keep last-confirmed commitments historical, and limit approval where identities affect writes.
  - Stories: Operator can discuss invoice priorities despite a service outage; executor cannot accidentally update a fabricated "WP#110".
  - W45 simulation: draft has [OP-OFFLINE: WP-MA-03] from earlier; new no-access session reports "OP NOT CHECKED IN THIS RUNTIME; provisional W45-WP-MA-03" and leaves live status unknown.
  - Reverse: low; replace markers after verified API reads. Changes recommendation if there is a separately approved authoritative offline mirror with verified fresh data.
- **C — Assign synthetic numeric OP IDs based on examples (I25/E0/R99).** Treat examples [OP-WP#110] as actual until OP returns. Example: use 110 as invoice navigation WP despite no evidence.
  - Stories: Operator approves the wrong work item; executor may target an unrelated real WP.
  - W45 simulation: WP#110 assigned to Master of Arts; on reconnection it points to an unrelated project. Reverse: very high when writes occurred.

**Recommendation:** B.
**Reasoning:** This is the smallest safe continuation: planning is resilient, but identity claims and mutations remain fail-closed. A historic draft assertion of ECONNREFUSED is not a current probe.
**Notes:** A — freezes useful design work. C — unacceptable reference spoofing.
**Evidence:** agent-skills/master skills/openproject/SKILL.md (canonical API and fingerprinting, VERIFIED_REPO); spec offline markers (approved spec); service state UNKNOWN. **Independent check:** test disconnected and reconnected fixtures, validate no fake numeric IDs and full pagination.

### Q03 — L3 (I95/E55/R75): How are active projects, fifth project and four sequences reconciled?

**Question:** Is "Priority Website" a separate fifth project, a workstream under Master of Arts, or a deliberate overflow item—and must every active project be allocated a daily sequence?

**Options:**
- **A — Fixed 4-project roster, hide anything else (I60/E50/R85).** Only MoA, Investment, Apex OS and Leela appear even if another project has a hard external commitment.
  - Stories: Operator forgets a separately enrolled website; executor sees no allocated time for it.
  - W45 fixture: "Priority Website" appears in highlight list but vanishes from Matrix 1 because only four accepted rows exist. Reverse: moderate-high.
- **B — Dynamic Matrix 1 coverage; four named default execution streams, fifth item classified (I95/E83/R28).** All active and deferred projects appear in Matrix 1; confirm if Priority Website belongs to MoA or separately enrolled; Matrix 2 may allocate dedicated additional/overflow capacity if needed but does not create a fixed five-project gate.
  - Stories: Operator sees a distinct website deadline and consciously schedules/defers it; executor receives project/source identity rather than guessing the website's repository.
  - W45 simulation: fifth website remains "identity to resolve" in Matrix 1, with a review flag in Matrix 2; not silently merged or hidden.
  - Reverse: low. Changes recommendation if operator explicitly locks an immutable four-project scope for this week.
- **C — Hard 5-project roster with fifth daily lane (I65/E36/R68).** Resurrect a mandatory fifth stream and force allocation daily, even if no relevant WP exists.
  - Stories: Operator spends time filling an empty row; executor receives invented backlog to satisfy the schema.
  - W45 simulation: "Priority Website" forced into Seq 5, stealing a slot from a dated MoA invoice. Reverse: moderate.

**Recommendation:** B.
**Reasoning:** v4 explicitly eliminated the fixed roster gate, while v4.1 names four focus sequences. They are not mutually exclusive if project coverage and time-slot commitments are separate. Verify actual project ownership.
**Notes:** A — loses real commitments. C — recreates v1 fixed-roster failure.
**Evidence:** PrecapWeek active_project_set; W45 header "5 Active Projects" vs four project sections (VERIFIED_REPO); ownership UNKNOWN. **Independent check:** verify each candidate project via OP project.list and repo AGENTS/accepted scope.

### Q04 — L3 (I93/E77/R55): How deep should Matrix 1 process decomposition go?

**Question:** Should Matrix 1 list only epics, expand to tasks/subtasks, or fully prescribe 30-minute work units and micro-checklists?

**Options:**
- **A — Project -> epic -> evidenced tasks/dependencies; expand subtasks only when decision-relevant (I94/E85/R22).** Show baseline, target, deliverable, critical prerequisites, iteration points, selected backlog; open details on demand. Example: invoice engine -> schema -> PDF/export gate without dictating line-by-line 30m work.
  - Stories: Operator grasps an epic's progression in one scan; executor later expands a selected work package into precise sprint cards.
  - W45 simulation: three invoice steps and their blockers visible; no forced 3-item cards. Reverse: low; add needed subtask details later.
- **B — Every epic/task/subtask and 30-minute item in Matrix 1 (I69/E48/R77).** Pre-design all sprint microsteps on Sunday as a static source map.
  - Stories: Operator scrolls through ~100 microitems instead of spotting critical path; executor discovers changed repo state Tuesday and discards prior microplans.
  - W45 simulation: each work package has 3 sprint units and more subitems; duplicated again in Matrix 2. Reverse: medium-high; remove stale items while preserving selections.
- **C — Only project names and one-line outcomes (I47/E74/R50).** Example: "Build invoice engine" without showing prerequisite schema/export.
  - Stories: Operator cannot judge the critical path; executor starts the PDF engine before schema.
  - W45 simulation: one line hides the invoice prerequisite chain. Reverse: medium; must reconstruct all steps.

**Recommendation:** A.
**Reasoning:** Captures strategic control and executable selection while respecting PrecapNextDay ownership and token efficiency. Allow explicit expansion for unusually consequential critical paths.
**Notes:** B — excessive detail and role leakage. C — insufficient dependency visibility.
**Evidence:** DESIGN-DECISIONS.md week/day ownership (operator-validated); Matrix1 handover 30m target (newer but not reconciled). **Independent check:** ask operator to identify blocker and next useful outcome from a one-screen project view, and confirm NextDay can expand.

### Q05 — L3 (I92/E58/R68): What makes a work item "critical path" or eligible for the weekly shortlist?

**Question:** What actual evidence must support critical-path labels, readiness, selection and re-entry from the longlist?

**Options:**
- **A — Evidence-backed prerequisites and explicit acceptance criteria (I94/E82/R25).** Mark critical only when dependency/order is documented or operator-accepted; choose shortlist via leverage, deadlines, readiness and capacity; maintain deferred trigger. Example: PDF export depends on verified invoice schema; no build until schema gate.
  - Stories: Operator can explain *why* an item is gating; executor has a direct acceptance check before next step.
  - W45 simulation: draft chain schema -> PDF -> export stays PROPOSED until repo/OP relation confirms; no asserted critical path just from diagram styling. Reverse: low.
- **B — Mark highest-looking impact/urgency as critical (I58/E35/R85).** Derive criticality from I/E/R or narrative excitement.
  - Stories: Operator chases a high-impact UI polish while a compliance gate blocks shipment; executor ignores a lower-scored prerequisite.
  - W45 simulation: UI tree "critical" solely due to its score, while missing DAG schema is skipped. Reverse: high after schedule miss.
- **C — Mark every task in a headline epic critical (I54/E60/R68).** Treat all tasks as blocking to avoid missing anything.
  - Stories: Operator cannot prioritize within the epic; executor serializes parallel work.
  - W45 simulation: every invoice style tweak blocks PDF/export. Reverse: medium.

**Recommendation:** A.
**Reasoning:** Critical path is an evidenced dependency claim, not a visualization ornament or score. Shortlist must be operator reviewable and distinguished from uncommitted longlist.
**Notes:** B — score cannot prove dependency. C — label loses meaning.
**Evidence:** dual-view and Matrix1 specs (VERIFIED_REPO as proposals), live dependency relations UNKNOWN. **Independent check:** independent graph reviewer checks cycles, actual OP relations and tests before critical-path promotion.

## Round B — Time, capacity and weekly-vs-daily detail

### Q06 — L3 (I98/E95/R72): What does "Sequence 1–4" mean everywhere?

**Question:** Are the four sequences fixed project identities or recurring daily time windows in the calendar?

**Options:**
- **A — Named project streams, independent of clock-block IDs (I98/E95/R15).** Seq 1 MoA; Seq 2 Investment; Seq 3 Apex OS; Seq 4 Leela. Time windows have separate labels (Block A/B/C/D); a project may occupy any available block and can have no allocation on some days.
  - Stories: Operator follows MoA from its process path to a Wednesday allocation; executor can work on MoA in the afternoon without renaming it "Seq 3".
  - W45 simulation: Monday 09:00 Apex OS becomes "Block A / Seq 3 Apex OS"; Monday 13:30 MoA becomes "Block C / Seq 1 Master of Arts". Reverse: low; mostly relabel cells.
- **B — Sequence = fixed daily time window (I75/E48/R75).** Seq 1 always 09-11; Seq 2 next midday block; project assigned per day.
  - Stories: Operator sees "Seq 1" refer to five different projects through the week; executor's MoA references break when it moves to the afternoon.
  - W45 simulation: Monday Seq 1 Apex, Tuesday Seq 1 Apex, Wednesday Seq 1 Leela; contradicts spec's Seq 1 = MoA. Reverse: medium-high: rewrite all links/labels.
- **C — A project permanently owns one fixed 2h clock window (I71/E50/R75).** Seq 1 MoA always 09-11, etc, even with fixed meetings or dependency delays.
  - Stories: Operator must ignore unavoidable 09:30 client call or displace MoA work; executor waits idle though an afternoon focus window exists.
  - W45 simulation: Tuesday 11:00 external sync and compressed 11:30 slot reduce sequence flexibility. Reverse: high after missed work.

**Recommendation:** A.
**Reasoning:** Same identity must survive changing time slots; W45 intentionally demonstrates why separate IDs matter. Fixed project sequence names do not require identical daily order.
**Notes:** B — direct source contradiction. C — inflexible calendar geometry.
**Evidence:** SPEC-DUAL-VIEW-WEEKLY-PRECAP.md + live template four named rows (VERIFIED_REPO); W45 draft clock-slot sequence conflict (VERIFIED_REPO). **Independent check:** reviewer traces one MoA item across three days and verifies its sequence label does not change.

### Q07 — L3 (I98/E64/R85): What is the source and calculation for available hours?

**Question:** How will weekly work slots be calculated and labeled without inventing meetings, 2h windows or focus capacity?

**Options:**
- **A — Calculate interval-by-interval from current calendar, show assumptions separately (I98/E88/R22).** Distinguish observed meeting occupancy, protected routines, available work windows, planned allocation and buffer; recalc after constraints. Example: 09-11=2h; 11:30-12:30=1h; 13:30-15:30=2h; 15:45-17:45=2h => 7h/day, 35h/5 days before extra meetings.
  - Stories: Operator trusts capacity figures and can spot overload; executor can see which exact block would be invalidated by a new meeting.
  - W45 simulation: 38h claim corrected to max 35h in listed windows, before other actual constraints. Reverse: low; source metadata enables re-evaluation.
- **B — Set 4 x 2h every day and adjust mentally (I65/E45/R80).** Declare standard 8h focus even though 11:30-12:30 is one hour.
  - Stories: Operator commits 40h of work that cannot fit; executor drops the last sprint or protected breaks.
  - W45 simulation: 4x2x5=40 but calendar grid fits 35; difference hides overload. Reverse: medium-high.
- **C — Use loose "busy/light" day labels only (I62/E85/R52).** No arithmetic, only qualitative meeting density.
  - Stories: Operator cannot allocate a 2-hour focus task confidently; executor cannot know whether 30m or 2h is available.
  - W45 simulation: Tuesday called "light" despite a fragmented midday slot. Reverse: medium.

**Recommendation:** A.
**Reasoning:** Capacity is a calculation, not a narrative or independent source of truth. Do not call a historic W45 meeting a real current meeting without a calendar read.
**Notes:** B — false 2h assumption. C — too weak for full-width hourly design.
**Evidence:** W45 draft time geometry (VERIFIED_REPO), calendar real events UNKNOWN. **Independent check:** deterministic interval-overlap test plus independent auditor; no impossible overlapping planned blocks.

### Q08 — L3 (I94/E75/R70): Does Sunday precap specify detailed 30-minute sprint checklists?

**Question:** Which layer owns the exact S1/S2/S3 microtasks and at what level does the weekly grid stop?

**Options:**
- **A — Week selects outcome and capacity; day expands exact sprints (I95/E91/R20).** Matrix 2 cells say "Wed / MoA invoice schema -> ready for PDF engine (2h candidate)"; PrecapNextDay on Wednesday creates 30m work and three microchecks where useful.
  - Stories: Operator sees a calm weekly agenda; executor sees precise tasks after checking Wednesday's current code and calendar.
  - W45 simulation: a Wednesday "Invoice schema review" remains directional Sunday; on Wednesday daily worker expands into tax formula/unit tests/review evidence. Reverse: low; add details selectively for a near-term critical task.
- **B — All 30-minute sprint items and 3-item lists fixed Sunday (I76/E55/R82).** Fully specify work for six days regardless of later changes.
  - Stories: Operator faces hundreds of microtasks; executor keeps stale tasks after Tuesday bug fix.
  - W45 simulation: first block has 3 x 30m x 3 = 9 checklist lines per cell, over 4 blocks x 5 days = potentially 180 microchecks before Saturday. Reverse: medium-high.
- **C — No day allocations at all until PrecapNextDay (I50/E72/R62).** Weekly precap states outcomes only and postpones weekdays.
  - Stories: Operator cannot see meeting conflicts or sequence allocation; executor starts Monday without strategic balancing.
  - W45 simulation: all tasks stay in a list; none appears against Tuesday stakeholder sync. Reverse: medium.

**Recommendation:** A.
**Reasoning:** v4 operator-validated ownership separates week architecture from daily execution. v4.1 detail-first specs conflict with this, so require deliberate promotion instead of drift.
**Notes:** B — duplicates downstream output and creates fake certainty. C — loses core weekly architecture value.
**Evidence:** DESIGN-DECISIONS.md + PrecapNextDay/SKILL.md (VERIFIED_REPO), v4.1 detailed W45 spec (CONFLICT). **Independent check:** two-stage fixture, Sunday then changed-Wednesday calendar, and assert no duplicated stale microsteps.

### Q09 — L3 (I85/E62/R57): Does Saturday belong in the weekly calendar?

**Question:** Is Saturday solely a review/buffer reference, an optional operator-directed workday, or a normally planned sixth day?

**Options:**
- **A — Mon-Fri standard plan; Saturday optional review/buffer annotation (I90/E90/R18).** Keep a sixth column visually labeled "Review/Buffer (not committed work)" but do not promise Saturday execution unless explicitly approved.
  - Stories: Operator can see a protected recovery option; executor does not infer new Saturday commitments.
  - W45 simulation: "Saturday review gate" remains visible, none of the four sequences automatically receives 30m sprint cards. Reverse: low.
- **B — Saturday is standard execution day (I72/E44/R75).** Assign four sequences, 30m sprints and deliverables all six days.
  - Stories: Operator discovers weekend time is already committed; executor treats buffer as mandatory.
  - W45 simulation: Saturday "Buffer" becomes 7h work. Reverse: medium-high, calendar cleanup required.
- **C — Remove Saturday completely (I68/E80/R45).** Pure Mon-Fri calendar with no Saturday review annotation.
  - Stories: Operator loses an explicit optional end-of-week review marker; executor has no weekend ambiguity.
  - W45 simulation: Saturday column disappears; Friday recap carries all review signals. Reverse: low.

**Recommendation:** A.
**Reasoning:** Preserves v4 weekday planning while explaining the v4.1 Saturday display. Whether to show an optional review column remains operator choice; no automatic calendar events.
**Notes:** B — exceeds current production scope. C — discards useful intentional review/buffer visibility.
**Evidence:** live PrecapWeek validation excludes Saturday (VERIFIED_REPO); v4.1 dual-view includes Saturday column (VERIFIED_REPO). **Independent check:** scope validation plus operator review in a Friday overload fixture.

### Q10 — L3 (I95/E65/R90): Who may propose and write calendar blocks?

**Question:** Does PrecapWeek write planned events on Sunday, does PrecapNextDay write approved day blocks, or is all placement manual?

**Options:**
- **A — PrecapWeek proposes; PrecapNextDay requests approved writes (I97/E91/R24).** Sunday shows real meetings and proposed capacity; daily worker revalidates and prepares a write request that requires operator confirmation and tool confirmation; existing external meetings are immutable.
  - Stories: Operator gets realistic planning without surprise calendar changes; executor adjusts Wednesday after a Tuesday meeting moved.
  - W45 simulation: Sunday proposes Wed 13:30-15:30 MoA; Wed has a new meeting, NextDay moves the slot and seeks explicit approval before writing. Reverse: low; pending proposals are reversible.
- **B — Sunday auto-writes every draft slot (I72/E34/R92).** Treat the W45 grid as final and insert all 2h blocks into Google Calendar.
  - Stories: Operator discovers unapproved work calendar clutter; executor double-books a real client meeting.
  - W45 simulation: 35-40h events written without live source; Tuesday conflicts not noticed. Reverse: high; must clean real calendar.
- **C — Never write any planned focus blocks (I58/E92/R38).** Calendar is read-only forever, daily focus blocks remain prose.
  - Stories: Operator manually re-enters approved work; executor cannot rely on calendar reservations.
  - W45 simulation: day plan remains in Markdown even after confirmed free time. Reverse: low; future opt-in support possible.

**Recommendation:** A.
**Reasoning:** Already closest to active runtime boundary and makes the risk of real external mutations explicit; calendar integration is a capability, not inferred permission.
**Notes:** B — violates current no-write boundary and external-meeting safety. C — loses useful approved execution automation.
**Evidence:** PrecapWeek/calendar-planning-guidance.md and PrecapNextDay/SKILL.md (VERIFIED_REPO); actual Google Calendar connectivity UNKNOWN. **Independent check:** schedule fixture with new conflict; verify *zero* writes without operator confirmation.

## Round C — One handoff, rendering, approval and proof

### Q11 — L3 (I96/E84/R61): How do Matrix 1 and Matrix 2 share task identities and pass one compact seed?

**Question:** Should the downstream YAML copy all sprint data, reference the one Brief and selected next-day work, or become an independent machine packet?

**Options:**
- **A — One Brief, stable refs, compact embedded presentation_handoff (I97/E93/R15).** Matrix 2 work cells reference Matrix 1 selected items. YAML keeps Brief path/section, target day, intended outcomes, review state, capacity assumption, fixed constraints and carry-forward; NextDay rereads relevant parts and elaborates only the actual day.
  - Stories: Operator approves one artifact, not two conflicting plans; daily worker opens the exact source brief and knows what to prioritize tomorrow.
  - W45 simulation: YAML contains "next_target_day: Monday" and source refs, not a huge duplicate monday_hourly_schedule tree. Reverse: low; add a missing orientation field if evidence demands it.
- **B — Full Monday sprint tree copied into embedded YAML (I68/E69/R65).** Treat the entire Monday schedule as handoff payload.
  - Stories: Operator edits visual grid but forgets YAML, causing divergence; daily worker trusts stale YAML and ignores updated meetings.
  - W45 simulation: full monday_hourly_schedule exists in draft; changing grid leaves 10s of duplicate lines. Reverse: medium.
- **C — Create a second machine artifact and replace embedded YAML (I42/E27/R86).** Separate weekly plan packet with its own checklist and status.
  - Stories: Operator must approve parallel artifacts; executor chooses the wrong version.
  - W45 simulation: original brief and new machine seed disagree on MoA timeline. Reverse: high; requires migration and reconciliation.

**Recommendation:** A.
**Reasoning:** Preserves accepted Module 01 invariant (no duplicate seed) and makes cross-matrix traceability explicit; downstream is a reader of the same artifact.
**Notes:** B — stale duplicate schedule. C — reverses v4 template promotion.
**Evidence:** PrecapWeek/SKILL.md, DESIGN-DECISIONS.md, live template and W45 YAML (VERIFIED_REPO). **Independent check:** change next-day meeting in fixture; verify daily worker reads updated brief and one seed only.

### Q12 — L3 (I98/E75/R95): What is the approval and writeback ownership at the end of the loop?

**Question:** Can the Weekly Orchestrator or a stage skill change OpenProject status or Git files automatically, or must updates be proposed and routed to the owning system after explicit approval?

**Options:**
- **A — One portfolio approval for week, per-action approved WP writes (I98/E90/R19).** Weekly Brief remains proposed until approved; later execution evidence targets owning OP WP via canonical client preview/--confirmed, lockVersion and post-write reread; Apex Session only for truly Apex-owned records. Existing repo file edits follow patch-only policy.
  - Stories: Operator knows exactly which work is approved and which WP will change; executor cannot silently "complete" a task in an unrelated task system.
  - W45 simulation: completed invoice export -> proposed OP status change with evidence; no write until approved, followed by verified reread. Reverse: low for proposals; actual writes still require auditable rollback procedure.
- **B — Auto-update OP and Apex Session on each recap (I64/E30/R95).** Mirror each completion to both task graphs without a clear ownership boundary.
  - Stories: Operator sees two conflicting statuses; executor cannot determine which task is canonical.
  - W45 simulation: same invoice item closed in OP and duplicate Apex task; later one reopens only in OP. Reverse: very high due to split-brain.
- **C — Never close or update PM tasks (I40/E85/R60).** All evidence stays in Git artifacts; human manually updates OP later.
  - Stories: Operator loses current PM state between weeks; executor repeats already completed work.
  - W45 simulation: export passes but remains open indefinitely in OP. Reverse: moderate; backlog reconciliation required.

**Recommendation:** A.
**Reasoning:** Separates week approval from mutation authorization and respects the November 6 transition candidate's proposed ownership split. The operator must explicitly accept routing changes before production skill patches.
**Notes:** B — unsafe dual-write and missing approval. C — PM state goes stale.
**Evidence:** agent-skills/master openproject write policy, Nov 6 transition decision and active weekly-orchestrator (VERIFIED_REPO); OP live write path UNTESTED. **Independent check:** API dry-run/preview, explicit confirmation audit, lockVersion conflict, reread, no Apex duplicate.

### Q13 — L2 (I83/E85/R35): What is the canonical rendering arrangement for Markdown and HTML?

**Question:** Which format is the source artifact and which is a view, and what qualifies as "interactive"?

**Options:**
- **A — One Markdown Brief as canonical durable content plus generated, read-only responsive HTML view (I93/E90/R21).** Markdown remains reviewable in Git/Obsidian. HTML shows a calendar readable at 100% width with horizontal overflow; "interactive" is reserved for actual working controls and state.
  - Worked W45 example: edit the Monday task ref in the canonical Brief; regenerated HTML must display the identical work ref. The current .html contains CSS and no script controls, so it is styled rather than genuinely interactive.
  - Reversal cost: low. Recommendation changes if operator selects a tested interactive source format with explicit durable export contract.
- **B — Independently hand-edit Markdown and HTML (I65/E75/R70).** Rich visual changes can diverge from task source. Worked example: Monday project fixed in .md but stale in .html.
  - Reversal cost: moderate-high for content reconciliation.
- **C — HTML-only source with opaque backend state (I70/E40/R60).** Easier custom interaction but hard to diff/patch or consume as a source-grounded agent artifact. Worked example: downstream seed has no canonical Markdown path.
  - Reversal cost: high.

**Recommendation:** A.
**Reasoning:** A single stable source plus deterministic rendering prevents two planning truths and supports patch-only auditability.
**Notes:** B — divergence. C — loses durable transparent source and current skill compatibility.
**Evidence:** W45 .md + .html and live PrecapWeek template (VERIFIED_REPO); no tested two-way interactive engine. **Independent check:** content parity, valid HTML, keyboard/readability and wide/narrow viewport screenshots.

### Q14 — L3 (I96/E62/R77): What proves these handovers are usable and production-ready?

**Question:** Is file creation sufficient, or must a future real-week test prove source truth, scheduling, daily handoff and operator comprehension?

**Options:**
- **A — One real week + next-day operational test, independently reviewed (I97/E88/R18).** Fetch actual OP IDs/updated times; read verified calendar; produce both views; have operator identify priority/blocker/available time; update one next-day plan after a change; verify no unsanctioned writes; compare evidence against outcomes.
  - Stories: Operator can approve/edit from the Brief without understanding schemas; executor can pick up Tuesday with no missing source refs.
  - W45 illustrative simulation: fabricated 38h claim fails interval check, provisional WP markers fail "live IDs" requirement, YAML duplication flagged. Test intentionally FAILS those claims pending real sources. Reverse: low; more fixtures can be added.
- **B — Pass if Markdown/HTML files exist with required headings (I40/E80/R88).** A template-shaped file is declared production-ready.
  - Stories: Operator discovers the reported hours are impossible; executor follows unverified WP links.
  - W45 simulation: all required headings exist, yet 35h vs 38h and Seq labeling remain wrong. Reverse: high after live run fails.
- **C — Exhaustive multiweek autonomous simulation before operator feedback (I55/E35/R76).** Simulate all cases with invented records, delaying actual testing.
  - Stories: Operator waits for a large synthetic test suite; executor finds first real calendar exception instantly invalidates it.
  - W45 simulation: hundreds of imagined tasks pass tests while no live OP or calendar is read. Reverse: high resource/time cost.

**Recommendation:** A.
**Reasoning:** A real operator-job test identifies errors structural validators cannot and satisfies November 6 decision candidate's promotion requirements without overbuilding tests.
**Notes:** B — format is not correctness. C — synthetic thoroughness does not substitute for current evidence.
**Evidence:** Nov 6 transition validation gate, Module 01 HANDOVER and W45 observed contradictions (VERIFIED_REPO); real run PENDING. **Independent check:** source/freshness reviewer and operator-comprehension reviewer separately sign findings.

## Decision coverage and dependency order

Q01-Q02 -> source ownership/freshness; Q03 -> project coverage; Q04-Q05 -> Matrix 1 detail/critical paths; Q06-Q07 -> semantic sequence mapping and time reality; Q08-Q10 -> weekly/day split, Saturday and calendar rights; Q11-Q13 -> shared handoff, mutation, rendering; Q14 -> final acceptance.

**Cross-matrix invariants** (design defaults, not silently promoted):
1. Unique work refs must be unchanged from Matrix 1 selection to Matrix 2 allocation and downstream NextDay handoff.
2. Matrix 1 stores no day/time; Matrix 2 does not infer source-of-truth status.
3. Unknown source and conflict remain visible with freshness and provenance.
4. The Brief remains one operator artifact, with embedded presentation_handoff; no wrapper agents or duplicate machine seeds.
5. Capacity is computed, not guessed; existing calendar meetings are never edited by precap.
6. Numeric ratings support the Q&A analysis but cannot become a mandatory task approval gate or composite score.
7. Production changes need exact-context patch-only review; the new files in this folder are proposals, not production contract replacement.

## Letters-only reply sheet (defaults shown, not accepted until operator responds)

- Q01 B — ownership by question
- Q02 B — OP unresolved/fail-closed degradation
- Q03 B — dynamic project set and four default streams
- Q04 A — selective project/epic/task detail
- Q05 A — evidenced critical path and shortlist
- Q06 A — stable project sequence ID distinct from time block ID
- Q07 A — calculate calendar capacity from actual time intervals
- Q08 A — week outcomes, day sprint expansion
- Q09 A — Saturday optional non-committed review/buffer
- Q10 A — weekly proposals, daily approved calendar writes
- Q11 A — one Brief + compact presentation_handoff references
- Q12 A — scoped approvals and owner-targeted writes
- Q13 A — Markdown canonical, HTML generated view
- Q14 A — real-week + next-day independent verification

**Operator reply form (plain text):**
\`C1-C6: understood / corrections ...; Q01 B; Q02 B; ...; Q14 A; Q07 L2 (override); extra notes ...\`

This is a **review sheet**, not an automatic approval mechanism. Silence means the questions remain pending, not that irreversible actions are authorized.

## Source index: required files and where they feed the handovers

Core control and version:
- apex-meta/handoff/weekly-precap-evolution-and-version-audit-handover-20261105.okf.md
- apex-meta/tools/project-improvement-orchestration-weekly/CURRENT-STATE.md
- apex-meta/tools/project-improvement-orchestration-weekly/DECISIONS.md
- apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/HANDOVER.md
- apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/DESIGN-DECISIONS.md
- apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/HANDOVER-MODULE-01-GUIDED-REAL-WORKFLOW-WALKTHROUGH.md
- apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/SPEC-DUAL-VIEW-WEEKLY-PRECAP.md
- .claude/skills/weekly-orchestrator/SKILL.md
- .claude/skills/PrecapWeek/SKILL.md

Matrix 1:
- apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/HANDOVER-01-PROJECT-MATRIX-EPICS-CRITICAL-PATH.md
- apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/WEEKLY_PRECAP_DRAFT_W45.md
- apex-meta/handoff/weekly-orchestration-openproject-transition-2026-11-06/01-DECISION-OPENPROJECT-WEEKLY-ORCHESTRATION.okf.md
- apex-meta/handoff/weekly-orchestration-openproject-transition-2026-11-06/02-CONFLICT-AND-DECISION-LOG.okf.md
- leela-spec/agent-skills (master): skills/openproject/SKILL.md, client/opCall.js and references/write-policy.md; project repositories' AGENTS.md/accepted decisions/current source/test artifacts

Matrix 2:
- apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/HANDOVER-02-TIMELINE-CALENDAR-SEQUENCE-SPRINT-VIEW.md
- apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/WEEKLY_PRECAP_DRAFT_W45.html
- .claude/skills/PrecapWeek/weekly-command-brief-template.md
- .claude/skills/PrecapWeek/calendar-planning-guidance.md
- .claude/skills/PrecapWeek/weekly-blueprint-standard.md
- .claude/skills/PrecapWeek/weekly-blueprint-meeting-example.md
- .claude/skills/PrecapWeek/references/validation-checklist.md

Shared output and downstream:
- .claude/skills/PrecapNextDay/SKILL.md
- apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/research/PRECAP-WEEK-INPUT-PIPELINE-DECISION-HANDOVER.md
- Existing presentation_handoff in the active Weekly Command Brief template
- Historical old schema/agents in apex-meta/archive/weekly-orchestration/ are provenance only, NOT runtime.

## Reconciliation and promotion sequence

1. Operator reviews comprehension C1-C6 and Q01-Q14 with concrete examples.
2. Create an explicit accepted-decision record; record overrides and dissent; no presumed approval.
3. Refresh OpenProject through authorized **local** canonical client, and real calendar access; if missing, retain uncertainty.
4. Simulate one real intended week and next day with current source WPs and calendar constraints; independent architecture + operator-usability review.
5. Prepare exact-context patch files rather than rewriting existing production contracts. Changes to active skills, templates and governance files must be narrow, diff-verified and explicitly reviewed.
6. Do not modify status/PM/calendar records without separate per-action confirmation and reread.
7. Retain D012/D013 direct forked-skill topology, one Weekly Command Brief, one embedded downstream YAML, and the no-mandatory-numeric-gate invariant.
