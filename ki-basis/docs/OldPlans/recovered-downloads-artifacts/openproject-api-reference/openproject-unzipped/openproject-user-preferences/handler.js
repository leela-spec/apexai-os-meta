const { confirmOrNull } = require("../_lib/opSkillWriteConfirm.js");

module.exports.runtime = {
  handler: async function (args) {
    args = args || {};
    const runtime = this.runtimeArgs || {};
    const base = (runtime.openproject_base_url || "http://web:8080").replace(/\/+$/, "");
    const token = runtime.openproject_token || "";
    const basic = `Basic ${Buffer.from(`apikey:${token}`).toString("base64")}`;
    const headers = { Authorization: basic, Accept: "application/json" };
    const operation = String(args.operation || "").trim();
    if (!operation) return "Bitte operation angeben.";

    const requireArgs = (names) => {
      for (const n of names) {
        if (args[n] === undefined || args[n] === null || args[n] === "") {
          return `Pflichtfeld fehlt für operation=${operation}: ${n}`;
        }
      }
      return null;
    };

    let method, path, body, missing;
    switch (operation) {
      case "get_my_preferences":
      method = "GET"; path = `/api/v3/my_preferences`;
      break;

      case "update":
      method = "PATCH"; path = `/api/v3/my_preferences`;
      {
        const knownArgs = new Set(["operation", "confirmed", "autoHidePopups", "timeZone"]);
        for (const key of Object.keys(args)) {
          if (knownArgs.has(key)) continue;
          if (args[key] === undefined || args[key] === null || String(args[key]).trim() === "") continue;
          return `Unbekanntes Feld für operation=${operation}: ${key}`;
        }
      }
      body = {};
      if (args.autoHidePopups !== undefined && args.autoHidePopups !== null && String(args.autoHidePopups).trim() !== "") {
        {
          const _raw = args.autoHidePopups;
          if (typeof _raw === "boolean") {
            body["autoHidePopups"] = _raw;
          } else {
            const _s = String(_raw).trim().toLowerCase();
            if (_s !== "true" && _s !== "false" && _s !== "1" && _s !== "0") {
              return `autoHidePopups muss boolean sein (got: ${args.autoHidePopups})`;
            }
            body["autoHidePopups"] = (_s === "true" || _s === "1");
          }
        }
      }
      if (args.timeZone !== undefined && args.timeZone !== null && String(args.timeZone).trim() !== "") {
        body["timeZone"] = args.timeZone;
      }
      break;
      default:
        return `Unbekannte operation: ${operation}`;
    }

    const confirmBlock = confirmOrNull({
      hubId: "openproject-user-preferences",
      operation,
      method,
      args,
    });
    if (confirmBlock) return confirmBlock;

    try {
      const res = await fetch(`${base}${path}`, {
        method,
        headers: body ? { ...headers, "Content-Type": "application/json" } : headers,
        body: body ? JSON.stringify(body) : undefined,
      });
      if (!res.ok) return `OpenProject-Fehler ${res.status}: ${await res.text()}`;
      const _raw = await res.text();
      if (!_raw || !String(_raw).trim()) {
        if (String(method).toUpperCase() === "DELETE") return "Gelöscht.";
        return `(leer, HTTP ${res.status})`;
      }
      let item;
      try { item = JSON.parse(_raw); }
      catch (e) { return `Fehler beim Aufruf von OpenProject: ${e.message}`; }
      // AnythingLLM surfaces skill returns as-is — Markdown table with header.
      if (item && item._type && (item._type === "Collection" || String(item._type).endsWith("Collection"))) {
        const els = (item._embedded && item._embedded.elements) ? item._embedded.elements : [];
        if (!els.length) return `Keine Benutzer (total=${item.total ?? 0}).`;
        const cell = (v) => String(v ?? "-").replace(/\|/g, "/").replace(/\r?\n/g, " ");
        const rows = els.map((u) => {
          const admin = u.admin ? "ja" : "nein";
          return `| ${u.id ?? "?"} | ${cell(u.name)} | ${cell(u.login)} | ${cell(u.email)} | ${cell(u.status)} | ${admin} |`;
        });
        return [
          `Benutzer (${els.length}/${item.total ?? els.length})`,
          "",
          "| ID | Name | Login | E-Mail | Status | Admin |",
          "| --- | --- | --- | --- | --- | --- |",
          ...rows,
        ].join("\n");
      }
      if (item && (item._type === "User" || item.login !== undefined)) {
        const cell = (v) => String(v ?? "-").replace(/\|/g, "/").replace(/\r?\n/g, " ");
        const admin = item.admin ? "ja" : "nein";
        return [
          "| ID | Name | Login | E-Mail | Status | Admin |",
          "| --- | --- | --- | --- | --- | --- |",
          `| ${item.id} | ${cell(item.name)} | ${cell(item.login)} | ${cell(item.email)} | ${cell(item.status)} | ${admin} |`,
        ].join("\n");
      }
      return JSON.stringify(item, null, 2).slice(0, 4000);
    } catch (e) {
      return `Fehler beim Aufruf von OpenProject: ${e.message}`;
    }
  },
};
