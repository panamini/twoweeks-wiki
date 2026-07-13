---
title: "Cover Letter Quality Production Roadmap"
category: task
status: current
created: 2026-06-22
updated: 2026-07-13
type: implementation-roadmap
sources: [2026-06-24-cover-letter-mistral-v2-staging-green, 2026-06-23-release-orchestration-staging-pr87-8-checkpoint, 2026-06-23-cover-letter-quality-pr249-staged-internal-gate, 2026-06-23-cover-letter-quality-pr248-merge-checkpoint, 2026-06-23-cover-letter-quality-pr246-merge-checkpoint, 2026-06-23-cover-letter-quality-production-roadmap-updated-checklist]
related: [[product/ai-product-model]], [[tech/proposal-ai-routing-and-inline-diff]], [[outputs/2026-05-26-proposal-language-generation-hardening]]
---

# Cover Letter Quality Production Roadmap

## Purpose

Track the current state of the cover-letter quality work through the deterministic replay contract in PR310 and the multilingual policy shadow in PR312.

This document is an updated working checklist. It does not replace the PRs, commits, diffs, or prior handoffs. Use those as source of truth when implementing.

## Workstream Boundary

This page owns only cover-letter generation quality, provenance, prompts, provider behavior, and quality repair gates.

It does not own the Twoweeks MCP / ChatGPT App SDK roadmap, manual application handoff, Apps SDK launch gates, OAuth, tools endpoints, provider submission, billing, or production App SDK release work. Those belong to [[product/chatgpt-app-sdk-roadmap]] and [[product/manual-application-handoff]].

Shared branch/base references such as `application-os-foundation` and PR245 are coordination anchors only. They do not mean the cover-letter quality checklist and the MCP/App SDK checklist should be executed in the same PR.

## Current State - 2026-07-13

Authoritative app target:

```text
application-os-foundation@3f3fb3a42c1a7594a43c0360613a7f2360ecf078
```

| Delivery | Exact evidence | Current meaning |
|---|---|---|
| PR310 - evaluation/replay truth contract | Reviewed head `ff6d93b356d77e5aff8f72348a4b2a743b18afe5`; merge `f1794d421a3b07b67315efd8e335929193979fd9` | Offline replay is deterministic, budgeted, prompt/config-bound, and provider-free by default. |
| PR312 - multilingual policy shadow | Reviewed head `4a3d2d48ec822bfbde2c4d7382cfd52d420b0629`; merge `3f3fb3a42c1a7594a43c0360613a7f2360ecf078` | Policy candidate remains shadow-only; no production cutover occurred. |

Post-merge verification:

- Production and replay call the same `attemptPremiumCoverLetterGeneration` preparation path and the same `finalizePremiumCoverLetterPayloadForPersistence` finalizer. A separate cosmetic "shared core" extraction is not justified; this roadmap treats that leaf as `ALREADY_SATISFIED`.
- Recorded replay remains provider-free and preserves the OpenAI and Mistral artifact/provenance hashes.
- Policy shadow remains 84 records, 70 plans, 14 rejections, and 13 non-English distant plans without demand anchors.
- Policy matrix hash remains `b447e3568abe93f4f42b3419894bb19720583f89f7f60e364ceea2aa22e20260`.
- Quality repair remains OFF. Production policy cutover and full production GO remain unapproved.

### Evidence boundary: examples versus quality benchmarks

- PR310 contains two authored synthetic replay fixtures, both in English: one OpenAI direct-fit case and one structured Mistral adjacent-fit case. They prove deterministic production-path replay and provenance, not live editorial superiority.
- There is no committed French replay fixture yet. A complete French letter exists only as synthetic test content, not as a recorded provider response or current live benchmark.
- The historical 2026-03-12 benchmark contains 48 complete English outputs across 12 cases and four models, including latency, token, and cost data. Its harness is explicitly isolated from current production generation, so it is historical evidence only.
- The 84-case multilingual shadow measures planning and acceptance policy. It does not score the prose quality of 84 generated letters.

Do not remove a configured document language solely because it lacks current editorial evidence. Separate deterministic capability, policy eligibility, and native-language quality; promote or demote only from cohort-specific evidence.

## Roadmap After PR312

