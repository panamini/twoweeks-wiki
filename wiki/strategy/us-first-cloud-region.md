---
title: "US-First Cloud Region"
category: strategy
tags: [cloud, convex, parser, us-first, data-residency]
created: 2026-07-27
updated: 2026-07-27
status: current
valid_from: 2026-07-27
sources: [[sources/2026-07-27-us-first-cloud-region]]
related: [[tech/local-vs-remote-parser-architecture]], [[strategy/language-localization]], [[howto/local-parser-operations]]
---

# US-First Cloud Region

Twoweeks is natively English-speaking and US-first. The first future Convex Cloud deployment defaults to **US East (N. Virginia)**, and the first production parser must run in US East. This is a region direction, not a parser-provider selection or a cloud-provisioning authorization.

## Current decision

- The frontend may remain globally served on Cloudflare Pages.
- `./run.sh local-fast` remains local development with local Convex and local parser; it does not require a cloud-region choice.
- Clerk is already US-hosted and remains unchanged for now.
- `run.sh` is local/dev-only and never the production entrypoint.
- Europe is phase 2. A separate EU parser and EU Convex deployment/project are considered only when contractual data residency justifies them.
- Frontend hosting, parser hosting, Convex region, and company legal/tax domicile are separate decisions.

## Provider gate

No provider is selected before a benchmark. The current candidates are role-based: Hetzner Ashburn is cost-first, Railway US-East is operations-first, and Cloud Run is a growth option. The gate must use raw measurements for parser latency, throughput, cold start, operational burden, observability, data handling, cost, and exit path; avoid pseudo-precise scoring.

## Data-region rule

Convex documents that all infrastructure powering a deployment is hosted in its selected region. An existing deployment's region cannot be changed in place; a move requires a new deployment or project and export/import. The production data map must separately cover Convex data, parser processing, logs, backups, and attached storage before launch.

## Reversibility and open measurements

The decision remains reversible before provisioning because no cloud region or parser provider has been selected here. Before production approval, require a frozen US data map, benchmark evidence, measured parser SLOs, confirmed region, backup/export validation, migration/rollback rehearsal, and an operations runbook. Local-fast runtime measurements, Convex Cloud provisioning, provider benchmarks, production data-flow measurements, and export/import rehearsal remain unverified.

## Sources

- [Convex Regions](https://docs.convex.dev/production/regions)
- [Convex Local Deployments for Development](https://docs.convex.dev/cli/local-deployments)
- [[sources/2026-07-27-us-first-cloud-region]]

