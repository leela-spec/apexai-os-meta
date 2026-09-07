"""
Unified Verification Suite for Fundraiser Hamburg — Equinox 2026
Audits all 4 modules: Pretix Adapter, Staged & Real File Archives, OpenProject, Firefly III, Paperless-ngx.
"""

import argparse
import os
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import httpx
from pretix_adapter import PretixAdapter

INSTANCE_PORTS = {
    "private": {"openproject": 8082, "firefly": 8086, "paperless": 8010},
    "community": {"openproject": 9082, "firefly": 9086, "paperless": 9010},
}

DEFAULT_INSTANCE = os.environ.get("KI_INSTANCE", "private")

OPENPROJECT_URL = os.environ.get(
    "OPENPROJECT_URL",
    f"http://127.0.0.1:{INSTANCE_PORTS.get(DEFAULT_INSTANCE, INSTANCE_PORTS['private'])['openproject']}"
)
OPENPROJECT_KEY = os.environ.get("OPENPROJECT_KEY", "21bf818464d30262e7012561ac934ad423df60d33d1debf29bf6880ea8c1f7ad")

DEFAULT_FIREFLY_TOKEN = (
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIwMWEwNWU2Yy1lYTliLTcyZTMtOTNjMS02OTE3OTcyZjgwNjEiLCJqdGkiOiI2"
    "Yjg5ZWE4MWYyN2EyM2I2YjQwZGFhYmJkZjE3OWExMWM5ZTU1YzQ2ZjMwMjRhYzIxNTYwNGJkZWZiZGI3ZTRmMWFjODIzMmVhZmM3YWNkYSIsIm"
    "lhdCI6MTc4ODU5MjA5Ni43Mzk2MDQsIm5iZiI6MTc4ODU5MjA5Ni43Mzk2MDYsImV4cCI6MTgyMDEyODA5Ni42NTQ2MjIsInN1YiI6IjEiLCJ"
    "zY29wZXMiOltdfQ.pEwRwpTIXJjCyPniAnRSiFut5VsO7X3CcITXqvq-uY5mojtu7y3lEo_lFoSPH3dwaHsOqczx57QzMRHg5M87FybHNzjBCY"
    "rRCa0XdyX3P8azyzW_a-tEzzi-Gj3sBTKKA6ipNuV5yZ8wzN18BksQny0hXIAc84Y9V2ydWztRUBQxPMPMXwC7ZukFSGrmmLt8nqb_yCFoHxE7"
    "WklxivZVyJaEl_ZplXrjcNjH2_Tn9C1_9g-EnDTXteMFLOFIBsIPv3D2dj3eOh6Kfi1utCBuqnGted7BVRyDJ6SQzgOVv8kBkft5tGdVFvqVTZi"
    "j7bMXnlWhIUeLSZTf-oqZ94DwvZXFh135-2JBE7QBDIVNZ43WgQp04NBa_onqVJLE0EPkA1oJClkGVxjzqnX8cx-MED3hKfHrb7eBz2eFmvzez"
    "lnpFwtkTbbStojlT9r9Vswmht6n1c6gmB3GrpEhOV9gUs0ThMDVP7VieF9LC6AB14A_AGkaqUUf6OPxqZ4qBvrCKQcwghEINxmDUWKoMZ7BWPcY"
    "R4e29GokXbANBktE-GC27gBoaQpHQY3YVoRK0GRMz1DbyxngbQk-aWVZUBtrYks4KOcfI1s1mb_IWE9Nt8WoDhxsWQJvcFqqPWXlfflwNNb-Wb"
    "min9p__lL3Rxnv3fHqod8hlZ_FoZ_bKuLLraM"
)

FIREFLY_URL = os.environ.get(
    "FIREFLY_URL",
    f"http://127.0.0.1:{INSTANCE_PORTS.get(DEFAULT_INSTANCE, INSTANCE_PORTS['private'])['firefly']}"
)
FIREFLY_TOKEN = os.environ.get("FIREFLY_TOKEN", DEFAULT_FIREFLY_TOKEN)

PAPERLESS_URL = os.environ.get(
    "PAPERLESS_URL",
    f"http://127.0.0.1:{INSTANCE_PORTS.get(DEFAULT_INSTANCE, INSTANCE_PORTS['private'])['paperless']}"
)
PAPERLESS_TOKEN = os.environ.get("PAPERLESS_TOKEN", "c0b591378103b3328b1bb3269fcf581191864a06")

