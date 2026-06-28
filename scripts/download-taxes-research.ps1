# download-taxes-research.ps1  --  Safer Space e.V. Tax Research
# Run: Set-ExecutionPolicy Bypass -Scope Process; .\download-taxes-research.ps1

$base = "C:\GitDev\OpenClaw\Lika\Verein & Finances\Research_Taxes_Accounting"
$jina = "https://r.jina.ai"

New-Item -ItemType Directory -Force -Path ($base + "\PDFs") | Out-Null
New-Item -ItemType Directory -Force -Path ($base + "\HTML-MD") | Out-Null

Write-Host "Downloading 33 sources -- Safer Space Tax Research"
Write-Host "Output: C:\GitDev\OpenClaw\Lika\Verein & Finances\Research_Taxes_Accounting"

# --- PDF downloads (4) ---

Write-Host "  [PDF 1/4] GPT-SRC-002"
try {
  Invoke-WebRequest -Uri "https://www.ihk-niederbayern.de/pdfs/checkliste-kleinbetragsrechnungen-data.pdf" -OutFile ($base + "\PDFs\IHK-Niederbayern_Checkliste-Kleinbetragsrechnungen.pdf") -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] IHK-Niederbayern_Checkliste-Kleinbetragsrechnungen" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [PDF 2/4] GPT-SRC-003"
try {
  Invoke-WebRequest -Uri "https://www.kuenstlersozialkasse.de/fileadmin/Dokumente/Mediencenter_Unternehmer_Verwerter/Informationsschriften/Info_04_Abgabepflicht_von_Veranstaltern.pdf" -OutFile ($base + "\PDFs\KSK_Info04_Abgabepflicht-Veranstalter.pdf") -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] KSK_Info04_Abgabepflicht-Veranstalter" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [PDF 3/4] GPT-SRC-004"
try {
  $u = "https://www.deutsche-rentenversicherung.de/SharedDocs/Formulare/DE/_pdf/K5001.pdf?__blob=publicationFile&v=9"
  Invoke-WebRequest -Uri $u -OutFile ($base + "\PDFs\DRV_K5001_Kuenstlersozialabgabe.pdf") -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] DRV_K5001_Kuenstlersozialabgabe" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [PDF 4/4] GPT-SRC-016"
try {
  Invoke-WebRequest -Uri "https://www.lfst.bayern.de/fileadmin/RESSOURCEN/INFORMATIONEN/Steuerinfos/Zielgruppen/Vereine/Merkblatt_Festveranstaltungen_2025-01.pdf" -OutFile ($base + "\PDFs\LfSt-Bayern_Merkblatt-Festveranstaltungen-2025.pdf") -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] LfSt-Bayern_Merkblatt-Festveranstaltungen-2025" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

# --- HTML to Markdown via Jina (29) ---

Write-Host "  [HTML 1/29] GPT-SRC-001"
try {
  Invoke-WebRequest -Uri "https://r.jina.ai/https://www.ihk.de/berlin/service-und-beratung/recht-und-steuern/steuern-und-finanzen/pflichtangaben-in-rechnungen-4400732" -OutFile ($base + "\HTML-MD\IHK-Berlin_Pflichtangaben-Rechnungen.md") -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] IHK-Berlin_Pflichtangaben-Rechnungen" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [HTML 2/29] GPT-SRC-005"
try {
  Invoke-WebRequest -Uri "https://r.jina.ai/https://www.datev.de/web/de/shop/produkt-details/datev-kontenrahmen-skr-42-vereine-stiftungen-ggmbh-bilanz-12901" -OutFile ($base + "\HTML-MD\DATEV_SKR42-Kontenrahmen.md") -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] DATEV_SKR42-Kontenrahmen" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [HTML 3/29] GPT-SRC-006"
try {
  Invoke-WebRequest -Uri "https://r.jina.ai/https://help-center.apps.datev.de/documents/1022996" -OutFile ($base + "\HTML-MD\DATEV_SKR42-Branchenpaket-Einrichten.md") -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] DATEV_SKR42-Branchenpaket-Einrichten" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [HTML 4/29] GPT-SRC-007"
try {
  Invoke-WebRequest -Uri "https://r.jina.ai/https://www.datev.de/web/de/berufsgruppenuebergreifend/ratgeber/rechnungswesen/verfahrensdokumentation-gemaess-gobd-erstellen" -OutFile ($base + "\HTML-MD\DATEV_Verfahrensdokumentation-GoBD.md") -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] DATEV_Verfahrensdokumentation-GoBD" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [HTML 5/29] GPT-SRC-008"
try {
  Invoke-WebRequest -Uri "https://r.jina.ai/https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Weitere_Steuerthemen/Abgabenordnung/AO-Anwendungserlass/2024-03-11-aenderung-gobd.html" -OutFile ($base + "\HTML-MD\BMF_GoBD-2024.md") -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] BMF_GoBD-2024" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [HTML 6/29] GPT-SRC-009"
