

Date: 2026-06-11
Status: planned audit
Scope: docs-only end-to-end safety audit before any non-production ChatGPT App scaffold.

## 1. Objective

Audit the PR18-PR29 ChatGPT App / Local MCP preparation chain before any PR31 scaffold work.

PR30 is review-only.

It does not add code.
It does not add runtime.
It does not add tests.
It does not add a manifest.
It does not install an SDK.
It does not connect to ChatGPT.
It does not expose tools.

The audit answers one question:

```txt
Can PR31 start a non-production fixture-backed scaffold without crossing the safety boundaries already defined?
```

## 2. Verdict

PR30 clears only this narrow next step:

```txt
PR31 may be planned as a non-production scaffold after explicit approval.
```

That does not mean:

```txt
production ready
ChatGPT App ready
runtime ready
remote approved
handler approved
OAuth ready
safe to expose real data
safe to export/send/submit/apply
```

PR31 remains blocked from:

- real handlers
- real user data
- production transport
- OAuth
- ChatGPT App submission
- export/download/send/submit/apply
- raw CV/resume/job/source text
- complete generated artifacts
- persistent audit
- public endpoints
- marketplace/distribution work

## 3. Audit boundary

PR30 is a docs-only audit.

Allowed:

- inspect PR18-PR29 decisions and plans
- summarize safety guarantees
- identify blocked surfaces
- define PR31 entry criteria
- define rollback expectations
- define verification commands

Forbidden:

- no `my-app/**` changes
- no package or lockfile changes
- no Apps SDK
- no MCP SDK
- no MCP server
- no route
- no transport
- no OAuth
- no Convex
- no handler
- no UI
- no component resource
- no manifest JSON
- no export/download/send/submit/apply
- no real user data

## 4. Evidence reviewed

| Source | Evidence used | Audit result |
| --- | --- | --- |
| PR18 schema projection | descriptors only; no `tools/list`, `tools/call`, JSON-RPC, route, server, transport, ChatGPT, OAuth, Convex, UI, export/send/submit/apply, or real handler | pass |
| PR19 call envelope | local envelope only; no OAuth, ChatGPT App, real handler, Convex, UI, export/send/submit/apply, or data mutation | pass |
| PR20 approval/audit boundary | approval/audit contracts only; no Convex, server/transport, OAuth, ChatGPT App, Remote MCP, real handler, export/send/submit/apply | pass |
| PR21 handler boundary | design-only handler boundary; real handlers, executable registry, product execution, transport, ChatGPT App, OAuth, export/send/submit/apply remain out of scope | pass |
| PR22 remote transport spike | disabled/non-production preflight only; no route, active transport, OAuth, ChatGPT App, deploy, Convex, UI, real handler, network call, persistent audit | pass |
| PR23 UX/privacy spec | hidden default, blocked tools never exposed, send/submit/apply/export never listed, approval required before real handler/data leaves/side effects | pass |
| PR24 privacy/redaction fixtures | raw source, raw resume/CV, private facts, `never_use`, secrets, sessions, stack traces, sourceQuote dumps, and complete generated text blocked from safe outputs | pass |
| PR25 visibility policy | hidden default; ready-for-review is not executable, production-ready, ChatGPT App-ready, or approved for real handler | pass |
| PR26 approval UX copy | short, safe copy; `listed_ready_for_review` maps to non-executable `review_first`; copy avoids executable readiness language | pass |
| PR27 / PR27.1 privacy review gate | fail-closed status model; `ready_for_internal_review` is review-only, not runtime permission | pass |
| PR28 prototype plan | Plan-only; Build/Deploy forbidden; PR27.1 required for future exposure review | pass |
| PR29 manifest draft | local-only, non-runnable manifest draft; no runtime manifest, SDK, server, transport, OAuth, handler, UI, component, package, or lockfile | pass |

## 5. End-to-end chain audit

### Descriptor layer

Finding:

- PR18 creates projected descriptors only.
- The descriptors are not a runtime protocol.
- PR29 candidate tool names are derived from PR18 but remain planning references only.

Verdict:

```txt
pass
```

Reason:

```txt
No descriptor currently creates a callable ChatGPT App tool.
```

### Call envelope layer

Finding:

- PR19 defines a local call envelope and safe error contract.
- It is MCP-like, not a protocol runtime.
- It does not launch tools.

Verdict:

```txt
pass
```

Reason:

```txt
No envelope path crosses into JSON-RPC, route handling, transport, or execution.
```

### Approval and audit layer

Finding:

- PR20 defines approval and audit shells.
- PR23 requires approval before real handlers, data leaving Twoweeks, sensitive summaries, or side effects.
- PR26 fixes approval/refusal copy.

