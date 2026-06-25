---
title: "MCP OAuth Authorization Request Boundary Checkpoint - PR87.17A"
category: source
type: checkpoint
created: 2026-06-26
status: current
tags: [mcp, chatgpt-app, apps-sdk, auth, oauth, checkpoint]
---

# MCP OAuth Authorization Request Boundary Checkpoint - PR87.17A

PR265, [PR87.17A: add MCP OAuth authorization request boundary](https://github.com/panamini/neyssan/pull/265), merged the server-only OAuth authorization-request boundary on `application-os-foundation`.

PR87.17A adds the validated MCP OAuth request normalization and safe intent-preservation layer that sits after PR87.16 account-link lifecycle work. It keeps the authorization request server-only, preserves the trusted provider-pending handoff, and rejects unsafe config or malformed OAuth boundary inputs without opening production MCP, consent UI, callback/code exchange, or token persistence.

## Merge facts

- PR: <https://github.com/panamini/neyssan/pull/265>
- Final merged head SHA: `3c7a48a8111019b08c1991ed540ff16a6a13d001`
- Merge commit SHA: `1f1cb7cb46a7bfa165bbfe37f728dd2aefe44091`
- Merged at: `2026-06-25T23:14:46Z`
- Base after merge: `application-os-foundation` at `1f1cb7cb46a7bfa165bbfe37f728dd2aefe44091`
- Merge method: merge commit.

## Changed app files

- `docs/plans/2026-06-25-pr87-17a-mcp-oauth-authorization-request-boundary-brief.md`
- `my-app/convex/__tests__/mcpAccountLinks.test.ts`
- `my-app/convex/mcpAccountLinks.ts`
- `my-app/src/modules/local-mcp/__tests__/mcpOAuthAuthorizationRequestBoundary.test.ts`
- `my-app/src/modules/local-mcp/mcpOAuthAuthorizationRequestBoundary.ts`

## Runtime behavior recorded

PR87.17A keeps the OAuth authorization request boundary server-only and provider-pending. It validates the request shape, preserves the split between server-only provider-forward data and browser-visible login-return data, accepts exact-client allowlists, rejects wildcard hosts in configured OAuth URLs, and keeps `id_token_hint` / `login_hint` out of browser-visible return URLs while preserving them server-side for future handling.

The resulting handoff remains `modelVisible: false`, `safeForLogging: false`, and does not add OAuth callback/code exchange, consent UI, token persistence, public account-link API, or production MCP behavior.

## Validation and review disposition

Local validation before merge reported:

- Focused OAuth boundary tests passed: 85 tests.
- Targeted ESLint passed.
- `git diff --check` passed.

Review and remote status at merge:

- CodeRabbit status was `SUCCESS`.
- Semgrep cloud scan was `SUCCESS`.
- Remote `CI / js-tests` failed twice.
- Remote `Playwright Tests / test` failed.
- `gh run view --log-failed` returned `log not found` for the failed jobs, and the Actions job API returned empty `steps` arrays.

## Non-permissions

PR87.17A does not add production `/mcp`, OAuth callback/code exchange, consent UI, token persistence, public account-link API, endpoint/Vite wiring, real Stytch/Clerk network calls, or real user data.

## Rollback

Revert PR265 to remove the OAuth authorization-request boundary mutations and tests.

After rollback:

- PR87.16 account-link lifecycle remains.
- PR87.15D runtime auth composition remains.
- No OAuth boundary checkpoint persists.
- No migration rollback is required.
- No production rollback is required.

## Next slice

The next step is `PR87.17B` as a separate reviewed slice.

PR87.17B must not be started from this checkpoint.

## Touched pages

- [[product/chatgpt-app-sdk-roadmap]]
- [[hot]]
- [[index]]
- [[log]]
