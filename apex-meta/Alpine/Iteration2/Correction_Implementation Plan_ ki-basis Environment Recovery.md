# Correction / Implementation Plan — ki-basis Environment Recovery

**Recommended canonical file:**  
`apex-meta/Alpine/ENVIRONMENT-CORRECTION-IMPLEMENTATION-PLAN.md`

**Status:** planning only.  
**Current WSL stack:** preserve as migration source and rollback environment.  
**Existing patch ZIP / 13-module correction program:** **do not execute unchanged**.

The failure analysis gives us the correct design principle for this recovery: the executor must distinguish **explicit authority**, **information required to execute that authority**, and **plausible but unauthorized extensions**. The Docker-host choice was in the third category but was silently promoted into implementation.

---

## 1. Corrected target architecture — lock this first

The target should now be explicit:

```
Windows 11
│
├── Existing Ubuntu WSL
│    └── existing development/APEX environment
│
│    NOT the ki-basis runtime host
│
└── Dedicated ki-basis Linux Docker environment
     │
     ├── independent Linux VM/kernel
     ├── independent Docker Engine
     ├── independent Docker storage/volumes
     └── ki-basis-net
          ├── nginx
          ├── postgres + pgvector
          ├── valkey
          ├── firefly
          ├── paperless
          ├── openproject
          └── hermes
```

**Host recommendation:** Docker Desktop using the **Hyper-V backend**, provided the machine/Windows edition supports it. Docker explicitly describes Hyper-V as running the Docker Linux VM in a fully isolated VM, whereas WSL2 is the integrated/shared-kernel backend. Docker Desktop currently supports WSL2, Hyper-V and Docker VMM on Windows; Hyper-V is the stable choice here because the explicit requirement is separation from WSL.

**Fallback:** if Hyper-V is unavailable, use a dedicated conventional Linux VM with Docker Engine. **Do not silently fall back to the existing Ubuntu WSL environment.**

### Important correction about Alpine

Do **not** create seven Alpine VMs.

The model is:

```
one independent Linux Docker host/kernel
        ↓
seven isolated Docker services
```

The containers use the appropriate upstream userspace/image:

```
nginx       -> Alpine appropriate
Valkey      -> Alpine appropriate
Postgres    -> pgvector upstream image
Firefly     -> Firefly upstream image
Paperless   -> Paperless upstream image
OpenProject -> OpenProject upstream image
Hermes      -> Hermes upstream image
```

That is exactly consistent with the supplied Alpine runbook, which explicitly warns against forcing Alpine onto complex Python/native stacks.

---

# 2. Program-level execution guardrail

This comes **before** any Docker correction.

The error analysis should result in one small Antigravity execution-rule patch, not a new orchestration framework.

Every module must start with this contract:

```
mode: READ_ONLY | MUTATE
explicit_goal:
target_repository:
target_environment:
allowed_reads:
allowed_mutations:
forbidden_mutations:
architecture_assumptions:
operator_decisions_required:
acceptance_evidence:
rollback:
```

And every discovered action must be classified:

|Classification|Agent may do|
|---|---|
|**EXPLICITLY_AUTHORIZED**|execute|
|**NECESSARY_TO_EXECUTE**|inspect/test only as required|
|**PLAUSIBLE_OR_USEFUL**|record/defer; do not execute|

Three hard rules follow from the failure analysis:

```
THINK / REVIEW / ANALYZE
→ mutation permission = false

material architecture ambiguity
→ stop at operator decision

adjacent/relevant repository content
→ does not become execution authority
```

This directly addresses both failure modes identified in the supplied analysis.

### Regression tests for the guardrail

Before using Antigravity for the migration, test two prompts:

**Test A — think-only lesson**

Expected result:

```
reads required material
produces recommendation
creates 0 files
modifies 0 files
```

**Test B — underspecified Docker host**

Prompt specifies Compose/services but not host environment.

Expected result:

```
identifies host boundary as unresolved
does NOT reuse existing Docker daemon automatically
asks/raises architecture gate
performs 0 runtime mutations
```

If either test fails, do not hand the migration program to that executor yet.

---

# 3. Disposition of what already exists

