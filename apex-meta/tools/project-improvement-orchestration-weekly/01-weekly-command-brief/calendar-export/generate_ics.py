#!/usr/bin/env python3
"""
generate_ics.py
Generates RFC 5545 compliant .ics calendar files for the APEX Weekly Command Brief flows.
Grounded in operator decisions: MoA (Website, Content, Invoices), IPOS, Sequencing, and Residual Flow.
"""

import os
from datetime import datetime, timezone

def generate_ics(output_path: str):
    events = [
        # Monday Nov 9
        {
            "uid": "apex-20261109-f1@apexai-os",
            "summary": "[APEX F1] Master of Arts: Content Production & Essay Pipeline (3x3)",
            "start": "20261109T090000",
            "end": "20261109T104500",
            "desc": (
                "Project: Master of Arts (Content Production)\n"
                "Weekly Target: Creative Essay & Media Publishing Pipeline\n\n"
                "=== 3x3 SPRINT CHECKLIST ===\n"
                "• S1 (Essay Framework):\n"
                "  1. Outline core thesis & field notes\n"
                "  2. Reconcile intellectual distinctions\n"
                "  3. Draft script outline\n"
                "• S2 (Asset Creation):\n"
                "  1. Record spoken-word narration\n"
                "  2. Edit audio hooks & balance frequencies\n"
                "  3. Format quotes and captions\n"
                "• S3 (Publishing Pipeline):\n"
                "  1. Format multi-channel distribution copy\n"
                "  2. Schedule publishing draft\n"
                "  3. Archive raw master recordings\n\n"
                "Flow Card: file:///artifacts/flows/2026-11-09/F1-card.md"
            ),
        },
        {
            "uid": "apex-20261109-f2@apexai-os",
            "summary": "[APEX F2] Master of Arts: Website Flexbox Navigation (3x3)",
            "start": "20261109T111500",
            "end": "20261109T123000",
            "desc": (
                "Project: Master of Arts Website ([OP #14, WP #163])\n"
                "Weekly Target: Modern Responsive Flexbox Navigation & Mobile Drawer\n\n"
                "=== 3x3 SPRINT CHECKLIST ===\n"
                "• S1 (CSS Flexbox Header):\n"
                "  1. Refactor CSS navigation bar with modern flexbox\n"
                "  2. Style navigation link states & active indicator\n"
                "  3. Format typography & container widths\n"
                "• S2 (Mobile Drawer Layout):\n"
                "  1. Implement mobile drawer layout & toggle hook\n"
                "  2. Build smooth slide-out hamburger animation\n"
                "  3. Test tablet and smartphone breakpoints\n"
                "• S3 (Deploy & Verification):\n"
                "  1. Cross-browser layout verification\n"
                "  2. Lighthouse performance & accessibility audit\n"
                "  3. Commit layout branch & staging deploy\n\n"
                "Flow Card: file:///artifacts/flows/2026-11-09/F2-card.md"
            ),
        },
        {
            "uid": "apex-20261109-f3@apexai-os",
            "summary": "[APEX F3] Investment / IPOS: Karakeep Deprecation & Docling Adapter (3x3)",
            "start": "20261109T133000",
            "end": "20261109T153000",
            "desc": (
                "Project: Investment / IPOS ([OP #16, WP #224 & #226])\n"
                "Weekly Target: Research Intake Pipeline & Evidence Ingestion\n\n"
                "=== 3x3 SPRINT CHECKLIST ===\n"
                "• S1 (WP #224 ADR-003 Karakeep Retirement):\n"
                "  1. Audit deprecated Karakeep import references\n"
                "  2. Formalize retirement decision record\n"
                "  3. Remove stale adapter mocks\n"
                "• S2 (WP #226 Docling & Trafilatura Ingestion):\n"
                "  1. Implement IBM Docling PDF extractor adapter\n"
                "  2. Wire Trafilatura web article parser\n"
                "  3. Verify structured JSON output schema\n"
                "• S3 (WP #233 Ingestion Test Harness):\n"
                "  1. Run sample document extraction benchmark\n"
                "  2. Verify error handling and timeouts\n"
                "  3. Write ingestion evidence receipt\n\n"
                "Flow Card: file:///artifacts/flows/2026-11-09/F3-card.md"
            ),
        },
        {
            "uid": "apex-20261109-f4@apexai-os",
            "summary": "[APEX F4] Residual Flow: Apartment, Sexy Content & Community (3x3)",
            "start": "20261109T160000",
            "end": "20261109T174500",
            "desc": (
                "Project: Residual Integration (Sequencing System)\n"
                "Weekly Target: Living Space, Creative Brand & Community Harmony\n\n"
                "=== 3x3 SPRINT CHECKLIST ===\n"
                "• S1 (Apartment & Art):\n"
                "  1. Workspace acoustic and ergonomic tune-up\n"
                "  2. Studio material sorting & canvas prep\n"
                "  3. Living space reset & visual declutter\n"
                "• S2 (Sexy Content):\n"
                "  1. Moodboard review & aesthetic lighting setup\n"
                "  2. Visual capture / photoshoot execution\n"
                "  3. High-tier photo grading & portfolio curation\n"
                "• S3 (Community & Traveling):\n"
                "  1. Peer network outreach & sync responses\n"
                "  2. Travel logistics & route planning review\n"
                "  3. Community event / meetup coordination\n\n"
                "Flow Card: file:///artifacts/flows/2026-11-09/F4-card.md"
            ),
        },

        # Tuesday Nov 10
        {
            "uid": "apex-20261110-f1@apexai-os",
            "summary": "[APEX F1] Master of Arts: Content Production & Video Slicing (3x3)",
            "start": "20261110T090000",
            "end": "20261110T104500",
            "desc": (
                "Project: Master of Arts (Content Production)\n"
                "=== 3x3 SPRINT CHECKLIST ===\n"
                "• S1: Cut short reel video clips from audio\n"
                "• S2: Generate visual cards & thumbnail graphics\n"
                "• S3: Multi-channel queue formatting & preview"
            ),
        },
        {
            "uid": "apex-20261110-f2@apexai-os",
            "summary": "[APEX F2] Master of Arts: Content Engine & Dynamic Routing (3x3)",
            "start": "20261110T111500",
            "end": "20261110T123000",
            "desc": (
                "Project: Master of Arts Website ([OP #14, WP #163])\n"
                "=== 3x3 SPRINT CHECKLIST ===\n"
                "• S1: Connect dynamic markdown content feed\n"
                "• S2: Responsive article layout test\n"
                "• S3: Internal link validation & static build"
            ),
        },
        {
            "uid": "apex-20261110-f3@apexai-os",
            "summary": "[APEX F3] Investment / IPOS: Trafilatura Ingestion & FRED Schema (3x3)",
            "start": "20261110T133000",
            "end": "20261110T153000",
            "desc": (
                "Project: Investment / IPOS ([OP #16, WP #226 & #230])\n"
                "=== 3x3 SPRINT CHECKLIST ===\n"
                "• S1: Implement web article text cleansing with Trafilatura\n"
                "• S2: FRED macro data schema mapping (WP #230)\n"
                "• S3: Pipeline integration test with fixture files"
            ),
        },
        {
            "uid": "apex-20261110-f4@apexai-os",
            "summary": "[APEX F4] Residual Flow: Apartment, Sexy Content & Community (3x3)",
            "start": "20261110T160000",
            "end": "20261110T174500",
            "desc": (
                "Project: Residual Integration\n"
                "=== 3x3 SPRINT CHECKLIST ===\n"
                "• S1 (Apartment & Art): Physical studio space refinement & artwork mounting\n"
                "• S2 (Sexy Content): Visual aesthetics, color palette fine-tuning\n"
                "• S3 (Community & Traveling): Travel packing checklist & travel itinerary sync"
            ),
        },

        # Wednesday Nov 11
        {
            "uid": "apex-20261111-f1@apexai-os",
            "summary": "[APEX F1] Master of Arts: Content Production & Longform Writing (3x3)",
            "start": "20261111T090000",
            "end": "20261111T104500",
            "desc": "Project: Master of Arts (Content Production)\n=== 3x3 SPRINT CHECKLIST ===\n• S1: Long-form deep dive essay draft\n• S2: Diagram & visual card generation\n• S3: Editorial polish & proofreading pass",
        },
        {
            "uid": "apex-20261111-f2@apexai-os",
            "summary": "[APEX F2] Master of Arts: Invoicing Schema & Tax Engine (3x3)",
            "start": "20261111T111500",
            "end": "20261111T123000",
            "desc": "Project: Master of Arts Business ([OP #7])\n=== 3x3 SPRINT CHECKLIST ===\n• S1: Define line-item JSON invoice schema\n• S2: Implement tax and subtotal formula unit tests\n• S3: Connect accounting export path & test schema",
        },
        {
            "uid": "apex-20261111-f3@apexai-os",
            "summary": "[APEX F3] Investment / IPOS: End-to-End Pipeline Harness (3x3)",
            "start": "20261111T133000",
            "end": "20261111T153000",
            "desc": "Project: Investment / IPOS ([OP #16, WP #233])\n=== 3x3 SPRINT CHECKLIST ===\n• S1: End-to-end reality validation script\n• S2: Ingestion failure recovery verification\n• S3: Execution evidence receipt generation",
        },
        {
            "uid": "apex-20261111-f4@apexai-os",
            "summary": "[APEX F4] Residual Flow: Apartment, Sexy Content & Community (3x3)",
            "start": "20261111T160000",
            "end": "20261111T174500",
            "desc": "Project: Residual Integration\n=== 3x3 SPRINT CHECKLIST ===\n• S1 (Apartment & Art): Studio layout reset & lighting adjustment\n• S2 (Sexy Content): Visual narrative & photo session\n• S3 (Community & Traveling): Connect with creative peers & community updates",
        },

        # Thursday Nov 12
        {
            "uid": "apex-20261112-f1@apexai-os",
            "summary": "[APEX F1] Master of Arts: Content Production & Audio Narration (3x3)",
            "start": "20261112T090000",
            "end": "20261112T104500",
            "desc": "Project: Master of Arts (Content Production)\n=== 3x3 SPRINT CHECKLIST ===\n• S1: Narrative voiceover recording cut\n• S2: Background audio balancing & mastering\n• S3: Podcast / audio package bundling",
        },
        {
            "uid": "apex-20261112-f2@apexai-os",
            "summary": "[APEX F2] Master of Arts: Automated PDF Billing Generator (3x3)",
            "start": "20261112T111500",
            "end": "20261112T123000",
            "desc": "Project: Master of Arts Business ([OP #7])\n=== 3x3 SPRINT CHECKLIST ===\n• S1: HTML invoice template & print stylesheet\n• S2: HTML-to-PDF rendering engine\n• S3: Batch billing run & visual diff audit",
        },
        {
            "uid": "apex-20261112-f3@apexai-os",
            "summary": "[APEX F3] Investment / IPOS: Cockpit UX Dashboard Architecture (3x3)",
            "start": "20261112T133000",
            "end": "20261112T153000",
            "desc": "Project: Investment / IPOS ([OP #16, WP #232])\n=== 3x3 SPRINT CHECKLIST ===\n• S1: Multi-tier operator dashboard wireframe\n• S2: Live query views for research intake\n• S3: Status indicator component build",
        },
        {
            "uid": "apex-20261112-f4@apexai-os",
            "summary": "[APEX F4] Residual Flow: Apartment, Sexy Content & Community (3x3)",
            "start": "20261112T160000",
            "end": "20261112T174500",
            "desc": "Project: Residual Integration\n=== 3x3 SPRINT CHECKLIST ===\n• S1 (Apartment & Art): Artwork finishing & framing\n• S2 (Sexy Content): Image curation & high-res exports\n• S3 (Community & Traveling): Travel destination scouting & accommodation checks",
        },

        # Friday Nov 13
        {
            "uid": "apex-20261113-f1@apexai-os",
            "summary": "[APEX F1] Master of Arts: Content Production & Weekly Newsletter (3x3)",
            "start": "20261113T090000",
            "end": "20261113T104500",
            "desc": "Project: Master of Arts (Content Production)\n=== 3x3 SPRINT CHECKLIST ===\n• S1: Synthesis newsletter drafting\n• S2: Email template build & test dispatch\n• S3: Multi-channel broadcast release",
        },
        {
            "uid": "apex-20261113-f2@apexai-os",
            "summary": "[APEX F2] Master of Arts: Invoicing E2E & Production Deploy (3x3)",
            "start": "20261113T111500",
            "end": "20261113T123000",
            "desc": "Project: Master of Arts ([OP #14 & #7])\n=== 3x3 SPRINT CHECKLIST ===\n• S1: End-to-end invoice generation & PDF verify\n• S2: Production website build & staging merge\n• S3: Live release smoke test & signoff",
        },
        {
            "uid": "apex-20261113-f3@apexai-os",
            "summary": "[APEX F3] Investment / IPOS: Telegram Digest Dispatch Verification (3x3)",
            "start": "20261113T133000",
            "end": "20261113T153000",
            "desc": "Project: Investment / IPOS ([OP #16, WP #227])\n=== 3x3 SPRINT CHECKLIST ===\n• S1: Verify telegram dispatch adapter\n• S2: Test dry-run weekly research summary payload\n• S3: Register delivery evidence log",
        },
        {
            "uid": "apex-20261113-f4@apexai-os",
            "summary": "[APEX F4] Residual Flow: Apartment, Sexy Content & Community (3x3)",
            "start": "20261113T160000",
            "end": "20261113T174500",
            "desc": "Project: Residual Integration\n=== 3x3 SPRINT CHECKLIST ===\n• S1 (Apartment & Art): Studio clean room reset & material restocking\n• S2 (Sexy Content): Brand aesthetic review & visual lookbook sync\n• S3 (Community & Traveling): Weekend social plan & trip confirmation",
        },

        # Saturday Nov 14 (D017: Saturday Precap & Buffer)
        {
            "uid": "apex-20261114-precap@apexai-os",
            "summary": "[APEX PRECAP] Weekly Retrospective & Next Week Precap (D017)",
            "start": "20261114T090000",
            "end": "20261114T110000",
            "desc": (
                "Weekly Precap & Retrospective Session (Decision D017)\n\n"
                "=== 3x3 SPRINT CHECKLIST ===\n"
                "• S1: Audit week evidence receipts & flow metrics\n"
                "• S2: Scan OpenProject status shifts & dependency changes\n"
                "• S3: Formulate next week's Command Brief & Flow proposals"
            ),
        },
        {
            "uid": "apex-20261114-buffer@apexai-os",
            "summary": "[APEX BUFFER] Workspace Clean Room Reset & System Maintenance",
            "start": "20261114T113000",
            "end": "20261114T130000",
            "desc": "Overflow buffer, documentation reconciliation, workstation clean room reset.",
        },
    ]

    lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//ApexAI OS//Weekly Orchestration Flow Calendar//EN",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
        "X-WR-CALNAME:APEX Flow Calendar (2026-W45/W46)",
        "X-WR-TIMEZONE:Europe/Berlin",
    ]

    now_stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    for ev in events:
        lines.append("BEGIN:VEVENT")
        lines.append(f"UID:{ev['uid']}")
        lines.append(f"DTSTAMP:{now_stamp}")
        lines.append(f"DTSTART;TZID=Europe/Berlin:{ev['start']}")
        lines.append(f"DTEND;TZID=Europe/Berlin:{ev['end']}")
        lines.append(f"SUMMARY:{ev['summary']}")
        
        # Escape newlines for iCalendar
        escaped_desc = ev['desc'].replace("\n", "\\n")
        lines.append(f"DESCRIPTION:{escaped_desc}")
        lines.append("STATUS:CONFIRMED")
        lines.append("TRANSP:OPAQUE")
        lines.append("BEGIN:VALARM")
        lines.append("ACTION:DISPLAY")
        lines.append("DESCRIPTION:APEX Flow Reminder")
        lines.append("TRIGGER:-PT10M")
        lines.append("END:VALARM")
        lines.append("END:VEVENT")

    lines.append("END:VCALENDAR")
    lines.append("")

    content = "\r\n".join(lines)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated {output_path} with {len(events)} events.")

if __name__ == "__main__":
    out_dir = os.path.dirname(os.path.abspath(__file__))
    target_file = os.path.join(out_dir, "2026-W45-flows.ics")
    generate_ics(target_file)
