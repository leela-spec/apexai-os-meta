# APEX Weekly Command Brief Visualization Decision Report

## 1. Recommendation

**Select Candidate A: an annotated Project × Week calendar matrix** as the primary `Weekly_Command_Brief` visualization.

It should use **projects as rows and Monday–Friday as columns**, with each cell containing the actual day-level movement for that project, including the required inline `Task (I94/R25/E9)` notation. Day headers carry the **day role + capacity shape + only material fixed constraints**; dependencies, deadlines and deliberate deferrals are encoded locally with a very small symbol vocabulary and expanded only when an exception needs explanation.

This is the strongest design because it answers both operator questions with one visual:

- scan a **column** → “What happens Tuesday?”
    
- scan a **row** → “What happens to Leela this week?”
    

It scored **4.60/5 (92/100)** and tied mathematically with the more elaborate dual-lens board. The matrix is nevertheless the recommendation because the dual-lens design achieves its score by **showing the same plan twice**, which becomes a material failure under realistic density and directly conflicts with APEX's established anti-duplication/progressive-disclosure direction.

**Delivery recommendation:** use **Mode B — a complete Markdown Brief plus an optional automatically generated enhanced projection of that same matrix**. The Markdown remains independently complete and authoritative. The enhanced view should be a **read-only static HTML/SVG projection**, generated deterministically from the Brief and linked from it; it should **not** be an independently editable calendar or planning system.

## A conventional hourly week calendar is specifically **not** recommended. Current calendar components such as FullCalendar TimeGrid explicitly couple weekdays to a vertical time axis, while timeboxing tools schedule tasks at exact times and durations. That is excellent for daily scheduling, but it would visually claim a precision that Module 01 deliberately assigns to `PrecapNextDay`.

## 2. Recommended W34 Visualization

### Evidence status of this prototype

The following are **verified repository facts**:

- Leela, MasterOfArts, Apex and Investment are equal primary W34 categories.
    
- The MasterOfArts website is a named weekly focus.
    
- Monday–Friday all have standard assumed capacity in the approved W34 packet.
    
- Monday is `start`, Tuesday/Wednesday `build`, Thursday `review`, Friday `buffer`.
    
- Residual is recovery/support rather than a promised daily flow.
    
- Calendar information was unavailable and must be revalidated downstream.
    
- The project task names and dependency chains below come from the current W34 project-state material.
    

The W34 artifact predates the newly locked I/R/E notation. Therefore, **the I/R/E values below are research-fixture values, not reconstructed historical W34 facts**, except for the user-supplied example `Verify Home runtime (I90/R20/E95)`. Likewise, Monday's concrete work is directly corroborated by the next-day plan, while Tue–Fri use the verified dependency chains to construct a consistent comparison fixture rather than pretending the historical W34 packet assigned those exact tasks to those days.

### Recommended primary view

|Project|**MON · START**STANDARD|**TUE · BUILD**STANDARD|**WED · BUILD**STANDARD|**THU · REVIEW**STANDARD|**FRI · BUFFER**STANDARD|
|---|---|---|---|---|---|
|**Leela**|Verify Home runtime (I90/R20/E95)|Verify bounded spatial Skill Tree runtime (I88/R25/E92)|Promote bounded cluster to primary Skill Tree navigation (I92/R45/E80)↳ after Mon + Tue|Make ScopeSelection handoff origin-aware (I86/R40/E78)↳ after Wed|Reconcile ResolutionRequest/Context with Home + Skill Tree (I82/R35/E76)↳ after Thu|
|**MasterOfArts ★ focus**|Locate current website-definition source (I92/R15/E85)|Reconcile purpose, audience & conversion outcomes (I94/R25/E80)↳ after Mon|Define information architecture & page responsibilities (I90/R25/E78)↳ after Tue|Define page-level content & interactions (I88/R30/E75)↳ after Wed|Review website definition for implementation readiness (I86/R20/E72)↳ after Thu|
|**Apex**|Re-baseline ApexKB implementation & contract (I88/R20/E90)|Build operator-value & retrieval benchmark (I84/R25/E85)↳ after Mon|Evaluate cheapest credible upgrade path (I78/R30/E80)↳ after Tue|Evaluate alternatives & hybrid options (I80/R35/E78)↳ after Tue|Run controlled ApexKB comparison (I90/R40/E75)↳ after Wed + Thu|
|**Investment**|Collect required operator inputs for one equal branch (I82/R15/E60)|Define video-discovery contract (I76/R25/E68)↳ if video branch chosen|Collect alert-contract conditions (I80/R20/E65)|Collect decision-feedback process input (I78/R20/E65)|Configure/test video-search job (I72/R35/E70)↳ after Tue|
|**Residual — recovery/overflow**|Recovery reserve|Recovery reserve|Recovery reserve|Recovery reserve|Recovery / overflow|

**Week exceptions:** `★` named weekly focus · `↳` consequential dependency.  
**Calendar:** unavailable in W34; `STANDARD` is an accepted planning assumption, not verified free time. PrecapNextDay must revalidate actual capacity.  
**Deliberate allocation:** Residual receives no promised daily project flow so the four equal primary categories retain the W34 planning envelope.

### Why this view works

The matrix is doing real comparative work rather than using a table merely for visual layout. GOV.UK's current design-system guidance recommends tables when information needs to be **compared and scanned across rows and columns**, which is exactly the operator task here. It also warns that excess table data hurts usability, which is why the matrix should contain the **week architecture**, while deeper project detail stays underneath through progressive disclosure.

