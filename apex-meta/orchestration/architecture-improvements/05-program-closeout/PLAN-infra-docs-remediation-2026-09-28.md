---
type: Plan
title: Infra-docs remediation — ranked, dependency-ordered, test-gated (NOT yet executed)
description: >
  Ranked fix list + dependency order + single-canonical-home design for the ki-basis infrastructure
  documentation, grounded in the 2026-09-26 environment baseline (+ its post-build optimizations) and
  verified against the LIVE system. Nothing here is executed; each step is gated, git-reversible, and
  gets an independent adversarial review before push.
created: 2026-09-28
status: awaiting operator GO (per-step)
baseline: "VALID CURRENT STATE = the environment created 2026-09-26 + the optimizations that followed (node moved outside, skills re-placed). Anything predating that which conflicts with it is SUPERSEDED history."
authority_order: "LIVE running system > single most-recent authoritative decision (ADR-002 / latest D-xx) > everything older. Superseded ≠ authoritative, even if it was once deliberate."
companion_audit: apex-meta/orchestration/architecture-improvements/05-program-closeout/FINDINGS-infra-docs-audit-2026-09-28.md
tests: apex-meta/orchestration/architecture-improvements/05-program-closeout/tests/
---

# Infra-docs remediation plan (2026-09-28)

## 0. The decision test (applied to every candidate, currency BEFORE tidiness)
1. Does it **contradict the live system / current authority**? → STALE → banner/archive (regardless of how
   deliberate it once was — this is how superseded decisions get cleaned, not protected).
2. Does it **match live AND is it a current, deliberate decision**? → LEAVE ALONE (protected even if it looks
   redundant, e.g. an intentional mirror — *if still current*).
3. **Unclear** which decision governs / whether it's current? → ASK, don't guess.
Ground truth for step 1 = the LIVE system, verified below — not other documents.

## 1. Test evidence (run 2026-09-28; re-runnable — see `tests/`)
- **Runtime health/efficiency — GREEN 29/29** (`tests/infra-health-test.sh`): 13/13 containers running; all
  endpoints warm (<2s: Hermes ~11 ms, OpenProject 0.8 s); idle CPU <2% (no bottleneck); Postgres roles ≤18%
  of limit; cross-DB `REVOKE CONNECT` holds; and every *claimed fact* verified (private Hermes really →
  leela-op178, OpenProject really 17.8.0, Hermes really on bind mounts, drift-volume really absent, keepalive
  really active). **No bottleneck, no hallucinated functionality. The live baseline is sound — this is a
  docs-only cleanup, not a system change.**
- **Doc-integrity/consumer scan — SAFE** (`tests/doc-integrity-lint.sh`): the candidate docs have **no
  automated consumer** (references are session logs + throwaway `.agents/` scratch, not skills/manifests/
  run-state) → editing them cannot break automation. The scan also expands the stale set (a pre-baseline
  `Alpine/ImplementationPlans/2026-09-03-*` tree) and shows **false positives** (it flags the *current*
  `03-…/index.md` and vendored KB sources) — so remediation is per-file judgment, never grep-and-banner.

## 2. Single canonical home (the "one place") — DESIGN for approval
**Proposal:** one current-state file — **`apexai-os-meta/ki-basis/docs/INFRASTRUCTURE.md`** — is THE description
of "what is true now": the one WSL2 Apex engine, the shared Postgres cluster, all four compose stacks + the
three sibling repos (`ki-basis-shared`, `leela-op178`, `lika-community`), ports, volumes, keepalive, and the
T10 state. It links **down** to the supporting layers rather than duplicating them:
- **Why/decisions:** `DUAL_INSTANCE_ARCHITECTURE.md` §6 (ADR-002) — kept as the decision record.
- **How it got here / execution history:** the `03-`/`05-` bundles.
- **Actual runtime definitions:** the four `compose*.yaml` (authoritative for services/volumes/networks).
Every entrypoint (root `CLAUDE.md`/`AGENTS.md`, `ki-basis` ones, `AGENT-OPERATING-CONTEXT.md §13`) points **here**.
Every superseded doc gets: a one-line banner `> ⛔ SUPERSEDED (pre-2026-09-26 or reversed by ADR-002) — current truth: ki-basis/docs/INFRASTRUCTURE.md` and, if fully dead, is moved to an `_archive/` sibling (kept, not deleted) with the banner + a back-link.
*(Alternative if you prefer no new file: designate the existing ADR-002 §6 + `03-` bundle as the canonical pair and point everything there. INFRASTRUCTURE.md is cleaner because it separates "what is true now" from "why we decided it.")*