### Architecture and reliability

1. Run a separate `HIGH`-risk assessment and plan for single-flight request claiming, transactional accepted-artifact commit, abandoned-processing recovery, and idempotency/concurrency tests.
2. Keep that work behavior-preserving: no prompt tuning, provider/model switch, policy cutover, or UI change in the same PR.
3. Preserve the existing shared preparation/finalization path; do not create a duplicate truth model or façade.

### Multilingual quality evidence

1. Add at least one committed French replay fixture that exercises the same final artifact path as the English fixtures.
2. Add one representative non-Latin replay fixture before claiming broad multilingual editorial parity.
3. Resolve or explicitly reclassify the 13 distant non-English plans with zero demand anchors, then rebaseline the matrix and explain every hash change.
4. Run blind paired editorial review by eligible language/context cohorts. Deterministic tests alone cannot prove hiring-quality prose.
5. If live provider comparison is needed, use a small explicit budget and representative cohorts first; PR310/PR312 themselves made zero provider calls.

### Cutover gates

- Keep the policy candidate shadow-only until the multilingual acceptance gaps and editorial review are closed.
- Keep quality repair OFF until a separately budgeted latency, cancellation, factuality, and provenance canary passes.
- Keep production full GO, client post-save patch removal, server artifact authority, and simplified user messaging in later reversible PRs.
- Keep GPT, Mistral, Qwen, routing, and model-selection changes separate from persistence and cutover work.

## Historical checkpoint - 2026-06-24

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
8375257fea4799fef29a97db76b58e0b90b276cf
```

PR248 merge commit:

```text
2fd7ebef142859fb089bf8e9d270bf6b5b590fa1
```

PR249 merge commit:

```text
d628bed79c0063d2c06c836015e87d313385bbd2
```

Overall decision:

```text
Merged baseline with flags OFF: OK
PR246 merged into application-os-foundation: YES
Post-merge Mistral V2 canary: CLEAN
PR248 merged into application-os-foundation: YES
PR248 decision marker: READY_FOR_STAGED_INTERNAL_MISTRAL_V2_EXPANSION
PR249 merged into application-os-foundation: YES
PR249 staged internal Mistral V2 gate: STAGED_INTERNAL_MISTRAL_V2_READY
Previous checkpoint: COVER_LETTER_MISTRAL_V2_READY_FOR_INTERNAL_STAGING_ONLY
Current staging decision: COVER_LETTER_MISTRAL_V2_STAGING_GREEN
Quality repair: OFF / NO-GO
Full production GO: NO-GO
Latest staging checkpoint: STAGING_GREEN on Convex `dev:neat-starfish-33` after stale function-spec sync and stale `proposalHandoffs` cleanup. Canonical staging flag `cover_letter_premium_prompt_v2=1` is enabled only on staging. Production full GO remains a separate later decision.
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
| PR248 - no-CV candidate-history boundary | Done, merged | Squash merge `2fd7ebef142859fb089bf8e9d270bf6b5b590fa1`; expected head `fd478470525942caacbec12d01cdcb39d2688c22`; diff scope stayed in `premiumCoverLetter.ts` and `premiumCoverLetter.test.ts`; merge message reports `READY_FOR_STAGED_INTERNAL_MISTRAL_V2_EXPANSION`. |
| PR249 - staged internal Mistral V2 gate | Done, merged/gate clean | Squash merge `d628bed79c0063d2c06c836015e87d313385bbd2`; head `11f56d5e44b24db8b3a479cff0bee76c24974b05`; GitHub `CI` and `Playwright Tests` passed before merge; local staged internal gate reported `STAGED_INTERNAL_MISTRAL_V2_READY` / `COVER_LETTER_MISTRAL_V2_READY_FOR_INTERNAL_STAGING_ONLY`. |

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

## PR248 Merge Checkpoint - No-CV Candidate-History Boundary

PR248 merged after the PR246 canary path. It tightened no-CV validation for Mistral V2, especially candidate-history leakage in English and French present-tense operational wording.

Verified local merge facts:

