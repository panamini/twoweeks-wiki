---
aliases:
  - Twoweeks MCP / ChatGPT App SDK Roadmap Checkpoint
---
# 

Date: 2026-06-23  
Purpose: keep track of where we are in the real MCP/App SDK roadmap while the current release/canary troubles are still being stabilized.  
Status: `CHECKPOINT_ONLY_DO_NOT_IMPLEMENT_FROM_THIS_FILE_DIRECTLY`

## Correction

This checkpoint is about the real Twoweeks MCP / ChatGPT App SDK product track.

It is not about the old placeholder `mcp-client.ts` alone.

The actual project is the full Twoweeks tool surface that can be accessed from ChatGPT/Codex-style agents to:

```txt
1. expose Twoweeks tools safely;
2. summarize and review real Twoweeks application data;
3. generate professional resume, cover-letter, application-message, and package artifacts;
4. require human approval before risky or outward actions;
5. export/download/send/apply only with explicit confirmation;
6. run with auth, consent, privacy, redacted audit, rate limits, rollback, and production monitoring.
```

Canonical roadmap sources:

```txt
docs/plans/2026-06-12-chatgpt-app-implementation-roadmap-agent-contract.md
docs/plans/2026-06-12-chatgpt-app-roadmap-progress-ledger.md
```

Do not infer roadmap progress from old placeholder files alone.

## Current known base

Latest confirmed release-trouble checkpoint:

```txt
application-os-foundation:
2ceb98d071b51e87a368dc3d01f33d7ce147f724

PR245:
Harden GPT premium cover-letter finalization
Merged: yes
Post-merge flags-off smoke: clean
```

Post-merge smoke reported clean:

```txt
GPT premium cover letter: PASS
Mistral medium premium V2 OFF: PASS
Mistral large premium V2 OFF: PASS
No-CV Mistral: PASS
Qwen flags OFF legacy path: PASS
```

Current feature posture:

```txt
Mistral V2 canary: GO for small internal canary only
Quality repair: OFF / NO-GO
Full production GO: not yet
```

## Actual roadmap position

We are not at early MCP skeleton.

We are around:

```txt
PR87 / production deployment gate
+ release stabilization
+ post-PR245 canary planning
```

The roadmap has already passed the early MCP/App SDK phases.

## What is already merged

### PR41-PR52 — Non-production ChatGPT/MCP demo foundation

Status: merged according to the roadmap ledger.

Includes:

```txt
PR41  Agent roadmap contract
PR42  Package-only MCP SDK dependency
PR43  Dependency import boundary
PR44  Descriptor adapter contract tests
PR45  Static descriptor registry
PR46  Disabled local MCP server skeleton
PR47  Fixture-only tools/list simulation
PR48  Fixture-only tools/call simulation
PR49  Golden safety tests
PR50  Disabled local dev transport adapter
PR51  Dev-only /mcp endpoint behind flag
PR52  Fake ChatGPT flow demo
```

Meaning:

```txt
The product is not merely planned.
A local non-production MCP/App SDK surface already exists in the roadmap history.
```

### PR53-PR64 — Auth, consent, privacy, and real read-only integration

Status: merged according to the roadmap ledger.

Key milestones:

```txt
PR53  Auth/OAuth decision
PR54  Auth/OAuth blocked boundary guards
PR55  Consent gate
PR56  Redacted audit log
PR57  Retention and deletion
PR58  Semantic privacy test harness
PR59  Read-only Twoweeks data adapter
PR60  Real application package summary
PR61  Real evidence graph summary
PR62  Real resume variant plan summary
PR63  Real review cockpit summary
PR64  Real read-only E2E ChatGPT test
```

Meaning:

```txt
The first useful real-data read-only ChatGPT/MCP integration milestone has already been crossed.
```

### PR65-PR67 — Component / UI experience

Status: merged according to the roadmap ledger.

Includes:

```txt
PR65  Component/UI data policy
PR66  Read-only review component
PR67  Component error/loading/refusal UX
```

Important rule:

```txt
_meta is not a privacy boundary.
```

### PR68-PR75 — Artifact generation, approval, revision, export

Status: merged according to the roadmap ledger.

Includes:

```txt
PR68  Generated artifact boundary
PR69  Resume variant generation preview
PR70  Cover letter / application message preview
PR71  Human approval workflow
PR72  Artifact revision loop
PR73  Export/download policy
PR74  Resume export
PR75  Cover letter / application package export
```

Meaning:

```txt
The product has local controlled artifact-generation/export boundaries.
```

### PR76-PR80 — Write-action foundations and manual handoff

Status: merged through manual handoff path, with live submit/apply still blocked.

Includes:

