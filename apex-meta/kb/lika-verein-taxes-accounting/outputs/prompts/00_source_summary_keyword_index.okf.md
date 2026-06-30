---
okf_version: "0.1"
document_type: "source_summary_keyword_index"
project: "lika-verein-taxes-accounting"
created_for: "LIKA / Safer Space e.V. event ticketing, tax, accounting, PM process execution"
repo_root: "apexai-os-meta"
kb_root: "apex-meta/kb/lika-verein-taxes-accounting"
status: "operator_validated_input_index"
write_policy: "read-first; write only derived outputs after explicit operator instruction"
---

# LIKA Source Summary + Keyword Index

## 1. Purpose

This file is the short source-orientation layer for future executor chats.

It tells the executor where to look before creating the LIKA event operating model and before testing the `apex-plan`, `apex-sync`, and `apex-session` process chain.

The goal is not to summarize every source in full. The goal is to prevent drift, reduce token waste, and make source lookup deterministic.

---

## 2. Project Context

```yaml
organisation:
  name: "Safer Space e.V. / LIKA"
  legal_form: "eingetragener Verein"
  seat: "Hamburg"
  charitable_status: "nicht gemeinnützig"
  donation_receipts: false
  activity: "Kulturveranstaltungen, Workshops, künstlerische Begegnungsformate"
  accounting_method: "Einnahmenüberschussrechnung / EÜR"
  vat_status: "USt auf Rechnungen; Kleinunternehmerregelung nicht als Standardannahme verwenden"
  tax_method: "Istversteuerung laut Projektkontext / zu bestätigen"
```

Important implication:

```yaml
transfer_warning:
  - "Do not silently apply Gemeinnützigkeit, Zweckbetrieb, Spendenbescheinigung, Übungsleiterpauschale, or Ehrenamtspauschale assumptions."
  - "Provider documentation can define workflows, exports, and configuration, but cannot decide tax law."
  - "Venue settlement, 7% vs. 19% ticket VAT, foreign artists, KSK, and contractor status remain validation points."
```

---

## 3. Event Description Source

```yaml
event_description_source:
  title: "Location - Fundraiser Hamburg.xlsx"
  project_source_name: "Location - Fundraiser Hamburg .xlsx"
  role: "Primary concrete event-description file for the planned fundraiser / club-cultural event."
  expected_use:
    - "Extract venue/event assumptions."
    - "Extract capacity, location, revenue, ticketing, settlement, bar/minimum revenue, and operational constraints if present."
    - "Treat it as the concrete event case that the generic KB must be applied to."
  instruction_to_executor:
    - "Explicitly inspect this file before finalizing the event operating model."
    - "Do not replace it with generic event assumptions."
    - "If the file is unavailable in the execution environment, stop and request it as required input."
```

---

## 4. Canonical Repo Paths

```yaml
repo_paths:
  skill_packages:
    apex_plan: ".claude/skills/apex-plan"
    apex_sync: ".claude/skills/apex-sync"
    apex_session: ".claude/skills/apex-session"
  kb:
    root: "apex-meta/kb/lika-verein-taxes-accounting"
    readme: "apex-meta/kb/lika-verein-taxes-accounting/README.md"
    manifest: "apex-meta/kb/lika-verein-taxes-accounting/manifests/source-manifest.json"
    raw_refs: "apex-meta/kb/lika-verein-taxes-accounting/raw/refs"
    ingest_analysis: "apex-meta/kb/lika-verein-taxes-accounting/ingest-analysis"
    wiki: "apex-meta/kb/lika-verein-taxes-accounting/wiki"
    outputs: "apex-meta/kb/lika-verein-taxes-accounting/outputs"
```

---

## 5. Source Clusters and Lookup Hints

