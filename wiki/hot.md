---
title: "Hot Cache - twoweeks"
category: overview
status: current
created: 2026-05-02
updated: 2026-09-30
---

# Hot Cache

This page is the active-memory cache for LLM retrieval. It is overwrite-only and non-canonical. Use it to choose pages, then trust durable pages.

## Current Focus

twoweeks centers on CV ingestion/parsing, canonical saved profile/CV data, and
personalized resumes, cover letters, and proposals. Keep product behavior,
provider qualification, and commercial launch evidence distinct.

## Key Active Facts

- **Billing activation (2026-09-24)**: `BILLING_LAUNCH_MODE=enforced` in
  Convex Production and Infisical EU `prod /twoweeks`; readiness is 23/23,
  `ready=true`, `trialReady=true`. Read
  [[product/billing-launch-readiness]].
- **Billing décisions (2026-09-29)**: prix 7,90 € TTC (Price `tax_behavior=inclusive`
  `price_1UL3EUFkKSo5QGwIdGDjp4H2`); webhook compare `amount_subtotal` (incident TVA,
  PR #531); essais plafonnés à 50, e-mails jetables refusés; plafond d’édition
  32 000 octets (PR #534). Détails : [[product/billing-launch-readiness]].
- **Export documents (2026-09-30)** : le navigateur passe par le relais Convex
  authentifié `/document-export/*` (jamais le parser en direct) ; Access laisse
  passer la clé de service « parser » via une politique Service Auth ; le worker
  Lightsail a `DOCUMENT_EXPORT_FRONTEND_URL=https://twoweeks.ai`. Réglages et
  diagnostic : [[tech/export-pipeline]].
- The 2026-09-16 billing audit and qualification plan are preserved as
  historical archives only: [[archive/outputs/2026-09-16-billing-launch-current-state]]
  and [[archive/tasks/2026-09-16-billing-launch-qualification]]. Do not use
  them as current production truth; the 2026-09-24 readiness page supersedes
  them.
- Authenticated billing smoke succeeded: trial claim showed 2 letters and 4
  optimizations; live Checkout opened for €7.90. No paid purchase was submitted;
  a user-completed paid purchase is the remaining user-owned proof.
- Live offer is `twoweeks_letters_25_optimizations_50_v1`: €7.90 one-time.
  Enabled webhook received the no-charge expired-session event; no session ID
  is recorded.
- PR #481 merge `8513c35f` is deployed to Cloudflare Pages and Convex.
  Immutable parser image is healthy behind cloudflared with no public app
  ports. No code was added after merge during activation.
- Stable endpoint: `https://mcp.twoweeks.ai/mcp`; MCP proof remains
  operational evidence, not commercial value proof.
- Product truth is `twoweeks`; CVForge and ProposalForge are internal names.
- Persistent wiki mutations require `wiki/index.md`, `wiki/log.md`, and
  `wiki/hot.md`.

## Canonical Pages To Read

- Billing activation: [[product/billing-launch-readiness]], [[product/product-roadmap]]
- Billing history: [[archive/outputs/2026-09-16-billing-launch-current-state]], [[archive/tasks/2026-09-16-billing-launch-qualification]]
- MCP commercial roadmap: [[product/chatgpt-app-sdk-roadmap]], [[howto/chatgpt-mcp-private-beta-tunnel-connector]]
- Product/parser/export routing: [[overview]], [[concepts/cv-parsing-pipeline]], [[tech/export-pipeline]]
- Jobs/Mistral/UI checkpoint: [[sources/2026-08-31-neyssan-jobs-mistral-ui-merge-checkpoint]], [[product/job-library]]
- Cloud region / parser hosting: [[strategy/us-first-cloud-region]], [[tech/local-vs-remote-parser-architecture]]
- Wiki operations: [[meta/llm-wiki-pattern]], [[meta/temporal-management]]
