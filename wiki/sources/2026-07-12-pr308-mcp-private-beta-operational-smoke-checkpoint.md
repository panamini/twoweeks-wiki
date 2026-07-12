---
title: "PR308 MCP Private-beta Operational Smoke Checkpoint"
category: source
tags: [mcp, oauth, private-beta, smoke, checkpoint]
created: 2026-07-12
updated: 2026-07-12
status: current
type: checkpoint
related: [[product/chatgpt-app-sdk-roadmap]], [[howto/chatgpt-mcp-private-beta-tunnel-connector]]
---

# PR308 MCP Private-beta Operational Smoke Checkpoint

## Merged result

Application PR308 merged into `application-os-foundation` as `b101a75a1b625f7b0f3a62f677f474b4a030bff6`. Its final reviewed head was `99e0cd6a340b8efdb972e5a0b944498514a780fb`.

`./run.sh mcp-smoke` is the no-credential public canary for the private-beta MCP boundary. It skips dotenv, local secret-file, and runtime-state setup, disables `xtrace`, sends no authorization header or cookie, and never prints response bodies.

## Contract retained as durable knowledge

- Authorization-server and protected-resource metadata are exact: confidential `client_secret_post`, PKCE `S256`, authorization-code grant/response, issuer-response parameter support, one read-only scope, and canonical origins/resources.
- The MCP probe completes `initialize` then `notifications/initialized`, requires the negotiated `2025-11-25` protocol, and advertises JSON plus SSE for Streamable HTTP.
- Unauthenticated `tools/call` must return a parsed Bearer challenge with exact resource metadata, error, description, scope, and matching MCP-body `_meta` mirror.
- A token request without a resource must fail with `invalid_target` and `no-store`; no valid code, client secret, token, login, tool execution, or private record is used.
- Redirects are rejected, non-loopback origins require HTTPS, response reads remain timed and bounded, and only exact JSON media types are accepted.

## Verification

- Focused smoke suite: 16 tests passed.
- Combined root Node suite: 181/181 passed with explicit exit 0.
- Live `./run.sh mcp-smoke` against the public private-beta origin: passed.
- Local Bash and Bash 3.2 syntax: passed.
- Application build, GitHub CI, Playwright, and Semgrep: passed.
- Three Codex review rounds produced concrete findings that were fixed; the fourth review could not start because the review quota was exhausted.
- Fallow remained advisory and reported static import-graph, complexity, and duplication findings.

## Boundary

PR308 changes operational verification only. It does not add tools or user-data fields, issue real tokens, call providers or models, write data, add refresh tokens, change billing or account-link lifecycle, widen private-beta eligibility, or authorize public launch.

PR309 remains `NOT APPROVED`. Its planning candidate is the existing safe `application_package` summary, subject to an exact post-PR308 file allowlist and separately approved high-risk Change Contract.
