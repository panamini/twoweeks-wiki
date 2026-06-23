---
title: "Cover Letter Mistral V2 Staging Green Checkpoint"
category: source
status: current
created: 2026-06-24
updated: 2026-06-24
type: analysis
related: [[tasks/2026-06-22-cover-letter-quality-production-roadmap]], [[sources/2026-06-23-cover-letter-quality-pr249-staged-internal-gate]]
---

# Cover Letter Mistral V2 Staging Green Checkpoint

## Summary

The cover-letter Mistral V2 staging gate completed successfully on Convex dev/staging deployment `dev:neat-starfish-33` after the stale function-spec blocker and stale `proposalHandoffs` schema-data blocker were resolved. The recorded decision is:

```text
COVER_LETTER_MISTRAL_V2_STAGING_GREEN
```

This supersedes the previous checkpoint:

```text
COVER_LETTER_MISTRAL_V2_READY_FOR_INTERNAL_STAGING_ONLY
```

Production full GO remains not approved.

## Key points

- App base: `application-os-foundation`.
- Required app HEAD: `d628bed79c0063d2c06c836015e87d313385bbd2`.
- PR249 merged into base:
  - PR: <https://github.com/panamini/neyssan/pull/249>
  - Merge SHA: `d628bed79c0063d2c06c836015e87d313385bbd2`
  - Head SHA: `11f56d5e44b24db8b3a479cff0bee76c24974b05`
- Staging target:
  - Convex deployment: `dev:neat-starfish-33`
  - Team: `panamini`
  - Project: `banzai`
- Production was untouched:
  - no `--prod`
  - no `npx convex deploy`

## Staging sync prerequisite

The deployed staging function spec was stale and initially missed:

- `mistral-medium-latest`
- `qwen3.7-max`

The schema push was then blocked by stale `proposalHandoffs` documents missing `handoffToken`.

Stale data summary:

- invalid `proposalHandoffs`: 28
- fresh invalid rows: 0
- oldest invalid row: `2026-04-08T06:16:25.843Z`
- newest invalid row: `2026-06-06T22:50:12.107Z`
- all invalid rows were older than 24h

Cleanup and sync:

- A table-scoped cleanup removed 28/28 invalid `proposalHandoffs`.
- `npx convex dev --once` completed after cleanup.
- The deployed function spec after sync includes:
  - `chatgpt`
  - `mistral-agent`
  - `mistral-large-latest`
  - `mistral-medium-latest`
  - `mistral-small-latest`
  - `qwen3.7-max`

## Staging flag state

Only the canonical Mistral V2 prompt flag was enabled on staging:

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

Path flags were unchanged:

```text
cover_letter_premium_path_v1=1
COVER_LETTER_PREMIUM_PATH_V1=1
ENABLE_COVER_LETTER_PREMIUM_PATH_V1=1
```

## Smoke result

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

## Safety summary

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

Final app status was clean except the pre-existing untracked file:

```text
docs/plans/2026-06-22-cover-letter-quality-production-roadmap.md
```

## Implications

Mistral V2 is now green on internal staging. The next decision is not automatic production rollout; production still requires a separate release gate, monitoring plan, and explicit approval.

## Touched pages

- [[tasks/2026-06-22-cover-letter-quality-production-roadmap]]
- [[hot]]
- [[index]]
- [[log]]
