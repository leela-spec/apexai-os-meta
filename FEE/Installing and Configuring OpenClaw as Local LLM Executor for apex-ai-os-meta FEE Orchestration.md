# Installing and Configuring OpenClaw as Local LLM Executor for apex-ai-os-meta FEE Orchestration

## Overview

This report describes a resilient, evidence-backed setup of **OpenClaw** as the bounded local LLM executor for the Flow Execution Engine (FEE) program in the `apexai-os-meta` repository, aligned with the operator’s decision to select OpenClaw and install it as the runtime harness. It focuses on integrating OpenClaw with an already installed local Qwen3-8B model running under `llama.cpp`/Vulkan on port 8090, and wiring it into the orchestration flows and loops of the apex meta stack via the existing OpenClaw configuration and skill scaffolding under `apex-meta/openclaw`.[^1]

OpenClaw is treated here not as a generic chat assistant, but as a **local-first gateway and execution runtime** that can run agent turns, invoke tools, and act as the controlled executor behind FEE’s deterministic authority spine and subscription AI workflows. The configuration emphasizes:[^2][^3]

- Local-first model execution (no cloud dependency for executor turns).
- Strict authority separation between FEE (deterministic spine) and OpenClaw (bounded runtime executor).[^1]
- Robust configuration and observability for production-grade, repeatable behavior.[^4][^3]

## Source Context and Constraints

The FEE Phase-0 environment design and implementation handover documents explicitly state that:

- OpenClaw has been **selected** as the executor harness; installing it is now the active mission, superseding earlier constraints that forbade runtime installation in Phase-0.[^5][^1]
- A ready OpenClaw config exists at `apex-meta/openclaw/openclaw.json`, with the local provider and skill directory already wired.[^1]
- The executor skill exists at `apex-meta/openclaw/skills/apex-flow-executor/SKILL.md`.
- Qwen3-8B is installed as a local model candidate under `llama.cpp`/Vulkan, reachable at port 8090, with benchmark evidence but no certification.[^5][^1]

The operator locks and research synthesis emphasize:

- FEE as a four-layer system: subscription deep-reasoning AI, deterministic FEE authority spine, bounded local LLM execution runtime (OpenClaw/Hermes/Odysseus), and scarce CLI AI reviewers.[^1]
- Strong constraints on authority, evidence, and non-goals: FEE must not absorb planning authority; OpenClaw must be evidence-gated and hardened before broader use.[^1]

This report therefore assumes:

- The repository layout and decision locks described in the handover are authoritative for local design.[^1]
- The operator is working primarily on a single machine (likely Windows with WSL or Linux), with Qwen3-8B already installed and benchmarked.

## OpenClaw Architecture and Local LLM Role

### Gateway and Agent Runtime

OpenClaw’s official and community documentation describe it as a **gateway process** that runs on a machine you control and connects messaging channels (WhatsApp, Telegram, Discord, etc.) to AI agents. The core concepts include:[^3][^2]

- **Gateway**: long-lived process, exposes an HTTP UI (`http://127.0.0.1:18789` by default) and internal APIs.[^2][^4]
- **Agents**: configurable brains with models, tools, memory/workspace, and background behavior.[^4]
- **Providers / Models**: configuration for cloud or local backends (Anthropic, OpenAI, Ollama, vLLM, llama.cpp, etc.).[^6][^4]
- **Skills / Tools**: structured plugins invoked via tool calls (code execution, browser, automation, custom skills).[^3][^4]

In the FEE architecture, OpenClaw’s gateway and agent runtime serve as the **bounded execution layer** behind FEE:

- FEE assembles deterministic work packets, roots, and checkpoints.
- OpenClaw agent(s) run turns against a local LLM, invoke browser or automation tools, and capture evidence.
- FEE maintains the canonical traceability and authority; OpenClaw stays replaceable and runtime-scoped.[^1]

### Local LLM Backends

OpenClaw supports multiple local LLM backends, commonly through Ollama, vLLM, or direct HTTP APIs:[^7][^6]

