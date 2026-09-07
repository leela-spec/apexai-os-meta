"""
Generator for Fundraiser Hamburg — Equinox Assets
Generates 6+ official PDF documents and 3 visual diagrams for Lika / Safer Space e.V.,
saving them into both the ki-basis staging directory and MasterOfArts/Lika permanent budget archive.
"""

import shutil
from datetime import datetime
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

STAGING_DIR = Path("C:/GitDev/apexai-os-meta/ki-basis/fixtures/fundraiser_hamburg")
LIKA_BUDGET_DIR = Path("C:/GitDev/MasterOfArts/Lika/Verein & Finances/Budgets/Fundraiser_Hamburg_2026")

STAGING_DIR.mkdir(parents=True, exist_ok=True)
LIKA_BUDGET_DIR.mkdir(parents=True, exist_ok=True)

# Brand colors
COLOR_DARK = colors.HexColor("#2E2A5C")
COLOR_VIOLET = colors.HexColor("#7B61FF")
COLOR_BG_GRAY = colors.HexColor("#F9F8FD")
COLOR_BORDER = colors.HexColor("#CCCCCC")

styles = getSampleStyleSheet()
title_style = ParagraphStyle("T", parent=styles["Heading1"], fontSize=18, leading=22, textColor=COLOR_DARK, fontName="Helvetica-Bold")
subtitle_style = ParagraphStyle("S", parent=styles["Heading2"], fontSize=12, leading=16, textColor=COLOR_VIOLET, fontName="Helvetica-Bold")
body_style = ParagraphStyle("B", parent=styles["Normal"], fontSize=9, leading=13, textColor=colors.HexColor("#222222"))
bold_body = ParagraphStyle("BB", parent=body_style, fontName="Helvetica-Bold")


def build_pdf(filename: str, elements: list):
    path = STAGING_DIR / filename
    doc = SimpleDocTemplate(str(path), pagesize=A4, leftMargin=36, rightMargin=36, topMargin=36, bottomMargin=36)
    doc.build(elements)
    # Copy to permanent Lika budget folder
    shutil.copy(path, LIKA_BUDGET_DIR / filename)
    print(f"[PDF] Created {filename}")