Structurally, this is also close to the **resource timeline** pattern used in scheduling interfaces: FullCalendar's current Resource Timeline places time horizontally and resources in rows. The APEX adaptation deliberately removes precise duration bars and uses fixed weekday columns instead, because the weekly layer has day placement but not executable intra-day timing.

---

## 3. Runner-Up — Dual-Lens Week Board

### Concrete W34 example

#### Calendar lens

||**MON**|**TUE**|**WED**|**THU**|**FRI**|
|---|---|---|---|---|---|
|**Role**|Start|Build|Build|Review|Buffer|
|**Capacity**|Standard|Standard|Standard|Standard|Standard|
|**Work**|Leela — Verify Home (I90/R20/E95)MoA — Locate website source (I92/R15/E85)Apex — Re-baseline ApexKB (I88/R20/E90)Investment — Collect inputs (I82/R15/E60)|Leela — Verify Skill Tree (I88/R25/E92)MoA — Reconcile website purpose (I94/R25/E80)Apex — Build benchmark (I84/R25/E85)Investment — Define video contract (I76/R25/E68)|Leela — Promote bounded cluster (I92/R45/E80)MoA — Define IA (I90/R25/E78)Apex — Evaluate cheapest path (I78/R30/E80)Investment — Collect alert conditions (I80/R20/E65)|Leela — ScopeSelection handoff (I86/R40/E78)MoA — Page requirements (I88/R30/E75)Apex — Evaluate alternatives (I80/R35/E78)Investment — Decision-feedback input (I78/R20/E65)|Leela — Reconcile contexts (I82/R35/E76)MoA — Readiness review (I86/R20/E72)Apex — Controlled comparison (I90/R40/E75)Investment — Test video job (I72/R35/E70)|

#### Project lens

**Leela:** Verify Home → Verify Skill Tree → Promote cluster → ScopeSelection → Resolution context  
**MasterOfArts ★:** Locate source → Purpose/audience → IA → Page requirements → Readiness review  
**Apex:** Re-baseline → Benchmark → Cheapest path / alternatives → Controlled comparison  
**Investment:** Input → selected branch contract → blocker clearing → implementation/test  
**Residual:** recovery/overflow reserve

### Why it lost

The visual quality is strong and both questions are easy to answer. But the second lens is essentially an alternate rendering of the first. As the week gets more constrained, the same dependency, deferral and meeting information has to appear in **two human surfaces**, creating either drift or obvious repetition.

That conflicts with two strong repository doctrines: minimum necessary duplication and progressive disclosure. Earlier APEX research explicitly identified table/schema repetition as a failure mode and recommends links/references instead of reprinting related content.

**Verdict:** excellent dashboard; inferior canonical Brief.

---

## 4. Stress-Test Result

### Overall result

|Candidate|Meeting-heavy Scenario B|Dependency/deadline Scenario C|Result|
|---|---|---|---|
|**A — Project × Week matrix**|Capacity deformation stays obvious because it lives in day headers; deferrals remain local.|Best at showing both chains and the deliberate loss of a high-I task.|**Pass — strongest**|
|**E — Dual-lens board**|Still understandable, but meetings/deferrals are repeated across both lenses and visual height grows quickly.|Dependency information appears twice or must be omitted from one lens.|**Pass with duplication penalty**|
|**C — Week strip + project arcs**|Very resilient and elegant.|Excellent project chain visibility; weaker at showing total composition of one particular day.|**Pass — strongest fallback**|

### Scenario B — meeting-heavy/compressed week

**Research stress inputs, not historical W34 facts:**

- Tuesday: compressed; fixed meetings 14:00–17:00.
    
- Wednesday: minimal; fixed meetings 10:00–16:00.
    
- Thursday: compressed; fixed website checkpoint at 13:00.
    
- Explicit deferrals must remain visible.
    

#### A — Project × Week matrix

|Project|**MON · START**STANDARD|**TUE · BUILD**COMPRESSED◐ meetings 14–17|**WED · CONSTRAINED**MINIMAL◐ meetings 10–16|**THU · REVIEW**COMPRESSED◐ website checkpoint 13:00|**FRI · BUFFER**STANDARD|
|---|---|---|---|---|---|
|**Leela**|Verify Home runtime (I90/R20/E95)|Verify bounded Skill Tree runtime (I88/R25/E92)|↘ defer — minimal capacity|Promote bounded cluster (I92/R45/E80)↳ Mon + Tue|ScopeSelection handoff (I86/R40/E78)|
|**MasterOfArts ★**|Locate website source (I92/R15/E85)|Reconcile purpose/audience (I94/R25/E80)|Define website IA (I90/R25/E78)|Define page requirements (I88/R30/E75)|Readiness review (I86/R20/E72)|
|**Apex**|Re-baseline ApexKB (I88/R20/E90)|Build benchmark (I84/R25/E85)|↘ defer — minimal capacity|Evaluate cheapest path (I78/R30/E80)|Evaluate alternatives/hybrid (I80/R35/E78)|
|**Investment**|Collect branch input (I82/R15/E60)|↘ defer — meetings|↘ defer — minimal capacity|Define selected branch contract (I76/R25/E68)|Configure/test selected branch (I72/R35/E70)|
|**Residual**|Recovery reserve|Recovery reserve|Recovery reserve|Recovery reserve|Overflow / recovery|

