---
title: "PR309 MCP Protocol Compatibility Checkpoint"
category: source
tags: [mcp, chatgpt-app, protocol, private-beta, checkpoint]
created: 2026-07-13
updated: 2026-07-13
status: current
type: checkpoint
related: [[product/chatgpt-app-sdk-roadmap]], [[howto/chatgpt-mcp-private-beta-tunnel-connector]]
---

# PR309 MCP Protocol Compatibility Checkpoint

## Merged result

Application PR309 merged into `application-os-foundation` as `b2090fd71e643120d2d695704536d1a45f690b57`. Its final reviewed head was `6db6bacef190cc4f62d9ea1ba3999a54abeaefbf`.

The first causal boundary was an MCP protocol-version mismatch: ChatGPT used the documented `2025-06-18` version while the server accepted only `2025-11-25`. PR309 accepts exactly those two versions and returns the supported version requested by the client; requests without a supported version retain the latest `2025-11-25` fallback.

## Live proof

- Post-merge `./run.sh mcp-smoke` passed against the public private-beta endpoint.
- A public MCP lifecycle using `2025-06-18` returned HTTP `200` and exactly six tools: `search`, `fetch`, and the four existing twoweeks read-only summary tools.
- The fresh ChatGPT connector displayed exactly six Actions, including exactly one `twoweeks.application_package.summarize` action.
- One authenticated ChatGPT call to `twoweeks.application_package.summarize` succeeded with the safe deterministic `no_data_available` result, schema version `1`, and zero counts. No private content was recorded.
- The connector and successful authenticated tool call are behavioral evidence of OAuth completion. `POST /oauth/token` was not captured separately and must not be described as direct network-log proof.

## Verification

- Focused MCP protocol and route tests passed.
- Application build passed.
- `./run.sh mcp-smoke` passed before and after merge.
- GitHub JavaScript tests, Playwright, and Semgrep passed.
- Codex Review reported no major issue on the exact final head.
- A context-separated final review concluded `LOCAL_REVIEW_CLEAR`.

## Boundary

PR309 changes protocol compatibility only. It does not add a new tool or result field, change OAuth clients, redirects, secrets, tokens, sessions, account linking, or eligibility, call providers or models, write data, add refresh tokens, alter billing, or authorize public launch.
