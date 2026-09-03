#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPT="$ROOT/scripts/backup-stack.sh"
TEST_ROOT="$(mktemp -d "${TMPDIR:-/tmp}/ki-basis-backup-test.XXXXXX")"
trap 'rm -rf "$TEST_ROOT"' EXIT

FAKE_BIN="$TEST_ROOT/bin"
PAYLOAD="$TEST_ROOT/payload"
mkdir -p "$FAKE_BIN" "$PAYLOAD"
printf 'ordinary state\n' > "$PAYLOAD/state.txt"
printf 'must not be backed up\n' > "$PAYLOAD/.env"

cat > "$FAKE_BIN/docker" <<'FAKE_DOCKER'
#!/usr/bin/env bash
set -euo pipefail
printf '%s\n' "$*" >> "$FAKE_DOCKER_LOG"

command_name="${1:-}"
shift || true
case "$command_name" in
  compose|stop|start)
    exit 0
    ;;
  inspect)
    printf 'helper-image\r\n'
    exit 0
    ;;
  volume)
    [[ "${1:-}" == "inspect" ]] || exit 90
    volume="${2:-}"
    [[ "$volume" != "${FAKE_MISSING_VOLUME:-}" ]]
    ;;
  exec)
    printf 'disposable database dump\n'
    ;;
  run)
    args=("$@")
    mount=""
    entrypoint_seen=0
    forgiving_archive=0
    for ((i = 0; i < ${#args[@]}; i++)); do
      if [[ "${args[$i]}" == "-v" ]]; then
        mount="${args[$((i + 1))]}"
      fi
      if [[ "${args[$i]}" == "--entrypoint" && "${args[$((i + 1))]:-}" == "sh" ]]; then
        entrypoint_seen=1
      fi
      if [[ "${args[$i]}" == *'|| true'* ]]; then
        forgiving_archive=1
      fi
    done
    volume="${mount%%:*}"
    if [[ -n "${FAKE_MISSING_VOLUME:-}" || "${FAKE_HELPER_FAILURE:-0}" == 1 ]]; then
      [[ "$forgiving_archive" -eq 1 ]] && exit 0
      exit 93
    fi
    if [[ "${FAKE_CORRUPT_ARCHIVE:-0}" == 1 ]]; then
      printf 'not a gzip archive'
      exit 0
    fi
    [[ "$entrypoint_seen" -eq 1 ]] || exit 92
    for arg in "${args[@]}"; do
      [[ "$arg" != *$'\r'* && "$arg" != *$'\n'* ]] || exit 91
    done
    if [[ "$volume" == "ki-basis-hermes-data" && " $* " == *' --exclude=./.env '* ]]; then
      tar -czf - --exclude='./.env' -C "$FAKE_PAYLOAD" .
    else
      tar -czf - -C "$FAKE_PAYLOAD" .
    fi
    ;;
  *)
    exit 95
    ;;
esac
FAKE_DOCKER
chmod +x "$FAKE_BIN/docker"

run_expected_failure() {
  local name="$1"
  shift
  local case_root="$TEST_ROOT/$name"
  mkdir -p "$case_root"
  : > "$case_root/docker.log"
  if env PATH="$FAKE_BIN:$PATH" \
      ENV_FILE="$ROOT/.env.example" \
      FAKE_DOCKER_LOG="$case_root/docker.log" \
      FAKE_PAYLOAD="$PAYLOAD" \
      "$@" \
      "$SCRIPT" "$case_root/backup" >"$case_root/output.log" 2>&1; then
    echo "FAIL: $name should exit non-zero" >&2
    return 1
  fi
  grep -Eq '^compose .*start ' "$case_root/docker.log" || {
    echo "FAIL: $name did not restart application writers through cleanup" >&2
    return 1
  }
  ! grep -q 'Backup complete' "$case_root/output.log" || {
    echo "FAIL: $name printed Backup complete" >&2
    return 1
  }
  echo "PASS: $name"
}

run_expected_failure nonexistent-volume \
  FAKE_MISSING_VOLUME=ki-basis-valkey-data
run_expected_failure helper-command-failure \
  FAKE_HELPER_FAILURE=1
run_expected_failure corrupt-archive \
  FAKE_CORRUPT_ARCHIVE=1

success_root="$TEST_ROOT/success"
mkdir -p "$success_root"
: > "$success_root/docker.log"
env PATH="$FAKE_BIN:$PATH" \
  ENV_FILE="$ROOT/.env.example" \
  FAKE_DOCKER_LOG="$success_root/docker.log" \
  FAKE_PAYLOAD="$PAYLOAD" \
  "$SCRIPT" "$success_root/backup" >"$success_root/output.log" 2>&1

grep -q 'Backup complete' "$success_root/output.log"
test -s "$success_root/backup/volumes/hermes_data.tar.gz"
tar -tzf "$success_root/backup/volumes/hermes_data.tar.gz" >/dev/null
if tar -tzf "$success_root/backup/volumes/hermes_data.tar.gz" | grep -Eq '(^|/)\.env$'; then
  echo 'FAIL: Hermes archive contains .env' >&2
  exit 1
fi
echo 'PASS: valid archives complete and Hermes .env is excluded'
