# 1. Executive Summary

Die Quellenbasis ist **brauchbar, aber noch nicht playbook-reif**. Für eine Safer-Space-KB sind die stärksten Quellen klar: **IHK/BMF/BMJ/BZSt/KSK/DRV/Minijob-Zentrale/DATEV/AWV/pretix**. Die größte Schwäche bleibt: **Venue-Settlement / Mindestbarumsatz / Barumsatzgarantie** und die **konkrete 7%-vs.-19%-Eintritts-USt für Club-/DJ-/Kultur-Mischformate**. Diese Themen bleiben trotz Recherche **steuerberaterpflichtige Prüffelder**.

Safer Space ist laut Projektkontext als **nicht gemeinnütziger e.V.**, mit **wirtschaftlichem Geschäftsbetrieb**, **EÜR**, **USt auf Rechnungen** und **Istversteuerung** angelegt; genau deshalb sind Quellen mit Gemeinnützigkeits-, Zweckbetriebs- oder Spendenlogik gefährlich und dürfen nur markiert/selektiv genutzt werden. Die recherchierten Dateien benennen selbst als offene Kernlücken: Ticket als Rechnung nur indirekt belastbar, Venue-Settlement kaum offiziell belegt, und Quellen zu nicht gemeinnützigen e.V. mit Club-Event bleiben dünn.

**Gesamtbewertung Quellenbasis:** `72 / 100`

|Entscheidung|Ergebnis|
|---|--:|
|**P0 sofort archivieren**|16 Quellen|
|**P1 stark archivieren**|10 Quellen|
|**P2 selektiv archivieren**|12 Quellen|
|**P3 nur Referenz/Layout**|5 Quellen|
|**Discard aus Core-KB**|7 Quellen|
|**größte Lücke**|Venue-Settlement + Mindestbarumsatz-USt|
|**zweite Lücke**|7% vs. 19% für Club-/DJ-/Kultur-Mischveranstaltung|
|**dritte Lücke**|Ticket als Rechnung ausdrücklich für Eventtickets|

---

# 2. Methodik des 1–100 Scorings

```yaml
scoring_method:
  authority_score_20:
    weighting: 20
    interpretation: "Rechts-/Behörden-/Institutionenautorität"
  specificity_score_15:
    weighting: 15
    interpretation: "Passung zu nicht gemeinnützigem e.V. + Kultur/Event + USt + EÜR"
  practical_depth_score_15:
    weighting: 15
    interpretation: "Checklisten, Beispiele, Workflows, Muster"
  implementation_value_score_15:
    weighting: 15
    interpretation: "Direkt in KB-Regel, Template oder Prozess übertragbar"
  extractability_score_10:
    weighting: 10
    interpretation: "PDF/HTML sauber archivierbar"
  freshness_score_10:
    weighting: 10
    interpretation: "2024–2026 oder laufende Fassung"
  transfer_safety_score_10:
    weighting: 10
    interpretation: "Risiko falscher Übertragung auf Safer Space"
  redundancy_score_5:
    weighting: 5
    interpretation: "Unique Gap-Closer vs. Dublette"
  penalties:
    seo_article: -10
    marketing: -15
    gemeinnuetzigkeit_confusion_high: -10
    no_clear_publisher: -15
    outdated_thresholds: -20
    duplicate_replaced: -30
```

---

# 3. Deduplizierte Quellenliste

## 3.1 Canonical Sources

