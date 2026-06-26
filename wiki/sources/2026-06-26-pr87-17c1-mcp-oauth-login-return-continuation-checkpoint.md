---
title: "MCP OAuth Login Return Continuation Boundary Checkpoint - PR87.17C1"
category: source
type: checkpoint
created: 2026-06-26
updated: 2026-06-26
status: current
tags: [mcp, chatgpt-app, apps-sdk, auth, oauth, login-return, continuation, checkpoint]
---

# MCP OAuth Login Return Continuation Boundary Checkpoint - PR87.17C1

PR269, [PR87.17C1: add MCP OAuth login return continuation boundary](https://github.com/panamini/neyssan/pull/269), merged the server-only continuation boundary for local/dev MCP OAuth login-return flow into `application-os-foundation`.

PR87.17C1 composes PR87.17A authorization request validation, PR87.17B digest-only authorization-intent storage, and PR87.17C0 login-return convention. It adds route-independent prepare/resume logic only; it does not add a React page, route registration, provider handoff, token exchange, authorization-code issuance, account-link lifecycle invocation, production OAuth runtime, or real application-data access.

## Merge facts

- PR: <https://github.com/panamini/neyssan/pull/269>
- Title: `PR87.17C1: add MCP OAuth login return continuation boundary`
- Final merged head SHA: `133efa7af3c7fe5be4feac6d7f3887321d85683b`
- Merge commit SHA: `84d6b9bab8c4f2b046f6d298eda2b329b65d52dd`
- Merged at: `2026-06-26T15:58:19Z`
- Base after merge: `application-os-foundation` at `84d6b9bab8c4f2b046f6d298eda2b329b65d52dd`
- Changed files:
  - `my-app/src/modules/local-mcp/mcpOAuthLoginReturnContinuationBoundary.ts`
  - `my-app/src/modules/local-mcp/__tests__/mcpOAuthLoginReturnContinuationBoundary.test.ts`
- CodeRabbit status: `SUCCESS`; latest review comment was non-blocking after merge.
- Semgrep cloud scan: `SUCCESS`.
- Remaining red checks at merge: `CI / js-tests` and `Playwright Tests / test` failed in the remote rollup.

## Runtime behavior recorded

PR87.17C1 adds server-only `prepareMcpOAuthLoginReturnContinuation` and `resumeMcpOAuthAuthorizationAfterLoginReturn` behavior behind the `mcpOAuthLoginReturnContinuationBoundary` module.

The boundary uses CSPRNG raw continuation handles, SHA-256 digest storage semantics, PR267-style create/consume ports, PR268 constants `mcp_oauth_return`, `/mcp/oauth/authorize/continue`, and `mcp_oauth_intent`, and PR265/PR87.17A normalized request and handoff-owner types.

The raw continuation handle remains outside storage. Continuation resume is one-time, owner-bound, expiry-aware, replay-safe, and fail-closed for sensitive hint decisions.

## Non-permissions

PR87.17C1 does not add a route, React page, router registration, Clerk or Stytch call, Convex runtime/schema import, Vite change, network behavior, browser storage, token/code/account-link behavior, production OAuth runtime, PR88, PR89, cover-letter work, or real user-data access.

## Rollback

Revert PR269 to remove the continuation boundary and focused tests.

After rollback:

- PR87.17C0 login-return convention remains.
- PR87.17B authorization-intent storage remains.
- PR87.17A authorization-request boundary remains.
- PR87.16 account-link lifecycle remains.
- No provider/dashboard rollback is required.
- No token revocation is required.
- No production rollback is required.

## Next slice

The next step is `PR87.17C2 - Wire MCP OAuth login-return continuation into local/dev authorization flow` as a separate reviewed slice.

PR87.17C2 must wire the existing local/dev route/page layer to the PR87.17C1 boundary without adding Stytch calls, token exchange, authorization-code issuance, account-link lifecycle invocation, production OAuth runtime, PR88, PR89, or cover-letter changes.

## Touched pages

- [[product/chatgpt-app-sdk-roadmap]]
- [[hot]]
- [[index]]
