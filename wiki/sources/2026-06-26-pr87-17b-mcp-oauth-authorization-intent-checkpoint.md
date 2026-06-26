---
title: "MCP OAuth Authorization Intent Storage Checkpoint - PR87.17B"
category: source
type: checkpoint
created: 2026-06-26
status: current
tags: [mcp, chatgpt-app, apps-sdk, auth, oauth, intent, checkpoint]
---

# MCP OAuth Authorization Intent Storage Checkpoint - PR87.17B

PR267, [PR87.17B: add MCP OAuth authorization intent storage](https://github.com/panamini/neyssan/pull/267), merged the server-only authorization-intent storage boundary on `application-os-foundation`.

PR87.17B adds short-lived one-time OAuth authorization-intent storage for the already-validated MCP OAuth handoff. It stores only the digest of the opaque continuation handle, keeps the raw handle out of storage, supports one-time consume, and leaves login-return routing and UI integration deferred.

## Merge facts

- PR: <https://github.com/panamini/neyssan/pull/267>
- Final merged head SHA: `4e78cdb302eb8d9b12422db7b8668197de8f73e3`
- Merge commit SHA: `108f740a5cbcc5a75c58d0e16bd865f9e98ba169`
- Merged at: `2026-06-26T01:21:01Z`
- Base after merge: `application-os-foundation` at `108f740a5cbcc5a75c58d0e16bd865f9e98ba169`
- Merge method: merge commit.

## Changed app files

- `my-app/convex/__tests__/mcpOAuthAuthorizationIntents.test.ts`
- `my-app/convex/mcpOAuthAuthorizationIntents.ts`
- `my-app/convex/schema.ts`

## Runtime behavior recorded

PR87.17B adds server-only authorization-intent storage with digest-only handles and one-time consumption semantics. The created intent is short-lived, bound to the trusted owner, and expires or fails generically when replayed, consumed twice, or mismatched. The raw continuation handle is never written to storage, and the storage layer does not open any route, login UI, OAuth callback, or production behavior.

## Non-permissions

PR87.17B does not add production `/mcp`, production `tools/list`, production `tools/call`, OAuth authorization endpoint, OAuth callback, authorization-code exchange, consent UI, token persistence, raw-token storage, refresh-token storage, public account-link API, public Convex function, endpoint/Vite wiring, provider network calls, Clerk network lookup, real application-data access, outbound HTTP, model calls, write/export/send/apply behavior, provider dashboard changes, production flags, billing, PR88, or PR89.

It also does not change cover-letter behavior or mutate production/staging.

## Rollback

Revert PR267 to remove the server-only authorization-intent storage mutations and tests.

After rollback:

- PR87.17A authorization-request boundary remains.
- No authorization-intent storage checkpoint persists.
- No migration rollback is required.
- No production rollback is required.

## Next slice

The next step is `PR87.17C` as a separate explicit request and reviewed slice.

PR87.17C must not be started from this checkpoint. Its scope must stay separate from cover-letter work, production/staging mutation, PR88, and PR89 unless a later prompt explicitly opens those surfaces.

## Touched pages

- [[product/chatgpt-app-sdk-roadmap]]
- [[hot]]
- [[index]]