# 1. Equinox Venue Lease Contract
def create_venue_contract():
    elems = [
        Paragraph("MIETVERTRAG & VERANSTALTUNGSVEREINBARUNG", title_style),
        Paragraph("Equinox Club Hamburg × Safer Space e.V. (Temple of Lika)", subtitle_style),
        Spacer(1, 10),
        HRFlowable(width="100%", thickness=1.5, color=COLOR_DARK, spaceAfter=12),
    ]
    meta = [
        [Paragraph("<b>Vermieter:</b>", bold_body), Paragraph("Equinox Event GmbH & Co. KG<br/>Große Elbstraße 142, 22767 Hamburg", body_style),
         Paragraph("<b>Mieter:</b>", bold_body), Paragraph("Safer Space e.V. (Temple of Lika)<br/>Amtsgericht Hamburg VR 24198", body_style)],
        [Paragraph("<b>Veranstaltung:</b>", bold_body), Paragraph("Fundraiser Hamburg — Equinox 2026", body_style),
         Paragraph("<b>Datum & Zeit:</b>", bold_body), Paragraph("20. Nov 2026, 21:00 – 05:30 Uhr<br/>(Aufbau ab 14:00 Uhr, Abbau bis 13:00 Uhr)", body_style)],
    ]
    t_meta = Table(meta, colWidths=[90, 170, 90, 170])
    t_meta.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
    elems.extend([t_meta, Spacer(1, 12)])

    clauses = [
        ("§ 1 Gegenstand der Anmietung",
         "Vermietet werden die gesamten Räumlichkeiten des Equinox Hamburg: Haupt-Tanzfläche, erhöhte Pole-Bühne, Performance-Käfig, Untere Chill-Lounge sowie der abgetrennte Rückzugs- und Spielbereich im Obergeschoss."),
        ("§ 2 Mindestumsatzgarantie & Abrechnung",
         "Die Parteien vereinbaren einen garantierten Mindest-Getränkeumsatz an der Bar in Höhe von <b>7.500,00 EUR brutto</b>. Bei Erreichen des Mindestumsatzes sind die Bereitstellung des Sicherheitspersonals (4 zertifizierte Tür- und Sicherheitskräfte) sowie die Endreinigung vollständig abgegolten. Bei Unterschreitung haftet der Mieter für den Differenzbetrag."),
        ("§ 3 Kaution & Zahlungsmodalitäten",
         "Der Mieter leistet eine Sicherungskaution in Höhe von 1.500,00 EUR auf das Geschäftskonto des Vermieters bis zum 01.11.2026."),
        ("§ 4 Hausrecht, Awareness & Safer Space",
         "Das Hausrecht wird gemeinschaftlich ausgeübt. Der Mieter stellt ein eigenes, geschultes Lika Awareness- und Care-Team. Das Tür- und Einlasspersonal agiert im Einklang mit der Lika Consent-Policy."),
        ("§ 5 Lärmschutz & Behördliche Auflagen",
         "Der Schallpegel auf der Tanzfläche ist auf maximal 99 dB(A) Leq gemäß Hamburger Immissionsschutzverordnung begrenzt."),
    ]
    for title, text in clauses:
        elems.append(Paragraph(title, subtitle_style))
        elems.append(Paragraph(text, body_style))
        elems.append(Spacer(1, 6))

    elems.append(Spacer(1, 10))
    signatures = [
        [Paragraph("Hamburg, den 15.10.2026<br/><br/>___________________________<br/>Equinox Event GmbH", body_style),
         Paragraph("Hamburg, den 15.10.2026<br/><br/>___________________________<br/>Safer Space e.V. (Vorstand)", body_style)]
    ]
    t_sig = Table(signatures, colWidths=[260, 260])
    elems.append(t_sig)
    build_pdf("Equinox_Hamburg_Venue_Lease_Contract.pdf", elems)


# 2. Lika Awareness & Care Consent Guidelines
def create_awareness_guidelines():
    elems = [
        Paragraph("LIKA CARE TEAM — AWARENESS & CONSENT GUIDELINES", title_style),
        Paragraph("Standard Operating Procedure (SOP) | Equinox Hamburg 2026", subtitle_style),
        Spacer(1, 10),
        HRFlowable(width="100%", thickness=1.5, color=COLOR_VIOLET, spaceAfter=12),
    ]
    sections = [
        ("1. Core Philosophy & Safer Space Manifesto",
         "Lika events exist to cultivate authentic sensual expression, dance culture, and community trust. Affirmative, continuous, and enthusiastic consent is mandatory. A clear 'No' is respected immediately, and silence or ambiguity always equals 'No'."),
        ("2. Shift Structure & Active Presence",
         "The Care Team operates in 3 distinct shifts of 2-3 persons each, marked with discreet violet light bands. At least one Care Lead is stationed in the Cuddle Puddle Retreat, while two roving Angels patrol the Dance Floor, Cage, and Upper Area."),
        ("3. De-escalation & Incident Response Protocol",
         "Step 1: Check-in with the affected person in a quiet zone (Lower Lounge or Care Corner).<br/>"
         "Step 2: Prioritize emotional safety and emotional grounding.<br/>"
         "Step 3: If boundary violations occurred, escalate to Core Circle and Door Lead for guest expulsion without debate.<br/>"
         "Step 4: Complete an incident record in the Lika Shift Planning OS log."),
        ("4. Harm Reduction & Physical Care",
         "Free drinking water, electrolyte tablets, organic fruit, earplugs, barrier contraceptives, and menstrual products are available at the Care Station at zero cost."),
        ("5. Volunteer Care & Debriefing",
         "Every Care volunteer is entitled to a mandatory 2-hour rest window between shifts and a group debriefing session at 05:45 with the Core Circle."),
    ]
    for title, text in sections:
        elems.append(Paragraph(title, subtitle_style))
        elems.append(Paragraph(text, body_style))
        elems.append(Spacer(1, 8))
    build_pdf("Lika_Awareness_Care_Consent_Guidelines.pdf", elems)


