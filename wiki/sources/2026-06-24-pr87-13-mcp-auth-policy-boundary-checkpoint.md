---
title: "MCP Auth Metadata And Policy Boundary Checkpoint - PR87.13"
category: source
tags: [chatgpt-app, apps-sdk, mcp, auth, checkpoint, pr87-13]
created: 2026-06-24
updated: 2026-06-24
status: current
type: analysis
related: [[product/chatgpt-app-sdk-roadmap]], [[product/manual-application-handoff]], [[sources/2026-06-24-pr87-12-mcp-dev-fixture-demo-checkpoint]], [[sources/2026-06-24-pr87-11-mcp-auth-account-linking-architecture-checkpoint]], [[sources/2026-06-24-pr87-10-mcp-dev-endpoint-blocked-reachability-checkpoint]]
---

# MCP Auth Metadata And Policy Boundary Checkpoint - PR87.13

## Summary

PR254, [PR87.13: add MCP auth metadata and policy boundary](https://github.com/panamini/neyssan/pull/254), merged a pure local-MCP auth policy boundary into `application-os-foundation`. It adds protected-resource metadata, canned Bearer challenge construction, already-verified-claims policy evaluation, and server-only account-link resolution without wiring OAuth or auth into a runtime endpoint.

## Key points

- PR254 merged into `application-os-foundation` as merge commit `b23a83b3d9652093f7cbb79b1fd7fe5f7e2c1b49` on 2026-06-24, verified from GitHub merge result and local fetch.
- The head SHA before merge was `fb319b565e593a01f93c03d2e1fd06b7b6a5c4cc`.
- The changed files stayed exactly:
  - `my-app/src/modules/local-mcp/mcpAuthPolicyBoundary.ts`
  - `my-app/src/modules/local-mcp/__tests__/mcpAuthPolicyBoundary.test.ts`
  - `my-app/src/modules/local-mcp/mcpAccountLinkingStorageBoundary.ts`
- The boundary remains pure policy/metadata code. It does not register routes, verify JWTs, persist tokens, call Clerk or Stytch runtime APIs, call Convex, make outbound HTTP/model calls, expose production `/mcp`, or use real user data.
- Bearer challenges now derive from closed OAuth Bearer errors and canned descriptions only; free-form `input.error` / `input.errorDescription` values are not reflected.
- `resolveMcpAuthPolicyAccountLink` now validates the authorized principal shape at runtime before link matching and fails closed on malformed or identity-override input.
- Account-link records now validate safe finite non-negative integer timestamps and reject `updatedAtEpochSeconds < createdAtEpochSeconds`.
- Validation reported:
  - focused `mcpAuthPolicyBoundary.test.ts`: 89 tests passed
  - adjacent local-MCP tests: 79 tests passed
  - full local-MCP suite: 57 files / 1290 tests passed
  - `tsc --noEmit --pretty false`: passed
  - targeted ESLint on touched local-MCP files: passed
  - `git diff --check origin/application-os-foundation...HEAD`: passed
  - GitHub CodeRabbit status: success
- CodeRabbit's fresh review reported no actionable comments. The docstring coverage item remained advisory only and was not a required blocking check.
- Production MCP, runtime OAuth wiring, Stytch runtime, Clerk runtime, Convex runtime, real handlers, real data, outbound/model calls, live submit/apply, approved-answer copy, billing, PR88, and PR89 remain blocked.

## Implications

PR87.13 makes the auth-policy contract testable and reviewable before any runtime wiring. It is a policy-boundary checkpoint, not an authorization launch checkpoint; the next MCP/App SDK slice still needs a separate reviewed decision before endpoint auth wiring or production exposure begins.

## Touched pages

- [[product/chatgpt-app-sdk-roadmap]]
- [[hot]]
- [[index]]