|ID|Canonical Source|Publisher|Primärgruppe|Score|Prio|Entscheidung|
|--:|---|---|---|--:|---|---|
|S001|§33 UStDV — Rechnungen über Kleinbeträge|BMJ / Gesetze im Internet|invoicing_and_e_invoice|**92**|P0|archive_full|
|S002|IHK Pflichtangaben in Rechnungen|IHK Berlin / IHK|invoicing_and_e_invoice|**90**|P0|archive_full|
|S003|IHK Checkliste Kleinbetragsrechnung bis 250 €|IHK Niederbayern|invoicing_and_e_invoice|**89**|P0|archive_full|
|S004|KSK Informationsschrift Nr. 4 — Abgabepflicht Veranstalter|Künstlersozialkasse|ksk_and_artists|**93**|P0|archive_full|
|S005|DRV K5001 — Information zur Künstlersozialabgabe|Deutsche Rentenversicherung|ksk_and_artists|**88**|P0|archive_full|
|S006|BMF GoBD / Änderung 2024|BMF|gobd_and_document_archive|**91**|P0|archive_full|
|S007|DATEV Verfahrensdokumentation gemäß GoBD|DATEV|gobd_and_document_archive|**86**|P0|archive_full|
|S008|AWV Muster-Verfahrensdokumentation Belegablage|AWV|templates_and_checklists|**88**|P0|archive_full|
|S009|BMF FAQ E-Rechnung ab 2025|BMF|invoicing_and_e_invoice|**86**|P0|archive_full|
|S010|IHK München Elektronische Rechnungen|IHK München|invoicing_and_e_invoice|**84**|P1|archive_full|
|S011|Finanzverwaltung NRW — Vereine und Umsatzsteuer / Mein ELSTER für Vereine|Finanzverwaltung NRW|association_tax_and_accounting|**84**|P1|archive_full_marked|
|S012|pretix Fiscal Requirements Germany|pretix|ticketing_provider_operations|**82**|P1|archive_full|
|S013|pretix Taxes|pretix|ticketing_provider_operations|**76**|P1|archive_full|
|S014|pretix Order Lifecycle|pretix|reconciliation_and_event_accounting|**80**|P1|archive_full|
|S015|Minijob-Zentrale — Kurzfristige Beschäftigung|Minijob-Zentrale|contractors_crew_and_expenses|**86**|P0|archive_full|
|S016|DRV Scheinselbstständigkeit erkennen|Deutsche Rentenversicherung|contractors_crew_and_expenses|**86**|P0|archive_full|
|S017|BZSt Abzugsteuer §50a EStG|BZSt|foreign_services_and_reverse_charge|**87**|P0|archive_full|
|S018|Handelskammer Hamburg Reverse Charge|Handelskammer Hamburg|foreign_services_and_reverse_charge|**76**|P1|archive_selectively|
|S019|DATEV §13b UStG Tatbestände|DATEV Hilfe-Center|foreign_services_and_reverse_charge|**74**|P2|archive_selectively|
|S020|DATEV SKR42 Kontenrahmen|DATEV|association_tax_and_accounting|**73**|P2|archive_selectively|
|S021|DATEV SKR42 Branchenpaket einrichten|DATEV Hilfe-Center|association_tax_and_accounting|**67**|P2|reference_selective|
|S022|LfSt Bayern Merkblatt Festveranstaltungen 2025|LfSt Bayern|vat_and_ticket_tax|**72**|P2|archive_marked|
|S023|BFH V R 16/09 — Vorverkaufsgebühr|Bundesfinanzhof|vat_and_ticket_tax|**84**|P1|archive_full|
|S024|UStH/BMF echter vs. unechter Schadensersatz|BMF / UStH|venue_and_settlement|**82**|P1|archive_full|
|S025|Eventbrite Umsatzübersicht / Payout Reports|Eventbrite|reconciliation_and_event_accounting|**64**|P2|archive_selectively|
|S026|Eventbrite Event/Payout Details Invoice|Eventbrite|reconciliation_and_event_accounting|**63**|P2|archive_selectively|
|S027|ticket.io Event Controlling & Reporting|ticket.io|ticketing_provider_operations|**61**|P2|archive_selectively|
|S028|EVENTFAQ Mietvertrag Location|EVENTFAQ|venue_and_settlement|**58**|P3|reference_only|
|S029|Beck Law Locationvertrag|Beck Law|venue_and_settlement|**45**|P3|reference_only_or_discard|
|S030|Michow & Ulbricht Musterverträge Live Entertainment|Kanzlei|venue_and_settlement|**60**|P2|template_selective|
|S031|Deutsches Ehrenamt Rechnungslegung/Buchführung Verein|Deutsches Ehrenamt|association_tax_and_accounting|**59**|P3|reference_only|
|S032|Deutsches Ehrenamt Auslagenersatz|Deutsches Ehrenamt|contractors_crew_and_expenses|**54**|P3|inspiration_only|
|S033|Wegweiser Bürgergesellschaft Auslagen/Aufwand|Wegweiser Bürgergesellschaft|contractors_crew_and_expenses|**43**|P3|reference_only|
|S034|TSV Gersthofen Auslagenformular|TSV Gersthofen|templates_and_checklists|**35**|D|discard_core|
|S035|Lexware Stornorechnung|Lexware|reconciliation_and_event_accounting|**55**|P3|reference_only|
|S036|VUT Club/DJ/KSK-Kontext|VUT|ksk_and_artists|**62**|P2|archive_selectively|
|S037|Haufe Ticket-Eigenhändler / ermäßigter Steuersatz|Haufe|vat_and_ticket_tax|**65**|P2|archive_selectively|
|S038|generische Vereinssteuer-/SEO-Blogs|diverse|secondary_context|**20–35**|D|discard|

---

## 3.2 Duplicate Resolution

```yaml
duplicate_resolution:
  - duplicate_group_id: D01_invoice_required_fields
    canonical_source: S002
    duplicate_variants:
      - "IHK Pflichtangaben in Rechnungen"
      - "IHK Berlin Pflichtangaben"
      - "Pflichtangaben auf Rechnungen"
    keep: "IHK Berlin / konkrete IHK-Pflichtangabenquelle"
    discard_or_merge: "unspezifische IHK-Hamburg-Startseiten ohne direkten Deep-Link"
    reason: "konkreter, extrahierbarer und direkt zitierbarer"

  - duplicate_group_id: D02_small_invoice
    canonical_source: S001
    complement_source: S003
    duplicate_variants:
      - "§33 UStDV"
      - "Rechnungen über Kleinbeträge"
      - "Kleinbetragsrechnung bis 250 Euro"
    keep: "§33 UStDV als Normanker + IHK Checkliste als Umsetzung"
    reason: "Norm + Checkliste sind komplementär, nicht redundant"

  - duplicate_group_id: D03_ksk
    canonical_source: S004
    complement_source: S005
    duplicate_variants:
      - "KSK Informationsschrift Nr. 4"
      - "DRV K5001"
      - "Künstlersozialabgabe Veranstalter"
    keep: "beide"
    reason: "KSK = fachlicher Veranstalterleitfaden; DRV = prüfungsnahe Dokumentationslogik"

  - duplicate_group_id: D04_gobd
    canonical_source: S006
    complement_sources:
      - S007
      - S008
    duplicate_variants:
      - "BMF GoBD"
      - "DATEV Verfahrensdokumentation"
      - "AWV Muster-Verfahrensdokumentation"
    keep: "alle drei"
    reason: "BMF Normanker, DATEV Umsetzung, AWV Template"

  - duplicate_group_id: D05_pretix
    canonical_source: S012
    complement_sources:
      - S013
      - S014
    duplicate_variants:
      - "pretix Fiscal Germany"
      - "pretix Taxes"
      - "pretix Order Lifecycle"
    keep: "alle drei"
    reason: "Fiscal = Deutschland/GoBD, Taxes = Setup, Order Lifecycle = Storno/Refund"

  - duplicate_group_id: D06_eventbrite_reports
    canonical_source: S025
    complement_source: S026
    duplicate_variants:
      - "Eventbrite Umsatzübersicht"
      - "Export payout reports"
      - "Event/Payout Details Invoice"
    keep: "S025 + S026 selektiv"
    reason: "Reporting-Felder nutzbar; provider-spezifisch"

  - duplicate_group_id: D07_venue_contract
    canonical_source: S028
    duplicate_variants:
      - "EVENTFAQ Mietvertrag Location"
      - "Beck Law Locationvertrag"
      - "Michow & Ulbricht Musterverträge"
    keep: "S028/S030 selektiv"
    discard_or_merge: "S029 nur Referenz/Discard"
    reason: "Venue-Steuerfrage bleibt nicht belastbar; nur Vertragsstruktur"
```

---

# 4. Ranking nach Gruppen

## 4.1 Core Tax Law