try {
  Invoke-WebRequest -Uri "https://r.jina.ai/https://docs.pretix.eu/de/trust/fiscal/germany/" -OutFile ($base + "\HTML-MD\pretix_Fiscal-Requirements-Germany.md") -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] pretix_Fiscal-Requirements-Germany" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [HTML 7/29] GPT-SRC-010"
try {
  Invoke-WebRequest -Uri "https://r.jina.ai/https://docs.pretix.eu/de/guides/taxes/" -OutFile ($base + "\HTML-MD\pretix_Taxes-Guide.md") -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] pretix_Taxes-Guide" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [HTML 8/29] GPT-SRC-011"
try {
  Invoke-WebRequest -Uri "https://r.jina.ai/https://www.ticket.io/controlling/" -OutFile ($base + "\HTML-MD\ticketio_Event-Controlling-Reporting.md") -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] ticketio_Event-Controlling-Reporting" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [HTML 9/29] GPT-SRC-012"
try {
  Invoke-WebRequest -Uri "https://r.jina.ai/https://www.ticket.io/ticketing-software/faq-veranstalter/" -OutFile ($base + "\HTML-MD\ticketio_FAQ-Veranstalter.md") -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] ticketio_FAQ-Veranstalter" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [HTML 10/29] GPT-SRC-013"
try {
  Invoke-WebRequest -Uri "https://r.jina.ai/https://www.eventbrite.de/help/de/articles/187426/so-erstellen-und-exportieren-sie-eine-umsatzuebersicht/" -OutFile ($base + "\HTML-MD\Eventbrite_Umsatzuebersicht-Export.md") -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] Eventbrite_Umsatzuebersicht-Export" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [HTML 11/29] GPT-SRC-014"
try {
  Invoke-WebRequest -Uri "https://r.jina.ai/https://www.eventbrite.de/help/de/articles/312206/bericht-ueber-vertriebskanaele-und-zahlungsarten-herunterladen/" -OutFile ($base + "\HTML-MD\Eventbrite_Vertriebskanaele-Zahlungsarten.md") -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] Eventbrite_Vertriebskanaele-Zahlungsarten" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [HTML 12/29] GPT-SRC-015"
try {
  Invoke-WebRequest -Uri "https://r.jina.ai/https://www.finanzamt.nrw.de/steuerinfos/weitere-themen/vereine-und-stiftungen/vereine-und-die-umsatzsteuer" -OutFile ($base + "\HTML-MD\FinanzamtNRW_Vereine-Umsatzsteuer.md") -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] FinanzamtNRW_Vereine-Umsatzsteuer" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [HTML 13/29] GPT-SRC-017"
try {
  Invoke-WebRequest -Uri "https://r.jina.ai/https://www.ihk-muenchen.de/ratgeber/steuern/elektronische-rechnungen/" -OutFile ($base + "\HTML-MD\IHK-Muenchen_E-Rechnung.md") -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] IHK-Muenchen_E-Rechnung" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [HTML 14/29] GPT-SRC-018"
try {
  Invoke-WebRequest -Uri "https://r.jina.ai/https://www.bundesfinanzministerium.de/Content/DE/FAQ/e-rechnung.html" -OutFile ($base + "\HTML-MD\BMF_FAQ-E-Rechnung.md") -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] BMF_FAQ-E-Rechnung" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [HTML 15/29] GPT-SRC-019"
try {
  Invoke-WebRequest -Uri "https://r.jina.ai/https://deutsches-ehrenamt.de/steuern-finanzen/rechnungslegung-buchfuehrung-verein/" -OutFile ($base + "\HTML-MD\DeutschesEhrenamt_Rechnungslegung-Verein.md") -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] DeutschesEhrenamt_Rechnungslegung-Verein" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [HTML 16/29] GPT-SRC-020"
try {
  Invoke-WebRequest -Uri "https://r.jina.ai/https://www.buergergesellschaft.de/praxishilfen/arbeit-im-verein/rechtsgrundlagen/ehrenamtliche-mitarbeit-arbeits-beschaeftigungs-und-dienstverhaeltnisse/ehrenamt-auslagen-aufwandsentschaedigung/" -OutFile ($base + "\HTML-MD\Buergergesellschaft_Ehrenamt-Auslagen.md") -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] Buergergesellschaft_Ehrenamt-Auslagen" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [HTML 17/29] GEM-SRC-005"
try {
  Invoke-WebRequest -Uri "https://r.jina.ai/https://www.awv-net.de" -OutFile ($base + "\HTML-MD\AWV_GoBD-Praxisleitfaden.md") -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] AWV_GoBD-Praxisleitfaden" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [HTML 18/29] GEM-SRC-006"
