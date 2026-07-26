---
title: "Hot Cache - twoweeks"
category: overview
status: current
created: 2026-05-02
updated: 2026-07-27
---

# Hot Cache

This page is the active-memory cache for LLM retrieval. It is overwrite-only and non-canonical. Use it to choose pages, then trust durable pages.

## Current Focus

twoweeks centers on CV ingestion/parsing, canonical saved profile/CV data, and personalized resumes, cover letters, and proposals.

Keep two workstreams separate:

- MCP commercial launch: V19 proved the current-head private-beta transport, confidential-client OAuth, six-tool catalog and one protected read-only call. The result was `NO_DATA`; commercial value is not yet proven. The next slice is `COMMERCIAL-MCP-1`, a useful but bounded read-only projection.
- Cover-letter quality: PR337 (`QUALITY-CL-4`) is ready for merge review at `977f1a29d8b9a5b3f1f67964eff61f46e5373f53`; all 8 GitHub checks pass and the exact-head Codex review is clear. This proves deterministic EN/FR CV-backed prompt/finalizer integrity, not a provider-output quality win or default-model decision.

## Key Active Facts

- Stable endpoint: `https://mcp.twoweeks.ai/mcp`.
- V19 directly proved HEAD `0503832f5671b995b0095841104afc2e33b065ee`, MCP `2025-06-18` and `2025-11-25`, six ordered read-only tools, OAuth token-count delta `30 -> 31`, and exactly one protected `twoweeks.application_package.summarize` call.
- The protected result was the four-field status envelope with `status=NO_DATA`; no summary or private nested data was exposed.
- Current protected tools report availability/status only. A commercial V1 must add safe readiness, bounded counts/categories and next-action codes, then prove `OK` with controlled data.
- Private beta must cover one data-bearing subject and one empty subject before a 3-5 user cohort.
- Public launch, write tools, provider/model calls, export, live submit/apply, refresh tokens and billing remain blocked pending separate reviewed gates.
- The public distribution surface is evolving; decide the final tool catalog before submission because approved tools are snapshot-frozen.
- `application-os-foundation` is verified at PR336 merge `80b4af7a764b37cc57b5bcb25a4f3bfc0a16a23b`.
- Luna low passed the English direct/adjacent development cells but only matched the stable control; do not promote it as a general default.
- Historical French CV-backed EVAL3D vetoes are invalid for quality inference because a canonical formal closing was counted as body content. No provider rerun is required now.
- No-CV remains a separate evidence/UX problem and is byte-locked against QUALITY-CL-4 drift. Any four-cell EN/FR CV-backed old/new comparison requires a separate exact contract and approval after merge; no provider run is automatic.
- Product truth is `twoweeks`; CVForge and ProposalForge are internal module names.
- Cloud-region decision: Twoweeks is US-first; future Convex Cloud and first production parser default to US East (N. Virginia), while parser provider selection remains benchmark-gated. Read [[strategy/us-first-cloud-region]] and [[sources/2026-07-27-us-first-cloud-region]].
- Persistent wiki mutations require `wiki/index.md`, `wiki/log.md`, and usually `wiki/hot.md`.

## Canonical Pages To Read

- MCP commercial roadmap: [[product/chatgpt-app-sdk-roadmap]], [[sources/2026-07-15-mcp-current-head-authenticated-summary-reproof-checkpoint]], [[howto/chatgpt-mcp-private-beta-tunnel-connector]], [[sources/2026-07-13-pr322-mcp-public-catalog-url-checkpoint]]
- Cover-letter quality: [[tasks/2026-06-22-cover-letter-quality-production-roadmap]], [[sources/2026-06-24-cover-letter-mistral-v2-staging-green]]
- Product/parser/export routing: [[overview]], [[concepts/cv-parsing-pipeline]], [[tech/export-pipeline]]
- Cloud region / parser hosting: [[strategy/us-first-cloud-region]], [[tech/local-vs-remote-parser-architecture]], [[howto/local-parser-operations]]
- Wiki operations: [[meta/llm-wiki-pattern]], [[meta/temporal-management]]