|Rank|Quelle|Score|Prio|Best for|Limitierung|
|--:|---|--:|---|---|---|
|1|S001 §33 UStDV|92|P0|Kleinbetragsrechnung/Ticketbeleg|keine explizite Eventticket-Aussage|
|2|S006 BMF GoBD|91|P0|Archiv-/Datenzugriff-Normanker|nicht operativ genug|
|3|S009 BMF E-Rechnung FAQ|86|P0|B2B-E-Rechnung|Tickets B2C nicht Kern|
|4|S017 BZSt §50a|87|P0|ausländische Künstler:innen|nur Ausland|
|5|S024 UStH/BMF Schadensersatz|82|P1|Mindestumsatz-Prüflogik|keine Club-Beispiele|

**Group Readiness:** `78 / 100`

---

## 4.2 Invoicing and E-Invoice

|Rank|Quelle|Score|Prio|Best for|
|--:|---|--:|---|---|
|1|S001 §33 UStDV|92|P0|Ticket unter 250 € als Kleinbetragsrechnung|
|2|S002 IHK Pflichtangaben|90|P0|Rechnung >250 €, B2B, Vorsteuercheck|
|3|S003 IHK Kleinbetragsrechnung PDF|89|P0|konkrete Ticket-/Belegcheckliste|
|4|S009 BMF E-Rechnung|86|P0|offizieller E-Rechnungsanker|
|5|S010 IHK München E-Rechnung|84|P1|operative E-Rechnungsumsetzung|

**Group Readiness:** `86 / 100`

---

## 4.3 VAT and Ticket Tax

|Rank|Quelle|Score|Prio|Best for|Limitierung|
|--:|---|--:|---|---|---|
|1|S023 BFH Vorverkaufsgebühr|84|P1|Ticketgebühren als Teil Entgelt|enges Urteil, kein Playbook|
|2|S011 Finanzverwaltung NRW USt Vereine|84|P1|Verein als Unternehmer/Vorsteuer|Gemeinnützigkeitskontext markieren|
|3|S022 LfSt Bayern Festveranstaltungen|72|P2|Event-Einnahmen/Ausgabenlogik|hohes Zweckbetrieb-/Gemeinnützigkeitsrisiko|
|4|S037 Haufe Ticket-Eigenhändler|65|P2|Ergänzung Ticket-USt-Satz|Sekundärquelle|
|5|S013 pretix Taxes|76|P1|technische Steuersatzkonfiguration|keine Rechtsentscheidung|

**Group Readiness:** `61 / 100`

**Hauptgap:** 7% vs. 19% für Club-/DJ-/Kultur-Mischformat bleibt nicht final geschlossen.

---

## 4.4 Association Tax and Accounting

|Rank|Quelle|Score|Prio|Best for|
|--:|---|--:|---|---|
|1|S011 Finanzverwaltung NRW / Mein ELSTER Vereine|84|P1|Vereins-Steuererklärung/ELSTER/USt|
|2|S020 DATEV SKR42|73|P2|Konten-/Sphärenlogik|
|3|S021 DATEV Branchenpaket|67|P2|DATEV-Setup|
|4|S031 Deutsches Ehrenamt Buchführung Verein|59|P3|niedrigschwellige Prozesslogik|

**Group Readiness:** `63 / 100`

---

## 4.5 GoBD and Document Archive

|Rank|Quelle|Score|Prio|Best for|
|--:|---|--:|---|---|
|1|S006 BMF GoBD|91|P0|Normanker|
|2|S008 AWV Muster-Verfahrensdoku|88|P0|Vorlage|
|3|S007 DATEV Verfahrensdokumentation|86|P0|operative Umsetzung|
|4|S012 pretix Fiscal Germany|82|P1|Ticketshop in Verfahrensdoku|

**Group Readiness:** `90 / 100`

---

## 4.6 Ticketing Provider Operations

|Rank|Quelle|Score|Prio|Best for|
|--:|---|--:|---|---|
|1|S012 pretix Fiscal Requirements Germany|82|P1|deutsches Ticketing-/GoBD-Setup|
|2|S013 pretix Taxes|76|P1|Steuersatz-Setup|
|3|S014 pretix Order Lifecycle|80|P1|Storno/Refund/Order Status|
|4|S027 ticket.io Event Controlling|61|P2|Anbieterfragen / Reportinglogik|
|5|S025 Eventbrite Umsatzübersicht|64|P2|Exportfelder als Vergleich|

**Group Readiness:** `75 / 100`

---

## 4.7 Reconciliation and Event Accounting

|Rank|Quelle|Score|Prio|Best for|
|--:|---|--:|---|---|
|1|S014 pretix Order Lifecycle|80|P1|Refunds/Storno/Korrekturbelege|
|2|S025 Eventbrite Payout Reports|64|P2|Brutto/Netto/Gebühren/Refunds|
|3|S026 Eventbrite Event/Payout Details|63|P2|Reporting-Minimum|
|4|S035 Lexware Stornorechnung|55|P3|Begriffsklärung|
|5|S023 BFH Vorverkaufsgebühr|84|P1|Ticketgebühren als Entgeltbestandteil|

**Group Readiness:** `70 / 100`

---

## 4.8 KSK and Artists

|Rank|Quelle|Score|Prio|Best for|
|--:|---|--:|---|---|
|1|S004 KSK Informationsschrift Nr. 4|93|P0|Veranstalterpflicht|
|2|S005 DRV K5001|88|P0|Prüf-/Aufzeichnungspflicht|
|3|S017 BZSt §50a|87|P0|ausländische Künstler:innen|
|4|S036 VUT Club/DJ/KSK|62|P2|DJ-/Club-Kontext, nur Ergänzung|

**Group Readiness:** `86 / 100`

---

## 4.9 Contractors, Crew and Expenses

|Rank|Quelle|Score|Prio|Best for|
|--:|---|--:|---|---|
|1|S015 Minijob-Zentrale kurzfristige Beschäftigung|86|P0|bezahlte Eventhelfer:innen|
|2|S016 DRV Scheinselbstständigkeit|86|P0|Honorar-/Contractor-Abgrenzung|
|3|S032 Deutsches Ehrenamt Auslagenersatz|54|P3|Layout/Prozessidee|
|4|S033 Wegweiser Bürgergesellschaft|43|P3|Hintergrund|
|5|S034 TSV Auslagenformular|35|D|nicht Core-KB|

