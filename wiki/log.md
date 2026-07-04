---
title: "Log — twoweeks Wiki"
category: overview
updated: 2026-07-01
---

# Log du Wiki · twoweeks

Journal chronologique append-only de toutes les opérations sur le wiki.

```bash
grep "^## \[" wiki/log.md | tail -5   # Dernières 5 entrées
grep "^## \[" wiki/log.md | grep "ingest"  # Tous les ingests
```

---

## [2026-07-01] pr-branch | MCP PR107/PR108 summary status and launch-readiness checkpoint

**Agent** : Codex
**Mode** : pr-branch
**Source** : PR298 and PR299 merge metadata, GitHub PR bodies, user-provided PR299 merge facts, and live `application-os-foundation` head check

**Pages créées** :
- `wiki/sources/2026-07-01-pr107-pr108-mcp-summary-status-launch-readiness-checkpoint.md`

**Pages mises à jour** :
- `wiki/product/chatgpt-app-sdk-roadmap.md`
- `wiki/hot.md`
- `wiki/index.md`
- `wiki/log.md`

**Points notables** :
- PR298 `Add MCP readonly summary status boundary` merged into `application-os-foundation` as `072764abb80519bf2ce719a7816791d81053b0b9` on `2026-07-01T03:44:20Z`.
- PR299 `Harden MCP launch-readiness summary evidence` merged into `application-os-foundation` as `90424f14ad4d25969095dc4d397c38bcd01d1054` on `2026-07-01T13:20:26Z`.
- PR107 wraps the four PR106 real read-only summary tool results in a strict status envelope: `OK`, `STALE`, `NO_DATA`, `ONBOARDING_REQUIRED`, `MALFORMED`, `TIMEOUT`, or `DEPENDENCY_MISSING`.
- PR108 requires launch-readiness evidence to include explicit review flags for PR106 read-only summary execution and PR107 summary status normalization before evidence can be complete.
- Provider calls, write actions, refresh tokens, production account-link lifecycle expansion, billing/entitlements, and public launch remain blocked.

**Open items** : Do not rerun PR106, PR107, or PR108. Choose the next app-code safety or metadata refinement only after reloading the live roadmap and app code; public launch and provider/write expansion remain blocked unless a later reviewed decision explicitly opens them.

## [2026-07-01] pr-branch | MCP PR105 launch-readiness Vite wiring follow-up

**Agent** : Codex
**Mode** : pr-branch
**Source** : PR295 merge metadata, PR105 follow-up branch `codex/pr105-launch-readiness-vite-fix`, user-reported review findings, local verification evidence, and post-merge roadmap request

**Pages mises à jour** :
- `wiki/product/chatgpt-app-sdk-roadmap.md`
- `wiki/hot.md`
- `wiki/index.md`
- `wiki/log.md`

**Points notables** :
- PR293 `PR104: add MCP private beta eligibility gate` is merged into `application-os-foundation` as `7d96f7354a2c18282db019db718c0cc80862ab9e`.
- PR294 `PR105: add MCP launch readiness boundary` is merged into `application-os-foundation` as `6cadc1f6f2451e70734c8f0b36f91eaf7d505583`.
- PR295 `Fix PR105 launch readiness Vite wiring` merged into `application-os-foundation` as `d87260c018c3493d0f68de73fb5c0b38d7e7f710` from head `76f5580665be49813aaff689679468148fb276eb`.
- PR295 wires launch-readiness env into the default Vite production MCP route config, so real `/mcp` traffic no longer evaluates through an absent launch-readiness config.
- PR295 makes `publicLaunchRequested: true` return the blocking `public_launch_blocked` decision before evidence completeness checks, so public-launch-shaped requests cannot fall through to `tools/list` or `tools/call` dispatch.
- Validation evidence: focused launch-readiness tests passed with 7 tests, focused production route adapter tests passed with 165 tests, focused operational status tests passed with 18 tests, `tsc -p tsconfig.node.json --pretty false` passed, `git diff --check` passed, and Fallow audit passed with no issues in the 4 changed files.
- GitHub `js-tests`, Playwright `test`, CodeRabbit, and Semgrep passed; Semgrep completed successfully after the user-requested immediate merge.

**Open items** : Do not rerun PR104, PR105, or PR295. The next guarded MCP app PR must preserve PR101 policy, PR103 schema validation, PR104 private beta eligibility, and PR105 launch-readiness/public-launch blocking; provider calls, write actions, refresh tokens, production account-link lifecycle expansion, and public launch remain blocked.

## [2026-06-30] checkpoint | MCP PR99.2 trusted bearer quota caller

**Agent** : Codex
**Mode** : checkpoint
**Source** : PR287 merge metadata, PR287 review comments, active route-adapter anchors, and post-merge roadmap request

**Pages créées** :
- `wiki/sources/2026-06-30-pr99-2-mcp-bearer-quota-trusted-caller-checkpoint.md`

**Pages mises à jour** :
- `wiki/product/chatgpt-app-sdk-roadmap.md`
- `wiki/sources/2026-06-30-pr99-1-mcp-bearer-verification-hardening-bug-list.md`
- `wiki/hot.md`
- `wiki/index.md`
- `wiki/log.md`

**Points notables** :
- PR287 `PR99.2: trust socket address for MCP bearer quota` merged into `application-os-foundation` as `82fa9a09e40d2243bd2d220785c094788ff9e703` on `2026-06-30T04:20:56Z`.
- Final PR99.2 head was `b1d36fba3c74ca98854a7b75243f64774dbdc289`.
- PR99.2 changes `/mcp` bearer-verification quota keying to use the trusted socket address rather than caller-controlled forwarding headers.
- Post-merge Qodo review reported two narrow follow-up issues: canonicalize equivalent trusted socket address forms and fail closed if `/mcp` bearer verification has no trusted remote address.
- MCP execution, `tools/list`, `tools/call`, provider calls, refresh tokens, production account-link lifecycle, private beta, and public launch remain blocked.

**Open items** : The next narrow app PR is PR99.3 MCP bearer quota caller-key hardening. After PR99.3, PR100 should be the authenticated MCP protocol envelope boundary.

## [2026-06-30] bug-list | MCP PR99.1 bearer verification hardening follow-up

**Agent** : Codex
**Mode** : bug-list
**Source** : PR285 merge metadata, local PR99.1 hardening branch, and user-reported post-PR99 review findings

**Pages créées** :
- `wiki/sources/2026-06-30-pr99-1-mcp-bearer-verification-hardening-bug-list.md`

**Pages mises à jour** :
- `wiki/product/chatgpt-app-sdk-roadmap.md`
- `wiki/hot.md`
- `wiki/index.md`
- `wiki/log.md`

**Points notables** :
- PR285 `PR99: add production MCP bearer-token verification boundary` merged into `application-os-foundation` as `b306ea16f48bd7cf7591370949496d0c54e83ea9` on `2026-06-30T02:09:10Z`.
- Final PR99 head was `eee8ad0e8bd0859a3dd4173d97d090ec57d0b326`.
- PR99 validates production `/mcp` bearer access tokens against digest-backed storage and returns authenticated-MCP-blocked without executing MCP.
- PR99.1 bug list covers per-caller bearer verification quota before Convex lookup, route/storage clock skew at the final proof boundary, wrong-client/wrong-resource status as `401 invalid_token`, and production authorization-server metadata for OAuth discovery.
- MCP execution, `tools/list`, `tools/call`, provider calls, refresh tokens, production account-link lifecycle, private beta, and public launch remain blocked.

**Open items** : Finish and merge PR99.1 before starting PR100. Do not start PR88/private beta/public launch from this checkpoint.

## [2026-06-29] pr-branch | MCP PR98 access-token issuance checkpoint

**Agent** : Codex
**Mode** : pr-branch
**Source** : PR284 merge result, GitHub PR metadata, local validation evidence, review-fix hardening, and post-merge checkpoint request

**Pages créées** :
- `wiki/sources/2026-06-29-pr98-mcp-oauth-access-token-issuance-checkpoint.md`

**Pages mises à jour** :
- `wiki/product/chatgpt-app-sdk-roadmap.md`
- `wiki/hot.md`
- `wiki/index.md`
- `wiki/log.md`

**Points notables** :
- PR284 `PR98: add production OAuth access-token issuance boundary` merged into `application-os-foundation` as `e1a22cb5c1a660b9fd9a8f02b76226761128ea33` on `2026-06-29T21:34:08Z`.
- Final head was `02b2ef2df6bca8e6577db183aa498ee09986c44a`.
- PR98 issues bearer access tokens for valid authorization-code token requests, persists only token digests, and atomically consumes authorization codes with token digest persistence.
- Access-token storage includes expiry metadata and cleanup; OAuth responses filter OpenID Connect identity scopes because no ID token is minted.
- Final review hardening added storage, PKCE, scope, and clock-skew proof checks.
- Validation evidence: focused route adapter tests passed with 94 tests, focused Convex auth/access-token tests passed with 15 tests, `tsc -p tsconfig.node.json --pretty false` passed from `my-app`, `git diff --check` passed, Fallow ran read-only, Semgrep passed, CodeRabbit completed, and Qodo updated to the final head.
- Codex review trigger was blocked by usage limits; GitHub `js-tests` and Playwright `test` jobs failed before executing any steps with `runner_id: 0` and empty `steps`.

**Open items** : Do not rerun PR89, PR90, PR92, PR93, PR94, PR95, PR96, PR96.1, PR97, or PR98. The next narrow app PR should be PR99 production MCP bearer-token verification boundary while MCP execution, `tools/list`, `tools/call`, provider calls, refresh tokens, account-link lifecycle, private beta, and public launch remain blocked.

## [2026-06-29] pr-branch | MCP PR96.1 redirect URI normalization checkpoint

**Agent** : Codex
**Mode** : pr-branch
**Source** : PR282 merge result, GitHub PR metadata, local validation evidence, review fix request, and post-merge checkpoint request

**Pages créées** :
- `wiki/sources/2026-06-29-pr96-1-mcp-oauth-redirect-uri-normalization-checkpoint.md`

**Pages mises à jour** :
- `wiki/product/chatgpt-app-sdk-roadmap.md`
- `wiki/hot.md`
- `wiki/index.md`
- `wiki/log.md`

**Points notables** :
- PR282 `PR96.1: normalize production OAuth redirect URI allowlist` merged into `application-os-foundation` as `08651f259c1ffa57396cb36d41163aed90dfb8a9` on `2026-06-29T15:33:18Z`.
- PR96.1 fixes the post-merge PR96 redirect URI allowlist normalization review finding.
- `MCP_OAUTH_PRODUCTION_REDIRECT_URIS` entries are canonicalized before exact login-return handoff comparison.
- Raw C0 / DEL control characters and malformed percent escapes are rejected before `new URL()` can normalize them away.
- Invalid raw redirect entries are preserved so the existing downstream boundary parser still fails closed.
- Validation evidence: focused production route adapter tests passed with 61 tests, `tsc -p tsconfig.node.json --pretty false` passed, `git diff --check` passed, Fallow passed with no introduced findings, Semgrep passed, and CodeRabbit passed.
- GitHub `js-tests` and Playwright `test` jobs failed before executing any steps; these matched the external runner availability failure pattern already seen on PR281.

**Open items** : Do not rerun PR89, PR90, PR92, PR93, PR94, PR95, PR96, or PR96.1. The next narrow app PR should remain PR97 production OAuth token endpoint / authorization-code redemption boundary while token issuance, provider calls, account-link creation, token persistence, `/mcp`, `tools/list`, and `tools/call` remain blocked.

## [2026-06-28] pr-branch | MCP PR96 production authorization-code checkpoint

**Agent** : Codex
**Mode** : pr-branch
**Source** : PR280 and PR281 merge results, GitHub PR metadata, local validation evidence, review comments, and post-merge checkpoint request

**Pages créées** :
- `wiki/sources/2026-06-28-pr96-mcp-oauth-production-authorization-code-checkpoint.md`

**Pages mises à jour** :
- `wiki/product/chatgpt-app-sdk-roadmap.md`
- `wiki/hot.md`
- `wiki/index.md`
- `wiki/log.md`

**Points notables** :
- PR280 `PR95: bind production OAuth login return continuation` merged into `application-os-foundation` as `afde4f88d9b8bff6a4afbc2bb8d3aef3d6622f95` on `2026-06-28T03:27:36Z`.
- PR281 `PR96: issue production OAuth authorization codes` merged into `application-os-foundation` as `6beeee919a1cded82a3598f785eb507c58b76436` on `2026-06-28T04:43:17Z`.
- PR96 consumes the owner-bound authorization intent, stores only digest-backed short-lived authorization-code state server-side, and redirects the browser to the validated OAuth client `redirect_uri` with `code` and original `state`.
- Raw authorization codes remain browser-only after redirect; Convex storage keeps digest-backed state with owner, client, redirect URI, resource, scopes, state, PKCE, production environment, status, timestamps, and version.
- `/oauth/token`, production `/mcp`, provider calls, consent UI, token exchange, access tokens, refresh tokens, token persistence, production account links, `tools/list`, `tools/call`, PR88/private beta, and public launch remain blocked.
- Validation evidence: focused production route/storage tests passed with 65 tests, broader OAuth/local MCP subset passed with 280 tests, `npm run build` passed, `git diff --check` passed, Semgrep passed, CodeRabbit completed, and Qodo had no blocking finding.
- GitHub `js-tests` and Playwright `test` jobs failed before starting with `runner_id: 0`, zero steps, and billing/spending-limit annotations; these were external CI availability failures.

**Open items** : Do not rerun PR89, PR90, PR92, PR93, PR94, PR95, or PR96. Do not start PR88/private beta/public launch from this checkpoint. The next narrow app PR should be PR97 production OAuth token endpoint / authorization-code redemption boundary while token issuance, provider calls, account-link creation, token persistence, `/mcp`, `tools/list`, and `tools/call` remain blocked.

## [2026-06-27] pr-branch | MCP PR94 production authorize pre-auth checkpoint

**Agent** : Codex
**Mode** : pr-branch
**Source** : PR279 merge result, GitHub PR metadata, local validation evidence, review findings, and checkpoint request

**Pages créées** :
- `wiki/sources/2026-06-27-pr94-mcp-oauth-production-authorize-preauth-checkpoint.md`

**Pages mises à jour** :
- `wiki/product/chatgpt-app-sdk-roadmap.md`
- `wiki/hot.md`
- `wiki/index.md`
- `wiki/log.md`

**Points notables** :
- PR279 `PR94: connect production /oauth/authorize to existing pre-auth intent creation` merged into `application-os-foundation` as `d9e42556a511ca5b3e78dce07f48b2366b210a0d` on `2026-06-27T21:22:08Z`.
- The final merged head was `51a1a8052afd42b9d4d1788205506d5c14210a4c`; the final pushed bug-fix head before base merge was `1d2fcc8ee151e6adbfe777871bccf10fafcdb40a`.
- PR94 connects production `/oauth/authorize` to the existing ownerless pre-auth path using PR87.17A request projection, PR87.17C3 pre-auth storage, and the continuation/login-return convention.
- `/oauth/callback` and `/mcp` remain guarded inert production handlers.
- Review fixes included Vite default dependency wiring, preview middleware, OAuth host allowlisting, local route precedence, Convex fail-closed setup, refreshed create deadlines, trimmed resource guards, caller-scoped quotas, and server-time stale-deadline rejection.
- Validation evidence: focused production route and Convex pre-auth tests passed, broader OAuth/local MCP subset passed with 215 tests, TypeScript passed, `git diff --check` passed, Fallow was advisory-only, Semgrep passed, and Qodo reported no open findings on the final bug-fix commit.
- GitHub `js-tests` remained red for the Match Review guardrail job; PR279 was merged with admin bypass after resolving the base merge conflict.

**Open items** : Do not rerun PR89, PR90, PR92, PR93, or PR94. Do not start PR88/private beta/public launch from this checkpoint. The next narrow app PR should be production login-return / owner-binding continuation while provider validation, consent, authorization-code issuance, token exchange, account-link creation, token persistence, `/mcp`, `tools/list`, and `tools/call` remain blocked.

## [2026-06-27] direct-update | MCP PR89-PR93 OAuth production gate and route shell checkpoint

**Agent** : Codex
**Mode** : direct-update
**Source** : PR274, PR275, PR276, PR277 merge results; GitHub PR metadata; local code verification; and user request

**Pages créées** :
- `wiki/sources/2026-06-27-pr89-pr93-mcp-oauth-production-gate-route-shell-checkpoint.md`

**Pages mises à jour** :
- `wiki/product/chatgpt-app-sdk-roadmap.md`
- `wiki/hot.md`
- `wiki/index.md`
- `wiki/log.md`

