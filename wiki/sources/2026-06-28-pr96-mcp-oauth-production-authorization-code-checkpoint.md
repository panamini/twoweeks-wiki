---
title: "MCP OAuth Production Authorization Code Checkpoint - PR96"
category: source
type: checkpoint
created: 2026-06-28
updated: 2026-06-28
status: current
tags: [mcp, chatgpt-app, apps-sdk, auth, oauth, production-gate, authorization-code, checkpoint]
---

# MCP OAuth Production Authorization Code Checkpoint - PR96

PR281 connected production login-return continuation to short-lived OAuth authorization-code issuance after PR280 owner binding.

This checkpoint supersedes the PR94-only production `/oauth/authorize` state. It does not unlock token exchange, access tokens, refresh tokens, production account links, provider calls, consent UI, production `/mcp`, `tools/list`, or `tools/call`.

## Merge facts

- PR280: <https://github.com/panamini/neyssan/pull/280>
  - Title: `PR95: bind production OAuth login return continuation`
  - Final head SHA: `a26a50a0afa718101fcfa62014873e59f5ea5522`
  - Merge commit SHA: `afde4f88d9b8bff6a4afbc2bb8d3aef3d6622f95`
  - Merged at: `2026-06-28T03:27:36Z`
  - Base branch: `application-os-foundation`
- PR281: <https://github.com/panamini/neyssan/pull/281>
  - Title: `PR96: issue production OAuth authorization codes`
  - Final head SHA: `1fba009b0f67c68614a2a72daf4e6f832f9be0a9`
  - Merge commit SHA: `6beeee919a1cded82a3598f785eb507c58b76436`
  - Merged at: `2026-06-28T04:43:17Z`
  - Base branch: `application-os-foundation`

## Implementation summary

PR95 moved the production login-return continuation from ownerless pre-auth state to owner-bound server state after authenticated Clerk return.

PR96 then completed the next narrow OAuth step:

- consumes the owner-bound authorization intent server-side
- validates that the handoff still matches the production authorization config
- generates a short-lived raw OAuth authorization code
- stores only the SHA-256 authorization-code digest in Convex
- binds stored code state to owner identity, client ID, redirect URI, resource, scopes, original state, PKCE challenge, production environment, and version
- redirects the browser to the validated OAuth client `redirect_uri` with `code` and original `state`

The raw authorization code exists only in the browser redirect. Server storage keeps digest-backed state only.

## Storage and replay boundary

PR96 adds `mcpOAuthAuthorizationCodes` with:

- digest lookup by `authorizationCodeDigest`
- expiry lookup by `expiresAt`
- pending / consumed / expired status
- one-time consume semantics
- client and redirect URI binding
- 5 minute TTL
- server-only failure payloads that do not echo raw codes, digests, owner identifiers, or sensitive request values

Replay, expiry, duplicate digest rows, malformed storage, client mismatch, redirect mismatch, missing auth, missing continuation, invalid browser nonce cookie, unavailable Convex dependencies, and production preflight/config failures all fail closed.

## Validation evidence

- Focused production route adapter and authorization-code storage tests passed with 65 tests.
- Broader OAuth/local MCP subset passed with 280 tests.
- `npm run build` passed.
- `git diff --check` passed.
- Read-only Fallow audit reported only advisory unused-dependency, duplicate-test-helper, and complexity findings.
- CodeRabbit completed after the manual review trigger and reported no actionable finding.
- Qodo completed with non-blocking double-checks; redirect URI exact matching and digest duplicate fail-closed behavior were answered on the PR.
- Codex review trigger was attempted, but the connector reported code review usage limits.
- GitHub `semgrep-cloud-platform/scan` passed.
- GitHub `js-tests` and Playwright `test` jobs failed before starting with `runner_id: 0`, zero steps, and billing/spending-limit annotations; these were external CI availability failures, not code failures.

## Non-permissions

PR96 does not call Stytch or another OAuth provider, run consent UI, exchange authorization codes for tokens, issue access tokens, issue refresh tokens, persist provider tokens, create production account links, open production `/mcp`, expose `tools/list`, expose `tools/call`, open PR88/private beta/public launch behavior, or broaden runtime gates.

## Next state

Do not rerun PR89, PR90, PR92, PR93, PR94, PR95, or PR96.

Do not create PR88 retroactively.

The next narrow app PR should be PR97: production OAuth token endpoint / authorization-code redemption boundary. It should verify client, redirect URI, authorization-code digest, expiry, one-time status, and PKCE verifier server-side while still not issuing access tokens, refresh tokens, provider calls, production account links, production `/mcp`, `tools/list`, or `tools/call`.

## Touched pages

- [[product/chatgpt-app-sdk-roadmap]]
- [[hot]]
- [[index]]