- **Ollama**: fast setup, good for consumer hardware; exposes `http://localhost:11434` with a simple REST API.[^7][^6]
- **vLLM**: GPU-focused, scalable; exposes an OpenAI-compatible `/v1` endpoint.[^6]
- **llama.cpp**: minimal-dependency C++ runtime; often exposed via simple HTTP server or custom adapters.[^8][^6]

The FEE handover indicates a Qwen3-8B configuration via `llama.cpp`/Vulkan on port 8090, integrated into the existing benchmark and containment harness (`scripts/lmbench`). A key design choice is therefore whether OpenClaw points directly at this llama.cpp endpoint, or at an intermediate adapter (e.g., an OpenAI-compatible API wrapper or an Ollama-like server).[^5][^1]

### Role in apex-ai-os-meta Orchestration

The Phase-0 documents and backlog map FEE Workstream P3 ("Replaceable execution runtime OpenClaw/Hermes/Odysseus runtime mechanics") and Tasks 007–008 (install hardened OpenClaw composition, run Hermes comparison) as the bridge between the deterministic FEE spine and runtime executors. The integration pattern is:[^5]

- Use OpenClaw as the **runtime harness** for subscription/browser flows and bounded local LLM execution.[^1]
- Keep FEE’s canonical state (epic and task records, cockpit, traceability) in `apex-meta/local-orchestration-engine`.[^5]
- Implement an `apex-flow-executor` skill that translates FEE packets into OpenClaw agent tasks and returns evidence.

## Installation Strategy and High-Impact Options

### Option A: Node.js + npm Global Install (Recommended)

Several deployment guides for OpenClaw show installation via `npm install -g openclaw` after installing Node.js (often v22) on Linux. This path is well suited for an operator laptop with WSL or native Linux and integrates smoothly with CLI workflows.[^9][^8]

Baseline steps from community deployment guides:[^8]

```bash
# Install Node.js 22.x on Ubuntu/WSL
sudo apt-get update -y
sudo apt-get install -y ca-certificates curl gnupg
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt-get install -y nodejs
node -v && npm -v

# Install OpenClaw
npm install -g openclaw@latest

# Sanity check
openclaw --version
```

**Why this is recommended for apex-ai-os-meta:**

- Matches the Phase-0 environment’s emphasis on **file-based control**, Git, and Python/PowerShell automation; Node is an additive runtime that doesn’t conflict.[^5]
- Works smoothly under WSL with GPU passthrough for Ollama or llama.cpp, as demonstrated in local-LLM OpenClaw guides.[^10]
- Easier to script from FEE and `scripts/lmbench` compared to desktop-only installers.

### Option B: Shell Installer Script (Quick Start)

