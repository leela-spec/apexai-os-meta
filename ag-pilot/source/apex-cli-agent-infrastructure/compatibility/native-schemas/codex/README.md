---
type: Reference
id: APEX-INFRA-CODEX-SCHEMAS
title: Pinned Codex Schema Guide
description: Scope, provenance and interpretation limits for the proposed package artifacts.
status: draft
tags: [examples, compatibility, evidence]
---

# Pinned Codex wire schemas

The five JSON schemas are copied unchanged from OpenAI Codex release `rust-v0.167.2`. `provenance.json` records their original blob identities, direct URLs and local SHA-256 digests. `LICENSE` and `NOTICE` accompany the copies; their retrieval metadata is in `license-provenance.json`.

These files define wire shapes. They do not establish that every accepted field is implemented. The package separately checks the proposed adapter's narrow semantic contract in `../../../examples/native/codex_offline_check.py`. No Codex host was launched by that check.
