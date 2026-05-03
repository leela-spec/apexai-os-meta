# BEST_PRACTICES

## Purpose

Compact operating practices for `special_ops__hygiene_clean`.

This scaffold summarizes reusable hygiene rules and points to appendices for evidence. It is not a promotion surface and does not mutate accepted truth.

## Appendix map

| Appendix | Use |
|---|---|
| `appendices/APPENDIX_KB_SOURCE_MANIFEST.md` | source coverage, role fit, duplication, gap risk, authority risk |
| `appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md` | ranked information units and scaffold routing |
| `appendices/APPENDIX_KB_CANDIDATE_LEDGER.md` | candidate rules, templates, scoring, status |
| `appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md` | postmortem evidence and anti-drift safeguards |

## Core practices

### BP-HC-001 — Separate authority from verification

- **Rule:** Decide source authority before acting; verify output before approval.
- **Use when:** file, patch, audit, routing, cleanup, or KB extraction work will be reused or committed.
- **Evidence:** `HC-INFO-001`, `HC-EVID-001` to `HC-EVID-003`.
- **Status:** `strong_candidate`.

### BP-HC-002 — Treat process files as blocking gates

- **Rule:** Citing a process rule is insufficient; execution must prove compliance with that rule.
- **Use when:** an agent references doctrine, patch process, source authority, or migration rules.
- **Evidence:** `HC-INFO-009`, `HC-EVID-013`.
- **Status:** `strong_candidate`.

### BP-HC-003 — Lock execution mode before edits

- **Rule:** Declare exact mode, branch/root, target files, allowed actions, forbidden actions, stop conditions, and deliverable before patching or cleanup.
- **Use when:** work touches drift-sensitive files, repo structure, KB surfaces, rituals, or governance docs.
- **Evidence:** `HC-INFO-005`, `HC-EVID-004`, `HC-EVID-014`.
- **Status:** `strong_candidate`.

### BP-HC-004 — Patch one drift-sensitive file at a time

- **Rule:** Execute one file, verify the landed diff, then advance.
- **Use when:** content preservation, source hierarchy, or exact wording matters.
- **Evidence:** `HC-INFO-006`, `HC-EVID-006`.
- **Status:** `strong_candidate`.

### BP-HC-005 — Prefer exact-span repair over rewrite

- **Rule:** For bounded defects, repair only the damaged span. Whole-file rewrite is a protocol violation unless explicitly authorized.
- **Use when:** fixing corrupted fences, paths, anchors, local wording drift, or damaged blocks.
- **Evidence:** `HC-INFO-007`, `HC-INFO-008`, `HC-EVID-007` to `HC-EVID-012`.
- **Status:** `strong_candidate`.

### BP-HC-006 — Keep findings separate from truth changes

- **Rule:** Hygiene findings, postmortem lessons, and candidate rules remain findings/candidates unless routed through verification and promotion.
- **Use when:** a cleanup result appears to imply a canon, SSOT, config, or role-boundary change.
- **Evidence:** `HC-INFO-014`, `HC-INFO-015`.
- **Status:** `strong_candidate`.

### BP-HC-007 — Record duplication and access gaps before extraction

- **Rule:** Source manifests must record representative source, duplicate status, access status, inclusion decision, role fit, and authority risk.
- **Use when:** building or refreshing agent KB bases.
- **Evidence:** `HC-INFO-013`; `APPENDIX_KB_SOURCE_MANIFEST.md`.
- **Status:** `strong_candidate`.

## Apex status note

- **Accepted scope:** included in the Apex KB base as current operating guidance.
- **Promotion boundary:** entries marked `strong_candidate` remain non-runtime truth until validated and promoted through the governed path.
- **Validator:** `meta_detective`.

## Non-goals

- Do not design architecture.
- Do not approve promotions.
- Do not own stop law.
- Do not convert postmortems into universal doctrine without verification.
- Do not put detailed evidence into this scaffold; use appendices.
