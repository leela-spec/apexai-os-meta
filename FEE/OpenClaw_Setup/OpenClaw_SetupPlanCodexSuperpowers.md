# OpenClaw Local Executor — Revised Execution Plan

## Summary

The two research documents were read completely and reconciled with the existing master brief, handover, FEE project documents, OpenClaw configuration, executor skill, BAO rules, adapter, model installation record, tests, and stale duplicate specifications.

Verified research inputs:

- `OpenClaw Local Executor — Operator Decision Lock.md`: 593 lines, SHA-256 `909BADEDE92D9DC8CAF2F35845B413597DF31D123B82B503004EA1D5E83C5F51`
- `OpenClaw Local Executor — Installation and Implementation Plan.md`: 1,497 lines, SHA-256 `78DFEBF47E969319485CB874CEFAC28B5EB956CBC9D41B81A12BB8FF73884749`

The revised target is one persistent OpenClaw/Qwen Local Executor—not a separate FEE service. It receives bounded execution requests from APEX, uses explicitly granted browser/files/scripts/Git capabilities, supports immediate dispatch and Cron, and returns deterministic evidence. APEX and its reasoning models retain workflow, provider, prompt, evaluation, and scheduling authority.

## Architecture and Interfaces

- Make the two research documents the canonical architectural and installation authorities. Update only live pointers or contradictory installation blockers before installation; defer broad FEE renaming, archival, and `scripts/fee` migration until a successful vertical slice.
- Retain OpenClaw as the execution runtime, Qwen3-8B as the sole initial inference lane, and deterministic APEX-owned helpers as the authority boundary.
- Use a versioned execution-request document with:
    - `schema_version`, `execution_id`, and `idempotency_key`
    - originating repo, workflow, and step
    - instruction/skill, provider, and immutable `prompt_ref`
    - declared roots with `read` or `read_write` modes
    - granted tools, scripts, commands, and Git operations
    - success criteria, stop conditions, result path, and evidence directory
- Validate every request before OpenClaw receives it. Invalid paths, undeclared commands, missing success conditions, unknown tools, or widened authority fail closed.
- Support two dispatch paths:
    - Immediate: validate the request and invoke the executor using `openclaw agent --message-file`.
    - Scheduled: operator/APEX-created OpenClaw Cron jobs, including model-backed turns and deterministic exact-argv command jobs. Qwen cannot create or alter durable schedules.
- Do not introduce a global queue, FEE daemon, separate control plane, cloud-model fallback, community skill dependency, or autonomous orchestration authority.

## Execution Phases and Gates

1. **Canonicalize and preserve**
    
    - Reconfirm branch, upstream, dirty-tree inventory, model path/hash, ports, Node/npm state, and installed OpenClaw state.
    - Commit and push the decision lock, installation plan, master-brief pointer, and necessary live handover corrections directly to `main`.
    - Exclude `.obsidian`, scratch state, unrelated local files, and other user-owned changes.
    - Do not merge old branches already contained in `main`; inspect any newly supplied research branch before integrating it.
    - Preserve existing FEE code and historical documents until the post-vertical-slice audit.
