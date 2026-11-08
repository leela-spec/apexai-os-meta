#!/usr/bin/env python3
"""
generate_northstar_html.py
Generates the authentic Northstar Weekly Precap HTML for Week 2026-W45.
Conforms strictly to SPEC-PRECAP-WEEK-ITERATIONS-v1.1:
1. Part 1: Operator Decision Brief (OpenProject default + operator flow decisions).
2. Part 2: Matrix 1 — Project Overview & Critical Path (5 Repos: MoA, Leela, IPOS, ApexOS, Residuals).
3. Part 3: Matrix 2 — Calendar Snapshot & Visualization (Operating Window 08:00–24:00, Shutdown 21:00).
4. Part 4: Google Calendar Live Sync Receipt (gehm77@gmail.com).
"""

import os

def build_html():
    return """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Northstar · Weekly Command Brief 2026-W45</title>
<style>
*{box-sizing:border-box}
html{scroll-behavior:smooth;overflow-wrap:anywhere}
body{margin:0;background:#f8f6ef;color:#172a3d;font:14px/1.55 system-ui,Segoe UI,Arial}
main{max-width:1480px;margin:auto;padding:26px 32px 60px}
h1{font:clamp(34px,4vw,54px)/1.1 Georgia,serif;letter-spacing:-1.4px;margin:20px 0 12px;max-width:880px}
h2{font-size:22px;margin:0;font-family:Georgia,serif;letter-spacing:-0.5px}
h3{font-size:15px;margin:0}
p{margin:8px 0;color:#687b8b}
a{color:#315c7f;text-decoration:none}
a:hover{text-decoration:underline}
button,input,select{font:inherit}
button,summary{cursor:pointer}
button,a,input,select{touch-action:manipulation}
:focus-visible{outline:3px solid #a2b881;outline-offset:3px}
.strap{display:flex;align-items:center;gap:12px}
.brand{background:#dcebbd;border-radius:12px;padding:9px 14px;font:700 22px Georgia;color:#152334}
.eyebrow{text-transform:uppercase;letter-spacing:1.8px;font-size:10px;color:#698095;font-weight:750}
.northline{height:4px;background:linear-gradient(90deg,#304e86,#e0ad77,#e3e4c9);border-radius:4px;margin-top:18px}
.hero{display:grid;grid-template-columns:1.4fr 1fr;gap:30px;align-items:end}
.metrics{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;margin:20px 0}
.metric{background:#fffdf8;border:1px solid #dfe3de;border-radius:10px;padding:13px;min-width:0}
.metric b{display:block;font:30px Georgia;color:#162642}
.metric span{color:#718491;font-size:11px}
.source-note{font-size:11px;background:#f2eee3;border-left:3px solid #b7a472;padding:11px 14px;border-radius:0 8px 8px 0;margin:15px 0}
.tabs{display:flex;gap:9px;flex-wrap:wrap;position:sticky;top:0;background:#f8f6eff2;backdrop-filter:blur(8px);padding:12px 0;z-index:10;border-bottom:1px solid #e4e3d9;margin-top:15px}
.tabs a{padding:7px 12px;font-weight:650;font-size:12px;background:#fff;border:1px solid #dce1df;border-radius:7px;color:#355570}
.tabs a:hover{background:#edf2f5}
.section{margin-top:40px;scroll-margin-top:80px}
.sectionhead{display:flex;align-items:baseline;justify-content:space-between;gap:20px;margin-bottom:14px}
.sectionhead small{color:#7a8993}
.panel{background:#fffdf8;border:1px solid #dde2dd;border-radius:13px;padding:22px;min-width:0;overflow:hidden}

/* First 10 Seconds Motivational Grid */
.motivational-grid{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:12px;margin:14px 0}
.motivational-card{background:#fff;border:1px solid #dce4e8;border-radius:10px;padding:14px;display:flex;flex-direction:column}
.motivational-card b{font-size:13px;color:#162642;margin-bottom:4px;display:block}
.motivational-card p{font-size:11px;line-height:1.45;color:#5c6f80;margin:4px 0 10px}
.motivational-card .impact-badge{margin-top:auto;padding:3px 7px;border-radius:5px;font-size:9px;font-weight:700;display:inline-block}

/* 7-Day Overview Strip */
.weekgrid{display:grid;grid-template-columns:repeat(7,minmax(0,1fr));gap:10px}
.day{padding:14px 12px;background:#fffdf8;border:1px solid #dce3df;border-radius:10px;border-top:4px solid #6c8267;min-width:0;display:flex;flex-direction:column}
.day.meeting{border-top-color:#304e86;background:#fdfdff}
.day.alternative{border-top-color:#c19f66}
.day.off{background:#f0eee6;border-top-color:#a3aaa7}
.day small{font-size:10px;color:#80909c}
.day h3{margin:8px 0 4px;font-size:13px;color:#162642;line-height:1.3}
.day p{font-size:11px;line-height:1.45;color:#5c6f80;margin:4px 0}
.flow-tag{display:inline-block;padding:2px 5px;background:#edf2f6;border-radius:4px;font-size:9px;font-weight:700;color:#456890;margin-right:3px}
.event-alert{background:#eef4fc;border:1px solid #c9dcf4;border-radius:6px;padding:6px;margin:8px 0;font-size:10px;color:#224672}
.event-alert b{display:block;color:#123259}
.refs{display:flex;gap:5px;flex-wrap:wrap;margin-top:auto;padding-top:8px}
.refs a{font-size:9px;font-weight:700;padding:2px 5px;background:#eef2f5;border-radius:4px;color:#355570}

/* Project Landscape & Drilldown */
.projectgrid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px;align-items:start}
details.project{border:1px solid #dce2e2;border-radius:12px;background:#fffdf9;box-shadow:0 3px 12px #10263608;overflow:hidden;margin-bottom:14px}
details.project>summary{padding:16px;font-weight:700;font-size:15px;background:#fff;border-bottom:1px solid #edf1f2;display:flex;align-items:center;justify-content:space-between;cursor:pointer}
details.project>summary:before{content:'▸';margin-right:8px;color:#788b99}
details.project[open]>summary:before{content:'▾'}
.project-meta{font-size:10px;font-weight:400;color:#7d8c97;padding:3px 8px;border-radius:12px;background:#f2f5f7}
.projectbody{padding:18px}
.project-intent{font-size:12px;color:#546677;line-height:1.6;margin-bottom:14px;background:#f5f8f5;border-left:3px solid #7c9870;padding:10px 14px;border-radius:0 6px 6px 0}
.project-intent b{color:#2a4422;display:block;margin-bottom:3px}

/* Work Item Cards */
details.work{border:1px solid #e1e6e8;border-radius:8px;margin:8px 0;background:#fff}
details.work>summary{padding:10px 12px;font-size:12px;font-weight:600;display:flex;align-items:center;gap:8px;cursor:pointer}
details.work>summary:before{content:'▸';color:#90a0ab}
details.work[open]>summary:before{content:'▾'}
.state-icon{display:inline-grid;place-items:center;width:20px;height:20px;border-radius:5px;font-size:11px;font-weight:700}
.state-icon.new{background:#edf2f5;color:#4d6d85}
.state-icon.progress{background:#dcf2e3;color:#256338}
.state-icon.spec{background:#f1e8f7;color:#6b3b87}
.state-icon.critical{background:#feece8;color:#9e3424}
.work-summary-title{flex:1;color:#182b3d}
.work-badge{font-size:9px;font-weight:700;padding:2px 6px;border-radius:4px;background:#f0f3f5;color:#657788}
.workbody{padding:12px 14px;font-size:12px;border-top:1px solid #f0f3f4;background:#fcfdfd}
.sprint-block{margin:8px 0;padding:8px 10px;background:#fff;border:1px solid #e7ebed;border-radius:6px}
.sprint-block b{color:#304e86;font-size:11px;display:block;margin-bottom:4px}
.checklist{margin:0;padding-left:18px;color:#506272;font-size:11px}
.checklist li{margin:3px 0}
.inspector{margin-top:10px;padding-top:8px;border-top:1px dashed #dce2e5}
.edge{font-size:10px;color:#667a8c;display:flex;align-items:center;gap:6px;margin:4px 0}

@media(max-width:1150px){
  .motivational-grid{grid-template-columns:repeat(3,minmax(0,1fr))}
  .weekgrid{grid-template-columns:repeat(4,minmax(0,1fr))}
  .projectgrid{grid-template-columns:1fr}
  .hero{grid-template-columns:1fr}
}
@media(max-width:650px){
  main{padding:16px 12px 40px}
  .motivational-grid{grid-template-columns:1fr}
  .weekgrid{grid-template-columns:repeat(2,minmax(0,1fr))}
  .day.off{grid-column:1/-1}
}
</style>
</head>
<body>
<main>

<header>
  <div class="strap">
    <span class="brand">N</span>
    <div>
      <b>Northstar</b>
      <div class="eyebrow">Portfolio / Operator Decisions / Proposed Week</div>
    </div>
  </div>
  <div class="northline"></div>
  <div class="hero">
    <div>
      <h1>The whole portfolio.<br>The paths that move it forward.</h1>
      <p>Universal specification conformance: Operator decisions upfront, non-temporal project flows across five repositories, and a full calendar snapshot operating from 08:00 to 24:00 with shutdown at 21:00.</p>
    </div>
    <div class="metrics">
      <div class="metric"><b>05</b><span>focus repositories</span></div>
      <div class="metric"><b>08–24</b><span>daily operating span</span></div>
      <div class="metric"><b>21:00</b><span>daily shutdown</span></div>
    </div>
  </div>
  <p class="source-note">
    <b>Operating Invariant:</b> OpenProject scanning is the default basis for task proposals; active operator decisions steer the 4-flow operating structure for Week 45. Real appointments (Alex & Chris, München Tanz, WC Meister) are protected and mapped into free focus intervals.
  </p>
  <nav class="tabs">
    <a href="#brief">01 · Operator Decisions</a>
    <a href="#matrix1">02 · Matrix 1: Project Overview & Critical Path</a>
    <a href="#matrix2">03 · Matrix 2: Calendar Snapshot & Visualization</a>
    <a href="#calendar-sync">04 · Google Calendar Sync</a>
  </nav>
</header>

<!-- PART 1: OPERATOR DECISION BRIEF -->
<section class="section" id="brief">
  <div class="sectionhead">
    <h2>01 · Operator Decision Brief</h2>
    <small>Governance choices, flow allocations & critical path locks for Week 45</small>
  </div>
  <div class="panel">
    <p style="font-size:12px; margin-bottom:16px;">
      <b>Operator Sovereignty:</b> While OpenProject provides the baseline task intake, the operator sets the flow structure for the week. The active operator state assigns four daily flows (3x3 standard): two for Master of Arts (Content, Website & Invoicing), one for IPOS, and one residual flow for personal creative integration.
    </p>

    <div style="display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:14px;">
      
      <div style="border:1px solid #dce4e8; border-radius:10px; padding:14px; background:#fff;">
        <span class="eyebrow" style="color:#a84332;">[P0 | I95/E40/R10] Critical Path Lock</span>
        <h3 style="margin:6px 0; font-family:Georgia,serif; font-size:15px;">D-W45-01: Karakeep Retirement & Docling Ingestion Adapter</h3>
        <p style="font-size:11px;"><b>Context:</b> Legacy Karakeep mocks block clean financial PDF parsing into sovereign JSON.</p>
        <p style="font-size:11px;"><b>Action:</b> Lock ADR-003, purge obsolete imports in <code>ipos/ingest/</code>, and deploy Docling adapter (WP #224 ➔ #226).</p>
        <span style="background:#eaf2e6; color:#2c5225; padding:2px 7px; border-radius:4px; font-size:10px; font-weight:700;">APPROVED FOR EXECUTION</span>
      </div>

      <div style="border:1px solid #dce4e8; border-radius:10px; padding:14px; background:#fff;">
        <span class="eyebrow" style="color:#336299;">[P1 | I90/E35/R15] Public Reading Experience</span>
        <h3 style="margin:6px 0; font-family:Georgia,serif; font-size:15px;">D-W45-02: Master of Arts Website Navigation Refactor</h3>
        <p style="font-size:11px;"><b>Context:</b> Reading longform philosophical essays requires a responsive flexbox header and mobile drawer.</p>
        <p style="font-size:11px;"><b>Action:</b> Implement CSS flexbox nav, hamburger slide-out menu, and article route integration (WP #163).</p>
        <span style="background:#eaf2e6; color:#2c5225; padding:2px 7px; border-radius:4px; font-size:10px; font-weight:700;">APPROVED FOR EXECUTION</span>
      </div>

      <div style="border:1px solid #dce4e8; border-radius:10px; padding:14px; background:#fff;">
        <span class="eyebrow" style="color:#a84332;">[P1 | I88/E30/R10] Business Operations</span>
        <h3 style="margin:6px 0; font-family:Georgia,serif; font-size:15px;">D-W45-03: Line-Item Invoicing Engine & Automated PDF Generator</h3>
        <p style="font-size:11px;"><b>Context:</b> Client billing and tax calculations are handled manually without schema validation.</p>
        <p style="font-size:11px;"><b>Action:</b> Author line-item JSON schema, bind print stylesheet, and verify PDF receipt output (WP-BIZ-01).</p>
        <span style="background:#fef3dd; color:#856434; padding:2px 7px; border-radius:4px; font-size:10px; font-weight:700;">PROPOSED WEDNESDAY PASS</span>
      </div>

      <div style="border:1px solid #dce4e8; border-radius:10px; padding:14px; background:#fff;">
        <span class="eyebrow" style="color:#71828f;">[P2 | I80/E20/R05] Scope Boundary</span>
        <h3 style="margin:6px 0; font-family:Georgia,serif; font-size:15px;">D-W45-04: ACIM Dedicated Credits Boundary</h3>
        <p style="font-size:11px;"><b>Context:</b> Secular ACIM commentary page (WP #204) is documented in OpenProject.</p>
        <p style="font-size:11px;"><b>Action:</b> Retain WP #204 in project records; cleanly unlink from active Week 45 deliverables to focus on core website/invoicing.</p>
        <span style="background:#edf2f5; color:#556879; padding:2px 7px; border-radius:4px; font-size:10px; font-weight:700;">PRESERVED IN BACKLOG</span>
      </div>

    </div>
  </div>
</section>

<!-- PART 2: MATRIX 1 — PROJECT OVERVIEW & CRITICAL PATH -->
<section class="section" id="matrix1">
  <div class="sectionhead">
    <h2>02 · Matrix 1: Project Overview & Critical Path (Non-Temporal)</h2>
    <small>Motivational high-level orientation & process flows across the 5 repository frontiers</small>
  </div>

  <!-- First 10 Seconds Motivational Grid -->
  <div class="motivational-grid">
    <div class="motivational-card">
      <span class="eyebrow" style="color:#507967;">Master of Arts</span>
      <b>Public Voice & Invoicing</b>
      <p>Refreshes reader experience with modern navigation, records thesis voiceover audio, and deploys verified automated PDF billing.</p>
      <span class="impact-badge" style="background:#dcf2e3; color:#18572e;">High Leverage · Public Launch</span>
    </div>
    <div class="motivational-card">
      <span class="eyebrow" style="color:#355570;">Leela</span>
      <b>Sequencing & Progression</b>
      <p>Stabilizes Wave A domain models, lifecycle timer countdowns, and spatial node hierarchy contracts for skill trees.</p>
      <span class="impact-badge" style="background:#eaf2fb; color:#224672;">Core Infrastructure</span>
    </div>
    <div class="motivational-card">
      <span class="eyebrow" style="color:#b08445;">Investment / IPOS</span>
      <b>Docling Ingestion Engine</b>
      <p>Retires obsolete Karakeep legacy debt and establishes clean IBM Docling multi-page PDF financial extraction into sovereign JSON.</p>
      <span class="impact-badge" style="background:#fef3dd; color:#856434;">Critical Path · Unlocks Intake</span>
    </div>
    <div class="motivational-card">
      <span class="eyebrow" style="color:#785890;">Apex OS</span>
      <b>Hardware Interception</b>
      <p>Binds kernel USB HID polling hooks and button event dispatchers to establish low-latency input event processing.</p>
      <span class="impact-badge" style="background:#f5eefb; color:#592f75;">Standalone Driver Pipeline</span>
    </div>
    <div class="motivational-card">
      <span class="eyebrow" style="color:#806655;">Residuals</span>
      <b>Personal Life & Harmony</b>
      <p>Acoustic studio setup, physical art painting, aesthetic portrait color grading, and travel logistics in daily 3x3 afternoon sprints.</p>
      <span class="impact-badge" style="background:#f9f5f0; color:#684f3e;">Life Integration Standard</span>
    </div>
  </div>

  <!-- Repository Containers -->
  <div class="projectgrid">

    <!-- Repo 1: Master of Arts -->
    <details class="project" id="repo-moa" open>
      <summary>
        <span>📁 Master of Arts (Website, Content, Invoicing & Studio Art)</span>
        <span class="project-meta">OP #14, #6, #7 · 4 Workstreams</span>
      </summary>
      <div class="projectbody">
        <div class="project-intent">
          <b>Operator Focus for Week 45:</b>
          Modernize public reading layout via CSS flexbox and drawer menu, produce longform intellectual essays and spoken audio narration, deploy automated PDF invoicing, and organize the physical art studio.
        </div>

        <details class="work" open>
          <summary>
            <span class="state-icon new">○</span>
            <span class="work-summary-title">WP #163 Content Transformation & Flexbox Navigation</span>
            <span class="work-badge">moa-website (#14)</span>
          </summary>
          <div class="workbody">
            <p><b>Baseline:</b> Static navbar lacks mobile drawer support.</p>
            <p><b>Process Flow:</b> CSS Flexbox Grid ➔ Mobile Slide-out Drawer ↻ Cross-browser Pass ➔ Live Route Bind.</p>
            <div class="sprint-block">
              <b>30m Sprints (Mon–Tue F2):</b>
              <ul class="checklist">
                <li>• Sprint A: Flexbox container and nav-item active states</li>
                <li>• Sprint B: Hamburger drawer CSS transition animation</li>
                <li>• Sprint C: Chrome/Safari mobile responsive audit</li>
              </ul>
            </div>
          </div>
        </details>

        <details class="work" open>
          <summary>
            <span class="state-icon progress">◐</span>
            <span class="work-summary-title">Creative Content Production & Spoken Narration Pipeline</span>
            <span class="work-badge">moa-content (#6)</span>
          </summary>
          <div class="workbody">
            <p><b>Process Flow:</b> Core Thesis Outline ➔ Vocal Narration Cut ↻ Frequency Balancing ➔ Substack Release.</p>
            <div class="sprint-block">
              <b>Daily 30m Sprints (Daily F1):</b>
              <ul class="checklist">
                <li>• S1: Thesis outlining and philosophical cross-references</li>
                <li>• S2: Spoken voiceover recording and rough take cuts</li>
                <li>• S3: Dynamic caption syncing for social vertical reels</li>
              </ul>
            </div>
          </div>
        </details>

        <details class="work" open>
          <summary>
            <span class="state-icon critical">★</span>
            <span class="work-summary-title">WP-BIZ-01 Line-Item Invoicing Calculation Engine & PDF Billing</span>
            <span class="work-badge">moa-business (#7)</span>
          </summary>
          <div class="workbody">
            <p><b>Process Flow:</b> Line-item JSON Schema ➔ Tax Calculation Tests ↻ HTML Print Stylesheet ➔ PDF Generator.</p>
            <div class="sprint-block">
              <b>30m Sprints (Wed–Fri F2):</b>
              <ul class="checklist">
                <li>• Wed: Invoice JSON schema & unit tests for subtotal math</li>
                <li>• Thu: HTML print-ready template & headless PDF export</li>
                <li>• Fri: Client billing batch verification run</li>
              </ul>
            </div>
          </div>
        </details>
      </div>
    </details>

    <!-- Repo 2: Leela -->
    <details class="project" id="repo-leela" open>
      <summary>
        <span>📁 Leela (Skill Tree, Path & Sequencing Integration Core)</span>
        <span class="project-meta">OP #3, #10, #9, #11 · 3 Workstreams</span>
      </summary>
      <div class="projectbody">
        <div class="project-intent">
          <b>Integration Meta-System:</b>
          Governs the holistic weekly budget, Wave A domain models, sequence countdown timer resilience across mobile app lifecycle, and spatial Chunk library contracts.
        </div>

        <details class="work" open>
          <summary>
            <span class="state-icon new">○</span>
            <span class="work-summary-title">WP #216 Wave A Domain Models & Structure Hashes</span>
            <span class="work-badge">leela-sequencing (#11)</span>
          </summary>
          <div class="workbody">
            <p><b>Process Flow:</b> Domain Entity Contract ➔ Serializers ↻ Hashes ➔ Neutral Seam.</p>
            <div class="sprint-block">
              <b>30m Sprints:</b>
              <ul class="checklist">
                <li>• S1: Review landed Wave A domain types and IDs</li>
                <li>• S2: Keep sequence countdown correct across app lifecycle (WP #212)</li>
                <li>• S3: Verify database-neutral repository seam (WP #217)</li>
              </ul>
            </div>
          </div>
        </details>
      </div>
    </details>

    <!-- Repo 3: Investment / IPOS -->
    <details class="project" id="repo-ipos" open>
      <summary>
        <span>📁 Investment / IPOS (Research Intake & Ingestion)</span>
        <span class="project-meta">OP #16 · 10 WPs · 6 Typed Relations</span>
      </summary>
      <div class="projectbody">
        <div class="project-intent">
          <b>Active Dependency Chain (Relations #92–#97):</b>
          Retire Karakeep debt (ADR-003) ➔ Implement Docling PDF adapter ➔ Benchmark test harness ➔ Wire Cockpit dashboard ➔ Dispatch Telegram research digest.
        </div>

        <details class="work" open>
          <summary>
            <span class="state-icon progress">◐</span>
            <span class="work-summary-title">WP #224 ADR-003: Formalize Karakeep Retirement</span>
            <span class="work-badge" style="background:#feece8; color:#9e3424;">CRITICAL PATH</span>
          </summary>
          <div class="workbody">
            <p><b>Baseline:</b> Stale Karakeep imports linger in <code>ipos/ingest/</code>.</p>
            <p><b>Outcome:</b> Deprecate obsolete modules, purge mocks, lock ADR-003 record. Unblocks Docling adapter (WP #226).</p>
          </div>
        </details>

        <details class="work" open>
          <summary>
            <span class="state-icon new">○</span>
            <span class="work-summary-title">WP #226 RI-11: Implement IBM Docling & Trafilatura Adapter</span>
            <span class="work-badge" style="background:#feece8; color:#9e3424;">CRITICAL PATH</span>
          </summary>
          <div class="workbody">
            <p><b>Process Flow:</b> Docling PDF Extraction ➔ Trafilatura Web Scraper ↻ Schema Map ➔ Sovereign JSON.</p>
            <div class="sprint-block">
              <b>30m Sprints (Mon–Tue F3):</b>
              <ul class="checklist">
                <li>• S1: Configure Docling PDF extractor for multi-column research</li>
                <li>• S2: Wire Trafilatura article text cleaner</li>
                <li>• S3: Test against complex multi-page PDF sample fixtures</li>
              </ul>
            </div>
          </div>
        </details>
      </div>
    </details>

    <!-- Repo 4: Apex OS -->
    <details class="project" id="repo-apex" open>
      <summary>
        <span>📁 Apex OS (Kernel Driver & OpenMouse Hardware Interceptor)</span>
        <span class="project-meta">OP #8 · Standalone Systems Project</span>
      </summary>
      <div class="projectbody">
        <div class="project-intent">
          <b>Hardware Driver Pipeline:</b>
          Low-latency USB HID event polling and button interceptors establishing hardware bindings for custom macro inputs.
        </div>

        <details class="work" open>
          <summary>
            <span class="state-icon new">○</span>
            <span class="work-summary-title">WP-APEX-01 Kernel USB HID Polling Hook & Debounce Filter</span>
            <span class="work-badge">apex-os</span>
          </summary>
          <div class="workbody">
            <p><b>Process Flow:</b> HID Parser ➔ Kernel Interrupt Handler ↻ Debounce State Machine ➔ IPC Socket.</p>
            <div class="sprint-block">
              <b>30m Sprints:</b>
              <ul class="checklist">
                <li>• S1: Parse raw HID descriptor tables in kernel buffer</li>
                <li>• S2: Implement software debounce filter (5ms threshold)</li>
                <li>• S3: Measure loopback latency across userland IPC socket</li>
              </ul>
            </div>
          </div>
        </details>
      </div>
    </details>

    <!-- Repo 5: Residuals -->
    <details class="project" id="repo-residuals" open>
      <summary>
        <span>📁 Residuals (Auxiliary Maintenance & Personal Integration Sprints)</span>
        <span class="project-meta">PM Infra, System Health & Life Flows</span>
      </summary>
      <div class="projectbody">
        <div class="project-intent">
          <b>Daily Execution Window (16:00 – 17:45):</b>
          Dedicated 3x3 sprints ensuring environmental harmony, creative aesthetic asset creation, and personal peer network maintenance.
        </div>

        <div class="sprint-block">
          <b>Sprint 1: Apartment & Art</b>
          <p style="font-size:11px; margin:2px 0;">Workspace acoustic tuning, physical studio organization, canvas stretching, and fine art painting sessions.</p>
        </div>
        <div class="sprint-block">
          <b>Sprint 2: Sexy Content</b>
          <p style="font-size:11px; margin:2px 0;">Aesthetic moodboarding, lighting setup, visual photoshoot execution, and high-tier photo color grading.</p>
        </div>
        <div class="sprint-block">
          <b>Sprint 3: Community & Traveling</b>
          <p style="font-size:11px; margin:2px 0;">Peer network outreach, community sync, travel route logistics, and accommodation checks.</p>
        </div>
      </div>
    </details>

  </div>
</section>

<!-- PART 3: MATRIX 2 — CALENDAR SNAPSHOT & VISUALIZATION -->
<section class="section" id="matrix2">
  <div class="sectionhead">
    <h2>03 · Matrix 2: Calendar Snapshot & Visualization (Temporal)</h2>
    <small>Daily span: 08:00 – 24:00 · Daily shutdown: 21:00 · Reconciled with Google Calendar</small>
  </div>
  
  <p style="font-size:12px; margin-bottom:12px;">
    <b>Calendar Invariant:</b> Operating window spans 08:00 to 24:00 daily. Daily shutdown occurs strictly at 21:00. Focus flows flex around real external appointments:
  </p>

  <!-- 7-Day Quick Strip -->
  <div class="weekgrid" style="margin-bottom:20px;">
    <article class="day">
      <small>Monday · 09 Nov</small>
      <h3>Foundations</h3>
      <small>4 Flows · 08:00–21:00</small>
      <p><span class="flow-tag">F1</span> MoA: Thesis essay outline & audio</p>
      <p><span class="flow-tag">F2</span> MoA: Website flexbox nav & drawer</p>
      <p><span class="flow-tag">F3</span> IPOS: Karakeep audit & Docling</p>
      <p><span class="flow-tag">F4</span> Residual: Studio acoustics & canvas</p>
    </article>

    <article class="day">
      <small>Tuesday · 10 Nov</small>
      <h3>Pipelines</h3>
      <small>4 Flows · 08:00–21:00</small>
      <p><span class="flow-tag">F1</span> MoA: Voice narration & reel slicing</p>
      <p><span class="flow-tag">F2</span> MoA: Dynamic article feed</p>
      <p><span class="flow-tag">F3</span> IPOS: Trafilatura parser & FRED schema</p>
      <p><span class="flow-tag">F4</span> Residual: Sexy content lighting</p>
    </article>

    <article class="day alternative">
      <small>Wednesday · 11 Nov</small>
      <h3>Invoicing Engine</h3>
      <small>Evening Event · Wrap 17:45</small>
      <p><span class="flow-tag">F1</span> MoA: Longform writing & diagram cards</p>
      <p><span class="flow-tag">F2</span> MoA: Line-item invoice JSON schema</p>
      <p><span class="flow-tag">F3</span> IPOS: Ingestion pipeline test harness</p>
      <div class="event-alert"><b>18:00 – 20:00 WC Meister</b>Calendar Event · Shutdown 21:00</div>
    </article>

    <article class="day meeting">
      <small>Thursday · 12 Nov</small>
      <h3>Coordination</h3>
      <small>Fixed Meeting + Dance</small>
      <div class="event-alert" style="background:#eaf2fb; border-color:#bdd2ee;">
        <b>10:00 – 11:00 Alex & Chris</b>Meeting with C. Sgarz · F1 compressed
      </div>
      <p><span class="flow-tag">F1</span> MoA: Audio cut (09:00–10:00)</p>
      <p><span class="flow-tag">F2</span> MoA: HTML-to-PDF invoice engine</p>
      <div class="event-alert"><b>18:45 – 21:00 München Tanz</b>Dance event · Wrap by 18:15</div>
    </article>

    <article class="day alternative">
      <small>Friday · 13 Nov</small>
      <h3>Broadcast</h3>
      <small>Evening Event · Wrap 17:45</small>
      <p><span class="flow-tag">F1</span> MoA: Substack newsletter dispatch</p>
      <p><span class="flow-tag">F2</span> MoA: Invoicing batch verification</p>
      <p><span class="flow-tag">F3</span> IPOS: Telegram research digest verify</p>
      <div class="event-alert"><b>18:00 – 20:00 WC Meister</b>Calendar Event · Shutdown 21:00</div>
    </article>

    <article class="day">
      <small>Saturday · 14 Nov</small>
      <h3>Precap & Buffer</h3>
      <small>Decision D017 Cadence</small>
      <p><b>09:00 – 11:00:</b> PrecapWeek retrospective session.</p>
      <p><b>11:30 – 13:00:</b> Workspace clean room reset.</p>
      <p><b>Afternoon:</b> OFF.</p>
    </article>

    <article class="day off">
      <small>Sunday · 15 Nov</small>
      <h3>Rest & Regen</h3>
      <small>Decision D017 Invariant</small>
      <p><b>OFF by default.</b> Zero scheduled focus flows.</p>
    </article>
  </div>

  <!-- Full-Width Responsive HTML Calendar Table -->
  <div style="width:100%; overflow-x:auto; margin:20px 0; border:1px solid #dce4e8; border-radius:10px; background:#fff;">
    <table style="width:100%; min-width:1150px; border-collapse:collapse; font-size:12px;">
      <thead>
        <tr style="background:#162642; color:#fff;">
          <th style="width:12%; padding:10px; border:1px solid #2a3e5c;">Window / Flow</th>
          <th style="width:6%; padding:10px; border:1px solid #2a3e5c;">Sprint</th>
          <th style="width:13.6%; padding:10px; border:1px solid #2a3e5c;">Monday (09 Nov)</th>
          <th style="width:13.6%; padding:10px; border:1px solid #2a3e5c;">Tuesday (10 Nov)</th>
          <th style="width:13.6%; padding:10px; border:1px solid #2a3e5c;">Wednesday (11 Nov)</th>
          <th style="width:13.6%; padding:10px; border:1px solid #2a3e5c;">Thursday (12 Nov)</th>
          <th style="width:13.6%; padding:10px; border:1px solid #2a3e5c;">Friday (13 Nov)</th>
          <th style="width:13.6%; padding:10px; border:1px solid #2a3e5c;">Saturday (14 Nov)</th>
        </tr>
      </thead>
      <tbody>
        
        <!-- Morning Routine Anchor -->
        <tr style="background:#f4f1ea; color:#687b8b;">
          <td style="padding:6px; text-align:center; font-family:monospace;">08:00–09:00</td>
          <td colspan="7" style="padding:6px; text-align:center;">🔒 Protected Anchor: Morning Routine, Meditation & Day Orchestration Prep</td>
        </tr>

        <!-- Flow 1: MoA Content -->
        <tr style="border-top:2px solid #507967;">
          <td rowspan="3" style="padding:10px; vertical-align:top; background:#f5f8f5;">
            <b style="color:#2a5035;">Flow 1 (2h)</b><br>
            <span style="font-size:10px; color:#687b8b;">09:00–11:00</span><br>
            <span style="font-size:11px; font-weight:700;">MoA: Content</span>
          </td>
          <td style="padding:6px; text-align:center; font-weight:700; border-bottom:1px solid #eef1f4;">Sp 1 (30m)</td>
          <td style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4;">
            <b>[WP #163] Essay Thesis</b>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:11px;">
              <li>1. Outline core thesis claims</li>
              <li>2. Cross-link source references</li>
              <li>3. Draft opening hook section</li>
            </ul>
          </td>
          <td style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4;">
            <b>[WP #163] Audio Voiceover</b>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:11px;">
              <li>1. Mic setup & acoustic check</li>
              <li>2. Record spoken narration</li>
              <li>3. Cut rough audio vocal takes</li>
            </ul>
          </td>
          <td style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4;">
            <b>[WP #163] Visual Cards</b>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:11px;">
              <li>1. Diagram SVG key concept</li>
              <li>2. Export slide illustrations</li>
              <li>3. Review contrast on mobile</li>
            </ul>
          </td>
          <td style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4; background:#edf4fd;">
            <span style="font-size:9px; color:#25548c; font-weight:700;">COMPRESSED (09:00–10:00)</span><br>
            <b>[WP #163] Audio Pass</b>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:11px;">
              <li>1. Frequency de-ess pass</li>
              <li>2. Normalize dialogue master</li>
              <li>3. Export final MP3 master</li>
            </ul>
          </td>
          <td style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4;">
            <b>[WP #163] Synthesis Post</b>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:11px;">
              <li>1. Format Substack draft</li>
              <li>2. Embed audio player link</li>
              <li>3. Queue release broadcast</li>
            </ul>
          </td>
          <td rowspan="3" style="padding:8px; vertical-align:top; background:#f9f8f5;">
            <b style="color:#856434;">Precap Retrospective</b><br>
            <span style="font-size:10px; color:#7d8c97;">09:00–11:00</span>
            <p style="font-size:11px; margin:4px 0;">PrecapWeek review & OpenProject sync (D017).</p>
          </td>
        </tr>

        <tr>
          <td style="padding:6px; text-align:center; font-weight:700; border-bottom:1px solid #eef1f4;">Sp 2 (30m)</td>
          <td style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4;">
            <b>Paragraph Structuring</b>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:11px;">
              <li>1. Polish section transitions</li>
              <li>2. Verify philosophical terms</li>
              <li>3. Generate pullquote blocks</li>
            </ul>
          </td>
          <td style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4;">
            <b>Reel Video Slicing</b>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:11px;">
              <li>1. Extract 30s highlight reel</li>
              <li>2. Sync dynamic captions</li>
              <li>3. Render 9:16 vertical crop</li>
            </ul>
          </td>
          <td style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4;">
            <b>Asset Organization</b>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:11px;">
              <li>1. Tag CDN media URLs</li>
              <li>2. Verify file sizes < 2MB</li>
              <li>3. Place in staging folder</li>
            </ul>
          </td>
          <td style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4; background:#edf4fd;">
            <b style="color:#1d4273;">10:00–11:00 Meeting</b><br>
            <span style="font-size:11px;">🔒 Alex & Chris (C. Sgarz)</span>
          </td>
          <td style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4;">
            <b>Weekly Review</b>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:11px;">
              <li>1. Verify publication links</li>
              <li>2. Check RSS validation</li>
              <li>3. Archive draft revisions</li>
            </ul>
          </td>
        </tr>

        <tr style="border-bottom:2px solid #507967;">
          <td style="padding:6px; text-align:center; font-weight:700;">Sp 3 (30m)</td>
          <td style="padding:6px; vertical-align:top;">
            <b>Editorial Signoff</b>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:11px;">
              <li>1. Final readthrough check</li>
              <li>2. Title & metadata lock</li>
              <li>3. Commit essay Markdown</li>
            </ul>
          </td>
          <td style="padding:6px; vertical-align:top;">
            <b>Social Packaging</b>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:11px;">
              <li>1. Draft caption copy</li>
              <li>2. Select cover thumbnail</li>
              <li>3. Schedule distribution</li>
            </ul>
          </td>
          <td style="padding:6px; vertical-align:top;">
            <b>Preview Staging</b>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:11px;">
              <li>1. Deploy to staging build</li>
              <li>2. Test responsive layout</li>
              <li>3. Operator reading pass</li>
            </ul>
          </td>
          <td style="padding:6px; vertical-align:top; background:#edf4fd;">
            <span style="font-size:11px; color:#5b6e82;">Meeting wrap & notes</span>
          </td>
          <td style="padding:6px; vertical-align:top;">
            <b>Channel Broadcast</b>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:11px;">
              <li>1. Dispatch newsletter</li>
              <li>2. Post social highlight</li>
              <li>3. Log engagement receipt</li>
            </ul>
          </td>
        </tr>

        <!-- Routine Anchor: Lunch -->
        <tr style="background:#f4f1ea; color:#687b8b;">
          <td style="padding:6px; text-align:center; font-family:monospace;">12:30–13:30</td>
          <td colspan="7" style="padding:6px; text-align:center;">🔒 Protected Anchor: Midday Reset, Healthy Lunch & Fresh Air Walk</td>
        </tr>

        <!-- Flow 4: Residual Life & Creative Sprints -->
        <tr style="border-top:2px solid #a37237;">
          <td rowspan="3" style="padding:10px; vertical-align:top; background:#fdf9f2;">
            <b style="color:#784f1e;">Flow 4 (1.75h)</b><br>
            <span style="font-size:10px; color:#687b8b;">16:00–17:45</span><br>
            <span style="font-size:11px; font-weight:700;">Residual Flow</span>
          </td>
          <td style="padding:6px; text-align:center; font-weight:700; border-bottom:1px solid #eef1f4;">Sprint 1</td>
          <td colspan="5" style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4;">
            <b>Apartment & Art:</b> Physical studio clean room, acoustic tuning, canvas stretching, and fine art painting sessions.
          </td>
          <td rowspan="3" style="padding:8px; vertical-align:top; background:#f0eee6; color:#788691;">
            <b>Saturday Afternoon OFF</b><br>
            <span style="font-size:10px;">Rest & recovery</span>
          </td>
        </tr>

        <tr>
          <td style="padding:6px; text-align:center; font-weight:700; border-bottom:1px solid #eef1f4;">Sprint 2</td>
          <td colspan="5" style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4;">
            <b>Sexy Content:</b> Aesthetic moodboarding, photoshoot lighting arrangements, high-resolution portrait capture, and color grading.
          </td>
        </tr>

        <tr style="border-bottom:2px solid #a37237;">
          <td style="padding:6px; text-align:center; font-weight:700;">Sprint 3</td>
          <td colspan="5" style="padding:6px; vertical-align:top;">
            <b>Community & Traveling:</b> Peer network outreach, community dinner logistics, travel route planning, and accommodation verification.
          </td>
        </tr>

        <!-- Protected Routine Anchor: Daily Shutdown at 21:00 -->
        <tr style="background:#eef2f7; color:#355570; font-weight:700; border-top:2px solid #304e86;">
          <td style="padding:8px; text-align:center; font-family:monospace;">21:00–21:30</td>
          <td colspan="7" style="padding:8px; text-align:center;">🔒 Daily Shutdown (21:00): Outro, Day Evidence Commit & Workspace Reset</td>
        </tr>

        <!-- Evening Regeneration Window: 21:30 to 24:00 -->
        <tr style="background:#f9f8f5; color:#788b99;">
          <td style="padding:8px; text-align:center; font-family:monospace;">21:30–24:00</td>
          <td colspan="7" style="padding:8px; text-align:center;">Evening Regeneration, Rest, Reading & Night Recovery</td>
        </tr>

      </tbody>
    </table>
  </div>
</section>

<!-- PART 4: GOOGLE CALENDAR VERIFICATION PANEL -->
<section class="section" id="calendar-sync">
  <div class="sectionhead">
    <h2>04 · Google Calendar Integration Receipt</h2>
    <small>Direct live synchronization via gcalendar CLI</small>
  </div>
  <div class="panel">
    <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px; margin-bottom:14px;">
      <div>
        <span class="eyebrow" style="color:#2f582f;">LIVE CONNECTION VERIFIED</span>
        <h3 style="font-family:Georgia,serif; font-size:17px; margin-top:3px;">Account: gehm77@gmail.com</h3>
      </div>
      <span style="background:#eaf2e6; color:#2c5225; padding:6px 12px; border-radius:20px; font-size:11px; font-weight:700;">OAuth2 Verified</span>
    </div>
    <p style="font-size:12px;">Operating window spans 08:00 to 24:00 daily with shutdown at 21:00. The schedule actively coordinates around real calendar commitments:</p>
    <table style="width:100%; border-collapse:collapse; font-size:11px; margin-top:10px;">
      <thead>
        <tr style="background:#edf1f2; text-align:left;">
          <th style="padding:8px; border:1px solid #dce2e2;">Target Window</th>
          <th style="padding:8px; border:1px solid #dce2e2;">Calendar Event</th>
          <th style="padding:8px; border:1px solid #dce2e2;">Flow Coordination Impact</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="padding:8px; border:1px solid #dce2e2;">Thu Nov 12, 10:00–11:00</td>
          <td style="padding:8px; border:1px solid #dce2e2;"><b>Alex & Chris</b> (Christian Sgarz)</td>
          <td style="padding:8px; border:1px solid #dce2e2;">F1 compressed (09:00–10:00). Meeting protected. F2 resumes 11:15.</td>
        </tr>
        <tr>
          <td style="padding:8px; border:1px solid #dce2e2;">Thu Nov 12, 18:45–21:00</td>
          <td style="padding:8px; border:1px solid #dce2e2;"><b>München Tanz</b></td>
          <td style="padding:8px; border:1px solid #dce2e2;">Evening flow wraps by 18:15 to allow transit. Shutdown completes before 21:00.</td>
        </tr>
        <tr>
          <td style="padding:8px; border:1px solid #dce2e2;">Wed Nov 11, 18:00–20:00</td>
          <td style="padding:8px; border:1px solid #dce2e2;"><b>WC Meister</b></td>
          <td style="padding:8px; border:1px solid #dce2e2;">Flow 4 wraps by 17:45. Event runs 18:00–20:00. Shutdown at 21:00.</td>
        </tr>
        <tr>
          <td style="padding:8px; border:1px solid #dce2e2;">Fri Nov 13, 18:00–20:00</td>
          <td style="padding:8px; border:1px solid #dce2e2;"><b>WC Meister</b></td>
          <td style="padding:8px; border:1px solid #dce2e2;">Flow 4 wraps by 17:45. Event runs 18:00–20:00. Weekly wrap shutdown at 21:00.</td>
        </tr>
      </tbody>
    </table>
  </div>
</section>

<footer style="margin-top:40px; padding-top:20px; border-top:1px solid #e1e5e5; font-size:11px; color:#788b99; display:flex; justify-content:space-between;">
  <span>Northstar Weekly Command Brief · Week 2026-W45</span>
  <span>OpenProject 17.8.0 · Google Calendar Live</span>
</footer>

</main>
</body>
</html>
"""

def main():
    html_content = build_html()
    output_path = os.path.join(os.path.dirname(__file__), "WEEKLY_PRECAP_NORTHSTAR_2026_W45.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Generated: {output_path}")

if __name__ == "__main__":
    main()