Official docs and quick-start guides show curl-based installers, e.g.:[^11][^2]

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
openclaw start
```

This path is faster but more opaque; for a controlled, evidence-driven environment like FEE, the Node.js + npm method offers clearer versioning and OS integration. This quick path can be used for throwaway experiments or separate sandboxes but is not recommended as the primary FEE runtime installation.

### Option C: Docker or Kubernetes

OpenClaw can be containerized and run on Kubernetes or Docker-based homelab setups, but the FEE handover emphasizes a single repository and laptop-focused deployment. Introducing containers adds complexity (volume mounts for workspace and logs, network policy, GPU drivers) that may conflict with the "Phase-0 before runtime" sequencing and anti-overengineering constraints. Containers are therefore treated as a **later horizon** option, not the initial FEE executor deployment.[^5][^1]

## Gateway Configuration for Local-First Operation

### Core Gateway Settings

Community security-focused guides show a hardened local gateway configuration, with loopback binding and explicit ports:[^8]

```json
{
  "gateway": {
    "mode": "local",
    "port": 18789,
    "bind": "loopback",
    "auth": { "mode": "none" },
    "controlUi": {
      "enabled": true,
      "basePath": "/openclaw",
      "dangerouslyDisableDeviceAuth": true
    }
  }
}
```

Key choices:

- **`bind: "loopback"`** keeps the gateway accessible only via `127.0.0.1`, avoiding remote exposure on Phase-0 machines.[^8]
- **`mode: "local"`** indicates this gateway is not a multi-tenant remote orchestrator but a single-operator local runtime.[^8]
- **Control UI enabled** simplifies observability and manual validation, though device auth should be hardened later for multi-user contexts.[^8]

For apex-ai-os-meta, the existing `apex-meta/openclaw/openclaw.json` should be aligned with these practices, ensuring the gateway:

- Runs only on loopback.
- Logs to a workspace under the repo or a dedicated local directory.
- Uses a port that does not conflict with Qwen’s `llama.cpp` server (e.g., OpenClaw at 18789, Qwen at 8090).[^8][^1]

### Agent Defaults and Workspace

OpenClaw documentation highlights a per-agent workspace and model configuration under `agents.defaults`.[^4]

Example from an architecture guide:[^8]

```json
{
  "agents": {
    "defaults": {
      "workspace": "/home/operator/openclaw-workspace",
      "model": { "primary": "openai/gpt-4o-mini" },
      "backgroundMs": 10000,
      "timeoutSec": 1800,
      "cleanupMs": 1800000
    }
  }
}
```

For FEE:

- Set `workspace` to a durable path on the operator machine, ideally under a non-repo directory to avoid mixing logs with Git-controlled files.
- Override `model.primary` to the local Qwen backend once wired.
- Consider shorter `timeoutSec` for bounded executor flows; long-running jobs may be delegated to separate horizons.

## Wiring OpenClaw to a Local LLM

### Recommended Path: Intermediate Adapter vs Direct llama.cpp

Local-model guides emphasize Ollama and vLLM as robust backends with clear APIs and context management. While llama.cpp can expose HTTP endpoints directly, several warnings apply:[^7][^6]

- Tool calling reliability can suffer when pointing OpenClaw at generic OpenAI-compatible endpoints implemented by local runtimes (e.g., Ollama’s `/v1` endpoint) without careful schema alignment.[^7]
- Context window limits and token-based truncation can silently break agent behavior if not configured consistently across OpenClaw and the backend.[^12]

Given that Qwen3-8B is already benchmarked under llama.cpp/Vulkan on 8090, two main options exist:

- **Option A (Recommended):** Wrap the existing Qwen llama.cpp runtime with a thin HTTP adapter that exposes a stable, OpenClaw-friendly API (either OpenAI-compatible or a custom local provider). This aligns with vLLM-style setups and allows better control over context length and tool schemas.[^6]
- **Option B:** Reinstall Qwen or a comparable model under Ollama and point OpenClaw directly at the Ollama endpoint (11434), using Ollama’s ecosystem and documented integration patterns.[^10][^6][^7]

Because FEE already has containment evidence and test fixtures based on the llama.cpp configuration, Option A preserves those investments while still giving OpenClaw a clean interface. Option B is attractive if Ollama’s ecosystem and GPU offload features are desired and the overhead of re-benchmarking under the new runtime is acceptable.[^10][^6]

### Example Configuration: Ollama Backend

OpenClaw community docs show a simple local backend config for Ollama:[^6]

```yaml
# ~/.openclaw/config.yml
brain:
  provider: "local"
  local:
    endpoint: "http://localhost:11434"
    model: "llama3.1:8b"
    type: "ollama"
```

Local-LLM setup guides for OpenClaw recommend:

- Installing Ollama via `curl`.[^7][^6]
- Pulling models that match hardware constraints (e.g., 8B for heartbeat, larger for complex reasoning).[^12][^6]
- Setting environment variables like `OLLAMA_KEEP_ALIVE=-1` and `OLLAMA_NUM_CTX` to keep models loaded and context windows sized appropriately for agent load.[^12][^6]

For apex-ai-os-meta, an Ollama-based integration is an alternative path if Qwen is reinstalled under Ollama or a different model is chosen for executor tasks. In that case, FEE’s benchmark portfolio and local-model decision locks must be updated to reflect the new runtime.[^5][^1]

### Example Configuration: vLLM/OpenAI-Compatible Backend

For vLLM or other OpenAI-compatible servers, the local backend configuration becomes:[^6]

```yaml
brain:
  provider: "local"
  local:
    endpoint: "http://localhost:8000/v1"
    model: "meta-llama/Llama-3.1-70B-Instruct"
    type: "openai-compatible"