**Result:** no extra paragraph is required to understand why Wednesday contains less project work. The temporal deformation is encoded once, at the day boundary.

#### E — Dual-lens board

**Day lens**

|MON · Standard|TUE · Compressed|WED · Minimal|THU · Compressed|FRI · Standard|
|---|---|---|---|---|
|HomeWebsite sourceApexKB baselineInvestment input|Skill TreeWebsite purposeApex benchmarkInvestment deferred◐ 14–17 meetings|Website IALeela deferredApex deferredInvestment deferred◐ 10–16 meetings|Leela promotionWebsite requirementsApex upgrade pathInvestment contract◐ 13:00 checkpoint|Leela handoffWebsite reviewApex alternativesInvestment test|

**Project lens**

- **Leela:** Home → Skill Tree → _defer Wed_ → Promote → ScopeSelection
    
- **MasterOfArts:** Source → Purpose → IA → Requirements → Review
    
- **Apex:** Baseline → Benchmark → _defer Wed_ → Upgrade path → Alternatives
    
- **Investment:** Input → _defer Tue/Wed_ → Contract → Test
    

**Result:** understandable, but the deferrals and constrained days are now represented twice. The redundancy becomes obvious precisely when the week becomes interesting.

#### C — Week strip + project arcs

|**MON**|**TUE**|**WED**|**THU**|**FRI**|
|---|---|---|---|---|
|Start · Standard|Build · **Compressed**◐ meetings 14–17|Constrained · **Minimal**◐ meetings 10–16|Review · **Compressed**◐ checkpoint 13:00|Buffer · Standard|

**Leela**  
`Home (I90/R20/E95) → Skill Tree (I88/R25/E92) → ↘ defer → Promote cluster (I92/R45/E80) → ScopeSelection (I86/R40/E78)`

**MasterOfArts ★**  
`Source (I92/R15/E85) → Purpose (I94/R25/E80) → IA (I90/R25/E78) → Requirements (I88/R30/E75) → Review (I86/R20/E72)`

**Apex**  
`Baseline (I88/R20/E90) → Benchmark (I84/R25/E85) → ↘ defer → Upgrade path (I78/R30/E80) → Alternatives (I80/R35/E78)`

**Investment**  
`Input (I82/R15/E60) → ↘ defer → ↘ defer → Contract (I76/R25/E68) → Test (I72/R35/E70)`

**Result:** visually excellent and extremely robust, but answering “what exactly is Wednesday?” requires combining the header strip with four independent project lines.

---

### Scenario C — sequencing/dependency-driven week

**Research stress inputs, not historical W34 facts:**

- MasterOfArts website definition must be implementation-ready **Friday at 12:00**.
    
- Its verified task chain is sequential, so the deadline effectively forces one stage onto each weekday.
    
- Wednesday/Thursday have reduced deep-work capacity.
    
- `Promote bounded cluster to primary Skill Tree navigation (I92/R45/E80)` becomes dependency-clear after Monday/Tuesday but is **deliberately deferred despite its high impact**, because it has no fixed deadline and the website dependency chain has no recoverable slack.
    

This directly tests the locked rule that I/R/E informs judgment but does not override deadlines, dependencies, capacity or operator intent.

#### A — Project × Week matrix

|Project|**MON · START**STANDARD|**TUE · BUILD**STANDARD|**WED · BUILD**COMPRESSED|**THU · REVIEW**COMPRESSED|**FRI · BUFFER**◆ MoA due 12:00|
|---|---|---|---|---|---|
|**Leela**|Verify Home runtime (I90/R20/E95)|Verify Skill Tree runtime (I88/R25/E92)|↘ **defer Promote cluster (I92/R45/E80)** — deadline path wins|↘ defer — preserve integration capacity|↘ carry next week|
|**MasterOfArts ★**|Locate source (I92/R15/E85)|Reconcile purpose/audience (I94/R25/E80)|Define IA (I90/R25/E78)|Define page requirements (I88/R30/E75)|**◆ Review implementation readiness (I86/R20/E72) — due 12:00**|
|**Apex**|Re-baseline ApexKB (I88/R20/E90)|Build benchmark (I84/R25/E85)|Evaluate cheapest path (I78/R30/E80)|Evaluate alternatives/hybrid (I80/R35/E78)|Controlled comparison (I90/R40/E75)|
|**Investment**|Collect branch input (I82/R15/E60)|Define selected contract (I76/R25/E68)|↘ defer — compressed capacity|↘ defer — deadline protection|Continue selected branch after deadline|
|**Residual**|Recovery reserve|Recovery reserve|Recovery reserve|Recovery reserve|Overflow / recovery|

**Result:** this is the clearest stress-test win. A high-impact item is visibly losing for an intelligible reason; nothing about `(I92/...)` has to be reinterpreted into a synthetic priority score.

#### E — Dual-lens board

**Day lens**

|MON|TUE|WED|THU|FRI|
|---|---|---|---|---|
|HomeMoA sourceApex baselineInvestment input|Skill TreeMoA purposeApex benchmarkInvestment contract|**Leela promotion deferred**MoA IAApex upgrade path|**Leela deferred**MoA requirementsApex alternativesInvestment deferred|**◆ MoA review due 12:00**Apex comparisonLeela carry-forward|

