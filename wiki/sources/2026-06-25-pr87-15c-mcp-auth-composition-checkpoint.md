---
title: "MCP Auth Composition Checkpoint - PR87.15C"
category: source
tags: [chatgpt-app, apps-sdk, mcp, auth, stytch, account-link, checkpoint, pr87-15c]
created: 2026-06-25
updated: 2026-06-25
status: current
type: analysis
related: [[product/chatgpt-app-sdk-roadmap]], [[sources/2026-06-25-pr87-15b1-mcp-account-link-lookup-adapter-checkpoint]], [[sources/2026-06-25-pr87-15b0-mcp-account-link-canonical-storage-checkpoint]], [[sources/2026-06-25-pr87-15a-mcp-stytch-bearer-verifier-checkpoint]], [[sources/2026-06-24-pr87-14b-mcp-auth-dev-endpoint-wiring-checkpoint]]
---

# MCP Auth Composition Checkpoint - PR87.15C

## Summary

PR261, [PR87.15C: compose Stytch verification and account-link lookup for local/dev MCP auth](https://github.com/panamini/neyssan/pull/261), merged the deterministic non-production composition boundary into `application-os-foundation`. It composes the PR257 Stytch RS256 bearer verifier, PR259 bounded account-link lookup adapter, PR254 auth policy/resolver, and PR255 request orchestrator dependency ports without adding runtime endpoint wiring or production behavior.

## Key points

- PR261 merged into `application-os-foundation` as merge commit `f161ae9302269e5944101dd65ec4e375c112c070` on 2026-06-25 UTC.
- The final merged head SHA was `ccc4fe7469d17e62e8ec400288e45c4243679d94`.
- The changed files stayed exactly:
  - `my-app/src/modules/local-mcp/mcpAuthCompositionBoundary.ts`
  - `my-app/src/modules/local-mcp/__tests__/mcpAuthCompositionBoundary.test.ts`
- The composition builder exports endpoint dependency output that can be wired by a later local/dev runtime slice.
- The boundary fails closed when Stytch verifier configuration, account-link lookup configuration, canonical auth policy configuration, or JWKS material is malformed.
- The CodeRabbit P2 fix rejects malformed, empty, private, non-RSA, duplicate-`kid`, or otherwise unacceptable JWKS before reporting `configured: true`.
- Synthetic signed-token composition tests prove the valid path through verifier, claims policy, lookup adapter, and resolver without a runtime endpoint.

## Validation

- GitHub PR metadata verified PR261 is merged into `application-os-foundation` with merge commit `f161ae9302269e5944101dd65ec4e375c112c070` and final head `ccc4fe7469d17e62e8ec400288e45c4243679d94`.
- Local fetch and ancestry verification confirmed the merge commit is contained in `origin/application-os-foundation`.
- Local PR metadata showed the final changed-file set was limited to the two composition boundary files.
- Local validation before merge passed focused composition tests, Stytch verifier tests, request orchestrator tests, the full local-MCP suite, TypeScript, targeted ESLint, build, diff checks, and forbidden-surface checks.
- CodeRabbit reported success after the malformed-JWKS regression fix.
- GitHub CI and Playwright checks were red at merge time, but GitHub did not expose logs for those failures; the merge was an admin squash merge.

## Implications

PR87.15C remains a non-production composition boundary. It does not add endpoint wiring, Vite middleware wiring, production `/mcp`, production `tools/list`, production `tools/call`, OAuth callback, authorization-code exchange, refresh-token flow, PKCE runtime, Stytch API calls, remote JWKS fetch, token introspection, token persistence, account-link creation or mutation, public Convex query/mutation, HTTP action, real handlers, real application data, outbound HTTP, model calls, write/export/send/apply behavior, provider dashboard changes, production flags, billing, PR88, or PR89.

The next approved slice is PR87.15D: wire the composed auth dependencies into the actual local/dev Vite MCP runtime, preserving default, anonymous, and deny-all modes. It must not mutate this checkpoint after implementation begins.

## Rollback

Revert PR261 to remove the composition boundary and tests. No data migration, provider cleanup, token cleanup, production endpoint rollback, Vite rollback, package rollback, lockfile rollback, or account-link rollback is required because PR87.15C added no runtime wiring and no persistence path.

## Touched pages

- [[product/chatgpt-app-sdk-roadmap]]
- [[hot]]
- [[index]]
