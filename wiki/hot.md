---
title: "Hot Cache - twoweeks"
category: overview
status: current
created: 2026-05-02
updated: 2026-06-23
---

# Hot Cache

This page is the active-memory cache for LLM retrieval. It is overwrite-only and non-canonical. Use it to choose the next pages to read, then trust current durable pages when details matter.

## Current Focus

twoweeks is an active job application operating system centered on CV ingestion/parsing, canonical editable resume data, and contextual generation of resumes, cover letters, and proposals.

Two active workstreams must stay separate:

- Cover-letter quality: PR230-PR245 are merged, PR246 is merged and the post-merge Mistral V2 canary is clean, so internal Mistral V2 canary expansion is GO. Canonical page: [[tasks/2026-06-22-cover-letter-quality-production-roadmap]].
- Twoweeks MCP / ChatGPT App SDK: current checkpoint is PR87.8 production-gate reconciliation after PR245; PR80B manual handoff is implemented and is the safe delivery boundary; PR88 private beta and PR89 public launch remain blocked. Canonical pages: [[product/chatgpt-app-sdk-roadmap]] and [[product/manual-application-handoff]].

Do not combine these workstreams in one implementation PR. Shared branch/base references such as `application-os-foundation` and PR245 are coordination anchors, not permission to mix cover-letter prompt work with MCP/App SDK launch or handoff work.

## Key Active Facts

- Product truth is `twoweeks`; CVForge and ProposalForge are internal module names.
- Parser truth should flow through structured sections, especially `currentCv.sections[*].structuredContent`, when structured sections are valid.
- Export truth is generated final PDF/DOCX output from normalized data, not the preview DOM alone.
- Cover-letter quality PR246 is merged. It must not enable Mistral V2 by default, quality repair, Qwen premium behavior, MCP/App SDK tooling, OAuth, manual handoff, or launch-gate work.
- MCP/App SDK PR87.8 must keep runtime endpoints, `tools/list`, `tools/call`, OAuth, real handlers, outbound HTTP, model calls, export/download/send/submit/apply, approved answer copy, PR80-live, billing, and production behavior blocked until reviewed.
- Manual handoff PR80B exists in code and tests. It must not claim provider submission. `provider_verified_submitted` remains unreachable; `user_reported_submitted` is the highest external reported state.
- `wiki/index.md` and `wiki/log.md` remain mandatory for every persistent wiki mutation.
- The wiki ingest path is `rawinput/ -> raw/`; `raw/` is immutable after ingest.

## Canonical Pages To Read

- Cover-letter quality: [[tasks/2026-06-22-cover-letter-quality-production-roadmap]], [[sources/2026-06-23-cover-letter-quality-pr246-merge-checkpoint]], [[sources/2026-06-23-cover-letter-quality-production-roadmap-updated-checklist]]
- MCP / ChatGPT App SDK: [[product/chatgpt-app-sdk-roadmap]], [[product/manual-application-handoff]], [[sources/2026-06-23-twoweeks-mcp-chatgpt-app-sdk-roadmap-checkpoint]]
- Product state: [[overview]], [[entities/twoweeks]], [[product/product-roadmap]], [[product/product-vision]]
- Parser/import: [[concepts/cv-parsing-pipeline]], [[concepts/cv-families]], [[tech/import-ocr-pipeline]]
- Export/layout: [[tech/export-pipeline]], [[tech/preview-to-print-pipeline]], [[tech/workshop-pagination]]
- Wiki operations: [[meta/llm-wiki-pattern]], [[meta/temporal-management]], [[meta/codex-prompting-standards]]

## Recent Changes

- 2026-06-23: Separated active execution checklists so cover-letter PR246 is not collapsed with MCP/App SDK PR87.8/PR88/PR89 or PR80B manual handoff.
- 2026-06-23: Clarified that PR80B manual handoff is implemented/tested; the remaining items are guardrails and PR80-live/launch blockers, not PR80B initial implementation.
- 2026-06-23: Updated cover-letter quality status: PR246 merged, post-merge Mistral V2 canary clean, and internal Mistral V2 canary expansion is GO; quality repair and production remain NO-GO.
- 2026-06-23: Added the PR246 merge checkpoint source so the latest merge/canary state is routed before the older checklist checkpoint.
- 2026-06-23: Ingested the updated cover-letter checklist, ChatGPT/App SDK checkpoint, PR41-PR89 roadmap, and PR80B manual handoff source; `rawinput/` returned to `README.md` only.
