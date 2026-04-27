---
title: "Match Review V1 Dogfood Tool"
category: source
tags: [jobs, match-review, dogfood, evaluation]
created: 2026-04-27
updated: 2026-04-27
status: current
type: runbook
related: [[product/job-match-review]]
---

# Match Review V1 Dogfood Tool

## Summary

Developer/LLM note for reviewing real saved jobs and validating whether Match Review V1 is useful in live dogfood.

## Key points

- The tool is an internal review loop, not a benchmark generator, matcher rewrite, ATS evaluator, or hiring-decision engine.
- Product question: whether the scraped job is worth the user's attention.
- The loop exports safe visible records, lets reviewers label coherence, summarizes repeated failure types, and patches only repeated patterns.
- Labels include `makes_sense`, `too_harsh`, `too_generous`, `wrong_reason`, `credential_wrong`, `unsafe_or_leaky`, and no-signal variants.
- Safety boundary: exported/labeled files must not contain raw CV body, resume text, raw job source blob, email, phone, UUID-like source IDs, or unsafe debug material.

## Implications

This source gives the operational dogfood procedure for [[product/job-match-review]].

## Touched pages

- [[product/job-match-review]]