```yaml
source_clusters:
  invoicing_and_ticket_as_invoice:
    keywords:
      - "Rechnung"
      - "Pflichtangaben"
      - "Kleinbetragsrechnung"
      - "§33 UStDV"
      - "§14 UStG"
      - "Ticket als Rechnung"
    likely_files:
      - "raw/refs/IHK-Berlin_Pflichtangaben-Rechnungen.md"
      - "raw/refs/IHK-Niederbayern_Checkliste-Kleinbetragsrechnungen.pdf"
      - "raw/refs/_pdf_extracted_md/IHK-Niederbayern_Checkliste-Kleinbetragsrechnungen.md"
      - "raw/refs/BMJ_UStDV_33_Kleinbetragsrechnungen.md"
      - "raw/refs/BMJ_UStG_14_Rechnungen.md"
    use_for:
      - "Ticket receipt fields"
      - "Invoice checklist"
      - "B2B invoice requirements"
      - "Entry ticket as small invoice if price <= 250 EUR and fields are present"

  e_invoice:
    keywords:
      - "E-Rechnung"
      - "XRechnung"
      - "ZUGFeRD"
      - "B2B"
      - "PDF reicht nicht"
    likely_files:
      - "raw/refs/BMF_FAQ-E-Rechnung.md"
      - "raw/refs/IHK-Muenchen_E-Rechnung.md"
      - "raw/refs/IHK-Hannover_E-Rechnungspflicht-Vereine-2025.md"
    use_for:
      - "B2B supplier invoice process"
      - "Venue / contractor invoice intake"
      - "Accounting archive requirements"

  gobd_and_archive:
    keywords:
      - "GoBD"
      - "Verfahrensdokumentation"
      - "Belegablage"
      - "Unveränderbarkeit"
      - "Datenzugriff"
      - "ersetzendes Scannen"
    likely_files:
      - "raw/refs/BMF_GoBD-2024.md"
      - "raw/refs/BMF_GoBD-2024.pdf"
      - "raw/refs/DATEV_Verfahrensdokumentation-GoBD.md"
      - "raw/refs/AWV_GoBD-Praxisleitfaden.md"
      - "raw/refs/AWV_Muster-Verfahrensdokumentation-Belegablage.pdf"
      - "raw/refs/AWV_Muster-Verfahrensdokumentation-Belegablage.docx"
    use_for:
      - "Digital event archive"
      - "Ticketing export preservation"
      - "Audit trail"
      - "Closeout documentation"

  ticketing_provider_operations:
    keywords:
      - "pretix"
      - "Fiscal requirements Germany"
      - "Taxes"
      - "Order Lifecycle"
      - "Eventbrite"
      - "ticket.io"
      - "Payout"
      - "Refund"
      - "Storno"
      - "Export"
    likely_files:
      - "raw/refs/pretix_Fiscal-Requirements-Germany.md"
      - "raw/refs/pretix_Taxes-Guide.md"
      - "raw/refs/pretix_Order-Lifecycle.md"
      - "raw/refs/Eventbrite_Umsatzuebersicht-Export.md"
      - "raw/refs/Eventbrite_Event-Payout-Financial-Information.md"
      - "raw/refs/Eventbrite_Vertriebskanaele-Zahlungsarten.md"
      - "raw/refs/ticketio_Event-Controlling-Reporting.md"
      - "raw/refs/ticketio_FAQ-Veranstalter.md"
    use_for:
      - "Ticketing setup"
      - "Tax-rule configuration"
      - "Payout reconciliation"
      - "Refund/cancellation status mapping"
      - "Export field requirements"
    warning:
      - "Provider docs are operational, not legal authority."

  association_tax_and_accounting:
    keywords:
      - "Verein"
      - "wirtschaftlicher Geschäftsbetrieb"
      - "EÜR"
      - "SKR42"
      - "Körperschaftsteuer"
      - "Gewerbesteuer"
      - "Umsatzsteuer Verein"
    likely_files:
      - "raw/refs/FinanzamtNRW_Vereine-Umsatzsteuer.md"
      - "raw/refs/FinanzverwaltungNRW_Mein-ELSTER-fuer-Vereine.pdf"
      - "raw/refs/DATEV_SKR42-Kontenrahmen.md"
      - "raw/refs/DATEV_SKR42-Branchenpaket-Einrichten.md"
      - "raw/refs/DeutschesEhrenamt_Rechnungslegung-Verein.md"
      - "raw/refs/DeutschesEhrenamt_Wirtschaftlicher-Geschaeftsbetrieb.md"
      - "raw/refs/vereinsknowhow_*"
    use_for:
      - "Association accounting structure"
      - "EÜR model"
      - "Tax filing orientation"
      - "Sphärenlogik as reference only"
    warning:
      - "Many sources assume Gemeinnützigkeit; mark unsafe parts."

  vat_ticket_rate_and_culture:
    keywords:
      - "7%"
      - "19%"
      - "Kulturveranstaltung"
      - "Konzert"
      - "DJ"
      - "Club"
      - "Berghain"
      - "§12 Abs. 2 Nr. 7 UStG"
      - "UStAE 12.7"
      - "BFH"
    likely_files:
      - "raw/refs/IHK-MittlererNiederrhein_Kulturveranstaltungen-USt.md"
      - "raw/refs/BFH_V-R-16-09_Vorverkaufsgebuehr.md"
      - "raw/refs/BFH_XI-R-34-14_Berghain-Techno-Konzert.md"
      - "raw/refs/BMF_UStAE_12-7_Kultur-Konzerte.md"
    use_for:
      - "Ticket VAT risk model"
      - "7% vs. 19% validation path"
    warning:
      - "Do not finalize VAT rate without validation. Default safer assumption often remains 19% unless evidence supports 7%."

  ksk_and_artists:
    keywords:
      - "KSK"
      - "Künstlersozialabgabe"
      - "Veranstalter"
      - "DJ"
      - "Performer"
      - "Designer"
      - "Foto"
      - "Video"
      - "K5001"
    likely_files:
      - "raw/refs/KSK_Info04_Abgabepflicht-Veranstalter.pdf"
      - "raw/refs/DRV_K5001_Kuenstlersozialabgabe.pdf"
      - "raw/refs/_pdf_extracted_md/DRV_K5001_Kuenstlersozialabgabe.md"
      - "raw/refs/VUT_KSK-Abgabepflicht-Elektronische-Musik.md"
    use_for:
      - "Artist/vendor onboarding"
      - "KSK matrix"
      - "Annual reporting evidence"

  contractors_crew_and_expenses:
    keywords:
      - "kurzfristige Beschäftigung"
      - "Minijob"
      - "Scheinselbstständigkeit"
      - "Auslagen"
      - "Aufwandsentschädigung"
      - "Crew"
      - "Helfer"
    likely_files:
      - "raw/refs/DRV_Minijob-Kurzfristige-Beschaeftigung.md"
      - "raw/refs/DRV_Scheinselbststaendigkeit-Erkennen.md"
      - "raw/refs/Buergergesellschaft_Ehrenamt-Auslagen.md"
      - "raw/refs/Vereinswelt_Auslagenerstattung-Muster.md"
    use_for:
      - "Crew status matrix"
      - "Paid helper workflow"
      - "Expense reimbursement form"
    warning:
      - "Ehrenamt and Gemeinnützigkeit assumptions are risky for Safer Space."

  foreign_services_and_reverse_charge:
    keywords:
      - "§50a"
      - "Abzugsteuer"
      - "ausländische Künstler"
      - "Reverse Charge"
      - "§13b"
      - "ausländische Dienstleister"
    likely_files:
      - "raw/refs/BZSt_50a-Abzugsteuer.md"
      - "raw/refs/IHK-Koblenz_Reverse-Charge-Auslaendische-Dienstleister.md"
      - "raw/refs/Handelskammer-Hamburg_Reverse-Charge.md"
    use_for:
      - "Foreign artist checklist"
      - "Foreign supplier invoice intake"
      - "Reverse-charge validation"

  venue_and_settlement:
    keywords:
      - "Venue"
      - "Location"
      - "Mindestbarumsatz"
      - "Barumsatzgarantie"
      - "Settlement"
      - "Schadensersatz"
      - "Bereitstellungsentgelt"
      - "Z-Bon"
    likely_files:
      - "Location - Fundraiser Hamburg .xlsx"
      - "raw/refs/eventfaq_Club-Veranstaltungsvertrag-Mindestumsatz.md"
      - "raw/refs/StBK-Hamburg_Mindestumsatzgarantien-Gastronomie.md"
      - "raw/refs/EVENTFAQ_Mietvertrag-Location.md"
    use_for:
      - "Concrete venue contract and settlement assumptions"
      - "Open tax validation questions"
      - "Venue closeout document checklist"
    warning:
      - "This is one of the weakest evidence areas. Keep as validation point."
```

