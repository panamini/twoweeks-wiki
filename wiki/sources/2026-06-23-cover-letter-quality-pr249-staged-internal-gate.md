---
title: "Cover Letter Quality PR249 Staged Internal Gate"
category: source
tags: [cover-letter, quality, pr249, mistral-v2, internal-staging, canary]
created: 2026-06-23
updated: 2026-06-23
status: current
type: analysis
related: [[tasks/2026-06-22-cover-letter-quality-production-roadmap]], [[sources/2026-06-23-cover-letter-quality-pr248-merge-checkpoint]], [[sources/2026-06-23-cover-letter-quality-pr246-merge-checkpoint]]
---

# Cover Letter Quality PR249 Staged Internal Gate

## Summary

PR249 is merged into `application-os-foundation` by squash merge. The post-merge staged internal Mistral V2 evidence gate completed cleanly from local base `application-os-foundation` at `d628bed79c0063d2c06c836015e87d313385bbd2`.

Decision recorded:

```text
COVER_LETTER_MISTRAL_V2_READY_FOR_INTERNAL_STAGING_ONLY
```

This is not a production approval. Production full GO remains separate. Quality repair remains OFF. Qwen remains legacy-only. GPT remains unchanged. MCP/App SDK work remains separate.

## Merge Facts

- PR: <https://github.com/panamini/neyssan/pull/249>
- Base branch: `application-os-foundation`
- Merge method: squash
- Merge SHA: `d628bed79c0063d2c06c836015e87d313385bbd2`
- Head SHA: `11f56d5e44b24db8b3a479cff0bee76c24974b05`
- GitHub CI before merge: `CI` success, `Playwright Tests` success
- Local post-merge base: `application-os-foundation` at `d628bed79c0063d2c06c836015e87d313385bbd2`
- Local app status after gate: clean except pre-existing untracked `docs/plans/2026-06-22-cover-letter-quality-production-roadmap.md`

## Verification

Local post-merge commands:

```bash
CI=1 npx vitest run convex/lib/proposals/__tests__/premiumCoverLetter.test.ts convex/lib/proposals/__tests__/proposalWriterPrompt.test.ts --reporter=dot
CI=1 npx vitest run convex/lib/proposals/__tests__ --reporter=dot
git diff --check
```

Results:

- Targeted proposal tests: 2 files passed, 282 tests passed.
- Full proposal tests: 20 files passed, 581 tests passed.
- `git diff --check`: clean.

## Internal No-DB Canary

Post-merge internal no-DB canary passed:

- MM-9 French no-CV.
- MM-10 French no-CV.
- ML-20 French no-CV.
- English no-CV medium/large.
- Mistral direct control.
- Mistral adjacent control.
- GPT control.
- Qwen legacy-only control.

Expanded staged internal gate:

- 23 cases total.
- 19 PASS.
- 4 SKIPPED only because no committed French CV-backed fixtures existed.
- 0 FAIL.
- PR246 forbidden extrapolation hits: none.
- PR248 no-CV leakage hits: none.
- Unsupported claim examples: none found.
- Quality repair: OFF / not used.
- Qwen: legacy-only, `enteringPremiumAttempt=false`.
- GPT: clean, no Mistral V2 prompt marker or adapter text.
- Production full GO: still separate.

## Decision

```text
STAGED_INTERNAL_MISTRAL_V2_READY
```

Record this operationally as:

```text
COVER_LETTER_MISTRAL_V2_READY_FOR_INTERNAL_STAGING_ONLY
```

Allowed next scope:

- Internal/staging-only Mistral V2 rollout readiness work.
- Continue keeping quality repair OFF.
- Continue keeping Qwen premium OFF / legacy-only.
- Keep GPT behavior unchanged.

Not approved:

- Production full GO.
- Quality repair activation.
- Qwen premium activation.
- GPT behavior changes.
- MCP/App SDK launch, tooling, OAuth, billing, or production work.

## Touched pages

- [[tasks/2026-06-22-cover-letter-quality-production-roadmap]]
- [[sources/2026-06-23-cover-letter-quality-pr248-merge-checkpoint]]