# 3. Sound & Visual Rental Invoice
def create_sound_invoice():
    elems = [
        Paragraph("RECHNUNG — NORDIC SOUND & LIGHT HAMBURG", title_style),
        Paragraph("Rechnungsnummer: R-2026-8812 | Datum: 18.11.2026", subtitle_style),
        Spacer(1, 10),
        HRFlowable(width="100%", thickness=1.5, color=COLOR_DARK, spaceAfter=12),
    ]
    info = [
        [Paragraph("<b>Rechnungsempfänger:</b><br/>Safer Space e.V.<br/>z.Hd. Lika Produktion<br/>Große Brunnenstraße 63, 22763 Hamburg", body_style),
         Paragraph("<b>Leistungsempfänger / Lieferort:</b><br/>Equinox Club Hamburg<br/>Große Elbstraße 142, 22767 Hamburg<br/>Lieferdatum: 20.11.2026", body_style)]
    ]
    elems.extend([Table(info, colWidths=[260, 260]), Spacer(1, 12)])

    items = [
        ["Pos.", "Bezeichnung / Spezifikation", "Menge", "Einzelpreis", "Gesamtpreis"],
        ["1", "L-Acoustics 12kW PA-System (4x SB18 Subs, 4x ARCS II)", "1 Set", "1.200,00 €", "1.200,00 €"],
        ["2", "RoboWash LED Moving Heads & DMX GrandMA Console", "6 Stk", "75,00 €", "450,00 €"],
        ["3", "Pioneer DJ Set (2x CDJ-3000, 1x DJM-900NXS2)", "1 Set", "250,00 €", "250,00 €"],
        ["4", "Traversen-Rigging & Sicherheitsprüfung (Bühne & Käfig)", "Pauschal", "350,00 €", "350,00 €"],
        ["5", "Auf- und Abbau / Techniker-Bereitschaft vor Ort", "10 Std", "20,00 €", "200,00 €"],
        ["", "<b>Nettobetrag</b>", "", "", "<b>2.450,00 €</b>"],
        ["", "Umsatzsteuer 19%", "", "", "465,50 €"],
        ["", "<b>RECHNUNGSBETRAG (Brutto)</b>", "", "", "<b>2.915,50 €</b>"],
    ]
    t = Table([[Paragraph(c, bold_body if i in (0, 6, 8) else body_style) for c in row] for i, row in enumerate(items)], colWidths=[35, 255, 60, 85, 85])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), COLOR_DARK),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, 5), 0.5, COLOR_BORDER),
        ("BACKGROUND", (0, 8), (-1, 8), colors.HexColor("#EAE6FA")),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    elems.extend([t, Spacer(1, 15)])
    elems.append(Paragraph("Zahlbar rein netto innerhalb von 14 Tagen auf das Konto bei der Hamburger Sparkasse. IBAN: DE44 2005 0550 ...", body_style))
    build_pdf("Sound_Visual_Rental_Invoice_Hamburg.pdf", elems)