**Project lens**

**Leela:** Home → Skill Tree → **↘ high-impact promotion deferred**  
**MasterOfArts:** Source → Purpose → IA → Requirements → **◆ Review 12:00 Fri**  
**Apex:** Baseline → Benchmark → Upgrade/alternatives → Comparison  
**Investment:** Input → Contract → defer → continue

**Result:** dependency logic remains clear, but the important Leela deferral and MoA deadline must again appear twice to preserve both lenses.

#### C — Week strip + project arcs

|**MON**|**TUE**|**WED**|**THU**|**FRI**|
|---|---|---|---|---|
|Start · Standard|Build · Standard|Build · Compressed|Review · Compressed|Buffer · **◆ MoA due 12:00**|

**Leela**  
`Home (I90/R20/E95) → Skill Tree (I88/R25/E92) → ↘ Promote cluster (I92/R45/E80) deferred — deadline path wins`

**MasterOfArts ★**  
`Source (I92/R15/E85) → Purpose (I94/R25/E80) → IA (I90/R25/E78) → Requirements (I88/R30/E75) → ◆ Review (I86/R20/E72)`

**Apex**  
`Baseline (I88/R20/E90) → Benchmark (I84/R25/E85) → Cheapest path (I78/R30/E80) → Alternatives (I80/R35/E78) → Comparison (I90/R40/E75)`

**Investment**  
`Input (I82/R15/E60) → Contract (I76/R25/E68) → ↘ defer → ↘ defer → continue`

**Result:** probably the most elegant dependency representation of the three. It loses only because the operator must mentally reconstruct each day's complete portfolio composition.

---

## 5. Comparison Matrix

### Phase-2 hard gating

|Candidate|Structure|Hard-filter result|
|---|---|---|
|**A**|Projects as rows × Mon–Fri columns|**QUALIFIES**|
|**B**|One horizontal agenda row per day|**QUALIFIES**|
|**C**|Five-day capacity strip + project arcs|**QUALIFIES**|
|**D**|Generic Flow 1–4 rows × Mon–Fri columns|**DISQUALIFIED** — visually implies intra-day slots/order and therefore trespasses on PrecapNextDay ownership|
|**E**|Calendar lens + duplicated project lens|**QUALIFIES**|

Candidate D is not merely weaker. The flow-lane positions would be interpreted as “first flow / second flow / third flow,” which turns weekly architecture into an execution sequence. The authoritative design explicitly reserves exact intra-day sequencing, flows, sprints and execution structure for `PrecapNextDay`.

### Weighted evaluation

Scores are **research judgments from the concrete renderings**, not empirical usability-test measurements.

|Candidate|10s Clarity 20%|Temporal 15%|Project Trace 15%|Density 15%|Visual / Planning 15%|Constraints 10%|Resilience 10%|**Weighted Total**|Primary Failure Mode|
|---|--:|--:|--:|--:|--:|--:|--:|--:|---|
|**A — Project × Week matrix**|5|5|5|4|4|5|4|**4.60 / 5 — 92%**|Can become wide/tall if cells are allowed to become mini project plans|
|**E — Dual-lens week board**|5|5|5|3|5|5|4|**4.60 / 5 — 92%**|Duplicates the plan and scales poorly under exceptions|
|**C — Week strip + project arcs**|4|4|5|4|4|4|5|**4.25 / 5 — 85%**|A day's complete portfolio requires cross-row reconstruction|
|**B — Day-agenda rows**|4|5|3|4|4|5|5|**4.20 / 5 — 84%**|Weakest answer to “what happens to Project X this week?”|
|**D — Flow-lane matrix**|—|—|—|—|—|—|—|**DQ**|Encodes ownership/sequence semantics the weekly layer does not own|

Calculations:

- **A:** `5×.20 + 5×.15 + 5×.15 + 4×.15 + 4×.15 + 5×.10 + 4×.10 = 4.60`
    
- **E:** `5×.20 + 5×.15 + 5×.15 + 3×.15 + 5×.15 + 5×.10 + 4×.10 = 4.60`
    
- **C:** `4×.20 + 4×.15 + 5×.15 + 4×.15 + 4×.15 + 4×.10 + 5×.10 = 4.25`
    
- **B:** `4×.20 + 5×.15 + 3×.15 + 4×.15 + 4×.15 + 5×.10 + 5×.10 = 4.20`
    

### Remaining common-baseline prototypes

#### B — Day-agenda rows

|Day|Shape|Actual work|
|---|---|---|
|**Monday · Start**|Standard|**Leela:** Verify Home runtime (I90/R20/E95)**MoA:** Locate website source (I92/R15/E85)**Apex:** Re-baseline ApexKB (I88/R20/E90)**Investment:** Collect operator inputs (I82/R15/E60)|
|**Tuesday · Build**|Standard|**Leela:** Verify Skill Tree (I88/R25/E92)**MoA:** Reconcile purpose/audience (I94/R25/E80)**Apex:** Build benchmark (I84/R25/E85)**Investment:** Define video contract (I76/R25/E68)|
|**Wednesday · Build**|Standard|**Leela:** Promote bounded cluster (I92/R45/E80)**MoA:** Define IA (I90/R25/E78)**Apex:** Evaluate cheapest path (I78/R30/E80)**Investment:** Collect alert conditions (I80/R20/E65)|
|**Thursday · Review**|Standard|**Leela:** ScopeSelection handoff (I86/R40/E78)**MoA:** Define page requirements (I88/R30/E75)**Apex:** Evaluate alternatives (I80/R35/E78)**Investment:** Collect feedback-process input (I78/R20/E65)|
|**Friday · Buffer**|Standard|**Leela:** Reconcile contexts (I82/R35/E76)**MoA:** Readiness review (I86/R20/E72)**Apex:** Controlled comparison (I90/R40/E75)**Investment:** Test video job (I72/R35/E70)|

