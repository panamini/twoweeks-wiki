---
title: "MCP Account-Link Lookup Adapter Checkpoint - PR87.15B1"
category: source
tags: [chatgpt-app, apps-sdk, mcp, auth, account-link, checkpoint, pr87-15b1]
created: 2026-06-25
updated: 2026-06-25
status: current
type: analysis
related: [[product/chatgpt-app-sdk-roadmap]], [[product/manual-application-handoff]], [[sources/2026-06-25-pr87-15b0-mcp-account-link-canonical-storage-checkpoint]], [[sources/2026-06-25-pr87-15a-mcp-stytch-bearer-verifier-checkpoint]], [[sources/2026-06-24-pr87-14a-mcp-auth-request-orchestrator-checkpoint]]
---

# MCP Account-Link Lookup Adapter Checkpoint - PR87.15B1

## Summary

PR259, [PR87.15B1: add server-only MCP account-link lookup adapter](https://github.com/panamini/neyssan/pull/259), merged the bounded account-link lookup adapter into `application-os-foundation`. It adds the server-only adapter that converts the request-orchestrator account-link lookup port into an injected Convex query call, plus the bounded internal Convex query that reads canonical same-principal candidates through the PR87.15B0 index.

## Key points

- PR259 merged into `application-os-foundation` as merge commit `732bef170fd4175cb70cd2f0cc1bda858f2e93bb` on 2026-06-25 UTC.
- The merged head SHA was `4bc277f28253ffe8411160615d8af68f7cdd4b95`.
- The base before PR259 was PR258 / PR87.15B0 at `06a76a0b5f87f0d30c24635c436cfe3ffa80b29a`.
- The changed files stayed exactly:
  - `my-app/convex/__tests__/mcpAccountLinks.test.ts`
  - `my-app/convex/mcpAccountLinks.ts`
  - `my-app/src/modules/local-mcp/__tests__/mcpConvexAccountLinkLookupAdapter.test.ts`
  - `my-app/src/modules/local-mcp/mcpConvexAccountLinkLookupAdapter.ts`
- The adapter module exports `buildMcpConvexAccountLinkLookupAdapter`, `McpConvexAccountLinkLookupRunQueryV1`, and `McpConvexAccountLinkLookupAdapterConfigV1`.
- The adapter requires explicit `serverOnly: true`, `version: 1`, an opaque `queryRef`, and an injected `runQuery`; it does not import Convex runtime, generated Convex client code, Vite, React, or endpoint wiring.
- The bounded Convex query is `internalLookupMcpAuthPolicyAccountLinkCandidates`; it receives `issuer`, `subject`, `providerEnvironment`, and `version: 1`, queries index `by_provider_issuer_subject_environment` for provider `stytch`, projects canonical storage rows through `projectMcpAccountLinkCanonicalStorageRecordToPolicyCandidate`, sorts candidates deterministically, and returns malformed candidates for invalid input or candidate overflow.
- This checkpoint completes the lookup-adapter boundary required before any later non-production auth composition slice.

## Validation

- GitHub PR metadata verified PR259 is merged into `application-os-foundation` with merge commit `732bef170fd4175cb70cd2f0cc1bda858f2e93bb` and head `4bc277f28253ffe8411160615d8af68f7cdd4b95`.
- GitHub status rollup for PR259 reported `js-tests` success, `test` success, and CodeRabbit success.
- Local fetch verification confirmed `origin/application-os-foundation` resolves to `732bef170fd4175cb70cd2f0cc1bda858f2e93bb`.
- Local ancestry verification confirmed `732bef170fd4175cb70cd2f0cc1bda858f2e93bb` is an ancestor of `origin/application-os-foundation`.
- Local diff verification from `06a76a0b5f87f0d30c24635c436cfe3ffa80b29a` to `732bef170fd4175cb70cd2f0cc1bda858f2e93bb` showed exactly the four files listed above.
- Local source inspection confirmed the adapter and bounded Convex query names above.

## Implications

PR87.15B1 is a server-only lookup-adapter boundary. It does not add endpoint wiring, Vite middleware wiring, runtime Stytch verifier wiring, production `/mcp`, production `tools/list`, production `tools/call`, OAuth callback, authorization-code exchange, refresh-token flow, PKCE runtime, Stytch API calls, remote JWKS fetch, token introspection, token persistence, account-link creation or mutation, public Convex query/mutation, HTTP action, real handlers, real application data, outbound HTTP, model calls, write/export/send/apply behavior, provider dashboard changes, production flags, billing, PR88, or PR89.

The next approved slice may compose the already-merged non-production auth pieces with deterministic synthetic fixtures, but it must not mutate this checkpoint after implementation begins and must not open production MCP behavior.

## Rollback

Revert PR259 to remove the adapter, bounded lookup query, and tests. No data migration, provider cleanup, token cleanup, production endpoint rollback, Vite rollback, package rollback, or lockfile rollback is required because PR87.15B1 added no default runtime wiring and no account-link mutation path.

## Touched pages

- [[product/chatgpt-app-sdk-roadmap]]
- [[hot]]
- [[index]]
