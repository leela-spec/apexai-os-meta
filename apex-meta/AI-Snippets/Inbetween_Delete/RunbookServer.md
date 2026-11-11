## Answer first

Take a **VDS (dedicated-core), NVMe, Ubuntu 24.04 LTS, EU region, SSH key injected at order time** — not a Cloud VPS. Then change three things in your current stack before it ever touches a public IP: unbind the `0.0.0.0:8083` port mapping, move the `/mnt/c/GitDev/...` paths, and put a TLS reverse proxy in front. The rest of the Contabo work is ordering choices and two firewalls that must agree with each other.

Grounding for sizing: [ki-basis/docs/INFRASTRUCTURE.md](https://claude.ai/epitaxy/ki-basis/docs/INFRASTRUCTURE.md) — one PostgreSQL 16 cluster (pgvector), two OpenProject 17.8 instances (1536M / 1792M caps), Hermes ×2, Paperless ×2, Firefly ×2, Valkey ×2, Nginx ×2, all under a 16 GB WSL2 ceiling.

---

## 1. Which Contabo product

|Option|Spec|~Price/mo|Verdict|
|---|---|---|---|
|Cloud VPS 8|8 **shared** vCPU, 24 GB, 150 GB NVMe, 600 Mbit/s|~€14 incl. VAT|Entry. Accept CPU steal.|
|**Cloud VDS M**|8 **dedicated** AMD EPYC 7282 cores, 32 GB, 240 GB NVMe, 500 Mbit/s|~€68|**Recommended**|
|Cloud VDS L|12 dedicated cores, 48 GB, 360 GB NVMe, 750 Mbit/s|~€96|If agents/LLM traffic grows|

**Why dedicated cores matter for _this_ stack specifically:** PostgreSQL fsync latency and OpenProject's Puma/GoodJob workers are both latency-sensitive, and Contabo does not publish overcommit ratios. The only hard measurement I found reports **0–2 % CPU steal off-peak but 8–15 % at peak** on shared VPS plans (vmstat, during load testing). On the VDS line Contabo states dedicated AMD EPYC cores. For an interactive PM system two people actually use, paying €54/mo more to remove steal from the variable set is the cheaper debugging decision.

**Always pick NVMe, never the SSD variant.** The cheaper VPS tiers default to standard SSD; benchmark reviews of Contabo disk I/O conflict badly (one reports 2.1 GB/s read / 45k 4K IOPS, another claims ~¼ of a dedicated SATA DC SSD). Your Postgres cluster plus two Ruby apps is write-amplifying — don't buy the ambiguous tier.

**Caveats on these figures:** the plan/price table came from a page-content summary that the fetch flagged as not verbatim, and the steal-time numbers are from affiliate review blogs with unclear methodology. Confirm prices on the order form before you commit. Also: if "other orchestration systems" includes **local model inference, no VPS/VDS tier has a GPU** — that needs Contabo's dedicated/GPU line, which I did not verify.

**Region:** EU (Germany) — GDPR posture for Paperless/Firefly financial and document data, and lowest latency from your workstation. Contabo advertises 9 regions / 11 locations; cities only appear in a map image, so pick explicitly on the order form.

---

## 2. Contabo-specific ordering and first-hour steps

These are the things that are _actually different_ about Contabo versus a Hetzner/DO box:

**At order time**

1. **Paste your SSH public key / supply cloud-init user-data in the order form.** Contabo's default flow provisions root + password and **emails the root credentials in plaintext**. A new VPS is port-scanned within minutes of going live. If you take the key path at order time, the emailed password never becomes a live attack surface.
2. Select Ubuntu 24.04 LTS (free image). Decline cPanel/Plesk. Decline the "Docker" one-click app — install from Docker's own apt repo so you control the Compose version (you're on v2.40.3).
3. Decide **Auto Backup** now (paid add-on, price not published on the product page). Snapshots are **1–3 depending on tier and are not backups** — they're on the same infrastructure.
4. Expect a **possible manual verification delay on a first order**. Don't schedule a cutover window that assumes instant provisioning.