**Group Readiness:** `67 / 100`

---

## 4.10 Foreign Services and Reverse Charge

|Rank|Quelle|Score|Prio|Best for|
|--:|---|--:|---|---|
|1|S017 BZSt §50a|87|P0|Quellensteuer Auslandskünstler:innen|
|2|S018 Handelskammer Hamburg Reverse Charge|76|P1|Prüffeld §13b / Ausland B2B|
|3|S019 DATEV §13b|74|P2|Buchungs-/Steuerbüroübergabe|
|4|S012 pretix Fiscal Germany|82|P1|provider-seitige Reverse-Charge-Funktion|

**Group Readiness:** `74 / 100`

---

## 4.11 Venue and Settlement

|Rank|Quelle|Score|Prio|Best for|Entscheidung|
|--:|---|--:|---|---|---|
|1|S024 UStH/BMF Schadensersatz|82|P1|echte/unechte Schadensersatzlogik|archive_full|
|2|S028 EVENTFAQ Mietvertrag Location|58|P3|Vertragscheck|reference_only|
|3|S030 Michow & Ulbricht Musterverträge|60|P2|Vertragsstruktur|template_selective|
|4|S029 Beck Law Locationvertrag|45|P3|Rollenverständnis|reference/discard|

**Group Readiness:** `45 / 100`

**Kritisch:** Die Research4-Dateien sagen selbst, dass konkrete Beispiele zur Club-/Eventpraxis für Mindestbarumsätze fehlen und Venue-Fragen offen bleiben.

---

# 5. Globales Quellenranking

|Rank|ID|Quelle|Publisher|Score|Prio|KB-Entscheidung|
|--:|---|---|---|--:|---|---|
|1|S004|KSK Informationsschrift Nr. 4|KSK|93|P0|archive_full|
|2|S001|§33 UStDV Kleinbetragsrechnung|BMJ|92|P0|archive_full|
|3|S006|BMF GoBD 2024|BMF|91|P0|archive_full|
|4|S002|IHK Pflichtangaben Rechnungen|IHK Berlin|90|P0|archive_full|
|5|S003|IHK Kleinbetragsrechnung Checkliste|IHK Niederbayern|89|P0|archive_full|
|6|S005|DRV K5001 Künstlersozialabgabe|DRV|88|P0|archive_full|
|7|S008|AWV Muster-Verfahrensdokumentation|AWV|88|P0|archive_full|
|8|S017|BZSt §50a|BZSt|87|P0|archive_full|
|9|S007|DATEV Verfahrensdokumentation GoBD|DATEV|86|P0|archive_full|
|10|S009|BMF E-Rechnung FAQ|BMF|86|P0|archive_full|
|11|S015|Kurzfristige Beschäftigung|Minijob-Zentrale|86|P0|archive_full|
|12|S016|Scheinselbstständigkeit erkennen|DRV|86|P0|archive_full|
|13|S010|IHK München E-Rechnung|IHK München|84|P1|archive_full|
|14|S011|Finanzverwaltung NRW Vereine/USt|Finanzverwaltung NRW|84|P1|archive_marked|
|15|S023|BFH Vorverkaufsgebühr|BFH|84|P1|archive_full|
|16|S012|pretix Fiscal Germany|pretix|82|P1|archive_full|
|17|S024|UStH/BMF Schadensersatz|BMF/UStH|82|P1|archive_full|
|18|S014|pretix Order Lifecycle|pretix|80|P1|archive_full|
|19|S013|pretix Taxes|pretix|76|P1|archive_full|
|20|S018|Handelskammer Hamburg Reverse Charge|HK Hamburg|76|P1|archive_selectively|
|21|S019|DATEV §13b|DATEV|74|P2|archive_selectively|
|22|S020|DATEV SKR42|DATEV|73|P2|archive_selectively|
|23|S022|LfSt Bayern Festveranstaltungen|LfSt Bayern|72|P2|archive_marked|
|24|S021|DATEV Branchenpaket|DATEV|67|P2|reference_selective|
|25|S037|Haufe Ticket-Eigenhändler|Haufe|65|P2|archive_selective|
|26|S025|Eventbrite Umsatzübersicht|Eventbrite|64|P2|archive_selective|
|27|S026|Eventbrite Payout Details|Eventbrite|63|P2|archive_selective|
|28|S036|VUT Club/DJ/KSK|VUT|62|P2|archive_selective|
|29|S027|ticket.io Reporting|ticket.io|61|P2|archive_selective|
|30|S030|Michow & Ulbricht Musterverträge|Kanzlei|60|P2|template_selective|
|31|S031|Deutsches Ehrenamt Buchführung|Deutsches Ehrenamt|59|P3|reference_only|
|32|S028|EVENTFAQ Mietvertrag Location|EVENTFAQ|58|P3|reference_only|
|33|S035|Lexware Stornorechnung|Lexware|55|P3|reference_only|
|34|S032|Deutsches Ehrenamt Auslagenersatz|Deutsches Ehrenamt|54|P3|inspiration_only|
|35|S029|Beck Law Locationvertrag|Beck Law|45|P3|reference_or_discard|
|36|S033|Wegweiser Bürgergesellschaft|Wegweiser|43|P3|reference_only|
|37|S034|TSV Auslagenformular|TSV|35|D|discard_core|
|38|S038|generische SEO-/Vereinssteuerblogs|diverse|20–35|D|discard|

---

# 6. P0/P1/P2/P3/Discard Download-Manifest

