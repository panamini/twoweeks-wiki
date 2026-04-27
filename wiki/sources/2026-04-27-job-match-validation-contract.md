---
title: "Job Match Validation Contract"
category: source
tags: [jobs, match-review, validation, kpi, benchmark]
created: 2026-04-27
updated: 2026-04-27
status: current
type: spec
related: [[product/job-match-review]], [[product/kpis]]
---

# Job Match Validation Contract

## Summary

Validation contract for approving the job match system as a user-facing opportunity reviewer rather than an ATS, recruiter, or hiring decision engine.

## Key points

- The system answers whether a job deserves the user's attention.
- Required visible model includes tier, verdict, score, one-liner, reasons, watch-outs, and next step.
- Same-family role overlap plus at least two positive scorable overlaps and no missing hard gate should floor to partial / possible lead.
- Credentials must distinguish required, preferred, and unknown; preferred credentials are watch-outs, not blockers.
- Generic fragments such as `valid`, `ability`, `preferred`, `more`, or `lift` must not become visible missing requirements.
- Approval metrics include false-zero rate, contradiction rate, credential safety, preferred-not-blocking, negative precision, positive recall, copy safety, and time to decision.

## Implications

Adds the KPI and benchmark bar for [[product/job-match-review]].

## Touched pages

- [[product/job-match-review]]
- [[product/kpis]]

