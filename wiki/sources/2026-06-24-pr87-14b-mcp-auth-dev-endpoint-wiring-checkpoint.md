---
title: "MCP Local Dev Auth Discovery And Challenge Wiring Checkpoint - PR87.14B"
category: source
tags: [chatgpt-app, apps-sdk, mcp, auth, local-dev, checkpoint, pr87-14b]
created: 2026-06-24
updated: 2026-06-24
status: current
type: analysis
related: [[product/chatgpt-app-sdk-roadmap]], [[product/manual-application-handoff]], [[sources/2026-06-24-pr87-14a-mcp-auth-request-orchestrator-checkpoint]], [[sources/2026-06-24-pr87-13-mcp-auth-policy-boundary-checkpoint]], [[sources/2026-06-24-pr87-12-mcp-dev-fixture-demo-checkpoint]]
---

# MCP Local Dev Auth Discovery And Challenge Wiring Checkpoint - PR87.14B

## Summary

PR256, [PR87.14B: wire local/dev MCP auth discovery and challenge handling](https://github.com/panamini/neyssan/pull/256), merged the PR87.13 auth metadata/policy boundary and PR87.14A auth request orchestrator into the local/dev MCP fixture endpoint only. It adds protected-resource metadata routes, auth-mode `tools/list` security schemes, auth-gated fixture `tools/call`, missing-account-link challenges, Vite dev middleware wiring, and a narrow `tsconfig.node.json` closure for the Vite-facing imports.

## Key points

- PR256 merged into `application-os-foundation` as merge commit `4a98a97387b6675eb7d27f632434f390462f2d40` on 2026-06-24.
- The reviewed head SHA before merge was `7dbce814ccc851ac7d588dd98143b5b5b25925e5`.
- The changed files stayed exactly:
  - `my-app/src/modules/local-mcp/__tests__/localMcpDevEndpoint.test.ts`
  - `my-app/src/modules/local-mcp/localMcpDevAuthConfig.ts`
  - `my-app/src/modules/local-mcp/localMcpDevEndpoint.ts`
  - `my-app/tsconfig.node.json`
  - `my-app/vite.config.ts`
- The endpoint remains local/dev only and requires all explicit opt-ins for auth behavior:
  - `LOCAL_MCP_DEV_ENDPOINT=1`
  - `LOCAL_MCP_DEV_FIXTURE_DEMO=1`
  - `LOCAL_MCP_DEV_AUTH_POLICY=1`
- Auth config now fails closed when the parsed/deduped client allow-list is missing or empty.
- Protected-resource metadata is served only for loopback GET requests in valid auth mode.
- Auth-mode `tools/list` includes top-level and `_meta.securitySchemes` for the exact `twoweeks:applications:read` scope.
- Auth-mode `tools/call` returns MCP tool-result errors with `_meta["mcp/www_authenticate"]` for missing/malformed credentials and missing account links, without echoing raw bearer tokens or identity/account-link details.
- Runtime defaults remain deny-all unless tests inject fake verifier/account-link ports.
- Validation reported:
  - focused endpoint suite: 22 tests passed
  - full local-MCP suite: 58 files / 1339 tests passed
  - `rtk npx tsc --noEmit --pretty false`: passed
  - targeted ESLint: passed
  - Vite HTTP smoke: passed for metadata discovery, auth-mode `tools/list`, unauthenticated challenge, and reachability-only `tools/call` blocked
  - injected fake verifier/account-link smoke: passed for authorized fixture call and missing-account-link challenge
  - forbidden-surface grep: clean
  - GitHub checks were green: CodeRabbit, `js-tests`, and `test`
- `npm run build` still fails only on inherited Convex `_generated` baseline errors; filtered output had no PR256 changed-file hits and no prior TS6307, sync-return, or readonly-header errors.
- Non-permissions remain unchanged: no production `/mcp`, no production `tools/list` or `tools/call`, no real Stytch bearer verification, no OAuth callback or token exchange, no Clerk/Convex/Stytch runtime lookup, no account persistence, no real data, no outbound HTTP, no model calls, no write/export/send/apply, no cover-letter work, no PR88, and no PR89.

## Implications

PR87.14B proves the local/dev endpoint can advertise and deliver ChatGPT OAuth challenge metadata without opening production MCP or real auth/runtime behavior. The next MCP slice must remain separate and should not start until this checkpoint is treated as the current local/dev auth wiring baseline.

## Rollback

Revert PR256 to remove the local/dev endpoint auth discovery and challenge wiring. Earlier PR87.13 policy/metadata and PR87.14A orchestrator boundaries remain in place; no data migration, provider cleanup, token cleanup, production rollback, or package/lockfile rollback is required.

## Touched pages

- [[product/chatgpt-app-sdk-roadmap]]
- [[hot]]
- [[index]]
