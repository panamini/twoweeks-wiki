---
title: "PR80B - Safe Application Handoff While ATS Authorization Is Pending"
category: source
tags: [manual-handoff, ats, safety, audit, applications]
created: 2026-06-19
updated: 2026-06-19
status: current
type: implementation-plan
related: [[product/manual-application-handoff]], [[product/chatgpt-app-sdk-roadmap]]
---

# PR80B - Safe Application Handoff While ATS Authorization Is Pending

## Summary

PR80B defines a safe manual application handoff while Twoweeks waits for authorized ATS access: Twoweeks prepares an approved package, the user completes the external application manually, and any reported submission remains explicitly unverified by the provider.

## Key points

- PR80B is proposed and only becomes next after PR73-PR80A prerequisites are merged and verified.
- Twoweeks owns package preparation, final review, confirmation, immutable manifest, copy/download controls, destination-domain display, privacy-safe audit events, and truthful state labels.
- The user owns logging in, navigating the external form, pasting/uploading material, accepting provider consent text, solving CAPTCHA/MFA, submitting externally, and reporting the outcome.
- The PR explicitly forbids ATS transport, OAuth/API keys, provider adapters, browser automation, scraping, autofill, automated clicking, CAPTCHA/MFA handling, background submission, bulk apply, and multi-provider frameworks.
- The handoff manifest is digest-bound, minimal, approved-only, and labeled `manual_handoff_only`.
- `provider_verified_submitted` is reserved for a future official integration and must be unreachable in PR80B.
- The highest completion state in PR80B is `user_reported_submitted`, with evidence level `user_reported`.
- Audit records must use safe references and exclude answer text, document text, sensitive values, URL query strings, tokens, credentials, and file bytes.

## Implications

- PR80B validates useful application delivery without live ATS credentials or external write access.
- Opening the destination, copying answers, or downloading files must never imply submission.
- Future live ATS work stays blocked until one provider supplies written authorization, credentials, a test tenant, and an authorized test posting.

## Touched pages

- [[product/manual-application-handoff]]
- [[product/chatgpt-app-sdk-roadmap]]
