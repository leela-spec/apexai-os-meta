# Master of Arts Example Fragments

> **ILLUSTRATIVE ONLY — NOT CURRENT PROJECT TRUTH.** The fragments below use fictional dates, identifiers, decisions, paths, and execution results to demonstrate template use. They draw only on the work patterns in the Master of Arts workflow example database. They do **not** adopt that source's older Hermes profile, Kanban, cron, or orchestration architecture.

These are deliberately partial examples. Each section shows the part of a template that is easiest to misunderstand or most important to complete correctly.

## Source workflow legend

- **W03:** Master of Arts Project-to-Execution Matrix
- **W04:** Raw Idea to Idea Database Entry
- **W05:** Raw Concept to Workshop Outline Pipeline
- **W06:** Workshop Architecture Slide Compression
- **W07:** Embodied Technique to Drill Protocol
- **W08:** Sequencing Coaching Format to Leela Use Case
- **W09:** Legal and Organizational Self-Employment Setup Board
- **W10:** Specialized Agent Handover Packet Creation

---

## J01 Project State Success Card

**Demonstrates:** a planning-safe project snapshot without turning the card into the full project database.

> **Planning readiness:** USABLE_FOR_WEEKLY_PLANNING  
> **Outcome:** Master of Arts has one accepted near-term focus: turn the selected raw concept into a reviewable workshop outline before compressing it into slides. The legal setup board remains separate and cannot supply assumptions about workshop content.  
> **Next action:** USE_AS_CONTEXT  
> **Review needed:** Confirm whether the workshop is designed for a 90-minute or 120-minute delivery window.  
> **Warning:** Duration is unresolved and affects exercise count and pacing.

### Project — MasterOfArts

**Current phase:** Workshop architecture development  
**Current goal:** Produce a complete first workshop outline from the selected concept  
**Planning status:** USABLE  
**Accepted priorities:**

- Complete the workshop outline before slide compression.
- Preserve source-concept traceability through the outline.

**Next-action candidates:**

- Run the W05 concept-to-workshop-outline flow.
- Defer W06 slide compression until the outline has passed content review.

**Stale or conflicting information:** Delivery duration is stated as both 90 and 120 minutes in two notes.  
**Important artifact reference:** `examples/fictional-sources/workshop-concept-note.md`

---

## J02 Weekly Command Brief

**Demonstrates:** one project section that expresses weekly outcomes and planned work without freezing a daily execution plan.

### Project — MasterOfArts

**Weekly target:** Move one workshop concept from raw source material to a validated outline and prepare the strongest segment for later slide compression.  
**Why this week:** The workshop outline is the dependency for both facilitation rehearsal and W06 slide work.  
**Success evidence:** A reviewed outline names the audience, promise, sequence, exercise blocks, timing assumptions, and unresolved choices.

#### Priorities and desired results

1. **W05 outline creation** — A complete first workshop architecture exists and is reviewable.
2. **W07 drill translation** — One embodied technique is converted into a safe, teachable drill protocol.
3. **W06 preparation** — Slide-compression inputs are identified, but slide production does not begin until the outline is approved.

#### Planned work

- **Work item:** Draft the workshop architecture from the selected concept.
  - Expected output: `examples/fictional-outputs/workshop-outline-v1.md`
  - Dependency: Resolve or explicitly bracket the duration conflict.
  - Candidate day: Tuesday
- **Work item:** Review exercise safety and facilitation constraints.
  - Expected output: review notes attached to the outline
  - Dependency: First outline draft
  - Candidate day: Thursday

#### Decision needed

- Choose the duration assumption that daily planning should use, or authorize a duration-neutral first draft.

---

## J03 PreCap Next Day Brief

**Demonstrates:** compact three-sprint flow summaries that link to J4 instead of repeating full tasks, inputs, prompts, dependencies, and completion criteria.

