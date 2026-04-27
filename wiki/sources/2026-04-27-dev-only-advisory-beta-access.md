---
title: "Dev-only Advisory Beta Access"
category: source
tags: [jobs, structured-match, beta, dev, env]
created: 2026-04-27
updated: 2026-04-27
status: current
type: spec
related: [[product/job-match-review]]
---

# Dev-only Advisory Beta Access

## Summary

Implementation prompt for making structured match advisory preview visible to all users in local/dev when explicitly enabled, while keeping production/beta allowlist behavior safe.

## Key points

- Local/dev may show `Structured preview` to any user when advisory mode is on and either local/dev, wildcard viewers, or `STRUCTURED_MATCH_READ_ADVISORY_BETA_ALL=true` is present.
- Production/non-dev still requires advisory flag, shadow flag, and allowlisted viewer.
- Wildcard `*` must be rejected or ignored outside dev/local.
- Production score, tier, ranking, filtering, badges, CTA copy, extraction, model, prompt version, and scorer formula must not change.
- Copy must remain `Current match`, `Structured preview`, and `Experimental match read. Production score remains authoritative.`

## Implications

This is an implementation guardrail under [[product/job-match-review]], not a change to match authority.

## Touched pages

- [[product/job-match-review]]