**Points notables** :
- PR274 `PR89: controlled MCP OAuth production activation boundary` merged into `application-os-foundation` as `a1b7c01c05a5a2288a3ae6ab97cd5320844252f8` on `2026-06-27T03:39:08Z`.
- PR275 `PR90: production OAuth operational status` merged into `application-os-foundation` as `eb703b7ebc2c8cd8149adb9fb3705cb7aee56f34` on `2026-06-27T03:45:58Z`.
- PR276 `PR92: add production MCP OAuth route preflight boundary` merged into `application-os-foundation` as `d8eafac75fb3b7cbf53ff9732a5815bb85d5fa38` on `2026-06-27T05:18:05Z`.
- PR277 `PR93: wire production MCP OAuth routes behind preflight boundary` merged into `application-os-foundation` as `d63f3144dee5260a7d350f3dfde85e00fd4c9046` on `2026-06-27T06:03:01Z`.
- PR93 production route shells for `/oauth/authorize`, `/oauth/callback`, and `/mcp` remain guarded inert handlers: no provider calls, consent, owner binding, authorization-code issuance, token exchange, account-link creation, token persistence, `tools/list`, or `tools/call`.

**Open items** : Do not rerun PR89, PR90, PR92, or PR93. Do not create PR88 retroactively. The next narrow implementation PR is PR94: connect production `/oauth/authorize` to existing pre-auth intent creation while keeping `/oauth/callback` and `/mcp` inert.

## [2026-06-27] pr-branch | MCP PR87.17D OAuth local/dev route adapter checkpoint

**Agent** : Codex
**Mode** : pr-branch
**Source** : PR273 merge result, GitHub PR metadata, local validation evidence, and checkpoint request

**Pages créées** :
- `wiki/sources/2026-06-27-pr87-17d-mcp-oauth-local-dev-route-adapter-checkpoint.md`

**Pages mises à jour** :
- `wiki/product/chatgpt-app-sdk-roadmap.md`
- `wiki/hot.md`
- `wiki/index.md`
- `wiki/log.md`

**Points notables** :
- PR273 `PR87.17D: wire local MCP OAuth route adapter` merged into `application-os-foundation` as `ece26dbf2a899b69d42343e1d1165dbc05d12d53` on `2026-06-26T21:43:32Z`.
- The final merged head was `9b23d85682a5b69d4b76904f7cd5931280fd3218` on branch `codex/pr87-17d-mcp-oauth-local-dev-route-adapter`.
- Changed files were limited to the local/dev route adapter, its focused route tests, and `vite.config.ts`.
- PR87.17D wires the local/dev-only flow: ChatGPT OAuth request -> PR265 validation -> PR271 pre-auth storage -> PR268 Clerk login return -> PR272 owner binding -> PR267 owner-bound intent -> PR269 continuation.
- Validation evidence: focused OAuth suite 222 passing, full MCP suite 1,793 passing, TypeScript clean, changed-file ESLint with `--no-ignore` clean, and `git diff --check` clean.
- GitHub Actions `js-tests` and Playwright `test` failures had `runner_id: 0` and no steps, so they are classified as external runner/billing/spending-limit availability.
- This remains local/dev-only behind `LOCAL_MCP_DEV_OAUTH_AUTHORIZATION=1`: no production MCP/OAuth endpoints, Stytch runtime integration, authorization-code issuance, token exchange, production account-link creation, PR88, or PR89.

**Open items** : Do not rerun PR87.17D. Do not start PR88 or PR89 from this checkpoint. Choose the next implementation PR only after reloading the roadmap and verifying the current lowest-numbered unmerged blocker; production MCP/OAuth/token/account-link runtime remains blocked pending a separate reviewed gate.

## [2026-06-26] direct-update | MCP PR87.17C1 OAuth login-return continuation checkpoint

**Agent** : Codex
**Mode** : direct-update
**Source** : PR269 merge result, GitHub PR metadata, and PR87.17C2 precondition

**Pages créées** :
- `wiki/sources/2026-06-26-pr87-17c1-mcp-oauth-login-return-continuation-checkpoint.md`

**Pages mises à jour** :
- `wiki/product/chatgpt-app-sdk-roadmap.md`
- `wiki/hot.md`
- `wiki/index.md`
- `wiki/log.md`

**Points notables** :
- PR269 `PR87.17C1: add MCP OAuth login return continuation boundary` merged into `application-os-foundation` as `84d6b9bab8c4f2b046f6d298eda2b329b65d52dd` on `2026-06-26T15:58:19Z`.
- The final merged head was `133efa7af3c7fe5be4feac6d7f3887321d85683b`.
- Changed files were limited to `mcpOAuthLoginReturnContinuationBoundary.ts` and its focused test.
- CodeRabbit status was `SUCCESS`; Semgrep cloud scan was `SUCCESS`.
- Remaining red checks at merge were `CI / js-tests` and `Playwright Tests / test`.
- PR87.17C1 adds route-independent prepare/resume continuation logic that reuses PR87.17A requests, PR87.17B digest-only intents, and PR87.17C0 return constants.
- This remains server-only boundary work: no route/page, Stytch call, token exchange, authorization code, account-link lifecycle invocation, production OAuth runtime, PR88, PR89, cover-letter work, or real user data.

**Open items** : Start PR87.17C2 as the next separate reviewed slice. Do not start PR87.17D, PR88, PR89, or cover-letter work from this checkpoint.

## [2026-06-26] direct-update | MCP PR87.17C0 OAuth login-return convention checkpoint

**Agent** : Codex
**Mode** : direct-update
**Source** : PR268 merge result, GitHub PR metadata, and checkpoint request

**Pages créées** :
- `wiki/sources/2026-06-26-pr87-17c0-mcp-oauth-login-return-convention-checkpoint.md`

**Pages mises à jour** :
- `wiki/product/chatgpt-app-sdk-roadmap.md`
- `wiki/hot.md`
- `wiki/index.md`
- `wiki/log.md`

**Points notables** :
- PR268 `PR87.17C0: define MCP OAuth login return convention` merged into `application-os-foundation` as `cdf3b9e95e1abad77beb7d96f9de0fcfb830f369` on `2026-06-26T03:06:46Z`.
- The final merged head was `3892163e7850e2596d7f335cae4325ceb0dd3c34`.
- CodeRabbit and Semgrep were `SUCCESS`; Qodo issue was resolved.
- Remaining red checks at merge were inherited or broader `js-tests` and Playwright lanes.
- PR87.17C0 defines repository-owned `mcp_oauth_return`, preserves `/cv` fallback, allows only the fixed local/dev MCP OAuth continuation path, requires `mcp_oauth_intent`, rejects unsafe or arbitrary return URLs, and adds focused resolver plus SignInPage wiring tests.
- This remains convention/placeholder work only: no OAuth authorization endpoint behavior, Convex changes, Stytch provider integration, MCP endpoint/runtime composition, Vite/package/lockfile changes, PR88, PR89, or cover-letter changes.

**Open items** : Start PR87.17C1 as the next separate reviewed slice. Do not start PR87.17D, PR88, PR89, or cover-letter work from this checkpoint.

## [2026-06-26] direct-update | MCP PR87.17B OAuth authorization intent storage checkpoint

**Agent** : Codex
**Mode** : direct-update
**Source** : PR267 merge result, GitHub PR metadata, and checkpoint request

**Pages créées** :
- `wiki/sources/2026-06-26-pr87-17b-mcp-oauth-authorization-intent-checkpoint.md`

**Pages mises à jour** :
- `wiki/product/chatgpt-app-sdk-roadmap.md`
- `wiki/hot.md`
- `wiki/index.md`
- `wiki/log.md`

**Points notables** :
- PR267 `PR87.17B: add MCP OAuth authorization intent storage` merged into `application-os-foundation` as `108f740a5cbcc5a75c58d0e16bd865f9e98ba169` on `2026-06-26T01:21:01Z`.
- The final merged head was `4e78cdb302eb8d9b12422db7b8668197de8f73e3`; changed files stayed within the PR-local brief, `mcpOAuthAuthorizationIntents.ts`, its focused test, and the schema change.
- PR87.17B adds the server-only one-time authorization-intent storage boundary with digest-only continuation handles and short-lived expiry.
- Raw continuation handles stay out of storage, login-return routing remains deferred, and production MCP/OAuth/public account-link API/real handlers remain blocked.

**Open items** : Start PR87.17C only as a separate explicit request and reviewed slice. Do not start PR87.17C from this checkpoint.

## [2026-06-26] direct-update | MCP PR87.17A OAuth authorization request boundary checkpoint

**Agent** : Codex
**Mode** : direct-update
**Source** : PR265 merge result, GitHub PR metadata, local validation report, and checkpoint request

**Pages créées** :
- `wiki/sources/2026-06-26-pr87-17a-mcp-oauth-authorization-request-boundary-checkpoint.md`

**Pages mises à jour** :
- `wiki/product/chatgpt-app-sdk-roadmap.md`
- `wiki/hot.md`
- `wiki/index.md`
- `wiki/log.md`

**Points notables** :
- PR265 `PR87.17A: add MCP OAuth authorization request boundary` merged into `application-os-foundation` as `1f1cb7cb46a7bfa165bbfe37f728dd2aefe44091` on `2026-06-25T23:14:46Z`.
- The final merged head was `3c7a48a8111019b08c1991ed540ff16a6a13d001`; changed files stayed within the PR-local brief, `mcpOAuthAuthorizationRequestBoundary.ts`, its focused test, and the two already-merged account-link fixups plus the PR brief.
- PR87.17A adds the server-only MCP OAuth authorization request boundary and safe intent-preservation layer after PR87.16 account-link lifecycle work.
- Local validation reported focused OAuth boundary tests, targeted ESLint, and `git diff --check` passing before merge.
- CodeRabbit status was `SUCCESS`; Semgrep cloud scan was `SUCCESS`.
- Remote `CI / js-tests` failed twice and `Playwright Tests / test` failed; `gh run view --log-failed` returned `log not found`, and the Actions job API returned empty `steps` arrays.
- This remains server-only boundary work: no production MCP, no OAuth callback/code exchange, no consent UI, no token persistence, no public account-link API, no endpoint/Vite lifecycle wiring, no real Stytch/Clerk network calls, no real user data, no outbound/model calls, no write/export/send/apply, no production flags, no billing, no PR88, and no PR89.

**Open items** : Start PR87.17B only as a separate explicit request and reviewed slice. Do not start PR87.17B from this checkpoint.

## [2026-06-25] direct-update | MCP PR87.16 account-link lifecycle checkpoint

**Agent** : Codex
**Mode** : direct-update
**Source** : PR264 merge result, GitHub PR metadata, local validation report, and checkpoint request

**Pages créées** :
- `wiki/sources/2026-06-25-pr87-16-mcp-account-link-lifecycle-checkpoint.md`

**Pages mises à jour** :
- `wiki/product/chatgpt-app-sdk-roadmap.md`
- `wiki/hot.md`
- `wiki/index.md`
- `wiki/log.md`

**Points notables** :
- PR264 `PR87.16: add authoritative MCP account-link lifecycle` merged into `application-os-foundation` as `ba62200d28deaae56387e06fd13e20aea580758d` on `2026-06-25T18:26:13Z`.
- The final merged head was `1a3a94821b0d5409db64b88d5a7d500672c09b22`; changed files stayed within the PR-local brief, `mcpAccountLinks.ts`, and its focused Convex test.
- PR87.16 adds server-only canonical account-link link, refresh, and revoke lifecycle operations using already-verified OAuth evidence plus trusted Twoweeks owner context.
- Local validation passed focused lifecycle tests, adjacent auth/runtime tests, full local-MCP suite, full Convex test scope, TypeScript, targeted ESLint, build, diff checks, forbidden-surface grep, and Fallow advisory review.
- CodeRabbit status was `SUCCESS`; Semgrep was `SUCCESS`; the latest CodeRabbit review also recorded one minor test-tightening suggestion on the final head.
- Remote `CI / js-tests` failed twice and `Playwright Tests / test` failed; failed logs were unavailable through `gh run view --log-failed`, and the Actions job API returned empty `steps` arrays.
- This remains server-only lifecycle work: no production MCP, no OAuth callback/code exchange, no consent UI, no token persistence, no public account-link API, no endpoint/Vite lifecycle wiring, no provider/Clerk network calls, no real user data, no outbound/model calls, no write/export/send/apply, no production flags, no billing, no PR88, and no PR89.

**Open items** : Start PR87.17A only as a separate explicit request and reviewed slice. Do not start PR87.17A/PR87.17 from this checkpoint.

## [2026-06-25] direct-update | MCP PR87.15D local/dev auth runtime wiring checkpoint

**Agent** : Codex
**Mode** : direct-update
**Source** : PR263 merge result, GitHub PR metadata, local validation report, and checkpoint request

**Pages créées** :
- `wiki/sources/2026-06-25-pr87-15d-mcp-auth-local-runtime-wiring-checkpoint.md`

**Pages mises à jour** :
- `wiki/product/chatgpt-app-sdk-roadmap.md`
- `wiki/hot.md`
- `wiki/index.md`
- `wiki/log.md`

**Points notables** :
- PR263 `PR87.15D: wire composed auth into local/dev MCP runtime` merged into `application-os-foundation` as `97b8faa9c326868a298ed73d4357d03bdaf7ec47` on `2026-06-25T06:56:04Z`.
- The final merged head was `6faf7cd8f66134eb81a6d34bec8f21510a210773`; changed files stayed within the PR-local brief, local-MCP auth runtime module/tests, `tsconfig.node.json`, and `vite.config.ts`.
- The runtime wiring reuses PR87.15C auth composition, PR87.15B1 lookup adapter, PR87.15A verifier, PR87.14B local/dev challenge wiring, PR87.14A orchestrator, and PR87.13 policy/resolver boundaries.
- Local validation passed focused PR87.15D tests, adjacent auth tests, full local-MCP suite, relevant Convex guardrail tests, TypeScript, targeted ESLint, build, diff checks, forbidden-surface grep, and Fallow advisory review.
- CodeRabbit and Semgrep were green before merge. GitHub CI/Playwright stayed red with unavailable logs and empty job steps after rerun, so PR263 was admin-squash-merged.
- This remains local/dev runtime auth wiring only: no production MCP, no OAuth callback/code exchange, no real Stytch runtime call, no account-link lifecycle mutation, no public Convex function, no real handlers, no real user data, no outbound/model calls, no write/export/send/apply, no production flags, no billing, no PR88, and no PR89.

**Open items** : Run Gate87.16A MCP Inspector local authentication smoke next. Do not start PR87.16 account-link lifecycle work unless Gate87.16A returns green.

## [2026-06-25] direct-update | MCP PR87.15C auth composition checkpoint

**Agent** : Codex
**Mode** : direct-update
**Source** : PR261 merge result, GitHub PR metadata, and local fetch/source verification from `neyssan-new`

**Pages créées** :
- `wiki/sources/2026-06-25-pr87-15c-mcp-auth-composition-checkpoint.md`

**Pages mises à jour** :
- `wiki/product/chatgpt-app-sdk-roadmap.md`
- `wiki/hot.md`
- `wiki/index.md`
- `wiki/log.md`

**Points notables** :
- PR261 `PR87.15C: compose Stytch verification and account-link lookup for local/dev MCP auth` merged into `application-os-foundation` as `f161ae9302269e5944101dd65ec4e375c112c070`.
- The final merged head was `ccc4fe7469d17e62e8ec400288e45c4243679d94`; changed files stayed exactly `mcpAuthCompositionBoundary.ts` and `mcpAuthCompositionBoundary.test.ts`.
- The composition boundary uses the PR257 verifier, PR259 lookup adapter, PR254 policy/resolver, and PR255 orchestrator dependency ports; it exports endpoint dependency output for a later runtime wiring slice.
- The CodeRabbit P2 malformed-JWKS fix was included before merge; malformed, empty, private, non-RSA, duplicate-`kid`, or otherwise unacceptable JWKS fails closed before `configured: true`.
- Local validation passed focused composition tests, adjacent verifier/orchestrator tests, the full local-MCP suite, TypeScript, targeted ESLint, build, diff checks, and forbidden-surface checks.
- CodeRabbit reported success before merge. GitHub CI and Playwright checks were red at merge time with unavailable logs, and the PR was admin-squash-merged.
- This remains a composition boundary only: no endpoint wiring, no Vite middleware wiring, no production MCP, no real OAuth/Stytch runtime calls, no account-link creation or mutation, no public Convex auth surface, no real handlers, no outbound/model calls, no write/export/send/apply, no production flags, no billing, no PR88, and no PR89.

**Open items** : PR87.15D may wire the composed auth dependencies into the local/dev Vite MCP runtime, preserving existing default, anonymous, and deny-all modes. Do not mutate this checkpoint after PR87.15D implementation begins.

## [2026-06-25] direct-update | MCP PR87.15B1 account-link lookup adapter checkpoint

**Agent** : Codex
**Mode** : direct-update
**Source** : PR259 merge result, GitHub PR metadata, and local fetch/source verification from `neyssan-new`

**Pages créées** :
- `wiki/sources/2026-06-25-pr87-15b1-mcp-account-link-lookup-adapter-checkpoint.md`

**Pages mises à jour** :
- `wiki/product/chatgpt-app-sdk-roadmap.md`
- `wiki/hot.md`
- `wiki/index.md`
- `wiki/log.md`

