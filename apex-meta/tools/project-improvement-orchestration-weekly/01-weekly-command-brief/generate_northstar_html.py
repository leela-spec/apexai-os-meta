#!/usr/bin/env python3
"""
generate_northstar_html.py
Generates the canonical Precap Week HTML for Week 2026-W45.
Conforms strictly to SPEC-PRECAP-WEEK-ITERATIONS-v1.2:
- Header: Title 'Precap Week · 09 – 15 November 2026' with high-density stats.
- Part 1: Operator Decision Brief (Flow organization, 3x3 standard, Meister meetings declined).
- Part 2: Matrix 1 — Project Overview & Critical Path (Stacked 1-column layout, 3-level decomposition, NO SPRINTS).
  Repos: Master of Arts, Leela (Skill Tree ONLY), IPOS (Pipeline Recheck), Apex OS, Residuals.
- Part 3: Matrix 2 — Calendar Snapshot & Visualization (All 4 flows, 08:00–24:00, Shutdown 21:00, 3 items/sprint).
- No Google Calendar integration receipt.
"""

import os

def build_html():
    return """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Precap Week · 09 – 15 November 2026</title>
<style>
*{box-sizing:border-box}
html{scroll-behavior:smooth;overflow-wrap:anywhere}
body{margin:0;background:#f8f6ef;color:#172a3d;font:14px/1.55 system-ui,Segoe UI,Arial}
main{max-width:1480px;margin:auto;padding:26px 32px 60px}

/* Typography */
h1{font:clamp(32px,3.8vw,50px)/1.1 Georgia,serif;letter-spacing:-1.2px;margin:12px 0 6px}
h2{font-size:22px;margin:0;font-family:Georgia,serif;letter-spacing:-0.5px}
h3{font-size:15px;margin:0}
p{margin:8px 0;color:#687b8b}
a{color:#315c7f;text-decoration:none}
a:hover{text-decoration:underline}
button,input,select{font:inherit}
button,summary{cursor:pointer}
button,a,input,select{touch-action:manipulation}
:focus-visible{outline:3px solid #a2b881;outline-offset:3px}

/* Header & Top Bar */
.top-header{display:flex;justify-content:space-between;align-items:flex-end;border-bottom:1px solid #e2e6e2;padding-bottom:18px;margin-bottom:20px;flex-wrap:wrap;gap:20px}
.precap-title-block{max-width:700px}
.eyebrow{text-transform:uppercase;letter-spacing:1.8px;font-size:10px;color:#698095;font-weight:750}
.precap-date{font:20px Georgia,serif;color:#355570;margin-top:2px}

/* Portfolio Statistics Strap */
.stats-strap{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:10px;min-width:620px}
.stat-card{background:#fffdf8;border:1px solid #dfe3de;border-radius:10px;padding:12px;text-align:center}
.stat-card b{display:block;font:26px Georgia;color:#162642;line-height:1.1}
.stat-card span{color:#718491;font-size:10px;text-transform:uppercase;font-weight:600;letter-spacing:0.5px}

.source-note{font-size:11px;background:#f2eee3;border-left:3px solid #b7a472;padding:11px 14px;border-radius:0 8px 8px 0;margin:15px 0}

/* Sticky Navigation Tabs */
.tabs{display:flex;gap:9px;flex-wrap:wrap;position:sticky;top:0;background:#f8f6eff2;backdrop-filter:blur(8px);padding:12px 0;z-index:10;border-bottom:1px solid #e4e3d9;margin-top:15px}
.tabs a{padding:7px 14px;font-weight:650;font-size:12px;background:#fff;border:1px solid #dce1df;border-radius:7px;color:#355570}
.tabs a:hover{background:#edf2f5}

/* Sections */
.section{margin-top:40px;scroll-margin-top:80px}
.sectionhead{display:flex;align-items:baseline;justify-content:space-between;gap:20px;margin-bottom:14px}
.sectionhead small{color:#7a8993}
.panel{background:#fffdf8;border:1px solid #dde2dd;border-radius:13px;padding:22px;min-width:0;overflow:hidden}

/* Decision Cards */
.decisions-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;margin-top:10px}
.decision-card{border:1px solid #dce4e8;border-radius:10px;padding:16px;background:#fff}
.decision-card b{font-size:14px;color:#162642;display:block;margin:4px 0}
.decision-badge{padding:3px 8px;border-radius:5px;font-size:10px;font-weight:700;display:inline-block;margin-top:8px}

/* Matrix 1: Stacked 1-Column Layout */
.project-stack{display:flex;flex-direction:column;gap:18px}
details.project{border:1px solid #dce2e2;border-radius:12px;background:#fffdf9;box-shadow:0 3px 12px #10263608;overflow:hidden;width:100%}
details.project>summary{padding:18px 20px;font-weight:700;font-size:16px;background:#fff;border-bottom:1px solid #edf1f2;display:flex;align-items:center;justify-content:space-between;cursor:pointer}
details.project>summary:before{content:'▸';margin-right:10px;color:#788b99;font-size:14px}
details.project[open]>summary:before{content:'▾'}
.project-meta{font-size:11px;font-weight:400;color:#7d8c97;padding:3px 9px;border-radius:12px;background:#f2f5f7}
.projectbody{padding:20px}

/* Three-Level Project Decomposition */
.level-banner{border-radius:8px;padding:12px 14px;margin-bottom:14px}
.level-banner.l1{background:#f6f9f6;border-left:4px solid #507967}
.level-banner.l1 b{color:#2a5035;font-size:13px;display:block;margin-bottom:3px}
.level-banner.l1 p{font-size:12px;color:#546677;margin:0}

/* Level 2: Visual Process & Output Pipeline Flow */
.pipeline-flow{display:flex;align-items:center;gap:8px;margin:16px 0;overflow-x:auto;padding:8px 0}
.pipeline-step{background:#fff;border:1px solid #dce4e8;border-radius:8px;padding:10px 14px;min-width:180px;box-shadow:0 2px 6px #10263606}
.pipeline-step.critical{border-color:#e0ad77;background:#fdfcf9;border-left:4px solid #b08445}
.pipeline-step small{display:block;font-size:9px;text-transform:uppercase;font-weight:700;color:#788b99;margin-bottom:2px}
.pipeline-step b{font-size:12px;color:#162642;display:block}
.pipeline-step span{font-size:10px;color:#5c6f80}
.pipeline-arrow{font-size:18px;color:#a0b0bd;font-weight:bold;flex-shrink:0}

/* Level 3: Detail Tasks & Completion Evidence (NO SPRINTS) */
.task-deck{margin-top:14px}
details.task-card{border:1px solid #e1e6e8;border-radius:8px;margin:8px 0;background:#fff}
details.task-card>summary{padding:12px 14px;font-size:13px;font-weight:600;display:flex;align-items:center;gap:10px;cursor:pointer}
details.task-card>summary:before{content:'▸';color:#90a0ab}
details.task-card[open]>summary:before{content:'▾'}
.state-icon{display:inline-grid;place-items:center;width:20px;height:20px;border-radius:5px;font-size:11px;font-weight:700}
.state-icon.new{background:#edf2f5;color:#4d6d85}
.state-icon.progress{background:#dcf2e3;color:#256338}
.state-icon.spec{background:#f1e8f7;color:#6b3b87}
.state-icon.critical{background:#feece8;color:#9e3424}
.task-title{flex:1;color:#182b3d}
.task-badge{font-size:9px;font-weight:700;padding:2px 6px;border-radius:4px;background:#f0f3f5;color:#657788}
.task-body{padding:14px 16px;font-size:12px;border-top:1px solid #f0f3f4;background:#fcfdfd}
.evidence-block{margin:8px 0;padding:8px 10px;background:#f8fafc;border:1px solid #e2e8f0;border-radius:6px}
.evidence-block b{color:#355570;font-size:11px;display:block;margin-bottom:3px}
.checklist{margin:0;padding-left:18px;color:#506272;font-size:11px}
.checklist li{margin:3px 0}

/* Matrix 2: Calendar Visualization */
.weekgrid{display:grid;grid-template-columns:repeat(7,minmax(0,1fr));gap:10px;margin-bottom:20px}
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

@media(max-width:1150px){
  .stats-strap{grid-template-columns:repeat(3,minmax(0,1fr));min-width:0}
  .weekgrid{grid-template-columns:repeat(4,minmax(0,1fr))}
  .decisions-grid{grid-template-columns:1fr}
}
@media(max-width:650px){
  main{padding:16px 12px 40px}
  .stats-strap{grid-template-columns:repeat(2,minmax(0,1fr))}
  .weekgrid{grid-template-columns:repeat(2,minmax(0,1fr))}
  .day.off{grid-column:1/-1}
  .top-header{flex-direction:column;align-items:flex-start}
}
</style>
</head>
<body>
<main>

<!-- TOP HEADER -->
<div class="top-header">
  <div class="precap-title-block">
    <div class="eyebrow">Weekly Orchestration Brief · ISO Week 45</div>
    <h1>Precap Week</h1>
    <div class="precap-date">09 – 15 November 2026</div>
    <p>Operational direction, non-temporal project development flows, and calibrated calendar execution.</p>
  </div>
  <div class="stats-strap">
    <div class="stat-card">
      <b>38.5h</b>
      <span>Planned Focus</span>
    </div>
    <div class="stat-card">
      <b>24</b>
      <span>Flow Blocks</span>
    </div>
    <div class="stat-card">
      <b>72</b>
      <span>3x3 Sprints</span>
    </div>
    <div class="stat-card">
      <b>07</b>
      <span>Videos Due</span>
    </div>
    <div class="stat-card">
      <b>05</b>
      <span>Repositories</span>
    </div>
  </div>
</div>

<p class="source-note">
  <b>Operator State for Week 45:</b> OpenProject scanning provides the candidate task intake. The operator has explicitly structured the week into 4 daily flows (3x3 standard), declined external Meister evening meetings to protect build capacity, and focused Leela exclusively on the Skill Tree.
</p>

<!-- STICKY NAVIGATION TABS -->
<nav class="tabs">
  <a href="#brief">01 · Operator Decision Brief</a>
  <a href="#matrix1">02 · Matrix 1: Project Overview & Critical Path</a>
  <a href="#matrix2">03 · Matrix 2: Calendar Snapshot & Visualization</a>
</nav>

<!-- PART 1: OPERATOR DECISION BRIEF -->
<section class="section" id="brief">
  <div class="sectionhead">
    <h2>01 · Operator Decision Brief</h2>
    <small>Governance choices, flow allocations & calendar overrides for Week 45</small>
  </div>
  <div class="panel">
    <div class="decisions-grid">
      
      <!-- Decision 1: Flow Organization -->
      <div class="decision-card">
        <span class="eyebrow" style="color:#507967;">[P0 | I98/E95/R05] Operating Flow Architecture</span>
        <b>D-W45-01: 4-Flow Operating Structure & 3x3 Standard</b>
        <p style="font-size:11px;"><b>Context:</b> Need balanced progression across creative content, sovereign finance, system tools, and life integration.</p>
        <p style="font-size:11px;"><b>Resolution:</b> Schedulable days execute 4 flows: Flows 1 & 2 for Master of Arts (Content week 7 videos, Website content draft, Business invoicing), Flow 3 for Investment/IPOS, and Flow 4 for Residuals (Apartment & Studio Art, Sexy Content, Community & Travel). Sequencing serves as the integration meta-system.</p>
        <span class="decision-badge" style="background:#dcf2e3; color:#18572e;">CONFIRMED OPERATOR DIRECTIVE</span>
      </div>

      <!-- Decision 2: Meeting Overrides -->
      <div class="decision-card">
        <span class="eyebrow" style="color:#a84332;">[P0 | I92/E85/R10] Calendar Interventions</span>
        <b>D-W45-02: Decline Meister Meetings & Protect Evening Capacity</b>
        <p style="font-size:11px;"><b>Context:</b> Google Calendar contains external Meister meetings on Wednesday (18:00–20:00) and Friday (18:00–20:00).</p>
        <p style="font-size:11px;"><b>Resolution:</b> Operator explicitly declines and ignores all Meister and Meso meetings for Week 45, preserving evening flow capacity. Active protected commitments remain: <i>Alex & Chris</i> (Thu 10:00–11:00) and <i>München Tanz</i> (Thu 18:45–21:00).</p>
        <span class="decision-badge" style="background:#feece8; color:#9e3424;">MEISTER MEETINGS DECLINED</span>
      </div>

      <!-- Decision 3: Leela Scope Bounding -->
      <div class="decision-card">
        <span class="eyebrow" style="color:#355570;">[P1 | I90/E40/R10] Leela Project Boundary</span>
        <b>D-W45-03: Focus Leela Exclusively on Skill Tree</b>
        <p style="font-size:11px;"><b>Context:</b> Multitasking across Path progression and Sequencing domain engine scatters build attention.</p>
        <p style="font-size:11px;"><b>Resolution:</b> Pause Path and Sequencing feature development for Week 45. Dedicate all Leela attention to solidifying spatial node hierarchy contracts, Chunk library identity, and durable placement.</p>
        <span class="decision-badge" style="background:#eaf2fb; color:#224672;">SKILL TREE EXCLUSIVE</span>
      </div>

      <!-- Decision 4: IPOS Pipeline Recheck -->
      <div class="decision-card">
        <span class="eyebrow" style="color:#b08445;">[P1 | I94/E50/R15] Sovereign Financial Infrastructure</span>
        <b>D-W45-04: Full IPOS Pipeline Recheck & Data Viz Over Time</b>
        <p style="font-size:11px;"><b>Context:</b> Ingestion pipeline needs structural audit against external possibilities and clean temporal data display.</p>
        <p style="font-size:11px;"><b>Resolution:</b> Conduct a thorough architectural recheck of the entire IPOS ingestion chain, modularize adapters, and establish a sovereign engine for visualizing financial data over time.</p>
        <span class="decision-badge" style="background:#fef3dd; color:#856434;">PIPELINE RECHECK AUTHORIZED</span>
      </div>

    </div>
  </div>
</section>

<!-- PART 2: MATRIX 1 — PROJECT OVERVIEW & CRITICAL PATH -->
<section class="section" id="matrix1">
  <div class="sectionhead">
    <h2>02 · Matrix 1: Project Overview & Critical Path (Non-Temporal)</h2>
    <small>Three-level output decomposition across the 5 repositories · Single stacked column · Zero sprints</small>
  </div>

  <div class="project-stack">

    <!-- REPO 1: MASTER OF ARTS -->
    <details class="project" id="repo-moa" open>
      <summary>
        <span>📁 1. Master of Arts (Website, Content Week & Invoicing)</span>
        <span class="project-meta">OP #14, #6, #7 · High Leverage</span>
      </summary>
      <div class="projectbody">
        
        <!-- Level 1: High Level -->
        <div class="level-banner l1">
          <b>Level 1 (High Level Strategic Outcome):</b>
          <p>Deliver the <b>Content Week Milestone</b>: produce 7 completed videos, finalize the public website content draft with responsive navigation, and deploy the validated line-item invoicing calculation engine with automated PDF billing.</p>
        </div>

        <!-- Level 2: Mid Level Visual Process Pipeline -->
        <div class="eyebrow" style="margin-top:14px;">Level 2: Process & Output Flow Pipeline</div>
        <div class="pipeline-flow">
          <div class="pipeline-step">
            <small>Current Baseline</small>
            <b>Static Draft & Notes</b>
            <span>Unpublished essays, raw scripts</span>
          </div>
          <div class="pipeline-arrow">➔</div>
          <div class="pipeline-step critical">
            <small>Output A · Critical Path</small>
            <b>Website Content Draft</b>
            <span>Flexbox nav & reading drawer</span>
          </div>
          <div class="pipeline-arrow">➔</div>
          <div class="pipeline-step critical">
            <small>Output B · Critical Path</small>
            <b>7 Produced Videos</b>
            <span>Scripted, voiced, captioned reels</span>
          </div>
          <div class="pipeline-arrow">➔</div>
          <div class="pipeline-step critical">
            <small>Output C · Critical Path</small>
            <b>Automated PDF Billing</b>
            <span>Line-item schema & print engine</span>
          </div>
          <div class="pipeline-arrow">➔</div>
          <div class="pipeline-step">
            <small>Final Milestone</small>
            <b>Public Channel Launch</b>
            <span>Live site, videos out, receipts</span>
          </div>
        </div>

        <!-- Level 3: Detail Tasks (NO SPRINTS) -->
        <div class="eyebrow" style="margin-top:14px;">Level 3: Concrete Work Packages & Completion Evidence</div>
        <div class="task-deck">
          
          <details class="task-card" open>
            <summary>
              <span class="state-icon critical">★</span>
              <span class="task-title">WP #163 Website Content Draft & Responsive Layout</span>
              <span class="task-badge">CRITICAL PATH</span>
            </summary>
            <div class="task-body">
              <p><b>Description:</b> Author and stage public website content drafts; implement CSS flexbox header navigation and mobile drawer menu for essay reading.</p>
              <div class="evidence-block">
                <b>Completion Evidence:</b>
                <ul class="checklist">
                  <li>• Staged Markdown content files verified in reading routes</li>
                  <li>• Responsive navbar flexbox styles and mobile drawer animation</li>
                  <li>• Zero layout shift across desktop and mobile Chrome/Safari passes</li>
                </ul>
              </div>
              <p style="font-size:11px; color:#687b8b; margin-top:4px;"><b>Unblocks:</b> Public audience release and embedded video player routing.</p>
            </div>
          </details>

          <details class="task-card" open>
            <summary>
              <span class="state-icon critical">★</span>
              <span class="task-title">Content Production Week: 7 Mastered Videos</span>
              <span class="task-badge">CRITICAL PATH</span>
            </summary>
            <div class="task-body">
              <p><b>Description:</b> Systematic production pass authoring, recording, and editing 7 intellectual video reels for cross-platform distribution.</p>
              <div class="evidence-block">
                <b>Completion Evidence:</b>
                <ul class="checklist">
                  <li>• 7 authored scripts with core thesis outlines</li>
                  <li>• 7 clean spoken-word voiceover tracks with frequency normalization</li>
                  <li>• 7 final rendered 9:16 vertical video files with dynamic captions</li>
                </ul>
              </div>
            </div>
          </details>

          <details class="task-card" open>
            <summary>
              <span class="state-icon critical">★</span>
              <span class="task-title">WP-BIZ-01 Line-Item Invoicing Engine & Automated PDF Billing</span>
              <span class="task-badge">CRITICAL PATH</span>
            </summary>
            <div class="task-body">
              <p><b>Description:</b> Establish schema-backed line-item billing calculations, tax formulas, and automated HTML-to-PDF print generation.</p>
              <div class="evidence-block">
                <b>Completion Evidence:</b>
                <ul class="checklist">
                  <li>• JSON Schema defining line items, VAT, and client metadata</li>
                  <li>• Unit test suite validating subtotal and tax calculation formulas</li>
                  <li>• Headless PDF generation producing pixel-perfect client invoice receipts</li>
                </ul>
              </div>
            </div>
          </details>

        </div>
      </div>
    </details>

    <!-- REPO 2: LEELA -->
    <details class="project" id="repo-leela" open>
      <summary>
        <span>📁 2. Leela (Skill Tree ONLY · Path & Sequencing Paused)</span>
        <span class="project-meta">OP #10 · Core Architecture</span>
      </summary>
      <div class="projectbody">
        
        <div class="level-banner l1" style="background:#f0f5fa; border-left-color:#355570;">
          <b style="color:#1d3859;">Level 1 (High Level Strategic Outcome):</b>
          <p>Solidify and freeze <b>Skill Tree spatial node contracts</b> and durable placement identity. Path and Sequencing development are explicitly paused to prevent architecture churn.</p>
        </div>

        <div class="eyebrow" style="margin-top:14px;">Level 2: Process & Output Flow Pipeline</div>
        <div class="pipeline-flow">
          <div class="pipeline-step">
            <small>Current Baseline</small>
            <b>Pure Projection Adapter</b>
            <span>Transient renderer nodes</span>
          </div>
          <div class="pipeline-arrow">➔</div>
          <div class="pipeline-step critical">
            <small>Output A · Critical Path</small>
            <b>Canonical Chunk Identity</b>
            <span>Chunk library schema (#159)</span>
          </div>
          <div class="pipeline-arrow">➔</div>
          <div class="pipeline-step critical">
            <small>Output B · Critical Path</small>
            <b>Durable Placement ID</b>
            <span>Epic/Block placement contracts</span>
          </div>
          <div class="pipeline-arrow">➔</div>
          <div class="pipeline-step">
            <small>Final Milestone</small>
            <b>Skill Tree Contract Freeze</b>
            <span>Verified immutable node schema</span>
          </div>
        </div>

        <div class="eyebrow" style="margin-top:14px;">Level 3: Concrete Work Packages & Completion Evidence</div>
        <div class="task-deck">
          <details class="task-card" open>
            <summary>
              <span class="state-icon critical">★</span>
              <span class="task-title">WP #159 & #188 Canonical Chunk Identity & Durable Epic Placement</span>
              <span class="task-badge">CRITICAL PATH</span>
            </summary>
            <div class="task-body">
              <p><b>Description:</b> Decouple spatial renderer IDs from canonical chunk identity; establish durable placement IDs without leaking transient nodes.</p>
              <div class="evidence-block">
                <b>Completion Evidence:</b>
                <ul class="checklist">
                  <li>• SpatialViewNode contract separating local rendererId from canonicalContentId</li>
                  <li>• Unit tests verifying multi-placement of canonical chunks without state bleed</li>
                  <li>• Materialization validator clears STF-01 and STF-23 cleanly</li>
                </ul>
              </div>
            </div>
          </details>
        </div>

      </div>
    </details>

    <!-- REPO 3: INVESTMENT / IPOS -->
    <details class="project" id="repo-ipos" open>
      <summary>
        <span>📁 3. Investment / IPOS (Full Pipeline Recheck & Data Viz Over Time)</span>
        <span class="project-meta">OP #16 · Sovereign Finance</span>
      </summary>
      <div class="projectbody">
        
        <div class="level-banner l1" style="background:#fdf9f2; border-left-color:#b08445;">
          <b style="color:#784f1e;">Level 1 (High Level Strategic Outcome):</b>
          <p>Conduct a <b>complete architectural recheck of the entire ingestion pipeline</b>, evaluate external ingestion tooling, and modularize a sovereign engine for <b>visualizing financial data over time</b>.</p>
        </div>

        <div class="eyebrow" style="margin-top:14px;">Level 2: Process & Output Flow Pipeline</div>
        <div class="pipeline-flow">
          <div class="pipeline-step">
            <small>Current Baseline</small>
            <b>Mixed Mocks & Scripts</b>
            <span>Legacy Karakeep code debt</span>
          </div>
          <div class="pipeline-arrow">➔</div>
          <div class="pipeline-step critical">
            <small>Output A · Critical Path</small>
            <b>Full Pipeline Audit</b>
            <span>Retire legacy, modularize seams</span>
          </div>
          <div class="pipeline-arrow">➔</div>
          <div class="pipeline-step critical">
            <small>Output B · Critical Path</small>
            <b>External Intake Seam</b>
            <span>Docling & Trafilatura adapters</span>
          </div>
          <div class="pipeline-arrow">➔</div>
          <div class="pipeline-step critical">
            <small>Output C · Critical Path</small>
            <b>Data Viz Over Time</b>
            <span>Time-series chart component</span>
          </div>
          <div class="pipeline-arrow">➔</div>
          <div class="pipeline-step">
            <small>Final Milestone</small>
            <b>Cockpit Intelligence</b>
            <span>Interactive multi-tier dashboard</span>
          </div>
        </div>

        <div class="eyebrow" style="margin-top:14px;">Level 3: Concrete Work Packages & Completion Evidence</div>
        <div class="task-deck">
          <details class="task-card" open>
            <summary>
              <span class="state-icon critical">★</span>
              <span class="task-title">WP #224 & #228 Full Ingestion Pipeline Recheck & Seam Audit</span>
              <span class="task-badge">CRITICAL PATH</span>
            </summary>
            <div class="task-body">
              <p><b>Description:</b> Audit working assets in <code>ipos/ingest/</code>, retire obsolete Karakeep dependencies (ADR-003), and specify modular ingestion boundaries.</p>
              <div class="evidence-block">
                <b>Completion Evidence:</b>
                <ul class="checklist">
                  <li>• Formal ADR-003 record locked in repository</li>
                  <li>• Clean import trace with zero references to legacy mock classes</li>
                  <li>• Benchmark report comparing native Python cron vs external container performance</li>
                </ul>
              </div>
            </div>
          </details>

          <details class="task-card" open>
            <summary>
              <span class="state-icon critical">★</span>
              <span class="task-title">WP #232 Sovereign Data Visualization Over Time</span>
              <span class="task-badge">CRITICAL PATH</span>
            </summary>
            <div class="task-body">
              <p><b>Description:</b> Design and implement modular charting primitives for visualizing economic metrics and portfolio valuation trends across customizable time horizons.</p>
              <div class="evidence-block">
                <b>Completion Evidence:</b>
                <ul class="checklist">
                  <li>• Modular time-series component accepting sovereign JSON fixtures</li>
                  <li>• Interactive date range sliders and zoomable metric axes</li>
                  <li>• Multi-tier cockpit view rendering historical financial data without third-party cloud lock-in</li>
                </ul>
              </div>
            </div>
          </details>
        </div>

      </div>
    </details>

    <!-- REPO 4: APEX OS -->
    <details class="project" id="repo-apex" open>
      <summary>
        <span>📁 4. Apex OS (OpenMouse, Mindful Repo & Dark Factory)</span>
        <span class="project-meta">OP #8 · Standalone Systems Project</span>
      </summary>
      <div class="projectbody">
        
        <div class="level-banner l1" style="background:#f5eefb; border-left-color:#785890;">
          <b style="color:#592f75;">Level 1 (High Level Strategic Outcome):</b>
          <p>Establish low-latency <b>OpenMouse hardware input bindings</b>, enforce <b>mindful repository orchestration</b> across agent sessions, and integrate the <b>dark factory automated deployment pipeline</b>.</p>
        </div>

        <div class="eyebrow" style="margin-top:14px;">Level 2: Process & Output Flow Pipeline</div>
        <div class="pipeline-flow">
          <div class="pipeline-step">
            <small>Current Baseline</small>
            <b>Raw Device Tables</b>
            <span>Unbound HID interrupt hooks</span>
          </div>
          <div class="pipeline-arrow">➔</div>
          <div class="pipeline-step critical">
            <small>Output A · Critical Path</small>
            <b>Kernel HID Polling Hook</b>
            <span>Low-level event driver listener</span>
          </div>
          <div class="pipeline-arrow">➔</div>
          <div class="pipeline-step critical">
            <small>Output B · Critical Path</small>
            <b>Mindful Orchestration</b>
            <span>Repo isolation & anti-drift gate</span>
          </div>
          <div class="pipeline-arrow">➔</div>
          <div class="pipeline-step">
            <small>Final Milestone</small>
            <b>Dark Factory Integration</b>
            <span>Autonomous test & build pipeline</span>
          </div>
        </div>

        <div class="eyebrow" style="margin-top:14px;">Level 3: Concrete Work Packages & Completion Evidence</div>
        <div class="task-deck">
          <details class="task-card" open>
            <summary>
              <span class="state-icon critical">★</span>
              <span class="task-title">WP-APEX-01 OpenMouse Kernel Driver Hooks & Interceptor</span>
              <span class="task-badge">CRITICAL PATH</span>
            </summary>
            <div class="task-body">
              <p><b>Description:</b> Implement kernel USB HID polling routines, button press/hold state machine, and userland IPC event streaming.</p>
              <div class="evidence-block">
                <b>Completion Evidence:</b>
                <ul class="checklist">
                  <li>• Raw HID parser reading button bitmasks with zero buffer drop</li>
                  <li>• 5ms debounce filter verified in unit loopback tests</li>
                  <li>• Mindful repo boundary check preventing cross-environment leakage</li>
                </ul>
              </div>
            </div>
          </details>
        </div>

      </div>
    </details>

    <!-- REPO 5: RESIDUALS -->
    <details class="project" id="repo-residuals" open>
      <summary>
        <span>📁 5. Residuals (Studio Art, Sexy Content, Community & Logistics)</span>
        <span class="project-meta">Personal & Life Integration Standard</span>
      </summary>
      <div class="projectbody">
        
        <div class="level-banner l1" style="background:#f9f5f0; border-left-color:#806655;">
          <b style="color:#684f3e;">Level 1 (High Level Strategic Outcome):</b>
          <p>Protect environmental harmony and personal momentum via dedicated daily 3x3 sprints: <b>Apartment & Studio Art</b>, <b>Sexy Content creation</b>, and <b>Community & Travel logistics</b>.</p>
        </div>

        <div class="eyebrow" style="margin-top:14px;">Level 2: Process & Output Flow Pipeline</div>
        <div class="pipeline-flow">
          <div class="pipeline-step">
            <small>Sprint 1 Output</small>
            <b>Studio Fine Art</b>
            <span>Acoustics & stretched canvases</span>
          </div>
          <div class="pipeline-arrow">➔</div>
          <div class="pipeline-step">
            <small>Sprint 2 Output</small>
            <b>Sexy Content Visuals</b>
            <span>Lighting, shoot, color grading</span>
          </div>
          <div class="pipeline-arrow">➔</div>
          <div class="pipeline-step">
            <small>Sprint 3 Output</small>
            <b>Travel & Community</b>
            <span>Peer outreach, route logistics</span>
          </div>
          <div class="pipeline-arrow">➔</div>
          <div class="pipeline-step">
            <small>Final Milestone</small>
            <b>Environmental Reset</b>
            <span>Harmonious workspace & life balance</span>
          </div>
        </div>

        <div class="eyebrow" style="margin-top:14px;">Level 3: Concrete Work Packages & Completion Evidence</div>
        <div class="task-deck">
          <details class="task-card" open>
            <summary>
              <span class="state-icon progress">◐</span>
              <span class="task-title">Daily 3x3 Residual Sprints (Daily 16:00 – 17:45)</span>
              <span class="task-badge">DAILY RHYTHM</span>
            </summary>
            <div class="task-body">
              <div class="evidence-block">
                <b>Sprint 1 (30m) — Apartment & Studio Art:</b>
                <ul class="checklist">
                  <li>• Workspace acoustic treatment and monitor calibration</li>
                  <li>• Fine art canvas stretching, primer coating, and painting session</li>
                </ul>
              </div>
              <div class="evidence-block">
                <b>Sprint 2 (30m) — Sexy Content:</b>
                <ul class="checklist">
                  <li>• Aesthetic moodboarding and key lighting setup</li>
                  <li>• High-resolution portrait photoshoot capture</li>
                  <li>• Master color grading and export to private portfolio</li>
                </ul>
              </div>
              <div class="evidence-block">
                <b>Sprint 3 (30m) — Community & Traveling:</b>
                <ul class="checklist">
                  <li>• Peer sync communications and dinner planning</li>
                  <li>• Travel route itineraries, flights, and accommodation verification</li>
                </ul>
              </div>
            </div>
          </details>
        </div>

      </div>
    </details>

  </div>

  <!-- Consolidated Mermaid Topological Critical Path DAG -->
  <div class="panel" style="margin-top:20px;">
    <div class="eyebrow" style="color:#a84332;">Cross-Repository Critical Path Topological Network</div>
    <h3 style="margin:6px 0 14px; font-family:Georgia,serif;">Consolidated Process Dependency DAG</h3>
    <svg viewBox="0 0 1050 240" style="width:100%; height:auto;" role="img" aria-label="Consolidated Critical Path DAG">
      <defs>
        <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M0 0L10 5L0 10z" fill="#71828f"/>
        </marker>
      </defs>
      <style>
        .dag-node{rx:6;ry:6;stroke-width:1.5;transition:0.15s all}
        .dag-text{font-family:Arial,sans-serif;font-size:11px;font-weight:bold;fill:#172a3d}
        .dag-sub{font-family:Arial,sans-serif;font-size:9px;fill:#687b8b}
        .dag-line{stroke:#90a4b5;stroke-width:1.8;stroke-dasharray:none;marker-end:url(#arrow)}
        .dag-crit{stroke:#c55a43;fill:#fff7f5}
        .dag-norm{stroke:#4a6fa5;fill:#f8fbff}
      </style>
      
      <!-- MoA Chain -->
      <rect x="20" y="30" width="160" height="50" class="dag-node dag-crit"/>
      <text x="30" y="50" class="dag-text">WP #163 Content Draft</text>
      <text x="30" y="66" class="dag-sub">CRITICAL PATH · MoA</text>

      <line x1="180" y1="55" x2="220" y2="55" class="dag-line"/>

      <rect x="220" y="30" width="160" height="50" class="dag-node dag-crit"/>
      <text x="230" y="50" class="dag-text">7 Videos Produced</text>
      <text x="230" y="66" class="dag-sub">CRITICAL PATH · Content</text>

      <line x1="380" y1="55" x2="420" y2="55" class="dag-line"/>

      <rect x="420" y="30" width="170" height="50" class="dag-node dag-crit"/>
      <text x="430" y="50" class="dag-text">WP-BIZ-01 Invoicing Engine</text>
      <text x="430" y="66" class="dag-sub">CRITICAL PATH · Business</text>

      <!-- IPOS Chain -->
      <rect x="20" y="110" width="160" height="50" class="dag-node dag-crit"/>
      <text x="30" y="130" class="dag-text">WP #224 Pipeline Recheck</text>
      <text x="30" y="146" class="dag-sub">CRITICAL PATH · IPOS</text>

      <line x1="180" y1="135" x2="220" y2="135" class="dag-line"/>

      <rect x="220" y="110" width="160" height="50" class="dag-node dag-crit"/>
      <text x="230" y="130" class="dag-text">Modular Ingestion Seam</text>
      <text x="230" y="146" class="dag-sub">CRITICAL PATH · Docling</text>

      <line x1="380" y1="135" x2="420" y2="135" class="dag-line"/>

      <rect x="420" y="110" width="170" height="50" class="dag-node dag-crit"/>
      <text x="430" y="130" class="dag-text">WP #232 Data Viz Over Time</text>
      <text x="430" y="146" class="dag-sub">CRITICAL PATH · Cockpit</text>

      <!-- Leela Node -->
      <rect x="630" y="30" width="170" height="50" class="dag-node dag-crit"/>
      <text x="640" y="50" class="dag-text">WP #159 Skill Tree Contracts</text>
      <text x="640" y="66" class="dag-sub">CRITICAL PATH · Leela Only</text>

      <!-- Apex Node -->
      <rect x="630" y="110" width="170" height="50" class="dag-node dag-crit"/>
      <text x="640" y="130" class="dag-text">OpenMouse HID Intercept</text>
      <text x="640" y="146" class="dag-sub">CRITICAL PATH · Apex OS</text>

      <!-- Residuals Box -->
      <rect x="840" y="30" width="180" height="130" class="dag-node dag-norm"/>
      <text x="850" y="55" class="dag-text">Residual Life Flows (3x3)</text>
      <text x="850" y="75" class="dag-sub">• Sprint 1: Studio Art & Paint</text>
      <text x="850" y="95" class="dag-sub">• Sprint 2: Sexy Content Shoots</text>
      <text x="850" y="115" class="dag-sub">• Sprint 3: Community & Travel</text>
      <text x="850" y="140" class="dag-sub" style="font-weight:bold; fill:#355570;">Daily 16:00–17:45 Anchor</text>

      <!-- Join line to Saturday Milestone -->
      <line x1="590" y1="55" x2="630" y2="55" class="dag-line" stroke-dasharray="3,3"/>
      <line x1="590" y1="135" x2="630" y2="135" class="dag-line" stroke-dasharray="3,3"/>
      <line x1="800" y1="55" x2="840" y2="55" class="dag-line" stroke-dasharray="3,3"/>
    </svg>
  </div>
</section>

<!-- PART 3: MATRIX 2 — CALENDAR SNAPSHOT & VISUALIZATION -->
<section class="section" id="matrix2">
  <div class="sectionhead">
    <h2>03 · Matrix 2: Calendar Snapshot & Visualization (Temporal)</h2>
    <small>Daily operating window: 08:00 – 24:00 · Daily shutdown: 21:00 sharp · Meister meetings ignored</small>
  </div>
  
  <p style="font-size:12px; margin-bottom:12px;">
    <b>Reconciled Calendar Geometry:</b> All 4 daily focus flows are mapped across the operating span. Meister meetings are ignored per operator decision, keeping Wednesday and Friday evenings open. Thursday active commitments (Alex & Chris 10:00–11:00 and München Tanz 18:45–21:00) are protected.
  </p>

  <!-- 7-Day Quick Strip -->
  <div class="weekgrid">
    <article class="day">
      <small>Monday · 09 Nov</small>
      <h3>Foundations</h3>
      <small>4 Flows · 08:00–21:00</small>
      <p><span class="flow-tag">F1</span> MoA: Content Week scripts & audio</p>
      <p><span class="flow-tag">F2</span> MoA: Website content draft</p>
      <p><span class="flow-tag">F3</span> IPOS: Pipeline recheck & audit</p>
      <p><span class="flow-tag">F4</span> Residual: Studio acoustics & art</p>
    </article>

    <article class="day">
      <small>Tuesday · 10 Nov</small>
      <h3>Pipelines</h3>
      <small>4 Flows · 08:00–21:00</small>
      <p><span class="flow-tag">F1</span> MoA: Voiceover cuts & reel edit</p>
      <p><span class="flow-tag">F2</span> MoA: Website reading drawer layout</p>
      <p><span class="flow-tag">F3</span> IPOS: Ingestion seam modularization</p>
      <p><span class="flow-tag">F4</span> Residual: Sexy content lighting</p>
    </article>

    <article class="day">
      <small>Wednesday · 11 Nov</small>
      <h3>Invoicing Engine</h3>
      <small>4 Flows · Meister Declined</small>
      <p><span class="flow-tag">F1</span> MoA: 3 video reels finalized</p>
      <p><span class="flow-tag">F2</span> MoA: Line-item invoice JSON schema</p>
      <p><span class="flow-tag">F3</span> IPOS: Data viz over time schema</p>
      <p><span class="flow-tag">F4</span> Residual: Studio painting session</p>
      <div style="font-size:10px; color:#18572e; background:#dcfce7; padding:4px 6px; border-radius:4px; margin-top:4px;">
        Meister Ignored · Evening Open
      </div>
    </article>

    <article class="day meeting">
      <small>Thursday · 12 Nov</small>
      <h3>Coordination</h3>
      <small>Fixed Meeting + Dance</small>
      <div class="event-alert" style="background:#eaf2fb; border-color:#bdd2ee;">
        <b>10:00 – 11:00 Alex & Chris</b>Meeting with C. Sgarz · F1 compressed
      </div>
      <p><span class="flow-tag">F1</span> MoA: Audio cut (09:00–10:00)</p>
      <p><span class="flow-tag">F2</span> MoA: HTML-to-PDF invoice template</p>
      <p><span class="flow-tag">F3</span> IPOS: Time-series charting demo</p>
      <div class="event-alert"><b>18:45 – 21:00 München Tanz</b>Dance event · Wrap by 18:15</div>
    </article>

    <article class="day">
      <small>Friday · 13 Nov</small>
      <h3>Production Wrap</h3>
      <small>4 Flows · Meister Declined</small>
      <p><span class="flow-tag">F1</span> MoA: 7th video reel mastered</p>
      <p><span class="flow-tag">F2</span> MoA: Invoicing batch verification</p>
      <p><span class="flow-tag">F3</span> IPOS: Full intake test harness run</p>
      <p><span class="flow-tag">F4</span> Residual: Travel logistics sync</p>
      <div style="font-size:10px; color:#18572e; background:#dcfce7; padding:4px 6px; border-radius:4px; margin-top:4px;">
        Meister Ignored · Shutdown 21:00
      </div>
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

  <!-- Full-Width Responsive HTML Calendar Table Showing ALL 4 FLOWS -->
  <div style="width:100%; overflow-x:auto; margin:20px 0; border:1px solid #dce4e8; border-radius:10px; background:#fff;">
    <table style="width:100%; min-width:1180px; border-collapse:collapse; font-size:12px;">
      <thead>
        <tr style="background:#162642; color:#fff;">
          <th style="width:12%; padding:10px; border:1px solid #2a3e5c;">Window / Flow</th>
          <th style="width:6%; padding:10px; border:1px solid #2a3e5c;">Sprint</th>
          <th style="width:13.6%; padding:10px; border:1px solid #2a3e5c;">Monday</th>
          <th style="width:13.6%; padding:10px; border:1px solid #2a3e5c;">Tuesday</th>
          <th style="width:13.6%; padding:10px; border:1px solid #2a3e5c;">Wednesday</th>
          <th style="width:13.6%; padding:10px; border:1px solid #2a3e5c;">Thursday</th>
          <th style="width:13.6%; padding:10px; border:1px solid #2a3e5c;">Friday</th>
          <th style="width:13.6%; padding:10px; border:1px solid #2a3e5c;">Saturday</th>
        </tr>
      </thead>
      <tbody>
        
        <!-- Morning Routine Anchor -->
        <tr style="background:#f4f1ea; color:#687b8b;">
          <td style="padding:6px; text-align:center; font-family:monospace;">08:00–09:00</td>
          <td colspan="7" style="padding:6px; text-align:center;">🔒 Protected Anchor: Morning Routine, Meditation & Setup</td>
        </tr>

        <!-- FLOW 1: MoA Content Production (7 Videos) -->
        <tr style="border-top:2px solid #507967;">
          <td rowspan="3" style="padding:10px; vertical-align:top; background:#f5f8f5;">
            <b style="color:#2a5035;">Flow 1 (2h)</b><br>
            <span style="font-size:10px; color:#687b8b;">09:00–11:00</span><br>
            <span style="font-size:11px; font-weight:700;">MoA: 7 Videos Pass</span>
          </td>
          <td style="padding:6px; text-align:center; font-weight:700; border-bottom:1px solid #eef1f4;">Sp 1 (30m)</td>
          <td style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4;">
            <b>Video 1 & 2 Scripting</b>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:11px;">
              <li>1. Outline core hook thesis</li>
              <li>2. Draft 60s spoken script</li>
              <li>3. Polish visual cues</li>
            </ul>
          </td>
          <td style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4;">
            <b>Video 3 & 4 Scripting</b>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:11px;">
              <li>1. Outline thesis points</li>
              <li>2. Script spoken dialogue</li>
              <li>3. Check runtime limits</li>
            </ul>
          </td>
          <td style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4;">
            <b>Video 5 & 6 Scripting</b>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:11px;">
              <li>1. Draft narrative scripts</li>
              <li>2. Cross-link essays</li>
              <li>3. Polish conclusion</li>
            </ul>
          </td>
          <td style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4; background:#edf4fd;">
            <span style="font-size:9px; color:#25548c; font-weight:700;">COMPRESSED (09:00–10:00)</span><br>
            <b>Video 7 Script & Cut</b>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:11px;">
              <li>1. Finalize 7th script</li>
              <li>2. Record voice track</li>
              <li>3. Quick audio master</li>
            </ul>
          </td>
          <td style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4;">
            <b>Batch Video Mastering</b>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:11px;">
              <li>1. Color grade all 7 cuts</li>
              <li>2. Dynamic caption verify</li>
              <li>3. Render 1080x1920 masters</li>
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
            <b>Audio Voiceover Cuts</b>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:11px;">
              <li>1. Record vocal takes 1 & 2</li>
              <li>2. De-breath & remove clicks</li>
              <li>3. Export WAV vocals</li>
            </ul>
          </td>
          <td style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4;">
            <b>Audio Voiceover Cuts</b>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:11px;">
              <li>1. Record vocal takes 3 & 4</li>
              <li>2. De-ess dialogue track</li>
              <li>3. Equalize vocals</li>
            </ul>
          </td>
          <td style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4;">
            <b>Audio Voiceover Cuts</b>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:11px;">
              <li>1. Record vocal takes 5 & 6</li>
              <li>2. Normalize vocal loudness</li>
              <li>3. Export master dialogue</li>
            </ul>
          </td>
          <td style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4; background:#edf4fd;">
            <b style="color:#1d4273;">10:00–11:00 Meeting</b><br>
            <span style="font-size:11px;">🔒 Alex & Chris (C. Sgarz)</span>
          </td>
          <td style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4;">
            <b>Distribution Packaging</b>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:11px;">
              <li>1. Upload video package</li>
              <li>2. Generate thumbnail set</li>
              <li>3. Schedule distribution</li>
            </ul>
          </td>
        </tr>

        <tr style="border-bottom:2px solid #507967;">
          <td style="padding:6px; text-align:center; font-weight:700;">Sp 3 (30m)</td>
          <td style="padding:6px; vertical-align:top;">
            <b>Rough Cut & Captions</b>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:11px;">
              <li>1. Slice vertical B-roll</li>
              <li>2. Auto-generate captions</li>
              <li>3. Review pacing sync</li>
            </ul>
          </td>
          <td style="padding:6px; vertical-align:top;">
            <b>Rough Cut & Captions</b>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:11px;">
              <li>1. Cut visual transitions</li>
              <li>2. Style dynamic subtitles</li>
              <li>3. Export test MP4</li>
            </ul>
          </td>
          <td style="padding:6px; vertical-align:top;">
            <b>Rough Cut & Captions</b>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:11px;">
              <li>1. Assemble visual assets</li>
              <li>2. Verify subtitle timings</li>
              <li>3. Export test MP4</li>
            </ul>
          </td>
          <td style="padding:6px; vertical-align:top; background:#edf4fd;">
            <span style="font-size:11px; color:#5b6e82;">Meeting wrap & follow-ups</span>
          </td>
          <td style="padding:6px; vertical-align:top;">
            <b>7-Video Signoff</b>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:11px;">
              <li>1. Operator quality pass</li>
              <li>2. Tag release metadata</li>
              <li>3. Log content milestone</li>
            </ul>
          </td>
        </tr>

        <!-- FLOW 2: MoA Website Content Draft & Invoicing Engine -->
        <tr style="border-top:2px solid #355570;">
          <td rowspan="3" style="padding:10px; vertical-align:top; background:#f0f5fa;">
            <b style="color:#1d3859;">Flow 2 (1.25h)</b><br>
            <span style="font-size:10px; color:#687b8b;">11:15–12:30</span><br>
            <span style="font-size:11px; font-weight:700;">MoA: Site & Invoice</span>
          </td>
          <td style="padding:6px; text-align:center; font-weight:700; border-bottom:1px solid #eef1f4;">Sp 1 (30m)</td>
          <td style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4;">
            <b>Website Content Draft</b>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:11px;">
              <li>1. Stage draft essay files</li>
              <li>2. Author reading metadata</li>
              <li>3. Check typography hierarchy</li>
            </ul>
          </td>
          <td style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4;">
            <b>Flexbox Navigation</b>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:11px;">
              <li>1. CSS flexbox header pass</li>
              <li>2. Nav item active links</li>
              <li>3. Desktop responsive check</li>
            </ul>
          </td>
          <td style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4;">
            <b>Invoice JSON Schema</b>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:11px;">
              <li>1. Author line-item schema</li>
              <li>2. Define VAT & subtotal types</li>
              <li>3. Unit test schema parser</li>
            </ul>
          </td>
          <td style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4;">
            <b>HTML Print Template</b>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:11px;">
              <li>1. Author invoice HTML markup</li>
              <li>2. Embed print stylesheet</li>
              <li>3. Set page break rules</li>
            </ul>
          </td>
          <td style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4;">
            <b>Billing Engine Run</b>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:11px;">
              <li>1. Execute sample invoice run</li>
              <li>2. Verify tax line precision</li>
              <li>3. Check output PDF integrity</li>
            </ul>
          </td>
          <td rowspan="3" style="padding:8px; vertical-align:top; background:#f9f8f5;">
            <b style="color:#856434;">Workspace Reset</b><br>
            <span style="font-size:10px; color:#7d8c97;">11:30–13:00</span>
            <p style="font-size:11px; margin:4px 0;">Clean room & tool maintenance.</p>
          </td>
        </tr>

        <tr>
          <td style="padding:6px; text-align:center; font-weight:700; border-bottom:1px solid #eef1f4;">Sp 2 (30m)</td>
          <td style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4;">
            <b>Reading Route Bind</b>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:11px;">
              <li>1. Wire static route slugs</li>
              <li>2. Verify mobile viewport</li>
              <li>3. Test font scale readability</li>
            </ul>
          </td>
          <td style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4;">
            <b>Mobile Reading Drawer</b>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:11px;">
              <li>1. Hamburger drawer animation</li>
              <li>2. Toggle state JS hook</li>
              <li>3. Touch scroll lock test</li>
            </ul>
          </td>
          <td style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4;">
            <b>Tax Formula Unit Tests</b>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:11px;">
              <li>1. Write subtotal test cases</li>
              <li>2. Write discount rounding tests</li>
              <li>3. Confirm zero math drift</li>
            </ul>
          </td>
          <td style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4;">
            <b>Headless PDF Export</b>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:11px;">
              <li>1. Wire headless Chromium print</li>
              <li>2. Verify vector typography</li>
              <li>3. Validate PDF/A compliance</li>
            </ul>
          </td>
          <td style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4;">
            <b>MoA Deploy Signoff</b>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:11px;">
              <li>1. Push website draft to branch</li>
              <li>2. Archive invoice test receipts</li>
              <li>3. Commit verified codebase</li>
            </ul>
          </td>
        </tr>

        <tr style="border-bottom:2px solid #355570;">
          <td style="padding:6px; text-align:center; font-weight:700;">Sp 3 (15m)</td>
          <td style="padding:6px; vertical-align:top;">
            <b>Content Preview Pass</b>
            <span style="font-size:10px; color:#687b8b; display:block;">Operator editorial check</span>
          </td>
          <td style="padding:6px; vertical-align:top;">
            <b>Browser Audit</b>
            <span style="font-size:10px; color:#687b8b; display:block;">Chrome/Safari responsive pass</span>
          </td>
          <td style="padding:6px; vertical-align:top;">
            <b>Schema Validation</b>
            <span style="font-size:10px; color:#687b8b; display:block;">Freeze JSON schema v1.0</span>
          </td>
          <td style="padding:6px; vertical-align:top;">
            <b>Print Alignment</b>
            <span style="font-size:10px; color:#687b8b; display:block;">Margin & header review</span>
          </td>
          <td style="padding:6px; vertical-align:top;">
            <b>Milestone Archive</b>
            <span style="font-size:10px; color:#687b8b; display:block;">Lock week 45 billing receipts</span>
          </td>
        </tr>

        <!-- Protected Routine Anchor: Lunch -->
        <tr style="background:#f4f1ea; color:#687b8b;">
          <td style="padding:6px; text-align:center; font-family:monospace;">12:30–13:30</td>
          <td colspan="7" style="padding:6px; text-align:center;">🔒 Protected Anchor: Midday Reset, Healthy Lunch & Fresh Air Walk</td>
        </tr>

        <!-- FLOW 3: IPOS Pipeline Recheck & Data Viz Over Time -->
        <tr style="border-top:2px solid #b08445;">
          <td rowspan="3" style="padding:10px; vertical-align:top; background:#fdf9f2;">
            <b style="color:#784f1e;">Flow 3 (2h)</b><br>
            <span style="font-size:10px; color:#687b8b;">13:30–15:30</span><br>
            <span style="font-size:11px; font-weight:700;">IPOS: Pipeline Recheck</span>
          </td>
          <td style="padding:6px; text-align:center; font-weight:700; border-bottom:1px solid #eef1f4;">Sp 1 (30m)</td>
          <td style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4;">
            <b>Ingestion Code Audit</b>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:11px;">
              <li>1. Audit <code>ipos/ingest/</code> codebase</li>
              <li>2. Identify Karakeep legacy debt</li>
              <li>3. Map external tool choices</li>
            </ul>
          </td>
          <td style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4;">
            <b>Modular Seam Architecture</b>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:11px;">
              <li>1. Author ingestion interface spec</li>
              <li>2. Separate PDF from web parsing</li>
              <li>3. Draft Docling adapter harness</li>
            </ul>
          </td>
          <td style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4;">
            <b>Time-Series Chart Schema</b>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:11px;">
              <li>1. Model time-series data types</li>
              <li>2. Define timestamped metric keys</li>
              <li>3. Author test JSON fixture</li>
            </ul>
          </td>
          <td style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4;">
            <b>Data Viz Prototype</b>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:11px;">
              <li>1. Wire chart rendering canvas</li>
              <li>2. Implement date range filter</li>
              <li>3. Verify responsive chart resize</li>
            </ul>
          </td>
          <td style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4;">
            <b>Test Harness Verification</b>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:11px;">
              <li>1. Run end-to-end ingestion pass</li>
              <li>2. Benchmark extraction latency</li>
              <li>3. Verify clean JSON output</li>
            </ul>
          </td>
          <td rowspan="3" style="padding:8px; vertical-align:top; background:#f0eee6; color:#788691;">
            <b>Saturday Afternoon OFF</b><br>
            <span style="font-size:10px;">Rest & personal regeneration</span>
          </td>
        </tr>

        <tr>
          <td style="padding:6px; text-align:center; font-weight:700; border-bottom:1px solid #eef1f4;">Sp 2 (30m)</td>
          <td style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4;">
            <b>Retirement Protocol</b>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:11px;">
              <li>1. Lock ADR-003 record</li>
              <li>2. Purge stale mock fixtures</li>
              <li>3. Run regression check</li>
            </ul>
          </td>
          <td style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4;">
            <b>Trafilatura Adapter</b>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:11px;">
              <li>1. Wire Trafilatura web cleaner</li>
              <li>2. Test article boilerplate strip</li>
              <li>3. Validate output metadata</li>
            </ul>
          </td>
          <td style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4;">
            <b>Modular Visualization Seam</b>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:11px;">
              <li>1. Decouple chart from storage</li>
              <li>2. Write data normalization adapter</li>
              <li>3. Test missing-period fills</li>
            </ul>
          </td>
          <td style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4;">
            <b>Multi-Tier Cockpit Card</b>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:11px;">
              <li>1. Bind metrics to cockpit card</li>
              <li>2. Test trend delta indicator</li>
              <li>3. Verify light/dark theme styles</li>
            </ul>
          </td>
          <td style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4;">
            <b>IPOS Review & Signoff</b>
            <ul style="margin:2px 0 0 12px; padding:0; font-size:11px;">
              <li>1. Operator review of data viz</li>
              <li>2. Lock modular pipeline design</li>
              <li>3. Commit verified IPOS branch</li>
            </ul>
          </td>
        </tr>

        <tr style="border-bottom:2px solid #b08445;">
          <td style="padding:6px; text-align:center; font-weight:700;">Sp 3 (30m)</td>
          <td style="padding:6px; vertical-align:top;">
            <b>Benchmark Documentation</b>
            <span style="font-size:10px; color:#687b8b; display:block;">Record external intake findings</span>
          </td>
          <td style="padding:6px; vertical-align:top;">
            <b>Docling PDF Pass</b>
            <span style="font-size:10px; color:#687b8b; display:block;">Multi-page research document test</span>
          </td>
          <td style="padding:6px; vertical-align:top;">
            <b>Canvas Performance</b>
            <span style="font-size:10px; color:#687b8b; display:block;">60fps scroll & zoom check</span>
          </td>
          <td style="padding:6px; vertical-align:top;">
            <b>Interactive Inspection</b>
            <span style="font-size:10px; color:#687b8b; display:block;">Crosshair tooltip testing</span>
          </td>
          <td style="padding:6px; vertical-align:top;">
            <b>Pipeline Archive</b>
            <span style="font-size:10px; color:#687b8b; display:block;">Emit execution receipts</span>
          </td>
        </tr>

        <!-- FLOW 4: Residual Life & Creative Sprints -->
        <tr style="border-top:2px solid #806655;">
          <td rowspan="3" style="padding:10px; vertical-align:top; background:#f9f5f0;">
            <b style="color:#684f3e;">Flow 4 (1.75h)</b><br>
            <span style="font-size:10px; color:#687b8b;">16:00–17:45</span><br>
            <span style="font-size:11px; font-weight:700;">Residual Life Flows</span>
          </td>
          <td style="padding:6px; text-align:center; font-weight:700; border-bottom:1px solid #eef1f4;">Sp 1 (30m)</td>
          <td colspan="5" style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4;">
            <b>Apartment & Studio Art:</b> Workspace acoustic tuning, studio clean room reset, canvas stretching, and fine art painting sessions.
          </td>
          <td rowspan="3" style="padding:8px; vertical-align:top; background:#f0eee6; color:#788691;">
            <b>Sunday Regeneration</b><br>
            <span style="font-size:10px;">OFF by default (D017)</span>
          </td>
        </tr>

        <tr>
          <td style="padding:6px; text-align:center; font-weight:700; border-bottom:1px solid #eef1f4;">Sp 2 (30m)</td>
          <td colspan="5" style="padding:6px; vertical-align:top; border-bottom:1px solid #eef1f4;">
            <b>Sexy Content:</b> Aesthetic moodboards, lighting setups, photoshoot portrait capture, and high-tier color grading passes.
          </td>
        </tr>

        <tr style="border-bottom:2px solid #806655;">
          <td style="padding:6px; text-align:center; font-weight:700;">Sp 3 (30m)</td>
          <td colspan="5" style="padding:6px; vertical-align:top;">
            <b>Community & Traveling:</b> Peer network outreach, community dinner logistics, travel route planning, and accommodation verification.
          </td>
        </tr>

        <!-- Daily Shutdown Anchor at 21:00 -->
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

<footer style="margin-top:40px; padding-top:20px; border-top:1px solid #e1e5e5; font-size:11px; color:#788b99; display:flex; justify-content:space-between;">
  <span>Precap Week · Week 2026-W45 · Operator Confirmed</span>
  <span>Operating Window: 08:00–24:00 · Shutdown: 21:00</span>
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
