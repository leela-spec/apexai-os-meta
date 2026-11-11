/**
 * Shared W34 prototype dataset for Weekly Command Brief visualization candidates.
 * Contains both 'normal' (baseline W34) and 'stress' (compressed/meeting-heavy W34) fixtures.
 */
const PROTOTYPE_DATA = {
  meta: {
    week: "2026-W34",
    title: "Weekly Command Brief — 2026-W34",
    portfolioGoal: "Advance the MasterOfArts website while preserving one planned daily flow for each of Leela, MasterOfArts, Apex, and Investment.",
    activeProjectCount: 5,
    majorOutcomeCount: 4
  },
  
  days: [
    { id: "mon", name: "Monday", date: "08-17", role: "Start", shortRole: "Start" },
    { id: "tue", name: "Tuesday", date: "08-18", role: "Build", shortRole: "Build" },
    { id: "wed", name: "Wednesday", date: "08-19", role: "Build", shortRole: "Build" },
    { id: "thu", name: "Thursday", date: "08-20", role: "Review", shortRole: "Review" },
    { id: "fri", name: "Friday", date: "08-21", role: "Buffer", shortRole: "Buffer" }
  ],

  projects: [
    {
      id: "moa",
      name: "MasterOfArts",
      label: "MasterOfArts ★ focus",
      isFocus: true,
      role: "Business / Content Focus",
      target: "Website Definition Baseline: Establish implementation-ready IA, copy blocks, and conversion outcomes."
    },
    {
      id: "leela",
      name: "Leela",
      label: "Leela",
      isFocus: false,
      role: "Product Core",
      target: "Spatial Skill Tree Runtime: Advance dependency-clear interaction mechanics and runtime verification."
    },
    {
      id: "apex",
      name: "Apex",
      label: "Apex",
      isFocus: false,
      role: "Orchestration Spine",
      target: "Apex KB Query & Contracts: Lock contract baselines, benchmark retrieval, and evaluate upgrade paths."
    },
    {
      id: "inv",
      name: "Investment",
      label: "Investment",
      isFocus: false,
      role: "Intelligence Stream",
      target: "Decision Intelligence: Collect branch inputs and structure alert/filtering contracts."
    },
    {
      id: "res",
      name: "Residual",
      label: "Residual — recovery/overflow",
      isFocus: false,
      role: "Recovery & Support",
      target: "Overflow Protection: Reserve recovery buffer without displacing the four primary flows."
    }
  ],

  scenarios: {
    normal: {
      label: "Normal W34",
      description: "Standard assumed capacity across all 5 weekdays (8h baseline, 4 flows/day). Calendar unverified.",
      calendarStatus: "Calendar unavailable in W34 baseline; all days assumed standard capacity.",
      dayCapacity: {
        mon: { capacity: "STANDARD", flows: 4, shapeClass: "standard", fixedConstraint: "🔒 Protected anchors (Morning/Lunch/Outro)", note: "Full capacity (4 flows)" },
        tue: { capacity: "STANDARD", flows: 4, shapeClass: "standard", fixedConstraint: "🔒 Protected anchors (Morning/Lunch/Outro)", note: "Full capacity (4 flows)" },
        wed: { capacity: "STANDARD", flows: 4, shapeClass: "standard", fixedConstraint: "🔒 Protected anchors (Morning/Lunch/Outro)", note: "Full capacity (4 flows)" },
        thu: { capacity: "STANDARD", flows: 4, shapeClass: "standard", fixedConstraint: "🔒 Protected anchors (Morning/Lunch/Outro)", note: "Full capacity (4 flows)" },
        fri: { capacity: "STANDARD", flows: 4, shapeClass: "standard", fixedConstraint: "🔒 Protected anchors (Morning/Lunch/Outro)", note: "Full capacity (4 flows)" }
      },
      grid: {
        moa: {
          mon: { task: "Locate current website-definition source", metric: "I92/R15/E85", type: "work", icon: "🎯" },
          tue: { task: "Reconcile purpose, audience & conversion outcomes", metric: "I94/R25/E80", type: "work", dep: "↳ after Mon", icon: "📝" },
          wed: { task: "Define information architecture & page responsibilities", metric: "I90/R25/E78", type: "work", dep: "↳ after Tue", icon: "📐" },
          thu: { task: "Define page-level content & interactions", metric: "I88/R30/E75", type: "work", dep: "↳ after Wed", icon: "🔍" },
          fri: { task: "Review website definition for implementation readiness", metric: "I86/R20/E72", type: "work", dep: "↳ after Thu", icon: "📦" }
        },
        leela: {
          mon: { task: "Verify Home runtime", metric: "I90/R20/E95", type: "work", icon: "⚡" },
          tue: { task: "Verify bounded spatial Skill Tree runtime", metric: "I88/R25/E92", type: "work", icon: "⚖️" },
          wed: { task: "Promote bounded cluster to primary Skill Tree navigation", metric: "I92/R45/E80", type: "work", dep: "↳ after Mon + Tue", icon: "🔗" },
          thu: { task: "Make ScopeSelection handoff origin-aware", metric: "I86/R40/E78", type: "work", dep: "↳ after Wed", icon: "🧪" },
          fri: { task: "Reconcile ResolutionRequest/Context with Home + Skill Tree", metric: "I82/R35/E76", type: "work", dep: "↳ after Thu", icon: "🛡️" }
        },
        apex: {
          mon: { task: "Re-baseline ApexKB implementation & contract", metric: "I88/R20/E90", type: "work", icon: "📜" },
          tue: { task: "Build operator-value & retrieval benchmark", metric: "I84/R25/E85", type: "work", dep: "↳ after Mon", icon: "⚙️" },
          wed: { task: "Evaluate cheapest credible upgrade path", metric: "I78/R30/E80", type: "work", dep: "↳ after Tue", icon: "🧩" },
          thu: { task: "Evaluate alternatives & hybrid options", metric: "I80/R35/E78", type: "work", dep: "↳ after Tue", icon: "🔍" },
          fri: { task: "Run controlled ApexKB comparison", metric: "I90/R40/E75", type: "work", dep: "↳ after Wed + Thu", icon: "📊" }
        },
        inv: {
          mon: { task: "Collect required operator inputs for one equal branch", metric: "I82/R15/E60", type: "work", icon: "📥" },
          tue: { task: "Define video-discovery contract", metric: "I76/R25/E68", type: "work", dep: "↳ if video branch chosen", icon: "📊" },
          wed: { task: "Collect alert-contract conditions", metric: "I80/R20/E65", type: "work", icon: "🎯" },
          thu: { task: "Collect decision-feedback process input", metric: "I78/R20/E65", type: "work", icon: "🔔" },
          fri: { task: "Configure/test video-search job", metric: "I72/R35/E70", type: "work", dep: "↳ after Tue", icon: "📑" }
        },
        res: {
          mon: { task: "Recovery reserve", metric: null, type: "deferral", reason: "Capacity reserved for primary flows" },
          tue: { task: "Recovery reserve", metric: null, type: "deferral", reason: "Capacity reserved for primary flows" },
          wed: { task: "Recovery reserve", metric: null, type: "deferral", reason: "Capacity reserved for primary flows" },
          thu: { task: "Recovery reserve", metric: null, type: "deferral", reason: "Capacity reserved for primary flows" },
          fri: { task: "Recovery / overflow buffer", metric: "I30/R20/E70", type: "work", icon: "🔄" }
        }
      }
    },

    stress: {
      label: "Stress Week",
      description: "Meeting-heavy constraints: Tuesday compressed (2 flows), Wednesday minimal (1 flow), Thursday compressed (2 flows), Friday website deadline 12:00.",
      calendarStatus: "Severe meeting constraints detected on Tue/Wed/Thu. Consequential deferrals active.",
      dayCapacity: {
        mon: { capacity: "STANDARD", flows: 4, shapeClass: "standard", fixedConstraint: "🔒 Protected anchors (Morning/Lunch/Outro)", note: "Full capacity (4 flows)" },
        tue: { capacity: "COMPRESSED", flows: 2, shapeClass: "compressed", fixedConstraint: "👥 Meetings 14:00–17:00 (3h blocked)", note: "Compressed (2 flows max)" },
        wed: { capacity: "MINIMAL", flows: 1, shapeClass: "minimal", fixedConstraint: "👥 Meetings 10:00–16:00 (6h blocked)", note: "Minimal (1 flow max)" },
        thu: { capacity: "COMPRESSED", flows: 2, shapeClass: "compressed", fixedConstraint: "👥 Website checkpoint 13:00 (2h blocked)", note: "Compressed (2 flows max)" },
        fri: { capacity: "STANDARD", flows: 3, shapeClass: "standard", fixedConstraint: "⏰ MoA Website readiness due 12:00", note: "Standard (3 flows + buffer)" }
      },
      grid: {
        moa: {
          mon: { task: "Locate website source", metric: "I92/R15/E85", type: "work", icon: "🎯" },
          tue: { task: "Reconcile purpose/audience", metric: "I94/R25/E80", type: "work", dep: "↳ after Mon", icon: "📝" },
          wed: { task: "Define website IA", metric: "I90/R25/E78", type: "work", dep: "↳ protected sole flow", icon: "📐" },
          thu: { task: "Define page requirements", metric: "I88/R30/E75", type: "work", dep: "↳ after Wed", icon: "🔍" },
          fri: { task: "⏰ GATE 12:00: Readiness review", metric: "I86/R20/E72", type: "deadline", dep: "↳ after Thu", icon: "📦" }
        },
        leela: {
          mon: { task: "Verify Home runtime", metric: "I90/R20/E95", type: "work", icon: "⚡" },
          tue: { task: "Verify bounded Skill Tree runtime", metric: "I88/R25/E92", type: "work", icon: "⚖️" },
          wed: { task: "↘ Defer — minimal capacity", metric: null, type: "deferral", reason: "Deferred due to 6h meeting overload" },
          thu: { task: "Promote bounded cluster", metric: "I92/R45/E80", type: "work", dep: "↳ after Mon + Tue", icon: "🔗" },
          fri: { task: "ScopeSelection handoff", metric: "I86/R40/E78", type: "work", dep: "↳ after Thu", icon: "🧪" }
        },
        apex: {
          mon: { task: "Re-baseline ApexKB", metric: "I88/R20/E90", type: "work", icon: "📜" },
          tue: { task: "Build benchmark", metric: "I84/R25/E85", type: "work", dep: "↳ after Mon", icon: "⚙️" },
          wed: { task: "↘ Defer — minimal capacity", metric: null, type: "deferral", reason: "Deferred due to 6h meeting overload" },
          thu: { task: "Evaluate cheapest path", metric: "I78/R30/E80", type: "work", dep: "↳ after Tue", icon: "🧩" },
          fri: { task: "Evaluate alternatives/hybrid", metric: "I80/R35/E78", type: "work", dep: "↳ after Tue", icon: "🔍" }
        },
        inv: {
          mon: { task: "Collect branch input", metric: "I82/R15/E60", type: "work", icon: "📥" },
          tue: { task: "↘ Defer — meetings 14–17", metric: null, type: "deferral", reason: "Deferred to protect Leela & MoA flows" },
          wed: { task: "↘ Defer — minimal capacity", metric: null, type: "deferral", reason: "Deferred due to 6h meeting overload" },
          thu: { task: "Define selected branch contract", metric: "I76/R25/E68", type: "work", dep: "↳ if branch chosen", icon: "📊" },
          fri: { task: "Configure/test selected branch", metric: "I72/R35/E70", type: "work", dep: "↳ after Thu", icon: "📑" }
        },
        res: {
          mon: { task: "Recovery reserve", metric: null, type: "deferral", reason: "Capacity reserved for primary flows" },
          tue: { task: "Recovery reserve", metric: null, type: "deferral", reason: "Capacity reserved for primary flows" },
          wed: { task: "Recovery reserve", metric: null, type: "deferral", reason: "Capacity reserved for primary flows" },
          thu: { task: "Recovery reserve", metric: null, type: "deferral", reason: "Capacity reserved for primary flows" },
          fri: { task: "Overflow / recovery", metric: "I30/R20/E70", type: "work", icon: "🔄" }
        }
      }
    }
  }
};

if (typeof module !== 'undefined' && module.exports) {
  module.exports = PROTOTYPE_DATA;
}
