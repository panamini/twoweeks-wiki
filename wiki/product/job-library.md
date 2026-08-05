	---
title: "Job Library"
category: product
tags: [jobs, library, extension, documents, retention]
created: 2026-04-27
updated: 2026-08-05
status: current
version: v1
sources: [2026-04-27-job-library-prd]
related: [[product/job-match-review]], [[product/product-roadmap]], [[product/kpis]], [[entities/twoweeks]]
---

# Job Library

Job Library is the canonical product surface for saved jobs: scraped or pasted opportunities that can be reopened, reviewed, and used to generate linked resumes and cover letters.

## Current state

The desired loop is:

`save job -> understand job -> generate document -> keep everything linked`

The merged Jobs flow now completes the core loop for a ready Job Brief with an attached canonical CV: review server-authoritative tailoring recommendations, accept or reject pending items, materialize a provenance-linked reviewed CV variant, and continue to the existing Proposal surface. A complete-source-CV pass-through remains available without creating a derived variant. Unavailable or stale Job/CV state fails closed with a recoverable UI state.

Post-merge local authenticated smoke on `origin/main@3ef0bbdb` passed on desktop and 640px mobile with zero runtime errors and zero horizontal overflow. This is a private-beta candidate checkpoint, not public-launch proof: deployed identity, two-account sign-out isolation, parser upload, and account-deletion/cache/late-write safety remain open. See [[sources/2026-08-05-neyssan-post-merge-jobs-smoke-checkpoint]].

The Jobs surface should feel like an inbox of opportunities, not a heavy recruiter CRM. Jobs become first-class objects without adding notes, activity timelines, batch apply queues, or complex status systems in V1.

## V1 scope

- saved `Job` object
- Job Library page
- extension save-to-library flow
- Job Brief view with editable extracted context
- handoff from an opened job to cover-letter generation or resume tailoring
- linked generated documents on the job record

### Deferred scalability work

Jobs still use bounded local loading/search/filtering and capped proposal aggregates. Pagination, server-owned search/filter/sort, legacy-link reconciliation, and exact aggregate counts are deferred; they are not part of the delivered tailoring-to-Proposal beta slice.

## Job Brief

The job detail view should expose raw job text, source URL, title, company, location, extracted keywords, responsibilities, tone cues, contacts, and linked documents. Extracted fields remain editable; the product must not present parsing as irreversible certainty.

## Metrics

- jobs imported per user
- job saved rate
- job to first document time
- cover-letter generation from saved job
- linked documents per job
- duplicate / retarget usage

## Sources

- [[sources/2026-04-27-job-library-prd]]

## Related

- [[product/job-match-review]]
- [[product/product-roadmap]]
- [[product/kpis]]
