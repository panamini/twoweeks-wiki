---
title: "Jobs Language Localization Scratchpad"
category: source
tags: [jobs, localization, matching, extraction, prompt, cache]
created: 2026-04-30
updated: 2026-05-04
status: current
type: scratchpad
related: [[product/job-library]], [[product/job-match-review]], [[tech/local-vs-remote-parser-architecture]]
---

# Jobs Language Localization Scratchpad

## Status

- PR3 delivered multilingual understanding (`en`, `fr`, `es`, `pt`, `it`, `de`).
- PR3 did not add user-preferred output language.
- Job extraction can preserve valid non-English LLM rows when saved language was misdetected.

## Follow-up goal

Add user-preferred output language support in Jobs while preserving source-language text.

## Why separate slice

Requires preference storage, extraction prompt changes, cache key updates, and UI review semantics; should stay isolated from PR3 parser split-pane extraction readiness work.

## Proposed implementation

1. Define `preferredLanguage` / `outputLanguage` source of truth (profile/account or default `en`).
2. Pass output language into extraction and keep `rawLanguageDetected` separately.
3. Include output language in job extraction cache identity.
4. Render job summary/requirements/keywords/match explanation in preferred language, keep source content unchanged.
5. Add regression tests for cross-language cache and output language behavior.

## Product constraints

No visible language dropdown in Jobs detail pane on first pass. Prefer account/profile-level preference first; per-job override only if needed.

## Source

- `raw/2026-04-30-jobs-language-localization-scratchpad.md`
