

Date: 2026-06-11
Status: planned spec
Scope: docs-only local-only static manifest draft for a future non-production ChatGPT App.

## 1. Objective

Define a local-only, non-runnable manifest shape for a future Twoweeks ChatGPT App.

PR29 does not create an app manifest file consumed by runtime.
PR29 does not install an SDK.
PR29 does not connect to ChatGPT.
PR29 does not start prototype work.

The draft exists to make the future app boundary boring before anything can run.

## 2. Verdict

Certain:

- PR29 is docs-only.
- PR29 is Plan-only.
- PR29 produces one static planning document.
- PR29 does not add code.
- PR29 does not add a real manifest artifact.
- PR29 does not add a server, route, transport, OAuth, UI, handler, Convex function, package, or lockfile.
- PR29 keeps all candidate tools non-runnable and hidden by default.
- PR29 inherits PR28's rule: PR27.1 gate pass is review evidence only, not runtime permission.

Non-goal:

- No ChatGPT App submission.
- No local tunnel.
- No developer-mode connection.
- No remote MCP server.
- No Apps SDK usage.

## 3. Source boundaries

PR29 can reference these existing boundaries only:

| Source | PR29 use | Hard stop |
| --- | --- | --- |
| PR18 schema projection | candidate public tool names | no `tools/list` runtime |
| PR19 call envelope | non-executable call shape reference | no `tools/call` |
| PR20 approval/audit shell | review and audit metadata requirement | no approval UI or audit persistence |
| PR21 handler boundary | design-only handler state | no real handler |
| PR22 remote transport spike | disabled preflight reference | no transport runtime |
| PR23 UX/privacy spec | consent, refusal, and privacy language | no user-facing UI |
| PR24 privacy fixtures | safe-output rule | no runtime sanitizer claim |
| PR25 visibility policy | hidden/default visibility state | no external exposure |
| PR26 copy fixtures | exact copy source | no improvised copy |
| PR27 privacy review gate | exposure review model | no executable permission |
| PR27.1 gate hardening | fail-closed and bounded output rules | no runtime permission |
| PR28 prototype plan | Plan-only / Build-forbidden / Deploy-forbidden boundary | no prototype scaffold |

## 4. Planning boundary

OpenAI Apps SDK work is organized around Plan, Build, and Deploy. PR29 stays in Plan.

### Plan - allowed in PR29

- define a static manifest draft
- define candidate app identity fields
- define candidate metadata fields
- map candidate tools to PR18 public names
- document visibility defaults
- document privacy and approval gates
- document forbidden manifest values
- document future implementation gates

### Build - forbidden in PR29

- no Apps SDK install
- no MCP SDK install
- no OpenAI SDK install
- no manifest JSON consumed by runtime
- no server
- no route
- no endpoint
- no UI component
- no widget resource
- no auth implementation
- no state management
- no handler registry
- no tests for runtime behavior

### Deploy - forbidden in PR29

- no ChatGPT connection
- no developer-mode link
- no test integration
- no app submission
- no production review
- no public endpoint
- no hosted resource
- no marketplace or app-store work

## 5. Draft artifact rule

PR29 may describe a manifest-like shape inside this document.

PR29 must not add any of these files:

```txt
app.json
manifest.json
chatgpt-app.json
apps-sdk.json
mcp.json
openai-app.json
```

PR29 must not add a machine-readable manifest that future code could accidentally load.

The only allowed output is this Markdown planning file.

## 6. Candidate app identity

Candidate values are placeholders. They are not production names.

| Field | Draft value | Rule |
| --- | --- | --- |
| app name | `Twoweeks Review` | short, direct, no hype |
| app slug | `twoweeks-review-local-draft` | local-only placeholder |
| audience | internal review only | no public users |
| status | `non_runnable_draft` | not executable |
| distribution | none | no app store |
| runtime | none | no server |
| transport | none | no remote MCP |
| authentication | none | no OAuth |
| persistence | none | no Convex |
| component | none | no UI/widget |

Bad names:

- `Twoweeks AI`
- `Twoweeks Auto Apply`
- `Twoweeks Exporter`
- `Twoweeks Production App`
- `Twoweeks ChatGPT App Ready`

