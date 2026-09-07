"""
Populate OpenProject with Equinox Hamburg Fundraiser Work Packages
Creates 19 structured work packages across 6 functional teams for Project ID 3,
establishing cross-references to Pretix tickets, Paperless documents, and Firefly transactions.
"""

import argparse
import os
from typing import Any, Dict, List
import httpx

INSTANCE_PORTS = {
    "private": 8082,
    "community": 9082,
}

DEFAULT_API_KEY = "21bf818464d30262e7012561ac934ad423df60d33d1debf29bf6880ea8c1f7ad"

OPENPROJECT_URL = os.environ.get(
    "OPENPROJECT_URL",
    f"http://127.0.0.1:{INSTANCE_PORTS.get(os.environ.get('KI_INSTANCE', 'private'), 8082)}"
)
API_KEY = os.environ.get("OPENPROJECT_API_KEY", DEFAULT_API_KEY)
PROJECT_ID = int(os.environ.get("OPENPROJECT_PROJECT_ID", "3"))

AUTH = ("apikey", API_KEY)
HEADERS = {
    "Content-Type": "application/json",
}

# Status mapping:
# 1: New, 6: Scheduled, 7: In progress, 12: Closed
# Types: 1: Task, 2: Milestone, 3: Phase


def create_work_package(client: httpx.Client, wp: Dict[str, Any]) -> int:
    payload = {
        "subject": wp["subject"],
        "description": {
            "format": "markdown",
            "raw": wp["description"],
        },
        "startDate": wp.get("startDate"),
        "dueDate": wp.get("dueDate"),
        "_links": {
            "type": {"href": f"/api/v3/types/{wp.get('type_id', 1)}"},
            "status": {"href": f"/api/v3/statuses/{wp.get('status_id', 1)}"},
        },
    }
    r = client.post(
        f"{OPENPROJECT_URL}/api/v3/projects/{PROJECT_ID}/work_packages",
        auth=AUTH,
        headers=HEADERS,
        json=payload,
    )
    if r.status_code in (200, 201):
        wp_id = r.json()["id"]
        print(f"[OK] WP #{wp_id}: {wp['subject']} (Status: {wp.get('status_id')})")
        return wp_id
    else:
        print(f"[ERR] WP Failed: {wp['subject']} -> {r.status_code}: {r.text}")
        return None


