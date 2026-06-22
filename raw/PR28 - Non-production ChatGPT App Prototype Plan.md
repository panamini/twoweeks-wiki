# 

Date: 2026-06-11
Status: planned spec
Scope: docs-only plan for a safe, non-production ChatGPT App prototype.

## 1. Objective

Define the safe path for a future non-production ChatGPT App prototype using the existing Local MCP boundaries.

This PR is a plan. It does not start the prototype.

The future prototype should show what Twoweeks could expose to ChatGPT later, without exposing real user data, real handlers, production transport, or outbound actions.

## 2. Planning boundary

OpenAI Apps SDK work is organized around planning, building, and deploying. PR28 stays in planning only.

### Plan - allowed in PR28

- research use cases
- define candidate tools
- define mock/demo surfaces
- define component intentions
- define safety gates
- define review requirements
- define rollback and kill-switch expectations

### Build - forbidden in PR28

- no server
- no ChatGPT UI
- no Apps SDK code
- no authentication
- no state management
- no MCP runtime
- no SDK package
- no API route
- no local tunnel
- no remote connection

### Deploy - forbidden in PR28

- no ChatGPT connection
- no test integration
- no app submission
- no production review
- no marketplace or distribution work
- no public endpoint
- no real user access

## 3. Prototype shape

The future prototype is:

- local-only
- mock-only
- non-production
- review-only
- no real user data
- no real handlers
- no network transport
- no persistence
- no outbound actions

| Prototype area | PR28 decision | Why |
| --- | --- | --- |
| Tool list | derived from PR25 | visibility must fail closed |
| Gate result | derived from PR27 and PR27.1 | privacy review controls exposure |
| Copy | derived from PR26 | no improvised UX copy |
| Output data | derived from PR24 | no raw or private leaks |
| Handler | blocked by PR21 | no real execution |
| Transport | blocked by PR22 | no remote runtime |
| Approval | derived from PR20 | no action without approval |
| Schema | derived from PR18 | only projected safe descriptors |
| Call shape | derived from PR19 | envelope is non-executable unless later approved |

## 4. Allowed surfaces

PR28 allows documentation for these future mock/demo surfaces only:

- mock/demo output surfaces
- Local MCP dry-run outputs
- PR18 projected descriptors for reference
- PR19 call envelope examples, non-executable
- PR20 approval and audit shells
- PR21 handler boundary states, design-only
- PR22 remote transport preflight evidence, disabled and non-production reference only
- PR23 UX/privacy spec examples
- PR24 privacy/redaction fixtures
- PR25 visibility policy decisions
- PR26 approval UX copy fixtures
- PR27 privacy review gate decisions
- PR27.1 privacy review gate hardening decisions

No surface created by PR28 can execute, persist, deploy, authenticate, transport, export, send, submit, or apply.

## 5. Forbidden real surfaces

PR28 forbids:

- ChatGPT App code
- Apps SDK package or code
- production transport
- enabled remote transport
- MCP server
- OAuth
- Convex persistence or functions
- UI routes, pages, or components
- real handlers
- export
- download
- email send
- application submit
- job apply
- auto-apply
- deployment
- real user data
- real CV text
- real resume text
- real cover letter text
- real job description text
- browser scraping
- LinkedIn scraping
- Upwork scraping
- Indeed scraping
- ATS scraping
- job-board scraping
- connector-based raw document dumps

## 6. Data policy

Only synthetic, fake, or fixture data is allowed in future prototype planning.

Allowed:

- fake tool names
- fake job IDs
- fake package references
- safe summaries
- redacted fixture output
- PR24 sentinel tests
- PR26 fixed copy strings
- PR27 gate statuses
- PR27.1 safe summaries

Forbidden:

- raw source documents
- raw CV or resume text
- raw cover letter text
- complete generated resume text
- complete generated cover letter text
- private facts
- `never_use` facts
- source quote dumps
- secrets
- tokens
- session details
- stack traces
- raw arguments
- real contact details
- real employer/user/job source payloads
- origin or host payloads

## 7. Prototype constraints

