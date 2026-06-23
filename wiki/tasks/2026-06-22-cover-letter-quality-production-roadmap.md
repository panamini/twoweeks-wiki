---
title: "Cover Letter Quality Production Roadmap"
category: task
status: current
created: 2026-06-22
updated: 2026-06-23
type: implementation-roadmap
sources: [2026-06-23-cover-letter-quality-pr246-merge-checkpoint, 2026-06-23-cover-letter-quality-production-roadmap-updated-checklist]
related: [[product/ai-product-model]], [[tech/proposal-ai-routing-and-inline-diff]], [[outputs/2026-05-26-proposal-language-generation-hardening]]
---

# Cover Letter Quality Production Roadmap

## Purpose

Track the current state of the cover-letter quality work after the PR230-PR245 sequence, the PR246 merge, and the clean post-merge Mistral V2 internal canary.

This document is an updated working checklist. It does not replace the PRs, commits, diffs, or prior handoffs. Use those as source of truth when implementing.

## Workstream Boundary

This page owns only cover-letter generation quality, provenance, prompts, provider behavior, and quality repair gates.

It does not own the Twoweeks MCP / ChatGPT App SDK roadmap, manual application handoff, Apps SDK launch gates, OAuth, tools endpoints, provider submission, billing, or production App SDK release work. Those belong to [[product/chatgpt-app-sdk-roadmap]] and [[product/manual-application-handoff]].

Shared branch/base references such as `application-os-foundation` and PR245 are coordination anchors only. They do not mean the cover-letter quality checklist and the MCP/App SDK checklist should be executed in the same PR.

## Current State - 2026-06-23

Current branch line:

```text
application-os-foundation
```

Known current head after PR245:

```text
2ceb98d071b51e87a368dc3d01f33d7ce147f724
```

PR246 cleanup commit:

```text
dbb992c98050a525ecde59f961ec39f886fdab79
```

PR246 merge commit:

```text
8375257fea4799fef29a97db76e8b90b276cf
```

Overall decision:

```text
Merged baseline with flags OFF: OK
PR246 merged into application-os-foundation: YES
Post-merge Mistral V2 canary: CLEAN
Internal Mistral V2 canary expansion: GO
Quality repair: OFF / NO-GO
Full production GO: NO-GO
Next step: run 3-5 additional internal generations and compare against V1
```

## Completed PRs / Gates

| Item | Status | Notes |
|---|---:|---|
| PR242 - lint config boundary | Done | Config boundary fixed; not a full lint cleanup. |
| PR243 - proposalBodyComposer evidence-chain contract | Done | Superseded old PR236. |
| PR244 - Playwright browser install workflow | Done | Real Playwright step reached and passed later. |
| PR230 - premium cover-letter final provenance | Done | Main provenance/finalization architecture merged. |
| PR231 - legacy `cover_letter` prompt routing | Done | Legacy cover letters no longer use generic creative proposal prompt. |
| PR232 - Mistral premium prompt V2 | Done, flag OFF | Merged behind flags; not enabled by default. |
| PR233 - bounded `qualityShadow` repair | Done, flag OFF | Merged behind `ENABLE_COVER_LETTER_QUALITY_REPAIR_V1`; not canaried. |
| PR245 - GPT premium finalization hardening | Done | GPT premium flags-off smoke became clean after merge. |
| Post-PR245 flags-OFF smoke | Done | GPT premium, Mistral medium/large V2 OFF, No-CV Mistral, Qwen legacy all passed. |
| First Mistral V2 internal canary | Done, failed gate | Mistral-large direct V2 produced unsupported expansion. |
| PR246 - factuality tightening | Done, merged | Branch `codex/pr246-mistral-v2-factuality-tightening`; cleanup removed the roadmap doc from the PR diff; post-merge canary clean. |
| Post-merge Mistral V2 internal canary | Done, clean | Medium/large direct V2 passed; forbiddenHits empty; internal expansion GO. |

## What Works Now With Flags OFF

- GPT premium cover letter: PASS.
- Mistral medium premium with V2 OFF: PASS.
- Mistral large premium with V2 OFF: PASS.
- No-CV Mistral: PASS with safe no-CV provenance.
- Qwen with premium flags OFF: legacy-only path, PASS.
- Quality repair remains disabled.