- PR: `https://github.com/panamini/neyssan/pull/248`
- Merge commit: `2fd7ebef142859fb089bf8e9d270bf6b5b590fa1`
- Expected head SHA matched: `fd478470525942caacbec12d01cdcb39d2688c22`
- Merge method: squash merge
- Changed files:
  - `my-app/convex/lib/proposals/premiumCoverLetter.ts`
  - `my-app/convex/lib/proposals/__tests__/premiumCoverLetter.test.ts`

Reported decision marker:

```text
READY_FOR_STAGED_INTERNAL_MISTRAL_V2_EXPANSION
```

Interpretation:

- PR248 is merged and the next stage can move forward internally.
- It is still not a production release.
- Quality repair remains OFF / NO-GO.
- Production full GO remains a separate later decision.

## PR249 Staged Internal Gate Checkpoint

PR249 merged after the PR248 no-CV boundary. It records the completed staged internal Mistral V2 expansion evidence gate after merge.

Verified merge facts:

- PR: `https://github.com/panamini/neyssan/pull/249`
- Base branch: `application-os-foundation`
- Merge method: squash
- Merge SHA: `d628bed79c0063d2c06c836015e87d313385bbd2`
- Head SHA: `11f56d5e44b24db8b3a479cff0bee76c24974b05`
- GitHub CI before merge: `CI` success and `Playwright Tests` success
- Local post-merge base: `application-os-foundation` at `d628bed79c0063d2c06c836015e87d313385bbd2`
- Local app status after gate: clean except pre-existing untracked `docs/plans/2026-06-22-cover-letter-quality-production-roadmap.md`

Post-merge verification:

- `CI=1 npx vitest run convex/lib/proposals/__tests__/premiumCoverLetter.test.ts convex/lib/proposals/__tests__/proposalWriterPrompt.test.ts --reporter=dot`: 2 files passed, 282 tests passed.
- `CI=1 npx vitest run convex/lib/proposals/__tests__ --reporter=dot`: 20 files passed, 581 tests passed.
- `git diff --check`: clean.

Staged internal Mistral V2 gate:

- 23 cases total.
- 19 PASS.
- 4 SKIPPED only because no committed French CV-backed fixtures existed.
- 0 FAIL.
- PR246 forbidden extrapolation hits: none.
- PR248 no-CV leakage hits: none.
- Unsupported claim examples: none found.
- French no-CV medium/large remained fixed.
- English no-CV medium/large remained fixed.
- Mistral direct and adjacent controls passed.
- GPT control passed: no Mistral V2 prompt marker or adapter text.
- Qwen control passed: legacy-only, `enteringPremiumAttempt=false`.
- Quality repair stayed OFF / not used.

Decision:

```text
STAGED_INTERNAL_MISTRAL_V2_READY
COVER_LETTER_MISTRAL_V2_READY_FOR_INTERNAL_STAGING_ONLY
```

Interpretation:

- Mistral V2 is ready for internal/staging-only rollout readiness.
- Production full GO is not approved.
- Quality repair remains OFF.
- Qwen remains legacy-only.
- GPT remains unchanged.
- MCP/App SDK work remains separate.

## Root Orchestration Checkpoint - 2026-06-23

Root spawned the internal/staging operator and MCP gate owner as isolated child lanes from `application-os-foundation` at `d628bed79c0063d2c06c836015e87d313385bbd2`.

Internal/staging rollout terminal decision after follow-up correction:

```text
ROLLED_BACK_AFTER_STAGING_FAILURE
```

Verified facts:

- Intended staging target: Convex `dev:neat-starfish-33` / `https://neat-starfish-33.convex.cloud`.
- Production target remained separate: `prod:giddy-basilisk-88` / `https://giddy-basilisk-88.convex.cloud`.
- Staging env reads work when root `.env.local` is sourced into the shell; using `convex env --env-file` was the wrong CLI path because it bypassed global-token fallback.
- Previous staging values for the three Mistral V2 flag names and quality repair were all unset.
- `cover_letter_premium_prompt_v2=on` was set as the single intended staging flag.
- A deployed `/test/generate` smoke rejected `mistral-medium-latest` at argument validation, while the verified base accepts that model type. This means the running staging function surface could not be proven to contain `d628bed79c0063d2c06c836015e87d313385bbd2`.
- The flag was rolled back to unset; rollback verification confirmed all three Mistral V2 flags and quality repair were unset.
- Production was untouched.

