---
title: "CV ATS Audit Heuristic (V1)"
category: tech
status: current
created: 2026-05-11
updated: 2026-05-11
tags: [ats, resume, scoring, parser, quality]
related: [[design/ats-safety]], [[concepts/cv-parsing-pipeline]], [[tech/import-ocr-pipeline]]
---

# CV ATS Audit Heuristic (V1)

Implementation note for the in-app CV health scoring pass that computes a non-ATS-parser compatibility score from trusted/canonical data.

## Current state

V1 is implemented and file-scoped in `my-app/src/lib/ats-audit/`:

- `types.ts`
- `rubric.ts`
- `evaluateCvAtsAudit.ts`
- `__tests__/evaluateCvAtsAudit.test.ts`

It is wired as a heuristic evaluator, not as a guarantee of real ATS parser compatibility.

## Details

- Inputs:
  - `cv: CvDocument`
  - `pageCount?: number`
  - `importIssueCount?: number`
- Canonical model preference:
  - Build `AuthoritativeResumeExportModel` from `readAuthoritativeResumeFromCv(cv)` and `hasTrustedAuthoritativeResume`.
  - If trusted export is missing, fallback is `cv.sections` to avoid false positives on profile/contact/experience/education/skills.
- Penalties and blockers:
  - `missing-cv` is a blocker.
  - `unresolved-import-review` is a blocker when `importIssueCount > 0`.
  - `missing-trusted-export-model` is **not** a blocker; it lowers parsing score and adds a high-priority issue.
- Category model:
  - `parsing`, `layout`, `typography`, `sections`, `keywords`, `content`.
  - `keywords` currently stays conservative/neutral unless explicit job-text logic is added.
- Weights:
  - parsing 20, layout 15, typography 5, sections 20, keywords 10, content 30.
- Verdict thresholds:
  - `score >= 90` => `excellent`
  - `score >= 75` => `good`
  - otherwise => `needs_review`
  - any blocker => `blocked`
- Layout signal:
  - `pageCount > 1` creates a warning.
  - `pageCount > 2` creates a stronger warning.
- Section scoring is based on visible, named, and non-empty content signals (section presence/naming, narrative quality, experience/education completeness, skills depth), not just export trust alone.

## Sources

- `my-app/src/lib/ats-audit/evaluateCvAtsAudit.ts`
- `my-app/src/lib/ats-audit/rubric.ts`
- `my-app/src/lib/ats-audit/__tests__/evaluateCvAtsAudit.test.ts`

## Related

- [[design/ats-safety]]
- [[design/document-token-contract]]
- [[tech/import-ocr-pipeline]]
