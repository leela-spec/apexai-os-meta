#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPT="$ROOT/scripts/restore-test-paperless.sh"
EXPECTED_SHA="$(tr -d '\r\n[:space:]' < "$ROOT/tests/fixtures/paperless-m5.expected.sha256")"
TEST_ROOT="$(mktemp -d "${TMPDIR:-/tmp}/ki-basis-restore-oracle-test.XXXXXX")"
trap 'rm -rf "$TEST_ROOT"' EXIT

make_backup_skeleton() {
  local dest="$1"
  mkdir -p "$dest/postgres" "$dest/volumes"
  : > "$dest/postgres/paperless.dump"
  for name in paperless_data paperless_media paperless_export paperless_consume; do
    : > "$dest/volumes/$name.tar.gz"
  done
}

fake_bin="$TEST_ROOT/bin"
mkdir -p "$fake_bin"
cat > "$fake_bin/docker" <<'FAKE_DOCKER'
#!/usr/bin/env bash
printf '%s\n' "$*" >> "$FAKE_DOCKER_LOG"
exit 97
FAKE_DOCKER
chmod +x "$fake_bin/docker"

missing_sha_backup="$TEST_ROOT/missing-sha"
make_backup_skeleton "$missing_sha_backup"
: > "$TEST_ROOT/docker.log"
if env PATH="$fake_bin:$PATH" \
    FAKE_DOCKER_LOG="$TEST_ROOT/docker.log" \
    PAPERLESS_RESTORE_EXPECT_SHA256_FILE="$TEST_ROOT/does-not-exist.sha256" \
    "$SCRIPT" "$missing_sha_backup" >"$TEST_ROOT/missing-sha.log" 2>&1; then
  echo 'FAIL: missing expected SHA should exit non-zero' >&2
  exit 1
fi
grep -q 'Expected Paperless restore SHA256 is required' "$TEST_ROOT/missing-sha.log" || {
  echo 'FAIL: missing expected SHA did not fail at the oracle gate' >&2
  exit 1
}
test ! -s "$TEST_ROOT/docker.log" || {
  echo 'FAIL: Docker was called before the missing SHA was rejected' >&2
  exit 1
}
echo 'PASS: missing expected SHA fails before Docker'

missing_media_backup="$TEST_ROOT/missing-media"
make_backup_skeleton "$missing_media_backup"
rm "$missing_media_backup/volumes/paperless_media.tar.gz"
if env PATH="$fake_bin:$PATH" \
    FAKE_DOCKER_LOG="$TEST_ROOT/docker.log" \
    PAPERLESS_RESTORE_EXPECT_SHA256="$EXPECTED_SHA" \
    "$SCRIPT" "$missing_media_backup" >"$TEST_ROOT/missing-media.log" 2>&1; then
  echo 'FAIL: missing media archive should exit non-zero' >&2
  exit 1
fi
grep -q 'Missing backup artifact: .*paperless_media.tar.gz' "$TEST_ROOT/missing-media.log"
echo 'PASS: missing media archive fails before Docker'

live_backup="${1:-}"
if [[ -z "$live_backup" ]]; then
  echo 'PASS: preflight oracle tests complete (live restore tests not requested)'
  exit 0
fi

wrong_sha="$(printf '0%.0s' {1..64})"
if PAPERLESS_RESTORE_EXPECT_SHA256="$wrong_sha" "$SCRIPT" "$live_backup" >"$TEST_ROOT/wrong-sha.log" 2>&1; then
  echo 'FAIL: wrong expected SHA should fail the real Paperless restore' >&2
  exit 1
fi
grep -q 'Restored document SHA256 mismatch' "$TEST_ROOT/wrong-sha.log"
echo 'PASS: wrong expected SHA fails against real Paperless download'

if PAPERLESS_RESTORE_EXPECT_TITLE='Definitely Not The Restored Title' \
    "$SCRIPT" "$live_backup" >"$TEST_ROOT/wrong-title.log" 2>&1; then
  echo 'FAIL: wrong expected title should fail the real Paperless restore' >&2
  exit 1
fi
grep -q 'Restored document not found' "$TEST_ROOT/wrong-title.log"
echo 'PASS: wrong expected title fails against real Paperless search'

"$SCRIPT" "$live_backup"
echo 'PASS: correct independent SHA and title pass the real Paperless restore'