```yaml
download_manifest:
  P0_core_archive:
    - source_id: S004
      title: "KSK Informationsschrift Nr. 4 — Abgabepflicht von Veranstaltern"
      publisher: "Künstlersozialkasse"
      url: "https://www.kuenstlersozialkasse.de/fileadmin/Dokumente/Mediencenter_Unternehmer_Verwerter/Informationsschriften/Info_04_Abgabepflicht_von_Veranstaltern.pdf"
      preferred_format: [pdf]
      archive_method: "download_pdf"
      reason: "zentrale Pflichtquelle für Veranstalter, DJs, Performer:innen"
      expected_extraction_value: "very_high"
      topic_tags: [ksk, artists, contractors, event]

    - source_id: S001
      title: "§33 UStDV — Rechnungen über Kleinbeträge"
      publisher: "Gesetze im Internet / BMJ"
      url: "https://www.gesetze-im-internet.de/ustdv_1980/__33.html"
      preferred_format: [html_snapshot, print_to_pdf]
      archive_method: "html_snapshot"
      reason: "Normanker für Ticket bis 250 Euro als Kleinbetragsrechnung"
      expected_extraction_value: "very_high"
      topic_tags: [invoice, small_invoice, ticket]

    - source_id: S006
      title: "GoBD — BMF-Schreiben Änderung 2024"
      publisher: "BMF"
      url: "https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Weitere_Steuerthemen/Abgabenordnung/AO-Anwendungserlass/2024-03-11-aenderung-gobd.html"
      preferred_format: [pdf]
      archive_method: "download_pdf"
      reason: "Primärquelle für digitales Belegarchiv"
      expected_extraction_value: "high"
      topic_tags: [gobd, archive, document_retention]

    - source_id: S002
      title: "Pflichtangaben in Rechnungen"
      publisher: "IHK Berlin"
      url: "https://www.ihk.de/berlin/service-und-beratung/recht-und-steuern/steuern-und-finanzen/pflichtangaben-in-rechnungen-4400732"
      preferred_format: [html_snapshot, print_to_pdf]
      archive_method: "html_snapshot"
      reason: "praktische Rechnungspflichtangaben"
      expected_extraction_value: "very_high"
      topic_tags: [invoice, vat, b2b]

    - source_id: S003
      title: "Checkliste Kleinbetragsrechnung bis 250 Euro"
      publisher: "IHK Niederbayern"
      url: "https://www.ihk-niederbayern.de/pdfs/checkliste-kleinbetragsrechnungen-data.pdf"
      preferred_format: [pdf]
      archive_method: "download_pdf"
      reason: "direkte Checkliste für Ticketbelege"
      expected_extraction_value: "very_high"
      topic_tags: [ticket, small_invoice, checklist]

    - source_id: S005
      title: "K5001 Information zur Künstlersozialabgabe"
      publisher: "Deutsche Rentenversicherung"
      url: "https://www.deutsche-rentenversicherung.de/SharedDocs/Formulare/DE/_pdf/K5001.pdf"
      preferred_format: [pdf]
      archive_method: "download_pdf"
      reason: "prüfungsnahe KSK-Dokumentationsquelle"
      expected_extraction_value: "high"
      topic_tags: [ksk, drv, records]

    - source_id: S008
      title: "AWV Muster-Verfahrensdokumentation zur Belegablage"
      publisher: "AWV"
      url: "https://www.awv-net.de/publikationen-produkte/publikationen/detailseite/musterverfahrensdokumentation-zur-belegablage"
      preferred_format: [pdf, docx]
      archive_method: "download_template"
      reason: "beste Template-Quelle für Verfahrensdokumentation"
      expected_extraction_value: "very_high"
      topic_tags: [gobd, template, document_archive]

    - source_id: S009
      title: "FAQ zur verpflichtenden E-Rechnung"
      publisher: "BMF"
      url: "https://www.bundesfinanzministerium.de/Content/DE/FAQ/e-rechnung.html"
      preferred_format: [html_snapshot]
      archive_method: "html_snapshot"
      reason: "offizielle E-Rechnungspflicht"
      expected_extraction_value: "high"
      topic_tags: [e_invoice, b2b]

    - source_id: S015
      title: "Kurzfristige Beschäftigung"
      publisher: "Minijob-Zentrale"
      url: "https://www.minijob-zentrale.de/DE/die-minijobs/kurzfristige-beschaeftigung"
      preferred_format: [html_snapshot]
      archive_method: "html_snapshot"
      reason: "Crew-/Helfer:innen-Statusprüfung"
      expected_extraction_value: "high"
      topic_tags: [crew, employment, minijob]

    - source_id: S016
      title: "Scheinselbstständigkeit erkennen"
      publisher: "Deutsche Rentenversicherung"
      url: "https://www.deutsche-rentenversicherung.de/DRV/DE/Rente/Arbeitnehmer-und-Selbststaendige/03_Selbststaendige/scheinselbststaendigkeit"
      preferred_format: [html_snapshot]
      archive_method: "html_snapshot"
      reason: "Contractor-/Honorarabgrenzung"
      expected_extraction_value: "high"
      topic_tags: [contractors, employment_status]

    - source_id: S017
      title: "Abzugsteuern nach §50a EStG"
      publisher: "BZSt"
      url: "https://www.bzst.de/DE/Privatpersonen/Abzugsteuern_50a/abzugsteuern_node.html"
      preferred_format: [html_snapshot]
      archive_method: "html_snapshot"
      reason: "ausländische Künstler:innen"
      expected_extraction_value: "high"
      topic_tags: [foreign_artists, withholding_tax]

  P1_strong_archive:
    - source_id: S007
      title: "DATEV Verfahrensdokumentation gemäß GoBD erstellen"
      url: "https://www.datev.de/web/de/berufsgruppenuebergreifend/ratgeber/rechnungswesen/verfahrensdokumentation-gemaess-gobd-erstellen"
      preferred_format: [html_snapshot]
      reason: "GoBD-Umsetzung"
      topic_tags: [gobd, process]

    - source_id: S010
      title: "IHK München Elektronische Rechnungen"
      url: "https://www.ihk-muenchen.de/ratgeber/steuern/elektronische-rechnungen/"
      preferred_format: [html_snapshot, pdf]
      reason: "E-Rechnung operativ"
      topic_tags: [e_invoice]

    - source_id: S011
      title: "Finanzverwaltung NRW — Vereine und Umsatzsteuer / Mein ELSTER für Vereine"
      url: "https://www.finanzamt.nrw.de/steuerinfos/weitere-themen/vereine-und-stiftungen/vereine-und-die-umsatzsteuer"
      preferred_format: [html_snapshot, pdf]
      reason: "Vereins-USt und ELSTER; Gemeinnützigkeitsabschnitte markieren"
      topic_tags: [association_tax, vat]

    - source_id: S012
      title: "pretix Fiscal Requirements Germany"
      url: "https://docs.pretix.eu/de/trust/fiscal/germany/"
      preferred_format: [html_snapshot]
      reason: "Ticketing-GoBD, Belege, Export"
      topic_tags: [ticketing, pretix, gobd]

    - source_id: S013
      title: "pretix Taxes"
      url: "https://docs.pretix.eu/de/guides/taxes/"
      preferred_format: [html_snapshot]
      reason: "Steuerregel-Konfiguration"
      topic_tags: [ticketing, vat_config]

    - source_id: S014
      title: "pretix Order Lifecycle"
      url: "https://docs.pretix.eu/dev/api/guides/order_lifecycle.html"
      preferred_format: [html_snapshot]
      reason: "Storno/Refund/Order-Workflow"
      topic_tags: [refunds, reconciliation]

    - source_id: S023
      title: "BFH V R 16/09 — Vorverkaufsgebühr"
      url: "https://www.bundesfinanzhof.de/de/entscheidung/entscheidungen-online/detail/STRE201210056/"
      preferred_format: [html_snapshot, print_to_pdf]
      reason: "Ticketgebühren als Entgeltbestandteil"
      topic_tags: [ticket_fees, vat]

    - source_id: S024
      title: "UStH/BMF echter vs. unechter Schadensersatz"
      preferred_format: [html_snapshot, print_to_pdf]
      reason: "Mindestbarumsatz / Ausgleichszahlung prüfen"
      topic_tags: [venue, damages, vat]

  P2_selective_archive:
    - source_id: S019
      title: "DATEV §13b UStG Tatbestände"
      exact_sections_to_capture: ["§13b-Markierung", "Buchungs-/Steuerbüroübergabe"]
      topic_tags: [reverse_charge, datev]

    - source_id: S020
      title: "DATEV SKR42 Kontenrahmen"
      exact_sections_to_capture: ["wirtschaftlicher Geschäftsbetrieb", "Kontenrahmenlogik"]
      topic_tags: [accounting, skr42]

    - source_id: S022
      title: "LfSt Bayern Merkblatt Festveranstaltungen"
      exact_sections_to_capture: ["Event-Einnahmen", "Event-Ausgaben", "USt-Prüffelder"]
      warning: "Gemeinnützigkeit/Zweckbetrieb markieren"
      topic_tags: [event_tax]

    - source_id: S025
      title: "Eventbrite Umsatzübersicht"
      exact_sections_to_capture: ["Bruttoumsatz", "Gebühren", "Refunds", "Tax", "Payout"]
      topic_tags: [reconciliation, reports]

    - source_id: S030
      title: "Michow & Ulbricht Musterverträge Live Entertainment"
      exact_sections_to_capture: ["Vertragsstruktur", "Künstler-/Eventvertragspunkte"]
      topic_tags: [templates, contracts]

  P3_reference_only:
    - source_id: S028
      title: "EVENTFAQ Mietvertrag Location"
      reason: "nur Vertragscheck; keine belastbare USt-Quelle"
    - source_id: S031
      title: "Deutsches Ehrenamt Buchführung Verein"
      reason: "Praxisorientiert, aber nicht autoritativ"
    - source_id: S032
      title: "Deutsches Ehrenamt Auslagenersatz"
      reason: "Auslagenidee, aber Gemeinnützigkeits-/Ehrenamtsrisiko"
    - source_id: S035
      title: "Lexware Stornorechnung"
      reason: "nur Begriffsklärung"

  D_discard:
    - source_id: S034
      title: "TSV Gersthofen Auslagenformular"
      reason: "fremdes Vereinsformular; nicht autoritativ"
      replacement: "eigene Vorlage auf Basis Minijob-Zentrale/DRV + interner Belegprozess"
    - source_id: S038
      title: "generische SEO-Vereinssteuerblogs"
      reason: "Gemeinnützigkeitskontamination / dünn / nicht belastbar"
      replacement: "Finanzverwaltung NRW, BMF, IHK, DATEV"
```

