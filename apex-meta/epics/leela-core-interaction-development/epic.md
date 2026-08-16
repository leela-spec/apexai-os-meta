---
title: "Leela Core Interaction Development"
status: open
priority: high
due_date: null
created_date: 2026-08-16
updated_date: 2026-08-16
source:
  - "apex-meta/handoff/plan-packets/apex_plan_packet-20260816-leela-core-interaction-development-v2.md"
review_flags:
  - resolution_context_contract_mismatch
  - path_optionality_mismatch
  - legacy_surface_disposition_requires_runtime_verification
---

# Leela Core Interaction Development

## Goal

Deliver a working evidence-backed Home -> Skill Tree -> confirmed scope -> frozen resolution-context vertical slice using the existing Leela architecture and ownership contracts.

## Constraints

- Reuse existing Home and bounded spatial Skill Tree implementations; do not rebuild them from scratch.
- Home is a non-owning presentation/composition surface.
- Skill Tree owns structural discovery and confirmed ScopeSelection only.
- Algorithm resolves within confirmed scope and must not widen it.
- Sequencing owns executable structure; Path owns demand/priority; Rhythm owns temporal supply/placement; Content owns Chunk metadata/prerequisites/relationships.
- No invented deadlines.
