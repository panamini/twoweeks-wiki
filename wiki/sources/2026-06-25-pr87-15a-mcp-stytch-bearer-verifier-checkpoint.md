---
title: "MCP Stytch Bearer Verifier Boundary Checkpoint - PR87.15A"
category: source
tags: [chatgpt-app, apps-sdk, mcp, auth, stytch, checkpoint, pr87-15a]
created: 2026-06-25
updated: 2026-06-25
status: current
type: analysis
related: [[product/chatgpt-app-sdk-roadmap]], [[product/manual-application-handoff]], [[sources/2026-06-24-pr87-14b-mcp-auth-dev-endpoint-wiring-checkpoint]], [[sources/2026-06-24-pr87-14a-mcp-auth-request-orchestrator-checkpoint]], [[sources/2026-06-24-pr87-13-mcp-auth-policy-boundary-checkpoint]]
---

# MCP Stytch Bearer Verifier Boundary Checkpoint - PR87.15A

## Summary

PR257, [PR87.15A: add MCP Stytch bearer verifier boundary](https://github.com/panamini/neyssan/pull/257), merged the server-only Stytch bearer verifier boundary into `application-os-foundation`. It adds local JWT verification against server-provided JWKS and focused fail-closed tests, but does not wire the verifier into runtime.

## Key points

- PR257 merged into `application-os-foundation` as merge commit `372d16830dd6d3b66f39ba96e317641dcb207793` on 2026-06-24 UTC.
- The original reviewed head SHA was `a89b2ed6005a7ac3fe2ea5bbaee7ba13fbc81966`.
- The final merged head SHA after CodeRabbit fixes was `00172f63a8a49d28756150e611a5371d615f2de3`.
- The changed files stayed exactly:
  - `my-app/src/modules/local-mcp/mcpStytchBearerVerifierBoundary.ts`
  - `my-app/src/modules/local-mcp/__tests__/mcpStytchBearerVerifierBoundary.test.ts`
- Server-only verifier config validation enforces:
  - provider `stytch`
  - HTTPS issuer and audience/resource
  - `jwksSource: "server_only_config"`
  - `tokenStorage: "none"`
  - RS256 only
  - canonical `twoweeks:applications:read`
  - legacy dotted scopes rejected.
- Verifier behavior now fails closed for compact JWT format, protected header `alg`/`kid`, duplicate or unknown `kid`, issuer, audience/resource, `exp`, `nbf`, `client_id`/`azp`, provider environment, and missing canonical scope.
- Signature verification uses server-provided JWKS through the local verifier boundary only.
- Semantic claim rejection runs only after `jwtVerify` succeeds; malformed JWT parsing remains only a structural precheck.
- Provider environment is required to match explicitly; tokens with no provider-environment claim fail closed.
- Raw tokens are never echoed in failure responses.
- CodeRabbit initially posted four actionable comments; commit `00172f63a8a49d28756150e611a5371d615f2de3` fixed them, and the latest CodeRabbit review reported no actionable comments.

## Validation

- Focused Stytch verifier suite: 38 tests passed.
- Adjacent Stytch/OAuth/orchestrator/policy suites: 188 tests passed.
- Full local-MCP suite: 59 files / 1377 tests passed.
- `rtk npx tsc --noEmit --pretty false`: passed.
- Targeted ESLint on changed files: passed.
- `rtk git diff --check`: passed.
- GitHub `js-tests`, Playwright `test`, and CodeRabbit checks were green before merge.
- `npm run build` remained red only on inherited Convex `_generated` baseline errors; changed-file filtering had no local-MCP or verifier hits.

## Implications

PR87.15A is a verifier boundary only. It does not permit or implement production `/mcp`, production `tools/list`, production `tools/call`, Vite middleware changes, OAuth callback, authorization-code exchange, refresh-token handling, Stytch API calls, remote JWKS fetch, token introspection, token persistence, provider secrets, Convex query/mutation, real MCP handlers, user data access, outbound HTTP, model calls, package/lockfile changes, PR88, or PR89.

The next MCP slice must remain a separate explicit request and separate reviewed PR before any runtime wiring.

## Rollback

Revert PR257 to remove the server-only Stytch bearer verifier boundary and its focused tests. No data migration, token cleanup, provider cleanup, package rollback, production endpoint rollback, or Vite rollback is required because PR87.15A added no runtime wiring.

## Touched pages

- [[product/chatgpt-app-sdk-roadmap]]
- [[hot]]
- [[index]]
