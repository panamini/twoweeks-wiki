---
title: "MCP Auth Request Orchestrator Boundary Checkpoint - PR87.14A"
category: source
tags: [chatgpt-app, apps-sdk, mcp, auth, checkpoint, pr87-14a]
created: 2026-06-24
updated: 2026-06-24
status: current
type: analysis
related: [[product/chatgpt-app-sdk-roadmap]], [[product/manual-application-handoff]], [[sources/2026-06-24-pr87-13-mcp-auth-policy-boundary-checkpoint]], [[sources/2026-06-24-pr87-12-mcp-dev-fixture-demo-checkpoint]], [[sources/2026-06-24-pr87-11-mcp-auth-account-linking-architecture-checkpoint]]
---

# MCP Auth Request Orchestrator Boundary Checkpoint - PR87.14A

## Summary

PR255, [PR87.14A: add MCP auth request orchestrator boundary](https://github.com/panamini/neyssan/pull/255), merged a local-MCP auth request orchestrator into `application-os-foundation`. It composes strict Bearer parsing, a verifier port, the PR87.13 policy boundary, account-link resolution, safe challenge output, a deny-all default verifier, and server-only authorization success data without wiring the endpoint runtime yet.

## Key points

- PR255 merged into `application-os-foundation` as merge commit `01aae0571b671f7b66141dbaff3796886c7186ad` on 2026-06-24.
- The reviewed head SHA before merge was `36531ae971931e37985b71bb00eac33190300e3a`.
- The changed files stayed exactly:
  - `my-app/src/modules/local-mcp/mcpAuthRequestOrchestrator.ts`
  - `my-app/src/modules/local-mcp/__tests__/mcpAuthRequestOrchestrator.test.ts`
- The PR preserves the PR87.13 policy boundary instead of duplicating it.
- The runtime verifier default is deny-all until a real verifier is explicitly provided in a later slice.
- Validation reported:
  - `mcpAuthRequestOrchestrator.test.ts`: 41 tests passed
  - full local-MCP test suite: 58 files / 1331 tests passed
  - `tsc --noEmit --pretty false`: passed
  - targeted ESLint on the touched orchestrator and test files: passed
  - `git diff --check origin/application-os-foundation...HEAD`: passed
  - changed-file guard returned exactly the two files listed above
  - forbidden-surface guards found no package/lockfile, Vite config, endpoint wiring, tools/list, metadata route, Convex/Clerk/Stytch import, network call, model call, production route, or cover-letter path change
  - GitHub checks were green: CI, Playwright Tests, and CodeRabbit success
- Non-permissions remain unchanged: no production `/mcp`, no production `tools/list` or `tools/call`, no runtime OAuth enablement, no real Stytch token verification, no OAuth callback or token exchange, no Clerk lookup, no Convex, no account-link persistence, no real data, no outbound HTTP, no model calls, no write/export/send/apply, no PR88, and no PR89.

## Implications

PR87.14A makes the auth request decision boundary testable and reviewable before endpoint wiring. The next slice is PR87.14B: wire this orchestrator and the PR87.13 metadata/policy boundary into the local/dev fixture endpoint only, preserving default-off and deny-all runtime behavior.

## Rollback

Revert PR255 to remove the orchestrator boundary. PR87.13 policy/metadata code, PR87.12 fixture demo behavior, and earlier local/dev reachability checkpoints remain in place; no data migration, provider cleanup, token cleanup, or production rollback is required.

## Touched pages

- [[product/chatgpt-app-sdk-roadmap]]
- [[hot]]
- [[index]]
