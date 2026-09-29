"use strict";

/**
 * PI-06 skill-level OpenProject write confirm (Two-Phase).
 * Compose Lexikon gate stays in ki-basis opWriteConfirm.js.
 *
 * Policy: confirm only update/delete (PATCH/PUT/DELETE). Create (POST)
 * and reads (GET) run without confirmed=true.
 */

const CONFIRM_METHODS = new Set(["PATCH", "PUT", "DELETE"]);

function truthyConfirmed(args) {
  const v = args && args.confirmed;
  return ["1", "true", "yes", "ja"].includes(String(v || "").trim().toLowerCase());
}

function isSkillWriteConfirmEnabled(env = process.env) {
  const raw =
    env.OP_SKILL_WRITE_CONFIRM !== undefined
      ? String(env.OP_SKILL_WRITE_CONFIRM).trim()
      : String(env.LEXICON_OP_WRITE_CONFIRM ?? "1").trim();
  if (/^(0|false|off|no)$/i.test(raw)) return false;
  return /^(1|true|yes|on)?$/i.test(raw) || raw === "";
}

function isMutatingMethod(method) {
  return CONFIRM_METHODS.has(String(method || "").trim().toUpperCase());
}

function summarizeArgs(args) {
  const bits = [];
  for (const key of [
    "subject",
    "title",
    "name",
    "id",
    "project_id",
    "project",
    "work_package_id",
    "principal",
    "status",
    "hours",
  ]) {
    if (args?.[key] != null && String(args[key]).trim() !== "") {
      bits.push(`${key}=${String(args[key]).trim()}`);
    }
  }
  return bits.join(" · ");
}

function formatConfirmAsk({ hubId, operation, method, args }) {
  const hub = String(hubId || "openproject").replace(/^@@/, "");
  const op = String(operation || "?").trim();
  const m = String(method || "").toUpperCase();
  const extra = summarizeArgs(args);
  return [
    "## Bestätigung erforderlich (Skill)",
    "",
    "Geplante OpenProject-Änderung über Agent-Skill:",
    `- hub=${hub} · operation=${op} · method=${m}${extra ? ` · ${extra}` : ""}`,
    "",
    "Schreibvorgang nicht ausgeführt.",
    "Nach Nutzer-OK denselben Aufruf mit **confirmed=true** wiederholen.",
  ].join("\n");
}

/**
 * @returns {string|null} Confirm markdown when blocked; null when call may proceed.
 */
function confirmOrNull({ hubId, operation, method, args, env = process.env }) {
  if (!isSkillWriteConfirmEnabled(env)) return null;
  if (!isMutatingMethod(method)) return null;
  if (truthyConfirmed(args)) return null;
  return formatConfirmAsk({ hubId, operation, method, args });
}

module.exports = {
  truthyConfirmed,
  isSkillWriteConfirmEnabled,
  isMutatingMethod,
  confirmOrNull,
  formatConfirmAsk,
};