**Points notables** :
- PR259 `PR87.15B1: add server-only MCP account-link lookup adapter` merged into `application-os-foundation` as `732bef170fd4175cb70cd2f0cc1bda858f2e93bb`.
- The merged head was `4bc277f28253ffe8411160615d8af68f7cdd4b95`; changed files stayed exactly `mcpAccountLinks.ts`, `mcpAccountLinks.test.ts`, `mcpConvexAccountLinkLookupAdapter.ts`, and `mcpConvexAccountLinkLookupAdapter.test.ts`.
- The adapter exposes `buildMcpConvexAccountLinkLookupAdapter` with an injected `runQuery` and opaque `queryRef`; the bounded Convex query is `internalLookupMcpAuthPolicyAccountLinkCandidates`.
- GitHub reported `js-tests`, `test`, and CodeRabbit success; local fetch, ancestry, changed-file, and source-symbol checks were verified before this checkpoint.
- This remains server-only lookup-adapter work: no endpoint wiring, no Vite middleware wiring, no runtime verifier wiring, no production MCP, no real OAuth/Stytch runtime calls, no account-link mutation, no real handlers, no outbound/model calls, no write/export/send/apply, no production flags, no billing, no PR88, and no PR89.

**Open items** : PR87.15C may compose the merged non-production auth pieces with deterministic synthetic fixtures, but must not mutate this checkpoint after implementation begins or open production MCP behavior.

## [2026-06-25] direct-update | MCP PR87.15B0 account-link canonical storage checkpoint

**Agent** : Codex
**Mode** : direct-update
**Source** : PR258 merge result, GitHub PR metadata, and local fetch verification from `neyssan-new`

**Pages créées** :
- `wiki/sources/2026-06-25-pr87-15b0-mcp-account-link-canonical-storage-checkpoint.md`

**Pages mises à jour** :
- `wiki/product/chatgpt-app-sdk-roadmap.md`
- `wiki/hot.md`
- `wiki/index.md`
- `wiki/log.md`

**Points notables** :
- PR258 `PR87.15B0: add MCP canonical account-link storage contract` merged into `application-os-foundation` as `06a76a0b5f87f0d30c24635c436cfe3ffa80b29a`.
- The merged head was `7c6ccc30c55334570da2da3d279f13920033a915`; changed files stayed exactly `schema.ts`, `mcpAccountLinks.ts`, and `mcpAccountLinks.test.ts`.
- The canonical contract adds optional issuer, provider environment, canonical granted scopes, expiry, canonical version, classification/projection helpers, and index `by_provider_issuer_subject_environment`.
- Reported validation included focused Convex account-link tests passing 24/24, full local-MCP suite passing 59 files / 1377 tests, TypeScript passing, targeted ESLint passing, build passing with existing warnings only, Fallow passing, and diff checks passing.
- This remains storage/index only: no final lookup adapter, no endpoint wiring, no Vite middleware change, no runtime verifier wiring, no production MCP, no OAuth callback/token exchange, no account-link creation or mutation, no real handlers, no outbound/model calls, no write/export/send/apply, no production flags, no billing, no PR88, and no PR89.

**Open items** : PR87.15B1 may add the server-only lookup adapter as a separate reviewed slice, but must not wire runtime auth or production MCP behavior.

## [2026-06-25] direct-update | MCP PR87.15A Stytch bearer verifier boundary checkpoint

**Agent** : Codex
**Mode** : direct-update
**Source** : PR257 merge result, GitHub PR metadata, CodeRabbit status, and local fetch verification from `neyssan-pr87-15a-mcp-stytch-verifier-boundary`

**Pages créées** :
- `wiki/sources/2026-06-25-pr87-15a-mcp-stytch-bearer-verifier-checkpoint.md`

**Pages mises à jour** :
- `wiki/product/chatgpt-app-sdk-roadmap.md`
- `wiki/hot.md`
- `wiki/index.md`
- `wiki/log.md`

**Points notables** :
- PR257 `PR87.15A: add MCP Stytch bearer verifier boundary` merged into `application-os-foundation` as `372d16830dd6d3b66f39ba96e317641dcb207793`.
- The final merged head was `00172f63a8a49d28756150e611a5371d615f2de3` after CodeRabbit fixes; changed files stayed limited to `mcpStytchBearerVerifierBoundary.ts` and its focused test.
- Focused verifier tests passed 38/38; adjacent Stytch/OAuth/orchestrator/policy suites passed 188/188; the full local-MCP suite passed 59 files / 1377 tests; typecheck, targeted ESLint, diff checks, GitHub checks, and latest CodeRabbit no-actionable review were verified before merge.
- `npm run build` still fails only on inherited Convex `_generated` baseline errors; filtered output had no local-MCP or verifier hits.
- This remains a server-only verifier boundary: production MCP endpoints, runtime verifier wiring, production `tools/list`/`tools/call`, OAuth callback/token exchange, real Stytch runtime calls, remote JWKS fetch, token persistence, real handlers, real data, outbound/model calls, live submit/apply, approved-answer copy, billing, PR88, and PR89 remain blocked.

**Open items** : The next MCP slice must be a separate explicit request and separately reviewed PR before any runtime wiring.

## [2026-06-24] direct-update | MCP PR87.14B local/dev auth endpoint wiring checkpoint

**Agent** : Codex
**Mode** : direct-update
**Source** : PR256 merge result, GitHub PR metadata, CodeRabbit status, and local fetch verification from `neyssan-pr87-14b-mcp-auth-dev-endpoint-wiring`

**Pages créées** :
- `wiki/sources/2026-06-24-pr87-14b-mcp-auth-dev-endpoint-wiring-checkpoint.md`

**Pages mises à jour** :
- `wiki/product/chatgpt-app-sdk-roadmap.md`
- `wiki/hot.md`
- `wiki/index.md`
- `wiki/log.md`

**Points notables** :
- PR256 merged into `application-os-foundation` as merge commit `4a98a97387b6675eb7d27f632434f390462f2d40`.
- The reviewed head was `7dbce814ccc851ac7d588dd98143b5b5b25925e5`.
- The changed files stayed exactly `localMcpDevEndpoint.test.ts`, `localMcpDevAuthConfig.ts`, `localMcpDevEndpoint.ts`, `tsconfig.node.json`, and `vite.config.ts`.
- GitHub checks were green: CodeRabbit, `js-tests`, and `test`.
- Reported validation included focused endpoint tests passing 22/22, full local-MCP suite passing 58 files / 1339 tests, TypeScript passing, targeted ESLint passing, Vite HTTP smoke passing, injected fake verifier/account-link smoke passing, and forbidden-surface grep passing.
- `npm run build` remained red only on inherited Convex `_generated` baseline errors, with no PR256 changed-file hits and no prior TS6307/sync/readonly errors.
- This remains local/dev only: no production `/mcp`, no production `tools/list` or `tools/call`, no real Stytch bearer verification, no OAuth callback/token exchange, no Convex/Clerk/Stytch runtime, no outbound HTTP/model calls, no cover-letter work, no PR88, and no PR89.

**Open items** : PR87.15A must remain a separate reviewed slice; it must not be treated as started by this checkpoint.

## [2026-06-24] direct-update | MCP PR87.14A auth request orchestrator checkpoint

**Agent** : Codex
**Mode** : direct-update
**Source** : PR255 merge result, GitHub PR metadata, and local fetch verification from `neyssan-new`

**Pages créées** :
- `wiki/sources/2026-06-24-pr87-14a-mcp-auth-request-orchestrator-checkpoint.md`

**Pages mises à jour** :
- `wiki/product/chatgpt-app-sdk-roadmap.md`
- `wiki/hot.md`
- `wiki/index.md`
- `wiki/log.md`

**Points notables** :
- PR255 `PR87.14A: add MCP auth request orchestrator boundary` merged into `application-os-foundation` as `01aae0571b671f7b66141dbaff3796886c7186ad`.
- The reviewed head was `36531ae971931e37985b71bb00eac33190300e3a`; changed files stayed exactly `mcpAuthRequestOrchestrator.ts` and `mcpAuthRequestOrchestrator.test.ts`.
- GitHub reported CI, Playwright Tests, and CodeRabbit success before merge.
- Reported validation included focused orchestrator tests passing 41/41, full local-MCP suite passing 58 files / 1331 tests, TypeScript passing, targeted ESLint passing, `git diff --check` passing, and forbidden-surface guards passing.
- This remains a boundary checkpoint only: no endpoint wiring, no production MCP, no runtime OAuth, no real Stytch verifier, no Clerk/Convex runtime lookup, no account persistence, no real data, no outbound HTTP/model calls, no live submit/apply, no approved-answer copy, no billing, no PR88, and no PR89.

**Open items** : PR87.14B may wire the orchestrator into the local/dev fixture endpoint only, preserving default-off, fixture-only, and runtime deny-all behavior.

## [2026-06-24] direct-update | MCP PR87.10 test-only reachability checkpoint

**Agent** : Codex
**Mode** : direct-update
**Source** : PR251 merge result and local verification from `neyssan-new`

**Pages créées** :
- `wiki/sources/2026-06-24-pr87-10-mcp-dev-endpoint-blocked-reachability-checkpoint.md`

**Pages mises à jour** :
- `wiki/hot.md`
- `wiki/index.md`
- `wiki/log.md`

**Points notables** :
- PR251 merged into `application-os-foundation` at `1f121b008296fb47cc13519595e9e0ac0c2e0637`; head SHA was `ac72565de07ae8fd13f70cf0dcd01643fd72d03a`.
- The changed file stayed test-only: `my-app/src/modules/local-mcp/__tests__/localMcpDevEndpoint.test.ts`.
- Focused endpoint tests were reported as passed: 13 tests.
- Broader local-MCP tests were reported as passed: 56 files, 1197 tests.
- `git diff --check application-os-foundation...HEAD` was clean and `git diff --name-only application-os-foundation...HEAD` showed exactly one file.
- The checkpoint proves the local/dev MCP endpoint remains default-off, loopback-only, JSON-only, bounded by request size, fixture-only for `initialize` and `tools/list`, and blocked for `tools/call`.
- No production MCP, OAuth, real handlers, outbound HTTP, model calls, live submit/apply, approved-answer production behavior, `provider_verified_submitted`, billing, PR88, or PR89 behavior changed.

**Open items** : the next MCP slice should be the auth/OAuth architecture decision, not runtime exposure.

## [2026-06-24] direct-update | MCP PR87.11 auth/account-linking architecture checkpoint

**Agent** : Codex
**Mode** : direct-update
**Source** : PR252 merge result and local verification from `neyssan-pr87-11-mcp-auth-account-linking-architecture`

**Pages créées** :
- `wiki/sources/2026-06-24-pr87-11-mcp-auth-account-linking-architecture-checkpoint.md`

**Pages mises à jour** :
- `wiki/hot.md`
- `wiki/index.md`
- `wiki/log.md`

**Points notables** :
- PR252 merged into `application-os-foundation` at `d9b47c72dd68dd388561b6c71d50d5952742c761`; head SHA was `7d7008c2943986c6b4c8d56f816c9381ffd79a05`.
- The changed files stayed docs-only: `docs/decisions/2026-06-24-chatgpt-app-mcp-auth-account-linking-architecture.md` and `docs/audits/2026-06-24-mcp-app-sdk-production-gate-blocker-register.md`.
- GitHub checks were green: CI success, Playwright Tests success, CodeRabbit success.
- The CodeRabbit wording nit in the ADR status banner was fixed before merge and the review thread resolved.
- The checkpoint records Clerk as the app login authority, Stytch Connected Apps as the OAuth bridge, `(issuer, subject)` account linking, and `twoweeks:applications:read` as the first external scope.
- Production MCP, runtime OAuth, production `tools/list`, production `tools/call`, real handlers, PR88, and PR89 remain blocked.

**Open items** : none. This checkpoint has been published and verified on `origin/main`.

## [2026-06-23] direct-update | cover-letter PR249 staged internal gate

**Agent** : Codex
**Mode** : direct-update
**Source** : user release-recorder checkpoint; local post-merge gate report from `neyssan-new`

**Pages créées** :
- `wiki/sources/2026-06-23-cover-letter-quality-pr249-staged-internal-gate.md`

**Pages mises à jour** :
- `wiki/tasks/2026-06-22-cover-letter-quality-production-roadmap.md`
- `wiki/index.md`
- `wiki/hot.md`
- `wiki/log.md`

**Points notables** :
- PR249 is merged into `application-os-foundation` by squash merge at `d628bed79c0063d2c06c836015e87d313385bbd2`; head SHA was `11f56d5e44b24db8b3a479cff0bee76c24974b05`.
- GitHub checks before merge reported `CI` success and `Playwright Tests` success.
- Local post-merge base was `application-os-foundation` at `d628bed79c0063d2c06c836015e87d313385bbd2`; local app status after the gate was clean except pre-existing untracked `docs/plans/2026-06-22-cover-letter-quality-production-roadmap.md`.
- Targeted proposal tests passed: 2 files, 282 tests. Full proposal test directory passed: 20 files, 581 tests. `git diff --check` was clean.
- Expanded staged internal gate reported 23 total cases, 19 PASS, 4 SKIPPED only because no committed French CV-backed fixtures existed, 0 FAIL.
- PR246 forbidden extrapolation hits: none. PR248 no-CV leakage hits: none. Unsupported claim examples: none found.
- Decision recorded: `COVER_LETTER_MISTRAL_V2_READY_FOR_INTERNAL_STAGING_ONLY`.
- Production full GO is not approved. Quality repair remains OFF. Qwen remains legacy-only with `enteringPremiumAttempt=false`. GPT remains unchanged. MCP/App SDK work remains separate.

**Open items** : internal/staging-only rollout readiness may proceed under the recorded gate; production full GO, quality repair, Qwen premium, GPT changes, and MCP/App SDK work require separate decisions.

## [2026-06-23] direct-update | cover-letter PR248 merge checkpoint

**Agent** : Codex
**Mode** : direct-update
**Source** : user merge checkpoint; local git verification in `neyssan-new`

**Pages créées** :
- `wiki/sources/2026-06-23-cover-letter-quality-pr248-merge-checkpoint.md`

**Pages mises à jour** :
- `wiki/tasks/2026-06-22-cover-letter-quality-production-roadmap.md`
- `wiki/index.md`
- `wiki/hot.md`
- `wiki/log.md`
- `/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan-new/docs/plans/2026-06-22-cover-letter-quality-production-roadmap.md`

**Points notables** :
- PR248 is merged by squash merge at `2fd7ebef142859fb089bf8e9d270bf6b5b590fa1`; expected head `fd478470525942caacbec12d01cdcb39d2688c22` matched.
- Local diff verification shows two files changed: `premiumCoverLetter.ts` and `premiumCoverLetter.test.ts`.
- PR248 tightened the Mistral V2 no-CV candidate-history boundary and reports `READY_FOR_STAGED_INTERNAL_MISTRAL_V2_EXPANSION`.
- Quality repair remains OFF / NO-GO and production full GO remains a separate later decision.

**Open items** : run post-merge verification from `2fd7ebef142859fb089bf8e9d270bf6b5b590fa1`; if clean, proceed to the staged internal Mistral V2 expansion/evidence gate.

## [2026-06-23] direct-update | PR246 merge SHA correction

**Agent** : Codex
**Mode** : direct-update
**Source** : local git verification in `neyssan-new`

**Pages mises à jour** :
- `wiki/tasks/2026-06-22-cover-letter-quality-production-roadmap.md`
- `wiki/sources/2026-06-23-cover-letter-quality-pr246-merge-checkpoint.md`
- `wiki/log.md`

**Points notables** :
- Corrected the PR246 merge commit from invalid `8375257fea4799fef29a97db76e8b90b276cf` to verified `8375257fea4799fef29a97db76b58e0b90b276cf`.
- The roadmap decision did not change: internal Mistral V2 canary expansion remains GO; quality repair and production remain NO-GO.

**Open items** : run the limited internal Mistral V2 expansion from the verified merge baseline.

## [2026-06-23] direct-update | cover-letter PR246 merge and post-merge canary

**Agent** : Codex
**Mode** : direct-update
**Source** : user checkpoint / attachment text

**Pages créées** :
- `wiki/sources/2026-06-23-cover-letter-quality-pr246-merge-checkpoint.md`

**Pages mises à jour** :
- `wiki/tasks/2026-06-22-cover-letter-quality-production-roadmap.md`
- `wiki/index.md`
- `wiki/hot.md`
- `wiki/log.md`

**Points notables** :
- PR246 is now merged into `application-os-foundation` and the roadmap doc stayed out of the PR diff.
- Post-merge Mistral V2 internal/no-DB canary is clean and internal canary expansion is GO.
- Quality repair remains OFF / NO-GO and production full GO remains a separate later decision.

**Open items** : keep using the merged PR246 checkpoint as the source of truth and treat the earlier draft/review state as historical.

## [2026-06-23] direct-update | PR246 draft review gate checkpoint