# 4. DJ Booking Agreements & Lineup
def create_dj_contracts():
    elems = [
        Paragraph("KÜNSTLERVERTRÄGE & LINEUP-VEREINBARUNG", title_style),
        Paragraph("Safer Space e.V. (Lika Music Curation) — Equinox Hamburg 2026", subtitle_style),
        Spacer(1, 10),
        HRFlowable(width="100%", thickness=1.5, color=COLOR_DARK, spaceAfter=12),
    ]
    artists = [
        ["Künstler / DJ", "Slot / Uhrzeit", "Genre / Ausrichtung", "Gage (netto)", "Status"],
        ["Mira Luna", "21:00 – 23:30", "Sensual Melodic Deep / Warmup", "400,00 €", "Bestätigt / Vertrag vorliegend"],
        ["Kollektiv Klangtherapie", "23:30 – 02:00", "Hypnotic Driving Groove & Vocals", "500,00 €", "Bestätigt / Vertrag vorliegend"],
        ["Soma & Shade", "02:00 – 04:00", "Ecstatic Peak Time Techno", "500,00 €", "Bestätigt / Vertrag vorliegend"],
        ["Aura Dawn", "04:00 – 05:30", "Organic Ambient / Sunrise Landing", "350,00 €", "Bestätigt / Vertrag vorliegend"],
        ["<b>Gesamthonorar</b>", "<b>21:00 – 05:30</b>", "<b>4 Acts</b>", "<b>1.750,00 €</b>", "<b>Vollständig gebucht</b>"],
    ]
    t = Table([[Paragraph(c, bold_body if i in (0, 5) else body_style) for c in row] for i, row in enumerate(artists)], colWidths=[120, 95, 155, 75, 75])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), COLOR_DARK),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.5, COLOR_BORDER),
        ("BACKGROUND", (0, 5), (-1, 5), COLOR_BG_GRAY),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    elems.extend([t, Spacer(1, 12)])
    elems.append(Paragraph("<b>Hospitality & Rider:</b> Gesunde Verpflegung, pflanzliche Snacks, alkoholfreie Erfrischungen, sowie je 2 Gästelistenplätze pro Act.", body_style))
    build_pdf("DJ_Booking_Agreements_Lineup.pdf", elems)


# 5. Catering & Care Station Receipt
def create_catering_receipt():
    elems = [
        Paragraph("BELEG / QUITTUNG — BIO-GROSSMARKT HAMBURG", title_style),
        Paragraph("Kunden-Nr: 441092 | Datum: 19.11.2026 | Beleg: BG-89124", subtitle_style),
        Spacer(1, 10),
        HRFlowable(width="100%", thickness=1.5, color=COLOR_DARK, spaceAfter=12),
    ]
    receipt_items = [
        ["Artikel", "Menge", "Einzelpreis", "Gesamt"],
        ["Bio-Bananen & Äpfel Kisten (Care Station)", "4 Kisten", "22,50 €", "90,00 €"],
        ["Elektrolyt-Pulver Zitrone & Beere (Dosen)", "6 Dosen", "14,90 €", "89,40 €"],
        ["Vegane Bio-Schokodrops & Nüsse (5kg Sack)", "1 Sack", "45,20 €", "45,20 €"],
        ["Ingwer-Tee & Kräutermischungen Großpackung", "3 Packungen", "12,00 €", "36,00 €"],
        ["Gläser & Thermobehälter Pfandgebühr", "2 Einheiten", "12,00 €", "24,00 €"],
        ["<b>Summe Netto</b>", "", "", "<b>284,60 €</b>"],
        ["<b>Gesamtbetrag Bar gezahlt / EC</b>", "", "", "<b>284,60 €</b>"],
    ]
    t = Table([[Paragraph(c, bold_body if i in (0, 6, 7) else body_style) for c in row] for i, row in enumerate(receipt_items)], colWidths=[240, 90, 90, 100])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), COLOR_DARK),
        ("GRID", (0, 0), (-1, -1), 0.5, COLOR_BORDER),
        ("BACKGROUND", (0, 7), (-1, 7), colors.HexColor("#EAE6FA")),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    elems.extend([t, Spacer(1, 12)])
    elems.append(Paragraph("Verwendungszweck: Versorgung Care-Team, Awareness-Retreat und Gäste-Wohlbefinden.", body_style))
    build_pdf("Catering_Bar_Snacks_Receipt.pdf", elems)