Verdict:

```txt
pass
```

Reason:

```txt
Approval and audit are modeled as gates, not as runtime permissions.
```

### Handler layer

Finding:

- PR21 is design-only.
- It explicitly blocks real handlers, executable registries, product execution, Convex writes, transport, ChatGPT App, OAuth, and export/send/submit/apply.

Verdict:

```txt
pass
```

Reason:

```txt
No real handler boundary exists for PR31 to reuse as execution.
```

### Transport layer

Finding:

- PR22 is disabled by default.
- Non-production preflight is not a listener.
- Auth remains future-required.
- Origin/host policy is exact allowlist only.
- Preflight performs no tool call, network, product read, or persistence.

Verdict:

```txt
pass
```

Reason:

```txt
No active remote transport exists.
```

### Visibility layer

Finding:

- PR25 defaults to `hidden`.
- Privacy block overrides listing states.
- `listed_ready_for_review` is not executable, production-ready, ChatGPT App-ready, or approved for a real handler.
- PR29 keeps future tools hidden and non-runnable.

Verdict:

```txt
pass
```

Reason:

```txt
Tool visibility is conservative and does not imply callability.
```

### Privacy/redaction layer

Finding:

- PR24 blocks raw source documents, raw resume/CV text, raw arguments, private facts, `never_use` facts, secrets, sessions, stack traces, sourceQuote dumps, and complete generated text from safe outputs.
- PR28 and PR29 preserve safe-summary-only defaults.

Verdict:

```txt
pass
```

Reason:

```txt
The current planning chain allows only bounded safe summaries, placeholders, statuses, and reason categories.
```

### UX/copy layer

Finding:

- PR23 requires short refusal and approval copy.
- PR26 provides exact fixture copy and maps `listed_ready_for_review` to non-executable copy.
- PR28 and PR29 forbid production-ready or executable wording.

Verdict:

```txt
pass
```

Reason:

```txt
Review states are worded as review states, not permission states.
```

### Gate layer

Finding:

- PR27/PR27.1 fail closed.
- Missing visibility, missing privacy review, unsafe privacy check, denied approval, missing audit, missing/invalid handler boundary, blocked transport, or invalid copy blocks.
- Review-required states stay review-only.
- `ready_for_internal_review` is review evidence only.

Verdict:

```txt
pass
```

Reason:

```txt
The gate cannot be treated as runtime permission by policy.
```

### Manifest layer

Finding:

- PR29 defines a local-only static manifest draft.
- It forbids real manifest artifacts, Apps SDK installation, server, route, transport, OAuth, handler, UI, component, package, lockfile, and ChatGPT connection.

Verdict:

```txt
pass
```

Reason:

```txt
No machine-consumed manifest exists.
```

## 6. Forbidden surfaces audit

PR30 confirms these remain forbidden before PR31 explicit approval:

| Surface | Status |
| --- | --- |
| ChatGPT App submission | blocked |
| Apps SDK install | blocked |
| MCP SDK install | blocked |
| MCP server | blocked |
| route handler | blocked |
| public endpoint | blocked |
| remote transport | blocked |
| OAuth | blocked |
| Convex persistence | blocked |
| real handler | blocked |
| handler registry | blocked |
| UI route/page/component | blocked |
| iframe/component resource | blocked |
| runtime manifest JSON | blocked |
| real user data | blocked |
| raw CV/resume text | blocked |
| raw job/source document text | blocked |
| complete generated resume/cover letter | blocked |
| export/download/send/submit/apply | blocked |
| scraping LinkedIn/Upwork/Indeed/ATS/job boards/browser pages | blocked |

## 7. PR31 entry criteria

PR31 may start only after PR30 is reviewed and merged.

Minimum PR31 constraints:

- explicit approval before work starts
- non-production scaffold only
- fixture-backed surfaces only
- hidden by default
- no real handler
- no real user data
- no production transport
- no OAuth
- no export/download/send/submit/apply
- no ChatGPT App submission
- no raw CV/resume/job/source text
- no complete generated artifacts
- PR27.1 gate result required before any exposed state
- rollback documented in the same PR
- kill switch documented in the same PR

PR31 must not skip any of these gates.

## 8. PR31 allowed starting shape

Allowed only after explicit approval:

```txt
fixture-backed scaffold
local-only
non-production
review-only
hidden by default
no real user data
no real handler
no network transport
no OAuth
no outbound actions
```

PR31 must use wording like:

```txt
Review first.
Nothing runs.
No handler yet.
Remote tools disabled.
Safe summary only.
```

PR31 must not use wording like:

```txt
ready for production
ready to execute
ready for ChatGPT
approved for remote
safe to run
```

## 9. Findings

