---
title: "Release Orchestration Checkpoint - Staging and PR87.8"
category: source
tags: [release-orchestration, cover-letter, staging, chatgpt-app, mcp, pr87-8]
created: 2026-06-23
updated: 2026-06-23
status: current
type: analysis
related: [[tasks/2026-06-22-cover-letter-quality-production-roadmap]], [[product/chatgpt-app-sdk-roadmap]], [[product/manual-application-handoff]], [[sources/2026-06-23-cover-letter-quality-pr249-staged-internal-gate]], [[sources/2026-06-23-twoweeks-mcp-chatgpt-app-sdk-roadmap-checkpoint]]
---

# Release Orchestration Checkpoint - Staging and PR87.8

## Summary

Root orchestration ran two isolated child lanes from `application-os-foundation` at `d628bed79c0063d2c06c836015e87d313385bbd2`, then corrected the staging access procedure after follow-up operator review.

Terminal decisions:

```text
CHILD A: STAGING_BLOCKED, corrected after follow-up to ROLLED_BACK_AFTER_STAGING_FAILURE
CHILD B: PR87_8_GATE_STILL_BLOCKED
```

No application code changed. No pull request was opened. No production, public launch, live submit/apply, quality repair, Qwen premium, or GPT behavior change occurred.

## Key points

- Application preflight confirmed `origin/application-os-foundation` at `d628bed79c0063d2c06c836015e87d313385bbd2`, with only the tolerated local untracked application roadmap mirror present in the primary checkout.
- Wiki checkpoint `cfa3c06b67180b87c4b8e8508514004eb748350e` was cleanly pushed to `origin/main` before child work.
- Staging target was identified as Convex `dev:neat-starfish-33` / `https://neat-starfish-33.convex.cloud`; production was separately identified as `prod:giddy-basilisk-88` / `https://giddy-basilisk-88.convex.cloud`.
- The initial `401 Unauthorized: MissingAccessToken` was caused by using `convex env --env-file`; this Convex CLI path selects the deployment from the env file but does not fall back to the global access token unless the file contains `CONVEX_DEPLOY_KEY`.
- Loading root `.env.local` into the shell environment instead allowed authenticated staging env reads through the existing global Convex token.
- Previous staging values for `cover_letter_premium_prompt_v2`, `COVER_LETTER_PREMIUM_PROMPT_V2`, `ENABLE_COVER_LETTER_PREMIUM_PROMPT_V2`, and `ENABLE_COVER_LETTER_QUALITY_REPAIR_V1` were all unset.
- `cover_letter_premium_prompt_v2=on` was applied to staging, then rolled back to unset after a deployed smoke check showed staging was not on the verified current code surface.
- Rollback verification confirmed all three Mistral V2 flag names and `ENABLE_COVER_LETTER_QUALITY_REPAIR_V1` were unset again.
- Evidence for stale staging surface: local `d628bed79c0063d2c06c836015e87d313385bbd2` code accepts `mistral-medium-latest`, but staging `/test/generate` rejected `mistral-medium-latest` during argument validation before generation.
- Current code proves Mistral V2 flag precedence as `cover_letter_premium_prompt_v2` > `COVER_LETTER_PREMIUM_PROMPT_V2` > `ENABLE_COVER_LETTER_PREMIUM_PROMPT_V2`; accepted true values are `1`, `true`, and `on`; V2 is scoped to `writerProvider === "mistral"`.
- Quality repair still reads only `ENABLE_COVER_LETTER_QUALITY_REPAIR_V1` and defaults false.
- PR87.8 reconciliation found the MCP/App SDK production gate still blocked: no production MCP endpoint, no production `tools/list` or `tools/call`, no OAuth/account linking path, no real tool handlers, no outbound HTTP/model calls through MCP, no live submit/apply, no approved-answer copy, no reachable `provider_verified_submitted`, and no production billing behavior.
- PR80B manual handoff remains implemented and tested as the safe delivery boundary, with manual export/download allowed and provider submission still user-owned.
- Focused MCP/manual-handoff/billing tests passed in the isolated PR87.8 worktree: 14 files, 104 tests.
- `npm run build` passed in the isolated PR87.8 worktree with warnings only for stale Browserslist data, `pdfjs-dist` eval, and large chunks.

## Implications

Cover-letter Mistral V2 remains ready for internal/staging-only rollout in principle, but the actual staging rollout is blocked until staging is redeployed or otherwise proven to run `d628bed79c0063d2c06c836015e87d313385bbd2` or a verified descendant. The attempted flag change was rolled back.

PR87.8 does not require a corrective PR from this checkpoint. The correct product state is that PR88 private beta and PR89 public launch remain blocked until a later reviewed gate explicitly opens production MCP/App SDK behavior.

## Touched pages

- [[tasks/2026-06-22-cover-letter-quality-production-roadmap]]
- [[product/chatgpt-app-sdk-roadmap]]
- [[hot]]
- [[index]]