```

This pattern can be reused if the Qwen3-8B llama.cpp server exports a `/v1` OpenAI-compatible endpoint. The vLLM-style integration is more robust than ad hoc HTTP calls because OpenClaw expects OpenAI-like semantics for models and tool calls.[^6]

## Integrating apex-flow-executor Skill

### Skill Concept and Location

The handover mentions an `apex-flow-executor` skill under `apex-meta/openclaw/skills/apex-flow-executor/SKILL.md`. In OpenClaw, skills are structured tools that the agent can discover and invoke via schema-valid tool calls. They typically define:[^1]

- A **name** and description.
- Input and output schemas (often JSON, with fields for packet IDs, actions, evidence paths).
- Execution logic that may call external programs, read/write files, or coordinate with other services.[^3][^4]

For FEE, the apex-flow-executor skill should:

- Accept FEE packet identifiers, canonical task IDs, and scope definitions (paths and forbidden writes) as inputs.
- Invoke deterministic scripts (e.g., `scripts/fee`, `scripts/lmbench`) or browser automation according to FEE’s constraints.
- Return structured evidence that the FEE traceability matrix can consume (paths, verdicts, timestamps).

### Skill Registration and Agent Wiring

OpenClaw’s skill system requires registering skill metadata and code under the gateway configuration or a skills directory. Typical steps include:[^4][^3]

1. Place skill definition files under a recognized skills directory (`~/.openclaw/skills` or repo-local path referenced by OpenClaw config).
2. Configure the gateway or agents to load the skill set at startup.
3. Expose skill names as available tools in the agent’s configuration.

For apex-ai-os-meta:

- Ensure `apex-meta/openclaw/openclaw.json` (or equivalent) includes the skills directory path pointing to `apex-meta/openclaw/skills`.
- Verify that `apex-flow-executor` appears in the agent’s tool list and is callable from a test prompt.
- Use Phase-0 test fixtures (e.g., T3/T7/T9/T11 hard gates) to validate that the skill respects containment, root permissions, and evidence capture.[^5]

## Security, Resilience, and Observability

### Local-First Security Practices

Security-focused OpenClaw documentation recommends:[^3][^8]

- **Loopback-only binding** (`bind: "loopback"`) to avoid external exposure on laptops.
- Minimal auth for single-operator setups, with device auth or API keys added later for multi-user environments.
- Clear separation between **workspace** (logs, evidence) and **codebase** (Git-managed files).
- Controlled use of powerful tools (exec, browser) with explicit allowlists and scopes.

For FEE:

- OpenClaw must not have blanket write access to the entire repo; apex-flow-executor should enforce path scopes that match FEE’s allowed writes.[^5][^1]
- Browser and subscription automation tools must respect operator gates and stop conditions (no live account changes in Phase-0).[^1]

### Resilience and Performance

Local-LLM OpenClaw guides highlight several resilience practices for GPU-backed runtimes:[^10][^7][^6]

- Auto-start and keep-alive for the LLM backend (Ollama or llama.cpp), ensuring models stay loaded between jobs.
- Context window tuning (e.g., `OLLAMA_NUM_CTX`) to avoid silent truncation that breaks agent behavior.[^12]
- Observability via the OpenClaw dashboard (logs, request traces), plus external monitoring of GPU/RAM usage.

For Qwen3-8B under llama.cpp:

- Use existing benchmark evidence to size jobs and concurrency; n1 trials show containment but not production reliability.[^1]
- Keep early executor flows narrow (single root, single job) to avoid overloading context windows and memory.

### Failure Modes and Safeguards

Potential failure modes include:

- Local LLM backend not running or unreachable.
- Context window exhaustion leading to truncated prompts and tool definitions.
- Skill-level bugs causing unintended writes or insufficient evidence capture.

Safeguards:

- Pre-flight checks in FEE before invoking OpenClaw (e.g., HTTP health checks for the backend, verifying model listing).[^7]
- Tool-call whitelists and schema validation in apex-flow-executor to block unapproved operations.[^3]
- Hard gates (e.g., QG-0–7) tied to OpenClaw’s behavior, enforcing zero successful unauthorized actions and independent evidence reconstruction.[^5]

## Step-by-Step Setup Instructions

### Step 1: Verify Repository and Qwen Runtime State

1. Confirm working in `apexai-os-meta` on `main`, as per Phase-0 constraints.[^5]
2. Verify Qwen3-8B llama.cppVulkan server is running on port 8090 and responding (e.g., via curl or existing `scripts/lmbench` tests).[^1]
3. Confirm existing OpenClaw scaffolding at `apex-meta/openclaw/openclaw.json` and `apex-meta/openclaw/skills/apex-flow-executor/SKILL.md` matches the handover.

### Step 2: Install Node.js and OpenClaw (Local Gateway)

1. On WSL or Linux:

```bash
sudo apt-get update -y
sudo apt-get install -y ca-certificates curl gnupg
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt-get install -y nodejs
node -v && npm -v
npm install -g openclaw@latest
openclaw --version
```

2. On macOS, use Homebrew or the official installer if preferred, but keep evidence of versions and commands used.[^11][^9]

### Step 3: Initialize Gateway and Base Config

1. Run the OpenClaw configuration wizard or onboarding command:

```bash
openclaw onboard
```

or non-interactively with local model placeholders.[^7]

2. Ensure the generated `openclaw.json` (or config YAML) uses:

- `gateway.mode` set to `local`.
- `gateway.bind` set to `loopback`.
- `gateway.port` set to a stable value (e.g., 18789).

3. Adapt the generated config to match the repo’s `apex-meta/openclaw/openclaw.json` structure, preserving the existing skills directory wiring.

### Step 4: Wire Gateway to Local LLM Backend

#### Path A: Direct llama.cpp Adapter (Aligned with Existing Qwen Runtime)

1. Implement or configure a small adapter that exposes Qwen3-8B llama.cppVulkan on port 8090 via an OpenAI-compatible `/v1` endpoint.
2. Configure OpenClaw’s local backend in `config.yml` or `openclaw.json`:

```yaml
brain:
  provider: "local"
  local:
    endpoint: "http://localhost:8090/v1"
    model: "qwen3-8b-local"
    type: "openai-compatible"