---

# 7. Themen-Coverage-Ranking

|Thema|Coverage|Confidence|Beste Quellen|Schwäche|Next Action|
|---|--:|--:|---|---|---|
|Rechnungsstellung|90|88|S001, S002, S003|Ticket-Sonderfall|archivieren|
|Kleinbetragsrechnung / Ticket als Rechnung|82|75|S001, S003, S012|kein offizielles Eventticket-Beispiel|Ticketanbieterrolle prüfen|
|E-Rechnung|85|85|S009, S010|B2C-Tickets nicht Kern|B2B-Prozess bauen|
|Umsatzsteuer allgemein|75|72|S011, S006, S009|Vereinsquellen oft gemeinnützig|markieren|
|7% vs. 19% Ticket-USt|52|45|S022, S023, S037, S013|Club-/DJ-Mischformat offen|Steuerberaterentscheidung|
|Vereinsbesteuerung nicht gemeinnütziger e.V.|58|50|S011, S020, S031|wenige direkte Quellen|gezielte Nachrecherche|
|EÜR|62|55|S011, S020, S031|operative Kontierung offen|Steuerbüro-Mapping|
|GoBD|92|90|S006, S007, S008|Umsetzung für kleines Team|Verfahrensdoku erstellen|
|Verfahrensdokumentation|90|88|S007, S008, S012|Safer-Space-spezifisch noch zu bauen|Template adaptieren|
|Ticketing-Anbieterrolle|78|70|S012, S013, S014|provider-spezifisch|pretix bevorzugt prüfen|
|Ticketing-Export / DATEV|76|68|S012, S014, S025, S026|Anbieterwahl offen|Export-Minimum definieren|
|Stripe/PayPal/Payout-Reconciliation|58|45|S025, S026, S014|Payment-Provider-Doku dünn|weitere Recherche|
|Refunds / Storno / Rechnungskorrektur|74|65|S014, S035, S023|Steuerliche Korrektur nicht vollständig offiziell|Workflow mit Steuerbüro|
|Venue Settlement|40|35|S024, S028, S030|größte Lücke|Vertrags-/Steuerprüfung|
|Mindestbarumsatz / Barumsatzgarantie|35|30|S024, S028|kaum konkrete Quellen|Steuerberater + Vertrag|
|KSK|92|90|S004, S005|Einzelfall Tätigkeit|KSK-Matrix bauen|
|Künstlerhonorare|84|80|S004, S005, S017|Ausland kombiniert komplex|Contractor-Check|
|Ausländische Künstler / §50a|86|82|S017, S005|DBA/Einzelfall offen|BZSt-Prozess bauen|
|Reverse Charge|76|68|S018, S019, S012|HK-Hamburg teils nur Referenz|BMF/UStAE ergänzen|
|Crew / Helfer / Minijob|86|82|S015, S016|Event-Crew-Konstellation|Statusmatrix|
|Scheinselbstständigkeit|86|83|S016|Einzelfall|Onboarding-Fragen|
|Auslagenersatz|58|48|S032, S033, S015|Ehrenamt/Gemeinnützigkeit riskant|eigene Vorlage|
|Dokumentenvorlagen|72|65|S008, S030, S034|fremde Templates riskant|eigene Safer-Space-Templates|

