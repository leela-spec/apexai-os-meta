# Goal

Build a NARM-support infrastructure that indexes NARM theory and personal psychological material, creates guided self-exploration flows aligned with NARM, and produces compact session-prep outputs for a NARM therapist. This is a therapy-support knowledgebase, not a replacement for the therapist.

# Current Step

Durable planning and session handoff files have been created from the operator-approved apex-plan packet.

# Phases

- Phase 1: Define safety and scope boundaries.
- Phase 2: Inventory and classify Therapy source files.
- Phase 3: Design NARM theory and personal-material index structures.
- Phase 4: Define cross-reference rules between NARM theory and personal material.
- Phase 5: Design self-exploration flows and therapist session-prep output format.
- Phase 6: Validate dependencies and compute next action through apex-sync.

# Decisions

- Operator approved the apex-plan packet for handoff.
- The project is recorded as epic `narm-support-knowledgebase`.
- The system must support therapy preparation without replacing therapist judgment.

# Open Items

- Confirm final index format and target knowledgebase location.
- Confirm whether generated index files should be written into the Obsidian Therapy folder or kept under `apex-meta`.
- Confirm privacy and redaction rules for therapist-prep outputs.
- Validate dependencies through apex-sync.

# Risks

- Scope drift into therapy replacement or diagnostic claims.
- Raw personal source material may require redaction before summary generation.
- Relationship-pattern evidence may be ambiguous until source files are inspected.
- Dependency actionability has not yet been computed.

# Next Actions

- Use apex-sync to validate dependencies and compute next action.
- Review task records under `apex-meta/epics/narm-support-knowledgebase/`.
- After validation, begin with the first confirmed actionable task.