> **Day state:** READY_WITH_REVIEW  
> **Day direction:** Advance the Master of Arts workshop from concept to a reviewable outline, then capture one drill protocol and organize one raw idea for later use. Do not start slide compression until the outline structure is stable.  
> **Next action:** OPEN_FIRST_FLOW_CARD  
> **Review needed:** Use a duration-neutral outline unless the operator selects 90 or 120 minutes before S1.  
> **Plan size:** 3 flows; 9 visible sprints

### Flow 1 — Raw Concept to Workshop Outline

**Flow ID:** `F2-W05`  
**Project:** MasterOfArts  
**Status:** PLANNED  
**Why today:** This is the dependency for slide compression and facilitation rehearsal.  
**Expected flow output:** Reviewable workshop-outline draft  
**Open full workspace:** [Open Flow Execution Card](../templates/J04-flow-execution-card.md) — `flows/2026-07-14/F2-W05-flow-execution-card.md`

- **S1 — Frame:** Extract audience, promise, source concepts, and design constraints → workshop design brief.
- **S2 — Architect:** Build the sequence, modules, exercises, and pacing logic → outline draft.
- **S3 — Capture:** Record decisions, gaps, evidence, and handoff notes → FlowRecap-ready evidence.

### Flow 2 — Embodied Technique to Drill Protocol

- **S1 — Extract:** Identify the technique's observable mechanism → mechanism note.
- **S2 — Translate:** Turn the mechanism into a bounded participant drill → protocol draft.
- **S3 — Safeguard:** Capture contraindications, facilitation cautions, and review needs → evidence handoff.

### Flow 3 — Raw Idea to Idea Database Entry

- **S1 — Clarify:** Separate the core idea from supporting observations → normalized idea statement.
- **S2 — Structure:** Add use cases, links, and open questions → database-ready entry.
- **S3 — Capture:** Record provenance and next-review cue → handoff note.

### Cross-flow execution order

1. `F2-W05 / S1–S2` — establishes the workshop architecture.
2. `F2-W07 / S1–S2` — supplies one exercise candidate for outline review.
3. `F2-W05 / S3`, then remaining S3 capture work — consolidates evidence after content work.

---

## J04 Flow Execution Card

**Demonstrates:** one complete sprint block. J4 owns execution depth; the related J3 entry remains a summary.

### S2 — Architect the workshop sequence

> **Sprint state:** READY_WITH_REVIEW  
> **Goal:** Convert the approved design brief into a coherent workshop sequence with modules, exercises, timing ranges, and transitions.  
> **Start or resume here:** Draft the module order before estimating exact minutes.  
> **Expected output:** `examples/fictional-outputs/workshop-outline-v1.md`  
> **Review trigger:** Stop if the duration choice changes the number of required modules rather than only their timing.

#### Tasks

- [ ] Define the opening state, promised participant shift, and closing evidence of learning.
- [ ] Arrange source concepts into three to five teachable modules.
- [ ] Place the W07 drill where it supports, rather than interrupts, the learning arc.
- [ ] Add timing ranges and transition intent without claiming a final run-of-show.
- [ ] Mark every unresolved content or safety choice for operator review.

#### Inputs

- `examples/fictional-sources/workshop-design-brief.md`
- `examples/fictional-sources/selected-concept-notes.md`
- `examples/fictional-sources/W07-drill-protocol-draft.md`

#### Dependencies

- S1 design brief is complete.
- Duration is either selected or explicitly handled as a range.
- The W07 drill remains provisional until safety review.

#### Prompt access

- [Open S2 architecture prompt](examples/fictional-prompts/F2-W05-S2-architecture.md) — `examples/fictional-prompts/F2-W05-S2-architecture.md`
- Routing context: `examples/fictional-routing/F2-W05-S2-route.md`

#### Expected outputs

- A complete workshop-outline draft.
- A visible list of timing, safety, and source-traceability questions.

#### Done when

- Every module has a purpose, participant action, expected learning evidence, and transition.
- The complete workshop promise can be traced through the module sequence.
- Unresolved decisions are named rather than silently settled.

#### Stop or review when