---

# 8. Quellen mit hohem Transfer-Risiko

|Quelle|Risiko|Safe Use|Unsafe Use|
|---|---|---|---|
|LfSt Bayern Festveranstaltungen|Gemeinnützigkeit/Zweckbetrieb/Festveranstaltung|Event-Einnahmen-/Ausgaben-Prüffelder|Zweckbetrieb oder Steuerfreiheit ableiten|
|DATEV SKR42|Sphärenlogik gemeinnütziger Körperschaften|Kontenrahmen-/Kategorie-Orientierung|automatische Kontierung als gemeinnütziger Verein|
|Finanzverwaltung NRW Vereine|enthält oft Vereins-/Gemeinnützigkeitslogik|USt-/ELSTER-Grundlagen|Steuerbefreiung übernehmen|
|Deutsches Ehrenamt|Praxisnah, aber sekundär und oft gemeinnützigkeitsnah|Beleg-/Ablauforientierung|Spenden-/Ehrenamtspauschalen übernehmen|
|Wegweiser Bürgergesellschaft|Ehrenamt-/Pauschalen-Kontext|Hintergrund|Zahlungen an Club-Crew steuerfrei behandeln|
|Ticketing-Anbieter-Dokus|Provider bias, keine Steuerberatung|technische Umsetzung, Exportfelder|USt-Satz/Steuerbefreiung entscheiden|
|EVENTFAQ / Beck Law / Kanzlei-Muster|rechtlich nützlich, aber nicht steuerlich final|Vertragschecklisten|Mindestumsatz-USt final ableiten|
|Fremde Vereinsformulare|kein Autoritätswert|Layout-Idee|als geprüfte Vorlage verwenden|
|Lexware|Software-/SEO-Wissensartikel|Begriffsklärung|finaler Rechnungskorrekturstandard|

---

# 9. Ausschlussliste mit Ersatzquellen

|Ausschließen aus Core-KB|Grund|Ersatz|
|---|---|---|
|TSV Gersthofen Auslagenformular|fremder Sportverein, keine Autorität|eigene Vorlage auf Basis S015/S016 + Belegprozess|
|generische SEO-Vereinssteuerblogs|dünn, häufig falsche Gemeinnützigkeitsannahmen|Finanzverwaltung NRW, BMF, IHK|
|PayPal Pricing/Marketing-Seiten|reine Gebühren-/Marketinginfo|echte Payment-Reports + Kontoauszüge|
|ticket.io FAQ ohne Exporttiefe|Marketing/FAQ, wenig prüfbar|konkrete Anbieterabrechnung + Vertrag|
|Medienberichte zu Berghain/BFH ohne Primärquelle|journalistisch, nicht ausreichend|BFH-Urteil / BMF / UStAE|
|Beck Law Locationvertrag als Core|zu dünn / nicht steuerlich|EVENTFAQ selektiv + konkreter Vertrag + Steuerberatung|
|Vereinswelt/VNR Templates als Core|Verlag/SEO, Ehrenamtsrisiko|AWV-Template + eigene Safer-Space-Vorlagen|

---

# 10. Top-20-Kernbibliothek

|Rank|Quelle|Score|Warum|
|--:|---|--:|---|
|1|KSK Informationsschrift Nr. 4|93|direkt Veranstalter/Künstler:innen|
|2|§33 UStDV Kleinbetragsrechnung|92|Normanker für Ticketbeleg|
|3|BMF GoBD 2024|91|Pflichtanker Archiv|
|4|IHK Pflichtangaben Rechnungen|90|Rechnungspflichtangaben|
|5|IHK Kleinbetragsrechnung Checkliste|89|Ticket-/Belegcheckliste|
|6|DRV K5001|88|KSK-Prüfung/Dokumentation|
|7|AWV Muster-Verfahrensdoku|88|beste Vorlage|
|8|BZSt §50a|87|Auslandskünstler:innen|
|9|DATEV Verfahrensdokumentation|86|GoBD praktisch|
|10|BMF E-Rechnung FAQ|86|B2B-Pflicht|
|11|Minijob-Zentrale kurzfristige Beschäftigung|86|bezahlte Helfer:innen|
|12|DRV Scheinselbstständigkeit|86|Contractor-Risiko|
|13|IHK München E-Rechnung|84|operative Umsetzung|
|14|Finanzverwaltung NRW Vereine/USt|84|Vereins-USt, ELSTER|
|15|BFH Vorverkaufsgebühr|84|Ticketgebühren/USt|
|16|pretix Fiscal Germany|82|Ticketing-GoBD/Export|
|17|UStH/BMF Schadensersatz|82|Venue-Mindestumsatz-Prüffeld|
|18|pretix Order Lifecycle|80|Storno/Refund|
|19|pretix Taxes|76|Steuerregel-Setup|
|20|Handelskammer Hamburg Reverse Charge|76|Auslandsdienstleister-Prüffeld|