2. **Prove the model baseline and install OpenClaw**
    
    - Start the existing standalone llama.cpp/Qwen server on loopback port `8090`, one inference lane, with `--jinja`.
    - Run a direct OpenAI-compatible tool-call fixture and require a genuine structured tool call—not JSON embedded in prose.
    - Dry-run and install exact OpenClaw version `2026.7.1-2` with onboarding disabled; install/confirm Node 24 first if required.
    - Run `openclaw setup --baseline`; keep the repository configuration as a reviewed template and the active configuration in OpenClaw’s normal user config location.
    - Configure the Gateway on `127.0.0.1:18789` with a non-repository token, then run config schema validation.
    - Stop on any failed baseline or version gate rather than silently substituting versions. The pin and current configuration commands are covered by the [OpenClaw npm package](https://www.npmjs.com/package/openclaw?activeTab=versions) and [configuration CLI documentation](https://docs.openclaw.ai/cli/config).
3. **Compare standalone and in-process providers**
    
    - First connect OpenClaw to the standalone server with a complete provider model catalog and run the same structured tool trajectory through OpenClaw.
    - Install llama-cpp-provider@2026.7.1-2; if that exact compatible release is unavailable, stop and record the incompatibility rather than choosing an unreviewed release.
    - Configure the official in-process provider against the existing GGUF, initially at 8K context.
    - Run identical normal-response, structured-tool, malformed-tool, timeout, and recovery fixtures through both provider modes.
    - Select the in-process provider only when it is equivalent or better. Keep standalone llama.cpp as the local diagnostic fallback until the complete acceptance suite passes; never add cloud fallback. Follow the [official llama.cpp provider contract](https://docs.openclaw.ai/plugins/llama-cpp).
4. **Build the bounded executor**
    
    - Create one `apex-executor` agent/workspace with minimal operational instructions and APEX-owned skills only; keep the skills watcher enabled.
    - Default-deny orchestration, subagents, messaging, schedule creation, unneeded web access, and elevated execution.
    - Make browser, file read/write/edit, process, scripts, tests, and Git available only when the validated request grants them.
    - Use cautious execution approval, strict inline-evaluation controls, and loop detection where supported by the installed schema. Validate every setting against that schema before enabling it.
    - Implement and test:
        - `validate-execution-request.py` for schema, roots, grants, success criteria, and evidence paths.
        - `run-script-safe.ps1` for declared-root, script, executable, and exact-argument enforcement.
        - `git-safe.ps1` for status/diff/add/commit and `push origin main`.
    - Reject inline payloads, `python -c`, eval-style execution, undeclared executables, paths outside granted roots, unexpected branches/remotes, force push, hard reset, rebase/history rewrite, branch deletion, and remote modification.
    - Permit at most one bounded micro-fix attempt when the request explicitly grants the affected files and required tests.
5. **Validate capabilities and promote to persistence**
    
    - Create a dedicated Chrome profile named `APEX Executor`, manually authenticate the subscription providers, install the official extension, and grant only selected provider tabs. All-tabs access remains disabled unless separately approved.
    - Test harmless browser control first, then one trivial subscription prompt and verbatim capture. Add hostile-page fixtures proving page content cannot alter provider, hostname, workflow, paths, commands, tools, or result destination.
    - Test file/script execution with both positive and adversarial cases.
    - Test Git operations in a disposable repository before allowing a request-scoped commit and `push origin main` in the real repository.
    - Test both one-shot model-backed and exact-argv deterministic Cron jobs, restart persistence, attribution, history, and single-lane concurrency. Command jobs are operator-authorized because they run directly in the Gateway; they may contain only reviewed exact argv. Use the current [Cron CLI contract](https://docs.openclaw.ai/cli/cron).
    - Install the persistent Windows Gateway only after all foreground gates pass. Then run doctor, configuration validation, and a deep [security audit](https://docs.openclaw.ai/cli/security).
    - Increase context from 8K to 16K and then 32K while measuring memory, latency, tool-call reliability, and coexistence with the Gateway. Stop at the largest stable setting; 32K is a target, not permission to accept instability.
    - Run the first complete subscription vertical slice: validated request → browser submission → verbatim capture → verification prompt → deterministic receipt containing hashes, byte counts, timestamps, provider identity, request identity, and output paths.
    - Interrupt and restart at each critical stage to prove idempotency and prevent duplicate prompt submission or duplicate Git mutation.
    - Enable real recurring workflows only after restart/idempotency tests pass.
    - Finally reconcile older FEE documents and audit `scripts/fee`; migrate useful pieces before archiving or deleting anything.

## Verification and Acceptance

- Run existing FEE and LMBench test suites before and after repository changes.
- Add unit and adversarial tests for the request validator and both safety wrappers.
- Require all installation gates G0–G12 from the research plan, including:
    - structured tool calls directly and through both OpenClaw provider modes
    - one active Qwen inference lane
    - validated configuration and APEX-owned skills
    - selected-tab browser operation and provider containment
    - bounded files, scripts, tests, Git commit, and authorized push
    - denial of every prohibited Git, path, command, scheduling, and authority-widening action
    - immediate dispatch and both Cron modes
    - Gateway restart persistence and end-to-end idempotency
    - a complete subscription-site vertical slice with independently verifiable evidence
- Record commands, versions, configuration hashes, model hash, outcomes, failures, and deviations in a dated verification report under `FEE`.
- Commit and push at reviewable checkpoints directly to `main`; never stage unrelated workspace files.
- Installation is complete only when the executor performs the bounded vertical slice without becoming a workflow planner, evaluator, scheduler, or independent orchestration layer.