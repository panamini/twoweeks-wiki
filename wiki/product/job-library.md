---
title: "Job Library"
category: product
tags: [jobs, library, extension, documents, retention]
created: 2026-04-27
updated: 2026-04-27
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

The Jobs surface should feel like an inbox of opportunities, not a heavy recruiter CRM. Jobs become first-class objects without adding notes, activity timelines, batch apply queues, or complex status systems in V1.

## V1 scope

- saved `Job` object
- Job Library page
- extension save-to-library flow
- Job Brief view with editable extracted context
- handoff from an opened job to cover-letter generation or resume tailoring
- linked generated documents on the job record

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