**Agent** : Codex
**Mode** : direct-update
**Source** : user checkpoint; local branch check in `neyssan-new`

**Pages mises à jour** :
- `wiki/tasks/2026-06-22-cover-letter-quality-production-roadmap.md`
- `wiki/index.md`
- `wiki/hot.md`
- `wiki/log.md`
- `/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan-new/docs/plans/2026-06-22-cover-letter-quality-production-roadmap.md`

**Points notables** :
- PR246 is now tracked as draft/open and ready for real review, not as unimplemented work.
- The reported PR246 implementation completed the Mistral V2 factuality tightening, regression coverage for `standardizing component usage and versioning`, targeted tests, and internal/no-DB canary rerun.
- Internal Mistral V2 canary expansion is conditional GO only after clean review, merge, and post-merge canary rerun.
- Quality repair remains OFF / NO-GO and full production remains NO-GO.

**Verification** :
- Local branch check reported `codex/pr246-mistral-v2-factuality-tightening`.
- `gh` is not installed in this worktree, so GitHub PR draft state was not independently queried from the shell.

**Open items** : review the real PR246 diff, merge only if clean, then rerun targeted tests and the same internal/no-DB Mistral V2 canary post-merge.

## [2026-06-23] direct-update | clarify PR80B manual handoff implementation state

**Agent** : Codex
**Mode** : direct-update
**Source** : code check in `neyssan-new`

**Pages mises à jour** :
- `wiki/product/manual-application-handoff.md`
- `wiki/product/chatgpt-app-sdk-roadmap.md`
- `wiki/index.md`
- `wiki/hot.md`
- `wiki/log.md`

**Points notables** :
- Confirmed PR80B manual handoff is implemented in `my-app/convex/manualApplicationHandoff.ts` and tested by `my-app/convex/__tests__/manualApplicationHandoff.test.ts`.
- Reframed the manual handoff checklist as operational guardrails, not remaining initial implementation.
- Preserved the blocked status for PR80-live submit/apply, approved answer copy, and provider-verified submission.

**Verification** :
- `rtk npx vitest run convex/__tests__/manualApplicationHandoff.test.ts` passed: 26 tests.

**Open items** : none for PR80B initial implementation; PR87.8 and PR80-live remain separate MCP/App SDK roadmap items.

## [2026-06-23] direct-update | split cover-letter quality from MCP/App SDK roadmap

**Agent** : Codex
**Mode** : direct-update
**Source** : user request to prevent roadmap collapse and clarify remaining work

**Pages mises à jour** :
- `wiki/tasks/2026-06-22-cover-letter-quality-production-roadmap.md`
- `wiki/product/chatgpt-app-sdk-roadmap.md`
- `wiki/product/manual-application-handoff.md`
- `wiki/index.md`
- `wiki/hot.md`
- `wiki/log.md`
- `/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan-new/docs/plans/2026-06-22-cover-letter-quality-production-roadmap.md`

**Points notables** :
- Cover-letter quality now explicitly owns PR246 Mistral V2 factuality tightening only; MCP/App SDK, manual handoff, OAuth, tools, launch gates, and production App SDK work are out of scope.
- ChatGPT/App SDK now has its own remaining checklist: PR87.8 production-gate reconciliation first, with PR88 private beta and PR89 public launch still blocked.
- Manual handoff now has its own PR80B checklist and keeps live submit/apply plus `provider_verified_submitted` blocked.
- The local code-adjacent cover-letter plan was synchronized from stale PR1-PR4 wording to the PR246-only checklist.
- `hot.md` was reduced to a short routing cache so future sessions read the correct canonical page for each workstream.

**Open items** : if new source files arrive in `rawinput/`, run ingest again and route each fact into the correct workstream.

## [2026-06-23] ingest | cover-letter checklist, ChatGPT/App SDK roadmap, and manual handoff planning

**Agent** : Codex
**Mode** : ingest
**Fichiers traités** :
- `rawinput/Cover Letter Quality Production Roadmap — Updated Checklist.md`
- `rawinput/Roadmap Twoweeks ChatGPTApp SDK — PR41 à PR89.md`
- `rawinput/PR80B — Safe Application Handoff While ATS Authorization Is Pending.md`

**Pages créées** :
- `wiki/sources/2026-06-23-cover-letter-quality-production-roadmap-updated-checklist.md`
- `wiki/sources/2026-06-12-chatgpt-app-sdk-roadmap-pr41-pr89.md`
- `wiki/sources/2026-06-19-pr80b-safe-application-handoff-while-ats-access-pending.md`
- `wiki/sources/2026-06-23-twoweeks-mcp-chatgpt-app-sdk-roadmap-checkpoint.md`
- `wiki/product/chatgpt-app-sdk-roadmap.md`
- `wiki/product/manual-application-handoff.md`

**Pages mises à jour** :
- `wiki/tasks/2026-06-22-cover-letter-quality-production-roadmap.md`
- `wiki/product/chatgpt-app-sdk-roadmap.md`
- `wiki/product/manual-application-handoff.md`
- `wiki/index.md`
- `wiki/hot.md`
- `wiki/log.md`

**Points notables** :
- The cover-letter roadmap is now the PR246 hold / factuality-tightening checklist after PR230-PR245 and the first Mistral V2 canary.
- The ChatGPT/App SDK track is now at PR87 production-gate reconciliation after PR245, with PR80B manual handoff current and PR88/PR89 blocked.
- The staged files were moved to `raw/` and `rawinput/` now returns to `README.md` only.

**Open items** : none

## [2026-06-22] direct-update | cover letter quality production roadmap

**Agent** : Codex
**Mode** : direct-update
**Source** : explicit user instruction from neyssan-new code review

**Pages créées** :
- wiki/tasks/2026-06-22-cover-letter-quality-production-roadmap.md

**Pages mises à jour** :
- wiki/index.md
- wiki/log.md
- wiki/hot.md

**Points notables** :
- Tracked roadmap PR 1 -> PR 4 for cover-letter quality and production readiness.
- PR 1 is constrained to premium provenance finalization with no naive candidateFactIds bypass.
- Local implementation mirror: neyssan-new/docs/plans/2026-06-22-cover-letter-quality-production-roadmap.md.

**Open items** : execute PR 1 on branch codex/premium-provenance-finalization.

## [2026-06-12] ingest | chatgpt apps sdk exploration and roadmap staging

**Agent** : Codex
**Mode** : ingest
**Fichiers traités** :
- `rawinput/PR35 - Non-production Apps SDK Exploration Plan.md`
- `rawinput/Roadmap.md`

**Pages créées** :
- `wiki/sources/2026-06-12-chatgpt-apps-sdk-roadmap-pr35.md`
- `wiki/sources/2026-06-12-non-production-apps-sdk-exploration-plan.md`

**Pages mises à jour** :
- `wiki/index.md`
- `wiki/log.md`
- `wiki/hot.md`

**Points notables** :
- Les deux sources staged ont été ingérées en tant que documentation de planning Apps SDK.
- PR35 a confirmé le mode "docs-only + bounded constraints" et a défini un prochain ordre de PR conservateur.
- Les fichiers source ont été déplacés vers `raw/` pour l'immutabilité.

**Open items** : none

## [2026-06-12] ingest | chatgpt app end-to-end safety audit

**Agent** : Codex
**Mode** : ingest
**Fichiers traités** :
- `rawinput/PR30 - ChatGPT App End-to-end Safety Audit.md`

**Pages créées** :
- `wiki/sources/2026-06-11-chatgpt-app-end-to-end-safety-audit.md`

**Pages mises à jour** :
- `wiki/index.md`
- `wiki/log.md`
- `wiki/hot.md`

**Points notables** :
- PR30 a été ingéré comme source d'audit docs-only de sécurité de chaîne PR18–PR29 pour la phase non-production.
- Source locale `rawinput/PR30 - ChatGPT App End-to-end Safety Audit.md` déplacée vers `raw/` pour immutabilité.
- `wiki/index.md` et `wiki/hot.md` ont été alignés avec la chaîne `readiness -> safety audit -> non-production -> manifest`.

**Open items** : none

## [2026-06-12] ingest | chatgpt-app non-production prototype and manifest draft

**Agent** : Codex
**Mode** : ingest
**Fichiers traités** :
- `rawinput/PR28 - Non-production ChatGPT App Prototype Plan.md`
- `rawinput/PR29 - Local-only ChatGPT App Manifest Draft.md`

**Pages créées** :
- `wiki/sources/2026-06-11-chatgpt-app-non-production-prototype-plan.md`
- `wiki/sources/2026-06-11-chatgpt-app-local-only-manifest-draft.md`

**Pages mises à jour** :
- `wiki/index.md`
- `wiki/log.md`
- `wiki/hot.md`

**Points notables** :
- Les deux notes staging ont été ingérées comme sources pour plan/manifest ChatGPT App non-production.
- Les fichiers sources ont été déplacés vers `raw/` pour immutabilité.
- `wiki/index.md` mis à jour avec les nouvelles sources et date de mise à jour.
- `wiki/log.md` consigne les fichiers traités et les artefacts créés.

---

## [2026-06-11] ingest | application-os execution notes and readiness inputs

**Agent** : Codex
**Mode** : ingest
**Fichiers traités** :
- `rawinput/Audit architecture — Application OS PR1 à PR17.md`
- `rawinput/CV Forge Save  Restore Pipeline Fix.md`
- `rawinput/FUTURE TWO WEEKS AGENTS READY.md`
- `rawinput/MCP  ChatGPT App Readiness Spec.md`
- `rawinput/cv persistence .md`
- `rawinput/emojis library .md`
- `rawinput/master architecture decision doc v1.md`
- `rawinput/oddyseo pietro schirano writing tool.md`
- `rawinput/.md` (empty placeholder)

**Pages créées** :
- `wiki/sources/2026-06-11-audit-architecture-application-os-pr1-pr17.md`
- `wiki/sources/2026-06-11-cv-forge-save-restore-pipeline-fix.md`
- `wiki/sources/2026-06-11-future-two-weeks-agents-ready.md`
- `wiki/sources/2026-06-11-mcp-chatgpt-app-readiness-spec.md`
- `wiki/sources/2026-06-11-cv-hydration-and-style-system.md`
- `wiki/sources/2026-06-11-emojis-library.md`
- `wiki/sources/2026-06-11-master-architecture-decision-doc-v1.md`
- `wiki/sources/2026-06-11-oddyseo-pietro-schirano-writing-tool.md`

**Pages mises à jour** :
- `wiki/index.md`
- `wiki/log.md`
- `wiki/hot.md`
- `wiki/sources/2026-06-11-audit-architecture-application-os-pr1-pr17.md`
- `wiki/sources/2026-06-11-cv-forge-save-restore-pipeline-fix.md`
- `wiki/sources/2026-06-11-future-two-weeks-agents-ready.md`
- `wiki/sources/2026-06-11-mcp-chatgpt-app-readiness-spec.md`
- `wiki/sources/2026-06-11-cv-hydration-and-style-system.md`
- `wiki/sources/2026-06-11-emojis-library.md`
- `wiki/sources/2026-06-11-master-architecture-decision-doc-v1.md`
- `wiki/sources/2026-06-11-oddyseo-pietro-schirano-writing-tool.md`

**Points notables** :
- `rawinput/README.md` n’est pas traité.
- Les 9 fichiers de stage restants ont été déplacés vers `raw/` (incluant le fichier vide `rawinput/.md`).
- `wiki/index.md` et `wiki/hot.md` ont été mis à jour avec les nouvelles entrées sources.

---

## [2026-06-09] direct-update | Kanban dasti — run.sh exploitation improvements

**Agent** : Codex
**Pages mises à jour** :
- `wiki/tasks/Kanban - dasti.md`
- `wiki/log.md`
**Notes de cards créées** :
- `wiki/tasks/Kanban_CardNotes/Documentation et audit de run.sh — 13.1 Priorité haute — Charger explicitement my-app-.env.local au démarrage..md`
- `wiki/tasks/Kanban_CardNotes/Documentation et audit de run.sh — 13.1 Priorité haute — Remplacer kill -9 par une stratégie progressive..md`
- `wiki/tasks/Kanban_CardNotes/Documentation et audit de run.sh — 13.1 Priorité haute — Ajouter une commande logs-all..md`
- `wiki/tasks/Kanban_CardNotes/Documentation et audit de run.sh — 13.1 Priorité haute — Ajouter des fonctions standardisées de log..md`
- `wiki/tasks/Kanban_CardNotes/Documentation et audit de run.sh — 13.1 Priorité haute — Pinner l'image cloudflare-cloudflared..md`
- `wiki/tasks/Kanban_CardNotes/Documentation et audit de run.sh — 13.1 Priorité haute — Séparer clairement les modes développement et production..md`
- `wiki/tasks/Kanban_CardNotes/Documentation et audit de run.sh — 13.1 Priorité haute — Ajouter des préchecks bloquants pour la production..md`
- `wiki/tasks/Kanban_CardNotes/Documentation et audit de run.sh — 13.2 Priorité moyenne — Extraire les blocs Node inline dans des scripts dédiés..md`
- `wiki/tasks/Kanban_CardNotes/Documentation et audit de run.sh — 13.2 Priorité moyenne — Ajouter une option --dry-run..md`
- `wiki/tasks/Kanban_CardNotes/Documentation et audit de run.sh — 13.2 Priorité moyenne — Renforcer le parsing .env..md`
- `wiki/tasks/Kanban_CardNotes/Documentation et audit de run.sh — 13.2 Priorité moyenne — Rendre le nettoyage Vite plus ciblé..md`
- `wiki/tasks/Kanban_CardNotes/Documentation et audit de run.sh — 13.2 Priorité moyenne — Ajouter une commande doctor..md`
- `wiki/tasks/Kanban_CardNotes/Documentation et audit de run.sh — 13.2 Priorité moyenne — Modulariser le script..md`
- `wiki/tasks/Kanban_CardNotes/Documentation et audit de run.sh — 13.2 Priorité moyenne — Mettre certaines variables dans un fichier de properties..md`
- `wiki/tasks/Kanban_CardNotes/Documentation et audit de run.sh — 13.3 Priorité basse — Ajouter une table de compatibilité des modes..md`
- `wiki/tasks/Kanban_CardNotes/Documentation et audit de run.sh — 13.3 Priorité basse — Ajouter des codes de sortie documentés..md`
- `wiki/tasks/Kanban_CardNotes/Documentation et audit de run.sh — 13.3 Priorité basse — Ajouter une section help plus compacte et une option help commande..md`
- `wiki/tasks/Kanban_CardNotes/Documentation et audit de run.sh — 14.2 Améliorations d'idempotence proposées — Formaliser une fonction ensure_- par ressource..md`
- `wiki/tasks/Kanban_CardNotes/Documentation et audit de run.sh — 14.2 Améliorations d'idempotence proposées — Rendre down totalement idempotent..md`
- `wiki/tasks/Kanban_CardNotes/Documentation et audit de run.sh — 14.2 Améliorations d'idempotence proposées — Rendre reset plus controlé..md`
- `wiki/tasks/Kanban_CardNotes/Documentation et audit de run.sh — 14.2 Améliorations d'idempotence proposées — Ajouter des postchecks après chaque démarrage..md`
- `wiki/tasks/Kanban_CardNotes/Documentation et audit de run.sh — 14.2 Améliorations d'idempotence proposées — Ajouter des tests automatisés d'idempotence..md`
- `wiki/tasks/Kanban_CardNotes/Documentation et audit de run.sh — 14.2 Améliorations d'idempotence proposées — Ajouter un mode de comparaison d'état avant-après..md`
- `wiki/tasks/Kanban_CardNotes/Documentation et audit de run.sh — 14.2 Améliorations d'idempotence proposées — Distinguer les commandes read-only des commandes mutantes..md`
- `wiki/tasks/Kanban_CardNotes/Documentation et audit de run.sh — 15.2 Recommandations concrètes — Centraliser les fonctions de logs..md`
- `wiki/tasks/Kanban_CardNotes/Documentation et audit de run.sh — 15.2 Recommandations concrètes — Ajouter des timestamps..md`
- `wiki/tasks/Kanban_CardNotes/Documentation et audit de run.sh — 15.2 Recommandations concrètes — Ajouter un fichier de log principal..md`
- `wiki/tasks/Kanban_CardNotes/Documentation et audit de run.sh — 15.2 Recommandations concrètes — Conserver les logs des sous-services..md`
- `wiki/tasks/Kanban_CardNotes/Documentation et audit de run.sh — 15.2 Recommandations concrètes — Ajouter une variable LOG_LEVEL..md`
- `wiki/tasks/Kanban_CardNotes/Documentation et audit de run.sh — 15.2 Recommandations concrètes — Masquer les secrets..md`
- `wiki/tasks/Kanban_CardNotes/Documentation et audit de run.sh — 15.2 Recommandations concrètes — Ajouter un résumé d'échec..md`
- `wiki/tasks/Kanban_CardNotes/Documentation et audit de run.sh — 15.2 Recommandations concrètes — Ajouter une commande logs service..md`
- `wiki/tasks/Kanban_CardNotes/Documentation et audit de run.sh — 16.1 Règles recommandées — Commenter l'intention, pas la syntaxe..md`
- `wiki/tasks/Kanban_CardNotes/Documentation et audit de run.sh — 16.1 Règles recommandées — Commenter les décisions dangereuses..md`
- `wiki/tasks/Kanban_CardNotes/Documentation et audit de run.sh — 16.1 Règles recommandées — Ajouter un commentaire d'en-tête par grande fonction complexe..md`
- `wiki/tasks/Kanban_CardNotes/Documentation et audit de run.sh — 16.1 Règles recommandées — Documenter les effets de bord..md`
- `wiki/tasks/Kanban_CardNotes/Documentation et audit de run.sh — 16.1 Règles recommandées — Ajouter un bloc contrat en haut du script..md`
**Points notables** :
- ajout uniquement de nouvelles cards dans la colonne `To do`
- déduplication effectuée par titre exact de card
- aucune card existante supprimée ou modifiée