STAGING_DIR = Path(os.environ.get("STAGING_DIR", "C:/GitDev/apexai-os-meta/ki-basis/fixtures/fundraiser_hamburg"))
LIKA_DIR = Path(os.environ.get("LIKA_DIR", "C:/GitDev/MasterOfArts/Lika/Verein & Finances/Budgets/Fundraiser_Hamburg_2026"))


def check(name: str, passed: bool, detail: str = ""):
    icon = "[PASS]" if passed else "[FAIL]"
    print(f"{icon} {name} {detail}")
    if not passed:
        sys.exit(1)


def audit():
    print("=" * 70)
    print("STARTING AUDIT: FUNDRAISER HAMBURG EQUINOX 2026")
    print("=" * 70)

    # 1. Pretix Ticketing Adapter
    print("\n--- 1. Pretix Ticketing Module ---")
    adapter = PretixAdapter()
    summary = adapter.get_event_summary()
    check("Pretix Organizer", summary["organizer"] == "safer-space-ev", f"({summary['organizer_name']})")
    check("Pretix Capacity", summary["capacity"] == 320, f"({summary['capacity']} attendees, sold out)")
    check("Pretix Gross Revenue", summary["gross_revenue"] == 11300.0, f"(€{summary['gross_revenue']:.2f})")
    check("Pretix Net Payout", summary["net_payout"] == 10833.9, f"(€{summary['net_payout']:.2f})")
    check("Pretix Mandatory Consent", any(q["required"] for q in summary["questions"]), "Mandatory consent enforced")

    # 2. Filesystem & Archives
    print("\n--- 2. Staging & Real-World File Archives ---")
    expected_staging_files = [
        "Equinox_Hamburg_Venue_Lease_Contract.pdf",
        "Lika_Awareness_Care_Consent_Guidelines.pdf",
        "Sound_Visual_Rental_Invoice_Hamburg.pdf",
        "DJ_Booking_Agreements_Lineup.pdf",
        "Catering_Bar_Snacks_Receipt.pdf",
        "Sixt_Transporter_Rental_Invoice.pdf",
        "Pretix_Ticketing_Payout_Settlement.pdf",
        "Lika_Equinox_Event_Poster.png",
        "Equinox_Venue_Floorplan_Zones.png",
        "Lika_OS_Volunteer_Shift_Overview.png",
    ]
    for f in expected_staging_files:
        check(f"Staging file: {f}", (STAGING_DIR / f).exists(), f"({(STAGING_DIR / f).stat().st_size} bytes)")

    check("Real Budget Overview", (LIKA_DIR / "Budget_Equinox_Hamburg_2026.md").exists(), "Found in MasterOfArts/Lika")
    check("Real Contract Mirrored", (LIKA_DIR / "Equinox_Hamburg_Venue_Lease_Contract.pdf").exists(), "Found in MasterOfArts/Lika")

    with httpx.Client(timeout=15.0) as client:
        # 3. OpenProject Audit
        print("\n--- 3. OpenProject Project & Work Packages (:8082) ---")
        r_p = client.get(f"{OPENPROJECT_URL}/api/v3/projects/3", auth=("apikey", OPENPROJECT_KEY))
        check("OpenProject Project Exists", r_p.status_code == 200, f"ID: {r_p.json().get('id')}, Name: '{r_p.json().get('name')}'")

        import json as py_json
        filter_all_statuses = py_json.dumps([{"status_id": {"operator": "*", "values": []}}])
        r_wp = client.get(f"{OPENPROJECT_URL}/api/v3/projects/3/work_packages?filters={filter_all_statuses}&pageSize=50", auth=("apikey", OPENPROJECT_KEY))
        check("OpenProject Work Packages Query", r_wp.status_code == 200)
        wps = r_wp.json().get("_embedded", {}).get("elements", [])
        total_wps = r_wp.json().get("total", len(wps))
        check("Work Packages Count >= 15", total_wps >= 15, f"(Found: {total_wps} work packages)")

        # Verify cross-references
        wps_with_paperless = [wp for wp in wps if "Paperless" in wp.get("description", {}).get("raw", "")]
        check("Cross-References: WPs referencing Paperless", len(wps_with_paperless) >= 6, f"(Found: {len(wps_with_paperless)} WPs with document links)")

        # 4. Firefly III Audit
        print("\n--- 4. Firefly III Financial Ledger (:8086) ---")
        ff_headers = {"Authorization": f"Bearer {FIREFLY_TOKEN}", "Accept": "application/vnd.api+json"}
        r_acc = client.get(f"{FIREFLY_URL}/api/v1/accounts/1", headers=ff_headers)
        check("Firefly GLS Bank Account", r_acc.status_code == 200, f"Name: {r_acc.json()['data']['attributes']['name']}")

        r_tx = client.get(f"{FIREFLY_URL}/api/v1/accounts/1/transactions", headers=ff_headers)
        check("Firefly Transactions Query", r_tx.status_code == 200)
        txs = r_tx.json().get("data", [])
        check("Transactions Count >= 8", len(txs) >= 8, f"(Found: {len(txs)} transactions)")

        # Verify bar guarantee note in transactions
        notes_concat = " ".join([t["attributes"]["transactions"][0].get("notes") or "" for t in txs])
        check("Bar Guarantee Note in Ledger", "7.500 EUR" in notes_concat or "7.500" in notes_concat, "Found €7,500 guarantee reference in Firefly notes")

        # 5. Paperless-ngx Audit
        print("\n--- 5. Paperless-ngx Document Archival (:8010) ---")
        pl_headers = {"Authorization": f"Token {PAPERLESS_TOKEN}"}
        r_docs = client.get(f"{PAPERLESS_URL}/api/documents/", headers=pl_headers)
        check("Paperless-ngx Query", r_docs.status_code == 200)
        doc_count = r_docs.json().get("count", 0)
        check("Paperless Ingested Documents >= 7", doc_count >= 7, f"(Found: {doc_count} total documents)")

        r_tags = client.get(f"{PAPERLESS_URL}/api/tags/", headers=pl_headers)
        tag_names = [t["name"] for t in r_tags.json().get("results", [])]
        for expected_tag in ["KI-BASIS-TEST", "LIKA", "SAFER-SPACE-EV", "PRETIX", "HAMBURG-FUNDRAISER-2026"]:
            check(f"Paperless Tag: {expected_tag}", expected_tag in tag_names)

    print("\n" + "=" * 70)
    print("ALL AUDIT VERIFICATIONS PASSED WITH ZERO ERRORS!")
    print("=" * 70)


