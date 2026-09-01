Yes. I think the architecture should change.

The web research supports a much simpler pattern than what we built:

> **Hermes should own its execution environment and bootstrap its own project tools inside that environment.**
> 
> Antigravity should disappear completely from the operational path.

Hermes' own documentation explicitly supports this. With the Docker terminal backend, Hermes uses a long-lived sandbox; installed packages and filesystem changes survive across tool calls and sessions, and Hermes' docs specifically recommend letting Hermes install Python/npm tools itself and installing `apt` packages inside the sandbox when needed. ([Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/docker?utm_source=chatgpt.com "Docker | Hermes Agent"))

## The architecture I now recommend

```text
YOU
 │
 ▼
HERMES
 │
 ├── owns task/orchestration state
 │
 ├── owns its Docker execution sandbox
 │
 ├── sees /root/MasterOfArts as /workspace
 │
 ├── checks required tools
 │
 ├── installs missing tools itself
 │
 ├── records exact versions
 │
 └── executes deterministic G1 scripts
          │
          ▼
      G1 artifacts
          │
          ▼
       YOU review
```

**Remove entirely:**

```text
Antigravity
   ↓
build environment
   ↓
explain environment to Hermes
   ↓
Hermes tries to understand foreign setup
```

That transfer boundary is producing exactly the coordination failure you identified.

---

# What Hermes upstream actually recommends

The official Hermes Docker documentation has a section specifically called **“Installing more tools in the container.”** It recommends several levels. For Python/npm software it recommends `uvx`/`npx`; for OS packages it explicitly says to instruct Hermes to install packages such as with `apt-get`, and to remember the installation command. Installed tools persist for the container lifetime. ([Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/docker?utm_source=chatgpt.com "Docker | Hermes Agent"))

For the Docker terminal backend, Hermes runs one persistent sandbox and routes terminal, file, and code execution through it. Packages installed once remain available on subsequent calls. ([Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/tools?utm_source=chatgpt.com "Tools & Toolsets | Hermes Agent"))

Hermes also supports persistent Docker state across processes and sessions through:

```yaml
container_persistent: true
docker_persist_across_processes: true
```

and explicitly documents that installed packages, files, working state and background processes can survive between Hermes invocations. ([Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/configuration?utm_source=chatgpt.com "Configuration | Hermes Agent"))

So **Hermes self-installing dependencies is not a workaround. It is a documented Hermes workflow.**

---

# But one important correction

I would **not** tell Hermes:

> “Figure out how to install Pandoc, Poppler and docx2python.”

That recreates the AI-improvisation problem.

Instead:

```text
Hermes owns installation
        ≠
Hermes invents installation
```

We give Hermes one deterministic project bootstrap:

```text
ensure-g1-tools
```

Hermes executes that command itself.

The bootstrap is idempotent:

```text
check Python
check docx2python
check Pandoc
check pdftotext
check pdftoppm
        │
        ├── everything correct → continue
        │
        └── missing → install exact required dependency
                              │
                              ▼
                         verify version
                              │
                              ▼
                           continue
```

This gives us **one AI, one environment, one procedure**.

---

# Where each thing should live

I recommend this instead of the custom Docker image:

|Component|Location|Owner|
|---|---|---|
|Hermes|WSL host|Hermes installation|
|Hermes sandbox|default Hermes Docker backend|Hermes|
|Repo|`/root/MasterOfArts`|Git|
|Repo inside sandbox|`/workspace`|Hermes Docker mount|
|Python G1 environment|persistent sandbox, e.g. `/root/.lhtl-g1-venv`|Hermes|
|`docx2python`|that Python venv|Hermes bootstrap|
|Pandoc|`/usr/bin/pandoc` in Hermes sandbox|Hermes bootstrap|
|Poppler|`/usr/bin/pdftotext`, `/usr/bin/pdftoppm`|Hermes bootstrap|
|extraction scripts|repository `tooling/g1/`|Git/project truth|
|install/bootstrap script|repository `tooling/g1/bootstrap.sh`|Git/project truth|
|exact package pins|repository `requirements.lock`|Git/project truth|
|results|repository `g1-extraction/`|deterministic pipeline|

This is much cleaner.

---

# First fix: Hermes must see the repository

The G0.3 failure was even more basic than package installation: `/workspace` was empty.

Hermes documentation says the Docker sandbox **does not mount the launch directory by default**. You either explicitly configure `docker_volumes`, or enable `docker_mount_cwd_to_workspace`. ([Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/configuration/?utm_source=chatgpt.com "Configuration | Hermes Agent"))

For this project I prefer an **explicit volume**, because it removes dependence on wherever Hermes happened to be launched:

```yaml
terminal:
  backend: docker
  docker_image: "nikolaik/python-nodejs:python3.11-nodejs20"

  docker_volumes:
    - "/root/MasterOfArts:/workspace"

  container_persistent: true
  docker_persist_across_processes: true

  docker_run_as_host_user: false
```

Why `docker_run_as_host_user: false`?

Because Hermes' own documentation says that running the container as the host UID prevents `apt install`; the default root container mode is appropriate when the sandbox needs to install OS packages. ([Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/configuration/?utm_source=chatgpt.com "Configuration | Hermes Agent"))

And `/root/MasterOfArts` is not a new guess: that is the operational repository recorded by the original Hermes installation, and its accepted Docker design already mapped that repository to `/workspace`.

---

# Then Hermes installs its own tools

Inside the actual Hermes terminal sandbox, Hermes can perform something equivalent to:

