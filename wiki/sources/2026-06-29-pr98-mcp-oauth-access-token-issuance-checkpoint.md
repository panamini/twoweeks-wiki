---
title: "MCP OAuth Access Token Issuance Checkpoint - PR98"
category: source
type: checkpoint
created: 2026-06-29
updated: 2026-06-29
status: current
tags: [mcp, chatgpt-app, apps-sdk, auth, oauth, access-token, production-gate, checkpoint]
---

# MCP OAuth Access Token Issuance Checkpoint - PR98

PR284 merged the production OAuth access-token issuance boundary after the PR97 authorization-code redemption boundary.

This checkpoint updates the PR96/PR96.1 production OAuth state. It does not unlock production `/mcp` execution, `tools/list`, `tools/call`, provider calls, refresh tokens, production account-link lifecycle, consent UI, private beta, or public launch.

## Merge facts

- PR284: <https://github.com/panamini/neyssan/pull/284>
  - Title: `PR98: add production OAuth access-token issuance boundary`
  - Final head SHA: `02b2ef2df6bca8e6577db183aa498ee09986c44a`
  - Merge commit SHA: `e1a22cb5c1a660b9fd9a8f02b76226761128ea33`
  - Merged at: `2026-06-29T21:34:08Z`
  - Base branch: `application-os-foundation`
  - Base after merge: `7f850c79257f6b7f1cbcfd75b8e1d5772a89b416`

## Implementation summary

PR98 changes production `/oauth/token` from validation-only to guarded access-token issuance for valid authorization-code token requests.

The implementation:

- issues a random bearer access token only at the route edge
- persists only the access-token digest in Convex
- atomically inserts the access-token digest record and consumes the authorization code
- adds `mcpOAuthAccessTokens` storage with status, owner, client, redirect URI, resource, scopes, timestamps, and expiry indexes
- adds expired access-token cleanup
- validates client, redirect URI, resource, authorization-code digest, one-time code status, expiry, and PKCE challenge through the issuance mutation
- filters OpenID Connect identity scopes from the OAuth access-token response because no ID token is minted
- rejects malformed success proofs that do not match expiry, client, redirect URI, resource, PKCE challenge, storage flags, or canonical application scopes
- uses storage-side time for code expiry and bounded route/storage clock skew for issuance deadlines

## Validation evidence

- Focused production route adapter test passed with 94 tests on the final review-fix head.
- Focused Convex authorization-code/access-token storage test passed with 15 tests on the final review-fix head.
- `cd my-app && rtk npx tsc -p tsconfig.node.json --pretty false` passed.
- `rtk git diff --check` passed.
- Read-only Fallow audit ran; it reported broad existing dependency, duplication, and complexity findings, but no new dead-code blocker from the review-fix patch.
- Semgrep passed.
- CodeRabbit completed on the final head.
- Qodo updated its review to the final head.
- Codex review trigger was blocked by account usage limits.
- GitHub `js-tests` and Playwright `test` jobs failed before executing any steps; the failed jobs had `runner_id: 0` and empty `steps`, matching the external runner startup failure pattern already seen on PR281 and PR282.

## Non-permissions

PR98 does not add production `/mcp` bearer-token verification, MCP request execution, `tools/list`, `tools/call`, provider token exchange, refresh tokens, production account-link lifecycle, consent UI, private beta, public launch behavior, billing/entitlements, live submit/apply, or provider-verified submission.

## Next state

Do not rerun PR89, PR90, PR92, PR93, PR94, PR95, PR96, PR96.1, PR97, or PR98.

The next narrow app PR should be PR99: production MCP bearer-token verification boundary. It should validate `Authorization: Bearer <access_token>` against the digest-backed access-token storage for `/mcp` requests, fail closed on missing, malformed, expired, revoked, wrong-resource, wrong-scope, or storage-unavailable tokens, and keep MCP execution, `tools/list`, `tools/call`, provider calls, refresh tokens, account-link lifecycle, private beta, and public launch blocked.

## Touched pages

- [[product/chatgpt-app-sdk-roadmap]]
- [[hot]]
- [[index]]
