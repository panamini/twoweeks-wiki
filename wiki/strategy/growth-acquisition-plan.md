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

- **Welcome offer cap: 50 in code, about 374 in production.** `LAUNCH_POLICY.provider.budgets.trialCampaignMicros` (45.90 USD) divided by `trialMicros` (0.918 USD) in `my-app/convex/lib/billingPolicy.ts` gives 50, but the production `billingV2Campaigns` row was created on 2026-09-24 with the constant of that day (343.62 USD) and the code only inserts the row when it is missing, never updates it. Verified read-only on 2026-10-17: cap 343 620 000 micros, 9 648 000 reserved, 8 trials claimed, about 363 more authorizable. Changing the constant alone changes nothing in production; an operator mutation patching the row (proposed: 2 000 trials = 1 836 000 000 micros, reviewed after 3 months) needs the founder's agreement.
- **Price is EUR 7.90 for a US audience.** USD 8.90 implemented in PR #675 (`claude/usd-launch-price`): same offer version and allowances, `STRIPE_LAUNCH_PRICE_ID_USD` optional, English UI defaults to USD with an EUR/USD switch, EN pages show $8.90. **In production since 2026-10-18**: live Price `price_1URs6AFkKSo5QGwIFbnkx9oc` (8.90 USD, one-time, tax-inclusive), `STRIPE_LAUNCH_PRICE_ID_USD` on Convex prod and Infisical `prod /twoweeks`, PR #675 squash-merged (`91efe598e`), backend deployed; `getLaunchMode --prod` lists `eur` and `usd`, readiness check `stripe_price_usd` ok, live Checkout opened from an English account at 8.90 USD without paying. Rollback: remove the variable.
- Measurement: Google Search Console already holds the domain property `sc-domain:twoweeks.ai` (verified; sitemap submitted 2026-10-11, read 2026-10-14, 122 URLs, 110 pages indexed, 21 not indexed, 0 clicks over the last six weeks). Umami Cloud Hobby **live since 2026-10-18**: site `twoweeks` (public id `d6bc48fa-1be8-4d7e-9ce2-26568fd7e1cb`), PR #676 squash-merged (`14a1e21cc`), tag on every public page, landing dialog corrected, privacy page has an audience-measurement section. US performance on 2026-10-18 (28 days): 449 impressions, 0 clicks, position 73.3; six new guides indexed, manual indexing requests capped by Google's daily quota. Bing Webmaster declined.

Channel priority for US candidates (organic first, paid only once activation ≥ 25 %): ChatGPT plugin directory, SEO on the EN pages, Reddit help threads, TikTok/Shorts, Product Hunt + Show HN as one-off launches, LinkedIn for prescribers. Google Search ads are not viable at a 7.90 one-time price with related-keyword CPCs around 2.5 USD; revisit after a higher-value pack exists.

Founder decisions of 2026-10-17 (evening): USD price approved (scope in `neyssan/docs/plans/2026-10-17-usd-launch-price.md`); Chrome Web Store listing confirmed published; ChatGPT app under OpenAI review since about 2026-10-10; first-30-users strategy approved; **all publishing (Reddit, LinkedIn, TikTok, newsletter) is delegated to the assistant**, the founder only ticks what goes out.

Operating model: a daily approval board (checkbox artifact) feeds a scheduled cloud session that publishes through one integration, Postiz (open source, API, 30 platforms), self-hosted on the existing Lightsail or cloud; Brevo for newsletter and activation e-mails; morning report from Search Console, `acquisition:report` and Stripe. Cloud access, least privilege (corrected 2026-10-17 evening): network secrets inject one HTTP header on requests to named hosts only. Needed now: a Stripe **restricted** read key (host `api.stripe.com`, header `Authorization`, prefix `Bearer`) and a read-only growth-report token for a small Convex HTTP endpoint (to build; replaces a production deploy key, which can deploy arbitrary code). Infisical is not needed in the cloud routine, and its Universal Auth login exchange cannot be done by header injection. Never put `STRIPE_SECRET_KEY` in the cloud. Later: Postiz, Brevo, Umami keys, one header each. Browser-bound checks (Reddit account, OpenAI review status, the paper-boat video) need the founder's machine. No fabricated testimonials, no paid votes, no third-party pixels; no unapproved post.

## Verified state on 2026-10-17 (local session, read-only production)

