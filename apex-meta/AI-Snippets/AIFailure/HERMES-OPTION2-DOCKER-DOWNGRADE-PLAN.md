# Option 2 — Downgrade Docker/containerd to a containerd-1.x runtime (execution plan)

**Goal:** remove the containerd-2.x half of the `s6-overlay ↔ containerd-2.x` incompatibility that is spuriously restarting the Hermes gateway, so the single-container (Arch-3) migration becomes stable.
**Companion:** `HERMES-MIGRATION-HANDOVER-OKF-v0.2.md` (full context, all failures, sources).
**Date:** 2026-08-26 · **Status:** proposed, not executed.

---

## 0. Why this can be the fix even though "Docker worked before"

Docker did not change or break. **Before (Arch 2)** the gateway ran on the WSL host and Docker only ran dumb `sleep infinity` command-sandboxes — no s6-overlay, so the bug was never exercised. **Now (Arch 3)** the gateway runs *inside* a container under **s6-overlay supervision** — a new code path that trips the latent containerd-2.x signal-delivery bug. Two levers exist:
- **Lever A (this plan):** downgrade the runtime to **containerd 1.x** (removes the containerd-2.x trigger).
- **Lever B (cheaper alternative, see §6):** run a **pre-s6-overlay Hermes image** (removes the s6 trigger) — an image-tag change, no host surgery.

**Recommendation:** try **Lever B first** (far lower risk, same expected outcome). Do Lever A only if B is unacceptable or fails. Either way, **nothing is "fixed" until the §5 verification soak passes.**

---

## 1. Current runtime (measured 2026-08-26)

| Package | Version | Source |
|---|---|---|
| `docker.io` | `29.1.3-0ubuntu4.1` | Ubuntu "resolute" universe |
| `containerd` | `2.2.2-0ubuntu1.1` | Ubuntu "resolute" main |
| `runc` | `1.4.0-0ubuntu1` | Ubuntu |

- **No `docker-ce`; no docker.com apt repo configured.** Ubuntu repos offer **only containerd 2.x** → a downgrade requires the **official Docker repo** (`download.docker.com`) or **manual .deb** installs of `containerd.io` 1.7.x (+ a matching `docker-ce` ~27.x).
- WSL distro codename is **"resolute"** (a very new Ubuntu). ⚠️ Docker's official repo may **not** publish packages for "resolute" yet → you will likely have to point the Docker apt source at the nearest supported LTS codename (e.g. `noble`) or install pinned `.deb`s by hand.
- Only one container exists (`hermes`), so a runtime change affects nothing else.

---

## 2. Target versions

- **`containerd.io` = 1.7.x** (last containerd 1.x line; e.g. `1.7.27-1`). This is the key change — it reverts the signal-delivery behavior.
- **`docker-ce` / `docker-ce-cli` ≈ 5:27.x** (the Docker CE line that pairs with containerd 1.7 and predates the containerd-2.x default).
- `runc` from the `containerd.io` package (bundled) — do not mix with Ubuntu's `runc`.

---

## 3. Pre-flight (do ALL of these first)

1. **Full WSL snapshot (real rollback):** from **Windows PowerShell**
   ```powershell
   wsl --shutdown
   wsl --export <distroName> D:\wsl-backups\apex-before-docker-downgrade.tar
   ```
   (Find `<distroName>` with `wsl -l -v`; here it is registered as "Ubuntu".) This lets you fully restore if the downgrade breaks Docker/WSL.
2. Confirm `/root/.hermes.backup-pre-arch3` still exists (root-owned) — the Hermes-data rollback net.
3. Record current versions (table in §1) so you can reinstall them if reverting.
4. Note the reproducible Hermes launch command (docs-exact, §4 step 6).

---

## 4. Execution steps (run in WSL as root, via `wsl.exe -e bash -lc '...'`)

> Do not proceed to the next step if one fails — stop and assess.

**A. Stop everything**
```bash
docker stop hermes
systemctl stop docker docker.socket containerd
```

**B. Remove the Ubuntu Docker stack (keeps image/data dirs)**
```bash
apt-get remove -y docker.io containerd runc
# do NOT purge /var/lib/docker or /var/lib/containerd yet (see risk R3)
```

**C. Add Docker's official repo + key** (adjust `CODENAME` — try the WSL codename first; if unsupported, use `noble`)
```bash
apt-get update && apt-get install -y ca-certificates curl gnupg
install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg
chmod a+r /etc/apt/keyrings/docker.gpg
CODENAME=noble   # or the actual supported codename
echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $CODENAME stable" > /etc/apt/sources.list.d/docker.list
apt-get update
```

**D. See exact available versions, then install pinned older ones**
```bash
apt-cache madison containerd.io docker-ce docker-ce-cli   # pick a 1.7.x containerd.io + 5:27.x docker-ce
apt-get install -y \
  containerd.io=<1.7.x-1> \
  docker-ce=<5:27.x.x-1~ubuntu.$CODENAME> \
  docker-ce-cli=<5:27.x.x-1~ubuntu.$CODENAME>
apt-mark hold containerd.io docker-ce docker-ce-cli   # prevent auto-upgrade back to 2.x
```

