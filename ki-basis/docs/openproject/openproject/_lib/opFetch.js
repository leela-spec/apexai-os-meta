"use strict";

/**
 * Shared OpenProject fetch helper (API-only). Write confirmation stays in opSkillWriteConfirm.
 */
const path = require("path");
const { createApiClient, formatSkillResult } = require(path.join(
  __dirname,
  "../../../platform/api-client/apiClient.js"
));

/**
 * @param {{ baseUrl: string, token: string, fetchImpl?: typeof fetch, timeoutMs?: number }} opts
 */
function createOpenProjectClient(opts) {
  const token = opts.token || "";
  const basic = `Basic ${Buffer.from(`apikey:${token}`).toString("base64")}`;
  return createApiClient({
    baseUrl: String(opts.baseUrl || "").replace(/\/+$/, ""),
    serviceName: "OpenProject",
    timeoutMs: opts.timeoutMs,
    fetchImpl: opts.fetchImpl,
    authHeaders: {
      Authorization: basic,
      Accept: "application/json",
    },
  });
}

/**
 * Compatibility helper matching previous inline fetch error string returns.
 * @param {import('../../../platform/api-client/apiClient.js')} client
 * @param {string} method
 * @param {string} pathName
 * @param {{ body?: unknown, idempotencyKey?: string }} [req]
 * @param {(data: unknown) => string} [formatOk]
 */
async function opRequest(client, method, pathName, req = {}, formatOk) {
  const result = await client.request(method, pathName, req);
  return formatSkillResult(result, formatOk);
}

module.exports = {
  createOpenProjectClient,
  opRequest,
};
