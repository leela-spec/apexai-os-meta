#!/usr/bin/env bash
# =============================================================================
# infra-health-test.sh — READ-ONLY health / efficiency / claimed-fact verifier
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

hr "2. Expected containers running (13)"
for c in ki-basis-hermes ki-basis-paperless ki-basis-firefly ki-basis-nginx ki-basis-valkey \
         community-hermes community-paperless community-firefly community-nginx community-openproject community-valkey \
         leela-op178-openproject ki-basis-shared-postgres; do
  st=$(docker inspect -f '{{.State.Status}}' "$c" 2>/dev/null || true)
  if [ "$st" = "running" ]; then ok "$c running"; else bad "$c not running (state: ${st:-absent})"; fi
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
check_http "comm-hermes"      "http://127.0.0.1:9642/health"  "200"
check_http "priv-nginx"       "http://127.0.0.1:8084/healthz" "200"
check_http "comm-nginx"       "http://127.0.0.1:9084/healthz" "200"
check_http "openproject-17.8" "http://127.0.0.1:8083/"        "302"

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
# 7d shared-db-net has the shared cluster
docker network inspect shared-db-net -f '{{range .Containers}}{{.Name}} {{end}}' 2>/dev/null | grep -q ki-basis-shared-postgres && ok "shared-db-net includes ki-basis-shared-postgres" || bad "shared-db-net missing ki-basis-shared-postgres"
# 7e keepalive alive
systemctl is-active openproject-keepalive >/dev/null 2>&1 && ok "openproject-keepalive systemd service active" || warn "openproject-keepalive not active"
ps -eo cmd 2>/dev/null | grep -q '[s]leep infinity' && ok "a held 'sleep infinity' keepalive session exists" || warn "no held sleep-infinity session (VM may idle-sleep)"

echo
echo "================ RESULT: PASS=$PASS  FAIL=$FAIL  WARN=$WARN ================"
[ "$FAIL" -eq 0 ] && echo "OVERALL: GREEN (no failures)" || echo "OVERALL: RED ($FAIL failures)"
exit $([ "$FAIL" -eq 0 ] && echo 0 || echo 1)
