# Apex KB Test Run Orchestrator Handover Pack

Use `00-ORCHESTRATOR-CHAT-HANDOVER.md` as the first message in a new ChatGPT chat.
That chat becomes the single operator-facing orchestrator for one Apex KB test run.

The orchestrator does not execute Phase 0 or semantic compilation itself. It creates bounded handoffs and verifies returned artifacts.

## Files

- `00-ORCHESTRATOR-CHAT-HANDOVER.md` - master copy-paste prompt for the new orchestrator chat.
- `01-CODEX-RUNTIME-PROBE.md` - first read-only Codex task.
- `02-CODEX-DETERMINISTIC-PHASES.md` - template for preflight, lock, Phase 0, reconciliation, and postflight tasks.
- `03-GPT-PHASE1-SEMANTIC.md` - template for fresh Phase 1 semantic chats.
- `04-GPT-PHASE2-COMPILE.md` - template for the Phase 2 compilation chat.
- `05-GPT-INDEPENDENT-ACCEPTANCE.md` - template for the fresh acceptance chat.
- `06-ORCHESTRATOR-RUN-LEDGER.okf.yaml` - durable cross-chat state template.

## Truthful test scope

Commit `4fddeab59a8e4d63a8efa347ec9b3d28f33f43c1` adds the mechanistic workflow design pack. The pack's implementation-change manifest still lists required changes to the live skill and Python runtime. Therefore the orchestrator must begin with the Codex runtime probe and select one of two modes:

- `live_cli`: only when Codex proves the v2 commands and contracts are installed and executable.
- `protocol_simulation`: validates the handoff design using bounded file artifacts without claiming the production CLI is complete.

No chat may silently upgrade `protocol_simulation` to `live_cli`.