---

## 6. Existing Research / Analysis Source Files

```yaml
research_source_files:
  uploaded_project_sources:
    - file: "gemini-research_sources.yaml"
      role: "Early Gemini source corpus / candidate source list."
      use_for: "Trace original source claims, but do not trust scores blindly."
    - file: "gpt_research_sources.yaml"
      role: "GPT source corpus / candidate source list."
      use_for: "Trace original source claims and compare with Gemini list."
    - file: "Research2_gem.md"
      role: "Research pass on event tax/accounting sources."
      use_for: "Find earlier assumptions, gaps, candidate official guides."
    - file: "research2_gpt.yaml"
      role: "Structured GPT follow-up source research."
      use_for: "Find verified URLs, source statuses, and priority notes."
    - file: "Research3Tickets_gpt.md"
      role: "Ticketing-specific research."
      use_for: "Ticket-as-invoice, ticketing export, provider docs, refund/storno logic."
    - file: "research4_gem.yaml"
      role: "Gap closure and source critique."
      use_for: "Venue, ticket VAT, donation/support wording, risk flags."
    - file: "Research4_perpDR.md"
      role: "Perplexity-style deep research gap closure."
      use_for: "Reachability, source quality, guide vs. thin page, discard decisions."
    - file: "Quellenanalyse Safer Space.txt"
      role: "Latest consolidated source ranking and quality analysis."
      use_for: "Primary ranking reference for P0/P1/P2/P3/discard."
    - file: "Location - Fundraiser Hamburg .xlsx"
      role: "Concrete event description and venue/fundraiser assumptions."
      use_for: "Apply generic KB to actual event case. Must be inspected."
```

