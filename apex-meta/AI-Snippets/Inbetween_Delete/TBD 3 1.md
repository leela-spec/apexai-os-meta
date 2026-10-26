Plan file is now a complete cold-start handover — ground truth G1–G6, five phases, the impact ranking, the open-items list, a full source index of every file I opened (with the ones I deliberately didn't, marked as such), and git facts.

**Here is the kickoff text to paste into a fresh chat:**

I'm continuing work on finalizing the Skill Tree feature in C:\GitDev\Leela-Cloud-2026.

Read docs/audits/handovers/2026-10-06-skill-tree-finalization-handover.md in full
before anything else. It is self-sufficient — every fact in it was verified against
the originating artifact, so do not re-derive sections G1–G6.

Execute Phase 0 and Phase 1 only. Stop at the Stage 1 exit gate and report.

Specifically:
- Phase 0's four record-repair edits.
- Phase 1's story→rule traceability in docs/ssot/features/skill-tree/spec.md —
  rule prose, never a new ledger column (a story_ref column fails
  materialization_contracts.py:944 on the first gate run; see G3).
- The read-only Stage 1 assessment over ST-01…ST-22, ST-23 as anti-requirement.
- The bounded Creator Content input-contract check only — hierarchy, lvl, branch,
  hasBundle/hasFusion/hasSuccessor, version identity. Do not design Creator Studio.

Constraints:
- Do NOT merge codex/p1to4. Cite b6b6b518 via git show (operator decision).
- Do NOT generate screens, mockups, or a design brief. Claude Design starts at Phase 5.
- Do NOT execute build packets P01–P04 yet.
- Preserve the newer no-confirmation / direct-add direction; ST-23 (tray) is superseded.
- Preserve unrelated dirty files — the tree has in-flight Kharma and user-story-census work.
- Verify with python scripts/gates.py --since origin/master. A clean --since is
  sufficient evidence; do not follow it with --full without one of the three named
  triggers in AGENTS.md.

Stage 1 is expected to halt at its exit gate on undecided stories. That is the designed
behavior. Report the gap list and the decision queue; do not guess a bucket for an
undefined story.

One caveat on zero-context-loss: the handover cites `b6b6b518` rather than merging it, per your decision. That's safe as long as `origin/codex/p1to4` survives — if that branch is ever pruned, the rulings go with it. Phase 3 removes the exposure by promoting R1 and R2 into `SSOT-D-###` records, which is where they belong regardless of branch policy. Worth not deleting that branch until Phase 3 lands.

Approving below writes the handover into the repo at docs/audits/handovers/2026-10-06-skill-tree-finalization-handover.md. Nothing else is touched — Phase 0's edits are for the next session, not this one.