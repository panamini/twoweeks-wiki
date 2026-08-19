---
title: "Neyssan post-merge Jobs smoke checkpoint"
category: source
tags: [neyssan, jobs, tailoring, proposal, private-beta, smoke]
created: 2026-08-05
updated: 2026-08-05
status: current
valid_from: 2026-08-05
type: checkpoint
---

# Neyssan post-merge Jobs smoke checkpoint

## Verified baseline

- `origin/main`: `3ef0bbdb1552eb064051df887379f637071ba037`.
- PRs #378, #379, #380, #381 and #382 are merged on the active main line.
- This checkpoint was run against an exact-main disposable checkout. No source, wiki, deployment, provider, model or MCP data was changed.

## Local authenticated smoke

With a synthetic local development account, the rendered desktop and 640px mobile flow passed:

`Job -> Job Brief -> attached CV -> tailoring review -> materialize reviewed CV -> Proposal`

The review opened with pending recommendations selected by default, required-demand coverage was enforced, materialization produced the reviewed variant, and Proposal received the selected Job/CV context. The complete-resume pass-through also reached Proposal without generating a variant. The unavailable-job state was recoverable. Both viewports had zero horizontal overflow; the browser recorded zero runtime errors and zero failed network loads.

## Limitations and beta decision

This is local acceptance evidence, not deployed-identity proof. The account was a synthetic development account (`fddf`), parser upload was not exercised because the owned parser runtime was unavailable, two-account sign-out/isolation was not proven in this smoke, and the synthetic local Job/CV remains in local development data.

**Decision:** the core Jobs-to-Proposal path is a private-beta candidate, not public-launch ready.

Before inviting a controlled cohort, prove deployed frontend identity, two-account isolation and sign-out, and account-deletion/cache/late-write safety. For the MCP/App SDK path, prove empty-account onboarding, authorize a 3–5 person cohort, and document rate limits, redacted audit, revocation/rollback, reauthentication, privacy, support and listing assets. Jobs pagination, local search/filter limits, and exact aggregate counts remain deferred scalability work, not a reason to reopen the merged tailoring slice.

## Related

- [[product/product-roadmap]]
- [[product/job-library]]
- [[product/chatgpt-app-sdk-roadmap]]
