---
title: "PR311 run.sh Doctor Regression Closure Checkpoint"
category: source
tags: [run-sh, doctor, mcp, portability, checkpoint]
created: 2026-07-13
updated: 2026-07-13
status: current
type: checkpoint
related: [[product/chatgpt-app-sdk-roadmap]], [[howto/chatgpt-mcp-private-beta-tunnel-connector]]
---

# PR311 run.sh Doctor Regression Closure Checkpoint

## Merged result

Application PR311 merged into `application-os-foundation` as `c61c9945e33f9208f4e3cb28dfd9e48d6fcfae50`. Its final reviewed head was `a077aa9da278ca25b975af61b3d5023289c7ae42`.

The change keeps `./run.sh doctor local-fast` and `./run.sh doctor mcp-private-beta` aligned with startup conditions that would otherwise fail immediately. It rejects parser, Convex, and Vite port collisions; requires Vite to keep the validated port; rejects remote Docker daemons that cannot use local mounts; verifies Docker Desktop integration for WSL2 MCP tunnels; and rejects incompatible Bash special-variable assignments in dotenv files.

## Verification

- Focused `run-sh-doctor` regression tests passed locally and in GitHub CI.
- macOS Bash 3.2 syntax and application build passed.
- Live `doctor local-fast` and `doctor mcp-private-beta` both passed value-silently; each reported only the expected warning for the already-running tracked Vite port.
- GitHub JavaScript tests, Playwright, Semgrep, and the dedicated doctor job passed.
- Codex Review found no major issue on the exact final head.

## Boundary

PR311 changes local startup diagnostics and CI coverage only. It does not change cover-letter generation or evaluation, MCP tools or schemas, authenticated data access, OAuth, secrets, provider calls, writes, account linking, billing, or public-launch eligibility.
