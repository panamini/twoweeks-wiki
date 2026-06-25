---
title: "MCP Account-Link Canonical Storage Checkpoint - PR87.15B0"
category: source
tags: [chatgpt-app, apps-sdk, mcp, auth, account-link, checkpoint, pr87-15b0]
created: 2026-06-25
updated: 2026-06-25
status: current
type: analysis
related: [[product/chatgpt-app-sdk-roadmap]], [[product/manual-application-handoff]], [[sources/2026-06-25-pr87-15a-mcp-stytch-bearer-verifier-checkpoint]], [[sources/2026-06-24-pr87-13-mcp-auth-policy-boundary-checkpoint]], [[sources/2026-06-24-pr87-11-mcp-auth-account-linking-architecture-checkpoint]]
---

# MCP Account-Link Canonical Storage Checkpoint - PR87.15B0

## Summary

PR258, [PR87.15B0: add MCP canonical account-link storage contract](https://github.com/panamini/neyssan/pull/258), merged the canonical storage/index contract for future MCP account-link lookup into `application-os-foundation`. It adds optional canonical account-link fields, canonical storage classification/projection helpers, and the provider/issuer/subject/environment index, while preserving legacy account-link rows and existing resolver behavior.

## Key points

- PR258 merged into `application-os-foundation` as merge commit `06a76a0b5f87f0d30c24635c436cfe3ffa80b29a` on 2026-06-25 UTC.
- The merged head SHA was `7c6ccc30c55334570da2da3d279f13920033a915`.
- The base before PR258 was PR257 / PR87.15A at `372d16830dd6d3b66f39ba96e317641dcb207793`.
- The changed files stayed exactly:
  - `my-app/convex/schema.ts`
  - `my-app/convex/mcpAccountLinks.ts`
  - `my-app/convex/__tests__/mcpAccountLinks.test.ts`
- The canonical storage contract adds:
  - optional canonical `issuer`
  - canonical `providerSubject`
  - optional `providerEnvironment`
  - optional `canonicalGrantedScopes`
  - optional `expiresAtEpochSeconds`
  - optional `canonicalAccountLinkVersion: 1`
  - index `by_provider_issuer_subject_environment` on `provider`, `issuer`, `providerSubject`, and `providerEnvironment`
  - `classifyMcpAccountLinkCanonicalStorageRecord`
  - `projectMcpAccountLinkCanonicalStorageRecordToPolicyCandidate`
- Legacy rows remain untouched and ineligible for canonical MCP auth unless all authoritative canonical fields are present and valid.
- Existing legacy resolver behavior remains unchanged.

## Validation

- `rtk npx vitest --run convex/__tests__/mcpAccountLinks.test.ts`: 24 passed.
- `rtk npx vitest --run src/modules/local-mcp/__tests__`: 59 files / 1377 passed.
- `rtk npx tsc --build --pretty false`: passed.
- `rtk npx eslint convex/mcpAccountLinks.ts convex/schema.ts --ext ts --report-unused-disable-directives --max-warnings 0`: passed.
- `rtk npx eslint --no-ignore convex/__tests__/mcpAccountLinks.test.ts --ext ts --report-unused-disable-directives --max-warnings 0`: passed.
- `rtk npm run build`: passed with existing Browserslist/pdfjs/chunk-size warnings only.
- `rtk npx fallow audit --changed-since origin/application-os-foundation --format compact`: exit 0; 3 changed files; inherited findings excluded.
- `git diff --check origin/application-os-foundation...HEAD`: passed.

## Implications

PR87.15B0 is a canonical storage/index contract only. It does not add the final lookup adapter, endpoint wiring, Vite middleware wiring, Stytch verifier runtime wiring, production `/mcp`, production `tools/list`, production `tools/call`, OAuth callback, authorization-code exchange, refresh-token flow, PKCE runtime, Stytch API calls, remote JWKS fetch, token introspection, token persistence, account-link creation or mutation, public Convex query/mutation, HTTP action, Clerk lookup, real user data, consent storage, outbound HTTP, model calls, write/export/send/apply behavior, provider dashboard changes, production flags, billing, PR88, or PR89.

PR87.15B1 may add a server-only lookup adapter that reads canonical same-principal candidates through the PR258 index and hands them to the existing MCP auth policy resolver, but it still must not wire runtime auth or production MCP behavior.

## Rollback

Revert PR258 to remove the canonical account-link storage fields, index, projection helpers, and tests. No data migration, provider cleanup, token cleanup, production endpoint rollback, Vite rollback, package rollback, or lockfile rollback is required because PR87.15B0 added no runtime wiring and no account-link mutation path.

## Touched pages

- [[product/chatgpt-app-sdk-roadmap]]
- [[hot]]
- [[index]]