## [2026-05-27] direct-update | docx layout parity follow-up backlog entry

**Agent** : Codex
**Mode** : direct-update
**Pages créées** :
- `wiki/tasks/docx-layout-parity-follow-up.md`
**Pages mises à jour** :
- `wiki/tasks/kanban.md`
- `wiki/index.md`
- `wiki/hot.md`
- `wiki/log.md`
**Points notables** :
- Recorded the merged DOCX document-language metadata work as complete.
- Added a deferred follow-up page for Arabic RTL layout parity, bullets, tables, and font strategy so the next work item is discoverable without reopening the completed metadata slice.
- Updated the hot cache and index/task catalog to point at the deferred follow-up rather than the merged metadata work.

## [2026-05-26] direct-update | proposal language hardening final state

**Agent** : Codex
**Mode** : direct-update
**Pages créées** :
- aucune
**Pages mises à jour** :
- `wiki/strategy/language-localization.md`
- `wiki/tech/proposal-ai-routing-and-inline-diff.md`
- `wiki/outputs/2026-05-26-proposal-language-generation-hardening.md`
- `wiki/hot.md`
- `wiki/log.md`
**Points notables** :
- Recorded final merged status for PR #58/#59/#60 in the proposal language hardening chain.
- Added explicit policy: unsupported exact numeric/duration/credential/ownership/operational claims remain hard-blocks in production, while vague timeline claims stay repair-first.
- Recorded that job title/job description are not candidate-proof sources for numeric/duration authorization.
- Preserved the `en`/`fr`/`es` UI scope and document-first rollout for additional language support (`de`, `ru`, `pl`, `ar`).
- Confirmed no page creation and no index reclassification was required in this pass.

---

## [2026-05-26] direct-update | proposal language pipeline hardening checkpoint

**Agent** : Codex
**Mode** : direct-update
**Pages créées** :
- `wiki/outputs/2026-05-26-proposal-language-generation-hardening.md`
**Pages mises à jour** :
- `wiki/index.md`
- `wiki/hot.md`
- `wiki/strategy/language-localization.md`
- `wiki/log.md`
**Points notables** :
- Captured the current language-generation state: UI layer still `en`/`fr`/`es`; document languages broader and independent (`de`, `ru`, `ar`, `pl`).
- Recorded that deterministic English fallback prose is blocked for non-`en`/`fr` document languages in proposal helper paths under the hardening pass.
- Added a forward-looking note for optional future document candidates (`zh`, `ta`) after QA evidence threshold is met.
- Confirmed hot/index/log consistency after this mutation.

---

## [2026-05-26] direct-update | proposal planner chain-of-thought documentation

**Agent** : Codex
**Mode** : direct-update
**Pages mises à jour** :
- `wiki/product/ai-product-model.md`
- `wiki/index.md`
- `wiki/hot.md`
**Points notables** :
- Added the Planner Agent chain-of-thought text verbatim to product documentation as the canonical shadow planner reasoning order.
- Added cross-references in wiki hot cache and retrieval index so the Planner Agent chain is discoverable.
- Linked [[product/ai-product-model]] to the existing source evidence: `sources/2026-05-25-proposal-generation-truth-planner`.

---

## [2026-05-26] ingest | language localization strategy reference

**Agent** : Codex
**Mode** : ingest
**Fichiers traités** :
- `rawinput/Two Weeks Language Map — Reference Note.md`
**Fichiers non traités** :
- `rawinput/emojis library .md` (intentionnellement ignoré)
**Pages créées** :
- `wiki/sources/2026-05-26-two-weeks-language-map-reference-note.md`
- `wiki/strategy/language-localization.md`
**Pages mises à jour** :
- `wiki/index.md`
- `wiki/hot.md`
- `wiki/log.md`
**Pages archivées** :
- aucune
**Points notables** :
- La note de langage est ingérée comme source de stratégie et déployée dans `wiki/strategy/language-localization.md`.
- Le fichier traité a été déplacé vers `raw/2026-05-26-two-weeks-language-map-reference-note.md` pour immutabilité `raw/`.
- La bibliothèque d’emojis n’a pas été ingérée par demande.

---

## [2026-05-25] ingest | proposal truth and theme palette ingest

**Agent** : Codex
**Mode** : ingest
**Fichiers traités** :
- `rawinput/Proposal Generation Truth Planner.md`
- `rawinput/light and dark theme two weeks .md`
**Pages créées** :
- `wiki/sources/2026-05-25-proposal-generation-truth-planner.md`
- `wiki/sources/2026-05-25-two-weeks-theme-palette.md`
**Mise à jour des pages** :
- `wiki/index.md`
- `wiki/hot.md`
- `wiki/log.md`
**Points notables** :
- Les nouvelles entrées de `rawinput/` ont été ingérées en tant que sources.
- Dédoublonnage vérifié : aucun duplicate exact n’a été trouvé dans `wiki/sources/`.
- Les fichiers ont été déplacés vers `raw/` avec conservation de l’original.
- `rawinput/` repasse à vide (hors `README.md`).
**Référence ingest** : `raw/` immuable.

---

## [2026-05-21] direct-update | shared command-layer parity for CV/Proposal toolbar + Ask

**Agent** : Codex
**Mode** : direct-update
**Pages créées** :
- `wiki/sources/2026-05-21-cv-proposal-command-layer-unification-note.md`
**Pages mises à jour** :
- `my-app/src/hooks/use-document-command-layer-position.ts`
- `my-app/src/lib/document-command-layer-layout.ts`
- `my-app/src/pages/CvForge.tsx`
- `my-app/src/pages/ProposalForge.tsx`
- `my-app/src/styles/product-cv.css`
- `my-app/src/styles/product-proposal.css`
- `my-app/src/styles/foundation.css`
- `my-app/src/styles/product.css`
- `my-app/src/components/__tests__/CvForgeToolbar.css.test.ts`
- `my-app/src/components/__tests__/ProposalDisplay.css.test.ts`
- `my-app/src/hooks/__tests__/use-document-command-layer-position.test.tsx`
- `my-app/src/lib/__tests__/document-command-layer-layout.test.ts`
- `wiki/hot.md`
- `wiki/index.md`
- `wiki/log.md`
**Points notables** :
- Unifie la logique de positionnement/densité du command-layer (toolbar + Ask) entre CV Forge et Proposal Forge via logique partagée (`use-document-command-layer-position` / `document-command-layer-layout`).
- Supprime les déviations CV-only qui causaient labels persistants à faible zoom, offsets Ask séparés et sauts de handle.
- Préserve les garde-fous de qualité: même comportement de mode compact/ultra et de sticky `commandLayerY` pour les deux surfaces.
- Garde la sémantique zoom CV intouchée (valeur utilisateur inchangée), en appliquant le rétrécissement uniquement par tokens de densité partagée.

---

## [2026-05-20] direct-update | topbar tokenized chrome alignment

**Agent** : Codex
**Mode** : direct-update
**Pages créées** :
- Aucune
**Pages mises à jour** :
- `my-app/src/styles/foundation.css`
- `my-app/src/styles/product.css`
- `my-app/src/components/__tests__/SidebarVisual.css.test.ts`
- `my-app/src/components/__tests__/ProposalDisplay.css.test.ts`
- `wiki/design/document-token-contract.md`
- `wiki/tech/proposal-forge-document-geometry.md`
- `wiki/hot.md`
- `wiki/index.md`
- `wiki/log.md`
**Points notables** :
- Définition explicite de la tokenisation topbar dans le contrat design pour stabiliser les métriques des contrôles (hauteur, gap, padding, alignement).
- Ajout de la règle “topbar commune” dans `proposal-forge-document-geometry` : les contrôles de toolbar sont gouvernés par les tokens app-topbar de `foundation.css`, pas des literals locaux.
- Mise à jour de la page de focus/chaleur (`hot.md`) avec la règle d’alignement CV/Proposal des contrôles, pour mémoire opérationnelle partagée.

## [2026-05-11] direct-update | CV ATS audit heuristic note ingested

**Agent** : Codex
**Mode** : direct-update
**Pages créées** :
- `wiki/tech/cv-ats-audit-heuristic.md`
**Pages mises à jour** :
- `wiki/index.md`
- `wiki/hot.md`
- `wiki/log.md`
**Points notables** :
- Ajoute la note technique V1 sur l'évaluation ATS heuristique CV (`evaluateCvAtsAudit`) et ses contraintes (heuristique, non parser-compatible ATS réel).
- Documente : seuils (excellent/good/needs_review/blocked), catégories, poids, fallback sur `cv.sections` quand le modèle export normalisé de confiance manque, et cas bloquants (`missing-cv`, `unresolved-import-review`).

## [2026-05-08] direct-update | ui audit proposal-polish snapshot

**Agent** : Codex
**Mode** : direct-update
**Pages créées** :
- `wiki/outputs/2026-05-08-ui-audit-proposal-polish.md`
**Pages mises à jour** :
- `wiki/index.md`
- `wiki/hot.md`
- `wiki/log.md`
**Points notables** :
- Ingest du recap UI audit en output snapshot non canonique.
- Conserve les valeurs CSS vérifiées séparément et marque le reste comme subjectif / screenshots only.
- Classe le diagnostic comme utile pour la direction design, mais pas comme source de vérité absolue.

## [2026-05-08] direct-update | proposal signature legacy artefact note

**Agent** : Codex
**Mode** : direct-update
**Pages mises à jour** :
- `wiki/tech/proposal-signature-closing-layer.md`
- `wiki/hot.md`
- `wiki/index.md`
- `wiki/log.md`
**Mise à jour technique associée (repo)** :
- `commit 9ed81aa9`
**Points notables** :
- Documente le comportement cible en edit/preview pour la signature structurée (edit = corps texte uniquement, signature = métadonnée/rendu).
- Ajoute la liste des artefacts legacy encore observés (`Warm regards`, nom en signature textuel) et leurs impacts connus.
- Ajoute des recommandations de migration: nettoyage legacy au chargement, sanitization du draft chargé, et test e2e ciblé sur ancienne proposition.
- Note que le flux manuscrit/image doit rester une couche de rendu (preview/print/export), jamais éditable dans le texte.

## [2026-05-08] direct-update | shared custom style color pipeline

**Agent** : Codex
**Mode** : direct-update
**Pages mises à jour** :
- `wiki/tech/proposal-style-layer.md`
- `wiki/index.md`
- `wiki/hot.md`
- `wiki/log.md`
**Mise à jour technique associée (repo)** :
- `my-app/src/pages/SettingsPage.tsx`
- `my-app/src/components/cv/CvRail.tsx`
- `my-app/src/pages/CvForge.tsx`
**Points notables** :
- Documente Custom comme septième option d'accent dans Settings, CV Forge, et Proposal Forge.
- Clarifie que Custom n'est pas un `paletteOverride` nommé: il persiste via `palette: "custom"` et `accentHex`.
- Note que sélectionner une couleur nommée doit effacer l'accent custom, tandis que sélectionner Custom conserve le slot de style courant en état personnalisé.
- Ajoute la règle de reset: Settings restaure le slot aux defaults factory sans déplacer le default actif; CV Forge reset vers le slot Settings utilisateur quand il existe.

## [2026-05-08] direct-update | proposal style default-slot semantics note

**Agent** : Codex
**Mode** : direct-update
**Pages mises à jour** :
- `wiki/tech/proposal-style-layer.md`
- `wiki/index.md`
- `wiki/hot.md`
- `wiki/log.md`
**Mise à jour technique associée (repo)** :
- `my-app/src/pages/SettingsPage.tsx`
- `my-app/convex/proposalSettings.ts`
**Points notables** :
- Clarifie la différence entre slot content and active default: editing a style slot does not make it default.

## [2026-05-08] direct-update | proposal signature closing structured pipeline note

**Agent** : Codex
**Mode** : direct-update
**Pages créées** :
- `wiki/tech/proposal-signature-closing-layer.md`
**Pages mises à jour** :
- `wiki/index.md`
- `wiki/hot.md`
- `wiki/log.md`
**Mise à jour technique associée (repo)** :
- `my-app/src/lib/proposal-closing.ts`
- `my-app/src/lib/proposal-output-draft.ts`
- `my-app/src/lib/document-export-models.ts`
- `my-app/src/components/proposal-render/ProposalDocumentRenderer.tsx`
- `my-app/src/pages/ProposalForge.tsx`
- `my-app/src/pages/ProposalPrintPage.tsx`
- `my-app/src/components/ProposalDisplay.tsx`
- `my-app/src/components/ProposalsList.tsx`
- `my-app/convex/schema.ts`
- `my-app/convex/createProposalPublic.ts`
- `my-app/convex/updateProposalPublic.ts`
- `my-app/convex/proposalsPublic.ts`
**Points notables** :
- Note de plan ajoutée dans le wiki sur la frontière Signature/Closing (pas de pipeline Python dédié; le flux actif est TypeScript + Convex + renderers).
- Résumé du plan `plans/proposal-structured-closing.md` intégré en mode "started": métadonnée close structurée, fallback legacy, et propagation preview/print/export.
- Le contrôle UI avancé (toggle/override dédié) reste planifié après stabilisation de la persistance et des tests de parité.
- Records the explicit `Set as default` control as the only action that should move the active default badge.
- States the intended rule for new docs: start from the active default slot when no more specific document style exists.

## [2026-05-08] direct-update | proposal style layer live-boundary scratchpad

**Agent** : Codex
**Mode** : direct-update
**Pages mises à jour** :
- `wiki/tech/proposal-style-layer.md`
- `wiki/index.md`
- `wiki/hot.md`
- `wiki/log.md`
**Mise à jour technique associée (repo)** :
- `my-app/convex/proposalSettings.ts`
- `my-app/convex/schema.ts`
**Points notables** :
- Enregistre le vrai cause/résolution du bug live: `savePreset` faisait un fan-out sur tous les `userProfiles` du même Clerk, ce qui dépassait la limite de lecture Convex et empêchait la sauvegarde.
- Clarifie que le Style 2 natif reste `quiet-editorial` avec le template CV Workshop deux colonnes.
- Oriente le diagnostic vers les champs persistés `proposalPreset2`, `proposalFontPairId`, et `proposalVerbatiStyle.typography` si l'UI affiche encore Parisienne/Cormorant.

## [2026-05-08] direct-update | document style slot live-boundary trace

**Agent** : Codex
**Mode** : direct-update
**Pages mises à jour** :
- `wiki/tech/proposal-style-layer.md`
- `wiki/hot.md`
- `wiki/log.md`
**Mise à jour technique associée (repo)** :
- Style slot debugging in app worktree, uncommitted
**Points notables** :
- Documente que Style 1/2/3 traverse trois frontières gagnantes: factory slots, Settings/CV Forge presets, et Proposal Forge current settings.
- Note que `studio-grotesk` / Parisienne-Cormorant ne vient pas des factory slots actuels et pointe plutôt vers un preset Convex ou un champ current settings persisté.

## [2026-05-07] direct-update | workshop two-column resume pagination

**Agent** : Codex
**Mode** : direct-update
**Pages mises à jour** :
- `wiki/tech/workshop-pagination.md`
- `wiki/hot.md`
- `wiki/log.md`
**Mise à jour technique associée (repo)** :
- Branch app `new-layout`
**Points notables** :
- Étend la vérité Workshop pagination aux templates planner-backed `workshop_resume_onecol_ats` et `workshop_resume_twocol_ats`.
- Préserve `committedPages` comme autorité des page breaks preview/print/export.
- Documente que le placement des colonnes two-column reste local au renderer sauf preuve browser mesurée.

## [2026-05-07] direct-update | proposal forge document geometry canon