- All tools default hidden unless explicitly allowed by a future prototype review.
- Any tool visibility must come from PR25.
- Any external-style exposure must pass PR27 and PR27.1.
- Approval is required for any future action.
- Audit shell presence is required before a tool can be shown as reviewable.
- PR22 transport may be referenced only as disabled preflight evidence.
- No runtime transport is enabled by this plan.
- Safe summary only.
- Copy must follow PR23 and PR26: short, direct, no hype, no filler.
- All prototype outputs must be derivable from PR20-PR27.1 fixtures or decisions.
- `ready_for_internal_review` is not execution readiness.
- `ready_for_internal_review` is not production readiness.
- `ready_for_internal_review` is not ChatGPT App readiness.
- `ready_for_internal_review` is not remote approval.
- `ready_for_internal_review` is not handler approval.

## 8. PR27.1 gate hardening

PR27.1 is mandatory context for any future prototype review.

The gate remains fail-closed:

- missing visibility blocks
- hidden, disabled, admin-disabled, or privacy-blocked visibility blocks
- missing privacy review blocks
- missing privacy check blocks
- unsafe PR24 privacy check blocks
- denied approval blocks
- missing audit blocks when audit is required
- missing handler boundary blocks when handler boundary is required
- invalid handler boundary blocks
- missing remote transport preflight blocks when remote preflight is required
- blocked remote transport preflight blocks
- invalid copy blocks

Review-only states stay review-only:

- missing approval may return `review_required`, not runnable
- missing copy may return `review_required`, not runnable
- `manual_review_required` is not approval to expose
- `all_design_gates_present` is not approval to execute
- `isLocalMcpPrivacyReviewGatePassedForInternalReview` is review evidence only

Gate output must stay bounded:

- use PR26 copy only
- use approved safe summaries only
- return reason categories only
- never return raw arguments
- never return raw source text
- never return private facts
- never return `never_use` facts
- never return source quote dumps
- never return stack traces
- never return user or session IDs
- never return secrets or tokens
- never return origin or host payloads

Allowed PR27.1 safe summaries:

```txt
Blocked. Review privacy.
Approval required.
Denied. Nothing ran.
Audit unavailable. Tool blocked.
No handler yet.
Remote tools disabled.
Ready for internal review. No handler executed.
```

Forbidden PR27.1 interpretation:

```txt
ready_for_production
ready_to_execute
ready_for_chatgpt
approved_for_remote
safe_to_run
```

## 9. Allowed demo scenarios

| Scenario | Source boundary | Allowed output | Forbidden output |
| --- | --- | --- | --- |
| Show what tools would exist | PR18, PR25 | safe descriptor name and visibility state | raw args, real user data, callable endpoint |
| Show why a tool is hidden | PR25 | `hidden` / reason summary | stack trace, policy internals with raw payload |
| Show dry-run-only state | PR25, PR26 | `Dry run only.` | generated resume or handler result |
| Show approval-required state | PR20, PR26, PR27.1 | `Approval required.` | action execution, approval bypass |
| Show denied state | PR20, PR26, PR27.1 | `Denied. Nothing ran.` | mutation, send, submit, apply |
| Show audit-missing state | PR20, PR27.1 | `Audit unavailable. Tool blocked.` | review-ready wording, execution path |
| Show privacy-blocked state | PR24, PR27, PR27.1 | `Blocked. Review privacy.` | sentinel value, raw finding payload |
| Show no-handler state | PR21, PR26, PR27.1 | `No handler yet.` | fake handler execution |
| Show remote-disabled state | PR22, PR26, PR27.1 | `Remote tools disabled.` | active remote call or tunnel |
| Show ready-for-internal-review state | PR27, PR27.1 | `Ready for internal review. No handler executed.` | production-ready or executable wording |
| Show redacted safe summary | PR24, PR26 | `Output redacted.` | raw CV, source quote, token, secret |

## 10. Forbidden scenarios

The prototype must not support:

- generate a real resume
- generate a real cover letter
- export a file
- download a file
- send an email
- submit an application
- apply to a job
- scrape LinkedIn, Upwork, Indeed, ATS, job boards, or browser pages
- connect to ChatGPT from a real endpoint
- authenticate a real user
- persist user data
- run a handler
- run transport
- deploy a server
- pass raw CV, resume, cover letter, job text, or source document text into a ChatGPT App surface
- show complete generated artifacts inside ChatGPT
- treat PR27.1 gate pass as runtime permission
- treat PR27.1 gate pass as production readiness
- treat PR27.1 gate pass as ChatGPT App readiness

## 11. Future PR gates

### PR29 - Local-only App Manifest Draft

Allowed:

- docs/spec/static draft only
- candidate metadata fields
- candidate tool names derived from PR18/PR25
- explicit non-production markers
- no runtime
- no SDK package
- no server

Forbidden:

- install Apps SDK
- connect to ChatGPT
- define production endpoints
- define OAuth credentials
- define real handler URLs

Gate:

- must cite PR27.1 fail-closed behavior
- must keep all tools non-runnable
- must keep all endpoints placeholder-only

### PR30 - End-to-end Safety Audit

Allowed:

- audit PR18-PR29
- verify no execution path exists
- verify all gates fail closed
- verify doc/code consistency
- verify forbidden scenarios remain blocked

Forbidden:

- adding runtime behavior
- adding UI
- adding remote transport

Gate:

- must prove PR27.1 cannot be treated as runtime permission
- must verify no raw privacy material can enter a ChatGPT App surface

### PR31 - Non-production Prototype Scaffold

Allowed only after explicit approval.

Minimum constraints:

- no real handler
- no real user data
- no production transport
- no OAuth
- no export/send/submit/apply
- only fixture-backed surfaces
- must use PR27.1 gate result before any exposed state

## 12. Manual review checklist

Before any prototype implementation:

1. Every tool respects visibility rules from PR25.
2. Every tool passes PR24 privacy/redaction checks.
3. All approval, denial, blocked, and review copy matches PR26 fixtures.
4. No tool can be exposed externally unless PR27.1 returns `ready_for_internal_review`.
5. `ready_for_internal_review` is treated as review-only.
6. Remote transport is not enabled by the prototype.
7. UX messages follow PR23 and Twoweeks voice.
8. Mock/demo surfaces cannot download, send, submit, apply, auto-apply, export, or mutate production data.
9. Rollback instructions exist for each mock/demo surface.
10. The prototype cannot authenticate a real user.
11. The prototype cannot persist user data.
12. The prototype cannot call a real endpoint.
13. The prototype cannot show raw source text.
14. The prototype cannot claim production readiness.
15. The prototype cannot claim ChatGPT App readiness.
16. The prototype cannot claim handler readiness.
17. The prototype cannot claim remote readiness.

## 13. Rollback / kill switch

Rollback for PR28 is deletion-only:

- remove `docs/plans/2026-06-11-chatgpt-app-non-production-prototype-plan.md`

Future prototype rollback requirements:

- all mock/demo tools reset to hidden
- all fixture exposure disabled
- all sessions invalidated if any accidental enablement occurs
- all PR25 visibility checks rerun
- all PR27.1 privacy gate checks rerun
- all unsafe outputs blocked before review resumes

## 14. Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Prototype plan is mistaken for implementation approval | unsafe code may start too early | PR28 states Plan-only, Build/Deploy forbidden |
| `ready_for_internal_review` is mistaken for execution readiness | accidental exposure | PR28 repeats non-executable meaning |
| PR27.1 gate pass becomes runtime permission | handler or transport may run too early | PR28 states gate pass is review evidence only |
| Mock/demo output grows into real user-data output | privacy leak | PR24 and PR27.1 required before exposure |
| Copy drifts from Twoweeks voice | confusing UX | PR26 copy fixtures required |
| Transport gets enabled early | remote exposure | PR22 stays disabled/reference-only |
| Handler boundary becomes a real handler too early | execution path appears | PR21 remains design-only until later approval |
| Future Apps SDK docs change | stale assumptions | re-check official docs before PR29/PR31 |