**Verdict:** the best low-risk fallback, but project continuity is unnecessarily difficult to inspect.

#### C — Week strip + project arcs

|MON · Start|TUE · Build|WED · Build|THU · Review|FRI · Buffer|
|---|---|---|---|---|
|Standard|Standard|Standard|Standard|Standard|

**Leela:** Home (I90/R20/E95) → Skill Tree (I88/R25/E92) → Promote cluster (I92/R45/E80) → ScopeSelection (I86/R40/E78) → Context reconciliation (I82/R35/E76)

**MasterOfArts ★:** Source (I92/R15/E85) → Purpose/audience (I94/R25/E80) → IA (I90/R25/E78) → Page requirements (I88/R30/E75) → Readiness review (I86/R20/E72)

**Apex:** Baseline (I88/R20/E90) → Benchmark (I84/R25/E85) → Cheapest path (I78/R30/E80) → Alternatives (I80/R35/E78) → Comparison (I90/R40/E75)

**Investment:** Input (I82/R15/E60) → Video contract (I76/R25/E68) → Alert input (I80/R20/E65) → Feedback input (I78/R20/E65) → Video test (I72/R35/E70)

**Residual:** recovery / overflow reserve

**Verdict:** beautiful and resilient; best fallback when project continuity matters more than day composition.

---

## 6. External / Enhanced View Verdict

### Delivery-mode scores

Here **5 is always favorable**: for setup/maintenance/vendor dimensions, 5 means low burden or low risk.

|Mode|Incremental visual value|Setup|Source-of-truth safety|Maintenance|Vendor risk|Determinism|Open friction|Graceful fallback|**Total / 40**|
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
|**A — Markdown only**|2|5|5|5|5|5|5|5|**37**|
|**B — Markdown + generated static visual**|5|4|5|4|5|5|4|5|**37**|
|**C — Markdown + external planning product**|4|2|2|2|2|3|4|4|**23**|

### Decision

**Recommend Mode B, with Mode A as automatic fallback.**

The incremental renderer is worth having because this task explicitly optimizes visual design as well as functional comprehension. But it should remain a **projection, never an authority**.

### Recommended architecture

```text
Weekly_Command_Brief.md
        │
        │ canonical persisted plan
        ▼
extract "Week architecture" section
        │
        ├── calculate source_digest
        │
        ▼
deterministic renderer
        │
        ├── 2026-W34.svg
        └── 2026-W34.html
                │
                ▼
      optional GitHub Pages view

Weekly_Command_Brief.md
        └── "Open enhanced week view ↗"
```

GitHub supports relative links between repository files, automatically resolving them against the current branch, so a committed SVG can be linked without introducing another service. For a richer browser view, GitHub Pages can publish a static site automatically through Actions on changes to `main`.

### Source-of-truth rule

The renderer should **read the canonical Markdown section**. It should not read an independently edited calendar database.

Minimal generation logic:

```js
const brief = readFile(briefPath);
const weekSection = extractSection(brief, "Week architecture");

const sourceDigest = sha256(normalize(weekSection));
const model = parseWeekMatrix(weekSection);

writeFile(svgPath, renderWeekSvg(model, { sourceDigest }));
writeFile(htmlPath, renderWeekHtml(model, { sourceDigest }));
```

The generated file embeds:

```text
source: Weekly_Command_Brief.md
source_digest: <sha256>
generated_at: <timestamp>
editable: false
```

Validation:

```text
current Week architecture digest == projection digest
    -> link is current

digest mismatch
    -> regenerate projection
       OR suppress/stamp the enhanced-view link as stale

renderer unavailable
    -> do nothing to the Markdown Brief
```

This produces graceful failure: **the week's plan never disappears because the projection failed.**

### Why not make Linear/Sunsama/etc. the canonical enhanced view?

Linear's current Timeline is intentionally project-level: its documentation says individual issues are not displayed there. That directly conflicts with the hard requirement that real actionable work—not merely project names—remain visible.

Sunsama's timeboxing model explicitly places tasks onto a calendar at a desired time and duration, and can create corresponding external calendar events. That is a good pattern for `PrecapNextDay`, but too operationally precise for `PrecapWeek`.

So Mode C does not merely have synchronization cost; the strongest available products also encode the wrong planning ownership.

---

## 7. Evidence

### Repository evidence

**Authority:** `DESIGN-DECISIONS.md` explicitly freezes the runtime boundary, human information architecture, I/R/E notation, week/day ownership and downstream handoff. Weekly visualization alone remains unresolved.

**Current weakness:** the current Weekly Command Brief template still expresses day structure primarily as a prose `Daily seed map`, after separate project sections.

**Available semantics:** the PrecapWeek skill and blueprints already carry standard/compressed/minimal/overloaded capacity, weekday direction, dependencies, omissions and meeting deformation. A stronger visualization therefore does not require changing the planning architecture.