def parse_args():
    parser = argparse.ArgumentParser(description="Unified Verification Suite for Fundraiser Hamburg — Equinox 2026")
    parser.add_argument("-i", "--instance", choices=["private", "community"], default=os.environ.get("KI_INSTANCE", "private"),
                        help="Target instance: private or community. Default: private")
    parser.add_argument("--openproject-url", default=None, help="Explicit OpenProject base URL")
    parser.add_argument("--firefly-url", default=None, help="Explicit Firefly base URL")
    parser.add_argument("--paperless-url", default=None, help="Explicit Paperless base URL")
    parser.add_argument("--openproject-key", default=None, help="OpenProject API key")
    parser.add_argument("--firefly-token", default=None, help="Firefly Bearer token")
    parser.add_argument("--paperless-token", default=None, help="Paperless token")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    ports = INSTANCE_PORTS[args.instance]

    if args.openproject_url:
        OPENPROJECT_URL = args.openproject_url
    elif "OPENPROJECT_URL" in os.environ:
        OPENPROJECT_URL = os.environ["OPENPROJECT_URL"]
    else:
        OPENPROJECT_URL = f"http://127.0.0.1:{ports['openproject']}"

    if args.firefly_url:
        FIREFLY_URL = args.firefly_url
    elif "FIREFLY_URL" in os.environ:
        FIREFLY_URL = os.environ["FIREFLY_URL"]
    else:
        FIREFLY_URL = f"http://127.0.0.1:{ports['firefly']}"

    if args.paperless_url:
        PAPERLESS_URL = args.paperless_url
    elif "PAPERLESS_URL" in os.environ:
        PAPERLESS_URL = os.environ["PAPERLESS_URL"]
    else:
        PAPERLESS_URL = f"http://127.0.0.1:{ports['paperless']}"

    if args.openproject_key:
        OPENPROJECT_KEY = args.openproject_key
    if args.firefly_token:
        FIREFLY_TOKEN = args.firefly_token
    if args.paperless_token:
        PAPERLESS_TOKEN = args.paperless_token

    print(f"==> Target Instance: {args.instance}")
    print(f"    OpenProject: {OPENPROJECT_URL}")
    print(f"    Firefly:     {FIREFLY_URL}")
    print(f"    Paperless:   {PAPERLESS_URL}")
    audit()
