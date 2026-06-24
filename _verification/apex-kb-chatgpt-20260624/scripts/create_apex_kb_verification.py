import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "_verification" / "apex-kb-chatgpt-20260624"
BACKUP_REF = "origin/backup/apex-kb-before-chatgpt-20260624"
COMMITS = [
    "ac259b632f77d0836aef722b1b640392f623f24d",
    "96b21e861c738fd2ccb2eaa7abecf509a924a487",
    "daa8e25e1758192ffc9632e9629070a38d7c1d8d",
    "cc9f69ad44280615368877d6234bc3983d7fba54",
    "ae59348c953b9a946638c4bd25f1a1f013e2c064",
    "d5e9dd0eac2ec44797764a3558f5087ff62c503d",
    "84757a7b0498b76710c78bae0b1e25d48c2bfc48",
]
EXPECTED = {
    ".claude/skills/apex-kb/references/source-custody-and-read-verification.md": "A",
    ".claude/skills/apex-kb/templates/source-intake-lock-template.md": "A",
    ".claude/skills/apex-kb/SKILL.md": "M",
    ".claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md": "M",
    ".claude/skills/apex-kb/templates/ingest-analysis-template.md": "M",
    ".claude/skills/apex-kb/package-manifest.md": "M",
    ".claude/skills/apex-kb/references/kb-contract.md": "M",
}
ADDED = [path for path, status in EXPECTED.items() if status == "A"]
MODIFIED = [path for path, status in EXPECTED.items() if status == "M"]


def git(*args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=check,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def line_count(path: Path) -> int:
    return len(path.read_text(encoding="utf-8", errors="replace").splitlines())


def commit_name_status(commit: str) -> list[dict[str, str]]:
    out = git("show", "--name-status", "--format=", "--no-renames", commit).stdout
    rows = []
    for line in out.splitlines():
        if not line.strip():
            continue
        parts = line.split("\t")
        rows.append({"status": parts[0], "path": parts[-1]})
    return rows


def exists_in_ref(ref: str, path: str) -> bool:
    return git("cat-file", "-e", f"{ref}:{path}", check=False).returncode == 0


def write_ledger() -> dict:
    touched: dict[str, str] = {}
    for commit in COMMITS:
        for row in commit_name_status(commit):
            touched[row["path"]] = row["status"]

    unexpected = sorted(set(touched) - set(EXPECTED))
    missing = sorted(set(EXPECTED) - set(touched))
    wrong_status = sorted(
        path for path, status in touched.items() if path in EXPECTED and EXPECTED[path] != status
    )
    status = "pass" if not unexpected and not missing and not wrong_status else "fail"
    notes = []
    if missing:
        notes.append(f"Missing expected files: {', '.join(missing)}")
    if unexpected:
        notes.append(f"Unexpected files: {', '.join(unexpected)}")
    if wrong_status:
        notes.append(f"Files with unexpected status: {', '.join(wrong_status)}")

    data = {
        "backup_ref": BACKUP_REF,
        "backup_commit": git("rev-parse", BACKUP_REF).stdout.strip(),
        "current_head": git("rev-parse", "HEAD").stdout.strip(),
        "known_chatgpt_commits": COMMITS,
        "touched_files": sorted(touched),
        "added_files": sorted(ADDED),
        "modified_files": sorted(MODIFIED),
        "unexpected_files": unexpected,
        "verification_status": status,
        "notes": notes,
    }
    (OUT / "changed-files-ledger.json").write_text(
        json.dumps(data, indent=2) + "\n", encoding="utf-8"
    )
    return data


def write_added_files_report() -> bool:
    lines = [
        "# Added Files Report",
        "",
        f"Backup ref: `{BACKUP_REF}`",
        "",
        "| File | Current exists | Existed before backup | Lines | SHA-256 |",
        "| --- | --- | --- | ---: | --- |",
    ]
    ok = True
    for rel in ADDED:
        current = ROOT / rel
        current_exists = current.exists()
        before_exists = exists_in_ref(BACKUP_REF, rel)
        if (not current_exists) or before_exists:
            ok = False
        count = line_count(current) if current_exists else 0
        digest = sha256(current) if current_exists else ""
        lines.append(
            f"| `{rel}` | {'yes' if current_exists else 'no'} | "
            f"{'yes' if before_exists else 'no'} | {count} | `{digest}` |"
        )
    lines.append("")
    (OUT / "reports" / "added-files-report.md").write_text("\n".join(lines), encoding="utf-8")
    return ok


def main() -> int:
    (OUT / "reports").mkdir(parents=True, exist_ok=True)
    ledger = write_ledger()
    added_ok = write_added_files_report()
    if ledger["verification_status"] != "pass" or not added_ok:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