```txt
PR76  Write action framework
PR77  Outbound egress allowlist and SSRF protection
PR78  Send application email/message, manual confirmation only
PR79  Job platform submit/apply dry run
PR80A Durable live external-action safety foundation
PR80B Safe application handoff while ATS authorization is pending
PR80B follow-up: approved manual-handoff artifact delivery
```

Still blocked:

```txt
PR80-live submit/apply
Approved answer copy
```

### PR81-PR85 — Production-readiness hardening

Status: merged.

Includes:

```txt
PR81  Rate/budget/abuse protection for manual handoff and controlled flows
PR82  MCP/Stytch config and account-link hardening
PR83  Observability and incident-response helpers/runbook
PR84  Owner/profile boundary hardening
PR85  Stripe test-mode boundary and internal test access
```

Meaning:

```txt
Some production-hardening surfaces exist, but production launch is still blocked.
```

### PR86-PR87 — Audit and production gate

PR86 founder smoke / pre-launch audit merged, but recorded blockers.

PR87 production deployment gate merged as a governance/status gate and returned:

```txt
BLOCKED_PRODUCTION_GATE
```

Known blocker categories from PR87 history:

```txt
- production build was red at the first PR87 gate;
- lint had boundary/debt blockers;
- runtime dependency audit was red;
- preview/staging target was not fully proven;
- MCP production runtime was not deployable;
- signed-in smoke was missing;
- runtime observability and rollback were not fully proven;
- PR88 private beta remained blocked;
- PR89 public launch remained blocked;
- PR80-live remained blocked;
- approved answer-copy remained blocked.
```

Follow-up work after PR87:

```txt
PR87.5  Production TypeScript build follow-up
PR87.6  TS6307 project-membership build fix
PR242   Lint config boundary
PR243   Proposal body composer contract / release gate fix
PR244   Playwright browser install workflow fix
PR245   GPT premium cover-letter finalization hardening
```

## Current interpretation

Current status:

```txt
Roadmap stage: PR87 / production gate reconciliation
Not at: early MCP skeleton
Not at: PR59 preflight
Not at: PR64 read-only E2E
Not ready for: PR88 private beta or PR89 public launch
```

The project has moved far into the roadmap, but the launch path is still blocked by release-gate and production-readiness questions.

## Immediate do-not-touch list

Do not start these while current trouble/canary stabilization is unresolved:

```txt
- broad lint cleanup;
- quality repair enablement;
- full production launch;
- PR88 private beta;
- PR89 public launch;
- PR80-live submit/apply;
- approved answer-copy implementation;
- production billing beyond existing Stripe test-mode boundary;
- broad OAuth/token/provider runtime expansion;
- browser automation or live ATS submission;
- package/lockfile changes outside a specific approved PR.
```

## Remaining tasks after current troubles are quiet

### A. Finish current release stabilization

- [ ] Keep quality repair OFF.
- [ ] Run only a small internal Mistral V2 canary.
- [ ] Record Mistral V2 canary results with exact telemetry.
- [ ] Confirm no quality repair is attempted during Mistral V2 canary.
- [ ] Confirm GPT premium remains clean after PR245.
- [ ] Confirm Mistral medium and large stay clean with V2 OFF.
- [ ] Confirm Qwen remains legacy-only with premium flags OFF.
- [ ] Confirm no-CV remains safe and does not gain fake CV provenance.
- [ ] If Mistral V2 canary fails, disable/park it without touching quality repair.
- [ ] If Mistral V2 canary passes, decide whether it remains internal-only or expands gradually.

### B. Reconcile PR87 production gate after PR245

Recommended next roadmap checkpoint:

```txt
PR87.8 - Production Gate Reconciliation After PR245
```

Goal:

```txt
Answer exactly what still blocks PR88/private beta and PR89/public launch after PR245 and flags-off smoke are green.
```

Checklist:

- [ ] Update `docs/plans/2026-06-12-chatgpt-app-roadmap-progress-ledger.md`.
- [ ] Record current `application-os-foundation` SHA.
- [ ] Record PR245 merge SHA.
- [ ] Record flags-off smoke results.
- [ ] State which PR87 blockers are fixed.
- [ ] State which PR87 blockers remain.
- [ ] Confirm current build status.
- [ ] Confirm current lint status.
- [ ] Confirm current npm audit/runtime dependency audit status.
- [ ] Confirm current Playwright status.
- [ ] Confirm signed-in smoke status.
- [ ] Confirm preview/staging target status.
- [ ] Confirm monitoring/incident/rollback status.
- [ ] Confirm PR88 remains blocked or becomes eligible.
- [ ] Confirm PR89 remains blocked.

