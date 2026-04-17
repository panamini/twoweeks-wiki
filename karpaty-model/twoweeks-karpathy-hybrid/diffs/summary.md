# Diff Summary

## CLAUDE.md
- Added a **Behavioral execution overlay** section.
- Added explicit preflight fields: Goal, Assumptions, Smallest safe change, Verification.
- Added mode-specific verification contracts.
- Preserved the original category router, frontmatter contract, retrieval order, and maintenance rules.

## skills/ingest-wiki/SKILL.md
- Added mandatory preflight before non-trivial writes.
- Added behavior constraints against overcomplication and drive-by cleanup.
- Added mode-specific verification for ingest, direct-update, lint, and save-output.
- Kept the original mode names for compatibility.

## Score summary
- twoweeks baseline: 62.4
- karpathy baseline: 76.4
- hybrid target: 100.0
