# 

**Status:** Proposed — ready for a PR-local implementation brief  
**Date:** 2026-06-19  
**Target wiki path:** `docs/plans/2026-06-19-pr80b-safe-application-handoff-while-ats-access-pending.md`  
**Risk level:** High — real application data and user-facing action state, but no external write  
**Live ATS status:** Blocked until an approved provider supplies authorized credentials, a test tenant, and a test posting

## 0. Ordering and prerequisite guard

This document does not override the canonical rule to implement the lowest-numbered unmerged PR. PR80B becomes the next implementation PR only when the real repository and progress ledger prove that PR73 through PR80A, including the relevant approval, audit, privacy, export, write-action, egress, dry-run, idempotency, and kill-switch gates, are merged and passing.

- If PR80A is not merged and verified, PR80A remains next.
- If an earlier prerequisite PR is unmerged, complete that PR first.
- If the roadmap, ledger, repository, and GitHub state disagree, mark the PR-local brief `BLOCKED` and resolve the discrepancy before coding.
- Provider authorization is not a prerequisite for writing this plan, but it remains a prerequisite for any live ATS transport.

Because the actual repository and GitHub state were not available while this wiki document was drafted, its status is **proposed**, not proof that PR80B is currently ready to implement.

## 1. Decision

While Twoweeks waits for official ATS authorization, the next PR is:

> **PR80B — Safe manual application handoff, with no ATS transport and no browser automation.**

Twoweeks will prepare and verify the application package. The user will remain responsible for navigating the employer website, pasting/uploading the approved material, and clicking the final submit button.

This PR must not pretend that Twoweeks submitted an application. It must distinguish clearly between:

- content prepared by Twoweeks;
- an external page opened by the user;
- a submission reported by the user;
- a submission verified later through an official provider receipt.

The final state available in this PR is **`user_reported_submitted`**, never **`provider_verified_submitted`**.

## 2. Why this PR exists

PR80 live is correctly blocked because no ATS provider has yet supplied all required production prerequisites. Waiting for provider approval must not block useful product validation.

PR80B allows Twoweeks to validate the safest delivery path now:

1. prepare an exact application package;
2. show a final review;
3. obtain exact human approval;
4. give the user copy/download tools;
5. open the official destination without reading or modifying it;
6. let the user report the result truthfully;
7. preserve an auditable, privacy-safe record.

This creates immediate user value without scraping, browser control, ATS credentials, or a misleading fake integration.

## 3. End goal

At the end of PR80B, a user can complete this end-to-end flow with fixture data and, where existing product gates permit, real approved application data:

```text
approved application package
  -> final handoff preview
  -> exact human confirmation
  -> handoff manifest frozen by digest
  -> copy individual answers and/or download approved files
  -> open the official job URL manually
  -> user completes the application outside Twoweeks
  -> user records one truthful outcome
```

The supported outcomes are:

- `not_started`;
- `handoff_prepared`;
- `handoff_confirmed`;
- `destination_opened`;
- `user_reported_submitted`;
- `user_reported_not_submitted`;
- `abandoned`.

`provider_verified_submitted` is reserved for a future official ATS integration and must be unreachable in PR80B.

## 4. Product boundary

### Twoweeks owns

- package preparation;
- document and answer review;
- sensitive-field warnings;
- exact confirmation;
- immutable handoff manifest;
- copy/download controls;
- destination-domain display;
- privacy-safe audit events;
- truthful state labels;
- optional user-entered notes or receipt references marked as unverified.

### The user owns

- logging into the employer/job platform;
- navigating the application form;
- deciding what to paste or upload;
- answering any unexpected question;
- accepting provider-specific consent text;
- solving CAPTCHA or MFA personally;
- clicking the final submit button;
- reporting whether submission occurred.

### Twoweeks explicitly does not own in this PR

- reading a third-party page;
- DOM inspection;
- scraping;
- autofill;
- browser control;
- cookie/session access;
- CAPTCHA or MFA handling;
- final external submit;
- provider receipt verification;
- ATS OAuth/API credentials.

## 5. Required handoff manifest

Create one immutable, canonical handoff manifest per approved application attempt.

The manifest must include only the minimum required references and approved values:

- internal application/package ID;
- internal user/actor ID or opaque reference;
- job title and company display name;
- exact destination URL supplied by the approved job record;
- normalized destination origin for display;
- approved resume artifact reference;
- approved cover-letter/application-message artifact reference when present;
- answer cards in intended presentation order;
- answer provenance/reference without exposing unrelated source material;
- required/optional status when known;
- sensitive-field classification when known;
- consent warnings when known;
- filename, media type, byte size, and SHA-256 for each file;
- schema/version reference used to prepare the package, when available;
- canonical payload digest;
- confirmation ID and confirmation timestamp;
- creation and expiry timestamps;
- capability label: `manual_handoff_only`.

