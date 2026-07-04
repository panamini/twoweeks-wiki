---
title: "PR304 Live MCP Connector Smoke Checkpoint"
category: source
tags: [chatgpt-app, mcp, oauth, cloudflare, private-beta, smoke]
created: 2026-07-04
updated: 2026-07-04
status: current
type: checkpoint
related: [[product/chatgpt-app-sdk-roadmap]], [[howto/chatgpt-mcp-private-beta-tunnel-connector]]
---

# PR304 Live MCP Connector Smoke Checkpoint

## Summary

PR304 is a merged proof slice for the ChatGPT private-beta connector boundary after PR303. It proves the local Vite/Convex OAuth/MCP/read-only summary path through a real ChatGPT connector and an ephemeral Cloudflare quick tunnel, without opening public launch or write surfaces.

## Key points

- Base app state: `origin/application-os-foundation` after PR303 merge commit `f63d35dc6f8ae765d9afb004991e2a2aeb6c5679`.
- App branch: `codex/mcp-pr304-live-connector-smoke`.
- App PR: `https://github.com/panamini/neyssan/pull/304`, merged as `d158768d28e418aeca5e176e504b8cf79fb1a8c1`.
- Tunnel used for proof: `https://are-effort-skirts-hints.trycloudflare.com`.
- Connector used for proof: `twoweeks-mcp-pr304-fixed-1783182736885`.
- The tunnel was created with `cloudflared tunnel --config /dev/null --no-autoupdate --loglevel info --protocol http2 --url http://localhost:5187`.
- `--config /dev/null` was required because the local default cloudflared config routed quick tunnels to `http_status:404`.
- Live ChatGPT tool call for `twoweeks.application_package.summarize` returned `status=available`, `count=1`, and real read-side data.

## Verification

- Focused production MCP route/tool-call tests passed: 194 tests.
- Broader focused MCP/OAuth/sign-in continuation tests passed: 228 tests.
- `rtk npx tsc -p tsconfig.node.json --pretty false` passed.
- `rtk git diff --check` passed.
- OAuth metadata and MCP `tools/list` were reachable through the tunnel.
- `tools/list` returned the four read-only summary tools.
- ChatGPT connector smoke reached real Convex/read-side data instead of synthetic fallback or empty stub data.

## Fixes captured by PR304

- Local Vite route wiring for the private-beta connector proof.
- Mixed-auth discovery behavior for connector handshake.
- OAuth continuation handling for direct sign-in return and browser nonce ordering.
- Safe handling of bounded client `_meta` on production `tools/call`.
- OAuth security-scheme projection for the read-only MCP tools.

## Boundaries

PR304 does not approve public launch. It does not add provider calls, write actions, refresh tokens, billing, account-link lifecycle expansion, production/shared DB mutation, or raw user-data logging.

## Touched pages

- [[product/chatgpt-app-sdk-roadmap]]
- [[howto/chatgpt-mcp-private-beta-tunnel-connector]]
- [[hot]]
- [[index]]
- [[log]]
