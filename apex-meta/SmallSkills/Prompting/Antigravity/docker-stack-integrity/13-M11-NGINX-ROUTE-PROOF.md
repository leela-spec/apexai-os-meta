# M11 — Prove, Fix, or Remove nginx Application Proxy Routes

## Goal

Establish whether the configured nginx application subpaths are genuinely usable against Firefly, Paperless and OpenProject. Keep only routes that work through the real products.

## Depends on

M04 PASS and current app runtime healthy.

## Required active context

Read only:

- correction control files;
- this module;
- `ki-basis/docker/nginx/default.conf`;
- nginx service section of `ki-basis/compose.yaml`;
- current live Firefly/Paperless/OpenProject endpoints;
- current official reverse-proxy/subpath guidance only for a product whose route fails.

Do not load unrelated module plans.

## Current defect

The prior acceptance report proves nginx `/healthz`, but does not prove the configured `/firefly/`, `/paperless/`, and `/openproject/` routes actually traverse nginx and result in usable application behavior. Some web applications require base-URL/subpath configuration and may not work correctly behind an arbitrary path prefix.

## Required method

For each configured nginx application route:

1. make a request through nginx, not the direct host port;
2. follow redirects in a controlled way;
3. inspect status, Location headers and returned product identity;
4. verify that generated links/assets/auth redirects remain on a usable route;
5. compare with the direct application endpoint.

## Allowed outcomes per product

Choose one evidence-backed outcome:

- `KEEP`: route works correctly as configured;
- `FIX`: apply the smallest supported nginx/app base-path correction and verify it;
- `REMOVE`: if the product does not support the intended subpath cleanly and direct localhost ports already satisfy the operator model, remove the misleading route rather than maintaining a broken facade.

The nginx health endpoint and stack index may remain even if one or more app subpaths are removed.

## Forbidden substitutes

- testing only `/healthz`;
- host-side direct application curl presented as proxy proof;
- accepting an initial `200/302` if subsequent app assets/navigation break;
- inventing unsupported rewrite behavior instead of following upstream proxy requirements.

## Verification

Positive:

- each retained route reaches the named real product through nginx Docker DNS;
- product identity/HTML/API response is observable;
- nginx config passes `nginx -t`;
- direct localhost app ports still work if retained by the architecture.

Negative/adversarial:

- temporarily point one disposable/test upstream to an invalid service name or port and prove the route fails through nginx;
- deliberate invalid nginx syntax must fail validation;
- search config for routes labeled as available but not proven.

## Acceptance

PASS when every nginx-advertised application route is either demonstrably functional or removed/marked unavailable, with no misleading proxy claims.

Persist M11 result with route-by-route KEEP/FIX/REMOVE evidence, update state, commit only nginx/app proxy configuration and directly related index labels, context-reset, continue M12.