- The source material supports two materially different workshop promises.
- A proposed exercise creates a safety or professional-scope concern.
- A duration choice would require removing an accepted learning outcome.

#### Capture during this sprint

- Decisions made about module order.
- Artifacts created or changed.
- Constraints that changed the design.
- Actual route used, when known.

---

## J05 Prompt Files and Index

**Demonstrates:** a direct prompt-file entry and a simple prompt file. The entry does not repeat the J4 work plan.

### Prompt index entry

- **Sprint:** `S1`
- **Prompt:** [Compress workshop architecture into a slide narrative](examples/fictional-prompts/F2-W06-S1-slide-compression.md)
- **Visible path:** `examples/fictional-prompts/F2-W06-S1-slide-compression.md`
- **Recommended surface:** `long_context_surface`
- **Routing reference:** `examples/fictional-routing/F2-W06-S1-route.md`
- **Use when:** A reviewed workshop outline exists and the operator needs a first slide-story structure.
- **Availability:** READY
- **Degraded warning:** none

### Prompt file fragment

```markdown
# Workshop Architecture Slide Compression

**Recommended surface:** `long_context_surface`  
**Use when:** The source outline has passed content review.  
**Expected return:** A slide-by-slide narrative map, not finished visual design.

## Prompt

Using the supplied workshop outline as the sole content authority, create a concise slide narrative that preserves the workshop promise, module sequence, participant actions, and essential transitions.

Return:
1. a one-sentence narrative arc;
2. a slide sequence with one job per slide;
3. speaker-intent notes only where the slide cannot stand alone;
4. a list of content omitted or compressed;
5. review flags for any source ambiguity.

Do not invent research claims, participant outcomes, timing, or visual assets. Distinguish source-backed content from proposed compression choices.
```

---

## J06 Execution Evidence Handoff

**Demonstrates:** an evidence item that records what exists without deciding what it means for project state.

> **Evidence state:** READY_FOR_FLOWRECAP  
> **Outcome:** The W07 flow produced a drill-protocol draft and a separate safety-review list. Execution evidence is compact and source-linked; no normalization beyond labeling is needed.  
> **Next action:** SEND_TO_FLOWRECAP  
> **Review needed:** none

### Evidence item — W07 drill protocol draft

- **What was planned:** Translate one embodied technique into a participant-ready drill protocol.
- **What actually happened:** A four-step drill was drafted; facilitator language and debrief questions were added; contraindication review remains open.
- **Output:** `examples/fictional-outputs/W07-drill-protocol-v1.md`
- **Decision recorded:** Keep the drill experiential and avoid diagnostic or therapeutic framing.
- **Blocker or failure:** No clinical or legal review was performed.
- **Unresolved question:** Which participant conditions require an explicit opt-out instruction?
- **Source references:** operator notes, prompt output, and the draft file listed above.
- **Evidence reliability:** medium; output exists, but the safety review is incomplete.

**Interpretation boundary:** This handoff does not claim that the protocol is approved, safe for all contexts, or ready for project-state acceptance.

---

## J06a Skip Marker

**Demonstrates:** the smallest useful record for a planned but unexecuted flow.

> **Skipped:** `F2-W09` — Legal and Organizational Self-Employment Setup Board  
> **Reason:** The jurisdiction and required professional-advice boundary were not available; no reliable setup recommendation could be produced.  
> **Handling:** Wait for dependency, then return to weekly review. Partial work did not occur, so a full evidence handoff is unnecessary.

```yaml
skipped_flow_marker:
  marker_id: "skipped_flow_marker_2026-07-14_F2-W09_dependency"
  artifact_name: "skipped_flow_marker"
  execution_day: "2026-07-14"
  flow_id: "F2-W09"
  source_flow_packet_ref:
    flow_packet_path_or_label: "examples/fictional-flows/F2-W09-flow-packet.md"
    source_status: "available"
  skip_reason: "Jurisdiction and professional-advice boundary were unavailable."
  skip_type: "dependency_missing"
  impact_on_plan:
    impact_level: "medium"
    impact_summary: "The setup-board output is deferred; workshop content work can continue."
  recommended_next_handling:
    handling_type: "convert_to_blocker_review"
    recommendation: "Resolve jurisdiction and advice boundary before replanning the flow."
    recommended_owner: "operator"
  validation_status: "valid"
```

