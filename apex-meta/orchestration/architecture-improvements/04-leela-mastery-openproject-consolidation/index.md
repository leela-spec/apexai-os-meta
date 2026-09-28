# Leela & Mastery — OpenProject Consolidation and Multi-Agent Skill Standardization

Consolidate personal/professional project orchestration into **one root OpenProject project**
("Leela & Mastery"), so the operator can see and direct everything from one place instead of
fragmented per-account, per-tool views. Verify that **all AI agent accounts** (Codex ×2, Claude Code
×2, Antigravity ×1) discover and use the **same existing OpenProject skill** identically. Prove
OpenProject can carry **real dependency structure** (not flat todo lists) using **real existing data**,
not synthetic test fixtures.

This is a **cross-repo** initiative — it touches `Leela-Cloud-2026` (owns the OpenProject skill and the
live PM instance), `MasterOfArts` (the entrepreneurship side, many verticals), and `apexai-os-meta`
(this bundle, plus the WSL2 Docker migration that this initiative's live OpenProject instance now runs
on). It lives here, not inside any one product repo, for the same reason the Docker migration bundle
does: it's cross-cutting, and `Leela-Cloud-2026` in particular has a **frozen** `docs/orchestration/`
allowlist that forbids new top-level handovers there.

* [00-handover](00-handover.md) — full context, decisions already made, open decisions still needed,
  safety boundaries, and the exact next actions for whoever picks this up.
* [01-leela-plan-breakdown-design](01-leela-plan-breakdown-design.md) — the full, cited epic→task→subtask
  →dependency mapping for all Leela plans (3 apex-meta epics + 30 SSOT packets) and the locked build plan.
* [02-preflight-and-transport-diagnosis](02-preflight-and-transport-diagnosis.md) — read-only, reproducible
  proof of the two blockers (skill can't reach the instance from Windows; project types not enabled) and the
  minimal change plan. Nothing applied.
* [03-visual-explainer](03-visual-explainer.html) — plain-language, diagram-based explainer of the setup,
  the problems, and the fix options (open in a browser).
* [05-handover-browser-keepalive](05-handover-browser-keepalive.md) — **DONE 2026-09-28**: idle-sleep fixed
  via a self-healing Windows-held `wsl` session (Startup vbs) + systemd app-warmer; verified 401 in <1s after
  95s idle. OpenProject #122–125 Closed.
* [06-handover-mastery-taxonomy](06-handover-mastery-taxonomy.md) — **DONE 2026-09-28**: live design with
  operator → created `MoA-Content` (id 6), `MoA-Business` (id 7), `ApexAI-OS` (id 8) under root; containers only.
* [07-handover-5account-skill-standardization-test](07-handover-5account-skill-standardization-test.md) —
  **DONE 2026-09-28** — all 3 tool surfaces (Codex/Claude/Antigravity) auto-invoke the one canonical skill,
  verified live (Antigravity fixed via the antigravity-cli link). Optional: 2nd Codex/Claude accounts + Antigravity multi-account.
* [08-handover-audit-and-improve](08-handover-audit-and-improve.md) — auditor/improver brief: quantify the
  WSL drag, best-practice web research (incl. custom skill vs official MCP server), and prove multi-repo
  (MasterOfArts) access with a real agent.

**Status: BUILT — full Leela plan imported (2026-09-27).** Under root project **Leela & Mastery** (id 4) →
sub-project **Leela** (id 3): 83 work packages (11 Epics, 30 Features, 23 User stories, 15 Tasks,
4 Milestones), statuses set (22 Closed / 2 In progress / 17 On hold / 42 New), 67 dependency relations —
all created through the OpenProject skill and verified by read-back. Enabling infra done this session:
Node LTS installed in WSL (option C, skill transport), OpenProject republished on `0.0.0.0:8083` (option A,
Windows browser access), all 7 work-item types enabled on Leela, skill hardened (`doctor`,
`type.list --project`, type name→id). Remaining/deferred: browser idle-sleep keepalive (operator skipped
for now); Mastery-of-Arts sub-project taxonomy (live session); 5-account skill-standardization test;
optional wave milestones + finer task breakdown. Full evidence in
[02-preflight-and-transport-diagnosis](02-preflight-and-transport-diagnosis.md) and
[01-leela-plan-breakdown-design](01-leela-plan-breakdown-design.md).