## Historical Canary Result - Mistral V2

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
PR246 fixed this blocker in the merged branch.
```

## Post-merge Canary - Mistral V2

After PR246 merged into `application-os-foundation`, the internal/no-DB canary came back clean:

- Mistral medium direct V2 ON: premium structured saved, validation passed, repair disabled.
- Mistral large direct V2 ON: premium structured saved, validation passed, repair disabled.
- Full-output direct scan: `forbiddenHits: []` for medium and large, including the previously blocked unsupported-detail terms.
- GPT with V2 flags ON: premium structured saved; repair disabled.
- Qwen with premium flags OFF: legacy-only path, `executedPath: legacy`, `saveOutcome: legacy_saved_parsed`, `enteringPremiumAttempt: false`.
- Benchmark matrix across direct, adjacent, real-world adjacent, and no-CV: 8/8 premium validation passed.

Decision:

```text
Internal Mistral V2 canary expansion: GO
Quality repair: OFF / NO-GO
Production full GO: separate later decision
```

## Current Flags Policy

Keep these OFF/unset outside a controlled internal test:

```text
ENABLE_COVER_LETTER_PREMIUM_PROMPT_V2=off
COVER_LETTER_PREMIUM_PROMPT_V2=off
cover_letter_premium_prompt_v2=off
ENABLE_COVER_LETTER_QUALITY_REPAIR_V1=off
```

Allowed only for post-merge internal canary expansion:

- Mistral V2 flags ON in internal/no-DB canary only
- Quality repair OFF always
- Qwen premium flags OFF

## Checklist - Completed

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
- [x] Start PR246 from `application-os-foundation` after `2ceb98d071b51e87a368dc3d01f33d7ce147f724`.
- [x] Create branch `codex/pr246-mistral-v2-factuality-tightening`.
- [x] Keep PR246 scoped to cover-letter quality.
- [x] Inspect Mistral V2 prompt guidance in `my-app/convex/lib/proposals/premiumCoverLetter.ts`.
- [x] Add regression coverage for `standardizing component usage and versioning`.
- [x] Tighten Mistral V2 factuality guidance.
- [x] Keep production/default flags OFF.
- [x] Avoid GPT/Qwen/routing/parser/UI/DB/MCP/App SDK changes.
- [x] Run targeted tests for PR246.
- [x] Rerun internal/no-DB Mistral V2 canary for PR246.
- [x] Return reported GO for internal Mistral V2 canary expansion, subject to review/merge and post-merge rerun.
- [x] Remove the roadmap doc from the PR diff and keep it local-only.
- [x] Merge PR246 into `application-os-foundation`.
- [x] Rerun the post-merge internal/no-DB Mistral V2 canary.
- [x] Confirm internal Mistral V2 canary expansion GO.

## Checklist - Active / Next

### Internal Mistral V2 expansion after PR246 merge

- [ ] Keep Mistral V2 internal/staging only.
- [ ] Run 3-5 additional internal generations for `mistral-medium-latest`.
- [ ] Run 3-5 additional internal generations for `mistral-large-latest`.
- [ ] Compare against V1 baseline for specificity, unsupported claims, finalization, provenance, latency/cost.
- [ ] Decide whether to expand internal canary or keep on hold.
- [ ] Do not enable production without a separate release decision.

Acceptance criteria for PR246:

- [x] Mistral-large direct V2 no longer expands `design-system migration` into unsupported component/versioning details in the reported PR246 canary.
- [x] Direct-match cases stay narrow and CV-backed in the reported PR246 canary.
- [x] Adjacent/distant cases still preserve factual-overlap framing in the reported PR246 canary.
- [x] No-CV still does not invent candidate evidence in the reported PR246 canary.
- [x] GPT does not receive V2.
- [x] Qwen remains unaffected / legacy with flags OFF.
- [x] Quality repair remains disabled.
- [x] Targeted tests reported pass.
- [x] PR246 canary rerun table reported clean.
- [x] Independent review confirms the diff.
- [x] Post-merge rerun confirms the same result.

### Quality Repair Later - Not Now

- [ ] Keep `ENABLE_COVER_LETTER_QUALITY_REPAIR_V1=off`.
- [ ] Create a separate canary plan only after Mistral V2 is stable or explicitly deferred.
- [ ] Verify extra model-call cost and latency.
- [ ] Verify cancellation path.
- [ ] Verify repair never changes provenance into unsupported candidate claims.
- [ ] Verify no-CV and legacy-wrapped outputs do not repair.

### Qwen Premium Later - Not Now

- [ ] Keep Qwen premium flags OFF.
- [ ] If Qwen premium is desired later, create a separate PR for schema/body-parts compatibility.
- [ ] Do not mix Qwen premium work with Mistral V2 or quality repair.

### Production Release Later

- [ ] Define production rollout separately.
- [ ] Verify staging deploy.
- [ ] Verify smoke in deployed environment.
- [ ] Keep rollback flags documented.
- [ ] Monitor finalization failures, unsupported-claim reports, provider schema failures, latency/cost, and regeneration rates.

## Guardrails for Internal Expansion

- Parser / CV ingest.
- UI.
- DB schema.
- Billing.
- OAuth / provider token flow.
- MCP / ChatGPT App SDK tools, manifests, handlers, or endpoint exposure.
- Manual application handoff behavior.
- Deployment.
- Lint cleanup.
- Qwen premium behavior.
- GPT prompt/behavior unless a regression is proven.
- Quality repair behavior.

## Suggested Commands for PR246

Run from `my-app` unless repo instructions say otherwise:

```bash
git diff --check
npx vitest run convex/lib/proposals/__tests__/premiumCoverLetter.test.ts convex/lib/proposals/__tests__/proposalWriterPrompt.test.ts
npx vitest run convex/lib/proposals/__tests__
```

## Rollback Notes

Runtime rollback / hold:

```text
ENABLE_COVER_LETTER_PREMIUM_PROMPT_V2=off
COVER_LETTER_PREMIUM_PROMPT_V2=off
cover_letter_premium_prompt_v2=off
ENABLE_COVER_LETTER_QUALITY_REPAIR_V1=off
```

Git rollback:

- Revert PR246 only if PR246 is merged and introduces a regression.
- Do not revert PR230-PR245 unless a specific regression is proven and approved.

## Local Alignment

Code-adjacent mirror:

```text
/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan-new/docs/plans/2026-06-22-cover-letter-quality-production-roadmap.md
```

As of 2026-06-23, the local mirror is aligned to this PR246-only cover-letter quality plan and explicitly excludes MCP/App SDK and manual handoff work.

## Current Next Smallest Step

```text
Run 3-5 additional internal generations for `mistral-medium-latest` and `mistral-large-latest`, then compare against V1.
```