The manifest must not contain:

- ATS credentials;
- session cookies;
- browser tokens;
- raw source documents that were not approved for the application;
- hidden private facts;
- `never_use` data;
- guessed consent;
- guessed answers;
- a fabricated provider application ID.

## 6. Confirmation rules

The handoff confirmation must be bound to the exact final manifest.

The confirmation binding must include at least:

- package ID;
- destination URL/origin;
- ordered answer values;
- artifact IDs and file digests;
- sensitive-field inclusion decisions;
- consent-related values already present in the package;
- manifest digest;
- actor/user reference.

Any change after confirmation must invalidate the confirmation, including:

- changing an answer;
- replacing a file;
- changing the destination URL;
- changing the job/company target;
- changing a sensitive-field decision;
- changing an application message;
- adding or removing an attachment.

No model-generated revision may occur after confirmation without creating a new preview and confirmation.

## 7. User experience required

The PR must provide a simple handoff view or existing equivalent surface with:

1. **Target** — company, role, and clearly displayed destination domain.
2. **Approved files** — download controls and file fingerprints/metadata.
3. **Application answers** — one answer card at a time with explicit copy controls.
4. **Sensitive fields** — visually distinct warning and voluntary/required status when known.
5. **Checklist** — what the user must verify on the external form.
6. **Open destination** — a normal user-initiated link; no server fetch and no hidden navigation.
7. **Outcome** — explicit user controls for submitted, not submitted, or abandoned.
8. **Truth label** — `Reported by you; not verified by the provider` for user-reported submission.

Opening the destination must never transition the application to submitted.

Copying or downloading an item must never transition the application to submitted.

## 8. URL safety rules

PR80B does not fetch the destination URL. It only presents a user-initiated link.

Even without a server fetch, the implementation must:

- accept only `https:` destinations by default;
- reject credentials embedded in a URL;
- reject malformed URLs;
- display the normalized hostname before navigation;
- reject `javascript:`, `data:`, `file:`, custom schemes, and local/private-network targets;
- never follow or inspect redirects server-side;
- never use the destination URL as an API endpoint;
- never copy query-string secrets into audit logs.

Any exception requires a separate reviewed decision.

## 9. Truthful status and evidence model

Every outcome must carry an evidence level:

| Evidence level | Meaning | Reachable in PR80B |
|---|---|---:|
| `twoweeks_prepared` | Twoweeks generated and froze the package | Yes |
| `user_interaction_observed` | Twoweeks observed a local copy/download/open action | Yes |
| `user_reported` | The user stated what happened externally | Yes |
| `provider_receipt_verified` | Official provider/API receipt was validated | No |

A user may optionally paste an external reference or note. It must be stored as **user-provided and unverified**. It must never be promoted automatically to provider-verified evidence.

Avoid a generic `submitted=true` boolean. Use explicit status and evidence fields so downstream code cannot confuse a user report with an API-confirmed result.

## 10. Audit and privacy requirements

Audit events must be reference-based and redacted.

Required event categories:

- `manual_handoff.prepared`;
- `manual_handoff.confirmed`;
- `manual_handoff.item_copied`;
- `manual_handoff.file_downloaded`;
- `manual_handoff.destination_opened`;
- `manual_handoff.outcome_reported`;
- `manual_handoff.abandoned`;
- `manual_handoff.confirmation_invalidated`.

Audit logs must not contain:

- copied answer text;
- resume or cover-letter text;
- email addresses unless the existing audit policy explicitly permits a redacted form;
- sensitive/EEO answer values;
- URL query strings;
- document bytes;
- tokens or credentials.

Log IDs, categories, timestamps, digests, and safe metadata only.

## 11. Scope allowed

- A provider-neutral **manual handoff** domain object, without provider API abstractions.
- A manifest builder from an already approved application package.
- Final preview and exact-confirmation binding.
- Copy/download/open-destination user actions.
- User-reported outcome recording.
- Redacted audit integration.
- Feature flag, default off.
- Fake/fixture E2E tests.
- Tests proving no network transport exists.
- Minimal documentation and rollback notes.

## 12. Scope forbidden

