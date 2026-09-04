# 6. About your `Docker-Desktop-Windows.md` file

You are correct here too.

I **used it**, but I **did not include the actual file in the repository or patch it into the authority chain**.

The file itself says:

- container usage is relatively lean;
- Docker Desktop/host overhead may be involved in UI lag;
- possible responses include GUI reduction, OpenProject worker reduction, memory ceilings, WSL2 limits, PostgreSQL/Valkey tuning.

I used that analysis in three ways.

### A. I accepted the central diagnostic direction

Namely:

> Do not automatically assume that container RAM usage itself explains the Windows UI problem.

That was part of why I **did not** immediately start reducing service resources.

### B. I deliberately rejected several proposed implementation actions

The file suggests:

```
OpenProject worker = 1
container memory limits
Postgres buffer tuning
Valkey maxmemory
.wslconfig limit
```

I did **not** propagate those into runtime configuration.

That was intentional.

Especially:

### `.wslconfig`

Your target is:

```
Docker Desktop
→ Hyper-V backend
```

not:

```
Docker Desktop
→ WSL2 backend
```

Therefore that particular recommendation is not applicable to the current target.

### OpenProject / memory / DB tuning

Those may eventually be useful, but the report does not establish that they solve your observed problem.

Your current architecture document now correctly says:

> measure first; no CPU/RAM ceilings, worker reductions, PostgreSQL or Valkey tuning without workload evidence.

That was one concrete outcome of reviewing your file.

### C. I separated it from the later, stronger Docker Desktop failure evidence

The later execution run produced a much more specific observation:

```
Windows sleep/resume
→ Docker Desktop control plane became unreachable/stalled
→ app HTTP endpoints remained alive
→ Docker CLI pipe hung
→ Docker Desktop restart fixed it
```

That is stronger operational evidence than the generic performance analysis.

Therefore I added the proposed:

```
one Docker probe
→ if dead
→ don't spam more Docker commands
→ restart Docker Desktop
→ retry once
```

process rule.

---

# 7. What I did **not** do with the file

I did not:

```
Docker-Desktop-Windows.md
        ↓
repo
```

and I did not create:

```
ARCHITEKTUR-BASIS.md
    → reference to Docker-Desktop-Windows.md
```

So when you say _“I don't see where you included the file”_, that is correct.

It is not included.

I synthesized part of it, but lost the **provenance link**.

That is a process defect.

---

# 8. What I think we should do with that file

I would **not make it architecture authority**, because the file combines:

1. observations that may be useful;
2. generic external recommendations;
3. assumptions about WSL2 that do not match the current Hyper-V target;
4. tuning suggestions we intentionally have not validated.

Instead preserve it as:

```
evidence / research input
        ↓
not authority
```

For example:

```
apex-meta/Alpine/research/
└── Docker-Desktop-Windows.md
```

with a short header:

```
Status: RESEARCH INPUT / NON-AUTHORITATIVE

Purpose:
Preserve the Windows/Docker Desktop performance
analysis that informed the evidence-gated tuning decision.

Accepted findings:
- distinguish container usage from Docker Desktop/host overhead;
- measure before tuning.

Not adopted:
- WSL2 .wslconfig, because current backend is Hyper-V;
- speculative worker/memory/database/cache limits;
- unverified GUI/headless claims.

Authority remains:
- compose.yaml
- ARCHITEKTUR-BASIS.md
- live runtime measurements
```

And then M08/architecture can link to it for provenance.

That is one file, no new workflow, and no runtime consequence. I would consider that **worth doing**.