---
title: "MCP Dev Endpoint Test-Only Reachability Checkpoint - PR87.10"
category: source
tags: [chatgpt-app, apps-sdk, mcp, checkpoint, tests, pr87-10]
created: 2026-06-24
updated: 2026-06-24
status: current
type: analysis
related: [[product/chatgpt-app-sdk-roadmap]], [[product/manual-application-handoff]], [[sources/2026-06-23-release-orchestration-staging-pr87-8-checkpoint]], [[sources/2026-06-23-twoweeks-mcp-chatgpt-app-sdk-roadmap-checkpoint]]
---

# MCP Dev Endpoint Test-Only Reachability Checkpoint - PR87.10

## Summary

PR251, [PR87.10 MCP dev endpoint blocked reachability tests](https://github.com/panamini/neyssan/pull/251), merged a test-only checkpoint for the local/dev MCP endpoint boundary. It adds unit coverage for disabled/default behavior, local-only reachability, request guards, fixture-only initialize/tools/list responses, blocked tools/call behavior, and headers, without changing runtime code or production exposure.

## Key points

- PR251 merged into `application-os-foundation` as merge commit `1f121b008296fb47cc13519595e9e0ac0c2e0637` on 2026-06-24 02:20:46 +0200, verified from local git.
- The only changed file stayed `my-app/src/modules/local-mcp/__tests__/localMcpDevEndpoint.test.ts`.
- Focused endpoint test result was reported as 13 tests passed.
- Broader local-MCP suite result was reported as 56 files / 1197 tests passed.
- `git diff --check 1f121b008296fb47cc13519595e9e0ac0c2e0637^1..1f121b008296fb47cc13519595e9e0ac0c2e0637` was clean in the app checkout.
- The tests now prove the endpoint is disabled by default, stays loopback-only when enabled, accepts only POST JSON, rejects oversized and invalid JSON-RPC requests, returns fixture-only `initialize` and `tools/list` payloads, and keeps `tools/call` blocked.
- No runtime permission is granted by this checkpoint.
- Production `/mcp`, production `tools/list`, production `tools/call`, real handlers, real data, OAuth runtime, outbound/model calls, write actions, PR88, and PR89 remain blocked.
- Rollback is limited to reverting the PR251 merge / the test file change; no runtime rollback is required.

## Implications

PR87.10 is now the test-proof checkpoint for the dev endpoint boundary. The next MCP slice should be the auth/OAuth architecture decision, not runtime exposure, because the remaining blockers are still policy and boundary work rather than a missing reachability proof.

## Touched pages

- [[product/chatgpt-app-sdk-roadmap]]
- [[product/manual-application-handoff]]
- [[hot]]
- [[index]]