- No ATS HTTP client.
- No OAuth flow or API key support.
- No Ashby, Teamtailor, Lever, Greenhouse, SmartRecruiters, Workable, Recruitee, Workday, or Taleo adapter.
- No generic multi-provider framework.
- No fake provider presented as live.
- No browser extension in this PR.
- No page scraping or DOM inspection.
- No autofill.
- No automated clicking.
- No browser session/cookie handling.
- No CAPTCHA or MFA interaction.
- No LinkedIn or other platform-specific automation.
- No Gmail/Outlook send implementation changes; use the existing controlled-send path only where already approved.
- No bulk application workflow.
- No auto-apply.
- No background submission.
- No automatic retry of an external write.
- No broad refactor.
- No new roadmap or renumbering of unrelated PRs.

## 13. Required tests

### Manifest and confirmation

- The same approved package produces the same canonical digest.
- Reordered semantically ordered answers change the digest when order matters.
- Changing one answer invalidates confirmation.
- Replacing one attachment invalidates confirmation.
- Changing the destination invalidates confirmation.
- Expired confirmation cannot create a handoff session.
- Unapproved packages cannot create a confirmed handoff.

### Truthful outcome

- Opening a destination does not mark an application submitted.
- Copying all answers does not mark an application submitted.
- Downloading all files does not mark an application submitted.
- `user_reported_submitted` is labeled unverified.
- `provider_verified_submitted` cannot be created by any PR80B path.
- A pasted external reference remains unverified.

### Network and browser boundary

- Tests cannot open sockets.
- Tests cannot resolve DNS.
- No ATS/provider hostname exists in runtime transport configuration.
- No browser automation package is imported.
- No DOM selector, content-script, autofill, or click automation is introduced.
- No server-side fetch is performed for the destination URL.

### URL safety

- Non-HTTPS schemes are rejected.
- URLs with embedded credentials are rejected.
- Private/local targets are rejected.
- Malformed destinations fail closed.
- Query strings are omitted from audit metadata.

### Privacy and audit

- Answer text is absent from audit records.
- Attachment bytes and document text are absent from audit records.
- Sensitive values are absent from logs and errors.
- `never_use` data cannot enter the handoff manifest.
- Copy/download events use safe references only.

### Feature control

- The feature flag is false by default.
- Disabled mode fails closed.
- Kill-switch behavior remains compatible with PR80A if the shared foundation applies to this user action.

## 14. Acceptance criteria

PR80B is complete only when all of the following are true:

- A confirmed application package can produce one immutable manual handoff session.
- The user can download approved artifacts and copy approved answers.
- The user can open the destination through an ordinary user-initiated link.
- No external page is read, modified, or submitted by Twoweeks.
- The user can report an outcome with an explicit unverified evidence label.
- No code path can create a provider-verified submission.
- Confirmation is invalidated by any material package change.
- Audit events are useful but contain no application content.
- Feature flags are disabled by default.
- All tests run without network access.
- The diff does not add a provider adapter or multi-provider framework.
- The PR summary states clearly: **this is manual handoff, not live submit/apply**.

## 15. Five-mode validation plan

The safe strategy is validated as five separate modes. They must not be collapsed into one broad PR.

| Mode | Validation goal | Current action |
|---|---|---|
| 1. Manual apply assist | User can complete an application from an approved package without Twoweeks touching the external form | **Implement in PR80B** |
| 2. Controlled recruiter email | One approved recipient, message, confirmation, send result, and audit event through an authorized mail channel | Reuse and E2E-test the existing PR78 path; do not modify it opportunistically in PR80B |
| 3. Export/download | Approved resume and application package are downloadable and fingerprinted | Reuse PR73–PR75 outputs inside the handoff; fix only blocking integration defects with explicit scope |
| 4. Browser companion | Side panel/checklist may assist the user, but cannot read, fill, click, or submit third-party pages without a separate policy decision | Deferred until PR80B user testing proves the need; requires its own reviewed PR |
| 5. Official ATS submit | Schema fetch, exact preview, authorized submit, durable idempotency, and provider receipt | Remains blocked until one provider supplies written authorization, credentials, test tenant, and test posting |

## 16. ATS authorization gate running in parallel

The founder may continue provider outreach while PR80B is implemented. A provider is not approved based only on a sales demo.

Before a provider-specific live PR can start, record all of the following:

- provider and product name;
- written confirmation that the Twoweeks candidate-assistant use case is allowed;
- official schema/questions endpoint;
- official submit/apply endpoint;
- server-to-server authentication method;
- test or sandbox tenant;
- one authorized test posting;
- credentials stored server-side only;
- attachment/upload contract;
- success receipt contract;
- error and rate-limit semantics;
- duplicate/retry behavior;
- candidate email/notification behavior;
- sensitive-data and consent requirements;
- provider terms/partner requirements;
- named provider contact;
- kill-switch and revocation procedure.

If provider idempotency is not officially documented, Twoweeks must use durable local idempotency and treat ambiguous post-send timeouts as unknown. No undocumented provider field may be invented as an idempotency key.