|Existing asset|Disposition|
|---|---|
|Working seven-service WSL stack|**KEEP temporarily — migration source**|
|WSL PostgreSQL/volumes/Hermes state|**KEEP — authoritative data source until target verified**|
|Antigravity-specific implementation plans|**KEEP**|
|Older generic duplicate implementation plans|**DELETE/archive as previously decided**|
|`docker-stack-integrity/` 13-module program|**DO NOT EXECUTE directly**; reuse its findings in this plan|
|Previous local patch ZIP|**SUPERSEDED — do not run unchanged**|
|`ARCHITEKTUR-BASIS.md`|Patch after target architecture is verified|
|Current integration report|Keep as **source-runtime evidence**, not final target acceptance|

The current Antigravity implementation plan correctly specifies the Compose topology but does not specify the Docker-host boundary.

The older Hermes architecture actually explicitly assumed Docker running on WSL, which explains why the executor inherited that environment.

---

# 4. W0 — Freeze and inventory the current source environment

### Goal

Turn the current WSL installation into a controlled **migration source**.

### Allowed actions

Read/inventory/backup only.

Do **not**:

```
upgrade images
change secrets
rename volumes
delete containers
delete old plans
patch Compose
recreate applications
```

### Capture

Record:

```
source_environment:
  host: Ubuntu WSL2
  docker_endpoint:
  compose_project:
  compose_file:
  git_commit:

services:
  postgres:
  valkey:
  firefly:
  paperless:
  openproject:
  nginx:
  hermes:

for_each_service:
  image_tag:
  image_id:
  repo_digest:
  container_id:
  networks:
  mounts:
  published_ports:
  health:

volumes:
  - name
  - consumer
  - mount_destination
  - approximate_size

hermes:
  state_source:
  workspaces_source:
  config:
  skills:
  memory:
  sessions:
```

### Repository issue

Do **not** touch the three unrelated dirty files reported by the CLI.

Use a **new clean worktree or clone** for the correction.

No stashing somebody else's work.  
No committing those files.  
No resetting them.

### G0 acceptance

Proceed only if:

- exact source runtime is documented;
- all persistent data sources are known;
- source remains healthy;
- exact image digests are captured;
- no unrelated repository changes occurred.

---

# 5. W1 — Produce a complete migration backup

This must happen **before provisioning/cutover work**.

The previous acceptance only proved PostgreSQL dumps plus Hermes archive; physical application state was incomplete.

### Backup required

```
PostgreSQL:
  globals / roles
  firefly DB
  paperless DB
  openproject DB

Volumes:
  Valkey
  Firefly uploads
  Paperless data
  Paperless media
  Paperless export
  Paperless consume
  OpenProject assets

Hermes:
  /opt/data source
  config
  skills
  memory
  sessions
  credentials without exposing them
  workspace state as required

Configuration:
  compose
  nginx
  postgres initialization
  env variable names
```

Real `.env` and API credentials remain outside Git.

### Required proof

Do one restore **before migration**:

```
source backup
      ↓
disposable Paperless DB + volumes
      ↓
real Paperless container
      ↓
Paperless API
      ↓
known test document retrieved/downloaded
```

This proves the migration source is recoverable, including physical media.

### G1 acceptance

No target deployment until the backup is proven usable.

---

# 6. W2 — Provision the independent Docker host

This is the architecture correction itself.

## Preferred path

Configure Docker Desktop to use:

```
Hyper-V backend
WSL engine disabled for this Docker environment
Ubuntu WSL integration not used
```

Docker documents Hyper-V as a fully isolated Docker Linux VM.

### Verification must prove independence

The executor must establish:

```
SOURCE ENGINE != TARGET ENGINE
```

Evidence should include:

```
source:
  environment: Ubuntu WSL
  docker_endpoint: <old>

target:
  environment: Docker Hyper-V Linux VM
  docker_context: <target>
  engine_id: <target>
```

Test that creating a disposable target container does **not** appear in the old Ubuntu Docker daemon.

Test the opposite too.

### No migration yet

At the end of W2 the target should have:

```
Docker Engine
Docker Compose
target context
empty Docker storage
```

but **no restored production state**.

### G2 acceptance

A verifier must prove the two engines are genuinely separate.

