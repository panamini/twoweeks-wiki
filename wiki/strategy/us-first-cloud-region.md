---
title: "US-First Cloud Region"
category: strategy
tags: [cloud, convex, parser, us-first, data-residency]
created: 2026-07-27
updated: 2026-08-14
status: current
valid_from: 2026-07-27
sources:
  - "[[sources/2026-07-27-us-first-cloud-region]]"
  - "[[sources/2026-08-14-neyssan-auth-production-transition-checkpoint]]"
related:
  - "[[tech/aws-production-industrialization]]"
  - "[[tech/local-vs-remote-parser-architecture]]"
  - "[[strategy/language-localization]]"
  - "[[howto/local-parser-operations]]"
---

# US-First Cloud Region

Twoweeks is natively English-speaking and US-first. Convex Cloud and the production parser default to **US East (N. Virginia)**. Lightsail a été retenu comme baseline du parser beta; ce choix ne préjuge pas de la plateforme de croissance, qui reste soumise aux mesures et aux gates de [[tech/aws-production-industrialization]].

## Current decision

- The frontend may remain globally served on Cloudflare Pages.
- The documented beta parser baseline is a stateless Lightsail host in `us-east-1`, exposed only through the approved Cloudflare tunnel path.
- `./run.sh local-fast` remains local development with local Convex and local parser; it does not require a cloud-region choice.
- Clerk is already US-hosted and remains unchanged for now.
- Environment note: the public Cloudflare Production build was still using a Clerk `pk_test` key for `accounts.dev` at the 2026-08-14 checkpoint; Clerk Production identity is a separate pre-launch gate, not a region decision.
- `run.sh` is local/dev-only and never the production entrypoint.
- Europe is phase 2. A separate EU parser and EU Convex deployment/project are considered only when contractual data residency justifies them.
- Frontend hosting, parser hosting, Convex region, and company legal/tax domicile are separate decisions.

## Long-term provider gate

Lightsail is selected for the controlled beta baseline. No growth platform is selected before a benchmark. The long-term gate must use raw measurements for parser latency, throughput, concurrency, cold start, operational burden, observability, data handling, cost, availability and exit path; avoid pseudo-precise scoring.

## Data-region rule

Convex documents that all infrastructure powering a deployment is hosted in its selected region. An existing deployment's region cannot be changed in place; a move requires a new deployment or project and export/import. The production data map must separately cover Convex data, parser processing, logs, backups, and attached storage before launch.

## Reversibility and open measurements

The growth-platform decision remains reversible because the parser beta is stateless and deployed from an immutable image. Before broader production approval, require a frozen US data map, benchmark evidence, measured parser SLOs, backup/export validation, migration/rollback rehearsal, and an operations runbook. Capacity measurements, provider benchmarks, production data-flow measurements, and Convex export/import rehearsal remain to be proven.

## Sources

- [Convex Regions](https://docs.convex.dev/production/regions)
- [Convex Local Deployments for Development](https://docs.convex.dev/cli/local-deployments)
- [[sources/2026-07-27-us-first-cloud-region]]
