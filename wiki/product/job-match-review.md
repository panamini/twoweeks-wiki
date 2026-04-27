---
title: "Job Match Review"
category: product
tags: [jobs, match, scoring, dogfood, beta-review, privacy]
created: 2026-04-27
updated: 2026-04-27
status: current
version: v1
sources: [2026-04-24-pass-3b-structured-scoring-decisions, 2026-04-27-match-review-v1-dogfood-tool, 2026-04-27-job-match-validation-contract, 2026-04-27-dev-only-advisory-beta-access]
related: [[product/job-library]], [[product/kpis]], [[product/product-roadmap]]
---

# Job Match Review

Job Match Review is a user-facing opportunity indicator for saved jobs. It answers whether a scraped job is worth the user's attention, not whether an employer should hire the user.

## Current state

Match Review V1 is dogfood-ready. The production score remains authoritative; structured match output stays advisory / shadow-only until dogfood review proves that it is useful and safe.

The core product question is:

`Is this scraped job worth this user's attention?`

Not:

`Should this employer hire this candidate?`

## Match contract

The visible output should stay compact:

- tier: `strong`, `partial`, `weak`, or `unknown`
- verdict: `strong_lead`, `possible_lead`, `probably_skip`, or `not_enough_signal`
- score: 0-100
- one-liner
- up to 3 reasons
- up to 2 watch-outs
- next step: apply, apply if true, skip, or review manually

The UI must avoid contradiction: positive evidence cannot sit beside a `probably_skip` verdict unless a real hard gate explains the downgrade.

## Validation contract

Internal approval depends on:

- false-zero rate: 0 on obvious same-family positive fixtures
- contradiction rate: 0 critical contradictions
- credential safety: no hallucinated required credentials
- preferred credentials: watch-out, not blocker
- negative precision: unrelated jobs stay weak / skip
- positive recall: obvious semantic matches reach at least partial
- copy safety: no raw CV, phone, email, UUID, source blob, or debug phrasing
- time to decision: user understands relevance, reason, and next step in under 5 seconds

## Dogfood loop

The dogfood loop exports safe visible review records for recent saved jobs, labels them manually, summarizes repeated failure types, and patches only repeated product patterns.

Important failure types include `false_zero`, `dangerous_overmatch`, `credential_hallucination`, `preferred_as_blocker`, `generic_fragment_leak`, `raw_evidence_leak`, `verdict_reason_contradiction`, `bad_next_step`, and `unclear_copy`.

## Dev advisory access

Local/dev can expose `Structured preview` to everyone when advisory mode is explicitly enabled. Production/non-dev must keep the allowlist boundary and require shadow mode plus an allowlisted viewer. Wildcard viewer access must be ignored or rejected outside dev/local.

Required copy remains:

- `Current match`
- `Structured preview`
- `Experimental match read. Production score remains authoritative.`

Forbidden framing remains: `AI score`, `Recommended score`, `Better score`, `New score`.

## Sources

- [[sources/2026-04-24-pass-3b-structured-scoring-decisions]]
- [[sources/2026-04-27-match-review-v1-dogfood-tool]]
- [[sources/2026-04-27-job-match-validation-contract]]
- [[sources/2026-04-27-dev-only-advisory-beta-access]]

## Related

- [[product/job-library]]
- [[product/kpis]]

