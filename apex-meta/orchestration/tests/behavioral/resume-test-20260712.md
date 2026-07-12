# Resume-from-files behavioral test — 2026-07-12: PASS

**Setup:** a fresh, context-isolated session (spawned Explore agent, zero chat memory) was given ONLY the US-IDEA-01 run folder + `schemas/run-record.schema.md` and asked to reconstruct: run identity, last completed step, finished-vs-in-flight, executed mutations + authorization, and the authoritative artifact version/hash/verified-status location.

**Result: all five reconstructed correctly from files alone.**
- run_id/story: correct (`US-IDEA-01-20260711`), derived from lock/decision/gate files + folder-name rule
- last step: `10-mutation-record.md`, correctly read as terminal (no `expected_action` = not a handoff)
- state: finished — completion statement + both mutations `lifecycle_stage: confirmed` with fetch-back
- mutations: G1+G2 with `operator_validation: confirmed` and verbatim answer channel cited
- artifact: v2, sha256 `cd83e576…`, verified status correctly located in the `08` **sidecar** — the resuming session explicitly avoided the DL-1 trap (artifact frontmatter still says `candidate`; sidecar wins)

**Honest caveats the tester raised (both by-design, recorded):**
1. DL-1: a naive resumer trusting artifact frontmatter alone would read `candidate` — verified status is only in the sidecar. Mitigation already in place: run-record schema line notes DL-1; the enforcement path (`orchestration_check.py canon-write`) takes state from the gate record, not the artifact.
2. Mutation targets outside the run folder are confirmed via `10`'s recorded fetch-back, not independent reads — expected under the test's scope restriction.

**Gate satisfied:** "A killed run can resume using only durable files and run_id" (M2 gate) and "The system resumes from files without chat-memory reconstruction" (M8 gate).