### P0

None found in the PR18-PR29 documentation chain.

No reviewed document authorizes:

- production ChatGPT App exposure
- real handlers
- real remote transport
- OAuth
- export/download/send/submit/apply
- raw private output to ChatGPT

### P1

Risk:

- PR31 could accidentally turn fixture-backed scaffold work into runtime work.

Required mitigation:

- PR31 must name every file changed.
- PR31 must explain why each changed file is non-production.
- PR31 must include rollback and kill switch notes.
- PR31 must verify no real handler, transport, OAuth, export/send/submit/apply, or raw data path exists.

### P2

Risk:

- Copy can drift from PR26.
- Manifest wording can imply runnable tools.
- Future Apps SDK docs can change.

Required mitigation:

- PR31 must use PR26 copy for user-facing states.
- PR31 must keep all executable readiness wording banned.
- Future Apps SDK docs must be rechecked before any real SDK work.

### P3

Risk:

- Table formatting and copy polish.

Required mitigation:

- Fix opportunistically.
- Do not block safety work.

## 10. Audit conclusion

PR30 finds the PR18-PR29 safety chain internally consistent for one narrow next step:

```txt
PR31 non-production scaffold may be proposed after explicit approval.
```

PR30 does not clear:

```txt
production
ChatGPT App submission
Apps SDK runtime
Remote MCP runtime
OAuth
real handlers
real user data
export/download/send/submit/apply
```

Safety status:

```txt
review-only pass
runtime blocked
production blocked
```

## 11. Acceptance criteria for PR30

PR30 passes only if:

- changed file count is exactly 1
- changed file is `docs/audits/2026-06-11-chatgpt-app-end-to-end-safety-audit.md`
- no files under `my-app/` changed
- no package files changed
- no lockfiles changed
- no manifest JSON file added
- no SDK dependency added
- no server, route, transport, OAuth, UI, handler, Convex, component, or resource is added
- audit states PR31 is blocked until PR30 approval/merge
- audit states PR31 remains non-production only
- audit states PR27.1 is review evidence only
- audit states all forbidden runtime/action surfaces remain blocked

## 12. Verification

Documentation/manual inspection only. No runtime execution required by PR30.

Run:

```bash
rtk git diff --check
rtk git diff --name-only application-os-foundation...HEAD
rtk npx fallow audit --changed-since application-os-foundation --format compact
```

Expected changed file list:

```txt
docs/audits/2026-06-11-chatgpt-app-end-to-end-safety-audit.md
```

Do not run app tests unless repository policy requires it.

Manual checks:

- Confirm no `my-app/**` files changed.
- Confirm no `package.json`, package lockfile, or config changed.
- Confirm no real manifest artifact was added.
- Confirm no Apps SDK, MCP SDK, server, route, OAuth, transport, handler, UI, component, or resource was added.
- Confirm PR27.1 remains review-only.
- Confirm PR31 remains blocked until explicit approval.
- Confirm no export, download, send, submit, apply, or auto-apply surface exists.

## 13. Rollback

Rollback for PR30 is deletion-only:

```txt
docs/audits/2026-06-11-chatgpt-app-end-to-end-safety-audit.md
```

Then run:

```bash
rtk git diff --check
rtk git diff --name-only application-os-foundation...HEAD
```

## 14. PR body draft

Summary:

- Adds a docs-only PR30 end-to-end safety audit across PR18-PR29.
- Confirms the planning chain remains non-runnable and fail-closed.
- Keeps PR31 blocked until explicit approval and limits it to a non-production fixture-backed scaffold.
- Reconfirms no runtime, SDK, server, transport, OAuth, handler, UI, manifest, package, lockfile, or outbound action is added.

Verification:

```txt
rtk git diff --check
rtk git diff --name-only application-os-foundation...HEAD
rtk npx fallow audit --changed-since application-os-foundation --format compact
```

Expected changed files:

```txt
docs/audits/2026-06-11-chatgpt-app-end-to-end-safety-audit.md
```

## 15. References

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
- PR28: `docs/plans/2026-06-11-chatgpt-app-non-production-prototype-plan.md`
- PR29: `docs/plans/2026-06-11-chatgpt-app-local-only-manifest-draft.md`
- Repo instructions: `AGENTS.md`
- Twoweeks brand voice: `twoweeks-wiki/wiki/design/brand-voice.md`

## 16. Next steps

After PR30 approval and merge:

1. Ask for explicit approval before PR31.
2. Start PR31 only as a non-production fixture-backed scaffold.
3. Keep PR31 hidden by default and blocked from real data, real handlers, transport, OAuth, export/download/send/submit/apply, and ChatGPT App submission.

Do not start PR31 from PR30.
