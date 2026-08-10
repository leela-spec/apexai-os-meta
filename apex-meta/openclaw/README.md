# OpenClaw — APEX executor harness

**What this folder is.** The configuration and skills for running a **bounded local LLM under OpenClaw** as the executor of pre-written APEX prompts on subscription AI surfaces. Nothing else.

**Status:** OpenClaw `2026.7.1-2`, the protected runtime, Qwen3-8B, the official Chrome extension, and the APEX browser-policy plugin are installed as of 2026-08-10. The bounded subscription-site vertical slice remains the promotion gate; see the dated FEE verification report.

## The one job

```text
reasoning model (subscription)      writes the prompt + the verification prompt
        |
        v
OpenClaw + bounded local LLM        opens the signed-in Chrome tab
                                    pastes the prompt exactly
                                    waits · captures verbatim · saves to the repo
                                    submits the verification prompt
                                    reports a capture receipt
        |
        v
reasoning model (subscription)      evaluates the result
```

The executor is a **copy-paster with a browser**. It replaces the operator and the scarce CLI agents at the clicking and pasting, and nothing more.

**It does not run the repo's skills.** `PrecapWeek`, `PrecapNextDay`, `flow-recap`, `status-merge`, `AIRouting` and the rest of `.claude/skills/` stay with the reasoning and CLI models. The executor never plans, routes, judges, or touches code.

## Why OpenClaw rather than Hermes

Hermes routes through Docker. On a single laptop that is unnecessary weight for what amounts to browser operation. OpenClaw needs no container, drives the operator's **already signed-in Chrome tabs** through an official extension, carries per-agent persistent memory, and loads skills as plain `SKILL.md`.

Prior research in `apex-meta/local-orchestration-engine/research-results/` that assumed a Hetzner server and ranked Hermes as a co-candidate is **superseded** — the operator's machine changed and the runtime choice with it.

## What OpenClaw supplies

Verified against the official documentation on 2026-08-10.

| Capability | Detail |
|---|---|
| Signed-in Chrome control | *"lets an agent control your signed-in Chrome tabs without launching a separate managed browser"* |
| Containment | Two access modes. In **selected tabs**, *"group membership is the access-control boundary"*, plus per-tab pause |
| Local model | JSON5 `models.providers.<name>` with `baseUrl`, `apiKey`, `api`. Any OpenAI-style `/v1/chat/completions` endpoint works |
| Skills | `SKILL.md` with YAML frontmatter; discovered up to 6 levels deep under configured roots; compiled into a compact XML block in the system prompt |
| Memory | Per-agent workspace files: `USER.md`, `MEMORY.md`, `memory/YYYY-MM-DD.md`, `DREAMS.md` |
| Learning | *"useful material from daily notes is distilled into MEMORY.md by the default dreaming sweep"* |
| Scheduling | Built-in Automations (`openclaw automations`, formerly `cron`) |

## Constraints that shape the design

**Page sharing is capped at ~120,000 characters.** A hard bound on capturing long deep-research output. The skill must report captured length and flag proximity to the cap.

**OpenClaw's own warning about small quantized models.** Its docs say to run *"the largest / full-size variant you can host — small or heavily quantized checkpoints raise prompt-injection risk"*, and suggest *"2+ maxed-out Mac Studios or an equivalent GPU rig (~$30k+) for a comfortable agent loop."* The operator runs Qwen3-8B `Q4_K_M` on integrated graphics — squarely the configuration warned about.

That risk was independently observed in this repo's own benchmark: fixture `MA-05-16` had the model obey an injected instruction inside untrusted content after two explicit warnings, recorded as `hard_gate_violation: false` because a broker can deny a tool call but cannot see a steered output. See [`RE-ANALYSIS-QWEN3-8B-N1-2026-08-10-ADVERSARIAL.md`](../local-orchestration-engine/benchmark/results/RE-ANALYSIS-QWEN3-8B-N1-2026-08-10-ADVERSARIAL.md) §3.

**The mitigation is the architecture, and it is OpenClaw's own recommendation** — *"keep agents narrow and compaction on to limit prompt-injection blast radius."* A copy-paster whose action set contains no delete, no shell, no cross-root write, confined by Chrome tab-group membership, has a small blast radius by construction. This is why the executor is deliberately not given the repo's skills.

**The residual risk is fidelity, not authority.** A narrow executor cannot do damage; it can produce a quietly wrong artifact — a paraphrase instead of a verbatim copy, a partial capture reported as complete. Benchmark fixture `MA-06` showed exactly that: instructed to record ~210 bytes verbatim, the model paraphrased. So the capture receipt reports byte counts, and **verification is done by deterministic code, not by the model that produced the capture.**

## Third-party skills

ClawHub has community skills covering ChatGPT web automation. OpenClaw's guidance is to treat third-party skills as **untrusted code** and review before enabling. The executor skill here is deliberately first-party for that reason, and because the prompt handling and stop conditions must match the APEX contract rather than a community author's assumptions.

## Contents

| Path | Role |
|---|---|
| [`skills/apex-flow-executor/SKILL.md`](skills/apex-flow-executor/SKILL.md) | The executor skill. Its body is the `BAO-001`..`BAO-013` runbook turned into operational instructions |
| [`INSTALL-AND-VERIFY.md`](INSTALL-AND-VERIFY.md) | The Claude Code task: install, wire the local model, and verify the four things that could invalidate this design |

## Related

- [`apex-meta/SmallSkills/AI-Browser-Orchestration/`](../SmallSkills/AI-Browser-Orchestration/) — the 13 empirical `BAO` rules this skill encodes
- [`.claude/skills/PrecapNextDay/references/flow-prompt-pack-contract.md`](../../.claude/skills/PrecapNextDay/references/flow-prompt-pack-contract.md) — defines `artifacts/flow-packets/<YYYYMMDD>/prompt-packs/bodies/<packet_id>.md`, the executor's input. **No such file has ever been written.**
- [`apex-meta/local-orchestration-engine/project/`](../local-orchestration-engine/project/) — FEE project environment. FEE is the deterministic guard around this executor, not a replacement for it.
