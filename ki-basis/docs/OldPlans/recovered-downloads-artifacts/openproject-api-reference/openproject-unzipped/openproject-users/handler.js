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
      case "list":
      method = "GET"; path = `/api/v3/users`;
      {
        const _qs = new URLSearchParams();
        if (args.offset !== undefined && args.offset !== null && String(args.offset).trim() !== "") _qs.set("offset", String(args.offset));
        if (args.pageSize !== undefined && args.pageSize !== null && String(args.pageSize).trim() !== "") _qs.set("pageSize", String(args.pageSize));
        if (args.filters !== undefined && args.filters !== null && String(args.filters).trim() !== "") _qs.set("filters", String(args.filters));
        if (args.sortBy !== undefined && args.sortBy !== null && String(args.sortBy).trim() !== "") _qs.set("sortBy", String(args.sortBy));
        if (args.select !== undefined && args.select !== null && String(args.select).trim() !== "") _qs.set("select", String(args.select));
        const _q = _qs.toString() ? `?${_qs.toString()}` : "";
        path = path + _q;
      }
      break;

      case "create":
      missing = requireArgs(["admin", "email", "login", "firstName", "lastName", "language"]); if (missing) return missing;
      method = "POST"; path = `/api/v3/users`;
      {
        const knownArgs = new Set(["operation", "confirmed", "offset", "pageSize", "filters", "sortBy", "select", "admin", "email", "login", "password", "currentPassword", "firstName", "lastName", "status", "language", "id"]);
        for (const key of Object.keys(args)) {
          if (knownArgs.has(key)) continue;
          if (args[key] === undefined || args[key] === null || String(args[key]).trim() === "") continue;
          return `Unbekanntes Feld für operation=${operation}: ${key}`;
        }
      }
      body = {};
      if (args.admin !== undefined && args.admin !== null && String(args.admin).trim() !== "") {
        {
          const _raw = args.admin;
          if (typeof _raw === "boolean") {
            body["admin"] = _raw;
          } else {
            const _s = String(_raw).trim().toLowerCase();
            if (_s !== "true" && _s !== "false" && _s !== "1" && _s !== "0") {
              return `admin muss boolean sein (got: ${args.admin})`;
            }
            body["admin"] = (_s === "true" || _s === "1");
          }
        }
      }
      if (args.email !== undefined && args.email !== null && String(args.email).trim() !== "") {
        body["email"] = args.email;
      }
      if (args.login !== undefined && args.login !== null && String(args.login).trim() !== "") {
        body["login"] = args.login;
      }
      if (args.password !== undefined && args.password !== null && String(args.password).trim() !== "") {
        body["password"] = args.password;
      }
      if (args.currentPassword !== undefined && args.currentPassword !== null && String(args.currentPassword).trim() !== "") {
        body["currentPassword"] = args.currentPassword;
      }
      if (args.firstName !== undefined && args.firstName !== null && String(args.firstName).trim() !== "") {
        body["firstName"] = args.firstName;
      }
      if (args.lastName !== undefined && args.lastName !== null && String(args.lastName).trim() !== "") {
        body["lastName"] = args.lastName;
      }
      if (args.status !== undefined && args.status !== null && String(args.status).trim() !== "") {
        body["status"] = args.status;
      }
      if (args.language !== undefined && args.language !== null && String(args.language).trim() !== "") {
        body["language"] = args.language;
      }
      break;

      case "get_schema":
      method = "GET"; path = `/api/v3/users/schema`;
      break;

      case "delete":
      missing = requireArgs(["id"]); if (missing) return missing;
      method = "DELETE"; path = `/api/v3/users/${encodeURIComponent(args.id)}`;
      break;

      case "get":
      missing = requireArgs(["id"]); if (missing) return missing;
      method = "GET"; path = `/api/v3/users/${encodeURIComponent(args.id)}`;
      break;

      case "update":
      missing = requireArgs(["id", "admin", "email", "login", "firstName", "lastName", "language"]); if (missing) return missing;
      method = "PATCH"; path = `/api/v3/users/${encodeURIComponent(args.id)}`;
      {
        const knownArgs = new Set(["operation", "confirmed", "offset", "pageSize", "filters", "sortBy", "select", "admin", "email", "login", "password", "currentPassword", "firstName", "lastName", "status", "language", "id"]);
        for (const key of Object.keys(args)) {
          if (knownArgs.has(key)) continue;
          if (args[key] === undefined || args[key] === null || String(args[key]).trim() === "") continue;
          return `Unbekanntes Feld für operation=${operation}: ${key}`;
        }
      }
      body = {};
      if (args.admin !== undefined && args.admin !== null && String(args.admin).trim() !== "") {
        {
          const _raw = args.admin;
          if (typeof _raw === "boolean") {
            body["admin"] = _raw;
          } else {
            const _s = String(_raw).trim().toLowerCase();
            if (_s !== "true" && _s !== "false" && _s !== "1" && _s !== "0") {
              return `admin muss boolean sein (got: ${args.admin})`;
            }
            body["admin"] = (_s === "true" || _s === "1");
          }
        }
      }
      if (args.email !== undefined && args.email !== null && String(args.email).trim() !== "") {
        body["email"] = args.email;
      }
      if (args.login !== undefined && args.login !== null && String(args.login).trim() !== "") {
        body["login"] = args.login;
      }
      if (args.password !== undefined && args.password !== null && String(args.password).trim() !== "") {
        body["password"] = args.password;
      }
      if (args.currentPassword !== undefined && args.currentPassword !== null && String(args.currentPassword).trim() !== "") {
        body["currentPassword"] = args.currentPassword;
      }
      if (args.firstName !== undefined && args.firstName !== null && String(args.firstName).trim() !== "") {
        body["firstName"] = args.firstName;
      }
      if (args.lastName !== undefined && args.lastName !== null && String(args.lastName).trim() !== "") {
        body["lastName"] = args.lastName;
      }
      if (args.status !== undefined && args.status !== null && String(args.status).trim() !== "") {
        body["status"] = args.status;
      }
      if (args.language !== undefined && args.language !== null && String(args.language).trim() !== "") {
        body["language"] = args.language;
      }
      break;

      case "update_form":
      missing = requireArgs(["id"]); if (missing) return missing;
      method = "POST"; path = `/api/v3/users/${encodeURIComponent(args.id)}/form`;
      body = undefined;
      break;

      case "unlock":
      missing = requireArgs(["id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "DELETE"; path = `/api/v3/users/${encodeURIComponent(args.id)}/lock`;
      break;

      case "lock":
      missing = requireArgs(["id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "POST"; path = `/api/v3/users/${encodeURIComponent(args.id)}/lock`;
      body = undefined;
      break;
      default:
        return `Unbekannte operation: ${operation}`;
    }

    const confirmBlock = confirmOrNull({
      hubId: "openproject-users",
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
