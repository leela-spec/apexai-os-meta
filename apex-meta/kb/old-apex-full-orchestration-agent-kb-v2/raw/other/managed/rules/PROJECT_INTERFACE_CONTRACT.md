# PROJECT_INTERFACE_CONTRACT

## 1. Purpose

- **Decision:** This file defines the minimum control interface every active OpenClaw project must expose to the operating spine.
- **Decision:** The contract exists so the meta layer can route, plan, verify, escalate, and synthesize across projects without scanning each project's full internal tree.
- **Decision:** This contract standardizes project-facing control surfaces, not whole-project architecture.
- **Constraint:** The contract must preserve the boundary between local memory, accepted truth, live operational state, and durable trace.

## 2. Required project control surfaces

Every active project must expose a project interface package.

- **Adopt now:** Default project-local control directory is `.openclaw/`.
- **Constraint:** If a project cannot use the default directory for a hard reason, the registry must declare the alternative interface path explicitly.

### Required surfaces

1. `ProjCard.md`
2. `OpState.md`
3. `SSOT_INDEX.md`
4. `SigMat.json` or `SigMat.md`

### Recommended surfaces

5. latest `Session Export`
6. latest `QA/Hygiene`
7. open `Promotion Packet` queue reference
8. project-local overlay reference, if present

- **Decision:** Required surfaces are the minimum viable control package.
- **Decision:** Recommended surfaces become required only when project complexity or a local overlay makes them load-bearing.
- **Constraint:** Missing required surfaces are a hygiene failure and may block project participation in normal meta orchestration.

## 3. Minimum field meanings

- **Decision:** Contract surfaces should carry stable identity metadata.
- **Required dimensions:** `class`, `role`, `surface`, `quality`, `scope`, `purpose`, `dependencies`.

### 3.1 ProjCard

- **Purpose:** compact meta-facing summary of the project as a controllable unit.
- **Required fields:** `project_id`, `project_name`, `root_path`, `project_purpose`, `current_priority`, `current_operating_state`, `top_blockers`, `next_session_targets`, `ssot_entrypoints`, `opstate_pointer`, `sigmat_pointer`, `overlay_pointer` or `none`.
- **Constraint:** ProjCard is an interface summary, not a truth surface.

### 3.2 OpState

- **Purpose:** expose the project's live operational state.
- **Required sections or fields:** `active`, `blocked`, `next`, `holds`, `recent_changes`, `pending_recommendations`, `last_session_export`, `open_escalations`.
- **Constraint:** OpState is not a truth surface and may reference accepted truth without redefining it.

### 3.3 SSOT_INDEX

- **Purpose:** map where accepted truth lives inside the project.
- **Required fields:** `truth_domains`, `truth_files`, `module_or_domain_scope`, `authority_notes`, `last_truth_review`.
- **Constraint:** Each governed domain must have a clear truth owner.

### 3.4 SigMat

- **Purpose:** compact signal surface for evidence strength, risk, disagreement, and recommended action.
- **Required fields per tracked item:** `item_id`, `impact`, `evidence_strength`, `risk`, `confidence`, `disagreement`, `recommended_action`, `reason_refs`.
- **Constraint:** SigMat is a signal transport surface, not a reasoning substitute.

## 4. Validation and truth-boundary rules

- **Rule:** Read the interface package before deep project traversal.
- **Rule:** Deep traversal is justified only when the interface is missing or invalid, the task explicitly requires deeper content, truth review needs domain inspection, or escalation requires source inspection.
- **Constraint:** `ProjCard` and `OpState` are control surfaces, not accepted truth.
- **Constraint:** `SSOT_INDEX` maps accepted truth but does not replace the truth files it points to.
- **Constraint:** `SigMat` may summarize signal and recommended action, but scores without references are invalid.
- **Decision:** Missing required surfaces is a `P0` hygiene failure.
- **Decision:** Pointer breakage, stale `OpState`, or unresolved truth ownership are at least `P1` hygiene failures.
- **Decision:** Default cadence is session-bound for `OpState`, change-bound for `ProjCard` and `SigMat`, and truth-review-bound for `SSOT_INDEX`.

## 5. Relation to memory, session export, and night planning

- **Decision:** Local memory files remain lightweight, local, and durable support surfaces.
- **Constraint:** `user/memory/MEMORY.md` and `user/memory/context/active.md` are not project-interface substitutes, not `SSOT`, and not `OpState`.
- **Decision:** `SESSION_EXPORT_PROTOCOL.md` defines durable session trace. Session exports feed `OpState`, `ProjCard`, and later synthesis through explicit pointers rather than by making memory carry trace authority.
- **Decision:** `NIGHT_PLANNING_PROTOCOL.md` reads project interface surfaces and session exports to produce bounded recommendations.
- **Constraint:** Night outputs may recommend control updates, but they do not silently replace the interface package or mutate accepted truth.

## 6. Compatibility and defer note for local instances

- **Decision:** Legacy projects may map existing summary, state, truth-map, and signal files into the contract temporarily if the mapping is explicit and functionally equivalent.
- **Constraint:** Silent inferred mappings are invalid.
- **Constraint:** A legacy file that mixes truth, state, and reasoning so heavily that the boundary is unreadable is not a valid mapped surface.
- **Decision:** This contract exists before any concrete local `user/projects/PROJECT_INTERFACE.md` instance.
- **Constraint:** Do not force creation of `user/projects/PROJECT_INTERFACE.md` until a real operational need exists.
- **Decision:** The contract is compatible with gradual adoption and does not require repo-wide metadata backfill in the first rewrite round.