# 6. Sixt Transporter Invoice
def create_sixt_invoice():
    elems = [
        Paragraph("SIXT RENT-A-CAR — RECHNUNG TRANSPORTER", title_style),
        Paragraph("Mietvertragsnr: 948271014 | Station Hamburg Altona", subtitle_style),
        Spacer(1, 10),
        HRFlowable(width="100%", thickness=1.5, color=COLOR_DARK, spaceAfter=12),
    ]
    items = [
        ["Position", "Zeitraum / Details", "Betrag"],
        ["IVEVO Daily 3.5t Kastenwagen", "19.11. 12:00 – 21.11. 14:00 (48 Std)", "150,00 €"],
        ["Vollkasko- und Diebstahlschutz (SB 0€)", "2 Tage", "38,00 €"],
        ["Diesel-Kraftstoff Pauschale", "120 km gefahren", "27,80 €"],
        ["<b>Gesamtbetrag (inkl. MwSt.)</b>", "Gezahlt per Firmenkreditkarte Safer Space e.V.", "<b>215,80 €</b>"],
    ]
    t = Table([[Paragraph(c, bold_body if i in (0, 4) else body_style) for c in row] for i, row in enumerate(items)], colWidths=[200, 200, 120])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), COLOR_DARK),
        ("GRID", (0, 0), (-1, -1), 0.5, COLOR_BORDER),
        ("BACKGROUND", (0, 4), (-1, 4), colors.HexColor("#EAE6FA")),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    elems.extend([t, Spacer(1, 12)])
    elems.append(Paragraph("Einsatz: Transport 12kW Tonanlage, Lichttraversen, Deko und Bühnenaufbauten von Lager nach Equinox Hamburg.", body_style))
    build_pdf("Sixt_Transporter_Rental_Invoice.pdf", elems)


