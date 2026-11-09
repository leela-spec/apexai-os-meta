"""One-way mirror of the weekly dispersal bundle into apexai-os-meta.

DD-15: MasterOfArts is the single source of truth. A bidirectional mirror of one
file across two Git repositories produces conflicts with no merge authority, so
this script refuses to copy in reverse.

Dry-run by default. Pass --apply to write.

    python sync_dispersal.py                # report what would change
    python sync_dispersal.py --apply        # write the mirror
    python sync_dispersal.py --check        # exit 1 if the mirror is stale (CI)
"""

import argparse
import hashlib
import sys
from pathlib import Path

SOURCE = Path(__file__).resolve().parent
MIRROR = Path(
    "C:/GitDev/apexai-os-meta/apex-meta/tools/"
    "project-improvement-orchestration-weekly/02-weekly-dispersal"
)

# Only these are mirrored. The generator's output is mirrored, not regenerated
# there, so the mirror cannot diverge by running a different Python.
TRACKED = [
    "index.md",
    "SPEC-WEEKLY-DISPERSAL.okf.md",
    "ASSUMPTIONS-AND-DECISIONS-REGISTER.md",
    "PRECAP-INTEGRATION-ANALYSIS.md",
    "slot-inventory.json",
    "build_slot_inventory.py",
    "sync_dispersal.py",
]

BANNER = (
    "<!-- MIRROR. Source of truth: MasterOfArts/Sequencing/dispersal/ (DD-15).\n"
    "     Edits here are overwritten by sync_dispersal.py. -->\n"
)


def mirrored_bytes(src, name):
    """Exactly what this file should look like in the mirror.

    Markdown carries a banner under its frontmatter so an editor there sees it
    is a copy. JSON and Python take no banner: a comment would break the parse.
    The comparison uses this, not the raw source, or --check would report every
    banner-carrying file stale forever.
    """
    raw = src.read_bytes()
    if not name.endswith(".md"):
        return raw
    text = raw.decode("utf-8")
    if text.startswith("<!-- MIRROR"):
        return raw
    parts = text.split("---", 2)
    if len(parts) == 3 and parts[0] == "":
        text = f"---{parts[1]}---\n{BANNER}{parts[2].lstrip(chr(10))}"
    else:
        text = BANNER + text
    return text.encode("utf-8")


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else None


def digest_bytes(data):
    return hashlib.sha256(data).hexdigest()


def guard_direction():
    """Refuse to run from inside the mirror, whichever way the paths point."""
    here = SOURCE.resolve()
    if MIRROR.resolve() == here or MIRROR.resolve() in here.parents:
        sys.exit(
            "REFUSED: this copy lives inside the mirror. The mirror is one-way "
            "(DD-15); run the script from MasterOfArts/Sequencing/dispersal/."
        )
    if "apexai-os-meta" in here.parts:
        sys.exit(
            "REFUSED: running from apexai-os-meta. MasterOfArts is the source of "
            "truth (DD-15); nothing syncs back."
        )


def plan():
    rows = []
    for name in TRACKED:
        src, dst = SOURCE / name, MIRROR / name
        if not src.exists():
            rows.append((name, "MISSING AT SOURCE", None))
            continue
        want = mirrored_bytes(src, name)
        have = digest(dst)
        if have is None:
            rows.append((name, "new", want))
        elif digest_bytes(want) != have:
            rows.append((name, "changed", want))
        else:
            rows.append((name, "same", None))
    return rows


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true", help="write the mirror")
    ap.add_argument("--check", action="store_true",
                    help="exit 1 if the mirror is stale; writes nothing")
    args = ap.parse_args()

    guard_direction()
    rows = plan()

    missing = [n for n, st, _ in rows if st == "MISSING AT SOURCE"]
    stale = [(n, st) for n, st, _ in rows if st in ("new", "changed")]

    width = max(len(n) for n, _, _ in rows)
    for name, status, _ in rows:
        print(f"  {name.ljust(width)}  {status}")
    print(f"\n  source {SOURCE}\n  mirror {MIRROR}")

    if missing:
        sys.exit(f"\nREFUSED: tracked file(s) absent at source: {', '.join(missing)}")

    if args.check:
        if stale:
            print(f"\nSTALE: {len(stale)} file(s) differ. Run with --apply.")
            sys.exit(1)
        print("\nmirror is current")
        return

    if not args.apply:
        print(f"\ndry run — {len(stale)} file(s) would be written. Pass --apply.")
        return

    MIRROR.mkdir(parents=True, exist_ok=True)
    written = 0
    for name, status, want in rows:
        if want is None:
            continue
        (MIRROR / name).write_bytes(want)
        written += 1
        print(f"  wrote {name}")

    print(f"\nmirrored {written} file(s)")


if __name__ == "__main__":
    main()
