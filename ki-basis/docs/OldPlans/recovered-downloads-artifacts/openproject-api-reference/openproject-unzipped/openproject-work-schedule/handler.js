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
      case "list_days":
      method = "GET"; path = `/api/v3/days`;
      {
        const _qs = new URLSearchParams();
        if (args.filters !== undefined && args.filters !== null && String(args.filters).trim() !== "") _qs.set("filters", String(args.filters));
        const _q = _qs.toString() ? `?${_qs.toString()}` : "";
        path = path + _q;
      }
      break;

      case "list_non_working_days":
      method = "GET"; path = `/api/v3/days/non_working`;
      {
        const _qs = new URLSearchParams();
        if (args.filters !== undefined && args.filters !== null && String(args.filters).trim() !== "") _qs.set("filters", String(args.filters));
        const _q = _qs.toString() ? `?${_qs.toString()}` : "";
        path = path + _q;
      }
      break;

      case "create_non_working_day":
      missing = requireArgs(["_type", "date", "name"]); if (missing) return missing;
      method = "POST"; path = `/api/v3/days/non_working`;
      {
        const knownArgs = new Set(["operation", "confirmed", "filters", "_type", "date", "name", "_embedded", "day", "working"]);
        for (const key of Object.keys(args)) {
          if (knownArgs.has(key)) continue;
          if (args[key] === undefined || args[key] === null || String(args[key]).trim() === "") continue;
          return `Unbekanntes Feld für operation=${operation}: ${key}`;
        }
      }
      body = {};
      if (args._type !== undefined && args._type !== null && String(args._type).trim() !== "") {
        {
          const _allowed = ["NonWorkingDay"];
          if (!_allowed.includes(String(args._type))) {
            return `_type muss einer von: ${_allowed.join(", ")} sein (got: ${args._type})`;
          }
        }
        body["_type"] = args._type;
      }
      if (args.date !== undefined && args.date !== null && String(args.date).trim() !== "") {
        body["date"] = args.date;
      }
      if (args.name !== undefined && args.name !== null && String(args.name).trim() !== "") {
        body["name"] = args.name;
      }
      break;

      case "delete_non_working_day":
      missing = requireArgs(["date"]); if (missing) return missing;
      method = "DELETE"; path = `/api/v3/days/non_working/${encodeURIComponent(args.date)}`;
      break;

      case "get_non_working_day":
      missing = requireArgs(["date"]); if (missing) return missing;
      method = "GET"; path = `/api/v3/days/non_working/${encodeURIComponent(args.date)}`;
      break;

      case "update_non_working_day":
      missing = requireArgs(["date", "_type", "name"]); if (missing) return missing;
      method = "PATCH"; path = `/api/v3/days/non_working/${encodeURIComponent(args.date)}`;
      {
        const knownArgs = new Set(["operation", "confirmed", "filters", "_type", "date", "name", "_embedded", "day", "working"]);
        for (const key of Object.keys(args)) {
          if (knownArgs.has(key)) continue;
          if (args[key] === undefined || args[key] === null || String(args[key]).trim() === "") continue;
          return `Unbekanntes Feld für operation=${operation}: ${key}`;
        }
      }
      body = {};
      if (args._type !== undefined && args._type !== null && String(args._type).trim() !== "") {
        {
          const _allowed = ["NonWorkingDay"];
          if (!_allowed.includes(String(args._type))) {
            return `_type muss einer von: ${_allowed.join(", ")} sein (got: ${args._type})`;
          }
        }
        body["_type"] = args._type;
      }
      if (args.name !== undefined && args.name !== null && String(args.name).trim() !== "") {
        body["name"] = args.name;
      }
      break;

      case "list_week_days":
      method = "GET"; path = `/api/v3/days/week`;
      break;

      case "update_week_days":
      missing = requireArgs(["_type", "_embedded"]); if (missing) return missing;
      method = "PATCH"; path = `/api/v3/days/week`;
      {
        const knownArgs = new Set(["operation", "confirmed", "filters", "_type", "date", "name", "_embedded", "day", "working"]);
        for (const key of Object.keys(args)) {
          if (knownArgs.has(key)) continue;
          if (args[key] === undefined || args[key] === null || String(args[key]).trim() === "") continue;
          return `Unbekanntes Feld für operation=${operation}: ${key}`;
        }
      }
      body = {};
      if (args._type !== undefined && args._type !== null && String(args._type).trim() !== "") {
        {
          const _allowed = ["Collection"];
          if (!_allowed.includes(String(args._type))) {
            return `_type muss einer von: ${_allowed.join(", ")} sein (got: ${args._type})`;
          }
        }
        body["_type"] = args._type;
      }
      if (args._embedded !== undefined && args._embedded !== null && String(args._embedded).trim() !== "") {
        let _v__embedded = args._embedded;
        if (typeof _v__embedded === "string") {
          const _s = String(_v__embedded).trim();
          if (_s.startsWith("{") || _s.startsWith("[")) {
            try { _v__embedded = JSON.parse(_s); }
            catch (e) { _v__embedded = { raw: _s }; }
          } else {
            _v__embedded = { raw: _s };
          }
        }
        if (typeof _v__embedded !== "object" || _v__embedded === null || Array.isArray(_v__embedded)) {
          return `_embedded muss ein Objekt sein (z.B. Formattable mit raw: string)`;
        }
        body["_embedded"] = _v__embedded;
      }
      break;

      case "get_week_day":
      missing = requireArgs(["day"]); if (missing) return missing;
      {
        if (args.day !== undefined && args.day !== null && String(args.day).trim() !== "") {
          const _n = Number(args.day);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `day muss eine ganze Zahl und >= 1 sein (got: ${args.day})`;
          }
        }
      }
      method = "GET"; path = `/api/v3/days/week/${encodeURIComponent(args.day)}`;
      break;

      case "update_week_day":
      missing = requireArgs(["day", "_type", "working"]); if (missing) return missing;
      {
        if (args.day !== undefined && args.day !== null && String(args.day).trim() !== "") {
          const _n = Number(args.day);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `day muss eine ganze Zahl und >= 1 sein (got: ${args.day})`;
          }
        }
      }
      method = "PATCH"; path = `/api/v3/days/week/${encodeURIComponent(args.day)}`;
      {
        const knownArgs = new Set(["operation", "confirmed", "filters", "_type", "date", "name", "_embedded", "day", "working"]);
        for (const key of Object.keys(args)) {
          if (knownArgs.has(key)) continue;
          if (args[key] === undefined || args[key] === null || String(args[key]).trim() === "") continue;
          return `Unbekanntes Feld für operation=${operation}: ${key}`;
        }
      }
      body = {};
      if (args._type !== undefined && args._type !== null && String(args._type).trim() !== "") {
        {
          const _allowed = ["WeekDay"];
          if (!_allowed.includes(String(args._type))) {
            return `_type muss einer von: ${_allowed.join(", ")} sein (got: ${args._type})`;
          }
        }
        body["_type"] = args._type;
      }
      if (args.working !== undefined && args.working !== null && String(args.working).trim() !== "") {
        {
          const _raw = args.working;
          if (typeof _raw === "boolean") {
            body["working"] = _raw;
          } else {
            const _s = String(_raw).trim().toLowerCase();
            if (_s !== "true" && _s !== "false" && _s !== "1" && _s !== "0") {
              return `working muss boolean sein (got: ${args.working})`;
            }
            body["working"] = (_s === "true" || _s === "1");
          }
        }
      }
      break;

      case "get_day":
      missing = requireArgs(["date"]); if (missing) return missing;
      method = "GET"; path = `/api/v3/days/${encodeURIComponent(args.date)}`;
      break;
      default:
        return `Unbekannte operation: ${operation}`;
    }

    const confirmBlock = confirmOrNull({
      hubId: "openproject-work-schedule",
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