Next staging work must first redeploy or otherwise prove the staging function surface is at `d628bed79c0063d2c06c836015e87d313385bbd2` or a verified descendant, then reapply the single staging flag and run the deployed smoke matrix.

## Staging Green Checkpoint - 2026-06-24

Decision:

```text
COVER_LETTER_MISTRAL_V2_STAGING_GREEN
```

Staging target:

- Convex deployment: `dev:neat-starfish-33`
- Team: `panamini`
- Project: `banzai`
- Production untouched:
  - no `--prod`
  - no `npx convex deploy`

Staging sync prerequisite:

- Deployed function spec was initially stale and missed `mistral-medium-latest` and `qwen3.7-max`.
- Schema push was blocked by old `proposalHandoffs` rows missing `handoffToken`.
- Invalid `proposalHandoffs`: 28.
- Fresh invalid rows: 0.
- Oldest invalid row: `2026-04-08T06:16:25.843Z`.
- Newest invalid row: `2026-06-06T22:50:12.107Z`.
- All invalid rows were older than 24h.
- Table-scoped cleanup removed 28/28 invalid `proposalHandoffs`.
- `npx convex dev --once` completed after cleanup.
- Function spec after sync includes `chatgpt`, `mistral-agent`, `mistral-large-latest`, `mistral-medium-latest`, `mistral-small-latest`, and `qwen3.7-max`.

Staging flag enabled:

```text
cover_letter_premium_prompt_v2=1
```

Aliases remained unset:

```text
COVER_LETTER_PREMIUM_PROMPT_V2=not found
ENABLE_COVER_LETTER_PREMIUM_PROMPT_V2=not found
```

Quality repair remained unset/off:

```text
ENABLE_COVER_LETTER_QUALITY_REPAIR_V1=not found
```

Path flags remained unchanged:

```text
cover_letter_premium_path_v1=1
COVER_LETTER_PREMIUM_PATH_V1=1
ENABLE_COVER_LETTER_PREMIUM_PATH_V1=1
```

Staging smoke result:

```text
STAGING_GREEN
```

Smoke matrix:

| Case | Result |
|---|---:|
| Mistral medium French no-CV | PASS |
| Mistral large French no-CV | PASS |
| English no-CV control | PASS |
| CV-direct control | PASS |
| Adjacent-fit control | PASS |
| GPT isolation control | PASS |
| Qwen legacy-only control | PASS |
| Quality-repair-disabled control | PASS |

Safety summary:

- No PR246 forbidden extrapolation terms.
- No PR248 no-CV leakage phrases.
- No unsupported-claim pattern hits.
- GPT stayed on GPT and did not receive Mistral V2 behavior.
- Qwen stayed legacy-only in the control route.
- Quality repair stayed OFF.
- No source files changed.
- No app PR opened.
- No MCP work.
- Production full GO remains NOT approved.

## Current Flags Policy

Keep these OFF/unset outside a controlled internal test:

```text
ENABLE_COVER_LETTER_PREMIUM_PROMPT_V2=off
COVER_LETTER_PREMIUM_PROMPT_V2=off
cover_letter_premium_prompt_v2=off
ENABLE_COVER_LETTER_QUALITY_REPAIR_V1=off
```

Allowed only for post-merge verification and controlled internal/staging expansion:

