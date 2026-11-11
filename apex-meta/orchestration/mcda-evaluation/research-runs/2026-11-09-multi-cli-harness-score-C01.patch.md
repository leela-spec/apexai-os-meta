---
type: Adapter
id: PATCH-MULTICLI-HARNESS-C01-20261109
title: "C01 exact-match arithmetic correction to multi-CLI harness bake-off"
description: "One-byte-safe textual correction of weighted score; no existing file modified by this patch artifact."
status: candidate
date: 2026-11-09
tags: [patch, scoring, validation, exact-match]
---

# C01 — Exact-match score correction

**Status: PATCH PREPARED; NOT APPLIED.** The research report was independently read back. All 14 pilot test rows and source references exist; one arithmetic total was found incorrect.

**Target:** [2026-11-09-multi-cli-harness-operator-bakeoff.md](2026-11-09-multi-cli-harness-operator-bakeoff.md)

**Expected source Git blob SHA:** `e9cd6973b2f6d77505a31cda1b7f21030b681f39`

**Calculation:** Quota (4.0×25%) + CLI (5.0×20%) + durable (3.0×20%) + workflow (4.0×15%) + permissions (2.0×10%) + Windows/local (4.0×10%) = 3.80/5.00 = **76.0/100**, not 78.0. The ordering is unchanged (Paseo 76.0, CAO 74.5, OpenMausBot 69.5, Orca 64.0, Omnigent 61.5).

## Mode A — exact-match replacement

<file>apex-meta/orchestration/mcda-evaluation/research-runs/2026-11-09-multi-cli-harness-operator-bakeoff.md</file>
<old>
| **Paseo + one account plugin** | 4.0 | 5.0 | 3.0 | 4.0 | 2.0 | 4.0 | **78.0** | Plugin cannot prove Codex+Windows real failover; dangerous agy access |
</old>
<new>
| **Paseo + one account plugin** | 4.0 | 5.0 | 3.0 | 4.0 | 2.0 | 4.0 | **76.0** | Plugin cannot prove Codex+Windows real failover; dangerous agy access |
</new>

## CLI executor instructions

1. On `main`, fetch the latest authoritative target; inspect the exact old line and source blob SHA.
2. Require exactly one occurrence of the `<old>` block. If absent/multiple, STOP and report drift; never overwrite/regen the whole file.
3. Apply only this exact replacement using the canonical surgical patcher (or a deterministic unique-string replace in a clean checkout). Preserve all other bytes.
4. Verify the corrected total by the stated arithmetic; verify only the target file changed; re-read the entire affected table.
5. Commit and push the one-line mutation on `main` only if the exact-match patch applied and the final file diff is one line. Record the actual commit SHA. Do not declare C01 applied from the mere existence of this patch file.

**Why separate patch:** The Apex standard prohibits direct whole-file update APIs for existing files. This commit adds a standalone patch artifact only.
