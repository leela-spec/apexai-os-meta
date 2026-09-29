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
      case "list_query_filter_instance_schemas_for_project":
      missing = requireArgs(["id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "GET"; path = `/api/v3/projects/${encodeURIComponent(args.id)}/queries/filter_instance_schemas`;
      break;

      case "list_query_filter_instance_schemas":
      method = "GET"; path = `/api/v3/queries/filter_instance_schemas`;
      break;

      case "get":
      missing = requireArgs(["id"]); if (missing) return missing;
      method = "GET"; path = `/api/v3/queries/filter_instance_schemas/${encodeURIComponent(args.id)}`;
      break;

      case "list_query_filter_instance_schemas_for_workspace":
      missing = requireArgs(["id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "GET"; path = `/api/v3/workspace/${encodeURIComponent(args.id)}/queries/filter_instance_schemas`;
      break;
      default:
        return `Unbekannte operation: ${operation}`;
    }

    const confirmBlock = confirmOrNull({
      hubId: "openproject-query-filter-instance-schema",
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