## 17. Follow-on decision after PR80B

After PR80B is merged and tested with users:

### If no ATS provider has approved access

Continue with manual handoff, controlled email, and export as the supported production delivery modes. Do not create a live ATS transport.

### If exactly one provider has approved access

Create a new provider-specific PR-local brief for a **fake transport contract adapter first**. It must remain provider-specific, contain no live credentials, and have no network calls in tests.

Only after the fake contract adapter is accepted and a real test posting exists may the live transport PR be proposed.

### If several providers approve access

Choose exactly one using the documented scoring criteria. Do not start a multi-provider framework. The first live implementation remains one provider, one action, one posting, and one application.

## 18. Rollback plan

PR80B must be removable by:

- disabling its feature flag;
- hiding the handoff entry point;
- preserving existing approved artifacts and audit history;
- leaving PR78 email send and PR73–PR75 exports unchanged;
- deleting only handoff-session records according to the existing retention policy;
- requiring no schema migration that makes rollback unsafe, unless separately reviewed.

## 19. Required PR-local implementation brief

Before coding, the implementing agent must inspect the real repository and create a PR-local brief containing:

- current PR number and title;
- base branch and branch name;
- controlling roadmap sections;
- merged decisions and relevant guards;
- files to read;
- files proposed to touch;
- files forbidden to touch;
- exact data model changes;
- exact UI/tool surface changes;
- tests and grep/source guards;
- migration and rollback plan;
- `READY_TO_IMPLEMENT` or `BLOCKED`.

Because this PR touches real application data and user-visible action state, the agent must stop after the brief for maintainer approval before coding.

## 20. Codex prompt for the PR-local brief

```text
You are preparing PR80B for Twoweeks.

PR title:
PR80B — Safe Application Handoff While ATS Authorization Is Pending

Do not code yet.

Read, in this order:
1. AGENTS.md;
2. the canonical implementation roadmap;
3. the progress ledger/current merged PR state;
4. PR73–PR80 controlling docs and tests;
5. the PR80B plan:
   docs/plans/2026-06-19-pr80b-safe-application-handoff-while-ats-access-pending.md;
6. the actual repository files that implement approved artifacts, confirmation,
   audit, retention, feature flags, and PR80A durable action state.

Produce a PR-local implementation brief with:
- current base branch and proposed branch name;
- evidence of which prerequisite PRs are actually merged;
- exact files to read;
- exact files proposed to touch;
- files forbidden to touch;
- current domain types that can be reused;
- minimal data model changes;
- exact user flow;
- exact state/evidence model;
- exact feature flag behavior;
- exact tests;
- no-network and no-browser-automation source guards;
- migration/rollback plan;
- risks and unresolved conflicts;
- READY_TO_IMPLEMENT or BLOCKED.

Hard constraints:
- manual handoff only;
- no ATS HTTP client;
- no OAuth or API keys;
- no provider adapter;
- no fake provider presented as live;
- no browser extension;
- no scraping or DOM access;
- no autofill or automated click;
- no CAPTCHA/MFA handling;
- no email-send refactor;
- no bulk or auto-apply;
- no broad refactor;
- no multi-provider framework;
- no provider-verified submission state reachable in this PR;
- tests must not access the network.

The end state must be truthful:
Twoweeks prepares an immutable, confirmed handoff package; the user manually
uses it on the external site; any reported submission remains explicitly
user-reported and unverified by the provider.

This is a high-risk PR-local brief. Stop after the brief and wait for
maintainer approval. Do not implement code in the same run.
```

## 21. Canonical roadmap insertion

Add the following immediately after PR80A and before PR80 live in the canonical roadmap:

```markdown
### PR80B — Safe Application Handoff While ATS Authorization Is Pending

**Type:** code/tests, no external write.

**Purpose:** let users complete applications manually from an immutable,
confirmed Twoweeks package while official ATS access is unavailable.

**Required:**
- final handoff preview;
- exact human confirmation bound to the package digest;
- copy/download/open-destination controls;
- redacted audit events;
- user-reported outcome clearly labeled unverified;
- no provider-verified success state;
- feature flag default-off;
- tests with no network.

**Forbidden:**
- ATS transport or credentials;
- provider adapter;
- scraping, DOM access, autofill, browser automation, or submit;
- fake provider presented as live;
- bulk or auto-apply;
- broad refactor or multi-provider framework.

**Output:** Twoweeks can safely hand an approved application package to the
user without claiming to have submitted it.

PR80 live remains blocked until one provider supplies written authorization,
server-to-server credentials, a test tenant, and an authorized test posting.
```