**E. Start + verify the runtime downgraded**
```bash
systemctl enable --now containerd docker
docker version | grep -i version
containerd --version      # MUST show 1.7.x (containerd 1.x), NOT 2.x
```

**F. Re-launch Hermes (docs-exact) + re-apply the /root traversal**
```bash
# image may need re-pull if the image store changed (see R3):
docker image inspect nousresearch/hermes-agent:latest >/dev/null 2>&1 || docker pull nousresearch/hermes-agent:latest
rm -f /root/.hermes/gateway.lock
docker run -d --name hermes --restart unless-stopped \
  -v /root/.hermes:/opt/data \
  -v /root/workspaces:/root/workspaces \
  -p 8642:8642 -p 9119:9119 \
  -e HERMES_DASHBOARD=1 \
  nousresearch/hermes-agent:latest gateway run
sleep 12 && docker exec hermes chmod 711 /root   # repo traversal (still non-persistent; see handover TODO)
```

---

## 5. Verification gate (do NOT declare success without this)

1. **20-minute HANDS-OFF soak**, checks from OUTSIDE only (no `docker exec`, spaced ≥90s):
   ```bash
   # loop: docker inspect --format '{{.State.StartedAt}}' hermes ; curl -s -o /dev/null -w '%{http_code}' http://127.0.0.1:9119/
   ```
   **Pass = StartedAt never changes, dashboard 302 every check, AND** `docker logs --since 1200s hermes | grep -c "Hermes Gateway Starting"` returns **1**.
2. **The specific killer test:** confirm there is **NO idle SIGTERM** — `docker logs hermes | grep "Shutdown context"` should stay empty during the soak (the previous failure produced an idle `signal=SIGTERM` from `s6-supervise gateway-default` at ~20 min, loadavg 0.02).
3. **Dashboard login actually completes** (not just the login page): open `http://localhost:9119`, sign in `admin` / `zhwGcgTMUcagANhe`, confirm you reach the dashboard (this needs api_server 8642 up).
4. Only if 1–3 all pass → migration is stable on the downgraded runtime.

---

## 6. Lever B — the cheaper alternative to try FIRST

Instead of touching the host runtime, run a **pre-s6-overlay Hermes image** (the s6-overlay supervision — the other half of the incompatibility — was introduced around v0.15; v0.14.x used `tini` and does not have this bug per issue #35394). Steps:
```bash
docker rm -f hermes
docker pull nousresearch/hermes-agent:0.14   # confirm exact stable pre-s6 tag on Docker Hub first
docker run -d --name hermes --restart unless-stopped \
  -v /root/.hermes:/opt/data -v /root/workspaces:/root/workspaces \
  -p 8642:8642 -p 9119:9119 -e HERMES_DASHBOARD=1 \
  nousresearch/hermes-agent:0.14 gateway run
```
Then run the **same §5 verification**. ⚠️ Caveat: the migrated `config.yaml` is `_config_version: 39` (written by v0.20.5). An older image may **refuse or down-migrate** the config — test on a **copy** of `/root/.hermes` first, or be ready to accept a config re-init. If B is stable, it's a much smaller change than A (no host Docker surgery).

---

## 7. Risks & rollback

| Ref | Risk | Mitigation |
|---|---|---|
| R1 | Docker official repo has no `resolute` packages | Use nearest LTS codename (`noble`) in the apt source, or install pinned `.deb`s manually |
| R2 | Downgrade breaks Docker/WSL entirely | Restore the `wsl --export` snapshot (§3.1) |
| R3 | containerd 2.x→1.x image-store format mismatch → images/containers unreadable | `docker pull` the Hermes image again; data is safe on the `/opt/data` volume (host `/root/.hermes`) |
| R4 | Held packages block future security updates | Documented `apt-mark hold`; unhold when an upstream fix lands |
| R5 | **Downgrade may NOT fix it** (our signal read `SIGTERM`, not the `UNKNOWN` in #35394) | The §5 gate catches this; if it still restarts, revert and use Lever B or roll back to host |

**Revert the downgrade:**
```bash
apt-mark unhold containerd.io docker-ce docker-ce-cli
apt-get remove -y docker-ce docker-ce-cli containerd.io
rm /etc/apt/sources.list.d/docker.list && apt-get update
apt-get install -y docker.io=29.1.3-0ubuntu4.1 containerd=2.2.2-0ubuntu1.1 runc=1.4.0-0ubuntu1
```
Or restore the WSL snapshot (cleanest).

**Fallback if neither A nor B works:** roll back to the pre-migration host Hermes (see handover §7 option 1).

---

## 8. Sources
- s6-overlay ↔ containerd-2.x restart loop; "downgrade to v0.14.x / containerd 1.x works": https://github.com/NousResearch/hermes-agent/issues/35394 , https://github.com/NousResearch/hermes-agent/issues/35393
- Docker install/repo reference: https://docs.docker.com/engine/install/ubuntu/
- Full investigation + all ruled-out causes: `HERMES-MIGRATION-HANDOVER-OKF-v0.2.md`