- Production (`npx convex run … --prod`, tables read-only): launch mode enabled; 11 distinct accounts (30 profiles), 8 trials claimed, 1 Stripe purchase (2026-09-28, EUR 7.90), 7 billed letters completed (11 attempts, 4 failed), 36 `proposals` documents created since launch; `acquisition:report` only covers 3 attributed signups (2 direct, 1 Apple), 0 activated. Figures include founder test accounts. Ledger: `neyssan/docs/plans/growth/ledger.md`.
- OpenAI plugin directory: "TwoWeeks" 1.0.0 (metadata 1.1.0) **In review**, not published; MCP server `twoweeks-public-v2` configured, domain verified, but the MCPs tab shows "Needs attention: no scan has finished since this connection", 10 tools "Not published", last checked 10 days ago. No reviewer message, no submission date shown. A second draft "twoweeks" 1.0.6 is not submitted.
- Chrome Web Store (public listing, the developer dashboard cannot be read by browser tooling): "Twoweeks — Job Capture" 1.0.0, updated 2026-10-12, 3 users, 0 reviews. The listing still shows the former tutamail contact; `main` moved to support@twoweeks.ai.
- Reddit: not verifiable from the assistant's browser (domain blocked); founder to check age, karma and subreddit rules before any post.
- Video `paper-boat.mp4` (30 s, 1080p60): keep, rework the ending (replace the house with a desk in the grass, the opposite of "NO REPLY"); use on the landing (muted autoplay), as a 12–15 s vertical cut for TikTok/Shorts, and as the first Product Hunt gallery item.
- Cloud-session access (Infisical machine identity, Convex prod deploy key, Stripe restricted key): nothing created yet; each creation waits for the founder's explicit confirmation and an Infisical login.

## Founder decisions of 2026-10-17 (night)

- OpenAI MCP rescan returned "No findings"; review continues on OpenAI's side, nothing to do.
- No Stripe key, no Convex deploy key, no Infisical in the cloud; the founder wants zero key handling. Purchases and credits are already in Convex.
- No Reddit, manual or automated: automated posting from a personal account breaks Reddit rules and risks a ban.
- New US SEO pages are blocked: `cover-letter-content.test.mjs` requires example letters to come from the real Twoweeks pipeline, which needs an AI provider access.
- Local sessions are out of credit; routines run weekly (Monday) plus on demand, not daily.

## Prepared for the local run of 2026-10-18

Files in `neyssan/docs/plans/growth/`: content bank (English posts, scripts, threads), launch kits (Product Hunt, directories, Chrome Web Store text), credit-saving runbook `local-session-prompt-2.md`. Four US SEO guide drafts on branch `claude/seo-us-guides-batch-4` (unpublished, no PR). Corrections: FAQ/Article/Breadcrumb structured data already exist in the marketing layout; Show HN excludes sign-up pages, so it needs a no-account demo. Models: Sonnet is enough for content and docs, Opus for the USD price rollout, Opus or Fable for billing-touching work such as referrals.

## Name story and sharper target (2026-10-18)

"Two weeks" is the standard notice period: a job ends, by choice or layoff, and the app does the groundwork to find the next one in that window. Target sharpened to people whose job just ended or is ending. Content must follow [[design/brand-voice]] (Corporate Noir, staccato, no questions, no AI mention). Content bank rewritten around a 14-step series "Your two weeks"; four layoff-search guide drafts on branch `claude/seo-us-guides-batch-5`.

## SEO guides published (2026-10-17)

Six English-only US guides are live (neyssan PRs #677, #678, #679): how to write a cover letter, how to tailor a resume, and four layoff-search guides (job search, resume wording, cover letter, explaining being fired). Two published pages (`cover-letter-length`, `how-to-start-a-cover-letter`) gained format and greeting guidance in EN, FR and ES. The English resources hub now lists all six. Constraint: the 25 cover-letter pages are tested as an isolated family, so the examples hub cannot link outside it until those test fixtures are relaxed. FR and ES versions of the resources hub lag the EN additions by design (US target). Codex review was unavailable on #678 and #679 (usage limit).

## Session of 2026-10-18 (local, founder approvals at each production step)

- Done and verified: Umami counter live (PR #676), USD price live end to end (PR #675, Price, variable, deploy, Checkout smoke), Search Console US reading in the ledger, scheduler comparison (Buffer free recommended for the first 30 days; Publer excludes X on free; Postiz Cloud has no free tier).
- Scheduler decided and running (2026-10-18 evening): **Buffer free plan**, three channels connected (LinkedIn page `twoweeks.ai`, X `@twoweeksai`, TikTok `@solar.skytime`). Profiles redone from the founder's Chrome session: X renamed `Twoweeks` / `@twoweeksai` with bio, link, avatar and banner; TikTok bio and avatar updated (name and handle locked by TikTok until 2026-10-25 and 2026-11-17). Week 1 queued: LinkedIn L1–L5 Monday to Friday 09:00 New York, X thread X1 Tuesday 09:30 New York, UTM `d30-01…05`; TikTok waits for the videos. Details in `neyssan/docs/plans/growth/buffer-week-1.md`.
- Waiting for the founder: deletion of the unused Infisical machine identity `claude-growth` (created before the "no cloud keys" decision was read); seven indexing requests to resend another day; manual deletion of the old posts on X (18) and TikTok (4).
- Not done: Reddit (excluded by decision); Convex deploy key and Stripe restricted key (not created, per the same decision; the Convex key creation was also refused by the assistant's permission classifier).

## Sources

- `neyssan` repository: `docs/plans/2026-10-17-zero-to-hero-acquisition.md`, `my-app/convex/lib/billingPolicy.ts`, `my-app/marketing/`, commits #654 (acquisition), #666–#670 (SEO), #671–#673 (extension), #648 (ChatGPT).

## Related

- [[strategy/us-first-cloud-region]]
- [[product/billing-launch-readiness]]
- [[product/kpis]]
- [[product/chatgpt-app-sdk-roadmap]]