---

## J07 FlowRecap Result Card

**Demonstrates:** interpretation of evidence plus a candidate state change that remains explicitly unaccepted.

> **Flow result:** COMPLETED_WITH_REVIEW  
> **What changed:** The W05 flow produced a complete first workshop-outline draft with a coherent sequence and a visible decision register. Duration and one exercise-safety issue remain unresolved.  
> **Next action:** APPROVE_CANDIDATE_FOR_DOWNSTREAM_REVIEW  
> **Review needed:** Decide whether “first outline complete” is an acceptable project-status change despite the two open review items.  
> **Candidate warning:** No project status or KB record has been updated.

### Planned versus actual

- **Planned:** Produce a reviewable first workshop architecture.
- **Actual:** Produced the outline and module sequence; final timing and exercise approval remain open.
- **Variance:** Completion is content-complete but not delivery-ready.

### Candidate project-state change — candidate only

- **Candidate:** `MasterOfArts / Workshop architecture / First outline draft complete`
- **Proposed value:** `complete_with_review_items`
- **Evidence:** `examples/fictional-outputs/workshop-outline-v1.md`
- **Confidence:** high for draft completion; medium for delivery readiness.
- **Downstream status:** ready for J9 review.

### Proposed next step — not a next-day plan

Review timing and safety questions, then decide whether to proceed to W06 slide compression.

---

## J08 Usage Learning Card

**Demonstrates:** lightweight planned-versus-actual learning without turning one execution into a general model benchmark.

> **Learning result:** MEANINGFUL_LEARNING  
> **Planned versus actual:** The W06 compression task was planned for a `long_context_surface`; the operator instead used a `subscription_frontier_reasoning` surface because the outline contained unresolved structural choices.  
> **Learning signal:** `use_only_for_high_value_tasks`  
> **Future routing hint:** Use stronger reasoning for slide compression only when source ambiguity or consequential omission choices remain; otherwise prefer the lighter long-context route.  
> **Operator action:** ACCEPT_USAGE_LEARNING

### Evidence-bound observation

- **Comparable task:** Compressing a reviewed-but-not-fully-settled workshop outline into a narrative map.
- **Outcome quality:** useful; the output exposed two hidden sequence conflicts.
- **Operator friction:** low.
- **Evidence gap:** No exact token, cost, quota, or model label was recorded.
- **Confidence:** medium.

This signal advises J12. It does not automatically replace a route.

---

## J09 Status Merge Decision Card

**Demonstrates:** an operator merge decision that does not claim a durable write.

> **Merge review state:** APPROVED_AWAITING_WRITE  
> **Decision summary:** Approve the edited W05 candidate as “first workshop-outline draft complete; delivery readiness pending timing and safety review.”  
> **Next action:** SEND_APPROVED_CHANGE_TO_J10  
> **Review needed:** none  
> **Durable status:** Approved, but no project KB write is yet confirmed.

### Candidate decision

- **Candidate reference:** `examples/fictional-recaps/W05-flow-recap.md#candidate-project-state-change`
- **Conflict found:** The original candidate said “workshop outline complete,” which could imply delivery readiness.
- **Operator decision:** EDIT_AND_APPROVE
- **Approved value:** `first_outline_draft_complete_with_delivery_review_pending`
- **Required provenance:** W05 recap and workshop-outline-v1 artifact references.
- **Destination:** MasterOfArts project record through project-kb-manager.

### Durable write confirmation

- **State:** AWAITING_J10
- **J10 result:** none yet
- **Confirmed effective value:** not confirmed

---

## J10 Project KB Update Card

**Demonstrates:** a confirmed durable result, including the write evidence needed before J11 can use the value as truth.

