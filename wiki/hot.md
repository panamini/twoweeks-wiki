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

- Cover-letter quality: PR230-PR245, PR246, PR248, and PR249 are merged. PR249 completed the staged internal Mistral V2 evidence gate from `application-os-foundation` at `d628bed79c0063d2c06c836015e87d313385bbd2` and records `COVER_LETTER_MISTRAL_V2_READY_FOR_INTERNAL_STAGING_ONLY`. Production full GO is not approved; quality repair remains OFF; Qwen remains legacy-only; GPT remains unchanged. Canonical page: [[tasks/2026-06-22-cover-letter-quality-production-roadmap]].
- Twoweeks MCP / ChatGPT App SDK: current checkpoint is PR87.8 production-gate reconciliation after PR245; PR80B manual handoff is implemented and is the safe delivery boundary; PR88 private beta and PR89 public launch remain blocked. Canonical pages: [[product/chatgpt-app-sdk-roadmap]] and [[product/manual-application-handoff]].

Do not combine these workstreams in one implementation PR. Shared branch/base references such as `application-os-foundation` and PR245 are coordination anchors, not permission to mix cover-letter prompt work with MCP/App SDK launch or handoff work.

## Key Active Facts

- Product truth is `twoweeks`; CVForge and ProposalForge are internal module names.
- Parser truth should flow through structured sections, especially `currentCv.sections[*].structuredContent`, when structured sections are valid.
- Export truth is generated final PDF/DOCX output from normalized data, not the preview DOM alone.
- Cover-letter quality PR249 is merged and the staged internal Mistral V2 gate is clean: 23 total, 19 PASS, 4 SKIPPED only for missing committed French CV-backed fixtures, 0 FAIL, no PR246 forbidden extrapolation hits, no PR248 no-CV leakage hits. It must not enable production, quality repair, Qwen premium behavior, GPT behavior changes, MCP/App SDK tooling, OAuth, manual handoff, or launch-gate work.
- MCP/App SDK PR87.8 must keep runtime endpoints, `tools/list`, `tools/call`, OAuth, real handlers, outbound HTTP, model calls, export/download/send/submit/apply, approved answer copy, PR80-live, billing, and production behavior blocked until reviewed.
- Manual handoff PR80B exists in code and tests. It must not claim provider submission. `provider_verified_submitted` remains unreachable; `user_reported_submitted` is the highest external reported state.
- `wiki/index.md` and `wiki/log.md` remain mandatory for every persistent wiki mutation.
- The wiki ingest path is `rawinput/ -> raw/`; `raw/` is immutable after ingest.

## Canonical Pages To Read

- Cover-letter quality: [[tasks/2026-06-22-cover-letter-quality-production-roadmap]], [[sources/2026-06-23-cover-letter-quality-pr249-staged-internal-gate]], [[sources/2026-06-23-cover-letter-quality-pr248-merge-checkpoint]], [[sources/2026-06-23-cover-letter-quality-pr246-merge-checkpoint]], [[sources/2026-06-23-cover-letter-quality-production-roadmap-updated-checklist]]
- MCP / ChatGPT App SDK: [[product/chatgpt-app-sdk-roadmap]], [[product/manual-application-handoff]], [[sources/2026-06-23-twoweeks-mcp-chatgpt-app-sdk-roadmap-checkpoint]]
- Product state: [[overview]], [[entities/twoweeks]], [[product/product-roadmap]], [[product/product-vision]]
- Parser/import: [[concepts/cv-parsing-pipeline]], [[concepts/cv-families]], [[tech/import-ocr-pipeline]]
- Export/layout: [[tech/export-pipeline]], [[tech/preview-to-print-pipeline]], [[tech/workshop-pagination]]
- Wiki operations: [[meta/llm-wiki-pattern]], [[meta/temporal-management]], [[meta/codex-prompting-standards]]

## Recent Changes

- 2026-06-23: Recorded PR249 merge and staged internal Mistral V2 gate: `COVER_LETTER_MISTRAL_V2_READY_FOR_INTERNAL_STAGING_ONLY`; production full GO remains separate, quality repair OFF, Qwen legacy-only, GPT unchanged.
- 2026-06-23: Separated active execution checklists so cover-letter PR246 is not collapsed with MCP/App SDK PR87.8/PR88/PR89 or PR80B manual handoff.
- 2026-06-23: Updated cover-letter quality status for merged PR248: no-CV candidate-history boundary tightened; next step is post-merge verification, then staged internal Mistral V2 expansion/evidence gate if clean.
- 2026-06-23: Clarified that PR80B manual handoff is implemented/tested; the remaining items are guardrails and PR80-live/launch blockers, not PR80B initial implementation.
- 2026-06-23: Updated cover-letter quality status: PR246 merged, post-merge Mistral V2 canary clean, and internal Mistral V2 canary expansion is GO; quality repair and production remain NO-GO.
- 2026-06-23: Added the PR246 merge checkpoint source so the latest merge/canary state is routed before the older checklist checkpoint.
- 2026-06-23: Ingested the updated cover-letter checklist, ChatGPT/App SDK checkpoint, PR41-PR89 roadmap, and PR80B manual handoff source; `rawinput/` returned to `README.md` only.
