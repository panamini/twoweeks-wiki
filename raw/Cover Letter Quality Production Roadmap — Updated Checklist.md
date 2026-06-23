---
title: "Cover Letter Quality Production Roadmap — Updated Checklist"
category: task
status: current-no-go-for-full-production
created: 2026-06-22
updated: 2026-06-23
type: implementation-roadmap
related:
  - docs/plans/2026-06-22-cover-letter-quality-production-roadmap.md
  - /tmp/neyssan-pr246-mistral-v2-handoff.md
  - /mnt/data/neyssan-pr246-mistral-v2-handoff.md
---



## Purpose

Track the current state of the cover-letter quality work after the PR230–PR245 sequence, the post-merge smoke tests, and the first Mistral V2 internal canary.

This document is an updated working checklist. It does **not** replace the PRs, commits, diffs, or prior handoffs. Use those as source of truth when implementing.

## Current state — 2026-06-23

Current branch line:

```text
application-os-foundation
```

Known current head after PR245:

```text
2ceb98d071b51e87a368dc3d01f33d7ce147f724
```

Overall decision:

```text
Merged baseline with flags OFF: OK
Mistral V2 canary expansion: NO-GO / HOLD
Quality repair: OFF / NO-GO
Full production GO: NO-GO
Next implementation: PR246 Mistral V2 factuality tightening
```

## Completed PRs / gates

| Item | Status | Notes |
|---|---:|---|
| PR242 — lint config boundary | Done | Config boundary fixed; not a full lint cleanup. |
| PR243 — proposalBodyComposer evidence-chain contract | Done | Superseded old PR236. |
| PR244 — Playwright browser install workflow | Done | Real Playwright step reached and passed later. |
| PR230 — premium cover-letter final provenance | Done | Main provenance/finalization architecture merged. |
| PR231 — legacy `cover_letter` prompt routing | Done | Legacy cover letters no longer use generic creative proposal prompt. |
| PR232 — Mistral premium prompt V2 | Done, flag OFF | Merged behind flags; not enabled by default. |
| PR233 — bounded `qualityShadow` repair | Done, flag OFF | Merged behind `ENABLE_COVER_LETTER_QUALITY_REPAIR_V1`; not canaried. |
| PR245 — GPT premium finalization hardening | Done | GPT premium flags-off smoke became clean after merge. |
| Post-PR245 flags-OFF smoke | Done | GPT premium, Mistral medium/large V2 OFF, No-CV Mistral, Qwen legacy all passed. |
| First Mistral V2 internal canary | Done, failed gate | Mistral-large direct V2 produced unsupported expansion. |

## What works now with flags OFF

- GPT premium cover letter: PASS.
- Mistral medium premium with V2 OFF: PASS.
- Mistral large premium with V2 OFF: PASS.
- No-CV Mistral: PASS with safe no-CV provenance.
- Qwen with premium flags OFF: legacy-only path, PASS.
- Quality repair remains disabled.

## Current canary result — Mistral V2

Internal/no-DB canary with Mistral V2 ON and quality repair OFF:

| Case | Model | Flags | Outcome | Decision |
|---|---|---|---|---|
| CV direct | Mistral medium | V2 ON, repair OFF | premium saved, 4 verified facts | PASS |
| CV direct | Mistral large | V2 ON, repair OFF | premium saved, 4 verified facts | NO-GO risk |
| Adjacent/distant | Mistral medium | V2 ON, repair OFF | premium saved, 4 verified facts | PASS |
| Adjacent/distant | Mistral large | V2 ON, repair OFF | premium saved, 4 verified facts | PASS |
| No-CV | Mistral large | V2 ON, repair OFF | saved safely, `untrusted_no_cv`, 0 verified facts | PASS |
| GPT premium | V2 flags ON | GPT did not receive V2 | PASS |
| Qwen | Qwen premium OFF | legacy-only path | PASS |

Blocking issue:

```text
Mistral-large direct V2 generated: "standardizing component usage and versioning"
```

Supported CV facts only covered:

- design-system migration across four squads;
- improved release consistency across shared interface work.

Decision:

```text
Treat this as unsupported candidate-detail expansion.
Hold Mistral V2 canary expansion.
Create PR246 to tighten factuality guidance.
```

## Current flags policy

Keep these OFF/unset outside a controlled internal test:

```text
ENABLE_COVER_LETTER_PREMIUM_PROMPT_V2=off
COVER_LETTER_PREMIUM_PROMPT_V2=off
cover_letter_premium_prompt_v2=off
ENABLE_COVER_LETTER_QUALITY_REPAIR_V1=off
```

Allowed only for PR246 internal validation:

```text
Mistral V2 flags ON in internal/no-DB canary only
Quality repair OFF always
Qwen premium flags OFF
```

## Checklist — completed

- [x] Preserve final premium provenance through persistence.
- [x] Keep unsupported candidate claims blocked.
- [x] Prevent `candidateFactIds` alone from counting as proof.
- [x] Keep job/company/demand/system inference from counting as candidate evidence.
- [x] Keep no-CV safe and non-inventive.
- [x] Improve legacy `cover_letter` routing away from generic creative proposal generation.
- [x] Merge Mistral V2 behind explicit flags only.
- [x] Merge quality repair behind explicit default-OFF flag only.
- [x] Fix Playwright workflow so real tests run.
- [x] Fix GPT premium live finalization fail-closed case without weakening safety.
- [x] Verify post-PR245 flags-OFF smoke is clean.
- [x] Run first Mistral V2 internal canary.
- [x] Stop Mistral V2 canary on unsupported-detail expansion.

