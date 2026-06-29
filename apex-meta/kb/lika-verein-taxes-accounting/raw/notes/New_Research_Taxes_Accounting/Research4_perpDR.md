gap_closure_research_result:
  executive_summary:
    most_critical_remaining_gaps: >
      VAT rate classification (7% vs. 19%) for club/DJ events, venue settlement and
      minimum bar revenue (damages vs. consideration), and detailed implementation
      of ticket-as-invoice and Istversteuerung/refunds remain partly unresolved and
      should be validated with a tax advisor.[web:3][web:41][web:46]
    sources_that_are_not_good_enough: >
      Generic SEO-style Vereinssteuer blogs and non-official Verein tax overviews
      are too mixed with Gemeinnützigkeitsannahmen and lack precise guidance for
      non-charitable, ticketed club events, so they should be treated as secondary
      commentary only.[web:48][web:56]
    sources_that_are_real_guides: >
      The IHK Berlin Pflichtangaben-in-Rechnungen article, the IHK Niederbayern
      Kleinbetragsrechnung checklist PDF, the GoBD BMF-Schreiben and AWV Muster-
      Verfahrensdokumentation, KSK Informationsschrift Nr. 4, Minijob-Zentrale
      Kurzfristige Beschäftigung, DRV Scheinselbstständigkeit guidance, NRW
      Finanzverwaltung ELSTER/Vereine brochure, and pretix fiscal/tax docs are
      all substantive guides suitable for KB ingestion.[web:1][web:10][web:6][web:7][web:9][web:16][web:17][web:8][web:31][web:32]
    sources_to_download_now: >
      For immediate archiving: §33 UStDV (Gesetze im Internet), IHK Pflichtangaben
      and Kleinbetragsrechnung checklist, GoBD BMF-Schreiben PDF, AWV Muster-
      Verfahrensdokumentation plus DOCX Vorlage, KSK Info 4 and DRV K5001, Minijob-
      Zentrale Kurzfristige Beschäftigung checklist, DRV Scheinselbstständigkeit
      text, pretix fiscal and tax docs, NRW "Mein ELSTER für Vereine", and
      Brandenburg/NMV "Vereine und Steuern" for general association tax context
      with clear Gemeinnützigkeits warnings.[web:3][web:1][web:10][web:15][web:7][web:12][web:9][web:16][web:21][web:17][web:31][web:32][web:8][web:54][web:51]
    sources_to_discard: >
      Thin marketing pages (e.g. generic ticket.io FAQ without export detail),
      purely promotional PayPal pricing pages, and media-only Berghain coverage
      without direct citation of BFH/BMF are not suitable as primary KB content
      and should be used, at most, as low-priority references.[web:33][web:34][web:39]
    overall_source_base_readiness_score_0_100: 68

  source_audit:
    - source_id: invoices_1
      title: "Pflichtangaben in Rechnungen"
      publisher: "IHK Berlin"
      url: "https://www.ihk.de/berlin/service-und-beratung/recht-und-steuern/steuern-und-finanzen/pflichtangaben-in-rechnungen-4400732"
      final_url_after_redirect: "https://www.ihk.de/berlin/service-und-beratung/recht-und-steuern/steuern-und-finanzen/pflichtangaben-in-rechnungen-4400732"
      reachable: true
      source_type: ihk_hwk
      content_format: html_guide
      real_guide_or_thin_page: real_guide
      authority_score_0_10: 7
      guide_quality_score_0_10: 8
      extractability_score_0_10: 7
      downloadability_score_0_10: 5
      navigation_noise_risk: low
      gemeinnuetzigkeits_transfer_risk:
        level: low
        unsafe_assumptions: []
        safe_parts: "Rechnungspflichtangaben nach UStG/AO, unabhängig von Gemeinnützigkeit.[web:1]"
        unsafe_parts: ""
      kb_ingestion_decision: archive_html_snapshot
      reason: "Authoritative IHK guidance with clear lists of Pflichtangaben and examples, good long-term reference for ticket-as-invoice logic.[web:1]"
      citation: "[web:1]"

    - source_id: invoices_2
      title: "Checkliste Kleinbetragsrechnungen bis 250 Euro"
      publisher: "IHK Niederbayern"
      url: "https://www.ihk-niederbayern.de/pdfs/checkliste-kleinbetragsrechnungen-data.pdf"
      final_url_after_redirect: "https://www.ihk-niederbayern.de/pdfs/checkliste-kleinbetragsrechnungen-data.pdf"
      reachable: true
      source_type: ihk_hwk
      content_format: downloadable_pdf
      real_guide_or_thin_page: real_guide
      authority_score_0_10: 7
      guide_quality_score_0_10: 8
      extractability_score_0_10: 9
      downloadability_score_0_10: 9
      navigation_noise_risk: low
      gemeinnuetzigkeits_transfer_risk:
        level: low
        unsafe_assumptions: []
        safe_parts: "Checkliste mit Pflichtangaben für Kleinbetragsrechnungen nach §33 UStDV, direkt übertragbar auf Tickets.[web:10][web:3]"
        unsafe_parts: ""
      kb_ingestion_decision: archive_pdf
      reason: "Structured checklist PDF, ideal as a KB template for validating whether an entrance ticket qualifies as Kleinbetragsrechnung.[web:10]"
      citation: "[web:10]"

    - source_id: invoices_3
      title: "§33 UStDV – Rechnungen über Kleinbeträge"
      publisher: "Gesetze im Internet (BMJ/BGBl-Texte)"
      url: "https://www.gesetze-im-internet.de/ustdv_1980/__33.html"
      final_url_after_redirect: "https://www.gesetze-im-internet.de/ustdv_1980/__33.html"
      reachable: true
      source_type: official_law
      content_format: legal_text
      real_guide_or_thin_page: real_guide
      authority_score_0_10: 10
      guide_quality_score_0_10: 7
      extractability_score_0_10: 9
      downloadability_score_0_10: 7
      navigation_noise_risk: low
      gemeinnuetzigkeits_transfer_risk:
        level: low
        unsafe_assumptions: []
        safe_parts: "Normtext zu Kleinbetragsrechnungen mit klaren Mindestangaben, zentral für Ticket-als-Rechnung-Logik.[web:3]"
        unsafe_parts: ""
      kb_ingestion_decision: archive_html_snapshot
      reason: "Primary legal rule for Kleinbetragsrechnungen; essential backbone for automated reasoning on ticket invoice requirements.[web:3]"
      citation: "[web:3]"

    - source_id: e_invoice_1
      title: "FAQ zur verpflichtenden E-Rechnung"
      publisher: "BMF (aggregated via elektronisches-steuerpruefung.de)"
      url: "https://www.bundesfinanzministerium.de/Content/DE/FAQ/e-rechnung.html"
      final_url_after_redirect: "https://elektronische-steuerpruefung.de/bmf/faq-einfuehrung-obligatorische-e-rechnung.htm"
      reachable: true
      source_type: official_tax_authority
      content_format: faq
      real_guide_or_thin_page: mixed
      authority_score_0_10: 8
      guide_quality_score_0_10: 7
      extractability_score_0_10: 6
      downloadability_score_0_10: 5
      navigation_noise_risk: medium
      gemeinnuetzigkeits_transfer_risk:
        level: low
        unsafe_assumptions: []
        safe_parts: "E-Rechnung-Pflichten und Übergangsregeln, relevant für Eingangsrechnungen an Safer Space e.V. und zukünftige Ausgangsrechnungen.[web:4]"
        unsafe_parts: ""
      kb_ingestion_decision: archive_html_snapshot
      reason: "Official FAQ with evolving details on e-invoice obligations; useful for long-term compliance but less central than GoBD/verfahrensdoku.[web:4]"
      citation: "[web:4]"

    - source_id: e_invoice_2
      title: "Elektronische Rechnungen (Präsentation)"
      publisher: "IHK München/Oberbayern"
      url: "https://www.ihk-muenchen.de/ratgeber/steuern/elektronische-rechnungen/"
      final_url_after_redirect: "https://www.ihk-muenchen.de/Neu/E-RechnungMartinClemens.pdf"
      reachable: true
      source_type: ihk_hwk
      content_format: downloadable_pdf
      real_guide_or_thin_page: real_guide
      authority_score_0_10: 7
      guide_quality_score_0_10: 7
      extractability_score_0_10: 7
      downloadability_score_0_10: 9
      navigation_noise_risk: low
      gemeinnuetzigkeits_transfer_risk:
        level: low
        unsafe_assumptions: []
        safe_parts: "Slides explaining legal and technical aspects of e-receipts and E-Rechnung; practical background for digital workflows.[web:5]"
        unsafe_parts: ""
      kb_ingestion_decision: archive_pdf
      reason: "Good technical-legal overview; secondary but useful complement to BMF FAQ.[web:5]"
      citation: "[web:5]"

    - source_id: gobd_1
      title: "GoBD – BMF-Schreiben Änderung 2024"
      publisher: "Bundesministerium der Finanzen"
      url: "https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Weitere_Steuerthemen/Abgabenordnung/AO-Anwendungserlass/2024-03-11-aenderung-gobd.html"
      final_url_after_redirect: "https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Weitere_Steuerthemen/Abgabenordnung/AO-Anwendungserlass/2024-03-11-aenderung-gobd.pdf"
      reachable: true
      source_type: official_tax_authority
      content_format: downloadable_pdf
      real_guide_or_thin_page: real_guide
      authority_score_0_10: 10
      guide_quality_score_0_10: 8
      extractability_score_0_10: 6
      downloadability_score_0_10: 9
      navigation_noise_risk: medium
      gemeinnuetzigkeits_transfer_risk:
        level: low
        unsafe_assumptions: []
        safe_parts: "Verbindliche Grundsätze zur Führung und Aufbewahrung elektronischer Unterlagen inkl. Datenzugriff; maßgeblich für Safer-Space-Eventarchiv.[web:6][web:15]"
        unsafe_parts: ""
      kb_ingestion_decision: archive_pdf
      reason: "Primary GoBD source that should anchor all document-archive and verfahrensdoku guidelines.[web:6][web:15]"
      citation: "[web:6][web:15]"

    - source_id: gobd_2
      title: "Verfahrensdokumentation gemäß GoBD erstellen"
      publisher: "DATEV"
      url: "https://www.datev.de/web/de/berufsgruppenuebergreifend/ratgeber/rechnungswesen/verfahrensdokumentation-gemaess-gobd-erstellen"
      final_url_after_redirect: "https://www.datev.de/web/de/berufsgruppenuebergreifend/gesetzliche-themen/gobd/aenderung-vom-11-maerz-2024"
      reachable: true
      source_type: datev_or_awv
      content_format: html_guide
      real_guide_or_thin_page: real_guide
      authority_score_0_10: 8
      guide_quality_score_0_10: 8
      extractability_score_0_10: 7
      downloadability_score_0_10: 5
      navigation_noise_risk: medium
      gemeinnuetzigkeits_transfer_risk:
        level: low
        unsafe_assumptions: []
        safe_parts: "Explains structure, required content, and practical creation of GoBD-compliant Verfahrensdokumentation, including event-related processes.[web:14]"
        unsafe_parts: ""
      kb_ingestion_decision: archive_html_snapshot
      reason: "High-quality professional guide directly implementable as a template for Safer Space’s event accounting workflow documentation.[web:14]"
      citation: "[web:14]"

    - source_id: gobd_3
      title: "Muster-Verfahrensdokumentation zur Belegablage"
      publisher: "AWV (Arbeitsgemeinschaft für wirtschaftliche Verwaltung e.V.)"
      url: "https://www.awv-net.de/publikationen/datenverarbeitung/"
      final_url_after_redirect: "https://www.awv-net.de/publikationen-produkte/publikationen/detailseite/musterverfahrensdokumentation-zur-belegablage"
      reachable: true
      source_type: awv
      content_format: checklist
      real_guide_or_thin_page: real_guide
      authority_score_0_10: 8
      guide_quality_score_0_10: 8
      extractability_score_0_10: 9
      downloadability_score_0_10: 9
      navigation_noise_risk: low
      gemeinnuetzigkeits_transfer_risk:
        level: low
        unsafe_assumptions: []
        safe_parts: "Provides a concrete Muster-Verfahrensdokumentation and DOCX template for Belegablage and electronic workflows.[web:7][web:12]"
        unsafe_parts: ""
      kb_ingestion_decision: archive_pdf
      reason: "Excellent structural template for KB-ingested workflow documentation, directly adaptable to event ticketing and payouts.[web:7][web:12]"
      citation: "[web:7][web:12]"

    - source_id: vat_association_1
      title: "Mein ELSTER für Vereine (Umsatzsteuer/Erklärungen)"
      publisher: "Finanzverwaltung NRW"
      url: "https://www.finanzamt.nrw.de/steuerinfos/weitere-themen/vereine-und-stiftungen/vereine-und-die-umsatzsteuer"
      final_url_after_redirect: "https://www.finanzverwaltung.nrw.de/system/files/media/document/file/2026_05_26_internet_endf_einzs_brosch_meinelstervereine.pdf"
      reachable: true
      source_type: official_tax_authority
      content_format: downloadable_pdf
      real_guide_or_thin_page: real_guide
      authority_score_0_10: 9
      guide_quality_score_0_10: 8
      extractability_score_0_10: 8
      downloadability_score_0_10: 9
      navigation_noise_risk: low
      gemeinnuetzigkeits_transfer_risk:
        level: medium
        unsafe_assumptions:
          - "Gemeinnützigkeitsvorteile"
        safe_parts: "Erklärungspflichten, ELSTER-Nutzung, Grundzüge Umsatzsteuer/KSt/GewSt für Vereine allgemein.[web:8]"
        unsafe_parts: "Abschnitte zu Steuerbefreiungen und Sonderregeln für gemeinnützige Vereine müssen für Safer Space e.V. deutlich abgegrenzt werden.[web:8]"
      kb_ingestion_decision: archive_pdf
      reason: "High-value overview for association tax filings and ELSTER processes, but must be flagged for Gemeinnützigkeitskontamination.[web:8]"
      citation: "[web:8]"

    - source_id: ksk_1
      title: "Informationsschrift Nr. 4 – Abgabepflicht von Veranstaltern"
      publisher: "Künstlersozialkasse"
      url: "https://www.kuenstlersozialkasse.de/fileadmin/Dokumente/Mediencenter_Unternehmer_Verwerter/Informationsschriften/Info_04_Abgabepflicht_von_Veranstaltern.pdf"
      final_url_after_redirect: "https://www.kuenstlersozialkasse.de/fileadmin/Dokumente/Mediencenter_Unternehmer_Verwerter/Informationsschriften/Info_04_Abgabepflicht_von_Veranstaltern.pdf"
      reachable: true
      source_type: official_social_insurance
      content_format: downloadable_pdf
      real_guide_or_thin_page: real_guide
      authority_score_0_10: 10
      guide_quality_score_0_10: 9
      extractability_score_0_10: 8
      downloadability_score_0_10: 9
      navigation_noise_risk: low
      gemeinnuetzigkeits_transfer_risk:
        level: low
        unsafe_assumptions: []
        safe_parts: "Definiert abgabepflichtige Veranstaltertypen, Bemessungsgrundlagen und Meldepflichten für Künstlersozialabgabe bei kulturellen Veranstaltungen.[web:9]"
        unsafe_parts: ""
      kb_ingestion_decision: archive_pdf
      reason: "Core KSK compliance document for DJ/performer bookings; must be in KB for contractor matrix.[web:9]"
      citation: "[web:9]"

    - source_id: ksk_2
      title: "Information zur Künstlersozialabgabe (K5001)"
      publisher: "Deutsche Rentenversicherung"
      url: "https://www.deutsche-rentenversicherung.de/SharedDocs/Formulare/DE/_pdf/K5001.pdf"
      final_url_after_redirect: "https://www.deutsche-rentenversicherung.de/SharedDocs/Formulare/DE/_pdf/K5001.pdf"
      reachable: true
      source_type: official_social_insurance
      content_format: downloadable_pdf
      real_guide_or_thin_page: real_guide
      authority_score_0_10: 9
      guide_quality_score_0_10: 8
      extractability_score_0_10: 7
      downloadability_score_0_10: 9
      navigation_noise_risk: low
      gemeinnuetzigkeits_transfer_risk:
        level: low
        unsafe_assumptions: []
        safe_parts: "Formular und Merkblatt mit Informationen zur Künstlersozialabgabe aus DRV-Sicht.[web:13]"
        unsafe_parts: ""
      kb_ingestion_decision: archive_pdf
      reason: "Complements KSK Info 4 with DRV perspective; good to ingest alongside KSK docs.[web:13]"
      citation: "[web:13]"

    - source_id: foreign_services_1
      title: "Reverse Charge – Umsatzsteuerschuldnerschaft international"
      publisher: "Handelskammer Hamburg"
      url: "https://www.handelskammer-hamburg.de/recht-steuern/steuerrecht/umsatzsteuer-mehrwertsteuer/umsatzsteuer-mehrwertsteuer-international/umsatzsteuersteuerschuldnerschaft-reverse-charge-6682954"
      final_url_after_redirect: ""
      reachable: false
      source_type: ihk_hwk
      content_format: thin_webpage
      real_guide_or_thin_page: thin_page
      authority_score_0_10: 5
      guide_quality_score_0_10: 4
      extractability_score_0_10: 3
      downloadability_score_0_10: 1
      navigation_noise_risk: medium
      gemeinnuetzigkeits_transfer_risk:
        level: low
        unsafe_assumptions: []
        safe_parts: ""
        unsafe_parts: ""
      kb_ingestion_decision: reference_only
      reason: "Not directly accessed in this run; likely short overview but better to rely on UStAE/BMF for reverse-charge rules."[web:52]
      citation: "[web:52]"

    - source_id: foreign_services_2
      title: "Abzugsteuern nach §50a EStG"
      publisher: "Bundeszentralamt für Steuern (BZSt)"
      url: "https://www.bzst.de/DE/Privatpersonen/Abzugsteuern_50a/abzugsteuern_node.html"
      final_url_after_redirect: "https://www.bzst.de/DE/Privatpersonen/Abzugsteuern_50a/abzugsteuern_node.html"
      reachable: true
      source_type: bzst
      content_format: html_guide
      real_guide_or_thin_page: real_guide
      authority_score_0_10: 9
      guide_quality_score_0_10: 7
      extractability_score_0_10: 6
      downloadability_score_0_10: 4
      navigation_noise_risk: medium
      gemeinnuetzigkeits_transfer_risk:
        level: low
        unsafe_assumptions: []
        safe_parts: "Explains withholding tax obligations under §50a EStG, including cultural performances by foreign artists.[web:46]"
        unsafe_parts: ""
      kb_ingestion_decision: archive_html_snapshot
      reason: "Essential legal authority for foreign artist taxation; must be part of contractor matrix.[web:46]"
      citation: "[web:46]"

    - source_id: contractor_crew_1
      title: "Kurzfristige Beschäftigung"
      publisher: "Minijob-Zentrale"
      url: "https://www.minijob-zentrale.de/DE/die-minijobs/kurzfristige-beschaeftigung"
      final_url_after_redirect: "https://www.minijob-zentrale.de/DE/die-minijobs/kurzfristige-beschaeftigung"
      reachable: true
      source_type: minijob-zentrale
      content_format: html_guide
      real_guide_or_thin_page: real_guide
      authority_score_0_10: 9
      guide_quality_score_0_10: 8
      extractability_score_0_10: 7
      downloadability_score_0_10: 4
      navigation_noise_risk: low
      gemeinnuetzigkeits_transfer_risk:
        level: low
        unsafe_assumptions: []
        safe_parts: "Defines time limits, insurance status, and employer obligations for kurzfristige Beschäftigung.[web:16][web:28]"
        unsafe_parts: ""
      kb_ingestion_decision: archive_html_snapshot
      reason: "Key input for classifying short-term crew/paid helpers vs. volunteers.[web:16][web:28]"
      citation: "[web:16][web:28]"

    - source_id: contractor_crew_2
      title: "Scheinselbstständigkeit erkennen"
      publisher: "Deutsche Rentenversicherung"
      url: "https://www.deutsche-rentenversicherung.de/DRV/DE/Rente/Arbeitnehmer-und-Selbststaendige/03_Selbststaendige/scheinselbststaendigkeit"
      final_url_after_redirect: "https://www.deutsche-rentenversicherung.de/DRV/DE/Rente/Arbeitnehmer-und-Selbststaendige/03_Selbststaendige/scheinselbststaendige_node.html"
      reachable: true
      source_type: deutsche_rentenversicherung
      content_format: html_guide
      real_guide_or_thin_page: real_guide
      authority_score_0_10: 9
      guide_quality_score_0_10: 8
      extractability_score_0_10: 7
      downloadability_score_0_10: 4
      navigation_noise_risk: medium
      gemeinnuetzigkeits_transfer_risk:
        level: low
        unsafe_assumptions: []
        safe_parts: "Explains criteria and Anfrageverfahren for distinguishing employment vs. self-employment under §7 SGB IV.[web:17][web:22]"
        unsafe_parts: ""
      kb_ingestion_decision: archive_html_snapshot
      reason: "Crucial for contractor/crew matrix and employment risk assessment.[web:17][web:22]"
      citation: "[web:17][web:22]"

    - source_id: contractor_crew_3
      title: "Der Auslagenersatz im Verein"
      publisher: "Deutsches Ehrenamt"
      url: "https://deutsches-ehrenamt.de/steuern-finanzen/aufwandsentschaedigung-verguetung/auslagenersatz/"
      final_url_after_redirect: "https://deutsches-ehrenamt.de/steuern-finanzen/aufwandsentschaedigung-verguetung/auslagenersatz/"
      reachable: true
      source_type: professional_guide
      content_format: html_guide
      real_guide_or_thin_page: mixed
      authority_score_0_10: 6
      guide_quality_score_0_10: 6
      extractability_score_0_10: 6
      downloadability_score_0_10: 3
      navigation_noise_risk: medium
      gemeinnuetzigkeits_transfer_risk:
        level: high
        unsafe_assumptions:
          - "§3 Nr. 50 EStG steuerfreie Auslagenersätze im Ehrenamt"
          - "implizite Gemeinnützigkeitsannahmen"
        safe_parts: "Grunddefinition Auslagenersatz und Abgrenzung zur pauschalen Aufwandsentschädigung.[web:18][web:23]"
        unsafe_parts: "Steuerfreiheit und Pauschalierungsbeispiele sind für nicht gemeinnützige e.V. nur eingeschränkt übertragbar.[web:18][web:23]"
      kb_ingestion_decision: inspiration_only
      reason: "Useful conceptual starting point but too contaminated by Ehrenamt/Gemeinnützigkeit-specific assumptions.[web:18][web:23]"
      citation: "[web:18][web:23]"

    - source_id: contractor_crew_4
      title: "Ehrenamt, Auslagen, Aufwandsentschädigung"
      publisher: "Wegweiser Bürgergesellschaft"
      url: "https://www.buergergesellschaft.de/praxishilfen/arbeit-im-verein/rechtsgrundlagen/ehrenamtliche-mitarbeit-arbeits-beschaeftigungs-und-dienstverhaeltnisse/ehrenamt-auslagen-aufwandsentschaedigung/"
      final_url_after_redirect: ""
      reachable: false
      source_type: professional_guide
      content_format: thin_webpage
      real_guide_or_thin_page: mixed
      authority_score_0_10: 5
      guide_quality_score_0_10: 5
      extractability_score_0_10: 4
      downloadability_score_0_10: 1
      navigation_noise_risk: medium
      gemeinnuetzigkeits_transfer_risk:
        level: high
        unsafe_assumptions:
          - "Ehrenamts-/Übungsleiterpauschalen"
        safe_parts: ""
        unsafe_parts: ""
      kb_ingestion_decision: discard
      reason: "Not accessed and likely focused on Gemeinnützigkeit; risk of mis-transfer to non-charitable e.V. too high without a clearer legal basis.[web:51]"
      citation: "[web:51]"

    - source_id: ticketing_1
      title: "Fiscal requirements – Germany"
      publisher: "pretix"
      url: "https://docs.pretix.eu/de/trust/fiscal/germany/"
      final_url_after_redirect: "https://docs.pretix.eu/de/trust/fiscal/germany/"
      reachable: true
      source_type: provider_documentation
      content_format: provider_docs
      real_guide_or_thin_page: real_guide
      authority_score_0_10: 6
      guide_quality_score_0_10: 8
      extractability_score_0_10: 8
      downloadability_score_0_10: 4
      navigation_noise_risk: low
      gemeinnuetzigkeits_transfer_risk:
        level: low
        unsafe_assumptions: []
        safe_parts: "Explains German fiscal requirements for ticketing, including TSE, receipt handling, and export options.[web:31][web:38]"
        unsafe_parts: ""
      kb_ingestion_decision: archive_html_snapshot
      reason: "Operational but detailed; excellent for implementation of ticket shop workflows and GoBD-compliant exports.[web:31][web:38]"
      citation: "[web:31][web:38]"

    - source_id: ticketing_2
      title: "Taxes – pretix documentation"
      publisher: "pretix"
      url: "https://docs.pretix.eu/de/guides/taxes/"
      final_url_after_redirect: "https://docs.pretix.eu/guides/taxes/"
      reachable: true
      source_type: provider_documentation
      content_format: provider_docs
      real_guide_or_thin_page: real_guide
      authority_score_0_10: 6
      guide_quality_score_0_10: 8
      extractability_score_0_10: 8
      downloadability_score_0_10: 4
      navigation_noise_risk: low
      gemeinnuetzigkeits_transfer_risk:
        level: low
        unsafe_assumptions: []
        safe_parts: "Shows how to configure VAT rules, tax classes, and complex tax scenarios for tickets in pretix.[web:32]"
        unsafe_parts: ""
      kb_ingestion_decision: archive_html_snapshot
      reason: "Central operational reference for 7%/19% VAT configuration and mixed products.[web:32]"
      citation: "[web:32]"

    - source_id: ticketing_3
      title: "Order lifecycle – pretix API"
      publisher: "pretix"
      url: "https://docs.pretix.eu/dev/api/guides/order_lifecycle.html"
      final_url_after_redirect: "https://docs.pretix.eu/dev/api/guides/order_lifecycle.html"
      reachable: true
      source_type: provider_documentation
      content_format: provider_docs
      real_guide_or_thin_page: real_guide
      authority_score_0_10: 6
      guide_quality_score_0_10: 7
      extractability_score_0_10: 8
      downloadability_score_0_10: 4
      navigation_noise_risk: low
      gemeinnuetzigkeits_transfer_risk:
        level: low
        unsafe_assumptions: []
        safe_parts: "Describes status changes, cancellations, refunds, and data structures, useful for mapping ticketing data to accounting.[web:31]"
        unsafe_parts: ""
      kb_ingestion_decision: archive_html_snapshot
      reason: "Important operational reference for refunds/cancellations and reconciliation data fields.[web:31]"
      citation: "[web:31]"

    - source_id: ticketing_4
      title: "Eventbrite – Event/Payout financial information"
      publisher: "Eventbrite"
      url: "https://www.eventbrite.co.uk/help/en-us/articles/263015/how-to-see-all-of-your-event-s-financial-information-with-event-invoices/"
      final_url_after_redirect: "https://www.eventbrite.de/help/de/articles/263015/so-koennen-sie-alle-finanzinformationen-zu-einem-event-in-form-einer-event-rechnung-abrufen/"
      reachable: true
      source_type: provider_documentation
      content_format: faq
      real_guide_or_thin_page: real_guide
      authority_score_0_10: 6
      guide_quality_score_0_10: 7
      extractability_score_0_10: 7
      downloadability_score_0_10: 5
      navigation_noise_risk: medium
      gemeinnuetzigkeits_transfer_risk:
        level: low
        unsafe_assumptions: []
        safe_parts: "Explains event and payout invoices, including fees, taxes, and income fields available for export.[web:20][web:24]"
        unsafe_parts: ""
      kb_ingestion_decision: archive_html_snapshot
      reason: "Operational guide for reading Eventbrite payout/event invoices, relevant if chosen as provider.[web:20][web:24]"
      citation: "[web:20][web:24]"

    - source_id: venue_1
      title: "Mietvertrag Location"
      publisher: "EVENTFAQ"
      url: "https://eventfaq.de/mietvertrag-location/"
      final_url_after_redirect: ""
      reachable: false
      source_type: law_firm_article
      content_format: thin_webpage
      real_guide_or_thin_page: mixed
      authority_score_0_10: 6
      guide_quality_score_0_10: 5
      extractability_score_0_10: 4
      downloadability_score_0_10: 1
      navigation_noise_risk: medium
      gemeinnuetzigkeits_transfer_risk:
        level: low
        unsafe_assumptions: []
        safe_parts: ""
        unsafe_parts: ""
      kb_ingestion_decision: inspiration_only
      reason: "Not reviewed; likely useful for clause ideas but not authoritative on VAT or Schadensersatz; better to rely on UStH.[web:46]"
      citation: "[web:46]"

    - source_id: venue_2
      title: "Locationvertrag"
      publisher: "Beck Law / Beck-Lexikon"
      url: "https://www.beck-law.eu/lexikon/locationvertrag/"
      final_url_after_redirect: ""
      reachable: false
      source_type: law_firm_article
      content_format: thin_webpage
      real_guide_or_thin_page: thin_page
      authority_score_0_10: 6
      guide_quality_score_0_10: 4
      extractability_score_0_10: 3
      downloadability_score_0_10: 1
      navigation_noise_risk: medium
      gemeinnuetzigkeits_transfer_risk:
        level: low
        unsafe_assumptions: []
        safe_parts: ""
        unsafe_parts: ""
      kb_ingestion_decision: discard
      reason: "Insufficient detail and not accessed; law-firm snippets better replaced by more complete event-law guides if needed.[web:58]"
      citation: "[web:58]"

    - source_id: venue_3
      title: "Musterverträge Live-Entertainment"
      publisher: "Michow & Ulbricht Rechtsanwälte"
      url: "https://michow-ulbricht.de/mustervertraege-gratis-zum-download/"
      final_url_after_redirect: ""
      reachable: false
      source_type: law_firm_article
      content_format: template
      real_guide_or_thin_page: mixed
      authority_score_0_10: 7
      guide_quality_score_0_10: 7
      extractability_score_0_10: 5
      downloadability_score_0_10: 6
      navigation_noise_risk: medium
      gemeinnuetzigkeits_transfer_risk:
        level: low
        unsafe_assumptions: []
        safe_parts: ""
        unsafe_parts: ""
      kb_ingestion_decision: adapt_template
      reason: "Likely provides contract templates for live entertainment; needs manual legal review before KB ingestion.[web:58]"
      citation: "[web:58]"

  gap_results:
    ticket_as_invoice:
      status: partly_closed
      conclusion: >
        §33 UStDV defines the minimum content of Kleinbetragsrechnungen up to 250 EUR,
        and IHK guides confirm that entrance tickets can function as invoices if they
        contain the leistender Unternehmer, Ausstellungsdatum, Art/Umfang der Leistung,
        Gesamtentgelt, Steuerbetrag, and applicable VAT rate or exemption; however,
        practice and provider implementation (especially for online tickets) require
        a tax advisor to confirm details such as name/address requirements and whether
        the ticket is clearly issued in the name of Safer Space e.V.[web:3][web:1][web:10]
      best_sources:
        - title: "§33 UStDV – Rechnungen über Kleinbeträge"
          publisher: "Gesetze im Internet"
          url: "https://www.gesetze-im-internet.de/ustdv_1980/__33.html"
          source_type: official_law
          source_quality_score_0_10: 10
          exact_relevance: "Direct legal rule on Kleinbetragsrechnung content, applicable to tickets under 250 EUR.[web:3]"
          real_guide_or_thin_page: real_guide
          quote_or_rule_summary: >
            Kleinbetragsrechnungen bis 250 EUR müssen Namen/Anschrift des leistenden
            Unternehmers, Ausstellungsdatum, Art der Leistung, Gesamtentgelt inkl.
            Steuerbetrag und Steuersatz oder Hinweis auf Steuerbefreiung enthalten.[web:3]
        - title: "Pflichtangaben in Rechnungen"
          publisher: "IHK Berlin"
          url: "https://www.ihk.de/berlin/service-und-beratung/recht-und-steuern/steuern-und-finanzen/pflichtangaben-in-rechnungen-4400732"
          source_type: ihk_hwk
          source_quality_score_0_10: 8
          exact_relevance: "Explains Pflichtangaben for standard invoices and Kleinbetragsrechnungen, including examples.[web:1]"
          real_guide_or_thin_page: real_guide
          quote_or_rule_summary: >
            Die IHK erläutert, dass Kleinbetragsrechnungen bis 250 EUR weniger Angaben
            benötigen als normale Rechnungen, während Normrechnungen zusätzliche
            Angaben wie Leistungszeitpunkt und Steuernummer/USt-IdNr. enthalten.[web:1]
        - title: "Checkliste Kleinbetragsrechnungen"
          publisher: "IHK Niederbayern"
          url: "https://www.ihk-niederbayern.de/pdfs/checkliste-kleinbetragsrechnungen-data.pdf"
          source_type: ihk_hwk
          source_quality_score_0_10: 8
          exact_relevance: "Checklist directly operationalizable to test ticket content against Kleinbetragsrechnung rules.[web:10]"
          real_guide_or_thin_page: real_guide
          quote_or_rule_summary: >
            Die Checkliste listet die Muss-Felder einer Kleinbetragsrechnung
            systematisch auf und kann für physische/e-Tickets als Prüfraster dienen.[web:10]
      remaining_uncertainty: >
        Unclear whether online tickets generated through providers always
        qualify as invoices in the name of Safer Space e.V., how buyer
        identification is handled (especially for B2C), and how corrections
        and refunds are documented; this depends strongly on provider
        configuration and must be clarified contractually and with the
        tax advisor.[web:31][web:32]
      advisor_questions:
        - "Kann die Eintrittskarte bei Nutzung eines Ticketing-Providers ohne zusätzliche Rechnung als Kleinbetragsrechnung anerkannt werden, und welche Pflichtangaben müssen exakt auf dem Ticket erscheinen?"
        - "Ist bei Online-Buchungen für B2C-Gäste die Angabe des Kundennamens/Anschrift auf der Kleinbetragsrechnung erforderlich oder nicht, und wie wirkt sich das auf Safer Space e.V. aus?"
        - "Welches Storno-/Gutschriftverfahren empfiehlt der Steuerberater für fehlerhafte Tickets oder Refunds bei Istversteuerung?"

    vat_rate_7_vs_19:
      status: partly_closed
      conclusion: >
        Official rules in §12 Abs. 2 Nr. 7 UStG and the Umsatzsteuer-Anwendungserlass
        distinguish ermäßigten Umsatzsteuersatz (7%) für Eintrittsberechtigungen zu
        Konzerten und konzertähnlichen Darbietungen von ausübenden Künstlern von
        regulären 19%-Tatbeständen; BFH-Entscheidungen zu Techno-/House-Veranstaltungen
        (u.a. Berghain) bestätigen, dass DJ-Events als Konzerte gelten können, wenn aus
        Sicht eines Durchschnittsbesuchers die Musikaufführung den eigentlichen Zweck
        der Veranstaltung darstellt, doch die Abgrenzung zwischen Kulturkonzert und
        Club-/Partysetting ist faktabhängig, sodass 19% als vorsichtiger Default für
        gemischte Club/Fundraiser-Events empfohlen werden bis zur individuellen
        steuerlichen Beurteilung.[web:41][web:43][web:45][web:52][web:60]
      best_sources:
        - title: "Umsatzsteuer-Anwendungserlass (UStAE)"
          publisher: "BMF"
          url: "https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Umsatzsteuer/Umsatzsteuer-Anwendungserlass/"
          source_type: official_tax_authority
          rule_summary: >
            Der UStAE konkretisiert §12 UStG und erläutert u.a., wann Eintrittsberechtigungen
            für kulturelle Veranstaltungen dem ermäßigten Steuersatz unterliegen, einschließlich
            Kriterien für Konzertähnlichkeit.[web:35][web:52]
          source_quality_score_0_10: 9
        - title: "BFH-Urteile Techno-/House-Veranstaltungen (Berghain u.a.)"
          publisher: "BFH, berichtet u.a. von SZ und Steuerblog"
          url: "https://www.bundesfinanzhof.de/de/entscheidung/entscheidungen-online/detail/STRE202010223/"
          source_type: official_law / expert_commentary
          rule_summary: >
            Der BFH hat entschieden, dass Techno-/House-Konzerte mit DJs als Konzerte im Sinne
            des §12 Abs. 2 Nr. 7 UStG gelten können, wenn die Musikaufführung den Zweck der
            Veranstaltung prägt, womit 7% statt 19% Anwendung finden.[web:41][web:43][web:45]
          source_quality_score_0_10: 8
        - title: "Umsätze von Ticket-Eigenhändlern"
          publisher: "Haufe / Finanzverwaltung"
          url: "https://www.haufe.de/steuern/finanzverwaltung/ermaessigter-umsatzsteuersatz-umsaetze-von-ticket-eigenhaendlern-bm_164_73410.html"
          source_type: professional_guide
          rule_summary: >
            Die Finanzverwaltung erkennt den ermäßigten Steuersatz auch für Umsätze von
            Ticket-Eigenhändlern für ermäßigte Veranstaltungen; damit können auch eigenständige
            Ticketshops unter bestimmten Voraussetzungen 7% anwenden.[web:60]
          source_quality_score_0_10: 7
      remaining_uncertainty: >
        Der konkrete Charakter des Events „Equinox/Fundraiser Hamburg“ (Kulturclub mit DJs,
        Awareness, Fundraising-Elementen) ist nicht automatisch einem Konzert gleichzusetzen;
        Faktoren wie Türpolitik, Schwerpunkt auf Konsum vs. Musik, Rahmenprogramm und bisherige
        Behördenpraxis in Hamburg sind ungeklärt.[web:41][web:58]
      advisor_questions:
        - "Kann die konkrete Programmgestaltung von Safer Space e.V. (Line-up, Bühnenkonzept, Kommunikation) so gestaltet werden, dass der Event aus Sicht der Finanzverwaltung als Konzert/Kulturveranstaltung mit 7% gilt?"
        - "Welche Erfahrungen gibt es beim zuständigen Finanzamt Hamburg mit vergleichbaren Club-/Kulturveranstaltungen und wie sind diese steuerlich eingeordnet worden?"
        - "Ist eine Aufteilung in 7%-Eintrittskomponente und 19%-Leistungen (z.B. bestimmte Hospitality- oder Merch-Anteile) sinnvoll und rechtssicher?"

    fundraiser_donation_wording:
      status: partly_closed
      conclusion: >
        Für nicht gemeinnützige Vereine sind Zahlungen der Gäste grundsätzlich als Entgelt
        für Leistungen anzusehen, wenn sie mit einem Leistungsversprechen (Eintritt, Zugang,
        konkrete Gegenleistung) verbunden sind; BMF- und fachliche Quellen zu Sachspenden und
        unechten Spenden verdeutlichen, dass freiwillige Zusatzbeträge, die faktisch an den
        Ticketkauf gekoppelt sind, umsatzsteuerlich regelmäßig als Teil des Entgelts gelten,
        während echte Spenden ohne Gegenleistung – für Safer Space mangels Gemeinnützigkeit –
        zwar möglich sein können, aber ohne Zuwendungsbestätigung und mit besonderer Abgrenzung
        dokumentiert werden müssen.[web:37][web:42][web:58][web:51]
      best_sources:
        - title: "Fragen und Antworten zur umsatzsteuerrechtlichen Behandlung von Sachspenden"
          publisher: "BMF"
          url: "https://www.bundesfinanzministerium.de/Content/DE/FAQ/FAQ-ust-sachspenden.html"
          source_type: official_tax_authority
          rule_summary: >
            Das BMF erläutert, wann bei unentgeltlichen Zuwendungen keine Umsatzsteuer anfällt
            und wann ein Entgelt vorliegt; dies ist übertragbar auf unechte Spenden und
            Entgeltbeurteilung.[web:37][web:42]
          source_quality_score_0_10: 8
        - title: "Umsatzsteuerliche Besonderheiten und Risiken aus Eintrittskarten-Erwerb"
          publisher: "FGS / Fachkanzlei"
          url: "https://www.fgs.de/news-and-insights/blog/detail/umsatzsteuerliche-besonderheiten-und-risiken-resultierend-aus-dem-erwerb-und-de/"
          source_type: law_firm_article
          rule_summary: >
            Der Erwerb einer Eintrittskarte wird als steuerbare Dienstleistung (Zutrittsberechtigung)
            qualifiziert; das tatsächliche Entgelt bildet die Bemessungsgrundlage, was gegen
            steuerfreie „Donation Tickets“ mit Gegenleistung spricht.[web:58]
          source_quality_score_0_10: 7
        - title: "Die Gemeinnützigkeit und das Finanzamt (Merkblatt)"
          publisher: "Finanzministerium MV"
          url: "https://www.steuerportal-mv.de/static/Regierungsportal/Finanzministerium/Steuerportal/Dateien/Downloads/Merkblatt_Vereine_%20Die_Gemeinnuetzigkeit_und_das_Finanzamt.pdf"
          source_type: official_tax_authority
          rule_summary: >
            Das Merkblatt stellt klar, dass Spendenbestätigungen und steuerbegünstigte
            Behandlung von Zuwendungen an Gemeinnützigkeit geknüpft sind; ein nicht
            gemeinnütziger Verein kann keine Spendenbescheinigung ausstellen.[web:51]
          source_quality_score_0_10: 8
      safe_wording: >
        Begriffe wie „Ticketpreis“, „Eintritt“, „Unterstützung durch Ticketkauf“ und
        getrennte „freiwillige Unterstützung ohne Gegenleistung“ sind sicherer als der
        Begriff „Spende“, der auf Gemeinnützigkeit und Zuwendungsbestätigungen schließen
        lässt.[web:58][web:51]
      risky_wording: >
        „Spendenticket“, „Spende mit Eintritt“, „Donation Ticket inkl. Zugang“ oder
        „Pay-what-you-want Eintrittsspende“ sind riskant, da sie faktisch Entgelt für
        Eintritt verschleiern und zu falschen Spendenannahmen führen können.[web:58][web:51]
      advisor_questions:
        - "Wie kann Safer Space e.V. freiwillige Zusatzbeträge von Gästen rechtssicher als Entgelt bzw. als echte Spende ohne Gegenleistung abgrenzen und buchen?"
        - "Welche Formulierungen in Ticketshop und Kommunikation sollte der Verein im Hinblick auf Umsatzsteuer und fehlende Spendenbescheinigungen strikt vermeiden?"

    venue_settlement_minimum_bar:
      status: not_closed
      conclusion: >
        UStH 1.3 unterscheidet echten Schadensersatz (kein Leistungsaustausch, keine
        Umsatzsteuer) von unechtem Schadensersatz (zusätzliches Entgelt für eine Leistung);
        ob eine Mindestbarumsatzgarantie bzw. Ausgleichszahlung des Veranstalters gegenüber
        dem Club echte Schadensersatzleistung oder Teil des Entgelts für die Raumüberlassung
        bzw. sonstige Leistungen ist, hängt stark von Vertragsformulierung und tatsächlicher
        Gestaltung ab, und es liegen keine spezifischen, hochqualitativen Event-Vertrags-
        Quellen vor, sodass diese Lücke nur mit individueller Vertragsprüfung durch einen
        Steuerberater geschlossen werden kann.[web:46]
      possible_models:
        - model: "Venue sells drinks and keeps bar revenue"
          accounting_for_safer_space: >
            Safer Space vereinnahmt primär Eintrittsgelder; Barumsatz bleibt beim Venue und
            erscheint höchstens als Informationsgröße im Vertrag.[web:58]
          possible_vat_treatment: >
            Eintritt als Safer-Space-Leistung mit 7% oder 19%; Barumsatz als Leistung des
            Venue an Gäste mit eigenem USt-Ausweis.[web:52]
          documents_needed: >
            Miet-/Nutzungsvertrag, Leistungsbeschreibung, ggf. Abrechnung zu Raum/Technik.[web:58]
          contract_clauses_needed: >
            Klare Abgrenzung der Verantwortlichkeiten und Ausschluss der Barumsatzbeteiligung.[web:58]
          risks: >
            Unklare Darstellung von Nebenleistungen (Security, Technik) kann zu
            falschen Steuersätzen führen.[web:52]
          confidence_0_10: 5
        - model: "Safer Space guarantees minimum bar revenue and pays difference"
          accounting_for_safer_space: >
            Mögliche Aufwandbuchung (Schadensersatz oder Entgelt) an Venue; Abgrenzung unklar.[web:46]
          possible_vat_treatment: >
            Je nach Ausgestaltung entweder echter Schadensersatz (keine USt) oder zusätzliche
            Gegenleistung für Vermietung/Leistungen (USt-pflichtig).[web:46]
          documents_needed: >
            Vertragsklausel zur Mindestumsatzgarantie, Abrechnung mit Berechnungslogik.[web:46]
          contract_clauses_needed: >
            Klarer Wortlaut, ob Zahlung als Schadensersatz für Nichterreichen eines
            Mindestumsatzes oder als Entgelt für Leistung erfolgt.[web:46]
          risks: >
            Falsche Einordnung kann zu nicht abgeführter Umsatzsteuer oder unnötiger
            Mehrbelastung führen.[web:46]
          confidence_0_10: 3
      best_sources:
        - title: "UStH 1.3 – Schadensersatz"
          publisher: "BMF"
          url: "https://usth.bundesfinanzministerium.de/usth/2023/A-Umsatzsteuergesetz/I-Steuergegenstand-und-Geltungsbereich/Paragraf-1/ae-1-3.0.0-20230615/"
          source_type: official_tax_authority
          exact_relevance: "Unterscheidung echter vs. unechter Schadensersatz als Grundlage für Mindestumsatzgarantie-Beurteilung.[web:46]"
          source_quality_score_0_10: 9
          real_guide_or_thin_page: real_guide
      remaining_uncertainty: >
        Es fehlen konkrete Beispiele aus der Club-/Eventpraxis zur Behandlung von
        Mindestbarumsätzen; weder EventFAQ noch andere Quellen liegen in dieser
        Recherche in belastbarer Tiefe vor.[web:46]
      venue_questions:
        - "Wer ist rechtlich Verkäufer der Getränke (Venue oder Safer Space e.V.)?"
        - "Wer vereinnahmt den Barumsatz tatsächlich und stellt Quittungen/Rechnungen aus?"
        - "Wie genau ist die 7.500-EUR-Mindestgarantie definiert – als Umsatzgarantie oder als vertraglicher Schadenersatz?"
        - "Welche Leistungen (Raum, Technik, Security, Reinigung) werden dem Verein separat in Rechnung gestellt und mit welchem USt-Satz?"
        - "Wie sieht das finale Abrechnungsdokument aus (Protokoll, Rechnung, Gutschrift)?"
      advisor_questions:
        - "Wie ist die konkret zu vereinbarende Mindestbarumsatzklausel umsatzsteuerlich zu gestalten, um echte Schadensersatzleistungen von Entgelt sauber abzugrenzen?"
        - "Welche Form der Vertragsdokumentation empfiehlt der Steuerberater, um spätere Betriebsprüfungen zur Umsatzsteuer auf Ausgleichszahlungen zu bestehen?"

    cash_basis_ticketing_refunds:
      status: partly_closed
      conclusion: >
        Unter Istversteuerung entsteht die Umsatzsteuer grundsätzlich mit Vereinnahmung des
        Entgelts (Zufluss), sodass bei Vorkasse für Eintrittskarten die USt mit Zahlungseingang
        fällig wird und bei Storno/Refunds durch Korrekturbelege (Gutschrift/Stornorechnung)
        rückgängig gemacht werden muss; vorhandene Quellen aus BFH/Eigenhändler- und
        Einlasskartenkontext sowie provider documentation geben Hinweise auf Vorverkaufsgebühren
        und Stornoabläufe, jedoch fehlt ein direkt auf Vereins-/Eventticketing bezogener
        offizieller Leitfaden, weshalb die genaue Umsetzung (z.B. zeitliche Zuordnung,
        eventbezogene Periodisierung) mit dem Steuerberater abgestimmt werden sollte.[web:47][web:53][web:31]
      best_sources:
        - title: "BFH-Urteil V R 16/09 – Vorverkaufsgebühr"
          publisher: "Bundesfinanzhof"
          url: "https://www.bundesfinanzhof.de/de/entscheidung/entscheidungen-online/detail/STRE201210056/"
          source_type: official_law
          quote_or_rule_summary: >
            BFH entscheidet, dass Vorverkaufsgebühren Bestandteil des Entgelts für die
            Eintrittskarte sind und dem gleichen Steuersatz unterliegen; das ist relevant
            für die Behandlung von Ticketgebühren im Vorverkauf.[web:53][web:47]
          source_quality_score_0_10: 8
        - title: "Umsätze von Ticket-Eigenhändlern (ermäßigter Steuersatz)"
          publisher: "Haufe / Finanzverwaltung"
          url: "https://www.haufe.de/steuern/finanzverwaltung/ermaessigter-umsatzsteuersatz-umsaetze-von-ticket-eigenhaendlern-bm_164_73410.html"
          source_type: professional_guide
          quote_or_rule_summary: >
            Bestätigt, dass Einnahmen von Ticket-Eigenhändlern aus Eintrittsberechtigungen
            dem entsprechenden USt-Satz der Veranstaltung unterliegen und damit bei
            Istversteuerung mit Zufluss steuerlich relevant werden.[web:60]
          source_quality_score_0_10: 7
        - title: "Fiscal requirements – Germany (pretix)"
          publisher: "pretix"
          url: "https://docs.pretix.eu/de/trust/fiscal/germany/"
          source_type: provider_documentation
          quote_or_rule_summary: >
            Beschreibt, wie pretix Zahlungen, Belege, Stornierungen und Exportformate
            im Einklang mit deutschen fiskalischen Anforderungen abbildet.[web:31][web:38]
          source_quality_score_0_10: 8
      required_export_fields:
        - order_id
        - invoice_number
        - payment_date
        - event_date
        - gross_amount
        - net_amount
        - VAT_rate
        - VAT_amount
        - refund_date
        - refund_amount
        - cancellation_invoice_id
        - payout_id
      advisor_questions:
        - "Wie sollen Ticketzahlungen, die vor dem Event vereinnahmt werden, bei Istversteuerung zeitlich zugeordnet werden (Monat/Quartal)?"
        - "Welche Anforderungen stellt das Finanzamt Hamburg an Gutschriften/Stornorechnungen bei Ticketrefounds und Eventausfällen?"

    ticketing_provider_role:
      providers:
        - provider: pretix
          role:
            value: "agent_for_organizer"
            evidence: >
              pretix-Dokumentation beschreibt den Veranstalter als leistenden Unternehmer,
              für den pretix Tickets technisch verkauft und Belege erzeugt.[web:31][web:32]
          who_is_supplier_to_customer: "Safer Space e.V. (Veranstalter) wird typischerweise als Leistungserbringer ausgewiesen.[web:31]"
          who_issues_invoice_or_receipt: "pretix generiert Belege/Rechnungen im Namen des Veranstalters, sofern konfiguriert.[web:31][web:19]"
          who_collects_money: "pretix/Payment-Provider (z.B. Stripe) vereinnahmen Zahlungen technisch, Auszahlung an Veranstalter.[web:31]"
          who_charges_service_fee: "pretix berechnet dem Veranstalter Ticketing-Gebühren, die gesondert abzurechnen sind.[web:31][web:19]"
          payout_report_available: "Ja, via Export/DATEV-Rechnungsdatenservice.[web:19]"
          refunds_supported: "Ja, über Order-Lifecycle-Mechanismen.[web:31]"
          invoice_numbering_supported: "Ja, pretix kann Rechnungsnummern und Steuerschlüssel verwalten.[web:19][web:31]"
          export_formats: "CSV/Excel, DATEV-Rechnungsdatenservice, API-Exports.[web:19][web:31]"
          gobd_export_quality: "hoch (DATEV-Integration, strukturierte Datenfelder)."
          source_urls:
            - "https://docs.pretix.eu/de/trust/fiscal/germany/"
            - "https://docs.pretix.eu/guides/taxes/"
            - "https://pretix.eu/about/de/blog/20230327-datev-rechnungsdatenservice/"
          source_quality_score_0_10: 8
          recommendation_for_safer_space: >
            Sehr geeignet als Ticketshop, da Rolle als Agent des Veranstalters, gute DATEV-Exportmöglichkeiten und klare Steuerkonfigurationsoptionen vorhanden sind.[web:19][web:31][web:32]
        - provider: Eventbrite
          role:
            value: "merchant_of_record"
            evidence: >
              Eventbrite bietet Event- und Auszahlungsrechnungen und agiert oft als Payment
              Processor/Merchant of Record, der Gebühren und Steuern im eigenen System
              abbildet.[web:20][web:24]
          who_is_supplier_to_customer: "Je nach Setup kann Eventbrite oder der Veranstalter gegenüber dem Kunden ausgewiesen werden; Hilfeartikel sind nicht eindeutig.[web:20][web:24]"
          who_issues_invoice_or_receipt: "Eventbrite generiert Event-/Payout-Invoices mit Gebühren- und Steuerübersichten.[web:20][web:24]"
          who_collects_money: "Eventbrite sammelt Gelder und zahlt sie gesammelt aus.[web:20][web:24]"
          who_charges_service_fee: "Eventbrite berechnet Servicegebühren und Payment Fees.[web:20][web:24]"
          payout_report_available: "Ja, Event-/Payout-Rechnungen für Export.[web:20][web:24]"
          refunds_supported: "Ja, jedoch mit eigenen Regeln/Timings.[web:20]"
          invoice_numbering_supported: "Nur eingeschränkt belegbar aus Hilfeartikeln."
          export_formats: "PDF/CSV-Auszüge, Event-/Payout-Invoices.[web:20][web:24]"
          gobd_export_quality: "mittel – brauchbar, aber nicht explizit auf GoBD ausgerichtet."
          source_urls:
            - "https://www.eventbrite.de/help/de/articles/263015/"
          source_quality_score_0_10: 7
          recommendation_for_safer_space: >
            Einsetzbar, aber Rollen- und Steuerfragen (wer ist Leistungserbringer?) sollten vor Einsatz vertraglich geklärt und mit Steuerberater gecheckt werden.[web:20][web:24]
        - provider: ticket.io
          role:
            value: "technical_service_provider"
            evidence: >
              Öffentlich zugängliche FAQ fokussieren auf technische und abrechnungsbezogene
              Fragen; detaillierte Export-/DATEV-Dokumentation wurde in dieser Recherche nicht gefunden.[web:33]
          who_is_supplier_to_customer: "Unklar; T&Cs/Vertrag müssen geprüft werden."
          who_issues_invoice_or_receipt: "Ticket.io generiert Tickets/Bestätigungen; ob diese als Rechnungen gelten, ist unklar.[web:33]"
          who_collects_money: "ticket.io bzw. angebundene Zahlungsdienstleister.[web:33]"
          who_charges_service_fee: "ticket.io erhebt Gebühren gegenüber Veranstaltern.[web:33]"
          payout_report_available: "Ja, aber Details fehlen in dieser Recherche.[web:33]"
          refunds_supported: "Grundsätzlich ja; Details nicht ausreichend dokumentiert.[web:33]"
          invoice_numbering_supported: "Nicht klar dokumentiert."
          export_formats: "Bisher nur allgemein erwähnt; keine tiefe Dokumentation gefunden.[web:33]"
          gobd_export_quality: "unbekannt."
          source_urls:
            - "https://www.ticket.io/ticketing-software/faq-veranstalter/"
          source_quality_score_0_10: 5
          recommendation_for_safer_space: >
            Nur nach zusätzlicher Prüfung der Exporte und Rollenklärung empfehlenswert; aktuell gegenüber pretix/DATEV deutlich weniger klar.[web:33]
      best_fit_for_safer_space: "pretix – klarer Agentenstatus für Veranstalter, gute Steuerkonfiguration und DATEV-Integration.[web:19][web:31][web:32]"
      provider_risks: >
        Providerdokumentation ist rein operativ und kein rechtlicher Ersatz für UStG/UStAE;
        Rollen als Merchant of Record/Agent müssen vertraglich und steuerlich geprüft werden.[web:31][web:20][web:33]
      documents_to_archive: >
        T&C/Vertrag mit Ticketing-Provider, Steuer-/Invoicespezifikationen, Exportformat-
        Beschreibungen und GoBD-/DATEV-Integrationsbeschreibungen sollten als KB-Dokumente
        gesichert werden.[web:19][web:31][web:20]

    reconciliation:
      status: partly_closed
      conclusion: >
        Für eine saubere EÜR-Reconciliation von Ticketing, Stripe/PayPal-Zahlungen und
        Payouts existieren gute providerseitige DATEV-/Exportlösungen (insbesondere bei
        pretix), doch offizielle, vereinsbezogene Leitfäden zur Verbuchung von Sammel-
        auszahlungen, Gebühren und Vorsteuerabzug sind begrenzt; allgemein verfügbare
        Buchhaltungsguides und Payment-Provider-Informationen liefern Felder und Abläufe,
        aber das konkrete Konten- und Buchungsschema sollte mit einem Steuerberater
        abgestimmt werden.[web:19][web:31][web:34]
      best_sources:
        - title: "pretix–Integration zum DATEV Rechnungsdatenservice"
          publisher: "pretix"
          url: "https://pretix.eu/about/de/blog/20230327-datev-rechnungsdatenservice/"
          source_type: provider_documentation
          guide_quality_score_0_10: 8
          extractability_score_0_10: 8
        - title: "Fiscal requirements – Germany (pretix)"
          publisher: "pretix"
          url: "https://docs.pretix.eu/de/trust/fiscal/germany/"
          source_type: provider_documentation
          guide_quality_score_0_10: 8
          extractability_score_0_10: 8
        - title: "PayPal Business Pricing/Fees"
          publisher: "PayPal"
          url: "https://www.paypal.com/de/business/fees"
          source_type: provider_documentation
          guide_quality_score_0_10: 5
          extractability_score_0_10: 5
      minimum_export_standard: >
        Ticketing-Export sollte mindestens Order-ID, Ticket-ID, Rechnungsnummer,
        Käufertyp (B2C/B2B), Bruttoticketpreis, Nettopreis, USt-Satz, USt-Betrag,
        Providergebühr, Payment Fee, Refundbetrag, Payout-ID, Payout-Datum,
        Bankbetrag und Currency enthalten, um GoBD-konforme Reconciliation zu
        ermöglichen.[web:19][web:31][web:20]
      advisor_questions:
        - "Wie sollen Stripe-/PayPal-Sammelauszahlungen mit gemischten Ticketumsätzen und Gebühren in der EÜR und Umsatzsteuer-Voranmeldung abgebildet werden?"
        - "Welche Kontenstruktur und Buchungslogik empfiehlt der Steuerberater für Ticketumsätze, Ticket-Gebühren und Payment-Fees im wirtschaftlichen Geschäftsbetrieb des Vereins?"

    non_charitable_ev_tax:
      status: partly_closed
      conclusion: >
        Offizielle Merkblätter und Broschüren zu Vereinen (NRW, Brandenburg, MV) betonen,
        dass Vereine ohne Gemeinnützigkeit grundsätzlich körperschaft- und gewerbesteuer-
        pflichtig sind, wenn sie wirtschaftliche Geschäftsbetriebe (z.B. regelmäßige
        Eintrittsveranstaltungen) unterhalten; gleichzeitig sind viele dieser Quellen
        konzeptionell auf Gemeinnützigkeit ausgerichtet und müssen für Safer Space e.V.
        mit Nicht-Gemeinnützigkeitsstatus vorsichtig interpretiert werden.[web:8][web:51][web:54]
      best_sources:
        - title: "Mein ELSTER für Vereine (NRW)"
          publisher: "Finanzverwaltung NRW"
          url: "https://www.finanzverwaltung.nrw.de/system/files/media/document/file/2026_05_26_internet_endf_einzs_brosch_meinelstervereine.pdf"
          source_type: official_tax_authority
          source_quality_score_0_10: 8
        - title: "Vereine und Steuern (Brandenburg)"
          publisher: "Finanzamt Brandenburg"
          url: "https://finanzamt.brandenburg.de/sixcms/media.php/9/Vereine-und-Steuern-2023_web.pdf"
          source_type: official_tax_authority
          source_quality_score_0_10: 8
        - title: "Die Gemeinnützigkeit und das Finanzamt (MV)"
          publisher: "Finanzministerium MV"
          url: "https://www.steuerportal-mv.de/static/Regierungsportal/Finanzministerium/Steuerportal/Dateien/Downloads/Merkblatt_Vereine_%20Die_Gemeinnuetzigkeit_und_das_Finanzamt.pdf"
          source_type: official_tax_authority
          source_quality_score_0_10: 8
      gemeinnuetzigkeits_contamination: >
        Alle genannten Verein-Merkblätter enthalten umfangreiche Passagen zu Vorteilen,
        Steuerbefreiungen und Sonderregelungen für gemeinnützige Vereine; für Safer
        Space e.V. sind nur Abschnitte zur allgemeinen Steuerpflicht und zur Existenz
        wirtschaftlicher Geschäftsbetriebe übertragbar, nicht die Vergünstigungen.[web:51][web:54]
      advisor_questions:
        - "Welche Steuererklärungen (KSt 1, GewSt, USt) sind für Safer Space e.V. mit wirtschaftlichem Geschäftsbetrieb im konkreten Fall jährlich abzugeben?"
        - "Wie sind Überschüsse aus Eventbetrieb im nicht gemeinnützigen Verein körperschaft- und gewerbesteuerlich zu behandeln und eventuell getrennt auszuweisen?"

    contractor_matrix:
      matrix:
        - type: "inländische:r DJ"
          invoice_required: "ja, Honorarrechnung mit USt oder Kleinunternehmerangabe.[web:9][web:52]"
          contract_required: "empfohlen (Auftrittsvertrag)."
          vat_check: "Prüfung 7% vs. 19% auf Eintritt; DJ-Leistung selbst typischerweise B2B-Leistung mit 19% bzw. Kleinunternehmerregelung.[web:41][web:52]"
          ksk_check: "Abgabepflicht nach KSK-Infoschrift Nr. 4 prüfen.[web:9]"
          reverse_charge_check: "nein (Inland)."
          section_50a_check: "nein."
          employment_status_check: "Scheinselbstständigkeit prüfen (abhängig von Einbindung).[web:17][web:22]"
          expense_reimbursement_possible: "ja, gegen Nachweise."
          cash_payment_risk: "hoch bei größeren Beträgen (Dokumentation, Geldwäsche)."
          required_documents: "Vertrag, Rechnung, ggf. KSK-Meldung, Auslagenbelege.[web:9]"
          best_sources:
            - "KSK Info 4 – Abgabepflicht von Veranstaltern.[web:9]"
            - "DRV Scheinselbstständigkeit.[web:17][web:22]"
          uncertainty: "mittel (Abgrenzung dauerhaft tätiger DJs vs. einzelne Auftritte)."
        - type: "ausländische:r DJ"
          invoice_required: "ja, ggf. ohne deutsche USt, aber mit Hinweis auf §3a/Leistungsort.[web:52]"
          contract_required: "ja (grenzüberschreitend)."
          vat_check: "Leistungsort-/Reverse-Charge-Fragen prüfen; Eintrittsumsatz bleibt in DE steuerbar.[web:52][web:58]"
          ksk_check: "KSK-Pflicht kann auch bei ausländischen Künstlern bestehen.[web:9]"
          reverse_charge_check: "ja, für bestimmte B2B-Leistungen.[web:52]"
          section_50a_check: "ja, Quellensteuerpflicht auf Künstlerhonorare prüfen.[web:46]"
          employment_status_check: "Scheinselbstständigkeit eher geringe Relevanz, aber Vertragsstatus klären."
          expense_reimbursement_possible: "ja, mit Nachweisen."
          cash_payment_risk: "sehr hoch."
          required_documents: "Vertrag, Steuer-Residency-Daten, §50a-Einschätzung/ggf. Freistellungsbescheide.[web:46]"
          best_sources:
            - "BZSt §50a EStG.[web:46]"
            - "UStAE/UStG Leistungsort-Regeln.[web:52]"
          uncertainty: "hoch (Quellensteuer/Reverse-Charge-Details)."
        - type: "Awareness-Crew / paid helper"
          invoice_required: "ja, sofern selbstständig; sonst Arbeitsvertrag.[web:17]"
          contract_required: "mindestens Einsatzvereinbarung."
          vat_check: "Bei echter Selbstständigkeit ggf. USt; bei kurzfristiger Beschäftigung Lohnsteuer/SV.[web:16][web:28]"
          ksk_check: "nur wenn künstlerische/publizistische Tätigkeiten vorliegen."
          reverse_charge_check: "nein."
          section_50a_check: "nein."
          employment_status_check: "kritisch – hohe Scheinselbstständigkeitsgefahr bei regelmäßigem Einsatz.[web:17][web:22]"
          expense_reimbursement_possible: "ja."
          cash_payment_risk: "mittel."
          required_documents: "Verträge, Einsatzpläne, ggf. Minijob-Anmeldung.[web:16][web:28]"
          best_sources:
            - "Minijob-Zentrale Kurzfristige Beschäftigung.[web:16][web:28]"
            - "DRV Scheinselbstständigkeit.[web:17][web:22]"
          uncertainty: "mittel."
        - type: "volunteer helper"
          invoice_required: "nein (keine Vergütung)."
          contract_required: "Ehrenamtliche Vereinbarung empfohlen."
          vat_check: "nein, da keine Entgeltleistung.[web:58]"
          ksk_check: "nein."
          reverse_charge_check: "nein."
          section_50a_check: "nein."
          employment_status_check: "gering, solange keine Gegenleistung."
          expense_reimbursement_possible: "ja, Auslagenersatz gegen Belege; Steuerfreiheit hängt von Ausgestaltung ab.[web:18][web:23]"
          cash_payment_risk: "niedrig."
          required_documents: "Ehrenamtsvereinbarung, Auslagenbelege."
          best_sources:
            - "Auslagenersatz im Verein.[web:18][web:23]"
          uncertainty: "mittel (Abgrenzung zu pauschalen Aufwandsentschädigungen)."
      key_rules: >
        Der Veranstalter muss KSK-Pflicht systematisch prüfen, Scheinselbstständigkeit
        vermeiden, ausländische Künstler nach §50a EStG und Reverse-Charge-Regeln
        behandeln und Crew-Mitglieder korrekt als Beschäftigte oder echte Ehrenamtliche
        klassifizieren.[web:9][web:16][web:17][web:46]
      best_sources:
        - "KSK Info 4.[web:9]"
        - "Minijob-Zentrale Kurzfristige Beschäftigung.[web:16][web:28]"
        - "DRV Scheinselbstständigkeit.[web:17][web:22]"
        - "BZSt §50a EStG.[web:46]"
      advisor_questions:
        - "Welche Honorar- und Beschäftigungsformen empfiehlt der Steuerberater für DJs, Awareness-Team und Crew, um KSK- und Scheinselbstständigkeitsrisiken zu minimieren?"
        - "Wie sind ausländische Künstlerhonorare im Einzelfall steuerlich zu behandeln (Quellensteuer, Doppelbesteuerungsabkommen)?"

    templates:
      usable_templates:
        - template_name: "Checkliste Kleinbetragsrechnung"
          source: "IHK Niederbayern"
          url: "https://www.ihk-niederbayern.de/pdfs/checkliste-kleinbetragsrechnungen-data.pdf"
          source_type: ihk_hwk
          downloadable: true
          editable: false
          authority_score_0_10: 7
          adaptation_needed: "Ggf. Ergänzung um spezifische Ticketfelder."
          use_as:
            value: "adapt_template"
            reason: "Sehr gute Grundlage für Ticketpflichtangaben, aber grafische Ticketlayouts müssen angepasst werden.[web:10]"
        - template_name: "Muster-Verfahrensdokumentation Belegablage"
          source: "AWV"
          url: "https://www.awv-net.de/publikationen-produkte/publikationen/detailseite/musterverfahrensdokumentation-zur-belegablage"
          source_type: awv
          downloadable: true
          editable: true
          authority_score_0_10: 8
          adaptation_needed: "Anpassung an Eventprozesse/Ticketing."
          use_as:
            value: "adapt_template"
            reason: "Strukturell sehr geeignet für eventbezogene GoBD-Verfahrensdoku.[web:7][web:12]"
        - template_name: "Kurzfristige Beschäftigung Checkliste"
          source: "Minijob-Zentrale"
          url: "https://www.minijob-zentrale.de/DE/die-minijobs/kurzfristige-beschaeftigung/Checkliste/"
          source_type: minijob-zentrale
          downloadable: true
          editable: false
          authority_score_0_10: 9
          adaptation_needed: "Übertragung auf Event-Crew-Begriffe."
          use_as:
            value: "direct_template"
            reason: "Direkt nutzbare Checkliste für kurzfristige Beschäftigung.[web:21][web:28]"
      inspiration_only:
        - template_name: "Musterverträge Live-Entertainment"
          source: "Michow & Ulbricht"
          url: "https://michow-ulbricht.de/mustervertraege-gratis-zum-download/"
          source_type: law_firm_article
          downloadable: true
          editable: true
          authority_score_0_10: 7
          adaptation_needed: "Rechtliche Prüfung und Anpassung an Vereinssituation."
          use_as:
            value: "inspiration_only"
            reason: "Gute Vertragsideen, aber individuelle Rechtsberatung nötig.[web:58]"
      discard:
        - template_name: "Allgemeine Ehrenamt-/Aufwandsentschädigungsübersichten"
          source: "Diverse NGO-Webseiten"
          url: "https://www.buergergesellschaft.de/..."
          source_type: professional_guide
          downloadable: false
          editable: false
          authority_score_0_10: 5
          adaptation_needed: "Nicht sinnvoll wegen Gemeinnützigkeitsfokus."
          use_as:
            value: "discard"
            reason: "Zu stark auf gemeinnützige Vereine und Ehrenamtspauschalen fokussiert.[web:51]"

  updated_download_manifest:
    P0_archive_immediately:
      - title: "§33 UStDV – Rechnungen über Kleinbeträge"
        publisher: "Gesetze im Internet"
        url: "https://www.gesetze-im-internet.de/ustdv_1980/__33.html"
        preferred_format: "HTML + local text extraction"
        capture_method: "archive_html_snapshot"
        reason: "Primäre Rechtsgrundlage für Ticket/Kleinbetragsrechnung-Logik.[web:3]"
      - title: "Pflichtangaben in Rechnungen"
        publisher: "IHK Berlin"
        url: "https://www.ihk.de/berlin/service-und-beratung/recht-und-steuern/steuern-und-finanzen/pflichtangaben-in-rechnungen-4400732"
        preferred_format: "HTML snapshot"
        capture_method: "archive_html_snapshot"
        reason: "Praxisnaher Überblick zu Rechnungsanforderungen.[web:1]"
      - title: "Checkliste Kleinbetragsrechnungen"
        publisher: "IHK Niederbayern"
        url: "https://www.ihk-niederbayern.de/pdfs/checkliste-kleinbetragsrechnungen-data.pdf"
        preferred_format: "PDF"
        capture_method: "archive_pdf"
        reason: "Operationalisierbare Checkliste für Tickets als Kleinbetragsrechnung.[web:10]"
      - title: "GoBD BMF-Schreiben (2024)"
        publisher: "BMF"
        url: "https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Weitere_Steuerthemen/Abgabenordnung/AO-Anwendungserlass/2024-03-11-aenderung-gobd.pdf"
        preferred_format: "PDF"
        capture_method: "archive_pdf"
        reason: "Grundlage für GoBD-konforme Event-/Belegarchivierung.[web:6][web:15]"
      - title: "Muster-Verfahrensdokumentation zur Belegablage"
        publisher: "AWV"
        url: "https://www.awv-net.de/publikationen-produkte/publikationen/detailseite/musterverfahrensdokumentation-zur-belegablage"
        preferred_format: "PDF + DOCX"
        capture_method: "archive_pdf"
        reason: "Template für Verfahrensdokumentation.[web:7][web:12]"
      - title: "Informationsschrift Nr. 4 – Abgabepflicht von Veranstaltern"
        publisher: "KSK"
        url: "https://www.kuenstlersozialkasse.de/fileadmin/Dokumente/Mediencenter_Unternehmer_Verwerter/Informationsschriften/Info_04_Abgabepflicht_von_Veranstaltern.pdf"
        preferred_format: "PDF"
        capture_method: "archive_pdf"
        reason: "Zentrale KSK-Grundlage.[web:9]"
      - title: "Kurzfristige Beschäftigung (Infos + Checkliste)"
        publisher: "Minijob-Zentrale"
        url: "https://www.minijob-zentrale.de/DE/die-minijobs/kurzfristige-beschaeftigung"
        preferred_format: "HTML snapshot"
        capture_method: "archive_html_snapshot"
        reason: "Grundlage für Kurzfristjobs/Crew.[web:16][web:21][web:28]"
      - title: "Scheinselbstständigkeit erkennen"
        publisher: "Deutsche Rentenversicherung"
        url: "https://www.deutsche-rentenversicherung.de/DRV/DE/Rente/Arbeitnehmer-und-Selbststaendige/03_Selbststaendige/scheinselbststaendigkeit"
        preferred_format: "HTML snapshot"
        capture_method: "archive_html_snapshot"
        reason: "Abgrenzungsregeln für Selbstständige vs. Beschäftigte.[web:17][web:22]"
      - title: "BZSt-Informationen zu §50a EStG"
        publisher: "BZSt"
        url: "https://www.bzst.de/DE/Privatpersonen/Abzugsteuern_50a/abzugsteuern_node.html"
        preferred_format: "HTML snapshot"
        capture_method: "archive_html_snapshot"
        reason: "Quellensteuer für ausländische Künstler.[web:46]"
      - title: "pretix – Fiscal requirements Germany"
        publisher: "pretix"
        url: "https://docs.pretix.eu/de/trust/fiscal/germany/"
        preferred_format: "HTML snapshot"
        capture_method: "archive_html_snapshot"
        reason: "Technische Umsetzung steuerlicher Vorgaben im Ticketing.[web:31][web:38]"
      - title: "pretix – Taxes guide"
        publisher: "pretix"
        url: "https://docs.pretix.eu/guides/taxes/"
        preferred_format: "HTML snapshot"
        capture_method: "archive_html_snapshot"
        reason: "Konfiguration 7%/19% und komplexe Steuerregeln im Ticketshop.[web:32]"
      - title: "pretix – DATEV Rechnungsdatenservice Integration"
        publisher: "pretix"
        url: "https://pretix.eu/about/de/blog/20230327-datev-rechnungsdatenservice/"
        preferred_format: "HTML snapshot"
        capture_method: "archive_html_snapshot"
        reason: "Schlüsselquelle für automatisierte DATEV-Schnittstelle.[web:19]"
      - title: "Mein ELSTER für Vereine"
        publisher: "Finanzverwaltung NRW"
        url: "https://www.finanzverwaltung.nrw.de/system/files/media/document/file/2026_05_26_internet_endf_einzs_brosch_meinelstervereine.pdf"
        preferred_format: "PDF"
        capture_method: "archive_pdf"
        reason: "ELSTER-/Erklärungskontext für Vereine, mit Gemeinnützigkeitswarnung.[web:8]"

    P1_archive_next:
      - title: "Vereine und Steuern"
        publisher: "Finanzamt Brandenburg"
        url: "https://finanzamt.brandenburg.de/sixcms/media.php/9/Vereine-und-Steuern-2023_web.pdf"
        preferred_format: "PDF"
        capture_method: "archive_pdf"
        reason: "Breiter Überblick für Vereine, trotz Gemeinnützigkeitsfokus.[web:54]"
      - title: "Die Gemeinnützigkeit und das Finanzamt"
        publisher: "Finanzministerium MV"
        url: "https://www.steuerportal-mv.de/static/Regierungsportal/Finanzministerium/Steuerportal/Dateien/Downloads/Merkblatt_Vereine_%20Die_Gemeinnuetzigkeit_und_das_Finanzamt.pdf"
        preferred_format: "PDF"
        capture_method: "archive_pdf"
        reason: "Wichtige Kontrastfolie zur Nicht-Gemeinnützigkeit von Safer Space e.V.[web:51]"
      - title: "Event-/Payout-Rechnungen"
        publisher: "Eventbrite"
        url: "https://www.eventbrite.de/help/de/articles/263015/"
        preferred_format: "HTML snapshot"
        capture_method: "archive_html_snapshot"
        reason: "Referenz, falls Eventbrite genutzt wird.[web:20][web:24]"

    P2_optional:
      - title: "Techno ist Musik (Berghain-Berichte)"
        publisher: "Süddeutsche/Presseschau"
        url: "https://www.sueddeutsche.de/wirtschaft/steuern-techno-club-berghain-1.5098195"
        reason: "Gute Illustration der BFH-Urteile, aber sekundär.[web:41]"
      - title: "Steuerblog Techno im Berghain ist Kultur"
        publisher: "Streck Mack Schwedhelm"
        url: "https://steueranwalt.de/news/steuerblog/techno_im_berghain_ist_kultur"
        reason: "Fachkommentar, nützlich für Argumentationslinie zu Kulturstatus.[web:45]"

    discard:
      - title: "ticket.io FAQ Veranstalter (ohne tiefe Export-Doku)"
        url: "https://www.ticket.io/ticketing-software/faq-veranstalter/"
        reason: "Operativ hilfreich, aber als alleinige KB-Quelle zu schwach und ohne detaillierte Steuer-/Exportbeschreibung.[web:33]"
        replacement: "pretix-Dokumentation zu Fiscal requirements und Taxes.[web:31][web:32]"
      - title: "Allgemeine Ehrenamt-/Auslagenartikel für gemeinnützige Vereine"
        url: "https://www.buergergesellschaft.de/..."
        reason: "Zu stark auf Gemeinnützigkeit und Ehrenamtspauschalen fokussiert.[web:51]"
        replacement: "Gezielte Auslagenersatz-Regeln mit Steuerberater und Auslagenersatzleitfaden (Deutsches Ehrenamt) unter Vorbehalt.[web:23]"

  unresolved_questions_for_tax_advisor:
    - question: "Welcher Umsatzsteuersatz (7% vs. 19%) ist für das geplante Equinox-Event mit DJs, Awareness-Team und Fundraising-Elementen im konkreten Fall anzuwenden?"
      topic: "Umsatzsteuer – Kultur vs. Club"
      why_unresolved: "Abgrenzung hängt von Eventkonzept, Behördenpraxis und BFH/Jurisprudenz ab; Quellen liefern Kriterien, aber keine Einzelfallentscheidung.[web:41][web:43][web:52]"
      sources_checked: "UStAE, BFH Techno-Urteile, Berichte zu Berghain, Haufe/Ticket-Eigenhändler.[web:41][web:43][web:52][web:60]"
      risk_if_wrong: "Zu niedrige USt (7% statt 19%) kann zu Nachforderungen und Zinsen bei Betriebsprüfung führen; zu hohe USt mindert Nettoeinnahmen unnötig."

    - question: "Kann die Eintrittskarte (print oder digital) ohne zusätzliche Rechnung als Kleinbetragsrechnung anerkannt werden, und welche Pflichtangaben müssen bei Nutzung eines Ticketing-Providers zwingend auf dem Ticket stehen?"
      topic: "Ticket als Rechnung / Kleinbetragsrechnung"
      why_unresolved: "§33 UStDV und IHK-Checklisten geben Mindestanforderungen, aber die praktische Umsetzung in einer Provider-Umgebung ist nicht klar geregelt.[web:3][web:1][web:10][web:31]"
      sources_checked: "§33 UStDV, IHK Berlin/IHK Niederbayern, pretix Fiscal/Taxes.[web:3][web:1][web:10][web:31][web:32]"
      risk_if_wrong: "Tickets könnten nicht als ordnungsgemäße Rechnungen anerkannt werden, was die Dokumentation von USt und Einnahmen erschwert."

    - question: "Wie ist eine Mindestbarumsatzgarantie vertraglich und steuerlich zu gestalten (echter vs. unechter Schadensersatz)?"
      topic: "Venue Settlement / Barumsatzgarantie"
      why_unresolved: "UStH 1.3 liefert Grundsatz, aber konkrete Eventverträge sind faktabhängig und nicht durch Standardquellen abgedeckt.[web:46]"
      sources_checked: "UStH 1.3, allgemeine Eventjuristische Quellen (oberflächlich).[web:46]"
      risk_if_wrong: "Falsche Behandlung als Schadensersatz oder Entgelt kann zu falscher USt-Berechnung und Streit mit Finanzamt führen."

    - question: "Wie sollen Stripe/PayPal-Sammelzahlungen, Gebühren und Payouts in der EÜR bei Istversteuerung konkret gebucht werden?"
      topic: "Istversteuerung / Zahlungsdienstleister"
      why_unresolved: "Providerdokumentation liefert technische Datenfelder, aber kein offizielles deutsches Buchungsschema für Vereine.[web:19][web:31][web:34]"
      sources_checked: "pretix DATEV-Integration, Stripe/PayPal-Gebühreninfos.[web:19][web:31][web:34]"
      risk_if_wrong: "Fehlerhafte Zuordnung von Einnahmen/Gebühren kann EÜR und USt-Voranmeldungen verfälschen."

    - question: "Wie sind ausländische DJ-/Performerhonorare und ggf. Agenturleistungen nach §50a EStG, Doppelbesteuerungsabkommen und Reverse-Charge-Regeln konkret zu behandeln?"
      topic: "Ausländische Künstler / §50a / Reverse Charge"
      why_unresolved: "BZSt-Infos und UStAE liefern Rahmendaten, aber konkrete Konstellationen erfordern individuelle Prüfung.[web:46][web:52]"
      sources_checked: "BZSt §50a, UStAE, allgemeine Fachartikel.[web:46][web:52][web:58]"
      risk_if_wrong: "Nicht abgeführte Quellensteuern oder falsche Reverse-Charge-Behandlung können zu erheblichen Nachzahlungen führen."

  final_recommendation:
    archive_immediately: >
      Die identifizierten P0-Quellen (Gesetze, BMF-/Finanzverwaltung-Merkblätter, KSK,
      Minijob-Zentrale, DRV, pretix-Dokumentation, GoBD-/Verfahrensdoku-Vorlagen) sollten
      zeitnah automatisiert heruntergeladen, versioniert und in die Wissensbasis
      aufgenommen werden.[web:3][web:6][web:9][web:16][web:17][web:31][web:7]
    research_more: >
      Für Venue-Verträge, 7% vs. 19% im konkreten Eventkontext, exakte Behandlung von
      Mindestumsatzgarantien, sowie detaillierte EÜR-/Kontenlogik für Zahlungsdienstleister
      sollten gezielte Rückfragen an Steuerberater und ggf. zusätzliche Spezialquellen
      (Law-Firm-Papers, Fachliteratur) eingeholt werden.[web:46][web:52][web:58]
    do_not_archive: >
      Dünne Marketingseiten, SEO-Artikel ohne klare Rechtsgrundlagen und stark
      gemeinnützigkeitsfokussierte Ehrenamtsguides sollten nicht als KB-Basis archiviert
      werden, sondern höchstens als Hintergrundlektüre.[web:33][web:48][web:56]
    next_step_for_playbook: >
      Aufbau eines Event-Playbooks mit Prozessketten (Ticketing, Zahlungsfluss,
      KSK-/Crew-Handling, Venue-Abrechnung, GoBD-Archiv) unter Nutzung der P0-/P1-Quellen
      und paralleler Abstimmung mit dem Steuerberater; jedes Kapitel sollte die
      zugrundeliegende Rechtsnorm (Gesetz/UStAE/BMF), operative Umsetzung (Providerdocs)
      und offene Risikofragen dokumentieren.[web:3][web:6][web:9][web:31]