def run():
    with httpx.Client(timeout=30.0) as client:
        work_packages: List[Dict[str, Any]] = [
            # Team 1: Core Circle & Production Lead
            {
                "subject": "[Core] Project Charter & Budget Approval (€11.3k Gross / €5.4k Surplus)",
                "description": (
                    "**Approved by Safer Space e.V. Board.**\n\n"
                    "- Capacity: 320 attendees (Pretix)\n"
                    "- Gross Revenue: €11,300.00\n"
                    "- Projected Net Surplus: +€5,488.00\n"
                    "- Canonical budget: `MasterOfArts/Lika/Verein & Finances/Budgets/Fundraiser_Hamburg_2026/Budget_Equinox_Hamburg_2026.md`"
                ),
                "startDate": "2026-10-01",
                "dueDate": "2026-10-10",
                "type_id": 1,
                "status_id": 12,  # Closed
            },
            {
                "subject": "[Core] GLS Bank Escrow & Funding Allocation",
                "description": (
                    "Initial operational reserve of €5,000.00 confirmed on GLS Bank account.\n"
                    "Firefly III Asset Account ID: 1 (`GLS Bank — Safer Space e.V. (Girokonto)`)."
                ),
                "startDate": "2026-10-05",
                "dueDate": "2026-10-12",
                "type_id": 1,
                "status_id": 12,  # Closed
            },
            {
                "subject": "[Core] MILESTONE: All Systems Go Production Gate",
                "description": "Final cross-team sign-off before load-in and door opening.",
                "startDate": "2026-11-19",
                "dueDate": "2026-11-19",
                "type_id": 2,  # Milestone
                "status_id": 6,  # Scheduled
            },

            # Team 2: Venue Logistics & Infrastructure
            {
                "subject": "[Logistics] Equinox Venue Lease Contract & €7,500 Bar Turnover Guarantee Finalized",
                "description": (
                    "Lease agreement executed with Equinox Event GmbH.\n\n"
                    "- Bar minimum turnover: **€7,500.00 brutto**\n"
                    "- Security (4 certified bouncers) & cleaning included if turnover achieved\n"
                    "- Paperless Document: `Equinox_Hamburg_Venue_Lease_Contract.pdf`"
                ),
                "startDate": "2026-10-10",
                "dueDate": "2026-10-15",
                "type_id": 1,
                "status_id": 12,  # Closed
            },
            {
                "subject": "[Logistics] Security Deposit (€1,500) Transferred to Equinox Escrow",
                "description": (
                    "Transferred via GLS Bank online banking.\n"
                    "Firefly III Transaction ID #6.\n"
                    "Refund scheduled after Saturday post-event walkthrough."
                ),
                "startDate": "2026-10-25",
                "dueDate": "2026-10-28",
                "type_id": 1,
                "status_id": 12,  # Closed
            },
            {
                "subject": "[Logistics] Sixt 3.5t Van Booking & Transport Schedule",
                "description": (
                    "IVECO Daily 3.5t reserved at Sixt Altona (48h rental).\n"
                    "Paperless Document: `Sixt_Transporter_Rental_Invoice.pdf`\n"
                    "Firefly III Transaction ID #9 (€215.80)."
                ),
                "startDate": "2026-11-10",
                "dueDate": "2026-11-19",
                "type_id": 1,
                "status_id": 7,  # In progress
            },
            {
                "subject": "[Logistics] Venue Load-in & Power Grid Distribution",
                "description": "Equinox loading bay access from 14:00. Heavy power distribution for 12kW sound system and light rig.",
                "startDate": "2026-11-20",
                "dueDate": "2026-11-20",
                "type_id": 1,
                "status_id": 6,  # Scheduled
            },
            {
                "subject": "[Logistics] MILESTONE: Teardown & Venue Handover Walkthrough",
                "description": "Final inspection with Equinox facility manager. Kaution refund release confirmation.",
                "startDate": "2026-11-21",
                "dueDate": "2026-11-21",
                "type_id": 2,  # Milestone
                "status_id": 6,  # Scheduled
            },

            # Team 3: Sound, Lighting & Visual Art
            {
                "subject": "[Sound/Visuals] Nordic Sound & Light 12kW PA & Rigging Contract",
                "description": (
                    "L-Acoustics 12kW PA, RoboWash LED moving heads, GrandMA console.\n"
                    "Paperless Document: `Sound_Visual_Rental_Invoice_Hamburg.pdf`\n"
                    "Firefly III Transaction ID #7 (€2,915.50)."
                ),
                "startDate": "2026-10-15",
                "dueDate": "2026-11-18",
                "type_id": 1,
                "status_id": 12,  # Closed
            },
            {
                "subject": "[Sound/Visuals] Performance Cage & Pole Stage Structural Rigging Safety Check",
                "description": "Visual inspection and load-bearing test for elevated pole stage and sensual performance cage.",
                "startDate": "2026-11-15",
                "dueDate": "2026-11-20",
                "type_id": 1,
                "status_id": 7,  # In progress
            },
            {
                "subject": "[Sound/Visuals] Sound Level Monitoring & 99 dB(A) Leq Compliance Management",
                "description": "Continuous decibel logging to ensure Hamburg noise regulations compliance on main floor.",
                "startDate": "2026-11-20",
                "dueDate": "2026-11-21",
                "type_id": 1,
                "status_id": 6,  # Scheduled
            },

            # Team 4: Performers, DJs & Stage Management
            {
                "subject": "[Lineup] Artist Agreements Signed (Mira Luna, Klangtherapie, Soma & Shade, Aura Dawn)",
                "description": (
                    "4 DJ and artist contracts executed.\n"
                    "Paperless Document: `DJ_Booking_Agreements_Lineup.pdf`\n"
                    "Firefly III Transaction ID #8 (€1,750.00)."
                ),
                "startDate": "2026-10-20",
                "dueDate": "2026-11-10",
                "type_id": 1,
                "status_id": 12,  # Closed
            },
            {
                "subject": "[Lineup] Stage Management Timetable & Artist Hospitality",
                "description": "21:00-23:30 Mira Luna | 23:30-02:00 Klangtherapie | 02:00-04:00 Soma & Shade | 04:00-05:30 Aura Dawn. Rider prep.",
                "startDate": "2026-11-12",
                "dueDate": "2026-11-20",
                "type_id": 1,
                "status_id": 7,  # In progress
            },

            # Team 5: Lika Awareness, Care & Consent Team
            {
                "subject": "[Care/Consent] Lika Care Team SOP & Consent Guidelines Ratified",
                "description": (
                    "Harm reduction, active bystander, affirmative consent protocols approved.\n"
                    "Paperless Document: `Lika_Awareness_Care_Consent_Guidelines.pdf`\n"
                    "Aligned with Lika Shift Planning OS Governance v1.1."
                ),
                "startDate": "2026-10-15",
                "dueDate": "2026-10-20",
                "type_id": 1,
                "status_id": 12,  # Closed
            },
            {
                "subject": "[Care/Consent] Care Station Setup & Supplies Procurement",
                "description": (
                    "Procured from Bio-Großmarkt Hamburg: electrolyte packs, organic fruit, vegan chocolate, teas, earplugs.\n"
                    "Paperless Document: `Catering_Bar_Snacks_Receipt.pdf`\n"
                    "Firefly III Transaction ID #10 (€284.60)."
                ),
                "startDate": "2026-11-10",
                "dueDate": "2026-11-19",
                "type_id": 1,
                "status_id": 7,  # In progress
            },
            {
                "subject": "[Care/Consent] Cuddle Puddle Host Roster & Shift Rotation (Lika OS Fairness Matrix)",
                "description": "3 volunteer shifts of 2-3 people with mandatory rest intervals. Diagram: `Lika_OS_Volunteer_Shift_Overview.png`.",
                "startDate": "2026-11-14",
                "dueDate": "2026-11-20",
                "type_id": 1,
                "status_id": 7,  # In progress
            },

            # Team 6: Reception, Door & Bar Coordination
            {
                "subject": "[Door/Bar] Pretix Ticketing Shop Configuration & Quota Management (320 Max)",
                "description": (
                    "Pretix shop sold out (80 Early Bird, 180 Regular, 60 Supporter).\n"
                    "Mandatory consent acknowledgment: 100% (320/320).\n"
                    "Paperless Document: `Pretix_Ticketing_Payout_Settlement.pdf`\n"
                    "Firefly III Transactions #2, #3, #4, #5."
                ),
                "startDate": "2026-10-15",
                "dueDate": "2026-11-15",
                "type_id": 1,
                "status_id": 12,  # Closed
            },
            {
                "subject": "[Door/Bar] Pretix Mobile Scanner App Setup & Guest List Sync",
                "description": "PretixSCAN app configured on 3 mobile devices for rapid optical QR code intake at Equinox main door.",
                "startDate": "2026-11-16",
                "dueDate": "2026-11-20",
                "type_id": 1,
                "status_id": 7,  # In progress
            },
            {
                "subject": "[Door/Bar] Equinox Bar Turnover Monitoring Liaison (€7,500 Target)",
                "description": "Hourly check-ins with Equinox shift manager to monitor POS bar receipts against €7,500 threshold.",
                "startDate": "2026-11-20",
                "dueDate": "2026-11-21",
                "type_id": 1,
                "status_id": 6,  # Scheduled
            },
        ]

        created_count = 0
        for wp in work_packages:
            w_id = create_work_package(client, wp)
            if w_id:
                created_count += 1

        print(f"Total Work Packages created in OpenProject: {created_count}/{len(work_packages)}")