**Agent** : Codex
**Mode** : direct-update
**Pages créées** :
- `wiki/tech/proposal-forge-document-geometry.md`
**Pages mises à jour** :
- `wiki/index.md`
- `wiki/log.md`
- `wiki/hot.md`
**Mise à jour technique associée (repo)** :
- Commit app `f0e9208e fix(proposal): canonicalize workspace paper width`
- Commit app `93c093ae fix(proposal): align edit scrollbar with page edge`
**Points notables** :
- Documente le canon page-first Proposal Forge: `--proposal-paper-visual-inline-size` comme autorité de largeur visible.
- Clarifie l'alignement toolbar/panel/shell/stage/viewport autour du breakpoint 1420px.
- Définit la séparation page width vs reading measure et le placement des scrollbars preview/edit au bord de page.
- Ajoute un prompt guardrail réutilisable pour agents LLM travaillant sur cette surface.

## [2026-05-06] direct-update | proposal AI routing and inline diff overlay

**Agent** : Codex
**Mode** : direct-update
**Pages créées** :
- `wiki/tech/proposal-ai-routing-and-inline-diff.md`
**Pages mises à jour** :
- `wiki/index.md`
- `wiki/log.md`
- `wiki/hot.md`
**Mise à jour technique associée (repo)** :
- `docs/decisions/2026-05-06-proposal-ai-selector-and-inline-diff-overlay.md`
- `my-app/config/llmConfig.ts`
- `my-app/convex/lib/editorAi.ts`
- `my-app/convex/generateProposalMutation.ts`
- `my-app/convex/langchain/models/openai_responses_adapter.ts`
- `my-app/convex/lib/proposals/premiumCoverLetter.ts`
- `my-app/src/components/ProposalInputForm.tsx`
- `my-app/src/components/ProposalDisplay.tsx`
- `my-app/src/styles/product-proposal.css`
**Points notables** :
- Proposal generation remains on OpenAI `gpt-5.5`; the proposal form now honors env-driven default model overrides.
- Helper toolbar actions now route through Qwen first, with `fix_grammar` on `qwen-3.6-flash` and Mistral/DeepSeek fallbacks.
- Proposal text suggestions now render inline as an overlay diff rather than a detached suggestion card.
- Job summary and keyword match synthesis is on the Ministral/Mistral path, currently defaulting to `ministral-3-3b-instruct-2512`.

## [2026-05-06] direct-update | proposal style layer scratchpad

**Agent** : Codex
**Mode** : direct-update
**Pages créées** :
- `wiki/tech/proposal-style-layer.md`
**Pages mises à jour** :
- `wiki/index.md`
- `wiki/log.md`
- `wiki/hot.md`
**Mise à jour technique associée (repo)** :
- Commit app `ccbc4280 fix: stabilize proposal style customization`
**Points notables** :
- Documente le modèle Style 1/2/3 comme base durable avec état `Custom` pour les changements couleur/police/layout.
- Définit les palettes actives nommées `terre`, `cobalt`, `ink`, `sauge`, `plum`, `ochre`; les ids legacy restent lisibles seulement.
- Note les commandes de vérification Vitest/TypeScript à relancer pour cette couche.

## [2026-05-04] direct-update | CV Forge docs sync for paper width and AI routing

**Agent** : Codex
**Mode** : direct-update
**Pages mises à jour** :
- `wiki/sources/2026-04-30-cv-forge-pr4-remaining-tasks.md`
- `wiki/tasks/kanban.md`
- `wiki/hot.md`
- `wiki/index.md`
**Mise à jour technique associée (repo)** :
- `docs/plans/2026-03-21-ui-next-steps-todo.md`
- `docs/audits/2026-05-04-cv-forge-paper-width-and-ai-routing.md`
**Points notables** :
- Synchronisation de la doc active avec l’état live du CV Forge: edit et preview partagent maintenant le même paper width canonique (860px), sans stage compact.
- Alignement du helper AI CV Forge sur `mistral-small-latest` pour summary/custom et suggestion actions.
- Parité rich-summary conservée dans le renderer partagé; la paper editing complète reste partiellement différée.

## [2026-05-04] direct-update | e2e modal selector hardening for cvforge preview linking

**Agent** : Codex
**Mode** : direct-update
**Pages mises à jour** :
- `wiki/hot.md`
- `wiki/tasks/kanban.md`
- `wiki/sources/2026-04-30-cv-forge-pr4-remaining-tasks.md`
**Mise à jour technique associée (repo)** :
- `e2e/cvforge-preview-linking.spec.ts`
- `docs/plans/2026-03-21-ui-next-steps-todo.md`
- `docs/audits/2026-05-04-verbati-style-metadata-persistence-hardening.md`
**Points notables** :
- Résolution de fragilité Playwright: remplacement des assertions de nom exact de dialogue par assertions sur le heading (`Profile`, `Projects`, `Experience`, etc.) + fermeture via `button[aria-label="Close panel."]`.
- Fixe du seed test en forçant explicitement le mode preview via `dasti:cv-forge-workspace-mode:v1=preview`.
- Vérification: `rtk npx playwright test e2e/cvforge-preview-linking.spec.ts --project=chromium --grep "keeps modal targets in preview mode and routes aliases correctly"`.

## [2026-05-04] direct-update | CV style persistence hardening and guardrail documentation

**Agent** : Codex
**Mode** : direct-update
**Pages mises à jour** :
- `wiki/tasks/kanban.md`
- `wiki/sources/2026-04-30-cv-forge-pr4-remaining-tasks.md`
- `wiki/hot.md`
**Mise à jour technique associée (repo)** :
- `docs/audits/2026-05-04-verbati-style-metadata-persistence-hardening.md` (repo)
**Points notables** :
- Les sauvegardes style-only CV sont désormais routées vers une mutation Convex de métadonnées (`metadata.verbatiStyle`) sans `cvDocument`.
- Un garde-fou backend évite la création de ligne `userProfiles` quand le patch style est `metadata` only.
- Les tests de vérification incluent :
  - `my-app/convex/__tests__/profiles.patch.test.ts`
  - `my-app/src/adapters/__tests__/StorageAdapter.test.ts`
  - `src/features/verbati/__tests__/useBoundVerbatiCvStyle.test.tsx`
  - `src/features/verbati/__tests__/VerbatiCvPreviewPanel.test.tsx`
  - `src/features/verbati/__tests__/VerbatiCvPreviewPanel.workspace-style-cycle.test.tsx`

## [2026-05-04] ingest | rawinput ingest + task sync

**Agent** : Codex
**Fichiers traités** :
- `rawinput/2026-04-30-cv-forge-pr4-remaining-tasks 1.md`
- `rawinput/2026-04-30-cv-forge-pr4-remaining-tasks.md`
- `rawinput/2026-04-30-jobs-language-localization-scratchpad.md`
- `rawinput/refonte wiki claude-obsidian.md`
- `rawinput/two-weeks app skeleton -skill.md`
**Pages créées** :
- `wiki/sources/2026-04-30-cv-forge-pr4-remaining-tasks.md`
- `wiki/sources/2026-04-30-jobs-language-localization-scratchpad.md`
- `wiki/sources/2026-04-30-refonte-wiki-claude-obsidian.md`
- `wiki/sources/2026-04-30-two-weeks-app-skeleton-skill.md`
**Pages mises à jour** :
- `wiki/tasks/kanban.md`
- `wiki/index.md`
- `wiki/log.md`
**Points notables** :
- Toutes les entrées de `rawinput/` ont été ingérées et déplacées vers `raw/`.
- Dédoublonnage `cv-forge-pr4-remaining-tasks` : la version `... 1.md` (plus récente) a été conservée comme source principale.
- `wiki/tasks/kanban.md` a reçu un suivi PR4 plus explicite (actions en cours de confirmation).
- `wiki/index.md` mis à jour avec 4 nouvelles sources `2026-04-30-*`.

## [2026-05-02] direct-update | active memory gateway for LLM retrieval

**Agent** : Codex
**Pages créées** :
- `wiki/hot.md`
- `wiki/howto/wiki-commands-and-llm-export.md`
**Pages mises à jour** :
- `AGENTS.md`
- `WIKI_SCHEMA.md`
- `CLAUDE.md`
- `README.md`
- `SKILL.md`
- `skills/ingest-wiki/SKILL.md`
- `/Users/pana/.codex/skills/ingest-wiki/SKILL.md`
- `wiki/hot.md`
- `wiki/index.md`
- `wiki/log.md`
- `wiki/tasks/coffee talk.md`
**Points notables** :
- `wiki/hot.md` devient le cache actif non canonique pour retrieval LLM rapide
- `wiki/index.md` garde la carte canonique et reçoit une Retrieval Map courte
- les workflows doivent lire `hot.md` avant d'élargir vers `index.md` et pages durables
- `AGENTS.md`, `README.md` et le howto donnent un prompt court pour les agents futurs
- `README.md` pointe maintenant vers `hot.md` dans le démarrage wiki
- `coffee talk.md` contient la commande courte pour synchroniser la skill Codex collaborateur
- `wiki/howto/wiki-commands-and-llm-export.md` sauvegarde les commandes wiki et le plan `wiki/llms.txt`

## [2026-04-28] direct-update | AI Consistency P0 closure audit note

**Agent** : Codex
**Pages créées** :
- `wiki/product/ai-consistency-p0-editor-ai.md`
**Pages mises à jour** :
- `wiki/index.md`
- `wiki/log.md`
**Points notables** :
- closure audit snapshot for PRs #42 to #45
- status updated to implemented / audited / follow-up hardening pending
- dev docs mention added for `./run.sh local-fast`, `./run.sh tunnel`, and `./run.sh reload-env`

## [2026-04-12] ingest | Brand Bible twoweeks.ai 2026

**Agent** : Claude
**Fichiers traités** : `rawinput/twoweeks-brand-bible.md`
**Pages créées** :
- `wiki/sources/2026-04-12-twoweeks-brand-bible.md`
- `wiki/entities/twoweeks.md` — entité principale corrigée (nom réel du produit)
- `wiki/concepts/brand-voice.md` — voix staccato, Corporate Noir, règles copie UI
**Pages archivées** :
- `wiki/entities/cv-forge.md` → `wiki/archive/entities/cv-forge.md` (supersédée par twoweeks)
**Mises à jour** :
- `CLAUDE.md` — description app mise à jour : twoweeks.ai, tagline, positionnement, modules
- `wiki/timeline.md` — event Supersede cv-forge → twoweeks
- `wiki/index.md` — section Archive ajoutée, stats mises à jour

---

## [2026-04-12] ingest | Runbook tunnel Cloudflare + note pipeline import OCR

**Agent** : Claude
**Fichiers traités** : `rawinput/howto_tunnel.md`, `rawinput/pipeline note.md`
**Pages créées** :
- `wiki/howto/cloudflare-zero-trust-tunnel.md`
- `wiki/tech/import-ocr-pipeline.md`

---

## [2026-04-12] structure | Nouveaux répertoires tech/ howto/ kanban + récupération pages manquantes

**Agent** : Claude
**Pages créées** :
- `wiki/to do list/kanban.md`
- `wiki/concepts/parsing-poc-progress.md`
- `wiki/sources/2026-04-11-cv-parsing-poc-state.md`
- `wiki/sources/2026-04-11-todo-sprint.md`
- `wiki/sources/2026-04-11-jessica-helen-poc-state.md`
**Mises à jour** : `wiki/index.md`, `CLAUDE.md`

---

## [2026-04-11] decision | Finding stockage Convex — cvDocument est la source de vérité

**Agent** : Claude
**Pages mises à jour** : `wiki/entities/cv-forge.md` (archivé depuis) — architecture de stockage Convex documentée. `userProfiles.cvDocument` est la source de vérité. Les champs top-level `experience[]`, `education[]`, `skills[]` sont legacy et vides.

---

## [2026-04-11] ingest | CV Parsing POC State + Sprint Notes

**Agent** : Claude
**Fichiers traités** : `rawinput/2026-04-11-cv-parsing-poc-state.md`, `rawinput/to do.md`
**Pages créées** : sources/2026-04-11-cv-parsing-poc-state.md, sources/2026-04-11-todo-sprint.md, concepts/parsing-poc-progress.md
**Pages mises à jour** : concepts/cv-parsing-pipeline.md, entities/cv-forge.md (archivé depuis)

---

## [2026-04-10] decision | Refonte système de tones — 4 tones avec Auto

**Agent** : Claude
**Décision** : Remplacer Balanced/Warm/Formal par Auto/Natural/Formal/Warm. Auto = mode recommandé par défaut, analyse l'offre d'emploi et choisit le tone automatiquement.
**Pages mises à jour** : concepts/ai-product-model.md, entities/cv-forge.md (archivé depuis), concepts/product-vision.md, wiki/timeline.md

---

## [2026-04-10] ingest | Gap Analysis — diagnostic vs ResumeLab, priorités, 3 cycles

**Agent** : Claude
**Fichiers traités** : `rawinput/3_gap_analysis.md`
**Pages créées** : concepts/gap-analysis.md, sources/2026-04-10-gap-analysis.md

---

## [2026-04-10] ingest | Benchmark Matrix + Success Blueprint — scoring, vision, IA

**Agent** : Claude
**Fichiers traités** : `rawinput/1_ideal_benchmark_matrix.md`, `rawinput/2_success_blueprint.md`
**Pages créées** : concepts/benchmark-matrix.md, concepts/product-vision.md, concepts/ai-product-model.md, concepts/kpis.md, sources/2026-04-10-benchmark-matrix.md, sources/2026-04-10-success-blueprint.md

---

## [2026-04-10] ingest | Notion Roadmap CV Forge — phases, KPIs, décisions produit

**Agent** : Claude
**Fichiers traités** : `rawinput/6_NOTION_ROADMAP.MD`
**Pages créées** : concepts/product-roadmap.md, sources/2026-04-10-notion-roadmap-cvforge.md

---

## [2026-04-09] ingest | Décisions sprint CV Forge — parser, features, bugs

**Agent** : Claude
**Fichiers traités** : `rawinput/`
**Pages créées** : entities/cv-forge.md (archivé depuis), concepts/cv-parsing-pipeline.md, concepts/cv-families.md, sources/2026-04-09-decisions-cvforge-sprint.md, sources/2026-04-09-tweet-karpathy-llm-wiki.md, sources/2026-04-09-wiki-paste-llm-wiki.md

---

## [2026-04-09] init | Création du vault twoweeks

Initialisation du vault Obsidian + schema LLM wiki v1.

---

## [2026-04-09] architecture | Migration v1 → v2 : rawinput/ + gestion temporelle

Migration vers schema v2 : ajout rawinput/ (staging), gestion temporelle (status/horizon/version/superseded_by), wiki/archive/, wiki/timeline.md.

## [2026-04-14] ingest | ATS, parser canonical truth, local/cloud modes, extension, kanban

**Agent** : Codex
**Fichiers traités** : `rawinput/ATS COMPLIANT SCORE.md`, `rawinput/Local dev server vs Remote dev server Architecture.md`, `rawinput/run.sh launching commands for the app.md`, `rawinput/clerk chrome extension specs addon.md`, `rawinput/ARCHITECTURE PARSIN MISTRAL.md`, `rawinput/Docker commands.md`, `rawinput/kanban.md`
**Pages créées** :
- `wiki/sources/2026-04-14-ats-compliant-score.md`
- `wiki/sources/2026-04-14-local-dev-vs-remote-parser-architecture.md`
- `wiki/sources/2026-04-14-run-sh-modes.md`
- `wiki/sources/2026-04-14-clerk-chrome-extension-addon.md`
- `wiki/sources/2026-04-14-structured-parsing-canonical-truth.md`
- `wiki/sources/2026-04-14-docker-commands.md`
- `wiki/sources/2026-04-14-kanban-sprint-notes.md`
- `wiki/concepts/ats-safety.md`
- `wiki/concepts/cv-parsing-pipeline.md`
- `wiki/concepts/cv-families.md`
- `wiki/tech/local-vs-remote-parser-architecture.md`
- `wiki/howto/local-parser-operations.md`
**Pages mises à jour** :
- `wiki/overview.md`
- `wiki/entities/twoweeks.md`
- `wiki/tech/import-ocr-pipeline.md`
- `wiki/to do list/kanban.md`
- `wiki/timeline.md`
- `wiki/index.md`
**Pages archivées** :
- aucune

## [2026-04-14] ingest | run.sh quick note — main dev entrypoint

**Agent** : Codex
**Fichiers traités** : `rawinput/RUN.SH QUICK NOTE.md`
**Pages créées** :
- `wiki/sources/2026-04-14-run-sh-quick-note.md`
**Pages mises à jour** :
- `wiki/howto/APP-launcher-command.md`
- `wiki/tech/local-vs-remote-parser-architecture.md`
- `wiki/tech/import-ocr-pipeline.md`
- `wiki/entities/twoweeks.md`
- `wiki/concepts/parsing-poc-progress.md`
- `wiki/to do list/kanban.md`
- `wiki/howto/cloudflare-zero-trust-tunnel.md`
- `wiki/overview.md`
- `wiki/timeline.md`
- `wiki/index.md`
**Pages archivées** : aucune

## [2026-04-15] ingest | locale typography rules + French/English scratch pads

