# R01 — Hermes Local Safety Guardrails — Work Result

**Research date:** 2026-08-23  
**Repository baseline:** `leela-spec/MasterOfArts@52c8ba0d7692e83891cd281f0525ffcabbd353fd`  
**Track status:** **PASS**  
**Verdict:** `SAFETY_PROFILE_CONFIRMED`

## Executive decision

Use Hermes in **WSL2 on Windows**, with the MasterOfArts checkout and Hermes/QMD runtime in the same WSL filesystem. The normal profile is local-terminal execution with `approvals.mode: smart`, an explicit hard deny list, `HERMES_WRITE_SAFE_ROOT` limited to the repository plus the Hermes profile home, checkpoints enabled, no environment forwarding to containers/MCP beyond named variables, and every gateway/dashboard/QMD listener bound to loopback with explicit user allowlists or pairing.

This is the lowest-friction official profile that still meaningfully reduces honest-but-wrong agent risk. It does not turn terminal execution into a sandbox: Hermes' own documentation states that write-tool path controls are defense in depth and a shell command can bypass them. Use the official Docker backend, with the documented hardening controls, for untrusted skills or command-heavy tasks that do not require seamless host operation. Do not use `approvals.mode: off` for Master of Arts work.

## Plain-language threat model

The protected assets are the private repository, credentials available to the operator account, unrelated host files, the integrity of approved BMAD/MarketingSkills packages, private client/financial/therapy material, and the operator's ability to recover work. The expected actor is an authorized operator using a generally helpful but fallible agent. Credible failures are: a destructive command, writing outside the intended project, credential discovery or egress, prompt injection in a repository/context/skill file, unsafe third-party skill code, an exposed messaging or web endpoint, resource exhaustion, and a mistaken bulk edit. A hostile remote user becomes relevant only when gateway/messaging is enabled.

Hermes provides layered controls, not a single security boundary. Approvals and deny rules constrain tool use; path controls constrain Hermes write tools; Docker/SSH provide stronger process isolation; allowlists constrain remote users; checkpoints improve recovery. None of these makes the cloud model local: task prompts and returned passages go to the configured model provider.

## Official-control matrix

| Control | Verified behavior | Covers | Does not cover | State |
|---|---|---|---|---|
| Smart approvals | Auxiliary risk assessment; dangerous commands may be denied and uncertain commands escalated | Accidental risky shell/tool actions | Perfect detection; malicious instructions | `VERIFIED_OFFICIAL` |
| Manual approvals | Prompts on flagged actions | Maximum operator visibility | Low-friction autonomy | `VERIFIED_OFFICIAL` |
| Approval off | Removes normal approval friction | Nothing security-positive | Host safety | `VERIFIED_OFFICIAL`; rejected |
| Hardline blocklist | Blocks catastrophic root wipe, fork bomb, raw disk and similar patterns | Obvious catastrophic commands | Novel or indirect destructive commands | `VERIFIED_OFFICIAL` |
| `approvals.deny` | Glob rules remain hard blocks, including in yolo/off mode | Known forbidden command families | Commands omitted from rules | `VERIFIED_OFFICIAL` |
| `HERMES_WRITE_SAFE_ROOT` | Restricts write-file/patch tools to one or multiple roots | Accidental file-tool writes | Shell redirection/subprocess writes | `VERIFIED_OFFICIAL` |
| Checkpoints | Opt-in shadow-git snapshots before writes/destructive actions; `/rollback` recovery | Mistaken edits | Secrets egress; non-file side effects | `VERIFIED_OFFICIAL` |
| Docker backend | Container boundary, caps/resources/no-new-privileges options, explicit env forwarding | Host filesystem/process exposure | Provider egress; deliberately mounted data; dangerous-check bypass inside container | `VERIFIED_OFFICIAL` |
| Gateway allowlist/pairing | Default-deny user admission when configured | Unauthorized remote control | Authorized-user mistakes | `VERIFIED_OFFICIAL` |
| MCP env filtering | Safe system variables plus explicitly declared `env`; secrets redacted | Ambient-secret leakage to MCP servers | Secrets explicitly forwarded | `VERIFIED_OFFICIAL` |
| Context-file scanning | Context files are scanned for prompt injection | Some injected instructions | Guaranteed semantic safety | `VERIFIED_OFFICIAL` |
| Tirith | Additional shell analysis on Linux/macOS; silently skipped on native Windows | Some shell risks | Native Windows execution | `VERIFIED_OFFICIAL` |

## Recommended safety profile

1. **Platform:** WSL2, not native Windows, because Hermes marks WSL2 Tier 1 and Tirith is unavailable on native Windows. Keep the checkout inside the WSL filesystem so Hermes, Git and QMD see one path model.
2. **Approvals:** `smart` for normal work. Switch a sensitive one-off session to `manual`; never normalize `off`.
3. **Hard denies:** block force pushes, pipe-to-shell, raw disk tools, recursive broad deletion, credential-store access, and network upload commands not required for the task. Denies are policy, not a substitute for isolation.
4. **Write roots:** repository root and the selected Hermes profile home only. The Business invoice area and other sensitive family directories should be write-restricted by task/workdir and OS permissions where practical.
5. **Recovery:** enable checkpoints and verify rollback before the pilot. Normal Git commits remain the durable project history; checkpoints are emergency recovery.
6. **Networking:** gateway/dashboard/board/QMD on `127.0.0.1`; explicit gateway allowlist/pairing. Never bind the unauthenticated Kanban dashboard or QMD MCP endpoint to `0.0.0.0` on a shared host.
7. **Secrets:** use provider/MCP credential stores; do not place secrets in repository context, task bodies, Kanban comments, or QMD collections. Keep `docker_forward_env: []` and add only named, task-required variables.
8. **Skills:** install only reviewed upstream packages, run Hermes trust/security scanning, keep project upstream skills immutable by policy, and use a separate constrained profile/container for unknown skills.
9. **Resources:** configure Docker CPU/memory/PID limits for isolated tasks. For local terminal mode, rely on WSL/OS process controls and operator monitoring because Hermes does not impose a complete host resource boundary.

