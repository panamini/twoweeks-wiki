---
title: "PR307 run.sh Collaborator Portability Checkpoint"
category: source
tags: [run-sh, mcp, docker, portability, checkpoint]
created: 2026-07-12
updated: 2026-07-12
status: current
type: checkpoint
related: [[product/chatgpt-app-sdk-roadmap]], [[howto/chatgpt-mcp-private-beta-tunnel-connector]], [[howto/local-parser-operations]]
---

# PR307 run.sh Collaborator Portability Checkpoint

## Merged result

Application PR307 merged into `application-os-foundation` as `736c6193966006e91a7bbbad5ff4b60898dd45fb`. Its final reviewed head was `982ae1405899ed5fb7b76ada1cf2bb1236436a58`.

`./run.sh doctor [local-fast|mcp-private-beta]` is now the read-only collaborator preflight. It checks the selected startup path without sourcing dotenv files, retrieving Infisical secrets, printing configured values, creating runtime state, or starting and stopping services.

## Problems retained as durable knowledge

- Doctor and startup must use the same winning dotenv assignment, target-specific ports, sourced `HOME`, local Convex state, Docker image/runtime, and filesystem traversal rules.
- Docker CLI control variables in sourced env files can make doctor and startup target different daemons, contexts, TLS/config/platform/build/proxy behavior. The preflight rejects the documented controls, including lowercase Go proxy aliases.
- Root MCP `.env.local` and tunnel credential symlinks are rejected because startup checks link metadata for the required restrictive modes.
- Vite stays bound to `127.0.0.1`. Native Linux Docker Engine runs the MCP cloudflared container with host networking and targets loopback; Docker Desktop and WSL2 retain `host.docker.internal`.
- `my-app/.env.local` remains Vite-owned and must not be sourced globally by `run.sh`.

## Verification

- Doctor regression suite: 165 tests passed.
- macOS Bash syntax: passed.
- Linux Bash 3.2 container syntax: passed.
- Application build: passed with inherited warnings only.
- Live `doctor local-fast` and `doctor mcp-private-beta`: passed with only expected tracked UI-port warnings.
- GitHub CI and Playwright checks: passed.
- Independent context-separated review: clear after the lowercase proxy alias finding was fixed.
- Fallow remained advisory and reported inherited dependency/import-graph findings.

## Boundary

PR307 changes startup diagnostics and portability only. It does not add MCP tools, widen OAuth clients or redirects, expose user data, call providers or models, add write actions or refresh tokens, mutate shared data, or authorize public launch.