## 3. RANKED fix list (severity × reachability × risk)
| # | sev | item | why it matters | action | currency verdict |
|---|---|---|---|---|---|
| **R1** | 🔴 CRITICAL | Live routing hazard: `AGENT-OPERATING-CONTEXT.md §13` → `apex-meta/Alpine/ARCHITEKTUR-BASIS.md` → names Docker Desktop current + `compose.yaml` "runtime authority" | Only item that **actively misroutes agents** to retired topology + the dangerous rollback file | Re-point §13 to current authority; banner `ARCHITEKTUR-BASIS.md` superseded → canonical | SUPERSEDED (contradicts live) |
| **R2** | 🟠 HIGH | No single source of truth (6 overlapping "current arch" docs) | Root cause of recurring drift; prerequisite for clean banners | Author/designate the one `INFRASTRUCTURE.md` (§2) | n/a (new) |
| **R3** | 🟠 HIGH | Reachable stale docs asserting retired topology: `STACK_ARCHITECTURE.md` (v14), `DUAL_INSTANCE_RUNBOOK.md` (two-pg/DD), dossier `00_`/`02_` | A human/agent could read them as current | Banner → canonical; archive the clearly-dead | SUPERSEDED |
| **R4** | 🟡 MED | Leela misplacement: `Leela-Cloud-2026/docs/ProjectMM/openproject/` = shared infra in the product repo | Your stated concern; confusion + drift risk | Relocate to apexai-os-meta (style TBD) + update ~4 pointers + fix broken link | MISPLACED (content mostly current) |
| **R5** | 🟡 MED | Spec mirror drift (2 mirrors miss frontmatter + the ⛔ shared-DB reversal banner) | A mirror reader hits old "zero shared DBs" with no up-front warning | Re-sync the banner/frontmatter into mirrors, OR collapse mirrors to a pointer | DRIFTED |
| **R6** | 🟢 LOW | Pre-baseline history un-archived: `Alpine/ImplementationPlans/2026-09-03-*`, `Iteration2`, `Maybe3rdIt`, `TARGET-ACCEPTANCE-REPORT`, dossier `transcripts/`+`workflow_plans/` | Clutter; could mislead if opened, but not routed-to | Archive + banner as HISTORY (never delete). **Exclude** vendored KB raw sources (not ours) | SUPERSEDED-HISTORY |
| **R7** | 🟢 LOW | Cosmetics: `CURRENT-STATE.md` frontmatter says superseded though body is current; `GEMINI.md`/`.hermes.md` lack the pointer banner; `ki-basis/docs/BOT_WIRING…` (reverse-misplaced community doc) | Minor inconsistencies | Fix frontmatter; add pointer banner; move/point BOT_WIRING to lika-community | mixed |
| **SEC** | ⚫ SEPARATE | `leela-op178` compose files carry a hard-coded `SECRET_KEY_BASE` inline | Security, not docs | Move to `.env` — **separate track, its own gate** | n/a |

## 4. Dependency order (what must change first)
```
R1  (independent — points to the already-current 03 bundle) ── do FIRST (safest, highest value)
      │
R2  (author the one INFRASTRUCTURE.md) ── prerequisite for the banners below
      ├── R3  (banner/archive stale "current" docs → link to INFRASTRUCTURE.md)
      ├── R5  (mirror fix → point to / carry canonical)
      └── R7  (cosmetics that reference the canonical)
R4  (Leela relocation) ── independent of R2; needs its own ~4 pointer edits; do after R1–R3
R6  (archive pre-baseline history) ── independent; low risk; anytime after R2
SEC (security) ── fully separate track
```
Rationale: R1 needs nothing new (current authority already exists) so it goes first and removes the only *hazard*. R2 must precede R3/R5/R7 because their banners link to it. R4/R6/SEC are independent and can be sequenced by your preference.

## 5. Per-step guardrails (how we prevent drift during execution)
For **every** step, before push: (a) show the exact diff; (b) list inbound references touched; (c) **independent
adversarial review** by a fresh agent tasked only with "does this misread intent or break a dependency?"; (d)
re-run `tests/infra-health-test.sh` (must stay GREEN — proves the live system is untouched) and
`tests/doc-integrity-lint.sh`; (e) git-reversible, per-step commit. **Invariant: the live stack stays
byte-identical — this is documentation only.**

## 6. Definition of done
One authoritative current-infra description that every entrypoint routes to; no doc asserts retired topology
without a superseded banner; general infra no longer in the Leela product repo; the spec has one maintained
source; both test scripts pass; nothing on the live system changed (health test still GREEN).