## Configuration/command evidence — **DO NOT EXECUTE IN THIS RESEARCH RUN**

The following is an implementation sketch using documented keys; exact placement must be validated by the QA runbook against the installed release before use.

```yaml
# ~/.hermes/config.yaml — DO NOT EXECUTE / DO NOT INSTALL
approvals:
  mode: smart
  deny:
    - "git push --force*"
    - "*curl*|*sh*"
    - "dd if=*"

checkpoints:
  enabled: true

terminal:
  backend: local
```

```bash
# DO NOT EXECUTE — illustrative environment boundary
export HERMES_WRITE_SAFE_ROOT="/workspace/MasterOfArts:/home/<operator>/.hermes"
```

Do not copy a deny example blindly as the whole policy: QA must confirm the installed schema and add exact platform-appropriate patterns without blocking required Git reads, normal commits, QMD local access, or designated repository writes.

For an isolated Docker task, the documented alternative is `terminal.backend: docker` with `terminal.docker_forward_env: []` and appropriate `terminal.container_cpu`, `terminal.container_memory`, `terminal.container_disk`, and persistence values. It is not the baseline local-terminal setting above.

## Allowed-work simulation

| Work | Expected path | Controls encountered | Result |
|---|---|---|---|
| Read all repo Markdown, inspect Git state | Local read tools in repo | Context scan; no write approval | Allowed |
| Write a reviewed result in the designated repo path | Write/patch under safe root; checkpoint first | Smart approval only if risk-scored | Allowed |
| Query local QMD over stdio/loopback | Explicit MCP server, filtered env | No public listener | Allowed |
| Use provider model | HTTPS to configured provider | Named credential only | Allowed; content egress is explicit |
| Create/update Kanban task and attach artifact | Local Kanban DB and declared workspace | Durable audit state | Allowed |
| Normal Git commit | Repo-local Git | Checkpoint plus Git history | Allowed |

## Blocked-work simulation

| Attempt | Preventive layer | Expected result | Residual caveat |
|---|---|---|---|
| `rm -rf /` or fork bomb | Hardline blocklist; smart approval | Denied | Test benignly; do not execute destructive payload |
| Force-push main | Explicit deny | Denied | Rule syntax must match installed release |
| Write `/etc/...` through Hermes write tool | Safe root | Denied | Shell could bypass; Docker/OS permissions are stronger |
| Read/export unrelated credentials | Task policy, deny rules, filtered env, OS permissions | Denied/not exposed | Local shell under same user remains a residual risk |
| Unknown gateway user sends task | Allowlist/pairing | Denied | Authorized account compromise remains possible |
| QMD/dashboard reached from LAN | Loopback binding/firewall | Unreachable | `0.0.0.0` would defeat this |
| Skill tries pipe-to-shell installer | Deny plus smart approval and security scan | Denied/escalated | Novel exfiltration still requires isolation |
| Runaway container | CPU/memory/PID limits | Contained/terminated | Local-terminal processes need OS monitoring |

## Remaining risks and friction

The local-terminal shell is the largest residual risk because it can bypass the write-file safe root and operates with the operator's OS permissions. Smart approval is probabilistic. Repository documents and skills can contain adversarial instructions. Provider calls disclose selected prompt/context content. QMD is local, but retrieved text becomes provider input. Checkpoints do not reverse emails, network posts, payments, or data disclosure.

Normal friction is low: occasional smart-approval prompts, explicit task workdirs, credential setup, and local-only services. Docker raises friction to moderate because mounts, paths and tool availability must be declared. Manual approval mode is high friction and should be reserved for sensitive maintenance.

## Rollback and incident response

Stop the dispatcher/gateway, revoke exposed credentials, preserve the Hermes/Curator ledger and Kanban task record, use `/rollback` for checkpoint-covered edits, and use ordinary Git review/revert for committed repository changes. Do not force-reset shared history. If a skill is implicated, untrust/disable it, restore from Curator backup only if Curator managed it, and reinstall an approved upstream version through its native update mechanism after review.

## Evidence review

The draft initially risked treating the safe-root feature as a sandbox. It was corrected to state the documented shell bypass and to separate low-friction local operation from stronger Docker isolation. Every load-bearing control above is grounded in current official Hermes documentation. No software was installed and no destructive simulation was executed.

**Review result:** **PASS** — the profile protects the material risks without preventing the required repository, QMD, Kanban, provider and skill workflows.

## Official sources

- [Hermes Security](https://hermes-agent.nousresearch.com/docs/user-guide/security/)
- [Secure Hermes on a work machine](https://hermes-agent.nousresearch.com/docs/guides/secure-hermes-on-a-work-machine)
- [Hermes platform support](https://hermes-agent.nousresearch.com/docs/getting-started/platform-support)
- [Hermes Kanban](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban)