**Agent** : Codex
**Fichiers traités** : `rawinput/TYPOGRAPHY MODE.md`, `rawinput/FRENCH TYPOGRAPHY SCRATCH PAD.md`, `rawinput/ENGLISH TYPOGRAPHY SCRATCH PAD.md`
**Pages créées** :
- `wiki/sources/2026-04-15-typography-mode.md`
- `wiki/sources/2026-04-15-french-typography-scratch-pad.md`
- `wiki/sources/2026-04-15-english-typography-scratch-pad.md`
- `wiki/sources/2026-04-15-conversation-locale-typography-rules.md`
- `wiki/design/locale-typography-rules.md`
**Pages mises à jour** :
- `wiki/design/a4-layout-systems.md`
- `wiki/design/brand-voice.md`
- `wiki/tech/export-pipeline.md`
- `wiki/index.md`
- `wiki/log.md`
**Pages archivées** :
- aucune

## [2026-04-18] direct-update | Mistral Resume V3 section recovery refresh

**Agent** : Codex
**Références revues** : `cv_parser_service/mistral_resume_v3/section_headings.py`, `cv_parser_service/mistral_resume_v3/pipeline.py`, `cv_parser_service/mistral_resume_v3/post_validation.py`, `cv_parser_service/tests/test_mistral_resume_v3_pipeline.py`
**Pages mises à jour** :
- `wiki/sources/2026-04-15-mistral-resume-v3-section-recovery-scratchpad.md`
- `wiki/tech/import-ocr-pipeline.md`
- `wiki/concepts/cv-parsing-pipeline.md`
- `wiki/index.md`
- `wiki/log.md`
**Points notables** :
- alias `experience` multilingues maintenus explicitement
- split des headings composés borné aux séparateurs sûrs
- validation post-recovery et retry unique conservés via `section_evidence_contradiction`

## [2026-04-18] ingest | Quick Start module hierarchy

**Agent** : Codex
**Fichiers traités** : `rawinput/Quick Start Module Hierarchy.md`
**Pages créées** :
- `wiki/sources/2026-04-18-quick-start-module-hierarchy.md`
- `wiki/tech/quick-start-module-hierarchy.md`
**Pages mises à jour** :
- `wiki/product/product-roadmap.md`
- `wiki/strategy/gap-analysis.md`
- `wiki/overview.md`
- `wiki/index.md`
- `wiki/log.md`
**Pages archivées** :
- aucune
**Points notables** :
- Quick Start est un état d'app-shell content-pane, pas une modale
- le cold start cover-letter reste un état d'entrée intentionnel dans `/proposal`
- la primitive de carte partagée reste commune aux chemins resume et cover-letter
- l'onboarding de première session demeure le reliquat principal

## [2026-04-14] ingest | export pipeline brief — OCR to ATS / styled output

**Agent** : Codex
**Fichiers traités** : `rawinput/Export Pipeline Brief  OCR to ATS Styled Output.md`
**Pages créées** :
- `wiki/sources/2026-04-14-export-pipeline-brief-ocr-to-ats-styled-output.md`
- `wiki/tech/export-pipeline.md`
**Pages mises à jour** :
- `wiki/tech/import-ocr-pipeline.md`
- `wiki/concepts/cv-parsing-pipeline.md`
- `wiki/concepts/ats-safety.md`
- `wiki/entities/twoweeks.md`
- `wiki/overview.md`
- `wiki/index.md`
**Pages archivées** : aucune

## [2026-04-15] ingest | parser recovery scratchpad + run.sh workspace modes + section detection note

**Agent** : Codex
**Fichiers traités** : `rawinput/Mistral Resume V3 Section-Recovery Scratchpad.md`, `rawinput/run.sh\` LLM Scratchpad.md`, `rawinput/section detection.md`
**Pages créées** :
- `wiki/sources/2026-04-15-mistral-resume-v3-section-recovery-scratchpad.md`
- `wiki/sources/2026-04-15-run-sh-workspace-modes.md`
- `wiki/sources/2026-04-15-section-detection-future-note.md`
- `wiki/howto/local-parser-operations.md`
**Pages mises à jour** :
- `wiki/concepts/cv-parsing-pipeline.md`
- `wiki/tech/import-ocr-pipeline.md`
- `wiki/tech/local-vs-remote-parser-architecture.md`
- `wiki/entities/twoweeks.md`
- `wiki/overview.md`
- `wiki/to do list/kanban.md`

## [2026-04-16] ingest | proposal style persistence + verbati style pipeline

**Agent** : Codex
**Fichiers traités** : `rawinput/Proposal Style Persistence Quickmap Scratchpad.md`, `rawinput/Verbati Style Pipeline Scratchpad.md`
**Pages créées** :
- `wiki/sources/2026-04-16-proposal-style-persistence-quickmap-scratchpad.md`
- `wiki/sources/2026-04-16-verbati-style-pipeline-scratchpad.md`
**Pages mises à jour** :
- `wiki/design/document-token-contract.md`
- `wiki/tech/preview-to-print-pipeline.md`
- `wiki/tech/export-pipeline.md`
- `wiki/index.md`
- `wiki/log.md`
**Pages archivées** :
- aucune
- `wiki/sources/2026-04-14-run-sh-quick-note.md`
- `wiki/timeline.md`
- `wiki/index.md`
- `wiki/log.md`
**Pages archivées** :
- `wiki/archive/concepts/parsing-poc-progress.md`

## [2026-04-15] ingest | A4 grid canon spec writer

**Agent** : Codex
**Fichiers traités** : `rawinput/A4 Grid Canon Spec Writer.md`
**Pages créées** :
- `wiki/sources/2026-04-15-a4-grid-canon-spec-writer.md`
- `wiki/design/a4-layout-systems.md`
**Pages mises à jour** :
- `wiki/concepts/ats-safety.md`
- `wiki/tech/export-pipeline.md`
- `wiki/index.md`
- `wiki/log.md`
**Pages archivées** :
- aucune

## [2026-04-15] doc-update | design bucket pour specs visuelles durables

**Agent** : Codex
**Source** : explicit user instruction
**Pages créées** : aucune
**Pages mises à jour** :
- `CLAUDE.md`
- `wiki/design/a4-layout-systems.md` (déplacée depuis `wiki/concepts/`)
- `wiki/sources/2026-04-15-a4-grid-canon-spec-writer.md`
- `wiki/concepts/ats-safety.md`
- `wiki/tech/export-pipeline.md`
- `wiki/index.md`
- `wiki/log.md`
**Pages archivées** : aucune

## [2026-04-15] doc-update | buckets product strategy meta et rangement des concepts

**Agent** : Codex
**Source** : explicit user instruction
**Pages créées** : aucune
**Pages mises à jour** :
- `CLAUDE.md`
- `wiki/index.md`
- `wiki/entities/twoweeks.md`
- `wiki/overview.md`
- `wiki/tech/export-pipeline.md`
- `wiki/design/a4-layout-systems.md`
- `wiki/sources/2026-04-12-twoweeks-brand-bible.md`
- `wiki/sources/2026-04-14-ats-compliant-score.md`
- `wiki/sources/2026-04-14-export-pipeline-brief-ocr-to-ats-styled-output.md`
- `wiki/sources/2026-04-14-clerk-chrome-extension-addon.md`
- `wiki/sources/2026-04-15-a4-grid-canon-spec-writer.md`
- `wiki/timeline.md`
- `wiki/log.md`
**Pages archivées** : aucune

## [2026-04-16] ingest | preview-print pipelines, token contract, onboarding plan

**Agent** : Codex
**Fichiers traités** : `rawinput/Live Proposal Preview-to-Print Pipeline Scratchpad.md`, `rawinput/Live Resume Preview-to-Print Pipeline Scratchpad.md`, `rawinput/Plan Onboarding, Activation & Interactive Preview — twoweeks.ai.md`, `rawinput/pdf pipeline.md`, `rawinput/token classes for the layout.md`
**Pages créées** :
- `wiki/sources/2026-04-16-live-proposal-preview-to-print-pipeline-scratchpad.md`
- `wiki/sources/2026-04-16-live-resume-preview-to-print-pipeline-scratchpad.md`
- `wiki/sources/2026-04-16-plan-onboarding-activation-interactive-preview.md`
- `wiki/sources/2026-04-16-pdf-pipeline.md`
- `wiki/sources/2026-04-16-token-classes-for-the-layout.md`
- `wiki/tech/preview-to-print-pipeline.md`
- `wiki/design/document-token-contract.md`
**Pages mises à jour** :
- `wiki/tech/export-pipeline.md`
- `wiki/product/product-roadmap.md`
- `wiki/index.md`
- `wiki/log.md`
**Pages archivées** :
- aucune

## [2026-04-17] migration | hybrid control plane + tasks taxonomy

**Agent** : Codex
**Fichiers traités** : `WIKI_SCHEMA.md`, `CLAUDE.md`, `README.md`, `SKILL.md`, `wiki/index.md`, `wiki/meta/llm-wiki-pattern.md`, `wiki/overview.md`, `wiki/entities/twoweeks.md`, `wiki/concepts/cv-families.md`, `wiki/sources/2026-04-14-kanban-sprint-notes.md`, `wiki/sources/2026-04-14-clerk-chrome-extension-addon.md`, `/Users/pana/.codex/skills/ingest-wiki/SKILL.md`
**Pages créées** : aucune
**Pages mises à jour** : `wiki/index.md`, `wiki/meta/llm-wiki-pattern.md`, `wiki/overview.md`, `wiki/entities/twoweeks.md`, `wiki/concepts/cv-families.md`, `wiki/sources/2026-04-14-kanban-sprint-notes.md`, `wiki/sources/2026-04-14-clerk-chrome-extension-addon.md`
**Pages archivées** : aucune
**Migrations** : `wiki/to do list/` → `wiki/tasks/`, archive directories backfilled, bootstrap contract aligned on `WIKI_SCHEMA.md` + `CLAUDE.md`

## [2026-04-17] migration | twoweeks-pagecraft hybrid repo overlay

**Agent** : Codex
**Source** : explicit user instruction
**Pages créées** : aucune
**Pages mises à jour** :
- `README.md`
- `WIKI_SCHEMA.md`
- `CLAUDE.md`
- `AGENTS.md`
- `SKILL.md`
- `wiki/index.md`
- `wiki/log.md`
**Fichiers ajoutés** :
- `IMPLEMENTATION_RULES.md`
- `EXAMPLES.md`
- `skills/ingest-wiki/SKILL.md`
- `skills/apply-hybrid-code-layer/SKILL.md`
- `scripts/audit_code_repo.py`
- `scripts/score_code_repo.py`
- `scripts/validate_overlay.py`
- `audit/code-benchmark-criteria.csv`
**Pages archivées** : aucune
**Migrations** :
- `CLAUDE.md` devient le contrat canonique hybride wiki + code
- `AGENTS.md` devient un shim de compatibilité pour éviter une deuxième rulebook
- la skill ingest gagne un préflight explicite et des contrats de vérification
- les scripts d'audit ignorent les surfaces Obsidian/wiki/raw pour ne pas confondre outillage local et vrai code applicatif

## [2026-04-17] doc-update | skills howto

**Agent** : Codex
**Source** : explicit user instruction
**Pages créées** : aucune
**Pages mises à jour** :
- `README.md`
- `wiki/log.md`
**Fichiers ajoutés** :
- `SKILLS_HOWTO.md`
**Pages archivées** : aucune
**Migrations** :
- ajout d'un howto repo-level qui explique le rôle de `ingest-wiki` vs `apply-hybrid-code-layer`

## [2026-04-17] ingest | live resume preview runtime handoff

**Agent** : Codex
**Fichiers traites** : `rawinput/CVForge Live Resume Render  Interactive Preview Handoff.md`
**Pages creees** :
- `wiki/sources/2026-04-17-cvforge-live-resume-render-interactive-preview-handoff.md`
- `wiki/tech/live-resume-preview-runtime.md`
**Pages mises a jour** :
- `wiki/index.md`
- `wiki/log.md`
**Pages archivees** :
- aucune

## [2026-04-17] doc-update | roadmap and gap status refresh

**Agent** : Codex
**Source** : explicit user instruction
**Pages créées** : aucune
**Pages mises à jour** :
- `wiki/product/product-roadmap.md`
- `wiki/strategy/gap-analysis.md`
- `wiki/index.md`
- `wiki/log.md`
**Pages archivées** : aucune
**Migrations** :
- `Editor ↔ Preview linking` marqué comme implémenté avec reliquat UI/frontend
- `Import recovery layer` marqué comme implémenté avec reliquat de styling CSS et harmonisation des tokens
- `Document health / readiness layer` marqué comme implémenté avec reliquat de tests et validation

## [2026-04-24] ingest | Pass 3B Structured Scoring Decisions

**Agent** : Codex
**Fichiers traités** : `rawinput/Pass 3B Structured Scoring Decisions.md`
**Pages créées** :
- `wiki/sources/2026-04-24-pass-3b-structured-scoring-decisions.md`
**Pages mises à jour** :
- `wiki/index.md`
- `wiki/log.md`
**Pages archivées** :
- aucune
**Points notables** :
- contrat de beta review interne pour structured shadow output
- production score laissé inchangé
- rawinput déplacé vers `raw/` après ingest

## [2026-04-27] ingest | jobs, match review, brand voice, motion, workshop pagination

**Agent** : Codex
**Fichiers traités** :
- `rawinput/.md`
- `rawinput/ Prompt for ChatGPT — Twoweeks brand-voice copy refactor.md`
- `rawinput/Brand Voice Review — Twoweeks.ai.md`
- `rawinput/Contrat complet de validation  Job match kpi benchmark.md`
- `rawinput/Dev-only advisory beta access for everyone.md`
- `rawinput/GIT - GOOD HABIT -SKILL.md`
- `rawinput/Implementation Handoff — 2026 Elite Design System (Phases 1–4) (DONE VERIFIER SI VRAIMENT PLEINEMENT IMPLEMENTÉ SANS DRIFT).md`
- `rawinput/Job Library PRD.md`
- `rawinput/Match Review V1 Dogfood Tool — Developer  LLM Note.md`
- `rawinput/Meta-prompt maître.md`
- `rawinput/Note — système de tests du repo.md`
- `rawinput/TEST Headless browser setup for workshop preview probe.md`
- `rawinput/Twoweeks.ai Motion System — Implementation Hardening Pass -PR1 ,PR2,PR3.md`
- `rawinput/Twoweeks.ai — Brand Voice Card.md`
- `rawinput/Twoweeks.ai — Motion System.md`
- `rawinput/Typography Token Audit Table.md`
- `rawinput/UI design audit - prompt.md`
- `rawinput/VOICE CARD.md`
- `rawinput/Workshop Pagination.md`
- `rawinput/audit token workspace -en cours.md`
- `rawinput/brand Twoweeks.ai.md`
- `rawinput/brand logo system.md`
- `rawinput/claude light mode .md`
**Pages créées** :
- `wiki/product/job-library.md`
- `wiki/product/job-match-review.md`
- `wiki/design/motion-system.md`
- `wiki/design/logo-system.md`
- `wiki/design/elite-design-system.md`
- `wiki/tech/workshop-pagination.md`
- `wiki/tech/workshop-token-parity.md`
- `wiki/tech/repo-testing-system.md`
- `wiki/howto/headless-workshop-preview-probe.md`
- `wiki/howto/git-branch-hygiene.md`
- `wiki/meta/codex-prompting-standards.md`
- 23 pages source dans `wiki/sources/`
**Pages mises à jour** :
- `wiki/overview.md`
- `wiki/index.md`
- `wiki/log.md`
- `wiki/design/brand-voice.md`
- `wiki/design/document-token-contract.md`
- `wiki/product/kpis.md`
- `wiki/product/product-roadmap.md`
- `wiki/tech/export-pipeline.md`
- `wiki/tech/preview-to-print-pipeline.md`
**Pages archivées** :
- aucune
**Points notables** :
- `rawinput/` vidé sauf `README.md`
- fichiers source déplacés vers `raw/`
- les sources brand voice ont été dédupliquées vers une seule page durable `wiki/design/brand-voice.md`
- le fichier vide `rawinput/.md` a été conservé comme source vide sans page durable

## 2026-06-22 — Cover-letter quality roadmap PR1 published

**Pages mises à jour** :
- `wiki/tasks/2026-06-22-cover-letter-quality-production-roadmap.md`
- `wiki/hot.md`
- `wiki/log.md`

**Points notables** :
- PR1 `codex/premium-provenance-finalization` a été implémentée, relue en session indépendante, poussée, puis ouverte comme <https://github.com/panamini/neyssan/pull/230>.
- PR2 `legacy cover-letter prompt` est le prochain travail séquentiel recommandé.

## 2026-06-22 — Cover-letter quality roadmap PR2 published

**Pages mises à jour** :
- `wiki/tasks/2026-06-22-cover-letter-quality-production-roadmap.md`
- `wiki/hot.md`
- `wiki/index.md`
- `wiki/log.md`