> **Durable write state:** CONFIRMED_WRITTEN  
> **Result:** The accepted W04 idea entry was appended to the fictional Master of Arts project record, the registry reference was synchronized, and the stored value was read back successfully.  
> **Next action:** SEND_CONFIRMED_RESULT_TO_J11  
> **Review needed:** none  
> **Write evidence:** `examples/fictional-write-results/W04-kb-update-result.yaml`

### Actual durable result

- **Target:** `examples/fictional-kb/projects/master-of-arts.md`
- **Change type:** append new idea-database reference and next-review cue.
- **Write attempt:** succeeded.
- **Read-back verification:** succeeded.
- **Registry synchronization:** succeeded.
- **Effective stored value:** `Idea entry “Workshop threshold moments” added; review in next concept-selection pass.`
- **Durable result reference:** `examples/fictional-write-results/W04-kb-update-result.yaml`
- **Freshness:** `2026-07-14T17:20:00+02:00`

### J11 readiness

**Ready for Project Status Overview:** YES  
**Confirmed result reference:** `examples/fictional-write-results/W04-kb-update-result.yaml`  
**Residual review flag:** none

---

## J11 Project Status Overview

**Demonstrates:** a compact confirmed project entry and ranked task view. It excludes the unconfirmed W05 candidate until J10 confirms that write.

### Project — MasterOfArts

**Accepted status:** active  
**Current phase or goal:** Develop the workshop architecture and validated facilitation materials.  
**Current priority:** Complete delivery-readiness review for the first outline.  
**Next confirmed task:** Resolve timing and exercise-safety review.  
**Blocker:** Professional-scope review for the W09 setup board is not yet available.  
**Freshness:** 2026-07-14  
**Durable source:** `examples/fictional-write-results/W04-kb-update-result.yaml`

#### Tasks

1. **Workshop outline review** `[88/82/16-07]`
   - Status: active
   - Next action: decide duration and approve or replace the provisional drill.
   - Subtasks:
     - Timing decision `[85/90/16-07]`
     - Drill safety review `[92/86/16-07]`
2. **Slide narrative preparation** `[72/55/NA]`
   - Status: blocked by outline review
   - Next action: open W06 only after the outline review closes.

### Ranked task fragment

| Rank | Task and project | Rating | Confirmed next action |
|---|---|---|---|
| 1 | Drill safety review — MasterOfArts | `[92/86/16-07]` | Obtain the required review or replace the drill. |
| 2 | Timing decision — MasterOfArts | `[85/90/16-07]` | Select 90 minutes, 120 minutes, or an approved range. |

---

## J12 AI Routing Card

**Demonstrates:** an advisory route recommendation and a separate operator decision state.

> **Routing state:** RECOMMENDATION_READY  
> **Recommended route:** `subscription_frontier_reasoning`  
> **Next action:** APPROVE_ROUTE  
> **Review needed:** Confirm whether the handover packet includes repository inspection or only source synthesis.  
> **Confidence:** medium; task scope is clear, tool-access need is not.

### Task context

**Flow:** W10 — Specialized Agent Handover Packet Creation  
**Desired output:** A bounded, evidence-linked handover packet another capable AI can use without reconstructing the source set.  
**Risk:** medium; poor boundary wording could cause downstream scope drift.  
**Constraint:** Do not create or execute an agent. Produce the handover artifact only.

### Advisory recommendation

- **Stable surface class:** `subscription_frontier_reasoning`
- **Why it fits:** The task requires reconciling multiple source documents, preserving ownership boundaries, and writing a compact reusable artifact.
- **Fallback:** `long_context_surface` when the source set is stable and no repository inspection is required.
- **Do not use when:** The task requires repository navigation, file generation, or validation across many files; route that bounded work to an appropriate code/tool surface after separate approval.

### Operator route decision

- **Decision:** PENDING
- **Approved route:** none
- **Execution authorization:** not granted

Until the operator records a decision, this recommendation must not be passed to J4 or J5 as an approved execution route.