## 15. Acceptance criteria for PR28

PR28 passes only if:

- changed file count is exactly 1
- no files under `my-app/` changed
- no package files changed
- no lockfiles changed
- document says Plan-only
- document clearly forbids Build and Deploy
- document references PR24, PR25, PR26, PR27, and PR27.1 as mandatory gates
- document reflects PR27.1 fail-closed gate hardening
- document states `ready_for_internal_review` is not execution readiness
- document states `ready_for_internal_review` is review evidence only
- document states no real user data
- document states no ChatGPT App submission
- document states no Apps SDK code
- document states no MCP server
- document states no transport runtime
- document states no OAuth
- document states no export/send/submit/apply

## 16. Verification

Documentation/manual inspection only. No runtime execution.

Run:

```bash
rtk git diff --check
rtk git diff --name-only application-os-foundation...HEAD
rtk npx fallow audit --changed-since application-os-foundation --format compact
```

Expected changed file list:

```txt
docs/plans/2026-06-11-chatgpt-app-non-production-prototype-plan.md
```

Do not run app tests unless repository policy requires it.

Manual checks:

- Review all mock surfaces against PR24 privacy/redaction fixtures.
- Inspect PR23 UX/privacy spec for consent, privacy, and refusal consistency.
- Confirm PR27.1 privacy gate rules are documented and required.
- Cross-check PR25 visibility policy against allowed mock/demo tools.
- Confirm PR21 remains design-only.
- Confirm PR22 remains disabled/non-production reference only.
- Confirm no code, route, server, transport, OAuth, Convex, handler, UI, deployment, export, send, submit, apply, or real user-data surface is added.

## 17. PR body draft

Summary:

- Adds a docs-only PR28 plan for a future non-production ChatGPT App prototype.
- Locks PR28 to Plan-only work. Build and Deploy remain forbidden.
- Threads PR18-PR27.1 boundaries into explicit prototype, review, data, rollback, and future PR gates.

Verification:

```txt
rtk git diff --check
rtk git diff --name-only application-os-foundation...HEAD
rtk npx fallow audit --changed-since application-os-foundation --format compact
```

Expected changed files:

```txt
docs/plans/2026-06-11-chatgpt-app-non-production-prototype-plan.md
```

## 18. References

- PR18: `docs/decisions/2026-06-11-mcp-schema-projection.md`
- PR19: `docs/decisions/2026-06-11-mcp-call-envelope-error-contract.md`
- PR20: `docs/decisions/2026-06-11-mcp-approval-audit-boundary.md`
- PR21: `docs/decisions/2026-06-11-mcp-real-handler-boundary-design.md`
- PR22: `docs/decisions/2026-06-11-mcp-remote-transport-spike.md`
- PR23: `docs/plans/2026-06-11-chatgpt-app-ux-privacy-spec.md`
- PR24: `docs/decisions/2026-06-11-mcp-privacy-redaction-fixtures.md`
- PR25: `docs/decisions/2026-06-11-mcp-tool-visibility-policy.md`
- PR26: `docs/decisions/2026-06-11-mcp-approval-ux-copy-fixtures.md`
- PR27: `docs/decisions/2026-06-11-mcp-privacy-review-gate.md`
- PR27.1: `my-app/src/modules/local-mcp/mcpPrivacyReviewGate.ts`
- PR27.1 tests: `my-app/src/modules/local-mcp/__tests__/mcpPrivacyReviewGate.test.ts`
- OpenAI Apps SDK docs, checked 2026-06-11: Plan / Build / Deploy, Security & Privacy, submission guidelines.
- Twoweeks brand voice: `twoweeks-wiki/wiki/design/brand-voice.md`

## 19. Next steps

After PR28 approval:

1. PR29 - Local-only App Manifest Draft, docs/spec/static only.
2. PR30 - End-to-end Safety Audit, pure review, no runtime.
3. PR31 - Non-production Prototype Scaffold, only after explicit approval.

Do not skip PR29 or PR30.
Do not start prototype code from PR28.