try {
  Invoke-WebRequest -Uri "https://r.jina.ai/https://www.ihk.de/mittlerer-niederrhein" -OutFile ($base + "\HTML-MD\IHK-MittlererNiederrhein_Kulturveranstaltungen-USt.md") -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] IHK-MittlererNiederrhein_Kulturveranstaltungen-USt" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [HTML 19/29] GEM-SRC-008"
try {
  Invoke-WebRequest -Uri "https://r.jina.ai/https://deutsches-ehrenamt.de" -OutFile ($base + "\HTML-MD\DeutschesEhrenamt_Wirtschaftlicher-Geschaeftsbetrieb.md") -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] DeutschesEhrenamt_Wirtschaftlicher-Geschaeftsbetrieb" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [HTML 20/29] GEM-SRC-009"
try {
  Invoke-WebRequest -Uri "https://r.jina.ai/https://eventfaq.de" -OutFile ($base + "\HTML-MD\eventfaq_Club-Veranstaltungsvertrag-Mindestumsatz.md") -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] eventfaq_Club-Veranstaltungsvertrag-Mindestumsatz" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [HTML 21/29] GEM-SRC-010"
try {
  Invoke-WebRequest -Uri "https://r.jina.ai/https://www.vereinswelt.de" -OutFile ($base + "\HTML-MD\Vereinswelt_Auslagenerstattung-Muster.md") -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] Vereinswelt_Auslagenerstattung-Muster" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [HTML 22/29] GEM-SRC-012"
try {
  Invoke-WebRequest -Uri "https://r.jina.ai/https://www.vereinsknowhow.de" -OutFile ($base + "\HTML-MD\vereinsknowhow_Kassenfuehrung-Verein.md") -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] vereinsknowhow_Kassenfuehrung-Verein" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [HTML 23/29] GEM-SRC-013"
try {
  Invoke-WebRequest -Uri "https://r.jina.ai/https://www.lexoffice.de/wissenswelt" -OutFile ($base + "\HTML-MD\lexoffice_Ist-vs-Sollversteuerung.md") -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] lexoffice_Ist-vs-Sollversteuerung" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [HTML 24/29] GEM-SRC-014"
try {
  Invoke-WebRequest -Uri "https://r.jina.ai/https://www.vut.de" -OutFile ($base + "\HTML-MD\VUT_KSK-Abgabepflicht-Elektronische-Musik.md") -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] VUT_KSK-Abgabepflicht-Elektronische-Musik" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [HTML 25/29] GEM-SRC-015"
try {
  Invoke-WebRequest -Uri "https://r.jina.ai/https://www.deutsche-rentenversicherung.de" -OutFile ($base + "\HTML-MD\DRV_Minijob-Kurzfristige-Beschaeftigung.md") -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] DRV_Minijob-Kurzfristige-Beschaeftigung" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [HTML 26/29] GEM-SRC-016"
try {
  Invoke-WebRequest -Uri "https://r.jina.ai/https://www.ihk.de/koblenz" -OutFile ($base + "\HTML-MD\IHK-Koblenz_Reverse-Charge-Auslaendische-Dienstleister.md") -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] IHK-Koblenz_Reverse-Charge-Auslaendische-Dienstleister" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [HTML 27/29] GEM-SRC-017"
try {
  Invoke-WebRequest -Uri "https://r.jina.ai/https://www.hannover.ihk.de" -OutFile ($base + "\HTML-MD\IHK-Hannover_E-Rechnungspflicht-Vereine-2025.md") -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] IHK-Hannover_E-Rechnungspflicht-Vereine-2025" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [HTML 28/29] GEM-SRC-019"
try {
  Invoke-WebRequest -Uri "https://r.jina.ai/https://www.buchhaltungsbutler.de/wissen" -OutFile ($base + "\HTML-MD\BuchhaltungsButler_EUeR-Kostenstellen.md") -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] BuchhaltungsButler_EUeR-Kostenstellen" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "  [HTML 29/29] GEM-SRC-020"
try {
  Invoke-WebRequest -Uri "https://r.jina.ai/https://www.stbk-hamburg.de" -OutFile ($base + "\HTML-MD\StBK-Hamburg_Mindestumsatzgarantien-Gastronomie.md") -UseBasicParsing -TimeoutSec 30
} catch {
  Write-Host "    [SKIP] StBK-Hamburg_Mindestumsatzgarantien-Gastronomie" -ForegroundColor Yellow
}
Start-Sleep -Seconds 1

Write-Host "Done!" -ForegroundColor Green
$pc = (Get-ChildItem -Path ($base + "\PDFs") -Filter "*.pdf").Count
$mc = (Get-ChildItem -Path ($base + "\HTML-MD") -Filter "*.md").Count
Write-Host "Files saved: " + $pc + " PDFs, " + $mc + " Markdown"
explorer.exe $base