---

# 7. W3 — Correct the repository configuration for portability

Now apply the repository corrections we already identified.

This is where the previous patch program becomes useful again.

### A. Plan authority

Keep the Antigravity-specific integrated family.

Delete/archive the older generic duplicate family.

Repair moved relative links.

### B. Secret model

Repository:

```
.env.example
  -> names only / blank secret examples

compose.yaml
  -> ${SECRET:?required}
```

Local target environment:

```
.env
  -> real secrets
  -> ignored by Git
```

Add:

```
/ki-basis/.env
```

### C. Image pinning

Use the **source stack's actual accepted RepoDigests**.

Do not search documentation and arbitrarily select newer releases.

Target Compose becomes:

```
tested source image
        ↓
immutable sha256 digest
        ↓
target deployment
```

This prevents migration and upgrade from becoming the same operation.

### D. Hermes host coupling

This is a critical correction.

Remove:

```
/root/.hermes:/opt/data
/root/workspaces:/root/workspaces
```

when those paths refer to the **old WSL host**.

Replace them with target-local persistent storage, e.g.:

```
hermes_data       -> /opt/data
hermes_workspaces -> /root/workspaces
```

or equivalent Docker-host-local storage.

There must be:

```
no /mnt/c
no old Ubuntu /root/workspaces bind
no old Ubuntu ~/.hermes dependency
```

The old Hermes architecture explicitly identified WSL/host workspace mounting as one of the previous topology choices; for this new isolation requirement, that cross-environment dependency must disappear.

### E. Hermes repos

Inside the new Hermes environment:

```
GitHub
  ↓
Hermes workspaces
```

Do not copy live working repositories from the old WSL filesystem as the permanent architecture.

Clone/synchronize the approved Hermes repositories into target-local persistence.

### F. Remaining integrity corrections

Integrate here:

- Hermes 8642/9119 semantic verification;
- OpenProject orphan volume correction;
- source-controlled Hermes connector definitions;
- nginx route verification;
- seven-service verifier;
- backup/restore scripts.

### G3 acceptance

`docker compose config` must succeed against the new target configuration **without requiring paths from Ubuntu WSL**.

---

# 8. W4 — Restore data into target

Bring up only infrastructure first:

```
postgres
valkey
```

Restore and verify.

Then sequentially:

```
Firefly
    ↓
Paperless
    ↓
OpenProject
    ↓
nginx
    ↓
Hermes
```

Never `docker compose up` the entire migrated stack blindly as the first test.

For each application:

```
start
→ health
→ authenticate
→ verify migrated proof object
→ restart
→ verify again
→ next
```

### Hermes migration

Restore the necessary Hermes persistent state into the target-local `hermes_data`.

Then populate target-local workspaces through GitHub.

Verify:

```
boards
memory
skills
profiles
sessions
workspace discovery
git access
```

No Docker socket.

No old WSL filesystem.

---

# 9. W5 — Re-establish real Hermes control

Network access alone still does not count as integration.

Persist three small supported connectors/skills:

```
Hermes → Firefly API
Hermes → Paperless API
Hermes → OpenProject API v3
```

Each must define:

```
base_url:
credential_reference:
allowed_reads:
write_boundary:
error_behavior:
```

Secrets live only in target-local secret state.

### Verification

From the actual Hermes runtime:

```
valid token
→ authenticated product read succeeds

invalid token
→ product rejects request

remove connector
→ Hermes no longer claims product capability
```

That last test prevents another fake “URL configured = connector exists” result.

---

# 10. W6 — Seven-service target acceptance

The target environment must now pass the complete matrix.

|Area|Required proof|
|---|---|
|PostgreSQL|health + pgvector + role isolation|
|Valkey|PONG + persistence|
|Firefly|UI/API + migrated data|
|Paperless|UI/API + OCR/search + physical document|
|OpenProject|health/API + migrated work package/assets|
|nginx|`/healthz` + each retained real route|
|Hermes|dashboard/API + state + authenticated connectors|
|Docker DNS|service-name resolution inside target|
|Ports|expected Windows/operator access|
|DB/cache|not externally published|
|Secrets|absent from Git|
|Images|immutable tested pins|
|Persistence|full restart survives|
|Independence|target survives without Ubuntu WSL Docker engine|
|Security|Hermes Docker socket absent|