## 7. Candidate tool inventory

Candidate tools come from PR18 public names. PR29 does not add, rename, or expose tools.

| Candidate tool | Local source | Default visibility | Allowed result | Forbidden result |
| --- | --- | --- | --- | --- |
| `twoweeks.application_package.summarize` | `local_mcp.application_package.summarize` | hidden | safe package summary | resume text, cover letter text, export, send, submit, apply |
| `twoweeks.evidence_graph.summarize` | `local_mcp.evidence_graph.summarize` | hidden | safe evidence summary | private facts, `never_use` facts, source quotes |
| `twoweeks.resume_variant_plan.summarize` | `local_mcp.resume_variant_plan.summarize` | hidden | safe plan summary | generated resume, raw CV, raw job text |
| `twoweeks.review_cockpit.summarize` | `local_mcp.review_cockpit.summarize` | hidden | safe review status | user/session IDs, stack traces, raw payloads |

All tools remain non-runnable.
All tools require PR25 visibility and PR27.1 gate review before any future external-style state.

## 8. Candidate metadata rules

Metadata must guide the model toward narrow review use and away from accidental activation.

For every candidate tool:

- name uses the existing `twoweeks.*.summarize` public name from PR18
- title is short and boring
- description starts with `Use this when...`
- description includes `Do not use...` boundaries
- parameters are refs only, never raw document text
- output is safe summary only
- annotations are read-only, non-destructive, closed-world, and idempotent in intent
- no copy says production-ready, executable, automated, export, send, submit, or apply

The future implementation must re-check official Apps SDK metadata docs before coding.

## 9. Candidate tool metadata table

| Tool | Draft title | Draft description | Input refs only | Output |
| --- | --- | --- | --- | --- |
| `twoweeks.application_package.summarize` | `Review package` | `Use this when reviewing package status. Do not use to create, export, send, submit, or apply.` | `applicationPackageRef` | safe summary |
| `twoweeks.evidence_graph.summarize` | `Review evidence` | `Use this when reviewing evidence coverage. Do not use to reveal source quotes or private facts.` | `evidenceGraphRef` | safe summary |
| `twoweeks.resume_variant_plan.summarize` | `Review resume plan` | `Use this when reviewing a resume plan. Do not use to generate or expose resume text.` | `resumeVariantPlanRef` | safe summary |
| `twoweeks.review_cockpit.summarize` | `Review cockpit` | `Use this when reviewing workflow status. Do not use to run handlers or expose raw payloads.` | `reviewCockpitRef` | safe summary |

Draft annotation intent for each tool:

```txt
readOnlyHint: true
destructiveHint: false
openWorldHint: false
idempotentHint: true
```

This block is documentation only. It is not TypeScript, JSON, MCP config, or Apps SDK config.

## 10. Candidate `_meta` policy

PR29 does not define real `_meta` fields.

Future `_meta` work must follow these rules:

| Field family | PR29 stance | Future gate |
| --- | --- | --- |
| `securitySchemes` | omitted | OAuth/auth review required |
| `_meta.securitySchemes` mirror | omitted | OAuth/auth review required |
| `_meta.ui.resourceUri` | omitted | UI/component review required |
| `_meta.ui.visibility` | omitted | PR25 + PR27.1 required |
| `_meta["openai/outputTemplate"]` | omitted | UI/component review required |
| `_meta["openai/widgetAccessible"]` | false by future default | PR25 + PR27.1 required |
| `_meta["openai/visibility"]` | private by future default | PR25 + PR27.1 required |
| invocation copy | PR26 only | copy review required |
| file params | forbidden | file boundary review required |

PR29 cannot use `_meta` to hide sensitive data.
No component exists.
No tool result exists.
No transcript exists.
No data moves.

## 11. Static manifest draft

This is a non-runnable planning shape.
Do not copy it into a runtime file.
Do not load it.
Do not submit it.

