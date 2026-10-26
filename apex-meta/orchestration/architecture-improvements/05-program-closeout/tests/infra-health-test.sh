#!/usr/bin/env bash
# =============================================================================
# infra-health-test.sh — READ-ONLY health / efficiency / claimed-fact verifie
# for the Apex WSL2 stack (post-2026-09-26 consolidation baseline).
#
# Run inside the WSL2 "Apex" engine:
#   wsl -d Ubuntu -u root -- bash -c "tr -d '\r' < <this file> | bash"
# Exit code 0 = no FAIL. Prints PASS/FAIL/WARN tally. Never prints secrets
# (only non-secret env keys like OPENPROJECT_API_URL are inspected).
# =============================================================================
set -uo pipefail
PASS=0; FAIL=0; WARN=0
ok(){   echo "  [PASS] $*"; PASS=$((PASS+1)); }
bad(){  echo "  [FAIL] $*"; FAIL=$((FAIL+1)); }
warn(){ echo "  [WARN] $*"; WARN=$((WARN+1)); }
hr(){   echo "== $* =="; }

hr "1. Engine reachable"
if docker info >/dev/null 2>&1; then ok "docker engine reachable"; else bad "docker engine unreachable"; fi

hr "2a. Core always-on containers running (4)"
for c in ki-basis-hermes ki-basis-valkey leela-op178-openproject ki-basis-shared-postgres; do
  st=$(docker inspect -f '{{.State.Status}}' "$c" 2>/dev/null || true)
  if [ "$st" = "running" ]; then ok "$c running"; else bad "$c not running (state: ${st:-absent})"; fi
done

hr "2b. Private peripheral on-demand containers (3 — restart=no, stopped by default)"
PRIV_NGINX_RUNNING=0
for c in ki-basis-paperless ki-basis-firefly ki-basis-nginx; do
  st=$(docker inspect -f '{{.State.Status}}' "$c" 2>/dev/null || true)
  rp=$(docker inspect -f '{{.HostConfig.RestartPolicy.Name}}' "$c" 2>/dev/null || true)
  [ "$c" = "ki-basis-nginx" ] && [ "$st" = "running" ] && PRIV_NGINX_RUNNING=1
  if [ "$rp" = "no" ] && { [ "$st" = "exited" ] || [ "$st" = "running" ]; }; then
    ok "$c state=$st restart=$rp (on-demand)"
  else
    bad "$c state=${st:-absent} restart=${rp:-unset} (expected state=exited|running and restart=no)"
  fi
done

hr "2c. Community on-demand containers (6 — restart=no, stopped by default)"
COMM_RUNNING=0
for c in community-hermes community-paperless community-firefly community-nginx community-openproject community-valkey; do
  st=$(docker inspect -f '{{.State.Status}}' "$c" 2>/dev/null || true)
  rp=$(docker inspect -f '{{.HostConfig.RestartPolicy.Name}}' "$c" 2>/dev/null || true)
  [ "$st" = "running" ] && COMM_RUNNING=1
  if [ "$rp" = "no" ] && { [ "$st" = "exited" ] || [ "$st" = "running" ]; }; then
    ok "$c state=$st restart=$rp (on-demand)"
  else
    bad "$c state=${st:-absent} restart=${rp:-unset} (expected state=exited|running and restart=no)"
  fi
done

hr "3. Endpoints respond + latency (warm should be < 2.0s)"
check_http(){ # name url expected_code
  local name="$1" url="$2" exp="$3" resp code tt
  resp=$(curl -s -o /dev/null -w '%{http_code} %{time_total}' --max-time 8 "$url" 2>/dev/null || echo "000 8.0")
  code=${resp%% *}; tt=${resp##* }
  if [ "$code" = "$exp" ]; then
    awk "BEGIN{exit !($tt < 2.0)}" && ok "$name $url -> $code in ${tt}s" || warn "$name $url -> $code but SLOW ${tt}s (cold VM / bottleneck?)"
  else
    bad "$name $url -> $code (expected $exp) in ${tt}s"
  fi
}
check_http "priv-hermes"      "http://127.0.0.1:8642/health"  "200"
if [ "$PRIV_NGINX_RUNNING" -eq 1 ]; then
  check_http "priv-nginx"     "http://127.0.0.1:8084/healthz" "200"
else
  ok "priv-nginx skipped (private peripheral tools stopped on-demand)"
fi
check_http "openproject-17.8" "http://127.0.0.1:8083/"        "302"
if [ "$COMM_RUNNING" -eq 1 ]; then
  check_http "comm-hermes"    "http://127.0.0.1:9642/health"  "200"
  check_http "comm-nginx"     "http://127.0.0.1:9084/healthz" "200"
else
  ok "comm-hermes skipped (community stopped on-demand)"
  ok "comm-nginx skipped (community stopped on-demand)"
fi

hr "4. No bottleneck: per-container CPU/mem snapshot (flag CPU > 80%)"
docker stats --no-stream --format '{{.Name}}|{{.CPUPerc}}|{{.MemUsage}}' 2>/dev/null | while IFS='|' read -r n cpu mem; do
  case "$n" in ki-basis-*|community-*|leela-op178-*)
    v=${cpu%\%}; if awk "BEGIN{exit !($v > 80)}"; then echo "  [WARN] $n CPU $cpu (high) mem $mem"; else echo "  [ok]   $n CPU $cpu mem $mem"; fi ;;
  esac
