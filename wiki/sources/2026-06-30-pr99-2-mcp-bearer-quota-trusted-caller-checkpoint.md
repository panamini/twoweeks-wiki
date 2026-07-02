---
title: "MCP Bearer Quota Trusted Caller Checkpoint - PR99.2"
category: source
type: checkpoint
created: 2026-06-30
updated: 2026-06-30
status: current
tags: [mcp, chatgpt-app, apps-sdk, auth, oauth, bearer-token, production-gate, quota]
---

# MCP Bearer Quota Trusted Caller Checkpoint - PR99.2

PR287 merged PR99.2 into `application-os-foundation` as the follow-up fix to PR99.1's `/mcp` bearer-verification quota.

PR99.2 keeps the production MCP surface authenticated-but-blocked. It does not unlock MCP execution, JSON-RPC `tools/list`, JSON-RPC `tools/call`, provider calls, refresh tokens, account-link lifecycle, private beta, public launch, or UI changes.

## Merge facts

- PR287: <https://github.com/panamini/neyssan/pull/287>
  - Title: `PR99.2: trust socket address for MCP bearer quota`
  - Final head SHA: `b1d36fba3c74ca98854a7b75243f64774dbdc289`
  - Merge commit SHA: `82fa9a09e40d2243bd2d220785c094788ff9e703`
  - Merged at: `2026-06-30T04:20:56Z`
  - Base branch: `application-os-foundation`

## PR99.2 merged state

PR99.2 changes the production `/mcp` bearer-verification quota caller key so it uses the trusted socket address from the request boundary instead of caller-controlled forwarding headers such as `X-Forwarded-For`.

The existing authorize/token pre-auth quota behavior is intentionally unchanged. The change is scoped to the `/mcp` bearer-verification quota before access-token verification enters Convex.

## Review follow-up

Post-merge Qodo review reported two narrow caller-key robustness issues:

- Equivalent trusted socket address forms, especially IPv4-mapped IPv6, may produce different quota keys if they are not canonicalized.
- If an integration invokes the production route adapter without a trusted `remoteAddress`, `/mcp` bearer-verification quota falls back to the shared key `unknown`.

These findings do not reopen caller-controlled forwarding-header trust, but they should be fixed before moving into the production MCP protocol layer.

## Next state

Historical state at PR99.2 merge: the next narrow app PR was PR99.3 MCP bearer quota caller-key hardening:

- canonicalize trusted socket address forms before quota keying;
- fail closed for `/mcp` bearer verification when a trusted remote address is unavailable;
- keep authorize/token quota behavior unchanged unless a test proves the shared helper must change;
- keep MCP execution, `tools/list`, `tools/call`, provider calls, refresh tokens, account-link lifecycle, private beta, public launch, and UI changes blocked.

Superseding note: PR99.3, PR100, and PR101 have since merged. The current next app PR is PR102 `tools/call` read-only boundary plus hardening.

## Touched pages

- [[product/chatgpt-app-sdk-roadmap]]
- [[hot]]
- [[index]]
