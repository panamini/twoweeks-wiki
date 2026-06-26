---
title: "MCP OAuth Local Dev Route Adapter Checkpoint - PR87.17D"
category: source
type: checkpoint
created: 2026-06-27
updated: 2026-06-27
status: current
tags: [mcp, chatgpt-app, apps-sdk, auth, oauth, local-dev, route-adapter, checkpoint]
---

# MCP OAuth Local Dev Route Adapter Checkpoint - PR87.17D

PR273, [PR87.17D: wire local MCP OAuth route adapter](https://github.com/panamini/neyssan/pull/273), merged the local/dev-only MCP OAuth route adapter into `application-os-foundation`.

PR87.17D is merged.

PR87.17D wires the local/dev OAuth route flow behind `LOCAL_MCP_DEV_OAUTH_AUTHORIZATION=1`. The route flow is:

```text
ChatGPT OAuth request
-> PR265 validation
-> PR271 pre-auth storage
-> PR268 Clerk login return
-> PR272 owner binding
-> PR267 owner-bound intent
-> PR269 continuation
```

This remains a local/dev adapter checkpoint. It does not open production MCP/OAuth, add Stytch runtime integration, issue OAuth codes, exchange tokens, create production account links, unlock PR88/private beta, or unlock PR89/public launch.

## Merge facts

- PR: <https://github.com/panamini/neyssan/pull/273>
- Title: `PR87.17D: wire local MCP OAuth route adapter`
- Branch: `codex/pr87-17d-mcp-oauth-local-dev-route-adapter`
- Final merged head SHA: `9b23d85682a5b69d4b76904f7cd5931280fd3218`
- Merge commit SHA: `ece26dbf2a899b69d42343e1d1165dbc05d12d53`
- Merged at: `2026-06-26T21:43:32Z`
- Base branch: `application-os-foundation`
- Changed app files:
  - `my-app/src/modules/local-mcp/mcpOAuthLocalDevRouteAdapter.ts`
  - `my-app/src/modules/local-mcp/__tests__/mcpOAuthLocalDevRouteAdapter.test.ts`
  - `my-app/vite.config.ts`
- CodeRabbit status: `SUCCESS`.
- Semgrep cloud scan: `SUCCESS`.
- GitHub Actions `js-tests` and Playwright `test` failed before runner startup with `runner_id: 0` and no steps, matching external runner/billing/spending-limit availability rather than an app regression.

## Implementation summary

PR87.17D adds the local/dev OAuth route adapter and wires it behind `LOCAL_MCP_DEV_OAUTH_AUTHORIZATION=1`.

The adapter composes the existing reviewed OAuth pieces without accepting an owner from the request. It validates the ChatGPT OAuth request, stores pre-auth state server-side, returns through the Clerk login-return convention, binds the owner server-side, creates the owner-bound intent, and resumes through the continuation boundary.

The implementation keeps sensitive OAuth request material out of browser storage and does not persist sensitive data in browser state.

## Validation evidence

- Focused OAuth suite for PR265/267/268/269/271/272: 222 passing.
- Full MCP suite: 1,793 passing.
- TypeScript check: clean.
- Changed-file ESLint with `--no-ignore`: clean.
- `git diff --check`: clean.
- Broad/full-repo lint remains inherited repo-wide debt and is out of scope for this checkpoint.
- GitHub Actions runner/billing/spending-limit failures are external when jobs have `runner_id: 0` or no steps.

## Non-permissions

PR87.17D does not expose production MCP/OAuth endpoints, add Stytch runtime integration, issue OAuth authorization codes, exchange tokens, create production account links, persist sensitive OAuth request data in browser storage, accept owner from the request, unlock PR88/private beta, unlock PR89/public launch, or change cover-letter behavior.

Production MCP/OAuth/token/account-link runtime remains blocked pending a separate reviewed gate.

## Rollback

Revert PR273 to remove the local/dev route adapter, focused adapter tests, and Vite local/dev wiring.

After rollback:

- PR265 authorization request validation remains.
- PR267 authorization-intent storage remains.
- PR268 login-return convention remains.
- PR269 continuation boundary remains.
- PR271 pre-auth storage remains.
- PR272 owner binding remains.
- No production endpoint, token, Stytch, or account-link rollback is required.

## Next state

Do not rerun PR87.17D.

Do not start PR88 or PR89 from this checkpoint.

The next implementation PR must be chosen only after reloading the roadmap and verifying the current lowest-numbered unmerged blocker.

Production MCP/OAuth/token/account-link runtime remains blocked pending a separate reviewed gate.

## Touched pages

- [[product/chatgpt-app-sdk-roadmap]]
- [[hot]]
- [[index]]