**Historical warning:** APEX's validated output-design work prioritizes first-10-seconds comprehension, progressive disclosure and human-first presentation, and earlier research identified schema/table-first output as a failure mode. That evidence argues against a giant dashboard, not against a single task-specific comparison matrix.

**Real W34 complexity:** W34 has four equal primary projects, a MasterOfArts website focus, one planned daily flow for each primary project, Residual as support/recovery, and calendar uncertainty.

**Real task dependencies:** the current project-state overview supplies the actual Leela, MasterOfArts website, ApexKB and Investment chains used in these prototypes.

**Historical contract:** the archived weekly output contract is explicitly superseded. Its useful historical contribution is the established concept of `weekday_plan_direction`; its fixed five-project roster and mandatory old `[priority/urgency/date]` scheme must not return.

### External evidence

**Tables as comparative surfaces:** GOV.UK recommends tables when users need to compare and scan information across rows and columns, while also advising reduction/splitting when tables contain too much data. That directly supports a deliberately bounded week matrix plus deeper detail below it.

**Resource × time is an established scheduling structure:** FullCalendar's current Timeline uses a horizontal time axis with resources as rows. This strongly validates the basic project-row/week-column orientation; APEX should borrow the topology without borrowing duration precision.

**Hourly calendars mean exact timing:** FullCalendar's TimeGrid explicitly represents days plus a vertical midnight-to-midnight time axis, and Sunsama's timeboxing schedules work at particular times and durations. Those patterns belong more naturally to downstream daily operationalization.  
**Compact indicators should remain exceptional:** Carbon's current status-indicator guidance says shapes/icons improve scanning in information-heavy layouts, but also recommends pairing visual indicators with labels and avoiding excessive indicator use or color-only semantics.

**Timeline dependency visuals are useful but date-dependent:** Linear shows blocking relationships visually on its timeline, but these relationships are tied to project start/end dates. APEX can borrow the conceptual `after / blocked by` notation without introducing fictitious dates.

## **GitHub-native enhancement options exist:** GitHub Markdown can render Mermaid diagrams, supports relative links, and GitHub Pages can automatically publish static generated views.

## 8. Exact Weekly Command Brief Visualization Spec

### Placement

The order should become:

```text
Result card
Operator decision
Weekly direction
WEEK ARCHITECTURE MATRIX   ← new primary visualization
Project detail
Cross-project exceptions / rationale
Review flags
Provenance
Compact downstream handoff
```

The matrix does **not** replace detailed project sections. It becomes their orientation layer.

### Grammar

|Element|Required grammar|
|---|---|
|Columns|`Project` + Monday + Tuesday + Wednesday + Thursday + Friday|
|Rows|One per active project; project order follows actual weekly planning logic, not an old fixed roster|
|Day header|`DAY · ROLE` plus capacity on a second line|
|Work cell|`Task or outcome (I94/R25/E9)`|
|Dependency|`↳ after <day/task>`|
|Deadline|`◆ due <day/time>`|
|Fixed meeting/capacity cause|`◐ <meeting/constraint>` preferably in day header|
|Deliberate deferral|`↘ defer — <short reason>`|
|Named weekly focus|`★ focus` beside the project name|
|No planned project movement|Compact reason, never disappearance|
|Unknown calendar|One week-level statement unless the uncertainty varies by day|

The symbols are secondary scanning aids; text remains authoritative. Do not make color carry meaning by itself. This follows current status-indicator guidance favoring symbol/shape plus text rather than color-only status.

### Cell-density rule

**Preferred:** one concise day-leading movement per project/day.

When several tightly related work items belong to the same day, group them into a meaningful outcome instead of reproducing a task backlog. This is a **presentation heuristic, not a hard task-count cap**. All consequential weekly work must still exist in the detailed project section below.

A matrix cell should not become a paragraph.

### Capacity representation

Use the existing canonical vocabulary in full:

- `STANDARD`
    
- `COMPRESSED`
    
- `MINIMAL`
    
- `OVERLOADED`
    

Do not replace these with unexplained colored dots.

A material cause may appear immediately underneath:

```text
COMPRESSED
◐ meetings 14:00–17:00
```

### Deadline representation

```text
◆ Review implementation readiness (I86/R20/E72)
  due Fri 12:00
```

or, when the deadline shapes the entire day:

```text
FRI · BUFFER
STANDARD
◆ MoA due 12:00
```

### Dependency representation

Prefer local one-hop cues:

```text
Promote bounded cluster (I92/R45/E80)
↳ after Mon + Tue
```

Do **not** draw arrows across Markdown cells.

If a chain needs more explanation, put one compact sentence directly below the matrix.

### Deferral representation

A deliberate non-allocation is a real planning decision:

```text
↘ defer Promote bounded cluster (I92/R45/E80)
— website deadline path wins
```

Do not use a blank cell when the absence is intentional and material.

### Meetings

Meetings belong in the **day header** when they affect the whole day's capacity:

```text
WED · CONSTRAINED
MINIMAL
◐ meetings 10:00–16:00
```

Do not expand the matrix into a full hourly agenda.

### What belongs below the matrix

Only consequence-bearing context:

```text
Week exceptions
- Website definition must complete by Friday 12:00.
- Wednesday is minimal because fixed meetings consume most deep-work capacity.
- Leela promotion is deliberately deferred despite I92 because the deadline chain has no slack.
- Calendar source is stale/unavailable; PrecapNextDay must revalidate.
```