done

hr "5. Postgres connection headroom (flag any role > 80% of its limit)"
if docker exec ki-basis-shared-postgres psql -U postgres -tA -c "select 1" >/dev/null 2>&1; then
  docker exec ki-basis-shared-postgres psql -U postgres -tA -F'|' -c \
    "select r.rolname, r.rolconnlimit, count(a.pid),
       case when r.rolconnlimit>0 then round(100.0*count(a.pid)/r.rolconnlimit) else 0 end
     from pg_roles r left join pg_stat_activity a on a.usename=r.rolname
     where r.rolname ~ '^(priv|comm)_' group by 1,2 order by 1" 2>/dev/null \
  | while IFS='|' read -r role lim cur pct; do
      [ -z "$role" ] && continue
      if [ "${pct:-0}" -gt 80 ] 2>/dev/null; then bad "role $role $cur/$lim (${pct}%) OVER 80%"; else ok "role $role $cur/$lim (${pct}%)"; fi
    done
else
  warn "cannot query postgres as superuser (skipped connection headroom)"
fi

hr "6. Cross-DB isolation (REVOKE CONNECT must hold)"
iso(){ # app db expect(t/f)
  local got
  got=$(docker exec ki-basis-shared-postgres psql -U postgres -tA -c "select has_database_privilege('$1','$2','CONNECT')" 2>/dev/null | tr -d '[:space:]')
  if [ "$got" = "$3" ]; then ok "$1 -> $2 CONNECT=$got (expected $3)"; else bad "$1 -> $2 CONNECT=$got (expected $3)"; fi
}
if docker exec ki-basis-shared-postgres psql -U postgres -tA -c "select 1" >/dev/null 2>&1; then
  iso priv_openproject_app comm_openproject f
  iso comm_openproject_app priv_openproject f
  iso priv_openproject_app priv_openproject t
else warn "cannot query postgres (skipped isolation checks)"; fi