**Points notables** :
- PR2 `codex/legacy-cover-letter-prompt` a été implémentée, relue en session indépendante, poussée, puis ouverte comme <https://github.com/panamini/neyssan/pull/231>.
- Le statut roadmap note que PR3 doit rester bornée au prompt premium V2, Mistral first, avec flag et baseline.

## 2026-06-22 — Cover-letter quality roadmap PR3 published

**Pages mises à jour** :
- `wiki/tasks/2026-06-22-cover-letter-quality-production-roadmap.md`
- `wiki/hot.md`
- `wiki/index.md`
- `wiki/log.md`

**Points notables** :
- PR3 `codex/premium-cover-letter-prompt-v2-mistral` a été implémentée, relue en session indépendante, poussée, puis ouverte comme <https://github.com/panamini/neyssan/pull/232>.
- Le statut roadmap note que PR4 doit rester bornée à une réparation `qualityShadow` unique et réversible.

## 2026-06-24 — MCP auth policy boundary checkpoint PR87.13 merged

**Pages créées** :
- `wiki/sources/2026-06-24-pr87-13-mcp-auth-policy-boundary-checkpoint.md`

**Pages mises à jour** :
- `wiki/product/chatgpt-app-sdk-roadmap.md`
- `wiki/hot.md`
- `wiki/index.md`
- `wiki/log.md`

**Points notables** :
- PR254 `PR87.13: add MCP auth metadata and policy boundary` merged into `application-os-foundation` as `b23a83b3d9652093f7cbb79b1fd7fe5f7e2c1b49`.
- The merged head was `fb319b565e593a01f93c03d2e1fd06b7b6a5c4cc`; changed files stayed limited to `mcpAuthPolicyBoundary.ts`, its focused test, and `mcpAccountLinkingStorageBoundary.ts`.
- Focused boundary tests passed 89/89; adjacent local-MCP tests passed 79/79; the full local-MCP suite passed 57 files / 1290 tests; typecheck, targeted ESLint, diff checks, GitHub checks, and CodeRabbit no-actionable review were verified before merge.
- CodeRabbit's docstring coverage item remained advisory only and was not treated as a required blocking check.
- This remains pure policy/metadata only: runtime auth wiring, production MCP endpoints, production `tools/list`/`tools/call`, OAuth runtime, Clerk runtime, Stytch runtime, Convex runtime, real handlers, real data, outbound/model calls, live submit/apply, approved-answer copy, billing, PR88, and PR89 remain blocked.

## 2026-06-24 — MCP dev fixture demo checkpoint PR87.12 merged

**Pages créées** :
- `wiki/sources/2026-06-24-pr87-12-mcp-dev-fixture-demo-checkpoint.md`

**Pages mises à jour** :
- `wiki/product/chatgpt-app-sdk-roadmap.md`
- `wiki/hot.md`
- `wiki/index.md`
- `wiki/log.md`

**Points notables** :
- PR253 `PR87.12: add local/dev MCP fixture demo` merged into `application-os-foundation` as `ccd0e5d9b5a62722ec163e6b282e2e43619b33fe`.
- The merged head was `97bbe4b40c8028f331fabdb508b5bd67a070aa60`; changed files stayed limited to `localMcpDevEndpoint.ts`, its focused test, and `vite.config.ts`.
- Focused endpoint tests passed 17/17; the full local-MCP suite passed 56 files / 1201 tests; typecheck, targeted ESLint, GitHub checks, and CodeRabbit blocking review resolution were verified before merge.
- MCP Inspector was unavailable and live ChatGPT smoke was not run. Protocol-level HTTP smoke covered the fixture boundary.
- This remains local/dev fixture-only: production MCP endpoints, production `tools/list`/`tools/call`, OAuth, real handlers, real data, outbound/model calls, live submit/apply, approved-answer copy, billing, PR88, and PR89 remain blocked.

## 2026-06-22 — Cover-letter quality roadmap PR4 published

**Pages mises à jour** :
- `wiki/tasks/2026-06-22-cover-letter-quality-production-roadmap.md`
- `wiki/hot.md`
- `wiki/index.md`
- `wiki/log.md`

**Points notables** :
- PR4 `codex/quality-shadow-repair` a été implémentée, vérifiée, poussée, puis ouverte comme <https://github.com/panamini/neyssan/pull/233>.
- La réparation `qualityShadow` reste une tentative unique et bornée; si elle casse validation, JSON, amélioration ou provenance finale, la sortie originale sûre est conservée.

## 2026-06-23 — Release orchestration checkpoint: staging blocked, PR87.8 still blocked

**Pages créées** :
- `wiki/sources/2026-06-23-release-orchestration-staging-pr87-8-checkpoint.md`

**Pages mises à jour** :
- `wiki/tasks/2026-06-22-cover-letter-quality-production-roadmap.md`
- `wiki/product/chatgpt-app-sdk-roadmap.md`
- `wiki/hot.md`
- `wiki/index.md`
- `wiki/log.md`

**Points notables** :
- Child A returned `STAGING_BLOCKED`: Convex staging target `dev:neat-starfish-33` was identified, but authenticated env access failed with `401 Unauthorized: MissingAccessToken`; no flags changed and no deployed smoke ran.
- Child B returned `PR87_8_GATE_STILL_BLOCKED`: PR80B manual handoff remains implemented, while production MCP endpoints, tool calls, OAuth, live submit/apply, approved-answer copy, provider-verified submission, billing, PR88, and PR89 remain blocked.
- No application code changed, no application PR opened, no production behavior enabled, and the local application roadmap mirror remained untouched.

## 2026-06-23 — Release orchestration correction: staging flag rolled back

**Pages mises à jour** :
- `wiki/sources/2026-06-23-release-orchestration-staging-pr87-8-checkpoint.md`
- `wiki/tasks/2026-06-22-cover-letter-quality-production-roadmap.md`
- `wiki/hot.md`
- `wiki/index.md`
- `wiki/log.md`

**Points notables** :
- Follow-up found the Convex auth issue was caused by using `convex env --env-file`; sourcing root `.env.local` allowed the CLI to combine deployment selection with the global Convex token.
- Previous staging flag values were unset. `cover_letter_premium_prompt_v2=on` was applied to `dev:neat-starfish-33`, then rolled back after staging rejected `mistral-medium-latest` at `/test/generate` argument validation.
- Rollback verification confirmed the three Mistral V2 flag names and `ENABLE_COVER_LETTER_QUALITY_REPAIR_V1` are unset again. Production remained untouched.

## 2026-06-24 — Cover-letter Mistral V2 staging green checkpoint

**Pages créées** :
- `wiki/sources/2026-06-24-cover-letter-mistral-v2-staging-green.md`

**Pages mises à jour** :
- `wiki/tasks/2026-06-22-cover-letter-quality-production-roadmap.md`
- `wiki/hot.md`
- `wiki/index.md`
- `wiki/log.md`

**Points notables** :
- Decision recorded: `COVER_LETTER_MISTRAL_V2_STAGING_GREEN`, superseding `COVER_LETTER_MISTRAL_V2_READY_FOR_INTERNAL_STAGING_ONLY`.
- Convex staging `dev:neat-starfish-33` was synced after stale function spec and stale schema-data blockers were cleared; 28/28 old invalid `proposalHandoffs` missing `handoffToken` were removed, all older than 24h.
- `npx convex dev --once` completed and the deployed function spec now includes `mistral-medium-latest` and `qwen3.7-max`.
- Only canonical staging flag `cover_letter_premium_prompt_v2=1` was enabled; aliases remained unset, quality repair remained OFF, and path flags stayed unchanged.
- Staging smoke returned `STAGING_GREEN`: 8/8 PASS, no PR246 forbidden terms, no PR248 no-CV leakage, GPT stayed on GPT, Qwen stayed legacy-only, production untouched, no app PR/MCP/source-code changes.

## 2026-06-30 — MCP policy kernel and tools/list metadata checkpoint PR101 merged

**Pages créées** :
- `wiki/sources/2026-06-30-pr101-mcp-policy-kernel-tools-list-checkpoint.md`

**Pages mises à jour** :
- `wiki/product/chatgpt-app-sdk-roadmap.md`
- `wiki/hot.md`
- `wiki/index.md`
- `wiki/log.md`

**Points notables** :
- PR288 `PR99.3: harden MCP bearer quota caller key canonicalization` merged into `application-os-foundation` as `f1b233b0069b12872ea25ffc7c3594eba956ffdf`.
- PR289 `PR100: add authenticated MCP protocol and session envelope boundary` merged into `application-os-foundation` as `dc02d692a47be673ade48ba5a1de1842807532da`.
- PR290 `PR101: add MCP policy kernel and tools/list metadata boundary` merged into `application-os-foundation` as `44c70ddcad5f4bcf36e5076ec0a7c67a0facf395`.
- Production `/mcp` can now verify bearer tokens, apply trusted caller quota, run the authenticated JSON-RPC protocol shell, and return authenticated metadata-only `tools/list`.
- `tools/call`, MCP execution, provider calls, write actions, refresh tokens, production account-link lifecycle expansion, private beta, public launch, and UI changes remain blocked.
- The next app PR is PR102 `tools/call` read-only boundary plus hardening.

## 2026-06-30 — MCP tools/call and schema matcher hardening checkpoint PR102/PR103 merged

**Pages créées** :
- `wiki/sources/2026-06-30-pr102-pr103-mcp-tools-call-schema-hardening-checkpoint.md`

**Pages mises à jour** :
- `wiki/product/chatgpt-app-sdk-roadmap.md`
- `wiki/hot.md`
- `wiki/index.md`
- `wiki/log.md`

**Points notables** :
- PR291 `PR102: add MCP tools/call read-only boundary and hardening` merged into `application-os-foundation` as `1a18564865313fad679d9ae2268fb561b1cf16c8`.
- PR292 `PR103: add MCP schema normalization and matcher hardening` merged into `application-os-foundation` as `d269069922cd3e4e183223891f1fb175a9bbe568`.
- Production `/mcp` can now verify bearer tokens, apply trusted caller quota, run the authenticated JSON-RPC protocol shell, return authenticated metadata-only `tools/list`, and accept validated read-only `tools/call`.
- Provider calls, write actions, outbound HTTP/model calls, refresh tokens, production account-link lifecycle expansion, private beta, public launch, and UI changes remain blocked.
- The next app PR is PR104 private beta gate.

## 2026-07-01 — MCP read-only summary execution checkpoint PR106 merged

**Pages créées** :
- `wiki/sources/2026-07-01-pr106-mcp-readonly-summary-execution-checkpoint.md`

**Pages mises à jour** :
- `wiki/product/chatgpt-app-sdk-roadmap.md`
- `wiki/hot.md`
- `wiki/index.md`
- `wiki/log.md`

**Points notables** :
- PR296 `Add production MCP readonly summary executor` merged into `application-os-foundation` as `557b7799eedd6a7605c1da74baa62357974e6629`.
- Production `/mcp` validated read-only `tools/call` now executes the four existing Convex internal summary queries after bearer auth, quota, private-beta, launch-readiness, policy, and tools-call validation.
- The executor accepts only mapped public safe ref IDs, uses server-only owner identity, validates safe result kinds, and maps dependency/query/stalled/malformed failures to safe `Read-only summary unavailable.` errors.
- Provider calls, writes/mutations, outbound HTTP/model calls, OAuth/token issuance changes, refresh tokens, account-link lifecycle expansion, public launch, UI changes, export/send/submit/apply, and billing/entitlements remain blocked.

## 2026-07-01 — MCP tools/call synthetic metadata cleanup checkpoint PR300 merged

**Pages créées** :
- `wiki/sources/2026-07-01-pr300-mcp-tools-call-synthetic-metadata-cleanup-checkpoint.md`

**Pages mises à jour** :
- `wiki/product/chatgpt-app-sdk-roadmap.md`
- `wiki/hot.md`
- `wiki/index.md`
- `wiki/log.md`

**Points notables** :
- PR300 `Remove stale production tools-call synthetic metadata` merged into `application-os-foundation` as `d0141ea1ec3a5b21598190bb62e3577779421fd9`.
- Active production `tools/call` boundary no longer exports or builds stale PR102 synthetic result kind/type/builder/status/phase metadata.
- PR106 read-only summary execution and PR107 status normalization remain the real output/status owners.
- Validation recorded on PR300: local Vitest boundary/route and executor/status-normalizer tests, TypeScript, `diff --check`, Fallow audit, GitHub CI/Playwright/Semgrep, Codex Review, and Qodo review passed or reported no material issues.
- Provider calls, writes/mutations, outbound HTTP/model calls, OAuth/token issuance changes, refresh tokens, account-link lifecycle expansion, public launch, UI changes, export/send/submit/apply, approved-answer copy, and billing/entitlements remain blocked.

## 2026-07-01 — MCP readiness diagnostics checkpoint PR301 merged

**Pages créées** :
- `wiki/sources/2026-07-01-pr301-mcp-readiness-diagnostics-checkpoint.md`

**Pages mises à jour** :
- `wiki/product/chatgpt-app-sdk-roadmap.md`
- `wiki/hot.md`
- `wiki/index.md`
- `wiki/log.md`

**Points notables** :
- PR301 `PR301: Add MCP readiness cleanup diagnostic evidence` merged into `application-os-foundation` as `149ef8e8fbbb46bab0435f04eb1487c1b78b0040`.
- Launch-readiness evidence now accepts optional strict boolean `toolsCallSyntheticMetadataCleanupReviewed` from `MCP_OAUTH_PRODUCTION_LAUNCH_TOOLS_CALL_SYNTHETIC_METADATA_CLEANUP_REVIEWED`.
- The PR301 field is diagnostic-only and remains outside readiness completeness, so false or missing diagnostic evidence does not block an otherwise complete readiness decision.
- Malformed non-boolean diagnostic evidence still fails closed as `launch_config_invalid`.
- Local tests, TypeScript, `diff --check`, Fallow audit, GitHub CI/Playwright/Semgrep, Codex Review, CodeRabbit status, and Qodo summary/review-thread checks were recorded before merge.
- Provider calls, writes/mutations, outbound HTTP/model calls, OAuth/token issuance changes, refresh tokens, account-link lifecycle expansion, public launch, UI changes, export/send/submit/apply, approved-answer copy, and billing/entitlements remain blocked.

## 2026-07-02 — MCP Stage 3 read-side materialization checkpoint PR302/PR303 merged

**Pages créées** :
- `wiki/sources/2026-07-02-pr302-pr303-mcp-stage3-readside-materialization-checkpoint.md`

**Pages mises à jour** :
- `wiki/product/chatgpt-app-sdk-roadmap.md`
- `wiki/hot.md`
- `wiki/index.md`
- `wiki/log.md`

**Points notables** :
- PR302 `Add MCP Stage 3 read-side materialization` merged into `application-os-foundation` as `262444e5ea4ed24e493fd93599452ddb56a0c317`.
- PR303 `Post-merge Stage 3 MCP proof` merged into `application-os-foundation` as `f63d35dc6f8ae765d9afb004991e2a2aeb6c5679`.
- PR302 materializes safe Stage 3 MCP read-side `applicationContexts` and `applicationPackages` from proposal save/update paths and reconciles stale derived rows when jobs, profiles, ownership, or proposals become invalid.
- PR303 records a proof-only audit and adds a focused regression for owner-profile deletion cleanup; it does not grant runtime or production permission.
- PR303 was marked ready and merged after green GitHub checks, latest-head Codex review with no major issues, CodeRabbit full-review completion, and Qodo review updated to the latest head with no new findings.
- Provider calls, write actions, outbound HTTP/model calls, refresh tokens, account-link lifecycle expansion, production/shared database access, public launch, UI changes, export/send/submit/apply, approved-answer copy, and billing/entitlements remain blocked.

## 2026-07-04 — PR304 live MCP connector smoke and tunnel runbook

**Pages créées** :
- `wiki/sources/2026-07-04-pr304-live-mcp-connector-smoke-checkpoint.md`
- `wiki/howto/chatgpt-mcp-private-beta-tunnel-connector.md`

**Pages mises à jour** :
- `wiki/product/chatgpt-app-sdk-roadmap.md`
- `wiki/hot.md`
- `wiki/index.md`
- `wiki/log.md`

**Points notables** :
- Draft PR304 `PR304: prove live MCP connector smoke` was opened against `application-os-foundation`.
- The local/private-beta proof used an ephemeral Cloudflare quick tunnel, `https://are-effort-skirts-hints.trycloudflare.com`, created with `cloudflared tunnel --config /dev/null --no-autoupdate --loglevel info --protocol http2 --url http://localhost:5187`.
- `--config /dev/null` avoided the local default cloudflared config that otherwise routed quick tunnels to `http_status:404`.
- A real ChatGPT connector completed OAuth and called `twoweeks.application_package.summarize`, returning `status=available`, `count=1`, and real read-side data.
- The new French runbook documents the manual tunnel creation, ChatGPT connector OAuth fields, login expectations for Google/Clerk, smoke args, troubleshooting, and cleanup.
- Provider calls, write actions, refresh tokens, billing, production/shared database mutation, public launch, raw data logging, and durable production deployment remain blocked.