```txt
kind: local_only_chatgpt_app_manifest_draft
version: 1
status: non_runnable_draft
app:
  name: Twoweeks Review
  slug: twoweeks-review-local-draft
  audience: internal_review_only
  distribution: none
runtime:
  server: none
  endpoint: none
  transport: none
  oauth: none
  persistence: none
  component: none
safety:
  default_visibility: hidden
  requires_pr24_privacy_check: true
  requires_pr25_visibility_policy: true
  requires_pr26_copy: true
  requires_pr27_1_gate: true
  gate_pass_means: review_evidence_only
tools:
  - name: twoweeks.application_package.summarize
    source: local_mcp.application_package.summarize
    visibility: hidden
    output: safe_summary_only
    runnable: false
  - name: twoweeks.evidence_graph.summarize
    source: local_mcp.evidence_graph.summarize
    visibility: hidden
    output: safe_summary_only
    runnable: false
  - name: twoweeks.resume_variant_plan.summarize
    source: local_mcp.resume_variant_plan.summarize
    visibility: hidden
    output: safe_summary_only
    runnable: false
  - name: twoweeks.review_cockpit.summarize
    source: local_mcp.review_cockpit.summarize
    visibility: hidden
    output: safe_summary_only
    runnable: false
```

## 12. Data policy

Allowed in PR29:

- tool names from PR18
- local tool IDs from PR18/PR19
- placeholder app identity
- fixture-style refs
- safe summary wording
- PR26 copy strings
- PR27.1 safe summaries
- non-runnable draft blocks

Forbidden in PR29:

- raw CV or resume text
- raw cover letter text
- raw job description text
- complete generated resume
- complete generated cover letter
- source documents
- source quote dumps
- private facts
- `never_use` facts
- raw arguments
- user IDs
- session IDs
- secrets
- tokens
- origin or host payloads
- OAuth scopes for real resources
- endpoint URLs
- production domains

## 13. Golden prompt set draft

PR29 defines a future metadata test set. It does not run it.

| Prompt class | Example prompt | Expected future outcome |
| --- | --- | --- |
| direct | `Review my Twoweeks package.` | no run; show review-only state after gates |
| direct | `Summarize evidence coverage.` | no run; safe summary only after gates |
| indirect | `Is this application ready?` | no run; review status only after gates |
| negative | `Export this resume.` | do nothing; forbidden |
| negative | `Send the application.` | do nothing; forbidden |
| negative | `Apply to this job.` | do nothing; forbidden |
| negative | `Show my raw resume.` | do nothing; forbidden |
| negative | `Use the private facts anyway.` | do nothing; forbidden |

Future metadata evaluation must optimize for negative-prompt precision before recall.

## 14. Consent and review language

Candidate consent copy comes from PR23/PR26 only.

Allowed copy:

```txt
Tool disabled.
Dry run only.
Approval required.
Blocked. Review privacy.
Ready for internal review. No handler executed.
```

Forbidden copy:

```txt
Ready to run.
Ready for ChatGPT.
Production ready.
Automatically approved.
Export ready.
Send now.
Apply now.
```

No app or tool may be visible to a real user in PR29.

## 15. PR27.1 gate rule

PR27.1 remains mandatory.

`ready_for_internal_review` means:

- review evidence exists
- safe summaries are bounded
- no handler executed
- no transport ran
- no app is ready

`ready_for_internal_review` does not mean:

- execution readiness
- production readiness
- ChatGPT App readiness
- remote approval
- handler approval
- OAuth approval
- user-data approval

## 16. Forbidden scenarios

PR29 must not support:

- building a ChatGPT App
- submitting a ChatGPT App
- connecting from ChatGPT
- linking developer mode
- running an MCP server
- running `tools/list`
- running `tools/call`
- creating an endpoint
- creating a tunnel
- installing Apps SDK
- installing MCP SDK
- installing OpenAI SDK
- creating UI resources
- adding component templates
- adding OAuth
- adding Convex persistence
- adding handlers
- adding export/download/send/submit/apply
- adding browser scraping
- adding file upload handling

## 17. Future PR gates

### PR30 - End-to-end Safety Audit

Allowed:

- audit PR18-PR29
- verify no runtime path exists
- verify PR29 static draft cannot be loaded
- verify metadata is narrow and negative-prompt safe
- verify PR27.1 remains review-only

Forbidden:

- runtime behavior
- UI
- Apps SDK
- transport
- OAuth
- handler

### PR31 - Non-production Prototype Scaffold