**Two firewalls, and they must agree**  
Contabo gives you a free **network firewall in the Customer Control Panel** that filters _upstream of the OS_, plus whatever you run on-host (UFW/nftables). The standard lockout: someone moves SSH to a non-standard port, updates UFW, forgets the CCP firewall — or enables default-deny before the SSH allow rule. Order of operations:

```bash
# on the server, BEFORE any default-deny
ufw allow 22/tcp
ufw allow 80/tcp
ufw allow 443/tcp
ufw default deny incoming
ufw enable
```

Then mirror exactly those three ports in the CCP firewall. Verify the **VNC console in the CCP** opens _before_ you disable password auth — that console is your only way back in.

**Partition / storage extension**  
Root is typically on `sda3`. Contabo's blog says cloud-init customers get partitions expanded automatically on a disk change, but a user report says a storage extension was delivered with the partition work left to the customer. Plan to do it yourself:

```bash
apt install -y cloud-guest-utils
growpart /dev/sda 3
resize2fs /dev/sda3   # or lvextend + resize2fs if LVM
```

**Backups to Contabo Object Storage** (S3-compatible, ~€2.49/250 GB, €9.96/TB in Europe; their blog claims no egress fees — a third-party comparison contradicts this with a free-allowance model, so verify). `pg_dump`/pgBackRest from the shared cluster plus a tar of the Hermes bind mounts, nightly, to a bucket. This replaces the snapshot illusion.

---

## 3. What has to change in your stack (the part that actually bites)

### 3.1 The `0.0.0.0:8083` mapping — fix this first

INFRASTRUCTURE.md §4.3: private OpenProject is bound `0.0.0.0:8083 → 80`. On Windows that's a LAN exposure. On a Contabo public IP it is **the internet**, and — critically — **Docker publishes ports by writing iptables rules that bypass UFW entirely**. Your `ufw default deny incoming` will not protect it. Every published port in all four compose files must become loopback-only:

```yaml
ports:
  - "127.0.0.1:8083:80"
```