## Checklist — active / next

### PR246 — Mistral V2 factuality tightening

- [ ] Start fresh from `application-os-foundation` at or after `2ceb98d071b51e87a368dc3d01f33d7ce147f724`.
- [ ] Create branch `codex/pr246-mistral-v2-factuality-tightening`.
- [ ] Inspect Mistral V2 prompt guidance in `my-app/convex/lib/proposals/premiumCoverLetter.ts`.
- [ ] Add a regression around the unsupported phrase `standardizing component usage and versioning`.
- [ ] Prefer prompt-side tightening first.
- [ ] Do not add broad post-generation rewrites.
- [ ] Do not weaken provenance/finalization guards.
- [ ] Do not change GPT/Qwen behavior.
- [ ] Do not enable V2 by default.
- [ ] Do not enable quality repair.
- [ ] Run targeted proposal tests.
- [ ] Rerun internal/no-DB Mistral V2 canary matrix.
- [ ] Return GO/NO-GO for internal canary expansion.

Acceptance criteria for PR246:

- [ ] Mistral-large direct V2 no longer expands `design-system migration` into unsupported component/versioning details.
- [ ] Direct-match cases stay narrow and CV-backed.
- [ ] Adjacent/distant cases still preserve factual-overlap framing.
- [ ] No-CV still does not invent candidate evidence.
- [ ] GPT does not receive V2.
- [ ] Qwen remains unaffected / legacy with flags OFF.
- [ ] Quality repair remains disabled.
- [ ] Tests pass.
- [ ] Canary rerun table is clean.

### After PR246 if canary is clean

- [ ] Keep Mistral V2 internal/staging only.
- [ ] Run 3–5 additional internal generations for `mistral-medium-latest`.
- [ ] Run 3–5 additional internal generations for `mistral-large-latest`.
- [ ] Compare against V1 baseline for specificity, unsupported claims, finalization, provenance, latency/cost.
- [ ] Decide whether to expand internal canary or keep on hold.
- [ ] Do not enable production without separate release decision.

### Quality repair later — not now

- [ ] Keep `ENABLE_COVER_LETTER_QUALITY_REPAIR_V1=off`.
- [ ] Create a separate canary plan only after Mistral V2 is stable or explicitly deferred.
- [ ] Verify extra model-call cost and latency.
- [ ] Verify cancellation path.
- [ ] Verify repair never changes provenance into unsupported candidate claims.
- [ ] Verify no-CV and legacy-wrapped outputs do not repair.

### Qwen premium later — not now

- [ ] Keep Qwen premium flags OFF.
- [ ] If Qwen premium is desired later, create a separate PR for schema/body-parts compatibility.
- [ ] Do not mix Qwen premium work with Mistral V2 or quality repair.

### Production release later

- [ ] Define production rollout separately.
- [ ] Verify staging deploy.
- [ ] Verify smoke in deployed environment.
- [ ] Keep rollback flags documented.
- [ ] Monitor finalization failures, unsupported-claim reports, provider schema failures, latency/cost, and regeneration rates.

## Do not change during PR246

- Parser / CV ingest.
- UI.
- DB schema.
- Billing.
- OAuth / provider token flow.
- Deployment.
- Lint cleanup.
- Qwen premium behavior.
- GPT prompt/behavior unless a regression is proven.
- Quality repair behavior.
- `docs/plans/2026-06-22-cover-letter-quality-production-roadmap.md` unless explicitly asked to commit docs.

## Suggested commands for PR246

Run from `my-app` unless repo instructions say otherwise:

```bash
git diff --check
npx vitest run convex/lib/proposals/__tests__/premiumCoverLetter.test.ts convex/lib/proposals/__tests__/proposalWriterPrompt.test.ts
npx vitest run convex/lib/proposals/__tests__
```

Then rerun the internal/no-DB Mistral V2 canary matrix:

- Mistral medium direct, V2 ON, repair OFF.
- Mistral large direct, V2 ON, repair OFF.
- Mistral medium adjacent/distant, V2 ON, repair OFF.
- Mistral large adjacent/distant, V2 ON, repair OFF.
- Mistral no-CV, V2 ON, repair OFF.
- GPT with V2 flags ON — should not receive V2.
- Qwen premium OFF — should stay legacy-only.

## Remaining risks

- Mistral V2 may still infer plausible implementation details from broad CV phrases.
- Prompt-only tightening may not be enough; a later validation guard may be needed if provider elaboration recurs.
- Over-tightening V2 could reduce the adjacent/distant quality improvement seen in canary.
- Quality repair is still uncanaried and must stay OFF.
- Repo-wide lint debt remains outside this roadmap.

## Rollback notes

Runtime rollback / hold:

```text
ENABLE_COVER_LETTER_PREMIUM_PROMPT_V2=off
COVER_LETTER_PREMIUM_PROMPT_V2=off
cover_letter_premium_prompt_v2=off
ENABLE_COVER_LETTER_QUALITY_REPAIR_V1=off
```

Git rollback:

- Revert PR246 only if PR246 is merged and introduces a regression.
- Do not revert PR230–PR245 unless a specific regression is proven and approved.

## Current next smallest step

```text
Open a fresh PR246 branch from application-os-foundation and tighten Mistral V2 factuality guidance with tests.
```