### The new critical environment test

Stop the old Ubuntu WSL Docker stack/daemon.

The entire new stack must continue to work.

That is the proof the original architectural error has actually been removed.

---

# 11. W7 — Target backup + restore acceptance

Run the backup system **again against the new target**.

Then restore Paperless into a disposable target environment and retrieve the document through the actual Paperless API.

This proves:

```
migration successful
+
new environment recoverable
```

not merely that the old WSL environment was recoverable.

---

# 12. W8 — Cutover

Only now perform the consequential gate.

### Before cutover

```
old WSL stack = running/available
new stack = PASS
new backup = PASS
new restore = PASS
```

### Cutover

1. stop the old WSL ki-basis stack;
2. switch the target to canonical user-facing ports if temporary ports were used;
3. run complete W6 acceptance again;
4. verify Windows/Homepage access;
5. verify Hermes control;
6. leave the old WSL volumes/data untouched.

### Rollback

If any critical target check fails:

```
stop target
restart old WSL stack
restore canonical ports
investigate
```

No data deletion during rollback.

---

# 13. W9 — Repository truth and cleanup

Only after successful cutover should documentation become definitive.

Patch `ARCHITEKTUR-BASIS.md` to say explicitly:

```
CURRENT RUNTIME:
Windows
→ independent Hyper-V Docker Linux VM
→ ki-basis Docker Engine
→ ki-basis-net
→ seven services
```

Also explicitly state:

```
Ubuntu WSL is not the ki-basis runtime host.
Alpine is an image strategy, not the platform host architecture.
```

The supplied old architecture file does not specify this host boundary and still describes a materially different service set, so it should no longer present itself as the current runtime authority.

Mark the old integration report:

```
SOURCE-ENVIRONMENT ACCEPTANCE / PRE-MIGRATION
```

Do **not** delete it; it is useful provenance.

Mark the existing `docker-stack-integrity` execution program as superseded by this migration/correction program, while preserving its findings.

---

# 14. W10 — Independent final verification

Give a fresh verifier only:

```
target architecture contract
current Compose
current architecture document
target Docker evidence
acceptance criteria
```

Do **not** give it the implementation narrative first.

It must independently answer:

```
docker_host_is_independent_of_wsl: true/false
old_wsl_mounts_present: true/false
seven_services_real: true/false
all_data_restored: true/false
hermes_connectors_reproducible: true/false
images_pinned: true/false
secrets_fail_closed: true/false
backup_complete: true/false
application_restore_proven: true/false
architecture_docs_truthful: true/false
```

Only all-critical-true permits:

```
FINAL PASS
```

---

# Final execution sequence

```
P0  Fix Antigravity execution boundary
 ↓
W0  Freeze/inventory existing WSL source
 ↓
W1  Complete + prove source backup
 ↓
GATE: select/confirm independent Docker host
 ↓
W2  Provision isolated Hyper-V Docker environment
 ↓
W3  Patch Compose/repo for portable independent target
 ↓
W4  Restore data + bring services up sequentially
 ↓
W5  Rebuild durable Hermes connectors
 ↓
W6  Seven-service + environment-isolation acceptance
 ↓
W7  Backup + application-level restore on target
 ↓
GATE: CUTOVER
 ↓
W8  Stop old WSL stack / activate canonical target
 ↓
W9  Documentation + authority cleanup
 ↓
W10 Independent final verifier
 ↓
PASS
 ↓
operator may later authorize deletion of old WSL stack
```

## Most important change from the previous plans

The old implementation flow began effectively at:

```
Compose → services → tests
```

The corrected one begins at:

```
EXECUTION AUTHORITY
        ↓
HOST-BOUNDARY DECISION
        ↓
SOURCE / TARGET SEPARATION
        ↓
Compose
        ↓
services
```

That is the missing architectural layer that caused the Docker mistake, while the explicit/necessary/plausible classification addresses the broader agent-drift problem identified in the error analysis.

I would **supersede the existing 13-module runtime-correction launcher with this program before Antigravity performs any further Docker mutation**.