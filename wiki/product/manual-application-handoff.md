---
title: "Manual Application Handoff"
category: product
tags: [manual-handoff, applications, ats, audit, privacy, safety]
created: 2026-06-23
updated: 2026-06-23
status: current
valid_from: 2026-06-19
type: feature
sources: [2026-06-23-twoweeks-mcp-chatgpt-app-sdk-roadmap-checkpoint, 2026-06-19-pr80b-safe-application-handoff-while-ats-access-pending]
related: [[product/chatgpt-app-sdk-roadmap]], [[product/job-library]], [[product/job-match-review]]
---

# Manual Application Handoff

Manual application handoff is now a current boundary on the ChatGPT/App SDK track: Twoweeks prepares a confirmed package, and the user completes the external application manually while live submit/apply remains blocked.

## Current state

PR80B is represented as the safe manual-handoff path. The code path exists and is covered by `my-app/convex/__tests__/manualApplicationHandoff.test.ts`; this page should not be read as saying PR80B still needs initial implementation.

The checkpoint says PR80B is merged through artifact delivery, but live submit/apply and approved answer copy remain blocked.

The feature must not claim that Twoweeks submitted an application. `provider_verified_submitted` remains unreachable, and `user_reported_submitted` is the highest externally reported state.

This page is part of the MCP / ChatGPT App SDK track. It is not part of the cover-letter generation quality track.

## Details

Twoweeks owns:

- approved package preparation
- final handoff preview
- exact human confirmation
- immutable manifest and digest
- copy/download/open-destination controls
- destination-domain display
- redacted audit events
- truthful outcome labels

The user owns:

- logging into the employer or job platform
- navigating the external form
- pasting or uploading approved material
- solving CAPTCHA or MFA
- clicking the final submit button
- reporting whether submission occurred

PR80B forbids ATS transport, OAuth/API keys, provider adapters, scraping, DOM inspection, autofill, automated clicks, browser session access, CAPTCHA/MFA handling, bulk apply, background submission, and multi-provider frameworks.

Every handoff manifest must be approved-only, digest-bound, minimal, and labeled `manual_handoff_only`. Any material package change invalidates confirmation and requires a new preview.

Outcome evidence must stay explicit:

| Evidence | Meaning | PR80B |
| --- | --- | --- |
| `twoweeks_prepared` | Twoweeks prepared and froze the package | allowed |
| `user_interaction_observed` | Twoweeks observed local copy/download/open action | allowed |
| `user_reported` | User reported what happened externally | allowed |
| `provider_receipt_verified` | Official provider receipt was verified | forbidden |

Audit events must contain safe references, timestamps, digests, categories, and redacted metadata only. They must not contain answer text, document text, sensitive values, URL query strings, tokens, credentials, or file bytes.

## Operational guardrails

These are invariants to preserve, not proof that PR80B is unimplemented:

- [x] PR80B manual handoff runtime exists in `my-app/convex/manualApplicationHandoff.ts`.
- [x] PR80B helpers and validators exist in `my-app/convex/lib/manualApplicationHandoff.ts`.
- [x] PR80B UI surface exists in `my-app/src/components/jobs/ManualApplicationHandoffPanel.tsx`.
- [x] PR80B targeted tests exist in `my-app/convex/__tests__/manualApplicationHandoff.test.ts`.
- [ ] Keep live submit/apply blocked.
- [ ] Keep `provider_verified_submitted` unreachable.
- [ ] Keep approved-answer copy blocked until the Apps SDK roadmap explicitly opens it.
- [ ] Preserve approved-only, digest-bound, minimal package delivery semantics.
- [ ] Preserve confirmation invalidation when material package content changes.
- [ ] Keep audit events redacted and digest/reference based.
- [ ] Keep all ATS transport, OAuth/API keys, scraping, autofill, automated clicks, CAPTCHA/MFA handling, bulk apply, background submission, and provider frameworks out of scope.
- [ ] Feed any launch or production decision back into [[product/chatgpt-app-sdk-roadmap]], not the cover-letter quality roadmap.

## Sources

- [[sources/2026-06-23-twoweeks-mcp-chatgpt-app-sdk-roadmap-checkpoint]]
- [[sources/2026-06-19-pr80b-safe-application-handoff-while-ats-access-pending]]

## Related

- [[product/chatgpt-app-sdk-roadmap]]
- [[product/job-library]]
- [[product/job-match-review]]
