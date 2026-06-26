---
title: "MCP OAuth Login Return Convention Checkpoint - PR87.17C0"
category: source
type: checkpoint
created: 2026-06-26
status: current
tags: [mcp, chatgpt-app, apps-sdk, auth, oauth, login-return, checkpoint]
---

# MCP OAuth Login Return Convention Checkpoint - PR87.17C0

PR268, [PR87.17C0: define MCP OAuth login return convention](https://github.com/panamini/neyssan/pull/268), merged the repository-owned sign-in return convention for MCP OAuth login continuation on `application-os-foundation`.

PR87.17C0 defines the `mcp_oauth_return` convention, preserves the default `/cv` sign-in fallback, allows only the fixed local/dev MCP OAuth continuation path, and requires the opaque `mcp_oauth_intent` continuation parameter. It adds resolver and SignInPage wiring tests only; it does not add OAuth behavior or provider integration.

## Merge facts

- PR: <https://github.com/panamini/neyssan/pull/268>
- Title: `PR87.17C0: define MCP OAuth login return convention`
- Final merged head SHA: `3892163e7850e2596d7f335cae4325ceb0dd3c34`
- Merge commit SHA: `cdf3b9e95e1abad77beb7d96f9de0fcfb830f369`
- Merged at: `2026-06-26T03:06:46Z`
- Base after merge: `application-os-foundation` at `cdf3b9e95e1abad77beb7d96f9de0fcfb830f369`
- CodeRabbit: `SUCCESS`
- Semgrep: `SUCCESS`
- Qodo: issue resolved.
- Remaining red checks at merge: inherited or broader `js-tests` and Playwright lanes.

## Runtime behavior recorded

PR87.17C0 defines repository-owned `mcp_oauth_return`, preserves `/cv` as the default sign-in fallback, allows only the fixed local/dev MCP OAuth continuation path, requires `mcp_oauth_intent`, rejects unsafe or arbitrary return URLs, and adds focused resolver plus SignInPage wiring tests.

The fixed continuation route/page remains a placeholder surface only. This checkpoint records no OAuth authorization endpoint behavior, no provider validation, no consent UI, no token exchange, and no production enablement.

## Non-permissions

PR87.17C0 does not add OAuth authorization endpoint behavior, Convex changes, Stytch provider integration, MCP endpoint/runtime composition, Vite changes, package or lockfile changes, PR88, PR89, cover-letter changes, production flags, deployment behavior, or real user data access.

## Rollback

Revert PR268 to remove the sign-in return convention and focused tests.

After rollback:

- PR87.17B authorization-intent storage remains.
- PR87.17A authorization-request boundary remains.
- No OAuth provider integration rollback is required.
- No Convex, Vite, schema, token, account-link, deployment, or production rollback is required.

## Next slice

The next step is `PR87.17C1 — MCP OAuth login return continuation boundary` as a separate reviewed slice.

PR87.17C1 must compose PR87.17A, PR87.17B, and this PR87.17C0 sign-in return convention without adding routes, React pages, provider integration, production MCP behavior, PR88, PR89, or cover-letter changes.

## Touched pages

- [[product/chatgpt-app-sdk-roadmap]]
- [[hot]]
- [[index]]
