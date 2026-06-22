---
title: "Cover Letter Quality Production Roadmap"
category: task
status: current
created: 2026-06-22
updated: 2026-06-22
type: implementation-roadmap
related: [[product/ai-product-model]], [[tech/proposal-ai-routing-and-inline-diff]], [[outputs/2026-05-26-proposal-language-generation-hardening]]
---

# Cover Letter Quality Production Roadmap

## Goal

Improve cover-letter generation without weakening factual safety:

- stop false `fail_closed` cases when premium provenance truly supports the final text;
- keep unsupported candidate claims blocked;
- reduce legacy/no-CV job-description repetition;
- simplify provider prompts after the provenance gate is safe;
- use `qualityShadow` later as one bounded repair trigger.

## Current Decision

Run the work sequentially:

1. PR 1: premium provenance through finalization.
2. PR 2: legacy cover-letter prompt.
3. PR 3: premium prompt V2, Mistral first.
4. PR 4: one-shot `qualityShadow` repair.

Parallel work is allowed only for read-only review or disjoint verification. Do not run multiple writers against `premiumCoverLetter.ts` or `generateProposalMutation.ts` at the same time.

## Execution Status

- PR 1: implemented, independently reviewed, pushed, PR opened: <https://github.com/panamini/neyssan/pull/230>.
- PR 2: implemented, independently reviewed, pushed, PR opened stacked on PR 1: <https://github.com/panamini/neyssan/pull/231>.
- PR 3: implemented, independently reviewed, pushed, PR opened stacked on PR 2: <https://github.com/panamini/neyssan/pull/232>.
- PR 4: blocked until PR 3 prompt behavior is reviewed as stable enough for a repair-layer change, or explicitly continued as a stack from PR 3.

## PR 1 Contract

Branch:

```text
codex/premium-provenance-finalization
```

Scope:

- `my-app/convex/lib/proposals/premiumCoverLetter.ts`
- `my-app/convex/generateProposalMutation.ts`
- `my-app/convex/lib/proposals/__tests__/premiumCoverLetter.test.ts`
- `my-app/convex/lib/proposals/__tests__/proposalWriterPrompt.test.ts`
- `my-app/convex/lib/proposals/__tests__/proposalProviderBusy.test.ts` only if full action coverage is needed

Non-goals:

- no parser/CV ingest changes;
- no `pdf-ingest/`;
- no UI;
- no DB schema change;
- no global `templates.ts` change;
- no new provider, embedding, judge LLM, or extra model call in PR 1;
- do not include unrelated dirty files in branch, staging, commit, or PR.

Safety invariant:

```text
Never bypass final candidate-evidence validation from candidateFactIds alone.
```

Trusted premium provenance must be tied to final text and either:

- `validated_final_text`, or
- `validated_after_structured_repair`.

It must never be trusted when:

- generated from a legacy wrapper only;
- normalized from a claim plan without text-to-fact validation;
- invalidated by later body-part mutation;
- `no_cv`;
- based on `demandIds`;
- based only on `system_inference`.

## Verified Anchors

- `PremiumWriterOutputV1` has `claimIds`, `factIds`, `demandIds`: `my-app/convex/lib/proposals/premiumCoverLetter.ts`.
- `PremiumCoverLetterGenerationResult` currently exposes `bodyParts`, `qualityShadow`, `mode`, `evidenceUsed`, `omittedWeakEvidence`, but not structured provenance.
- `toCoverLetterBodyParts()` drops the structured IDs.
- `normalizeProviderWriterOutputProvenance()` can correct IDs for provider-specific output.
- `wrapLegacyBodyPartsAsPremiumWriterOutputV1()` can inject IDs from the claim plan.
- `finalizeProposalForPersistence()` calls `assertCvBackedCoverLetterHasCandidateEvidence()`.
- `ProposalFinalizationError` currently routes to `fail_closed`.

## PR 1 Acceptance

- Premium CV-backed final text with verified provenance no longer fails only because the lexical regex misses the phrasing.
- A decorative valid `factId` is not enough.
- Job-only, no-CV, legacy, `system_inference`, `demandId`, invalidated provenance, and legacy-wrapped provenance still use lexical validation.
- Existing job-summary-only rejection tests remain valid.
- No DB schema change.
- Metadata/observability uses tags or already-supported metadata fields only.

## Suggested PR 1 Commands

```bash
cd my-app
rtk npx vitest run convex/lib/proposals/__tests__/premiumCoverLetter.test.ts convex/lib/proposals/__tests__/proposalWriterPrompt.test.ts
rtk npm run typecheck
rtk git diff -- convex/lib/proposals/premiumCoverLetter.ts convex/generateProposalMutation.ts convex/lib/proposals/__tests__/premiumCoverLetter.test.ts convex/lib/proposals/__tests__/proposalWriterPrompt.test.ts
```

Broaden to `proposalProviderBusy.test.ts` only if the implementation touches action-level persistence/routing behavior.

## PR Sequence Notes

PR 2 removed the generic `generateCreativeProposal` cover-letter fallback from the legacy `cover_letter` path and now routes that path through the cover-letter prompt via `generateTextWithFallbacks`.

PR 3 versions and flags premium prompt V2 for Mistral only. Default V1 remains unchanged when the flag is absent/off, and non-Mistral providers stay on V1 even if the flag is on.

PR 4 should introduce at most one `qualityShadow` repair attempt and preserve the original safe output if repair fails.

## Local Alignment

This wiki task is a retrieval mirror. The code-adjacent implementation truth is the local plan:

`/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan-new/docs/plans/2026-06-22-cover-letter-quality-production-roadmap.md`
