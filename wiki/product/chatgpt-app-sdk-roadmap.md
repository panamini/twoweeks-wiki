---
title: "ChatGPT/App SDK Roadmap"
category: product
tags: [chatgpt-app, apps-sdk, mcp, roadmap, safety]
created: 2026-06-23
updated: 2026-06-23
status: current
valid_from: 2026-06-12
type: roadmap
sources: [2026-06-23-twoweeks-mcp-chatgpt-app-sdk-roadmap-checkpoint, 2026-06-12-chatgpt-app-sdk-roadmap-pr41-pr89, 2026-06-12-non-production-apps-sdk-exploration-plan, 2026-06-19-pr80b-safe-application-handoff-while-ats-access-pending]
related: [[product/manual-application-handoff]], [[product/product-roadmap]], [[product/product-vision]], [[product/ai-product-model]]
---

# ChatGPT/App SDK Roadmap

The ChatGPT/App SDK roadmap is now a current checkpoint page, not just a future plan. The active truth is PR87 production-gate reconciliation after PR245, with PR88-PR89 still blocked.

## Current state

The roadmap has moved through the early MCP/App SDK phases and now sits around PR87 / production deployment gate reconciliation plus release stabilization.

PR80B manual handoff is already implemented as the safe delivery path while ATS authorization is pending, but live submit/apply remains blocked.

The PR245 reference is a shared branch/readiness checkpoint only. It does not move cover-letter prompt work into this roadmap, and it does not make MCP/App SDK launch work part of PR246.

## Workstream boundary

This page owns Twoweeks MCP, ChatGPT App SDK, Apps SDK readiness, production gates, manual handoff routing, launch blockers, and release sequencing.

It does not own cover-letter prompt V2, Mistral factuality tightening, premium provenance/finalization, Qwen premium behavior, or quality repair. Those belong to [[tasks/2026-06-22-cover-letter-quality-production-roadmap]].

## Details

| Range | Current truth | Boundary |
| --- | --- | --- |
| PR41-PR52 | Merged foundation for non-production ChatGPT/MCP demo | local demo / fixtures |
| PR53-PR64 | Merged auth, consent, privacy, and read-only real integration | no write actions |
| PR65-PR67 | Merged component / UI experience | read-only review UX |
| PR68-PR75 | Merged artifact generation, approval, revision, and export | human approval required |
| PR76-PR80 | Merged write-action foundations and manual handoff path | live submit/apply still blocked |
| PR80B | Implemented safe manual handoff while ATS authorization is pending | provider-verified submission unreachable |
| PR81-PR85 | Merged production-readiness hardening | launch still blocked |
| PR86-PR87 | Merged governance / production gate checkpoints | BLOCKED_PRODUCTION_GATE |
| PR87.8 | Production gate reconciliation after PR245 | next narrow checkpoint |
| PR88-PR89 | Private beta / public launch | blocked |

Forbidden surfaces stay blocked unless a later reviewed decision opens them: runtime endpoints, `tools/list`, `tools/call`, OAuth, real handlers, real user data, outbound HTTP, LLM/model calls, export/download/send/submit/apply, production behavior, approved answer copy, and PR80-live.

## Remaining checklist

### PR87.8 - Production gate reconciliation

- [ ] Reconcile the production gate after PR245 without changing cover-letter PR246 work.
- [ ] Confirm the current blocked surfaces are still blocked: runtime endpoints, tool listing/calls, OAuth, real handlers, outbound HTTP, LLM/model calls, export/download/send/submit/apply, approved answer copy, and PR80-live.
- [ ] Confirm PR80B manual handoff remains implemented and is still the only application-delivery path while ATS authorization is pending.
- [ ] Document which PR87 blockers are still real after the merged governance/status gates.
- [ ] Decide whether the next MCP/App SDK PR is another reconciliation slice or a launch-readiness slice.

### PR88 - Private beta, blocked

- [ ] Do not start until PR87.8 confirms the production gate is open.
- [ ] Keep private beta copy, approved-answer behavior, and production user data blocked until separately reviewed.
- [ ] Require a launch-readiness review before any production ChatGPT/App SDK exposure.

### PR89 - Public launch, blocked

- [ ] Do not start until private beta has a reviewed success signal.
- [ ] Do not open runtime, billing/entitlements, OAuth, provider submission, or public App SDK behavior by assumption.
- [ ] Treat public launch as a separate release decision, not as a continuation of cover-letter quality work.

## Sources

- [[sources/2026-06-23-twoweeks-mcp-chatgpt-app-sdk-roadmap-checkpoint]]
- [[sources/2026-06-12-chatgpt-app-sdk-roadmap-pr41-pr89]]
- [[sources/2026-06-12-non-production-apps-sdk-exploration-plan]]
- [[sources/2026-06-19-pr80b-safe-application-handoff-while-ats-access-pending]]

## Related

- [[product/manual-application-handoff]]
- [[product/product-roadmap]]
- [[product/product-vision]]
- [[product/ai-product-model]]
