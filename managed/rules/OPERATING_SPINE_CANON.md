# OPERATING_SPINE_CANON

## Purpose and authority position

This file defines the top-level operating law for the living OpenClaw system.

It is the authoritative runtime spine for how work moves across project control, sessions, truth change, hygiene, and escalation. It exists because no README, ritual, compact governance anchor, or companion document is a truthful host for this law.

This canon governs the operating center, authority posture, lane structure, and session-to-night continuity of the system. It does not replace the detailed field rules, packet schemas, routing mechanics, or ritual procedures defined in subordinate managed files.

## Scope and non-scope

This file covers:

- the system-wide operating posture
    
- the governing order between operating spine, project control, truth change, and file production
    
- the canonical authority chain between reasoning, accepted truth, and live state
    
- the four nested operating loops
    
- the two orthogonal lane splits
    
- the canonical cold-start, session, and night cycle
    
- the top-level role of project interface control surfaces
    
- the rule that escalation and hygiene are first-class architecture, not optional cleanup
    

This file does not cover:

- per-surface schemas or field definitions
    
- detailed role, delegation, handoff, or specialist-permission law
    
- detailed escalation trigger routing or hold-state taxonomy
    
- detailed promotion packet schema or approval choreography
    
- detailed session-export or night-planning ritual mechanics
    
- implementation choreography, tool-specific behavior, or config-schema behavior
    

## Core operating laws

- Operate from the living system, not from blueprint literalism.
    
- Keep the v0 runtime shell and treat compatibility as the default posture.
    
- Keep the center of gravity on the operating spine rather than on file production.
    
- Govern in this order: operating spine -> project interface control -> knowledge promotion -> file production.
    
- Work sequentially by default. Broader overlap is exceptional, bounded, and validation-gated.
    
- Start from explicit control surfaces before deep traversal.
    
- Use research before ambiguous execution, evidence before truth change, and truth before state propagation.
    
- Keep reasoning/evidence surfaces, accepted truth, and live operational state distinct. None silently substitutes for another.
    
- The authority chain is `BePr_SSOT -> SSOT -> OpState`.
    
- No accepted-truth change is valid without the promotion path.
    
- Session trace is required for material work.
    
- Night planning is the principal synthesis cycle for cross-session continuity.
    
- QA/Hygiene is a co-equal control lane and may block progress work.
    
- Escalation is first-class architecture; unsafe continuation is never the default.
    
- Operator-facing and cloud/background execution may inform one another but may not collapse into one undifferentiated stream.
    
- Docs may explain, exemplify, freeze, or reconcile, but they may not be the sole runtime authority for load-bearing behavior.
    
- File production is subordinate manufacturing work. It may be required by the operating spine, but it must not become the master process of the system.
    

## Canonical operating cycle

### Operating center

The operating spine runs through four nested loops:

1. **Meta orchestration loop:** prioritizes across projects, preserves lane separation, sequences work, and produces next-cycle plans.
    
2. **Project control loop:** moves a bounded project or system surface through active work, blockage, review, hold, and escalation.
    
3. **Knowledge governance loop:** converts evidence and reasoning into accepted truth through governed promotion.
    
4. **File production loop:** creates or revises governed artifacts only when required by the loops above.
    

Each lower loop serves the stability and throughput of the loop above it. No lower loop may silently redefine the authority of a higher loop.

### Lane model

The operating spine preserves two orthogonal splits:

**Execution split**

- **Operator lane:** interactive, session-facing, bounded-context execution.
    
- **Cloud lane:** background, scheduled, verification, aggregation, hygiene, and other low-risk execution.
    

**Work split**

- **Progress lane:** project advancement, delivery, follow-through, and next-step generation.
    
- **Hygiene lane:** interface validity, drift detection, stale-state detection, dependency breakage, and structural-risk management.
    

Both splits must remain legible in planning, review, and control surfaces.

### Cold start and bounded entry

1. Start from the managed runtime anchor and the relevant managed canon or ritual entrypoints.
    
2. Read the escalation/exception boundary before proceeding with work that could cross authority, truth, or hold boundaries.
    
3. Load the current bounded task, plan, or ritual entrypoint.
    
4. For project work, read the project interface package first.
    
5. Read only the specialized protocol surfaces needed for the bounded task.
    

A cold start is valid only when context expansion remains bounded to the current task.

### Project interface entry rule

Project work begins from the interface package, not from an unbounded tree scan.

At top level, the project interface package must expose the project control surfaces needed to route and understand work. Detailed schema and validation rules belong in `PROJECT_INTERFACE_CONTRACT.md`, not here.

### Session cycle

1. Classify the session as progress work or hygiene work.
    
2. Identify the target project or system surface.
    
3. Read the minimum required control surfaces and accepted truth.
    
4. Perform bounded work.
    
5. Route any truth-change candidate into the promotion path rather than mutating accepted truth directly.
    
6. Emit durable outputs for material work, including session trace, allowed state updates, hygiene findings where needed, and escalation artifacts when triggered.
    

A material session without durable trace is incomplete.

### Night cycle

Night planning is the principal synthesis cycle for cross-session continuity.

Night reads the latest session traces, project control surfaces, open promotion candidates, current hygiene findings, and open holds or escalations.

Night produces:

- progress-lane outputs such as next session targets, blockers, and bounded follow-up recommendations
    
- hygiene-lane outputs such as missing interfaces, stale state, drift, broken dependencies, and structural risk
    
- split plans for operator-facing work and cloud/background work where applicable
    

Night may recommend, queue, and package change. It does not directly mutate accepted truth.

## Authority order and subordinate surfaces

The runtime authority order is:

1. `OPERATING_SPINE_CANON.md`
    
2. sibling managed canons and protocols in `managed/rules/` and authoritative ritual protocols in `managed/rituals/`
    
3. compact managed anchors and rituals such as `AGENTS.base.md` and `BOOTSTRAP.md`, which point into the governing canons but do not replace them
    
4. user-owned local truth and override surfaces, including `user/AGENTS.md`, which may tighten or localize behavior but may not weaken managed governance
    
5. companion and reference material in `docs/`
    
6. transient working outputs, candidate artifacts, and ephemeral chat context
    

Subordinate outward pointers include, at minimum:

- `PROJECT_INTERFACE_CONTRACT.md` for project-interface control surfaces and validation boundaries
    
- `PROMOTION_PROTOCOL.md` for truth-change gating
    
- `SESSION_EXPORT_PROTOCOL.md` for durable session trace
    
- `NIGHT_PLANNING_PROTOCOL.md` for full night-synthesis procedure
    
- `QA_HYGIENE_PROTOCOL.md` for findings, severity, routing, and closure consequences
    
- `ESCALATION_EXCEPTION_BLOCK.md` for stop, hold, and escalation law
    
- `AGENT_SWARM_INTERACTION_CANON.md` for role, delegation, handoff, and routing law outside this top-level canon
    

## Boundaries and anti-drift rules

- Do not reinstall a file-production-first architecture under new terminology.
    
- Do not treat README files, docs, or rituals as substitute hosts for constitutional runtime law.
    
- Do not treat memory surfaces, session notes, or state snapshots as accepted truth.
    
- Do not mutate accepted truth from session outputs, night outputs, hygiene findings, experiment outputs, or cloud outputs outside the promotion path.
    
- Do not let `OpState` become de facto truth by convenience.
    
- Do not let `BePr_SSOT` be treated as accepted truth without promotion.
    
- Do not widen scope silently when a task stops being bounded.
    
- Do not collapse operator and cloud execution into one indistinct stream.
    
- Do not bypass project-interface entry by default with whole-tree traversal.
    
- Do not assume exact config behavior from desired architecture.
    
- Do not duplicate detailed subordinate law here when a managed protocol or canon is the truthful host.
    

## Compatibility notes

This canon is written for the living `07_finalopenclawsystem` shell, not for a clean-sheet rebuild.

Older files that lack the full newer metadata model remain usable when their authority boundary is still readable and when the managed canons are treated as the runtime source of truth.

Where an older living file and a new managed canon overlap, the managed canon governs runtime behavior and the older file must be read as bridged, companion, or transitional rather than as a competing authority surface.

Compatibility is preserved by keeping this file at the level of operating law, while detailed schemas, packet mechanics, and ritual procedures remain in their subordinate hosts.

## Self-check

- **Preserved from blueprint host:** operating-spine-first governance, the governing order `operating spine -> project interface -> knowledge promotion -> file production`, the four nested loops, the two orthogonal lane splits, the `BePr_SSOT -> SSOT -> OpState` authority chain, interface-first entry, packetized truth change, Night as principal synthesis cycle, and escalation/hygiene as first-class control surfaces.
    
- **Tightened or demoted for DR7 consistency:** the full surface metadata model, explicit initial surface set, packet-minimum field list, and other schema-adjacent details were demoted so this file stays constitutional and does not duplicate subordinate law; the vFin compatibility-first posture and concise top-level framing were kept.
    
- **Points outward to subordinate files:** `PROJECT_INTERFACE_CONTRACT.md`, `PROMOTION_PROTOCOL.md`, `SESSION_EXPORT_PROTOCOL.md`, `NIGHT_PLANNING_PROTOCOL.md`, `QA_HYGIENE_PROTOCOL.md`, `ESCALATION_EXCEPTION_BLOCK.md`, and `AGENT_SWARM_INTERACTION_CANON.md`; that matches DR7’s new-target-file lane and process ordering for this canon as an Alpha prerequisite.
    
- **Unresolved ambiguity:** the blueprint host pushes farther than the vFin seed on mandatory metadata/surface formalization and on how much explicit operating-surface taxonomy belongs here. This draft resolves that by keeping the law load-bearing but schema-light; broader metadata formalization is left to the later grammar and contract files rather than silently merged here.

## Holding-layer compatibility addendum

The first-iteration holding-orchestration model is compatible with this canon when it is expressed through managed seed files and process files rather than treated as self-executing runtime law.

The named first-iteration seed agents are:

- `alfred`
- `meta_ops`
- `meta_strategy`
- `meta_detective`
- `special_ops__knowledge_bank`
- `special_ops__informatics_design`
- `special_ops__prompts_workflows`
- `special_ops__ai_handling_routing`
- `special_ops__hygiene_clean`

These seeds:

- live in `managed/agents/`
- operationalize bounded routing and overlap clarity
- remain subordinate to this canon and the sibling managed rules
- do not by themselves authorize runtime, truth, project-interface, or config mutation

The final-system boundary for this architecture remains:

- `managed/`
- `user/`
- `docs/`
- `README-OpenClaw.md`

`NewFinals/`, `BaselinePatches/`, and `AdvancedUpdateProcess/` are source or staging surfaces only.

Project-local or subsidiary-style instances remain interface-gated. No local agentization becomes normal operating posture until the project exposes a valid interface package under the project-interface contract.

The domain-master pattern may be described in companion or seed surfaces, but concrete domain-master runtime authority is source-gated and not established by this addendum.

Any T3/T4 change affecting managed law, accepted truth, project-interface surfaces, or runtime/config behavior remains promotion-gated and operator-approved.