```

3. Validate with a simple prompt via OpenClaw’s chat UI or CLI, ensuring responses originate from Qwen and tool calls (if any) remain schema-valid.

#### Path B: Reinstall Qwen Under Ollama (Alternative)

1. Install Ollama on the same machine.[^6][^7]

```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull qwen2.5:7b
```

2. Set environment variables for keep-alive and context windows:[^12][^6]

```bash
export OLLAMA_KEEP_ALIVE=-1
export OLLAMA_NUM_CTX=24576
```

3. Configure OpenClaw local backend to point at Ollama:[^6]

```yaml
brain:
  provider: "local"
  local:
    endpoint: "http://localhost:11434"
    model: "ollama/qwen2.5:7b"
    type: "ollama"
```

4. Re-run FEE’s local-model benchmark portfolio under this new runtime to re-establish containment and reliability evidence.[^5][^1]

### Step 5: Register and Validate apex-flow-executor Skill

1. Ensure `apex-meta/openclaw/skills/apex-flow-executor/SKILL.md` defines a structured tool with clear input/output schemas aligned with FEE packets and evidence indexing.[^1]
2. Update OpenClaw’s config to include the skills directory and apex-flow-executor in the agent’s tool list.[^4][^3]
3. Run minimal integration tests:

- Invoke apex-flow-executor with a non-destructive FEE packet (e.g., a read-only status query).
- Verify that the tool call is logged, evidence is recorded, and no forbidden writes occur.

### Step 6: Harden Security and Observability

1. Verify gateway binding and auth:

- Confirm `bind: "loopback"` and that no external interface exposes the UI.[^8]
- Use minimal auth for Phase-0 (no multi-user tokens), but record any deviations in the evidence index.

2. Configure logging:

- Direct OpenClaw logs to a dedicated workspace path.
- Integrate log sampling or summaries into FEE’s evidence index for traceability.[^3][^5]

3. Monitor resource usage:

- Use OS tools (e.g., `top`, `nvidia-smi`) to monitor Qwen’s runtime footprint and ensure the gateway does not starve other processes.[^10][^1]

### Step 7: Run Phase-0 Validation Gates for OpenClaw

1. Use T3/T7/T9/T11 hard gates (hostile content, multi-root permissions, resume behavior, evidence reconstruction) to validate OpenClaw’s behavior as an executor.[^5]
2. Record outcomes in the traceability matrix and quality gates files (`apex-meta/local-orchestration-engine/project/07-TRACEABILITY-MATRIX.md`, `08-QUALITY-GATES.md`).[^5]
3. Ensure QG-0 (traceable scope and evidence) and QG-1 (zero successful unauthorized actions) hold under OpenClaw-driven flows.[^5]

## Configuration Choices and Alternatives

### Gateway Binding and Auth

- **Chosen:** `bind: "loopback"`, `mode: "local"`, minimal auth for single-operator use.[^8]
- **Alternative:** Remote gateway with device auth and Tailscale-based access (useful for multi-device setups).[^3]

For FEE Phase-0 on a single laptop, loopback-only is safer and sufficient; remote access can be introduced in later horizons once Phase-0 benchmarks and controls are stable.[^5]

### Local LLM Backend

- **Chosen (Recommended):** Adapter around existing Qwen3-8B llama.cppVulkan runtime, exposing an OpenAI-compatible endpoint for OpenClaw.[^6]
- **Alternative 1:** Ollama-based Qwen or other models, leveraging community tools and GPU optimizations.[^10][^7][^6]
- **Alternative 2:** vLLM-based high-end models (e.g., Llama-3.1 70B) for more demanding tasks.[^6]

The adapter path preserves existing benchmark evidence and local-model locks, while Ollama or vLLM may be preferable if FEE evolves toward heavier coding workflows or multi-model bake-offs.[^1]

### Skill Integration Strategy

- **Chosen:** apex-flow-executor as a single, well-scoped skill that mediates all FEE-to-OpenClaw interactions.
- **Alternative:** Multiple skills for different workstreams (e.g., separate skills for Detective evidence, hygiene tasks, coding micro-fixes).

Starting with a single executor skill simplifies traceability and reduces complexity; additional skills can be added once Phase-0 proves the pattern.[^5]

## Conclusion

The recommended setup treats OpenClaw as a **local-first, replaceable executor** behind the FEE authority spine, wired to an already installed Qwen3-8B local model via a controlled adapter or an Ollama/VLLM backend. By installing OpenClaw via Node.js/npm, hardening the gateway configuration, wiring the apex-flow-executor skill, and validating behavior against Phase-0 gates, the operator can achieve a resilient, evidence-backed runtime that aligns with the apex meta design and non-goals.[^6][^8][^1][^5]

Future work includes Hermes comparisons, broader workflow integrations (Weekly and Multi-Agent), and production-readiness decisions, all tracing back to the same OpenClaw-based executor harness and FEE-controlled authority ladder.[^1][^5]

---

## References

1. [HANDOVER-2026-08-10-FEE-PROJECT-ENVIRONMENT-2.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/e89e7901-9dd5-4020-b57e-d902883e4e02/HANDOVER-2026-08-10-FEE-PROJECT-ENVIRONMENT-2.md?AWSAccessKeyId=ASIA2F3EMEYERLOQVXM3&Signature=EYY6dYM%2FuKYRB%2FrmVpRSrj6e1UU%3D&x-amz-security-token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIH9aNmPpAfCV2KXsIdQO7l4SH70xvo1l2JJxjdJ0piO1AiEA6D6S8Tsi%2Bg6ajxXSWNPRYuMZM8jBLU1TAzYjKQgl8TIq%2FAQIoP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDObv93sTVeM9Pws62CrQBLpD5%2Btm5mHVlBdBIrk0eR%2FrCbd1zeica7LuHhwqsV0yUa0RxTA0mUNVacn3fBYOSM7Zy2ua4m1YranCCGQypG8njF1F%2F7oKw0zjXkihT0hvETTOQ4HDillsjmmtSGDGoJVd%2F%2FPl2gwAH1w4Tn5o0sYM3qYwszftxQkXLQrbuC6w1QaOAraGN19saQjiEG%2FsQxEaMyZ8RyBLQJf2Q6jAP%2F6VKJXyHls5gIPZ4YXJcncsLivJnkEN4taJhMpJfp5rG8P%2F2TLsqrVWXV4O0x%2FENElwH704u50%2Bj%2F8GWwbYZrcTzXVvIyqfypdJUZkK0jHj0IfPm6StmK1q5OxVvE5RSRhkn2un9A2Kaab7zdn6oxpC3XaIW3kffhw5A1qkVan2VEP16n02IZPM%2BWqYX%2FyUl%2F4b%2F%2BZC3aGGuKUrrbiiMaNnHcv1YbcXGREfwyJe65PA7YRgCaIoNGP0kVnm%2FWEzN3QajYYQuA6WmCt4oJDOkboN0GBPVOt1ko0FH5VA7fIdOvMR5z%2BFoiOmuYnVcY0w6rWfv1TrvtVgeXXagV11iVmKy8G959zca%2B0e%2BStHg5Zi%2BTulo1TleCnY6XV6i82Af5Nya4WLSmsPBdJV3q8Gp1X2UC2KQ2lgdIy6fxJzunQmGMCRHU%2Fx2wyq2R62giE%2FmwRv%2FFYl19jM9OgA%2FtmEhxhhoHtdJJrSFm5H6%2F5%2B2IKIO%2BvWTrfc96BkBtbsPBlomrfG%2FGUf6dI8%2BvQoAX83MJob8MAF%2FUaTf3ITmPVVrFA7ICTXQftk%2Bk2QBjoAEXmtCwUw%2Bdfn0wY6mAFm%2BPYY0%2BkWhUPGfsJwb1eOy7JN9%2FD1xm3F5fC5vgH7H0LKMQsh2vYqRqlgtDtIX1d%2BQqnXvefaF1R%2F2HRuESDCyWGpc5u7tYsVTm68uub7MZLkACfOdeVySA4aiWhPc9D4lCczARJvOisw9RarblX1dHjxemZv0Z0KiWKKgGOnDs%2BleK3ihztyznMeEr1J8EuBSHglP8p3Lw%3D%3D&Expires=1786378700) - --- title Handover Build the FEE Phase-0 Project Environment doctype implementationhandover initiati...

2. [OpenClaw Docs](https://docs.openclaw.ai/) - OpenClaw is a self-hosted gateway that connects your favorite chat apps — Discord, Google Chat, iMes...

3. [GitHub - centminmod/explain-openclaw: Multi-AI documentation for ...](https://github.com/centminmod/explain-openclaw) - Multi-AI documentation for OpenClaw: architecture, security audits, deployment guide - centminmod/ex...

4. [Documentation – OpenClaw - Open Source AI Coding Assistant](https://openclawlab.com/en/docs/) - Complete OpenClaw documentation, from quick start to advanced configuration

5. [2026-08-10-fee-project-environment-implementation-plan-3.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/92f69a32-8aab-49a7-a4fb-8fe958711717/2026-08-10-fee-project-environment-implementation-plan-3.md?AWSAccessKeyId=ASIA2F3EMEYERLOQVXM3&Signature=YRnmEyAWzxq%2BCZSmVUp8PmtgUSo%3D&x-amz-security-token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIH9aNmPpAfCV2KXsIdQO7l4SH70xvo1l2JJxjdJ0piO1AiEA6D6S8Tsi%2Bg6ajxXSWNPRYuMZM8jBLU1TAzYjKQgl8TIq%2FAQIoP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDObv93sTVeM9Pws62CrQBLpD5%2Btm5mHVlBdBIrk0eR%2FrCbd1zeica7LuHhwqsV0yUa0RxTA0mUNVacn3fBYOSM7Zy2ua4m1YranCCGQypG8njF1F%2F7oKw0zjXkihT0hvETTOQ4HDillsjmmtSGDGoJVd%2F%2FPl2gwAH1w4Tn5o0sYM3qYwszftxQkXLQrbuC6w1QaOAraGN19saQjiEG%2FsQxEaMyZ8RyBLQJf2Q6jAP%2F6VKJXyHls5gIPZ4YXJcncsLivJnkEN4taJhMpJfp5rG8P%2F2TLsqrVWXV4O0x%2FENElwH704u50%2Bj%2F8GWwbYZrcTzXVvIyqfypdJUZkK0jHj0IfPm6StmK1q5OxVvE5RSRhkn2un9A2Kaab7zdn6oxpC3XaIW3kffhw5A1qkVan2VEP16n02IZPM%2BWqYX%2FyUl%2F4b%2F%2BZC3aGGuKUrrbiiMaNnHcv1YbcXGREfwyJe65PA7YRgCaIoNGP0kVnm%2FWEzN3QajYYQuA6WmCt4oJDOkboN0GBPVOt1ko0FH5VA7fIdOvMR5z%2BFoiOmuYnVcY0w6rWfv1TrvtVgeXXagV11iVmKy8G959zca%2B0e%2BStHg5Zi%2BTulo1TleCnY6XV6i82Af5Nya4WLSmsPBdJV3q8Gp1X2UC2KQ2lgdIy6fxJzunQmGMCRHU%2Fx2wyq2R62giE%2FmwRv%2FFYl19jM9OgA%2FtmEhxhhoHtdJJrSFm5H6%2F5%2B2IKIO%2BvWTrfc96BkBtbsPBlomrfG%2FGUf6dI8%2BvQoAX83MJob8MAF%2FUaTf3ITmPVVrFA7ICTXQftk%2Bk2QBjoAEXmtCwUw%2Bdfn0wY6mAFm%2BPYY0%2BkWhUPGfsJwb1eOy7JN9%2FD1xm3F5fC5vgH7H0LKMQsh2vYqRqlgtDtIX1d%2BQqnXvefaF1R%2F2HRuESDCyWGpc5u7tYsVTm68uub7MZLkACfOdeVySA4aiWhPc9D4lCczARJvOisw9RarblX1dHjxemZv0Z0KiWKKgGOnDs%2BleK3ihztyznMeEr1J8EuBSHglP8p3Lw%3D%3D&Expires=1786378700) - For agentic workers REQUIRED SUB-SKILL Use superpowerssubagent-driven-development recommended or sup...

6. [Local Models - OpenClaw Docs](http://clawdocs.org/guides/local-models/) - Run OpenClaw with local LLMs via Ollama or vLLM — zero API costs, full privacy

7. [How to Run OpenClaw with a Local LLM: Complete Ollama Setup ...](https://doneclaw.com/blog/how-to-run-openclaw-with-a-local-llm-complete-ollama-setup-guide-2026/) - Learn how to run OpenClaw with a local LLM using Ollama. This complete 2026 guide covers setup, mode...

8. [How to Build a Secure Local-First Agent Runtime with OpenClaw ...](https://www.marktechpost.com/2026/04/11/how-to-build-a-secure-local-first-agent-runtime-with-openclaw-gateway-skills-and-controlled-tool-execution/) - How to Build a Secure Local-First Agent Runtime with OpenClaw Gateway, Skills, and Controlled Tool E...

9. [OpenClaw Docs — API, CLI, Config & Self-Host Reference ...](https://openclaw-ai.net/en/docs) - OpenClaw official documentation — REST & WebSocket API, CLI commands, config options, skill SDK, and...

10. [How to Run OpenClaw on a Local LLM Using Your GPU](https://www.youtube.com/watch?v=82TrKuAl7Ic) - 🇺🇸 America 250 / July 4 sale is live through July 6: 17.76% off sitewide, no code needed. Sale page:...

11. [Home | OpenClaw Docs — Community Documentation for the Open ...](https://clawdocs.org/) - Install OpenClaw, connect a channel, and start chatting with your AI agent. The Quick Start guide ge...

12. [OpenClaw + Ollama: Local LLM Setup (2026)](https://kaxo.io/insights/openclaw-ollama-local-llm-guide/) - OpenClaw local LLM documentation: Ollama setup, real GPU benchmarks, the context-window trap that br...

