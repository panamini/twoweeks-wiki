---
title: "MCP Dev Fixture Demo Checkpoint - PR87.12"
category: source
tags: [chatgpt-app, apps-sdk, mcp, checkpoint, fixture-demo, pr87-12]
created: 2026-06-24
updated: 2026-06-24
status: current
type: analysis
related: [[product/chatgpt-app-sdk-roadmap]], [[product/manual-application-handoff]], [[sources/2026-06-24-pr87-10-mcp-dev-endpoint-blocked-reachability-checkpoint]], [[sources/2026-06-24-pr87-11-mcp-auth-account-linking-architecture-checkpoint]], [[sources/2026-06-23-release-orchestration-staging-pr87-8-checkpoint]]
---

# MCP Dev Fixture Demo Checkpoint - PR87.12

## Summary

PR253, [PR87.12: add local/dev MCP fixture demo](https://github.com/panamini/neyssan/pull/253), merged the fixture-only local/dev MCP demo on top of the guarded `/mcp` development endpoint. It makes `initialize`, `notifications/initialized`, `tools/list`, and strictly synthetic fixture `tools/call` paths exercisable for ChatGPT Developer Mode / MCP protocol testing without enabling production MCP, OAuth, real handlers, real data, outbound HTTP, or model calls.

## Key points

- PR253 merged into `application-os-foundation` as merge commit `ccd0e5d9b5a62722ec163e6b282e2e43619b33fe` on 2026-06-24 05:35:59 +0200, verified from GitHub merge result and local fetch.
- The head SHA before merge was `97bbe4b40c8028f331fabdb508b5bd67a070aa60`.
- The changed files stayed exactly:
  - `my-app/src/modules/local-mcp/localMcpDevEndpoint.ts`
  - `my-app/src/modules/local-mcp/__tests__/localMcpDevEndpoint.test.ts`
  - `my-app/vite.config.ts`
- The endpoint remains disabled by default and local/dev only.
- `LOCAL_MCP_DEV_ENDPOINT=1` enables reachability; `LOCAL_MCP_DEV_FIXTURE_DEMO=1` enables fixture `tools/call` only when the endpoint flag is also enabled.
- Fixture `tools/call` returns deterministic synthetic dry-run structured content aligned with the advertised `tools/list` output schema.
- MCP-valid `_meta` params are accepted and ignored without echo; task-augmented `tools/call` is explicitly refused.
- Valid `notifications/initialized` requests without `id` return HTTP 202 with no body; notifications with `id` are rejected safely.
- Validation reported:
  - focused endpoint tests: 17 passed
  - full local-MCP suite: 56 files / 1201 tests passed
  - `tsc --noEmit --pretty false`: passed
  - targeted ESLint on the PR files: passed
  - GitHub checks: `test` success and both `js-tests` runs success
- MCP Inspector was not available locally (`MCP_INSPECTOR_NOT_AVAILABLE`), so protocol-level HTTP smoke was used.
- Live ChatGPT smoke was not run (`LIVE_CHATGPT_SMOKE_NOT_RUN`) because no approved HTTPS tunnel / Developer Mode execution boundary existed.
- CodeRabbit's blocking comments were addressed before merge; only a non-blocking blue/trivial test-helper comment remained.
- Production `/mcp`, production `tools/list`, production `tools/call`, real handlers, real data, OAuth runtime, Stytch runtime, Clerk account linking runtime, outbound/model calls, write actions, PR88, and PR89 remain blocked.

## Implications

PR87.12 is a local/dev fixture checkpoint, not a production launch checkpoint. It improves manual protocol testing for the existing guarded MCP dev boundary while preserving the production block on OAuth, real user data, real tool handlers, and launch-readiness work.

## Touched pages

- [[product/chatgpt-app-sdk-roadmap]]
- [[hot]]
- [[index]]
