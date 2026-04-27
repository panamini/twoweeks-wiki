

Use the LOCAL repo only. Same current branch.

Implement only this dev ergonomics fix.

## Problem

Advisory beta is currently allowlist-only through:

- STRUCTURED_MATCH_READ_ADVISORY_BETA
- STRUCTURED_MATCH_READ_BETA_VIEWERS

That is correct for production/beta, but too restrictive in local/dev. In dev, I want the advisory structured preview visible to everyone when the advisory flag is on.

## Mission

Allow all users to see `Structured preview` in local/dev when explicitly enabled.

Keep production/beta allowlist behavior safe.

## Required behavior

When `STRUCTURED_MATCH_READ_ADVISORY_BETA=true`:

### Dev/local mode

If one of these is true:

- app is running in local/dev environment
- `STRUCTURED_MATCH_READ_BETA_VIEWERS=*`
- optional explicit flag `STRUCTURED_MATCH_READ_ADVISORY_BETA_ALL=true`

then all users can see the advisory structured preview.

### Production/non-dev mode

Do not allow everyone by default.

Require:

- `STRUCTURED_MATCH_READ_ADVISORY_BETA=true`
- `STRUCTURED_MATCH_READ_SHADOW=true`
- viewer is in `STRUCTURED_MATCH_READ_BETA_VIEWERS`

Wildcard `*` must either be rejected outside dev/local or ignored outside dev/local.

## Hard boundary

Do NOT change:

- computeMatchRead
- production score
- production tier
- ranking
- filtering
- badges
- CTA copy
- Proposal Forge
- extraction schema
- model selection
- prompt version
- structured scorer formula

Do NOT make structured score authoritative.

## Copy must remain

Use:

- `Current match`
- `Structured preview`
- `Experimental match read. Production score remains authoritative.`

Forbidden copy remains forbidden:

- AI score
- Recommended score
- Better score
- New score

## Tests required

Add/update tests proving:

1. dev/local + advisory flag on + wildcard/all flag shows `Structured preview` to any user.
2. production/non-dev + wildcard does not expose to everyone.
3. production/non-dev still requires allowlist.
4. advisory flag off hides preview everywhere.
5. structured shadow flag off hides preview everywhere.
6. production score remains visible and authoritative.
7. no ranking/filtering/badges/CTA behavior changes.

## Env example / docs

Document dev usage:

```env
STRUCTURED_MATCH_READ_SHADOW=true
STRUCTURED_MATCH_READ_ADVISORY_BETA=true
STRUCTURED_MATCH_READ_BETA_VIEWERS=*
APP_GIT_COMMIT_SHA=<current commit>



