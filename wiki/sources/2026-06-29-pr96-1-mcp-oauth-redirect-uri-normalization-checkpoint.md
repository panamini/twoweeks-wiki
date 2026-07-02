---
title: "MCP OAuth Redirect URI Normalization Checkpoint - PR96.1"
category: source
type: checkpoint
created: 2026-06-29
updated: 2026-06-29
status: current
tags: [mcp, chatgpt-app, apps-sdk, auth, oauth, production-gate, redirect-uri, checkpoint]
---

# MCP OAuth Redirect URI Normalization Checkpoint - PR96.1

PR282 fixed the post-merge PR96 review finding around production OAuth redirect URI allowlist canonicalization.

This checkpoint amends the PR96 authorization-code state. It does not unlock token exchange, access tokens, refresh tokens, production account links, provider calls, consent UI, production `/mcp`, `tools/list`, or `tools/call`.

## Merge facts

- PR282: <https://github.com/panamini/neyssan/pull/282>
  - Title: `PR96.1: normalize production OAuth redirect URI allowlist`
  - Final head SHA: `0c65f11d2ccdc975336181cf9c4d003fc5eb905f`
  - Merge commit SHA: `08651f259c1ffa57396cb36d41163aed90dfb8a9`
  - Merged at: `2026-06-29T15:33:18Z`
  - Base branch: `application-os-foundation`

## Implementation summary

PR96.1 canonicalizes `MCP_OAUTH_PRODUCTION_REDIRECT_URIS` entries before the production login-return handoff exact-match comparison.

The fix:

- normalizes safe HTTPS redirect URI env entries through URL parsing
- deduplicates entries after canonicalization
- rejects raw C0 / DEL control characters before `new URL()` can normalize them away
- rejects malformed percent escapes before parsing
- preserves invalid raw entries so the existing downstream boundary parser still fails closed
- adds regression coverage for default-port canonicalization, duplicate canonical entries, wildcard invalid preservation, control-character preservation, and malformed-percent preservation

## Validation evidence

- Focused production route adapter test passed with 61 tests.
- `tsc -p tsconfig.node.json --pretty false` passed.
- `git diff --check` passed.
- Read-only Fallow audit passed with no introduced dead-code, complexity, or duplication findings.
- Semgrep passed.
- CodeRabbit passed.
- GitHub `js-tests` and Playwright `test` jobs failed before executing any steps; the jobs had zero steps and matched the external runner availability failure pattern already seen on PR281.

## Non-permissions

PR96.1 does not add `/oauth/token`, provider calls, token exchange, access tokens, refresh tokens, token persistence, production account links, consent UI, production `/mcp`, `tools/list`, `tools/call`, PR88/private beta, public launch behavior, or broader runtime gates.

## Next state

Do not rerun PR89, PR90, PR92, PR93, PR94, PR95, PR96, or PR96.1.

The next narrow app PR should still be PR97: production OAuth token endpoint / authorization-code redemption boundary. It should verify client, redirect URI, authorization-code digest, expiry, one-time status, and PKCE verifier server-side while still not issuing access tokens, refresh tokens, provider calls, production account links, production `/mcp`, `tools/list`, or `tools/call`.

## Touched pages

- [[product/chatgpt-app-sdk-roadmap]]
- [[hot]]
- [[index]]
