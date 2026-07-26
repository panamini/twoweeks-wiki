---
title: "US-First Cloud Region Decision"
category: source
status: current
created: 2026-07-27
updated: 2026-07-27
type: decision
related: [[strategy/us-first-cloud-region]], [[tech/local-vs-remote-parser-architecture]]
---

# US-First Cloud Region Decision

## Summary

The source decision fixes Twoweeks as natively English-speaking and US-first, with US East (N. Virginia) as the default for a future Convex Cloud deployment and for the first production parser. It leaves parser-provider selection open until benchmark evidence exists.

## Key points

- Cloudflare Pages may remain globally served; frontend distribution does not determine the Convex region.
- `./run.sh local-fast` remains local development with local Convex at the repo's loopback default; no cloud region is needed for local work.
- Hetzner Ashburn, Railway US-East, and Cloud Run remain candidate provider roles, not a selection.
- Europe is phase 2 and requires a demonstrated contractual data-residency reason before a separate EU parser or Convex deployment/project.
- A Convex region cannot be changed in place; migration requires a new deployment/project and export/import.

## Implications

The first production architecture should be US-coherent across Convex and parser processing, while the provider gate measures latency, throughput, cold start, operations, observability, data handling, cost, and exit path. Clerk remains US-hosted and unchanged for now. Company legal/tax domicile remains a separate decision.

## Touched pages

- `wiki/strategy/us-first-cloud-region.md`
- `wiki/index.md`
- `wiki/log.md`
- `wiki/hot.md`

## Source artifact

`/Users/pana/.codex/worktrees/08cf/neyssan-new/docs/decisions/2026-07-27-us-first-cloud-region.md`

## Official references

- [Convex Regions](https://docs.convex.dev/production/regions)
- [Convex Local Deployments for Development](https://docs.convex.dev/cli/local-deployments)