---

# 11. Noch offene Gaps

```yaml
remaining_gaps:
  - gap: "Venue-Settlement / Mindestbarumsatz / Barumsatzgarantie"
    severity: "critical"
    why_not_closed: "kaum offizielle oder praxisnahe Steuerquellen für Club-Mindestbarumsatz; vorhandene Quellen liefern eher Vertragsstruktur oder allgemeine Schadensersatzlogik"
    recommended_future_research:
      - "Barumsatzgarantie Umsatzsteuer"
      - "Mindestumsatz Eventlocation Rechnung"
      - "echter unechter Schadensersatz Umsatzsteuer Mindestumsatz"
      - "Clubmiete Mindestverzehr Umsatzsteuer"
    needed_source_type:
      - "Steuerkanzlei-Fachbeitrag mit Beispielen"
      - "BMF/UStH Schadensersatz"
      - "konkreter Venue-Vertrag"
      - "Steuerberater-Votum"

  - gap: "7% vs. 19% Ticket-USt bei Club-/DJ-/Kultur-Mischformat"
    severity: "critical"
    why_not_closed: "Quellen liefern Prüffelder, aber keine sichere Einordnung des konkreten Events"
    recommended_future_research:
      - "ermäßigter Umsatzsteuersatz Konzert DJ Veranstaltung"
      - "Clubnacht kulturelle Veranstaltung Umsatzsteuer 7 Prozent"
      - "BFH Konzertähnliche Veranstaltung DJ Umsatzsteuer"
    needed_source_type:
      - "BFH/BMF/UStAE"
      - "Steuerberater-Fallprüfung"
      - "Finanzamt-Anfrage optional"

  - gap: "Ticket als Rechnung ausdrücklich für Eventtickets"
    severity: "medium_high"
    why_not_closed: "§33 UStDV + IHK + pretix reichen für Gestaltungslogik, aber nicht als explizite Eventticket-Bestätigung"
    recommended_future_research:
      - "Eintrittskarte als Rechnung Umsatzsteuer"
      - "Ticket als Kleinbetragsrechnung Veranstalter"
      - "Rechnung im Namen des Veranstalters Ticketing"
    needed_source_type:
      - "IHK/Steuerberaterkammer"
      - "pretix konkrete Rechnung-im-Namen-des-Veranstalters Doku"
      - "Ticketanbieter-AGB"

  - gap: "Stripe/PayPal/Payout-Reconciliation"
    severity: "medium"
    why_not_closed: "Providerberichte sind operativ, aber steuerliche Verbuchung bleibt unvollständig"
    recommended_future_research:
      - "Stripe payout reconciliation accounting VAT Germany"
      - "PayPal Gebühren Umsatzsteuer Reverse Charge Deutschland Verein"
    needed_source_type:
      - "Provider-Dokumentation"
      - "DATEV/Steuerkanzlei-Leitfaden"

  - gap: "Nicht gemeinnütziger e.V. mit Club-/Kultur-Fundraiser"
    severity: "medium_high"
    why_not_closed: "Vereinsquellen sind meist gemeinnützigkeitszentriert"
    recommended_future_research:
      - "nicht gemeinnütziger Verein Umsatzsteuer Veranstaltung"
      - "wirtschaftlicher Geschäftsbetrieb nicht gemeinnütziger Verein Körperschaftsteuer"
    needed_source_type:
      - "Finanzverwaltung"
      - "IHK"
      - "Steuerberaterkammer"
```

---

# 12. Finale Empfehlung für die Wissensdatenbank

```yaml
final_recommendation:
  core_kb_size:
    target: "20 Kernquellen"
    reason: "genug für belastbares Playbook, ohne SEO-/Provider-Rauschen"

  archive_now:
    count: 16
    classes:
      - "P0 official_primary"
      - "P0 official_guide"
      - "P0 institutional_guide"
      - "P0 template"
    include:
      - "BMF/BMJ/BZSt/KSK/DRV/Minijob-Zentrale"
      - "IHK-Rechnung/E-Rechnung"
      - "BMF/DATEV/AWV-GoBD"
      - "pretix Fiscal/Taxes/Order Lifecycle"

  archive_later:
    count: 10
    classes:
      - "P1 provider_operational"
      - "P2 professional_secondary"
      - "P2 template_selective"
    include:
      - "Eventbrite/ticket.io nur bei Anbieterrelevanz"
      - "LfSt Bayern nur markiert"
      - "DATEV SKR42 nur mit Nicht-Gemeinnützigkeitswarnung"

  do_not_archive_core:
    count: 7
    include:
      - "fremde Vereinsformulare"
      - "SEO-Blogs"
      - "Marketingseiten"
      - "dünne Kanzlei-/Lexikonseiten ohne steuerliche Tiefe"

  knowledge_base_rules:
    - "Jede Quelle mit Gemeinnützigkeitsannahme bekommt Flag gemeinnuetzigkeit_assumed."
    - "Provider-Dokumentation darf Workflow erklären, aber keine Steuerentscheidung treffen."
    - "Venue-Settlement darf nicht ohne Steuerberaterentscheidung operationalisiert werden."
    - "Ticket als Rechnung: nur als gestaltbarer Kleinbetragsbeleg modellieren, nicht als automatisch geklärt."
    - "7% Ticket-USt nur als Entscheidungsbaum mit finaler externer Prüfung aufnehmen."

  next_best_action:
    - "P0/P1 Quellen archivieren und in saubere Markdown/PDF-Snapshots bringen."
    - "Für Venue und 7%-vs.-19%-USt einen separaten Mini-Research + Steuerberater-Fragenkatalog erstellen."
    - "Danach erst das Event-Steuer-/Buchhaltungs-Playbook bauen."
```

**Bottom line:** Die KB sollte jetzt mit einer **P0/P1-Core-Library von ca. 20 Quellen** starten. Alles zu **Venue-Settlement, Mindestbarumsatz und USt-Satz** bleibt außerhalb der automatisierten Playbook-Regeln und wird als **Prüfentscheidung** geführt.