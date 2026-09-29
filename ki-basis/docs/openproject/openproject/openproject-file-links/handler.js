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
      case "delete":
      missing = requireArgs(["id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "DELETE"; path = `/api/v3/file_links/${encodeURIComponent(args.id)}`;
      break;

      case "get":
      missing = requireArgs(["id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "GET"; path = `/api/v3/file_links/${encodeURIComponent(args.id)}`;
      break;

      case "download":
      missing = requireArgs(["id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "GET"; path = `/api/v3/file_links/${encodeURIComponent(args.id)}/download`;
      break;

      case "open":
      missing = requireArgs(["id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "GET"; path = `/api/v3/file_links/${encodeURIComponent(args.id)}/open`;
      {
        const _qs = new URLSearchParams();
        if (args.location !== undefined && args.location !== null && String(args.location).trim() !== "") _qs.set("location", String(args.location));
        const _q = _qs.toString() ? `?${_qs.toString()}` : "";
        path = path + _q;
      }
      break;

      case "list_project_storages":
      method = "GET"; path = `/api/v3/project_storages`;
      {
        const _qs = new URLSearchParams();
        if (args.filters !== undefined && args.filters !== null && String(args.filters).trim() !== "") _qs.set("filters", String(args.filters));
        const _q = _qs.toString() ? `?${_qs.toString()}` : "";
        path = path + _q;
      }
      break;

      case "get_project_storage":
      missing = requireArgs(["id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "GET"; path = `/api/v3/project_storages/${encodeURIComponent(args.id)}`;
      break;

      case "open_project_storage":
      missing = requireArgs(["id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "GET"; path = `/api/v3/project_storages/${encodeURIComponent(args.id)}/open`;
      break;

      case "list_storages":
      method = "GET"; path = `/api/v3/storages`;
      break;

      case "create_storage":
      method = "POST"; path = `/api/v3/storages`;
      {
        const knownArgs = new Set(["operation", "confirmed", "id", "location", "filters", "name", "storageAudience", "tokenExchangeScope", "applicationPassword", "forbiddenFileNameCharacters", "parent", "projectId", "fileName", "parentId", "clientId", "clientSecret"]);
        for (const key of Object.keys(args)) {
          if (knownArgs.has(key)) continue;
          if (args[key] === undefined || args[key] === null || String(args[key]).trim() === "") continue;
          return `Unbekanntes Feld für operation=${operation}: ${key}`;
        }
      }
      body = {};
      if (args.name !== undefined && args.name !== null && String(args.name).trim() !== "") {
        body["name"] = args.name;
      }
      if (args.storageAudience !== undefined && args.storageAudience !== null && String(args.storageAudience).trim() !== "") {
        body["storageAudience"] = args.storageAudience;
      }
      if (args.tokenExchangeScope !== undefined && args.tokenExchangeScope !== null && String(args.tokenExchangeScope).trim() !== "") {
        body["tokenExchangeScope"] = args.tokenExchangeScope;
      }
      if (args.applicationPassword !== undefined && args.applicationPassword !== null && String(args.applicationPassword).trim() !== "") {
        body["applicationPassword"] = args.applicationPassword;
      }
      if (args.forbiddenFileNameCharacters !== undefined && args.forbiddenFileNameCharacters !== null && String(args.forbiddenFileNameCharacters).trim() !== "") {
        body["forbiddenFileNameCharacters"] = args.forbiddenFileNameCharacters;
      }
      break;

      case "delete_storage":
      missing = requireArgs(["id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "DELETE"; path = `/api/v3/storages/${encodeURIComponent(args.id)}`;
      break;

      case "get_storage":
      missing = requireArgs(["id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "GET"; path = `/api/v3/storages/${encodeURIComponent(args.id)}`;
      break;

      case "update_storage":
      missing = requireArgs(["id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "PATCH"; path = `/api/v3/storages/${encodeURIComponent(args.id)}`;
      {
        const knownArgs = new Set(["operation", "confirmed", "id", "location", "filters", "name", "storageAudience", "tokenExchangeScope", "applicationPassword", "forbiddenFileNameCharacters", "parent", "projectId", "fileName", "parentId", "clientId", "clientSecret"]);
        for (const key of Object.keys(args)) {
          if (knownArgs.has(key)) continue;
          if (args[key] === undefined || args[key] === null || String(args[key]).trim() === "") continue;
          return `Unbekanntes Feld für operation=${operation}: ${key}`;
        }
      }
      body = {};
      if (args.name !== undefined && args.name !== null && String(args.name).trim() !== "") {
        body["name"] = args.name;
      }
      if (args.storageAudience !== undefined && args.storageAudience !== null && String(args.storageAudience).trim() !== "") {
        body["storageAudience"] = args.storageAudience;
      }
      if (args.tokenExchangeScope !== undefined && args.tokenExchangeScope !== null && String(args.tokenExchangeScope).trim() !== "") {
        body["tokenExchangeScope"] = args.tokenExchangeScope;
      }
      if (args.applicationPassword !== undefined && args.applicationPassword !== null && String(args.applicationPassword).trim() !== "") {
        body["applicationPassword"] = args.applicationPassword;
      }
      if (args.forbiddenFileNameCharacters !== undefined && args.forbiddenFileNameCharacters !== null && String(args.forbiddenFileNameCharacters).trim() !== "") {
        body["forbiddenFileNameCharacters"] = args.forbiddenFileNameCharacters;
      }
      break;

      case "get_storage_files":
      missing = requireArgs(["id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "GET"; path = `/api/v3/storages/${encodeURIComponent(args.id)}/files`;
      {
        const _qs = new URLSearchParams();
        if (args.parent !== undefined && args.parent !== null && String(args.parent).trim() !== "") _qs.set("parent", String(args.parent));
        const _q = _qs.toString() ? `?${_qs.toString()}` : "";
        path = path + _q;
      }
      break;

      case "prepare_storage_file_upload":
      missing = requireArgs(["id", "projectId", "fileName", "parent"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      {
        if (args.projectId !== undefined && args.projectId !== null && String(args.projectId).trim() !== "") {
          const _n = Number(args.projectId);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `projectId muss eine ganze Zahl und >= 1 sein (got: ${args.projectId})`;
          }
        }
      }
      method = "POST"; path = `/api/v3/storages/${encodeURIComponent(args.id)}/files/prepare_upload`;
      {
        const knownArgs = new Set(["operation", "confirmed", "id", "location", "filters", "name", "storageAudience", "tokenExchangeScope", "applicationPassword", "forbiddenFileNameCharacters", "parent", "projectId", "fileName", "parentId", "clientId", "clientSecret"]);
        for (const key of Object.keys(args)) {
          if (knownArgs.has(key)) continue;
          if (args[key] === undefined || args[key] === null || String(args[key]).trim() === "") continue;
          return `Unbekanntes Feld für operation=${operation}: ${key}`;
        }
      }
      body = {};
      if (args.projectId !== undefined && args.projectId !== null && String(args.projectId).trim() !== "") {
        {
          const _n = Number(args.projectId);
          body["projectId"] = Number.isNaN(_n) ? args.projectId : _n;
        }
      }
      if (args.fileName !== undefined && args.fileName !== null && String(args.fileName).trim() !== "") {
        body["fileName"] = args.fileName;
      }
      if (args.parent !== undefined && args.parent !== null && String(args.parent).trim() !== "") {
        body["parent"] = args.parent;
      }
      break;

      case "create_storage_folder":
      missing = requireArgs(["id", "name", "parentId"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "POST"; path = `/api/v3/storages/${encodeURIComponent(args.id)}/folders`;
      {
        const knownArgs = new Set(["operation", "confirmed", "id", "location", "filters", "name", "storageAudience", "tokenExchangeScope", "applicationPassword", "forbiddenFileNameCharacters", "parent", "projectId", "fileName", "parentId", "clientId", "clientSecret"]);
        for (const key of Object.keys(args)) {
          if (knownArgs.has(key)) continue;
          if (args[key] === undefined || args[key] === null || String(args[key]).trim() === "") continue;
          return `Unbekanntes Feld für operation=${operation}: ${key}`;
        }
      }
      body = {};
      if (args.name !== undefined && args.name !== null && String(args.name).trim() !== "") {
        body["name"] = args.name;
      }
      if (args.parentId !== undefined && args.parentId !== null && String(args.parentId).trim() !== "") {
        body["parentId"] = args.parentId;
      }
      break;

      case "create_storage_oauth_credentials":
      missing = requireArgs(["id", "clientId", "clientSecret"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "POST"; path = `/api/v3/storages/${encodeURIComponent(args.id)}/oauth_client_credentials`;
      {
        const knownArgs = new Set(["operation", "confirmed", "id", "location", "filters", "name", "storageAudience", "tokenExchangeScope", "applicationPassword", "forbiddenFileNameCharacters", "parent", "projectId", "fileName", "parentId", "clientId", "clientSecret"]);
        for (const key of Object.keys(args)) {
          if (knownArgs.has(key)) continue;
          if (args[key] === undefined || args[key] === null || String(args[key]).trim() === "") continue;
          return `Unbekanntes Feld für operation=${operation}: ${key}`;
        }
      }
      body = {};
      if (args.clientId !== undefined && args.clientId !== null && String(args.clientId).trim() !== "") {
        body["clientId"] = args.clientId;
      }
      if (args.clientSecret !== undefined && args.clientSecret !== null && String(args.clientSecret).trim() !== "") {
        body["clientSecret"] = args.clientSecret;
      }
      break;

      case "open_storage":
      missing = requireArgs(["id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "GET"; path = `/api/v3/storages/${encodeURIComponent(args.id)}/open`;
      break;
      default:
        return `Unbekannte operation: ${operation}`;
    }

    const confirmBlock = confirmOrNull({
      hubId: "openproject-file-links",
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
      // formatHalResponse — Markdown table with header (AnythingLLM shows skill returns as-is).
      // Signature: formatHalResponse(item: object) -> string
      // Handles Collection / *Collection, DRF {count, results}, and single resources.
      // HAL link titles (status/assignee/type/project/parent) + lockVersion for PM update flows.
      const cell = (v) => {
        if (v === null || v === undefined) return "-";
        if (typeof v === "object") {
          if (typeof v.raw === "string") return String(v.raw).replace(/\|/g, "/").replace(/\r?\n/g, " ").slice(0, 80) || "-";
          if (v.title) return String(v.title).replace(/\|/g, "/").replace(/\r?\n/g, " ");
          if (v.href) {
            const m = String(v.href).match(/\/(\d+)(?:\/)?$/);
            return m ? m[1] : String(v.href).replace(/\|/g, "/").slice(-40);
          }
          return "-";
        }
        return String(v).replace(/\|/g, "/").replace(/\r?\n/g, " ");
      };
      const linkTitle = (e, rel) => {
        const l = e && e._links && e._links[rel];
        if (!l) return undefined;
        const node = Array.isArray(l) ? l[0] : l;
        if (!node) return undefined;
        if (node.title) return node.title;
        if (node.href) {
          const m = String(node.href).match(/\/(\d+)(?:\/)?$/);
          return m ? `#${m[1]}` : undefined;
        }
        return undefined;
      };
      const fieldVal = (e, k) => {
        if (!e) return undefined;
        if (e[k] !== undefined && e[k] !== null && typeof e[k] !== "object") return e[k];
        if (k === "status") return linkTitle(e, "status");
        if (k === "assignee") return linkTitle(e, "assignee");
        if (k === "type" || k === "typeName") return linkTitle(e, "type");
        if (k === "project") return linkTitle(e, "project");
        if (k === "parent") return linkTitle(e, "parent");
        if (k === "priority") return linkTitle(e, "priority");
        if (k === "author") return linkTitle(e, "author");
        if (k === "lockVersion" && e.lockVersion !== undefined && e.lockVersion !== null) return e.lockVersion;
        return undefined;
      };
      const hasField = (e, k) => fieldVal(e, k) !== undefined;
      const LABELS = {
        de: {
          id: "ID", name: "Name", subject: "Betreff", title: "Titel", identifier: "Kennung",
          login: "Login", email: "E-Mail", status: "Status", active: "aktiv",
          createdAt: "erstellt", updatedAt: "aktualisiert", firstName: "Vorname", lastName: "Nachname",
          firstname: "Vorname", lastname: "Nachname",
          lockVersion: "lockVersion", assignee: "Assignee", type: "Typ", typeName: "Typ",
          project: "Projekt", parent: "Parent", priority: "Priorität", author: "Autor",
          percentageDone: "%", dueDate: "fällig", startDate: "Start",
        },
        en: {
          id: "ID", name: "Name", subject: "Subject", title: "Title", identifier: "Identifier",
          login: "Login", email: "E-Mail", status: "Status", active: "active",
          createdAt: "created", updatedAt: "updated", firstName: "First name", lastName: "Last name",
          firstname: "First name", lastname: "Last name",
          lockVersion: "lockVersion", assignee: "Assignee", type: "Type", typeName: "Type",
          project: "Project", parent: "Parent", priority: "Priority", author: "Author",
          percentageDone: "%", dueDate: "due", startDate: "Start",
        },
      };
      const UI = {
        de: {
          empty: (total) => `Keine Einträge (total=${total ?? 0}).`,
          entries: (n, total) => `Einträge (${n}/${total})`,
        },
        en: {
          empty: (total) => `No entries (total=${total ?? 0}).`,
          entries: (n, total) => `Entries (${n}/${total})`,
        },
      };
      const resolveLocale = () => {
        const raw =
          (args && (args.locale || args.lang)) ||
          (typeof runtime !== "undefined" && runtime && (runtime.locale || runtime.language)) ||
          (typeof this !== "undefined" && this && this.runtimeArgs && (this.runtimeArgs.locale || this.runtimeArgs.language)) ||
          "de";
        const s = String(raw || "de").toLowerCase();
        return s.startsWith("en") ? "en" : "de";
      };
      const locale = resolveLocale();
      const labels = LABELS[locale] || LABELS.de;
      const ui = UI[locale] || UI.de;
      const preferred = [
        "id", "name", "subject", "title", "identifier", "status", "type", "assignee",
        "project", "parent", "priority", "lockVersion", "percentageDone", "startDate", "dueDate",
        "login", "email", "active", "createdAt", "updatedAt", "firstName", "lastName", "firstname", "lastname",
      ];
      const collectionTable = (els, total) => {
        if (!els.length) return ui.empty(total ?? 0);
        let cols = preferred.filter((k) => els.some((e) => hasField(e, k)));
        if (!cols.length) {
          const keys = Object.keys(els[0] || {}).filter((k) => !k.startsWith("_") && typeof els[0][k] !== "object");
          cols = keys.slice(0, 8);
        }
        if (!cols.includes("id") && els[0] && els[0].id !== undefined) cols = ["id", ...cols.filter((c) => c !== "id")];
        cols = cols.slice(0, 10);
        const header = "| " + cols.map((c) => labels[c] || c).join(" | ") + " |";
        const sep = "| " + cols.map(() => "---").join(" | ") + " |";
        const rows = els.map((e) => "| " + cols.map((c) => cell(fieldVal(e, c))).join(" | ") + " |");
        return [ui.entries(els.length, total ?? els.length), "", header, sep, ...rows].join("\n");
      };
      if (item && item._type && (item._type === "Collection" || String(item._type).endsWith("Collection"))) {
        const els = (item._embedded && item._embedded.elements) ? item._embedded.elements : [];
        return collectionTable(els, item.total);
      }
      if (item && Array.isArray(item.results)) {
        return collectionTable(item.results, item.count);
      }
      if (item && typeof item === "object" && item._type && item._type !== "Error") {
        const cols = preferred.filter((k) => hasField(item, k)).slice(0, 10);
        if (cols.length) {
          return [
            "| " + cols.map((c) => labels[c] || c).join(" | ") + " |",
            "| " + cols.map(() => "---").join(" | ") + " |",
            "| " + cols.map((c) => cell(fieldVal(item, c))).join(" | ") + " |",
          ].join("\n");
        }
      }
      return JSON.stringify(item, null, 2).slice(0, 4000);

    } catch (e) {
      return `Fehler beim Aufruf von OpenProject: ${e.message}`;
    }
  },
};