Then expose only 80/443 via a reverse proxy (Caddy is the least work — automatic Let's Encrypt). Everything else — 8010, 8086, 8642, 9119, 8084 and the whole 9xxx community range — stays on loopback behind that proxy with auth.

### 3.2 OpenProject host-check

Your current workaround is "browse `http://127.0.0.1:8083`, not `localhost`, due to the host-check." Behind a proxy on a real domain that breaks. Set `OPENPROJECT_HOST__NAME=pm.yourdomain.tld` and `OPENPROJECT_HTTPS=true`, and have the proxy pass `X-Forwarded-Proto`.

### 3.3 Paths — the `/mnt/c` problem disappears, and takes work with it

Hermes uses bind mounts `/root/.hermes → /opt/data` (~4.4 GB) and `/root/workspaces` (~3.5 GB), and every lifecycle command in §7 is a `wsl -d Ubuntu -u root -- …/mnt/c/GitDev/…` invocation. On the server:

- Repos go to `/srv/apex/<repo>` on native ext4. Rewrite every `/mnt/c/GitDev/` path in compose files, `.env*`, and scripts.
- Your [Hermes ext4 launch gate](https://claude.ai/epitaxy/local_f4901d76-6d6e-4a11-a831-d9cef70d1768) is satisfied by construction — there is no `/mnt/c` — but the gate code in the WSL launcher binaries references that path and needs rewriting, not deleting.
- Don't put bind mounts under `/root`. Use `/srv/apex/hermes/{data,workspaces}`.

### 3.4 Delete, don't port, the WSL2 scaffolding

These exist only because of WSL2 and are pure waste on a server: `.wslconfig` 16 GB cap, `wsl-keepalive.vbs`, the `openproject-keepalive` in-VM service, the ~80 s cold-boot avoidance, and the `start/stop.ps1` wrappers. Replace with one systemd unit per stack (`Restart=always`, `After=docker.service`).

### 3.5 Revisit the on-demand sleep policy

Community (~2.45 GB) and the private peripheral tools (~840 MB) are stopped by default purely to claw back WSL2 RAM. On 32 GB that constraint is gone — flip them to `restart: unless-stopped` and retire `wake-tools.sh` / `sleep-tools.sh`. Likewise the Option 2A/2B memory surgery (`OPENPROJECT_WEB_WORKERS=0`, `mem_limit: 1536M`, `MALLOC_ARENA_MAX=2`) was forced by the 16 GB ceiling. Raise the limits and restore `WEB_WORKERS=1`, but **keep `mem_limit` set** — an unbounded Ruby heap on a shared host is how you get OOM-killed at 3 a.m. Keep jemalloc; it's a win regardless.

### 3.6 Secrets

`ki-basis-shared/.env`, `.env.shared-db`, `.env.wsl`, `op.env` currently sit in repo directories. On a public host: `/etc/apex/*.env`, `root:root`, `0600`, referenced by `--env-file`. Rotate every DB password during the migration — the current ones have lived on a workstation.

---

## 4. Build sequence on the box

```bash
# 1. identity + hardening (before anything else)
adduser apex && usermod -aG sudo apex
mkdir -p /home/apex/.ssh && cp /root/.ssh/authorized_keys /home/apex/.ssh/
chown -R apex:apex /home/apex/.ssh && chmod 700 /home/apex/.ssh
# /etc/ssh/sshd_config.d/99-hardening.conf:
#   PermitRootLogin no
#   PasswordAuthentication no
#   PubkeyAuthentication yes
systemctl restart ssh      # keep your current session open, test in a 2nd one
```

```bash
# 2. baseline
apt update && apt full-upgrade -y
apt install -y unattended-upgrades fail2ban chrony cloud-guest-utils
timedatectl set-timezone Europe/Berlin
```

```bash
# 3. Docker from the official repo (not docker.io)
install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] \
https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo $VERSION_CODENAME) stable" \
  > /etc/apt/sources.list.d/docker.list
apt update && apt install -y docker-ce docker-ce-cli containerd.io \
  docker-buildx-plugin docker-compose-plugin
```

```bash
# 4. the one external network, then stacks in dependency order
docker network create shared-db-net
# ki-basis-shared (postgres)  →  leela-op178  →  ki-basis  →  community
```

Then set `/etc/docker/daemon.json` with `log-driver: local`, `max-size: 10m` — unbounded JSON logs are the usual cause of "no space left on device" on a 240 GB box running this many containers.

---

## 5. Verification

Your `infra-health-test.sh` is read-only and already encodes the invariants. Port it (strip the `wsl -d Ubuntu -u root --` prefix, swap the paths) and make it the acceptance gate for the migration — it checks the cross-tenant `REVOKE CONNECT` isolation, which is the one property you most want to confirm survived the move. Add one new check it cannot currently have: `ss -tlnp` must show nothing but 22/80/443 on a non-loopback address.

Sources: [Contabo VPS](https://contabo.com/en/vps/), [Contabo VDS](https://contabo.com/en/vds/), [Contabo VPS security checklist](https://contabo.com/blog/vps-security-checklist/), [Contabo partition layout guide](https://contabo.com/blog/changing-the-partition-layout-of-your-vps-after-os-installation), [Contabo object storage pricing](https://contabo.com/blog/object-storage-feature-and-price-comparison/), [Contabo defaults encourage SSH passwords](https://jamesoclaire.com/2025/09/12/contabo-defaults-encourage-using-ssh-passwords/), [Contabo review — steal-time measurements](https://thatmy.com/contabo-review), [Contabo review 2026 — tradeoffs](https://space-node.net/blog/contabo-vps-review-2026), [BestUSAVPS Contabo benchmarks](https://bestusavps.com/reviews/contabo/).