Allowed only after PR30 approval.

Minimum constraints:

- no real handler
- no real user data
- no production transport
- no OAuth
- no export/send/submit/apply
- no public endpoint
- only fixture-backed surfaces
- PR27.1 gate result before any visible state

## 18. Manual review checklist

Before any future implementation:

1. Manifest draft is still Markdown-only.
2. No runtime manifest file exists.
3. All candidate tools map to PR18 names.
4. Every tool remains hidden by default.
5. Every candidate output is safe summary only.
6. PR24 privacy checks are mandatory.
7. PR25 visibility is mandatory.
8. PR26 copy is mandatory.
9. PR27.1 gate is mandatory.
10. `ready_for_internal_review` remains review-only.
11. No UI/resource URI exists.
12. No OAuth/security scheme is real.
13. No endpoint or domain is real.
14. No raw data can appear in metadata, content, structured content, or future `_meta`.
15. No export, download, send, submit, apply, or auto-apply appears.

## 19. Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Static draft is mistaken for a real manifest | accidental implementation starts | PR29 says Markdown-only and non-runnable |
| Metadata copy over-promises capability | wrong tool selection | use narrow `Use this when...` and `Do not use...` text |
| Tools become visible too early | privacy exposure | PR25 + PR27.1 required |
| `_meta` is treated as a privacy boundary | sensitive data may leak | no component, no tool result, no reliance on `_meta` |
| PR27.1 pass becomes runtime permission | handler or transport may run too early | repeat review-only rule |
| Future implementation uses stale Apps SDK docs | incorrect manifest fields | re-check official docs before code |

## 20. Acceptance criteria for PR29

PR29 passes only if:

- changed file count is exactly 1
- changed file is `docs/plans/2026-06-11-chatgpt-app-local-only-manifest-draft.md`
- no files under `my-app/` changed
- no package files changed
- no lockfiles changed
- no manifest JSON/config file added
- no code added
- no tests added
- no Apps SDK installed
- no MCP SDK installed
- no OpenAI SDK installed
- no server/route/endpoint added
- no UI/component/resource added
- no OAuth/auth added
- no Convex added
- no handler added
- no export/download/send/submit/apply added
- document states PR29 is Plan-only
- document states the draft is non-runnable
- document references PR27.1 as mandatory and review-only

## 21. Verification

Documentation/manual inspection only. No runtime execution.

Run:

```bash
rtk git diff --check
rtk git diff --name-only application-os-foundation...HEAD
rtk npx fallow audit --changed-since application-os-foundation --format compact
```

Expected changed file list:

```txt
docs/plans/2026-06-11-chatgpt-app-local-only-manifest-draft.md
```

Do not run app tests unless repository policy requires it.
Docs-only PR.

## 22. Rollback

Rollback is deletion-only:

```txt
docs/plans/2026-06-11-chatgpt-app-local-only-manifest-draft.md
```

Then run:

```bash
rtk git diff --check
rtk git status --short --branch
```

## 23. PR body draft

Summary:

- Adds PR29 as a docs-only local-only ChatGPT App manifest draft.
- Keeps the draft non-runnable and Markdown-only.
- Maps candidate tools to PR18 names while requiring PR24, PR25, PR26, and PR27.1 before any future visible state.
- Forbids Apps SDK, MCP server, transport, OAuth, UI, handlers, endpoints, packages, and export/send/submit/apply.

Verification:

```txt
rtk git diff --check
rtk git diff --name-only application-os-foundation...HEAD
rtk npx fallow audit --changed-since application-os-foundation --format compact
```

Expected changed files:

```txt
docs/plans/2026-06-11-chatgpt-app-local-only-manifest-draft.md
```

## 24. References

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
- OpenAI Apps SDK docs, checked 2026-06-11: Apps SDK overview, Optimize Metadata, Reference.
- Twoweeks brand voice: `twoweeks-wiki/wiki/design/brand-voice.md`

## 25. Next steps

After PR29 approval:

1. PR30 - End-to-end Safety Audit, pure review, no runtime.
2. PR31 - Non-production Prototype Scaffold, only after PR30 approval.

Do not start PR31 from PR29.
Do not skip PR30.
