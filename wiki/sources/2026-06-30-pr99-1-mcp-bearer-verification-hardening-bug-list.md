---
title: "MCP Bearer Verification Hardening Bug List - PR99.1"
category: source
type: checkpoint
created: 2026-06-30
updated: 2026-06-30
status: current
tags: [mcp, chatgpt-app, apps-sdk, auth, oauth, bearer-token, production-gate, bug-list]
---

# MCP Bearer Verification Hardening Bug List - PR99.1

PR285 merged PR99 production MCP bearer-token verification into `application-os-foundation`.

This follow-up bug list tracks the narrow PR99.1 hardening slice. It does not unlock MCP execution, JSON-RPC `tools/list`, JSON-RPC `tools/call`, provider calls, refresh tokens, account-link lifecycle, private beta, or public launch.

## Merge facts

- PR285: <https://github.com/panamini/neyssan/pull/285>
  - Title: `PR99: add production MCP bearer-token verification boundary`
  - Final head SHA: `eee8ad0e8bd0859a3dd4173d97d090ec57d0b326`
  - Merge commit SHA: `b306ea16f48bd7cf7591370949496d0c54e83ea9`
  - Merged at: `2026-06-30T02:09:10Z`
  - Base branch: `application-os-foundation`

## PR99 merged state

PR99 makes production `/mcp` parse `Authorization: Bearer <access_token>`, hash only the raw bearer token at the route edge, validate it against digest-backed access-token storage, and return an authenticated-MCP-blocked response on success.

The merged boundary keeps execution inert: no MCP execution, no `tools/list`, no `tools/call`, no provider calls, no refresh tokens, no production account-link lifecycle, no private beta, no public launch, and no UI changes.

## PR99.1 bug list

The next narrow fix slice is PR99.1 MCP bearer verification hardening:

- Add a per-caller `/mcp` bearer verification quota before Convex digest lookup so syntactically valid random tokens cannot force one storage lookup per request.
- Trust the storage-side access-token verification result for expiry and issued-at decisions, or apply only bounded route-side skew; do not reject a Convex `ok: true` proof with the app/Vite host clock.
- Challenge wrong-client and wrong-resource access tokens as `401 invalid_token`, not `403 forbidden`, so clients can restart authorization for the advertised protected resource.
- Serve production authorization-server metadata for the advertised issuer used by protected-resource metadata, so tokenless MCP clients can discover the authorize and token endpoints.

## Non-permissions

PR99.1 remains auth-boundary hardening only. It must not add MCP execution, `tools/list`, `tools/call`, provider calls, refresh tokens, production account-link lifecycle, consent UI, private beta, public launch behavior, billing/entitlements, live submit/apply, or provider-verified submission.

## Next state

Do not start PR100 or PR88/private beta/public launch until PR99.1 hardening is merged.

Historical note: after PR99.1, PR99.2 fixed forwarding-header trust in the `/mcp` bearer-verification quota, PR99.3 hardened caller-key canonicalization, PR100 added the authenticated MCP protocol/session envelope, and PR101 added the policy kernel plus metadata-only `tools/list`. The current next app PR is PR102 `tools/call` read-only boundary plus hardening.

## Touched pages

- [[product/chatgpt-app-sdk-roadmap]]
- [[hot]]
- [[index]]