- Mistral V2 canonical flag ON in internal/staging only
- Quality repair OFF always
- Qwen premium flags OFF
- Production/public env OFF until a separate production decision

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
- [x] Merge PR248 into `application-os-foundation`.
- [x] Confirm PR248 expected head SHA matched before merge.
- [x] Keep PR248 scoped to cover-letter quality no-CV candidate-history validation.
- [x] Keep PR248 diff scoped to `premiumCoverLetter.ts` and `premiumCoverLetter.test.ts`.
- [x] Keep quality repair and production flags OFF.
- [x] Record `READY_FOR_STAGED_INTERNAL_MISTRAL_V2_EXPANSION` as the reported PR248 decision marker.
- [x] Merge PR249 into `application-os-foundation`.
- [x] Confirm PR249 merge SHA `d628bed79c0063d2c06c836015e87d313385bbd2`.
- [x] Record GitHub CI before merge: `CI` success and `Playwright Tests` success.
- [x] Run post-merge targeted proposal tests from PR249 merge baseline.
- [x] Run post-merge full proposal test directory from PR249 merge baseline.
- [x] Run staged internal Mistral V2 gate: 23 total, 19 PASS, 4 SKIPPED for missing French CV-backed fixtures, 0 FAIL.
- [x] Confirm no PR246 forbidden extrapolation hits.
- [x] Confirm no PR248 no-CV leakage hits.
- [x] Confirm GPT control clean and unchanged.
- [x] Confirm Qwen legacy-only with `enteringPremiumAttempt=false`.
- [x] Confirm quality repair OFF / not used.
- [x] Record `COVER_LETTER_MISTRAL_V2_READY_FOR_INTERNAL_STAGING_ONLY`.
- [x] Clean stale invalid staging `proposalHandoffs` rows missing `handoffToken`: 28/28 removed, all older than 24h.
- [x] Sync Convex staging function surface with `npx convex dev --once`.
- [x] Confirm deployed function spec includes `mistral-medium-latest` and `qwen3.7-max`.
- [x] Enable only canonical staging Mistral V2 flag `cover_letter_premium_prompt_v2=1`.
- [x] Run deployed staging smoke matrix: 8/8 PASS, `STAGING_GREEN`.
- [x] Confirm GPT isolation, Qwen legacy-only control, quality repair OFF, PR246 forbidden terms absent, and PR248 no-CV leakage absent.
- [x] Record `COVER_LETTER_MISTRAL_V2_STAGING_GREEN`.

## Checklist - Active / Next

### Post-PR312 truth and shadow closeout

- [x] Merge PR310 deterministic replay truth contract with zero-provider default execution.
- [x] Bind recorded responses to production prompts, schemas, frozen configuration, finalizer, and stable artifact/provenance hashes.
- [x] Merge PR312 multilingual policy candidate as shadow-only.
- [x] Preserve the shadow baseline: 84 records, 70 plans, 14 rejections, 13 unanchored distant non-English plans, hash `b447e3568abe93f4f42b3419894bb19720583f89f7f60e364ceea2aa22e20260`.
- [x] Verify that production and evaluation already share deterministic preparation/finalization; dismiss a duplicate shared-core PR.
- [ ] Add a committed French replay fixture with a complete finalized letter.
- [ ] Add a representative non-Latin replay fixture.
- [ ] Resolve or explicitly reclassify the 13 unanchored distant non-English plans before policy cutover.
- [ ] Approve a separate transactional reliability program before changing claim/commit or recovery behavior.
- [ ] Run cohort-specific blind editorial review before claiming quality improvement or production readiness.

### Internal/staging-only Mistral V2 readiness

- [ ] Keep Mistral V2 internal/staging only.
- [x] Restore authorized Convex access for `dev:neat-starfish-33` by sourcing root `.env.local` instead of passing `--env-file`.
- [x] Record previous non-secret staging values before setting the selected Mistral V2 flag.
- [x] Redeploy or otherwise prove the staging function surface matches `d628bed79c0063d2c06c836015e87d313385bbd2` or a verified descendant.
- [x] Prove deployed staging revision before running deployed smoke.
- [ ] Do not enable production without a separate production release decision.
- [ ] Do not enable quality repair.
- [ ] Do not change Qwen premium behavior; keep Qwen legacy-only unless a separate Qwen PR is approved.
- [ ] Do not change GPT behavior.
- [ ] Keep MCP/App SDK work separate.
- [ ] Add committed French CV-backed direct/adjacent fixtures before treating those skipped rows as covered.

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

## Suggested Commands for Post-PR248 Verification

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

This wiki page is the canonical durable roadmap. The post-PR312 target does not contain a tracked code-adjacent mirror under `docs/plans/`; do not publish an older untracked local copy as current truth.

## Current Next Smallest Step

```text
Assess and plan the transactional reliability rail separately, while adding French/non-Latin replay evidence and resolving the 13 unanchored distant non-English shadow rows. Do not enable policy cutover, production, or quality repair without their own evidence and explicit gates.
```