### C. Keep the MCP/App SDK roadmap accurate

- [ ] Treat canonical roadmap + progress ledger as source of truth.
- [ ] Do not infer MCP state from old `mcp-client.ts` alone.
- [ ] Verify actual `my-app/src/modules/local-mcp/**` modules before any new MCP work.
- [ ] For each future PR, generate a PR-local implementation brief from the canonical roadmap, ledger, repo state, and GitHub PR state.
- [ ] Do not invent new PR numbers.
- [ ] Do not reorder PRs.
- [ ] Do not combine PRs unless explicitly approved.

### D. Blocked product areas needing decisions

#### PR80-live submit/apply

Still blocked until:

- [ ] provider authorization exists;
- [ ] credentials exist in safe env only;
- [ ] test tenant exists;
- [ ] test posting exists;
- [ ] provider-specific safety review is done;
- [ ] final preview, confirmation, idempotency, audit, and rollback are proven;
- [ ] no browser automation unless explicitly approved.

#### Approved answer copy

Still blocked until:

- [ ] authoritative owner-scoped approved answer source exists;
- [ ] answer is tied to exact provider question/prompt;
- [ ] human approval state is fresh;
- [ ] retention/delete policy exists;
- [ ] copy/export logic uses only that authoritative source.

#### Production billing / entitlements

Still blocked until:

- [ ] founder-approved production pricing/product mode exists;
- [ ] plan names and tiers are decided;
- [ ] production payment provider decision is made;
- [ ] checkout/webhook/subscription source of truth is designed;
- [ ] entitlement source and revocation model are designed;
- [ ] billing record privacy/retention model exists.

#### PR88 / PR89 launch

Still blocked until:

- [ ] production gate is green or explicitly waived with evidence;
- [ ] build/lint/audit gates are acceptable;
- [ ] staging/preview and signed-in smoke pass;
- [ ] runtime monitoring and incident response are ready;
- [ ] kill switches are verified;
- [ ] rollback plan is verified;
- [ ] feature flags are intentional;
- [ ] quality repair remains OFF unless separately approved;
- [ ] private beta allowlist/support/feedback path exists.

## Standing per-PR agent rule

Before implementing any roadmap PR, create a PR-local implementation brief derived from:

```txt
AGENTS.md
canonical roadmap
roadmap progress ledger
current repo files
current GitHub PR state
merged decisions
```

The PR-local brief must include:

```txt
- current PR number and title;
- base branch and proposed branch name;
- exact roadmap section controlling the PR;
- merged decisions that narrow or constrain the PR;
- files to read before coding;
- files proposed to touch;
- files forbidden to touch;
- exact allowed scope;
- exact forbidden scope;
- expected tests;
- expected grep/source guards;
- acceptance criteria;
- rollback plan;
- READY_TO_IMPLEMENT or BLOCKED.
```

High-risk PRs must stop after the PR-local brief and wait for maintainer approval.

High-risk includes:

```txt
- real data selectors;
- OAuth/auth/token changes;
- Convex reads/writes;
- handlers;
- production connector/runtime;
- export/download/send/submit/apply;
- live provider actions;
- package/lockfile changes;
- security/privacy gates;
- production deployment gates.
```

## Next exact prompt to use when current trouble is quiet

```txt
You are a senior engineer. Prepare PR87.8 only.

Goal:
Reconcile the production deployment gate after PR245 and flags-off smoke.

Read first:
- AGENTS.md
- docs/plans/2026-06-12-chatgpt-app-implementation-roadmap-agent-contract.md
- docs/plans/2026-06-12-chatgpt-app-roadmap-progress-ledger.md
- docs/plans/2026-06-21-pr87-production-deployment-gate.md
- recent PRs: PR242, PR243, PR244, PR245

Rules:
- Do not implement runtime features.
- Do not enable flags.
- Do not start lint cleanup.
- Do not enable quality repair.
- Do not start PR88 or PR89.
- Do not start PR80-live.
- Do not implement approved answer copy.
- Do not change packages or lockfiles.

Output:
A docs/test/status PR-local brief that answers:
1. What PR87 blockers are fixed after PR245?
2. What PR87 blockers remain?
3. Is PR88 still blocked?
4. What is the exact next narrow unblock PR, if any?

Status must be:
READY_TO_IMPLEMENT_NARROW_PR87_8
or
BLOCKED_ON_RELEASE_STABILIZATION
```

## Final recommendation

For now:

```txt
Do not restart broad implementation.
Do not restart lint cleanup.
Do not enable quality repair.
Do not launch PR88/PR89.
Run/record the small Mistral V2 internal canary.
Then do PR87.8 production gate reconciliation.
```
