---
title: "PR305 Durable MCP Connector Proof Checkpoint"
category: source
tags: [chatgpt-app, mcp, oauth, cloudflare, private-beta, smoke]
created: 2026-07-05
updated: 2026-07-05
status: current
type: checkpoint
related: [[product/chatgpt-app-sdk-roadmap]], [[howto/chatgpt-mcp-private-beta-tunnel-connector]]
---

# PR305 Durable MCP Connector Proof Checkpoint

PR305 is a draft proof-only slice for the durable private-beta MCP connector boundary at:

```text
https://mcp.twoweeks.ai/mcp
```

It does not replace PR304's merged quick-tunnel smoke. It records the follow-up durable-host proof and the remaining ChatGPT UI activation blocker.

## Proven

- Cloudflare named tunnel exists for `mcp.twoweeks.ai`.
- Durable OAuth protected-resource metadata returned `200`.
- Durable private-beta OAuth/token/MCP proof ladder passed directly through `https://mcp.twoweeks.ai`.
- MCP `initialize` worked.
- MCP `tools/list` returned the four read-only summary tools.
- MCP `tools/call` for `twoweeks.application_package.summarize` returned real read-side `application_package` data with `available` status.
- PR305 is docs-only in app code: it adds the proof audit, not a runtime expansion.

## Tunnel

Cloudflare named tunnel:

```text
name: neyssan-mcp-pr305-twoweeks-ai
id: 935a2064-9473-41bc-bd73-174660892847
hostname: mcp.twoweeks.ai
origin: http://127.0.0.1:5187
```

The local global `~/.cloudflared/config.yml` can point at an unrelated parser tunnel. For PR305, run the named tunnel with an explicit config or explicit credentials file for `935a2064-9473-41bc-bd73-174660892847`.

## ChatGPT activation status

The ChatGPT connector was created as:

```text
name: twoweeks-mcp-pr305-durable
url: https://mcp.twoweeks.ai/mcp
client id: local-chatgpt-client
client secret: empty
token endpoint auth: none
scope: twoweeks:applications:read
```

Activation through ChatGPT currently remains blocked at the local login boundary when the Vite worktree lacks `VITE_CLERK_PUBLISHABLE_KEY`. The OAuth request reaches `https://mcp.twoweeks.ai/sign-in`, then the React page cannot render Clerk.

The redirect allowlist for this ChatGPT UI flow must include:

```text
https://chatgpt.com/connector/oauth/*
```

The older `connector_platform_oauth_redirect` value is not sufficient for the current ChatGPT connector OAuth URL shape.

## Boundaries

PR305 does not approve public launch. It does not add provider calls, write actions, refresh tokens, billing, account-link lifecycle expansion, production/shared database mutation, raw user-data logging, or durable hosted production deployment.

## Next action

To finish the UI activation proof, provide or load a valid local `VITE_CLERK_PUBLISHABLE_KEY` for the Vite worktree, keep the named Cloudflare tunnel running, then reconnect `twoweeks-mcp-pr305-durable` from ChatGPT.

## Related

- [[howto/chatgpt-mcp-private-beta-tunnel-connector]]
- [[product/chatgpt-app-sdk-roadmap]]
