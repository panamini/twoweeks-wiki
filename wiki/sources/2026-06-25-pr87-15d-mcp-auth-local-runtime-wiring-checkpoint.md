---
title: "MCP Local Dev Auth Runtime Wiring Checkpoint - PR87.15D"
category: source
type: checkpoint
created: 2026-06-25
status: current
tags: [mcp, chatgpt-app, apps-sdk, auth, local-dev, checkpoint]
---

# MCP Local Dev Auth Runtime Wiring Checkpoint - PR87.15D

PR263, [PR87.15D: wire composed auth into local/dev MCP runtime](https://github.com/panamini/neyssan/pull/263), merged the PR87.15C composed auth dependencies into the local/dev Vite MCP middleware on `application-os-foundation`.

PR87.15D wires the previously merged non-production auth composition into the local/dev runtime only. It reuses the PR257 Stytch RS256 bearer verifier, PR259 canonical account-link lookup adapter, PR254 auth policy/resolver, PR255 request orchestrator dependency ports, and PR261 composition builder. The runtime remains explicit-flag gated and local/dev scoped.

## Merge facts

- PR: <https://github.com/panamini/neyssan/pull/263>
- Final merged head SHA: `6faf7cd8f66134eb81a6d34bec8f21510a210773`
- Merge commit SHA: `97b8faa9c326868a298ed73d4357d03bdaf7ec47`
- Merged at: `2026-06-25T06:56:04Z`
- Base after merge: `origin/application-os-foundation` at `97b8faa9c326868a298ed73d4357d03bdaf7ec47`
- Merge method: admin squash merge.

## Changed app files

- `docs/plans/2026-06-25-pr87-15d-mcp-auth-local-runtime-wiring-brief.md`
- `my-app/src/modules/local-mcp/__tests__/localMcpDevAuthRuntimeComposition.test.ts`
- `my-app/src/modules/local-mcp/__tests__/localMcpDevEndpoint.vite-auth-composition.test.ts`
- `my-app/src/modules/local-mcp/localMcpDevAuthRuntimeComposition.ts`
- `my-app/tsconfig.node.json`
- `my-app/vite.config.ts`

## Runtime behavior recorded

PR87.15D adds the local/dev runtime composition path behind explicit flags:

- `LOCAL_MCP_DEV_ENDPOINT=1`
- `LOCAL_MCP_DEV_FIXTURE_DEMO=1`
- `LOCAL_MCP_DEV_AUTH_POLICY=1`
- `LOCAL_MCP_DEV_STYTCH_COMPOSITION=1`
- `LOCAL_MCP_DEV_STYTCH_JWKS_JSON=<public synthetic JWKS JSON>`

When enabled with valid synthetic public JWKS, the Vite local/dev MCP middleware builds and injects the composed token verifier and account-link lookup dependencies once. When disabled or malformed, the runtime preserves fail-closed behavior and does not silently authorize.

The runtime no-link policy remains fail-closed. With no canonical account link, a valid verified token reaches account-link-required behavior instead of invoking fixture handlers. Tests also proved valid signed-token composition, duplicate-account-link fail-closed behavior, metadata/security-scheme consistency, and no token/JWKS/private-key echo.

## Validation and review disposition

Local stabilization before merge reported:

- Focused PR87.15D tests passed: 2 files / 35 tests.
- Adjacent auth tests passed: 6 files / 238 tests.
- Full local-MCP suite passed: 63 files / 1457 tests.
- Relevant Convex guardrail tests passed: 3 files / 53 tests.
- TypeScript passed.
- Targeted ESLint passed.
- `npm run build` passed with existing Vite warnings only.
- `git diff --check origin/application-os-foundation...HEAD` passed.
- Forbidden-surface grep passed.
- Fallow audit was advisory only: no P0/P1 finding was surfaced; moderate complexity/inherited dead-code findings remained.
- CodeRabbit status was `SUCCESS` and no inline CodeRabbit review comments were present.
- Semgrep status was `SUCCESS`.

GitHub CI and Playwright remained red at merge time, but the failed job logs were unavailable from the GitHub API/CLI boundary. The rerun failed again with:

- `CI / js-tests` failure x2.
- `Playwright Tests / test` failure.
- `gh run view --log-failed` returned `log not found`.
- Actions job API returned empty `steps` arrays for the failed jobs.

The merge was an admin squash merge after the local validation and review-bot checks above.

## Non-permissions

PR87.15D does not add production MCP, public `/mcp`, production `tools/list`, production `tools/call`, OAuth authorization endpoint, OAuth callback, authorization-code exchange, PKCE runtime, real Stytch API calls, remote JWKS fetch, token persistence, account-link creation or mutation, public Convex query/mutation, HTTP action, real handlers, real application data, outbound HTTP, model calls, write/export/send/apply behavior, provider dashboard changes, production flags, billing, PR88, or PR89.

It also does not change cover-letter behavior, package manifests, lockfiles, or Convex schema.

## Rollback

Revert PR263 to remove local/dev runtime composition wiring and tests.

After rollback:

- PR261 auth composition boundary remains.
- PR259 account-link lookup adapter remains.
- PR258 canonical account-link storage contract remains.
- PR257 Stytch verifier remains.
- PR254/PR255 auth policy and request orchestrator remain.
- No data migration, provider cleanup, token cleanup, production endpoint rollback, package rollback, lockfile rollback, or account-link rollback is required because PR87.15D added local/dev runtime wiring only and no persistence path.

## Next slice

The next step is `Gate87.16A - MCP Inspector local authentication smoke`.

Gate87.16A should test the merged PR87.15D runtime through MCP Inspector over loopback only. It must not create a branch, PR, commit, wiki mutation, production exposure, HTTPS tunnel, ChatGPT Developer Mode connection, real Stytch call, live Convex call, or real user data access.

Only after Gate87.16A returns green should PR87.16 account-link lifecycle work be considered.

## Touched pages

- [[product/chatgpt-app-sdk-roadmap]]
- [[hot]]
- [[index]]