def parse_args():
    parser = argparse.ArgumentParser(description="Populate OpenProject with Equinox Hamburg Fundraiser Work Packages")
    parser.add_argument("-i", "--instance", choices=["private", "community"], default=os.environ.get("KI_INSTANCE", "private"),
                        help="Target instance: private (port 8082) or community (port 9082). Default: private")
    parser.add_argument("-u", "--url", default=None, help="Explicit OpenProject base URL (overrides --instance and OPENPROJECT_URL)")
    parser.add_argument("-k", "--api-key", default=None, help="Explicit OpenProject API key")
    parser.add_argument("-p", "--project-id", type=int, default=None, help="Target OpenProject project ID (default: 3)")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    if args.url:
        OPENPROJECT_URL = args.url
    elif "OPENPROJECT_URL" in os.environ:
        OPENPROJECT_URL = os.environ["OPENPROJECT_URL"]
    else:
        OPENPROJECT_URL = f"http://127.0.0.1:{INSTANCE_PORTS[args.instance]}"

    if args.api_key:
        API_KEY = args.api_key
    AUTH = ("apikey", API_KEY)

    if args.project_id is not None:
        PROJECT_ID = args.project_id

    print(f"==> Connecting to OpenProject at: {OPENPROJECT_URL} (Project ID: {PROJECT_ID})")
    run()