### What must never appear inside the matrix

- sprint counts;
    
- Flow Execution Cards;
    
- prompts;
    
- exact execution sequence;
    
- exact start/end times for discretionary project work;
    
- separate I / R / E columns;
    
- combined priority scores;
    
- full provenance;
    
- raw source lists;
    
- generic blueprint mechanics;
    
- validation traces;
    
- owner/executor boilerplate unless genuinely necessary to understand allocation;
    
- a resurrected fixed five-project roster.
    

### Production-ready Markdown template

```markdown
## Week architecture

> **Week shape:** {{ONE_LINE_TEMPORAL_SUMMARY}}
> **Named focus:** {{FOCUS_PROJECT_OR_NONE}}
> **Fixed constraints:** {{ONLY_MATERIAL_WEEK_LEVEL_CONSTRAINTS_OR_NONE}}

| Project | **MON · {{MON_ROLE}}**<br>{{MON_CAPACITY}}<br>{{MON_FIXED_CONSTRAINT_IF_MATERIAL}} | **TUE · {{TUE_ROLE}}**<br>{{TUE_CAPACITY}}<br>{{TUE_FIXED_CONSTRAINT_IF_MATERIAL}} | **WED · {{WED_ROLE}}**<br>{{WED_CAPACITY}}<br>{{WED_FIXED_CONSTRAINT_IF_MATERIAL}} | **THU · {{THU_ROLE}}**<br>{{THU_CAPACITY}}<br>{{THU_FIXED_CONSTRAINT_IF_MATERIAL}} | **FRI · {{FRI_ROLE}}**<br>{{FRI_CAPACITY}}<br>{{FRI_FIXED_CONSTRAINT_IF_MATERIAL}} |
|---|---|---|---|---|---|
| **{{PROJECT_NAME}}{{FOCUS_MARKER}}** | {{MON_WORK_OR_DEFERRAL}} | {{TUE_WORK_OR_DEFERRAL}} | {{WED_WORK_OR_DEFERRAL}} | {{THU_WORK_OR_DEFERRAL}} | {{FRI_WORK_OR_DEFERRAL}} |
| {{REPEAT_FOR_EACH_ACTIVE_PROJECT}} | ... | ... | ... | ... | ... |

**Week exceptions:** {{ONLY_CONSEQUENTIAL_SEQUENCE_DEADLINE_CAPACITY_OR_DEFERRAL_RATIONALE}}

**Calendar confidence:** {{CALENDAR_SOURCE_STATUS_AND_ONLY_MATERIAL_FRESHNESS_NOTE}}

{{OPTIONAL_ENHANCED_VIEW_LINK}}
```

This is a presentation grammar only. The existing project-detail sections remain underneath and continue to carry weekly target, success evidence, actionable work, dependencies/blockers/decisions and expected outputs.

---

## 9. Reuse / Import Options

|Option|Reuse value|Decision|
|---|---|---|
|**FullCalendar Resource Timeline**|Best external structural analogue: resources as rows, time horizontally; current docs are v7.0.2.|**Borrow the pattern, not the dependency initially.** Timeline is Premium and still assumes time-axis/event semantics.|
|**FullCalendar TimeGrid / conventional week calendar**|Strong exact-time scheduling UI.|**Reject for Module 01 primary view.** It encodes hourly precision owned downstream.|
|**Mermaid Gantt**|Supports milestones, date markers, compact mode and dates; GitHub renders Mermaid natively.|**Conditional secondary view only.** Gantt bars imply duration and start/end dates that many APEX weekly movements do not have.|
|**Markwhen**|Markdown-ish source can render timeline/calendar views; components can be self-hosted and its project explicitly points to separate open-source timeline/calendar components.|**Promising experimental projection, not v1 default.** It creates another markup model and is more timeline-oriented than the recommended matrix.|
|**Linear Timeline**|Excellent high-level project/dependency pattern.|**Reject as external canonical host.** Individual issues are intentionally excluded from Timeline.|
|**GitHub Pages + Actions**|Existing repository infrastructure can host a static derived projection and update it automatically.|**Recommended host for Mode B if browser-quality rendering is wanted.**|
|**GOV.UK / Carbon patterns**|Strong guidance for comparative table structure, headers and restrained status encoding.|**Adopt the design principles.**|

### Reuse conclusion

No reviewed component cleanly implements the required semantics without bringing along **hour-level scheduling, duration bars, project-only granularity, or another editable source of truth**.

Therefore a small deterministic HTML/SVG renderer is justified. It is not a new planning framework; it is simply a visual projection of the Markdown matrix.

---

## 10. Failure Modes

### 1. Too many active projects

At roughly 8–10 active project rows, the matrix becomes significantly taller.

**Mitigation:** keep all projects visible but use compact deferred/maintenance rows. Do not delete low-activity projects.

### 2. Cells accumulate task backlogs

The recommendation fails if every cell becomes a mini project section.

**Mitigation:** show the day-leading outcome and material exceptions; preserve full work beneath the matrix. GOV.UK similarly recommends reducing or restructuring tables when too much data accumulates.

### 3. Long task names cause vertical explosion

**Mitigation:** use a faithful concise outcome label in the matrix and retain the full task wording/project evidence below. Never shorten away the substantive action.