# Visual Assets Generation using Pillow
def generate_visual_assets():
    # 1. Event Poster
    img_poster = Image.new("RGB", (800, 1200), color="#1B1736")
    draw = ImageDraw.Draw(img_poster)

    # Gradient-like top decorative bar
    draw.rectangle([(0, 0), (800, 15)], fill="#7B61FF")
    draw.rectangle([(0, 15), (800, 25)], fill="#9D88FF")

    # Titles and details
    draw.text((400, 120), "TEMPLE OF LIKA", fill="#FFFFFF", anchor="mm", font_size=42)
    draw.text((400, 175), "presents", fill="#C5BAF7", anchor="mm", font_size=20)
    draw.text((400, 230), "EQUINOX HAMBURG", fill="#7B61FF", anchor="mm", font_size=52)
    draw.text((400, 290), "Community Fundraiser & Sensory Gathering", fill="#E5E0FA", anchor="mm", font_size=22)

    # Decorative frame
    draw.rectangle([(50, 340), (750, 780)], outline="#7B61FF", width=2)
    draw.text((400, 390), "MUSIC • ART • SENSUALITY • CONSENT", fill="#FFFFFF", anchor="mm", font_size=24)
    draw.text((400, 445), "FRIDAY, 20 NOVEMBER 2026", fill="#FFD700", anchor="mm", font_size=28)
    draw.text((400, 490), "21:00 — 05:30 CET", fill="#FFFFFF", anchor="mm", font_size=20)

    draw.text((400, 560), "VENUE: EQUINOX CLUB HAMBURG", fill="#FFFFFF", anchor="mm", font_size=24)
    draw.text((400, 600), "Große Elbstraße 142 • 22767 Hamburg", fill="#C5BAF7", anchor="mm", font_size=18)

    draw.text((400, 670), "LINEUP", fill="#7B61FF", anchor="mm", font_size=20)
    draw.text((400, 715), "MIRA LUNA • KLANGTHERAPIE • SOMA & SHADE • AURA DAWN", fill="#FFFFFF", anchor="mm", font_size=16)

    # Bottom ticketing block
    draw.rectangle([(50, 820), (750, 1050)], fill="#252047", outline="#4A3F9F", width=2)
    draw.text((400, 860), "TICKETING VIA PRETIX (320 CAPACITY LIMIT)", fill="#7B61FF", anchor="mm", font_size=20)
    draw.text((400, 910), "Early Bird: 25 €  •  Regular: 35 €  •  Supporter: 50 €", fill="#FFFFFF", anchor="mm", font_size=19)
    draw.text((400, 960), "100% Pre-Sale via pretix.eu/safer-space-ev/equinox-2026/", fill="#C5BAF7", anchor="mm", font_size=16)
    draw.text((400, 1005), "Strict Affirmative Consent & Code of Conduct applies.", fill="#FFD700", anchor="mm", font_size=15)

    draw.text((400, 1120), "Hosted by Safer Space e.V. • Powered by Lika OS", fill="#8888AA", anchor="mm", font_size=16)

    poster_path = STAGING_DIR / "Lika_Equinox_Event_Poster.png"
    img_poster.save(poster_path)
    shutil.copy(poster_path, LIKA_BUDGET_DIR / "Lika_Equinox_Event_Poster.png")
    print("[IMG] Created Lika_Equinox_Event_Poster.png")

    # 2. Equinox Spatial Floor Plan
    img_floor = Image.new("RGB", (1000, 750), color="#1E1B38")
    draw_f = ImageDraw.Draw(img_floor)

    draw_f.text((500, 40), "EQUINOX HAMBURG — SPATIAL ZONING & PRODUCTION LAYOUT", fill="#FFFFFF", anchor="mm", font_size=26)
    draw_f.text((500, 75), "Capacity: 320 | Minimum Bar Turnover Zone: €7,500 | Sound: 12kW L-Acoustics", fill="#C5BAF7", anchor="mm", font_size=15)

    # Zones
    # Entrance / Pretix Box
    draw_f.rectangle([(60, 130), (280, 260)], fill="#2D2852", outline="#7B61FF", width=2)
    draw_f.text((170, 170), "ENTRANCE & DOOR", fill="#FFFFFF", anchor="mm", font_size=16)
    draw_f.text((170, 200), "Pretix Check-in & Scanner", fill="#7B61FF", anchor="mm", font_size=13)
    draw_f.text((170, 225), "Coat Check & Briefing", fill="#CCCCCC", anchor="mm", font_size=12)

    # Main Dance Floor
    draw_f.rectangle([(320, 130), (700, 480)], fill="#3B326B", outline="#9D88FF", width=3)
    draw_f.text((510, 230), "MAIN DANCE FLOOR", fill="#FFFFFF", anchor="mm", font_size=22)
    draw_f.text((510, 270), "12kW L-Acoustics System", fill="#FFD700", anchor="mm", font_size=15)
    draw_f.text((510, 305), "Max 99 dB(A) Leq limit", fill="#CCCCCC", anchor="mm", font_size=13)

    # Pole Stage
    draw_f.rectangle([(350, 360), (490, 450)], fill="#534594", outline="#FFD700", width=2)
    draw_f.text((420, 405), "ELEVATED POLE\nSTAGE", fill="#FFFFFF", anchor="mm", font_size=13)

    # Performance Cage
    draw_f.rectangle([(530, 360), (670, 450)], fill="#534594", outline="#FFD700", width=2)
    draw_f.text((600, 405), "PERFORMANCE\nCAGE", fill="#FFFFFF", anchor="mm", font_size=13)

    # Bar Area (€7,500 turnover zone)
    draw_f.rectangle([(740, 130), (940, 480)], fill="#2D2852", outline="#7B61FF", width=2)
    draw_f.text((840, 240), "EQUINOX BAR", fill="#FFFFFF", anchor="mm", font_size=20)
    draw_f.text((840, 280), "Turnover Guarantee", fill="#FFD700", anchor="mm", font_size=14)
    draw_f.text((840, 310), "Target: €7,500.00", fill="#FFFFFF", anchor="mm", font_size=15)
    draw_f.text((840, 350), "Equinox Bar Staff & POS", fill="#C5BAF7", anchor="mm", font_size=12)

    # Lower Lounge & Care Station
    draw_f.rectangle([(60, 520), (480, 690)], fill="#262244", outline="#50E3C2", width=2)
    draw_f.text((270, 560), "LIKA CARE STATION & LOWER LOUNGE", fill="#50E3C2", anchor="mm", font_size=17)
    draw_f.text((270, 600), "Active Care Angels • Electrolytes • Tea • First Aid", fill="#FFFFFF", anchor="mm", font_size=13)
    draw_f.text((270, 635), "De-escalation & Quiet Reflection Area", fill="#CCCCCC", anchor="mm", font_size=12)

    # Upper Play Area & Cuddle Puddle
    draw_f.rectangle([(520, 520), (940, 690)], fill="#352952", outline="#FF6584", width=2)
    draw_f.text((730, 560), "UPPER RETREAT & CUDDLE PUDDLE", fill="#FF6584", anchor="mm", font_size=17)
    draw_f.text((730, 600), "Sensual Expression & Soft Fabric Zone", fill="#FFFFFF", anchor="mm", font_size=13)
    draw_f.text((730, 635), "Monitored by Dedicated Consent Host (Lika OS)", fill="#FFD700", anchor="mm", font_size=12)

    floor_path = STAGING_DIR / "Equinox_Venue_Floorplan_Zones.png"
    img_floor.save(floor_path)
    shutil.copy(floor_path, LIKA_BUDGET_DIR / "Equinox_Venue_Floorplan_Zones.png")
    print("[IMG] Created Equinox_Venue_Floorplan_Zones.png")

    # 3. Lika OS Volunteer Shift Overview
    img_shifts = Image.new("RGB", (900, 600), color="#1C1833")
    draw_s = ImageDraw.Draw(img_shifts)

    draw_s.text((450, 35), "LIKA OS — VOLUNTEER SHIFT OPERATIONS MATRIX", fill="#FFFFFF", anchor="mm", font_size=24)
    draw_s.text((450, 70), "Fairness Governance v1.1 • Max 2 Shifts / Volunteer • Mandatory Rest Intervals", fill="#7B61FF", anchor="mm", font_size=14)

    teams = [
        ("Core Circle & Lead", "Production coordination, escalation bridge, Equinox liaison", "#7B61FF"),
        ("Logistics & Rigging", "12kW PA load-in, cage rigging, cable safety, tear-down", "#50E3C2"),
        ("Care & Consent Team", "Harm reduction, Cuddle Puddle host, emotional support", "#FF6584"),
        ("Door & Pretix Scanner", "Ticket QR validation, consent check, wristbands, coat check", "#FFD700"),
        ("Sound & Visual Tech", "DJ console support, sound levels Leq < 99dB, light control", "#9D88FF"),
    ]

    y = 120
    for team, desc, color in teams:
        draw_s.rectangle([(50, y), (850, y + 70)], fill="#2A2448", outline=color, width=2)
        draw_s.text((75, y + 25), team, fill=color, anchor="lm", font_size=18)
        draw_s.text((75, y + 50), desc, fill="#E5E0FA", anchor="lm", font_size=13)
        draw_s.rectangle([(720, y + 15), (830, y + 55)], fill=color)
        draw_s.text((775, y + 35), "CONFIRMED", fill="#1C1833", anchor="mm", font_size=13)
        y += 85

    draw_s.text((450, 560), "All shifts synchronized with OpenProject Work Packages & Lika Governance Sheet", fill="#8888AA", anchor="mm", font_size=13)

    shift_path = STAGING_DIR / "Lika_OS_Volunteer_Shift_Overview.png"
    img_shifts.save(shift_path)
    shutil.copy(shift_path, LIKA_BUDGET_DIR / "Lika_OS_Volunteer_Shift_Overview.png")
    print("[IMG] Created Lika_OS_Volunteer_Shift_Overview.png")


if __name__ == "__main__":
    create_venue_contract()
    create_awareness_guidelines()
    create_sound_invoice()
    create_dj_contracts()
    create_catering_receipt()
    create_sixt_invoice()
    generate_visual_assets()
    print("All fundraiser assets successfully generated and mirrored!")