```bash
apt-get update

apt-get install -y --no-install-recommends \
  pandoc \
  poppler-utils \
  zip \
  unzip
```

Hermes' own documentation specifically presents `apt-get ... install` as the normal way for the agent to add non-Python/npm tools to its Docker environment. ([Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/docker?utm_source=chatgpt.com "Docker | Hermes Agent"))

For `docx2python`, I would **not contaminate the system Python**.

Hermes should create its own persistent G1 Python environment:

```bash
python3 -m venv /root/.lhtl-g1-venv

/root/.lhtl-g1-venv/bin/pip install \
  -r "/workspace/LHTL/Learning LHTL Framework/learning-framework-2026/tooling/g1/requirements.lock"
```

Then our canonical Python command becomes:

```bash
/root/.lhtl-g1-venv/bin/python
```

rather than whichever Python happens to be on `PATH`.

That gives us:

```text
Hermes sandbox
│
├── /usr/bin/pandoc
├── /usr/bin/pdftotext
├── /usr/bin/pdftoppm
│
└── /root/.lhtl-g1-venv/
      ├── python
      └── docx2python
```

Everything is physically inside **Hermes' own execution environment**.

No handover.

---

# And installation becomes self-healing

The project should contain something like:

```text
tooling/g1/
├── bootstrap.sh
├── verify-environment.py
├── requirements.lock
├── scripts/
│   ├── run_g1.py
│   └── validate_g1.py
└── tests/
```

Then every relevant Hermes task starts with:

```bash
bash tooling/g1/bootstrap.sh
```

The script does:

```text
1. Verify /workspace is MasterOfArts
2. Verify expected source files exist

3. If Pandoc absent:
      apt install it

4. If Poppler absent:
      apt install it

5. If G1 Python venv absent:
      create it

6. Install/repair exact pinned Python packages

7. Print exact versions

8. Run deterministic smoke tests

9. PASS or exit non-zero
```

This is the key improvement.

If Docker gets recreated three months from now:

```text
Hermes starts
   ↓
bootstrap.sh
   ↓
"tools disappeared"
   ↓
Hermes installs them again itself
   ↓
verified
   ↓
continue
```

No Antigravity. No human archaeology. No “who installed what where?”

---

# Why I would not switch Hermes to `local`

Hermes also supports:

```yaml
terminal:
  backend: local
```

and then it could install everything directly in WSL. ([GitHub](https://github.com/openax-reference/nousresearch-hermes-agent/blob/main/website/docs/user-guide/configuration.md?utm_source=chatgpt.com "nousresearch-hermes-agent/website/docs/user-guide/configuration.md at main · openax-reference/nousresearch-hermes-agent · GitHub"))

That is even simpler technically.

I **wouldn't choose it yet**, because it throws away the useful security boundary we already intentionally established. Hermes' documentation describes Docker as the sandboxed choice and `local` as giving the agent the same filesystem access as the host user. ([Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/configuration/?utm_source=chatgpt.com "Configuration | Hermes Agent"))

The Docker design isn't what failed.

What failed was:

```text
custom foreign image
+
second AI
+
second repo path
+
launcher override
+
handover contract
+
Hermes sandbox reuse
```

We can remove all of that while keeping Docker.

---

# What happens to the Antigravity work?

I would demote it to **non-authoritative implementation history**.

We can reuse useful deterministic code it produced:

```text
run_g1.py
validate_g1.py
requirements.lock
tests
```

But these become simply **project code that Hermes owns and executes**.

The following concepts should disappear from the live architecture:

```text
Antigravity provisioner
moa-lhtl-g1-tools custom runtime requirement
Antigravity → Hermes capability handover
G0.2 Antigravity provisioning gate
G0.3 Hermes acknowledgement of Antigravity environment
project-specific Hermes launcher
```

Instead:

```text
G0.2 — Hermes execution bootstrap
        ↓
Hermes mounts repo
        ↓
Hermes installs its own dependencies
        ↓
Hermes validates its own environment
        ↓
operator review
        ↓
G1
```

Much better.

---

# One nuance from the official docs

Hermes upstream says that for **constantly used tools**, the most durable option is still a derived Docker image. ([Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/docker?utm_source=chatgpt.com "Docker | Hermes Agent"))

So there is a tradeoff:

|Model|Simplicity|Reproducibility|Transfer risk|
|---|--:|--:|--:|
|Antigravity builds custom image|poor|excellent|**high**|
|Hermes self-installs into persistent sandbox|**excellent**|good with pinned bootstrap|**none**|
|Hermes itself builds its own derived image|medium|excellent|none|

For this project I choose the **middle option**.

If later we discover that rebuilding Pandoc/Poppler after container recreation is actually annoying, **Hermes itself** can eventually promote its proven bootstrap into a derived image. But only after Hermes understands and successfully operates the pipeline.

That preserves the single-agent ownership you want.

---

## Recommended next move

**Do not send anything else to Antigravity.**

We should now change the repository architecture from:

```text
Antigravity provisions → Hermes acknowledges
```

to:

```text
Hermes bootstraps → Hermes verifies → Hermes executes
```

Then there is one tiny **operator-side bootstrap** that fixes Hermes' host configuration so `/root/MasterOfArts` is mounted into its sandbox. After that, Hermes can perform the entire installation and validation itself.

If you want, I can now **patch the project files in GitHub to remove Antigravity from the architecture and create the exact Hermes self-bootstrap specification/instruction you can paste directly into Hermes.**