### 4. Too many dependency markers create visual noise

**Mitigation:** only annotate dependencies that explain placement. Straightforward chains can be inferred from adjacent cells; explain non-obvious dependencies explicitly.

### 5. Symbols become a second language

**Mitigation:** restrict the vocabulary to approximately four exception markers and pair them with words. Carbon specifically cautions against excessive indicators and against using color alone.

### 6. The weekly view drifts into a daily scheduler

The biggest architectural failure would be adding exact discretionary time slots or row ordering that implies execution sequence.

**Mitigation:** fixed meeting/deadline times may be shown because they constrain the week; discretionary work remains day-level direction. PrecapNextDay retains exact sequencing.

### 7. Enhanced projection becomes stale

**Mitigation:** projection is generated read-only from the Markdown week section and carries its digest. A digest mismatch invalidates the projection. The Markdown itself remains usable.

### 8. External view becomes independently editable

**Mitigation:** never import changes back from the enhanced projection. Edits happen through the canonical Weekly Command Brief generation/approval path only.

### 9. Calendar uncertainty gets repeated everywhere

W34 currently has one global calendar-source uncertainty.

**Mitigation:** state it once below the matrix. Only put a capacity warning in individual day headers when that day's condition actually differs.

### 10. Color becomes semantic authority

**Mitigation:** Markdown requires no color. The enhanced view may use subtle color for visual grouping, but capacity/deadline/deferral meaning must remain legible through text and shape/symbol encoding.

---

## 11. Open Questions

There is **no remaining semantic question** required to select the primary layout: the project × weekday matrix fits the locked PrecapWeek/PrecapNextDay boundary without changing it.

One optional operator decision remains:

**A1 — Enhanced projection timing**

- **A1.1 — Recommended:** implement the Markdown matrix **and** the read-only generated HTML/SVG projection in the same Module 01 implementation pass.
    
- **A1.2 — Lower-complexity alternative:** implement the Markdown matrix first and leave the enhanced renderer for a later iteration.
    

This decision does not affect the canonical Brief grammar or any ownership boundary.

---

## 12. Implementation Handoff

No repository state was modified during this research.

For the later implementation AI:

1. **Record the accepted visualization decision** in `apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/DESIGN-DECISIONS.md`; do not reopen already validated Module 01 semantics.
    
2. **Update** `.claude/skills/PrecapWeek/weekly-command-brief-template.md`:
    
    - replace the prose-first `Daily seed map` as the primary week visualization with `## Week architecture`;
        
    - insert the project × Monday–Friday matrix grammar above;
        
    - retain project sections underneath;
        
    - preserve one compact downstream handoff;
        
    - point the downstream handoff to the `Week architecture` section rather than duplicating it.
        
3. **Update** `.claude/skills/PrecapWeek/SKILL.md` only as needed to specify matrix generation and validation. Do **not** alter weekly/daily ownership.
    
4. **Update** `.claude/skills/PrecapWeek/references/validation-checklist.md` with explicit checks:
    
    - all Monday–Friday columns present;
        
    - every active project visible;
        
    - actual work or explicit deferral present;
        
    - `Task (I#/R#/E#)` syntax valid;
        
    - capacity shape present for every day;
        
    - deadline/dependency/capacity exceptions visible when consequential;
        
    - no exact discretionary intra-day sequence;
        
    - no duplicate full machine representation.
        
5. **Use three regression fixtures**:
    
    - real W34-derived normal week;
        
    - meeting-heavy/compressed Scenario B;
        
    - dependency/deadline Scenario C.  
        The matrix must remain readable in all three before acceptance.
        
6. **Do not alter** the archived `weekly-plan-output-contract.md`. It is historical evidence only.
    
7. If **A1.1 / enhanced projection** is selected:
    
    - add one deterministic read-only renderer;
        
    - parse the canonical `Week architecture` Markdown;
        
    - produce static SVG/HTML;
        
    - embed the source digest;
        
    - add a one-line `Open enhanced week view ↗` link;
        
    - optionally publish the HTML through GitHub Pages;
        
    - never permit the projection to become independently editable;
        
    - never make projection generation a prerequisite for a usable Markdown Brief.
        
8. **Do not introduce** FullCalendar, Linear, Sunsama, Markwhen, Mermaid Gantt or another planning product merely because it renders prettier output. Import one only if a later test identifies a capability the static matrix projection genuinely cannot provide.
    

### Final ranked verdict

|Rank|Candidate|Score|Definitive verdict|
|--:|---|--:|---|
|**1**|**Annotated Project × Week matrix**|**4.60**|**Use this as the canonical weekly architecture view.**|
|**2**|Dual-lens week board|**4.60**|Beautiful but loses because its second lens duplicates the plan and degrades under exceptions.|
|**3**|Week strip + project arcs|**4.25**|Excellent resilient fallback; weaker for understanding one day across the portfolio.|
|**4**|Day-agenda rows|**4.20**|Operationally robust but weak for weekly project traceability.|
|**DQ**|Flow-lane calendar|—|Reject because it silently takes ownership of intra-day sequence from PrecapNextDay.|

**Decision recommendation:** **Candidate A + Delivery Mode B**, with the Markdown matrix remaining complete and authoritative and the enhanced static view remaining disposable. This is the format most likely to satisfy the “every Sunday” criterion without turning the Brief into either an ugly schema table or an over-engineered calendar application.