---
title: "Cover Letter Quality PR248 Merge Checkpoint"
category: source
tags: [cover-letter, quality, pr248, mistral-v2, no-cv, canary]
created: 2026-06-23
updated: 2026-06-23
status: current
type: analysis
related: [[tasks/2026-06-22-cover-letter-quality-production-roadmap]], [[sources/2026-06-23-cover-letter-quality-pr246-merge-checkpoint]]
---

# Cover Letter Quality PR248 Merge Checkpoint

## Summary

PR248 is merged into `application-os-foundation` by squash merge. The merge commit is verified locally in `neyssan-new`.

PR248 tightened the Mistral V2 no-CV candidate-history boundary and reported `READY_FOR_STAGED_INTERNAL_MISTRAL_V2_EXPANSION`.

## Key points

- PR: <https://github.com/panamini/neyssan/pull/248>
- Merge commit: `2fd7ebef142859fb089bf8e9d270bf6b5b590fa1`.
- Expected head SHA matched before merge: `fd478470525942caacbec12d01cdcb39d2688c22`.
- Merge method: squash merge.
- Merge message: `PR248: Tighten Mistral V2 no-CV candidate-history boundary`.
- Reported decision marker: `READY_FOR_STAGED_INTERNAL_MISTRAL_V2_EXPANSION`.
- Diff scope verified locally: two files only:
  - `my-app/convex/lib/proposals/premiumCoverLetter.ts`
  - `my-app/convex/lib/proposals/__tests__/premiumCoverLetter.test.ts`

## Implementation shape

- Replaced the single no-CV candidate-history regex with provider/language-aware candidate-history claim patterns.
- Added `hasNoCvHistoryClaim` and routed no-CV validation through it.
- Expanded no-CV validation to catch present-tense candidate operations in English and French.
- Kept conditional no-CV intent wording allowed when it stays employer/job-surface side.
- Kept quality repair disabled.
- Did not touch Qwen premium, GPT behavior, parser/CV ingest, UI, DB schema, MCP/App SDK, OAuth, billing, deployment, or production flags.

## Decision

The next step is not production and not quality repair.

Run post-merge verification from `2fd7ebef142859fb089bf8e9d270bf6b5b590fa1`. If clean, proceed to the staged internal Mistral V2 expansion/evidence gate.

## Touched pages

- [[tasks/2026-06-22-cover-letter-quality-production-roadmap]]
- [[sources/2026-06-23-cover-letter-quality-pr246-merge-checkpoint]]
