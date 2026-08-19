import { createHash } from "node:crypto";

const POLICY_SCHEMA = "apex.browser-policy/v1";
const OBSERVATION_ACTIONS = new Set(["status", "tabs"]);
const TARGETED_ACTIONS = new Set(["snapshot", "screenshot", "focus", "navigate", "act"]);
const ACT_KINDS = new Set(["click", "type", "press", "wait"]);

export function policyFileName(sessionKey) {
  return `${createHash("sha256").update(sessionKey, "utf8").digest("hex")}.json`;
}

function blocked(reason) {
  return { ok: false, reason: `APEX_BROWSER_POLICY: ${reason}` };
}

function isNonEmptyString(value) {
  return typeof value === "string" && value.length > 0;
}

export function validatePolicy(policy) {
  if (!policy || typeof policy !== "object" || Array.isArray(policy)) return false;
  if (policy.schema_version !== POLICY_SCHEMA) return false;
  for (const field of [
    "execution_id",
    "agent_id",
    "session_key",
    "browser_profile",
    "hostname",
    "tab_id",
    "expires_at",
  ]) {
    if (!isNonEmptyString(policy[field])) return false;
  }
  return true;
}

function normalizedHostname(urlText) {
  try {
    const url = new URL(urlText);
    return url.protocol === "https:" ? url.hostname.toLowerCase() : null;
  } catch {
    return null;
  }
}

function targetIdFor(params) {
  if (params?.action === "act" && params.request && typeof params.request === "object") {
    return params.request.targetId ?? params.targetId;
  }
  return params?.targetId;
}

export function authorizeBrowserCall({ agentId, sessionKey, params, policy, now = Date.now() }) {
  if (!policy) return blocked("missing policy");
  if (!validatePolicy(policy)) return blocked("invalid policy");
  const expiry = Date.parse(policy.expires_at);
  if (!Number.isFinite(expiry)) return blocked("invalid policy expiry");
  if (expiry <= now) return blocked("expired policy");
  if (agentId !== policy.agent_id) return blocked("agent mismatch");
  if (sessionKey !== policy.session_key) return blocked("session mismatch");
  if (!params || typeof params !== "object" || Array.isArray(params)) {
    return blocked("browser parameters are invalid");
  }
  if (params.profile !== policy.browser_profile) return blocked("profile mismatch");
  if (params.target !== undefined && params.target !== "host") return blocked("browser target mismatch");
  if (params.node !== undefined) return blocked("browser node is not permitted");

  const action = params.action;
  if (!OBSERVATION_ACTIONS.has(action) && !TARGETED_ACTIONS.has(action)) {
    return blocked("action is not permitted");
  }
  if (OBSERVATION_ACTIONS.has(action)) return { ok: true };

  const targetId = targetIdFor(params);
  if (!isNonEmptyString(targetId)) return blocked("targetId is required");
  if (targetId !== policy.tab_id) return blocked("tab mismatch");

  if (action === "navigate") {
    const destination = params.targetUrl ?? params.url;
    if (normalizedHostname(destination) !== policy.hostname) {
      return blocked("navigation hostname mismatch");
    }
  }
  if (action === "act") {
    const request = params.request && typeof params.request === "object" ? params.request : params;
    if (!ACT_KINDS.has(request.kind)) return blocked("act kind is not permitted");
    if (request.kind === "wait" && isNonEmptyString(request.fn)) {
      return blocked("act kind is not permitted");
    }
  }
  return { ok: true };
}
