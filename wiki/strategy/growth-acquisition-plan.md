---
title: "Growth and Acquisition Plan"
category: strategy
tags: [growth, acquisition, marketing, launch, seo, us-first]
created: 2026-10-17
updated: 2026-10-17
status: current
valid_from: 2026-10-17
related: [[strategy/us-first-cloud-region]], [[product/billing-launch-readiness]], [[product/kpis]], [[product/chatgpt-app-sdk-roadmap]]
---

# Growth and Acquisition Plan

Routing page for the commercial launch of twoweeks.ai: from zero users to paying customers. The full plan, calendar and weekly ledger live in the code repository (`neyssan`, `docs/plans/2026-10-17-zero-to-hero-acquisition.md` and `docs/plans/growth/ledger.md`); this page keeps the durable decisions and constraints.

## Current state

- Site live in EN/FR/ES with 117 published SEO pages, Stripe Checkout, Chrome extension 1.0.0 on the Web Store, ChatGPT app (MCP) open to every account, cookieless first-touch acquisition attribution (`acquisition:report`). Zero users as of 2026-10-17.
- Target market: United States job seekers first (founder decision 2026-10-17, consistent with [[strategy/us-first-cloud-region]]). FR and ES are secondary.
- Star metric: letters generated per week. Funnel: accounts created → activated (one letter) → buyers. Targets: 150 / 60 / 5 at month 1, 1 200 / 450 / 50 at month 3, 5 000 / 1 800 / 250 at month 6.

## Details

Constraints found in code on 2026-10-17 that gate every launch:

- **Welcome offer capped at 50 trials in total.** `LAUNCH_POLICY.provider.budgets.trialCampaignMicros` (45.90 USD) divided by `trialMicros` (0.918 USD) in `my-app/convex/lib/billingPolicy.ts`. After the 50th claim `trialReady` becomes false and the landing shows "subject to availability". Raising it is a production change requiring the founder's agreement.
- **Price is EUR 7.90 for a US audience.** The billing meter supports USD; a USD Stripe price and offer version are needed before paid US acquisition.
- Measurement: Google Search Console (to connect), Umami Cloud Hobby (cookieless, open source) chosen; Bing Webmaster declined. The landing's "no analytics" dialog and the privacy page must be updated in the same change as the counter script.

Channel priority for US candidates (organic first, paid only once activation ≥ 25 %): ChatGPT plugin directory, SEO on the EN pages, Reddit help threads, TikTok/Shorts, Product Hunt + Show HN as one-off launches, LinkedIn for prescribers. Google Search ads are not viable at a 7.90 one-time price with related-keyword CPCs around 2.5 USD; revisit after a higher-value pack exists.

Founder decisions of 2026-10-17 (evening): USD price approved (scope in `neyssan/docs/plans/2026-10-17-usd-launch-price.md`); Chrome Web Store listing confirmed published; ChatGPT app under OpenAI review since about 2026-10-10; first-30-users strategy approved; **all publishing (Reddit, LinkedIn, TikTok, newsletter) is delegated to the assistant**, the founder only ticks what goes out.

Operating model: a daily approval board (checkbox artifact) feeds a scheduled cloud session that publishes through one integration, Postiz (open source, API, 30 platforms), self-hosted on the existing Lightsail or cloud; Brevo for newsletter and activation e-mails; morning report from Search Console, `acquisition:report` and Stripe. Required cloud-environment secrets (names only): `CONVEX_DEPLOY_KEY` (prod), `INFISICAL_CLIENT_ID`/`INFISICAL_CLIENT_SECRET` (machine identity), `STRIPE_RESTRICTED_KEY`, `POSTIZ_API_KEY`, `BREVO_API_KEY`, `GOOGLE_SERVICE_ACCOUNT_JSON`, `UMAMI_API_KEY`. Browser-bound checks (Reddit account, OpenAI review status, the paper-boat video) need the founder's machine. No fabricated testimonials, no paid votes, no third-party pixels; no unapproved post.

## Sources

- `neyssan` repository: `docs/plans/2026-10-17-zero-to-hero-acquisition.md`, `my-app/convex/lib/billingPolicy.ts`, `my-app/marketing/`, commits #654 (acquisition), #666–#670 (SEO), #671–#673 (extension), #648 (ChatGPT).

## Related

- [[strategy/us-first-cloud-region]]
- [[product/billing-launch-readiness]]
- [[product/kpis]]
- [[product/chatgpt-app-sdk-roadmap]]
