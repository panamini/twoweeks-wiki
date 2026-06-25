---
title: "MCP Account-Link Lifecycle Checkpoint - PR87.16"
category: source
type: checkpoint
created: 2026-06-25
status: current
tags: [mcp, chatgpt-app, apps-sdk, auth, account-link, checkpoint]
---

# MCP Account-Link Lifecycle Checkpoint - PR87.16

PR264, [PR87.16: add authoritative MCP account-link lifecycle](https://github.com/panamini/neyssan/pull/264), merged the authoritative server-only MCP account-link lifecycle on `application-os-foundation`.

PR87.16 adds canonical internal Convex link, refresh, and revoke operations for MCP account links. It accepts only already-verified OAuth evidence from a trusted server-side source, keeps the Twoweeks owner identity separate from provider evidence, and proves create -> lookup -> authorize plus revoke -> deny behavior.

## Merge facts

- PR: <https://github.com/panamini/neyssan/pull/264>
- Final merged head SHA: `1a3a94821b0d5409db64b88d5a7d500672c09b22`
- Merge commit SHA: `ba62200d28deaae56387e06fd13e20aea580758d`
- Merged at: `2026-06-25T18:26:13Z`
- Base after merge: `application-os-foundation` at `ba62200d28deaae56387e06fd13e20aea580758d`
- Merge method: admin squash merge.

## Changed app files

- `docs/plans/2026-06-25-pr87-16-mcp-account-link-lifecycle-brief.md`
- `my-app/convex/__tests__/mcpAccountLinks.test.ts`
- `my-app/convex/mcpAccountLinks.ts`

## Runtime behavior recorded

PR87.16 adds three server-only lifecycle operations:

- `link`: validates the trusted owner and verified OAuth evidence, checks canonical same-principal candidates, creates one active canonical row, and is idempotent for identical existing evidence.
- `refresh`: updates exactly one active same-owner/same-client canonical row with newer evidence, rejects replay and expiry regression, and creates no row.
- `revoke`: marks the exact owner-owned canonical row revoked without deleting it and is idempotent for already-revoked rows.

Relink/reactivation remains intentionally unsupported because no current policy defines safe reactivation. Revoked rows return `relink_required` on create.

The lifecycle evidence contract requires provider, issuer, subject, provider environment, client ID, resource, canonical granted scope, expiry, verification timestamp, and version. The proof marker is `already_verified_by_provider_adapter`; the canonical scope is `twoweeks:applications:read`.

Gate87.16A1 preflight returned `MCP_INSPECTOR_AUTH_GATE_GREEN_WITH_DESCRIPTOR_NORMALIZATION_NOTE` with MCP Inspector `0.22.0`: raw endpoint top-level `securitySchemes` and `_meta.securitySchemes` were present, Inspector stripped top-level `securitySchemes` while preserving `_meta.securitySchemes`, metadata/auth behavior passed, and no runtime/auth descriptor change was needed.

## Validation and review disposition

Local validation before merge reported:

- Focused account-link lifecycle tests passed: 66 tests.
- Adjacent auth/runtime tests passed: 9 files / 339 tests.
- Full local-MCP suite passed: 63 files / 1457 tests.
- Full Convex test scope passed: 21 files / 282 tests.
- TypeScript build passed.
- Targeted ESLint passed.
- `npm run build` passed with existing Vite/Browserslist/pdfjs/chunk warnings.
- `git diff --check origin/application-os-foundation...HEAD` passed.
- Source-only forbidden-surface grep passed.
- Fallow read-only audit was advisory only: inherited dead-code noise, introduced complexity hotspots, and inherited duplication remained; no introduced unresolved imports, unlisted dependencies, circular dependencies, or boundary violations were reported.

Review and remote status at merge:

- CodeRabbit status context was `SUCCESS`.
- The latest CodeRabbit review also recorded one minor test-tightening suggestion on the final head; the PR was still admin-squash-merged with the CodeRabbit status green.
- Semgrep cloud scan was `SUCCESS`.
- Remote `CI / js-tests` failed twice.
- Remote `Playwright Tests / test` failed.
- `gh run view --log-failed` returned `log not found` for failed jobs `83483215187`, `83483202561`, and `83483215863`.
- The Actions job API returned empty `steps` arrays for those failed jobs.

The merge proceeded as an admin squash merge after the local validation and review/security status above.

## Non-permissions

PR87.16 does not add production `/mcp`, production `tools/list`, production `tools/call`, OAuth authorization endpoint, OAuth callback, authorization-code exchange, consent UI, token persistence, raw-token storage, refresh-token storage, public account-link API, public Convex function, endpoint/Vite wiring, provider network calls, Clerk network lookup, real application-data access, outbound HTTP, model calls, write/export/send/apply behavior, provider dashboard changes, production flags, billing, PR88, or PR89.

It also does not change cover-letter behavior or mutate production/staging.

## Rollback

Revert PR264 to remove the server-only account-link lifecycle mutations and tests.

After rollback:

- PR263 auth runtime remains.
- PR261 composition remains.
- PR259 lookup remains.
- PR258 storage contract remains.
- No account-link lifecycle mutation remains.
- No migration rollback is required.
- No token revocation is required.
- No provider/dashboard rollback is required.
- No production rollback is required.

## Next slice

The next step is `PR87.17A` as a separate explicit request and reviewed slice.

PR87.17A must not be started from this checkpoint. Its scope must stay separate from cover-letter work, production/staging mutation, PR88, and PR89 unless a later prompt explicitly opens those surfaces.

## Touched pages

- [[product/chatgpt-app-sdk-roadmap]]
- [[hot]]
- [[index]]
