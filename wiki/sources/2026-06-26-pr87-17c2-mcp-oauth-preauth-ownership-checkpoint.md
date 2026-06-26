---
title: "MCP OAuth Pre-Auth Ownership Decision Checkpoint - PR87.17C2"
category: source
type: checkpoint
created: 2026-06-26
updated: 2026-06-26
status: current
tags: [mcp, chatgpt-app, apps-sdk, auth, oauth, ownership, decision, checkpoint]
---

# MCP OAuth Pre-Auth Ownership Decision Checkpoint - PR87.17C2

PR270, [PR87.17C2: add MCP OAuth pre-auth ownership decision](https://github.com/panamini/neyssan/pull/270), merged the docs-only pre-auth ownership checkpoint into `application-os-foundation`.

PR87.17C2 records the `CLERK_OWNER_CONTEXT_GAP` decision for the MCP OAuth path. It adopts the two-phase pre-auth intent model, adds the browser-storage policy that keeps OAuth request state out of browser storage, and keeps route wiring, UI, Stytch consent, token exchange, account-link creation, and production behavior blocked until a later reviewed slice.

## Merge facts

- PR: <https://github.com/panamini/neyssan/pull/270>
- Title: `PR87.17C2: add MCP OAuth pre-auth ownership decision`
- Final merged head SHA: `b3600596bbf61ab2e127e04fd42f3f85548888ad`
- Merge commit SHA: `98653667421349e5c552eef7ea0dd4fbeadb2bda`
- Merged at: `2026-06-26T17:36:03Z`
- Base after merge: `application-os-foundation` at `98653667421349e5c552eef7ea0dd4fbeadb2bda`
- Changed file:
  - `docs/decisions/2026-06-26-mcp-oauth-preauth-ownership-decision.md`
- CodeRabbit status: `SUCCESS`; no actionable comments were generated.
- Semgrep cloud scan: `SUCCESS`.
- GitHub Actions `js-tests` and `Playwright Tests / test` failed before runner startup with a billing/spending-limit annotation; no app runtime regression was implicated by the docs-only diff.

## Decision behavior recorded

PR87.17C2 is a docs-only checkpoint. It records that unauthenticated OAuth intake may preserve only a server-side, short-lived pre-auth intent, that the browser may carry only the opaque continuation handle in the fixed same-origin continuation URL, and that future implementation must not persist raw OAuth request material in browser storage.

The recorded decision keeps owner binding server-side after Clerk sign-in and keeps consent, account-link creation, authorization-code issuance, token exchange, and production MCP behavior blocked until the owner-bound state is explicitly approved.

## Non-permissions

PR87.17C2 does not add a route, React page, router registration, Clerk or Stytch call, Convex runtime/schema import, Vite change, network behavior, browser storage behavior, token/code/account-link behavior, production OAuth runtime, PR88, PR89, cover-letter work, or real user-data access.

## Rollback

Revert PR270 to remove the docs-only amendment from the ADR.

After rollback:

- PR87.17C1 login-return continuation checkpoint remains.
- PR87.17B authorization-intent storage remains.
- PR87.17A authorization-request boundary remains.
- No route/runtime/provider/account-link rollback is required.
- No production rollback is required.

## Next slice

The next step is `PR87.17C3` as a separate reviewed slice.

PR87.17C3 must define the pre-auth OAuth request intent storage contract without opening route wiring, UI, Stytch integration, token exchange, account-link creation, production behavior, PR88, or PR89.

## Touched pages

- [[product/chatgpt-app-sdk-roadmap]]
- [[hot]]
- [[index]]
