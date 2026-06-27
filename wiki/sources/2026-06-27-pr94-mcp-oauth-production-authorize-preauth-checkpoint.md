---
title: "MCP OAuth Production Authorize Pre-auth Checkpoint - PR94"
category: source
type: checkpoint
created: 2026-06-27
updated: 2026-06-27
status: current
tags: [mcp, chatgpt-app, apps-sdk, auth, oauth, production-gate, pre-auth, checkpoint]
---

# MCP OAuth Production Authorize Pre-auth Checkpoint - PR94

PR279 connected production `/oauth/authorize` to the existing ownerless pre-auth intent creation path behind the PR89 activation gate, PR90 operational status, PR92 production route preflight, and PR93 route shells.

This checkpoint supersedes the PR89-PR93 route-shell state only for production `/oauth/authorize`. It does not unlock production `/oauth/callback`, `/mcp`, provider execution, owner binding, authorization-code issuance, token exchange, account-link creation, token persistence, `tools/list`, or `tools/call`.

## Merge facts

- PR279: <https://github.com/panamini/neyssan/pull/279>
  - Title: `PR94: connect production /oauth/authorize to existing pre-auth intent creation`
  - Final pushed head SHA before base merge: `1d2fcc8ee151e6adbfe777871bccf10fafcdb40a`
  - Final merged head SHA: `51a1a8052afd42b9d4d1788205506d5c14210a4c`
  - Merge commit SHA: `d9e42556a511ca5b3e78dce07f48b2366b210a0d`
  - Merged at: `2026-06-27T21:22:08Z`
  - Base branch: `application-os-foundation`

## Implementation summary

PR94 reuses the existing reviewed OAuth pieces instead of creating a parallel pre-auth path:

- PR87.17A authorization request projection
- PR87.17C3 pre-auth intent storage
- existing digest-backed continuation handle convention
- existing Clerk sign-in return path convention

When production route wiring is enabled and preflight allows `/oauth/authorize`, the route validates the request, applies quota protection, creates an ownerless pre-auth intent, and redirects to sign-in with the raw continuation handle only in the browser redirect. The stored row keeps the digest-backed pre-auth handle and server-only authorization request projection.

`/oauth/callback` and `/mcp` remain guarded inert production handlers.

## Review-driven fixes included

PR94 incorporated review fixes before merge:

- Default production dependencies are wired from the real Vite config path, so `/oauth/authorize` no longer returns `dependency_unavailable` solely because tests injected dependencies.
- `configurePreviewServer` installs the same middleware as `configureServer`.
- `preview.allowedHosts` and `server.allowedHosts` include the configured production OAuth host when the origin is a valid `http:` or `https:` origin.
- Local `/mcp` remains ahead of production route wiring when both local MCP and production route flags are enabled.
- Production `/oauth/authorize` remains ahead of the local OAuth route when both OAuth route flags are enabled.
- Convex client construction fails closed on bad URLs instead of crashing plugin setup.
- The create deadline is refreshed after quota completes.
- The production resource guard trims `MCP_OAUTH_PRODUCTION_RESOURCE` consistently with the authorization request config.
- Default pre-auth quota keys include a caller dimension from forwarded headers or remote address.
- Convex pre-auth storage rejects create requests whose caller deadline has already passed on server time.

## Validation evidence

- Focused production route adapter and Convex pre-auth tests passed.
- Broader OAuth/local MCP subset passed with 215 tests.
- TypeScript `tsc --noEmit --pretty false` passed.
- `git diff --check` passed.
- Fallow audit was run and reported only inherited advisory duplication/dependency/complexity findings.
- CodeRabbit and Qodo were triggered after the final fixes; Qodo reported no open findings for the final review-fix commit.
- Codex review trigger was attempted, but the connector reported code review usage limits.
- GitHub `semgrep-cloud-platform/scan` passed on the PR head.
- GitHub `js-tests` remained red for the Match Review guardrail job; PR279 was merged with admin bypass after the PR branch was brought up to date with `application-os-foundation`.

## Non-permissions

PR94 does not call Stytch or another OAuth provider, run consent, bind owners, resolve provider subjects, create owner-bound intents, issue authorization codes, exchange tokens, create account links, persist tokens, read real user data through production MCP, expose `tools/list`, expose `tools/call`, deploy hosted MCP, or open PR88/private beta/public launch behavior.

## Next state

Do not rerun PR89, PR90, PR92, PR93, or PR94.

Do not create PR88 retroactively.

The next narrow app PR should be the production login-return / owner-binding continuation slice: consume the pre-auth continuation after sign-in, bind the authenticated owner server-side, and prepare the owner-bound continuation handoff while keeping provider validation, consent, authorization-code issuance, token exchange, account-link creation, token persistence, `/mcp`, `tools/list`, and `tools/call` blocked unless that PR explicitly opens them behind reviewed gates.

## Touched pages

- [[product/chatgpt-app-sdk-roadmap]]
- [[hot]]
- [[index]]