hr "7. Claimed facts actually true (anti-hallucination)"
# 7a private Hermes really wired to leela-op178 (URL is not a secret)
u=$(docker inspect -f '{{range .Config.Env}}{{println .}}{{end}}' ki-basis-hermes 2>/dev/null | grep '^OPENPROJECT_API_URL=' | cut -d= -f2-)
[ "$u" = "http://leela-op178-openproject:80" ] && ok "priv Hermes OPENPROJECT_API_URL=$u" || bad "priv Hermes OPENPROJECT_API_URL=${u:-unset} (expected leela-op178)"
# 7b OpenProject image really 17.8
img=$(docker inspect -f '{{.Config.Image}}' leela-op178-openproject 2>/dev/null)
case "$img" in *17.8*) ok "OpenProject image $img" ;; *) warn "OpenProject image=$img (expected 17.8; may be sha-pinned)" ;; esac
# 7c private Hermes on BIND mounts (T10) + drift target volume absent
mt=$(docker inspect -f '{{range .Mounts}}{{.Type}}:{{.Source}} {{end}}' ki-basis-hermes 2>/dev/null)
case "$mt" in *bind:/root/.hermes*bind:/root/workspaces*|*bind:/root/workspaces*bind:/root/.hermes*) ok "priv Hermes on bind mounts (/root/.hermes,/root/workspaces)" ;; *) bad "priv Hermes mounts unexpected: $mt" ;; esac
if docker volume ls --format '{{.Name}}' 2>/dev/null | grep -q '^ki-basis-hermes-data$'; then bad "drift target volume ki-basis-hermes-data EXISTS (should not)"; else ok "drift target volume ki-basis-hermes-data absent"; fi
# 7d shared-db-net has the shared cluste
docker network inspect shared-db-net -f '{{range .Containers}}{{.Name}} {{end}}' 2>/dev/null | grep -q ki-basis-shared-postgres && ok "shared-db-net includes ki-basis-shared-postgres" || bad "shared-db-net missing ki-basis-shared-postgres"
# 7e keepalive alive
systemctl is-active openproject-keepalive >/dev/null 2>&1 && ok "openproject-keepalive systemd service active" || warn "openproject-keepalive not active"
ps -eo cmd 2>/dev/null | grep -q '[s]leep infinity' && ok "a held 'sleep infinity' keepalive session exists" || warn "no held sleep-infinity session (VM may idle-sleep)"
# 7f OpenProject 17.8 & Community memory/allocator bounds (Simulation F + Option 2A/2B + live /proc/<puma_pid>/environ + hocuspocus guard)
op_mem=$(docker inspect -f '{{.HostConfig.Memory}}' leela-op178-openproject 2>/dev/null || echo 0)
op_env=$(docker inspect -f '{{range .Config.Env}}{{println .}}{{end}}' leela-op178-openproject 2>/dev/null || true)
comm_mem=$(docker inspect -f '{{.HostConfig.Memory}}' community-openproject 2>/dev/null || echo 0)
comm_env=$(docker inspect -f '{{range .Config.Env}}{{println .}}{{end}}' community-openproject 2>/dev/null || true)
puma_live_env=$(docker exec -u app leela-op178-openproject bash -lc 'pid=$(pgrep -f "puma.*8080" | head -n1); [ -n "$pid" ] && xargs -0 -n1 -a /proc/$pid/environ && ps -T -p $pid -o comm' 2>/dev/null || true)
hp_node_running=$(docker exec leela-op178-openproject pgrep -f "node.*hocuspocus" 2>/dev/null || true)
if [ "$op_mem" = "1610612736" ] && [ "$comm_mem" = "1879048192" ] \
   && echo "$op_env" | grep -q '^OPENPROJECT_WEB_WORKERS=0$' \
   && echo "$comm_env" | grep -q '^OPENPROJECT_WEB_WORKERS=0$' \
   && echo "$op_env" | grep -q '^USE_JEMALLOC=true$' \
   && echo "$puma_live_env" | grep -q '^LD_PRELOAD=libjemalloc.so.2$' \
   && echo "$puma_live_env" | grep -q '^MALLOC_CONF=narenas:2,dirty_decay_ms:1000,muzzy_decay_ms:0,background_thread:true$' \
   && echo "$puma_live_env" | grep -q '^jemalloc_bg_thd$' \
   && [ -z "$hp_node_running" ]; then
  ok "OpenProject bounds, live Puma /proc environ & hocuspocus-disabled guard active (priv 1536M WEB_WORKERS=0 jemalloc_bg_thd no-hocuspocus; comm 1792M WEB_WORKERS=0)"
else
  bad "OpenProject bounds, live Puma /proc environ, or hocuspocus guard mismatch (priv_mem=$op_mem comm_mem=$comm_mem hp_pids=$hp_node_running)"
fi
# 7g shared-db-net DNS alias isolation (leela-op178-openproject must NOT alias 'openproject')
op_aliases=$(docker inspect -f '{{range (index .NetworkSettings.Networks "shared-db-net").Aliases}}{{.}} {{end}}' leela-op178-openproject 2>/dev/null || true)
case " $op_aliases " in
  *" openproject "*) bad "leela-op178-openproject still holds colliding 'openproject' alias on shared-db-net ($op_aliases)" ;;
  *" leela-openproject "*) ok "leela-op178-openproject shared-db-net aliases isolated ($op_aliases)" ;;
  *) bad "leela-op178-openproject shared-db-net aliases unexpected ($op_aliases)" ;;
esac

echo
echo "================ RESULT: PASS=$PASS  FAIL=$FAIL  WARN=$WARN ================"
[ "$FAIL" -eq 0 ] && echo "OVERALL: GREEN (no failures)" || echo "OVERALL: RED ($FAIL failures)"
exit $([ "$FAIL" -eq 0 ] && echo 0 || echo 1)