---

## 7. Recommended Read Order for Executor

```yaml
read_order:
  phase_0_orientation:
    - "This file: outputs/prompts/00_source_summary_keyword_index.okf.md"
    - "apex-meta/kb/lika-verein-taxes-accounting/README.md"
    - "apex-meta/kb/lika-verein-taxes-accounting/manifests/source-manifest.json"
  phase_1_event_case:
    - "Location - Fundraiser Hamburg .xlsx"
  phase_2_skill_contracts:
    - ".claude/skills/apex-plan/SKILL.md"
    - ".claude/skills/apex-sync/SKILL.md"
    - ".claude/skills/apex-session/SKILL.md"
  phase_3_source_evidence:
    - "Quellenanalyse Safer Space.txt"
    - "raw/refs/IHK-Berlin_Pflichtangaben-Rechnungen.md"
    - "raw/refs/IHK-Niederbayern_Checkliste-Kleinbetragsrechnungen.pdf or extracted MD"
    - "raw/refs/BMF_GoBD-2024.md"
    - "raw/refs/DATEV_Verfahrensdokumentation-GoBD.md"
    - "raw/refs/AWV_GoBD-Praxisleitfaden.md"
    - "raw/refs/pretix_Fiscal-Requirements-Germany.md"
    - "raw/refs/pretix_Taxes-Guide.md"
    - "raw/refs/pretix_Order-Lifecycle.md if present"
    - "raw/refs/KSK_Info04_Abgabepflicht-Veranstalter.pdf if present"
    - "raw/refs/DRV_K5001_Kuenstlersozialabgabe.pdf or extracted MD"
```

---

## 8. Output Standard for New Text

Use this Open Knowledge Format profile for written outputs:

```yaml
okf_text_profile:
  section_header: "clear numbered section"
  claim_style: "separate facts, interpretations, decisions, risks"
  source_style: "cite path or file name for every important source-derived claim"
  uncertainty_style: "mark unknown, assumption, validation_required"
  artifact_style: "copy-ready Markdown/YAML, not prose-only"
  decision_style:
    fields:
      - decision
      - recommended_answer
      - options
      - consequence
      - evidence
      - risk
  workflow_style:
    fields:
      - objective
      - trigger
      - inputs
      - steps
      - outputs
      - owner
      - handoff
      - done_when
      - risks
      - source_basis
```

---

## 9. Anti-Drift Rules

```yaml
anti_drift_rules:
  - "Do not treat Safer Space as gemeinnützig unless the operator provides updated recognition evidence."
  - "Do not treat support/donation ticket wording as safe without separate payment/no-counterperformance design."
  - "Do not decide 7% VAT from provider configuration docs."
  - "Do not treat venue minimum revenue settlement as solved by event-law blog posts."
  - "Do not generate micro-SOPs without linking each SOP to a source cluster and validation risk."
  - "Do not run broad web research unless explicitly asked."
  - "Prefer one source-index read and local grep/search over dozens of repeated repo fetches."
```
