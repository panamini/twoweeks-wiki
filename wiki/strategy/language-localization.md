---
title: "Language Localization Strategy"
category: strategy
tags: [localization, i18n, products, roadmap]
created: 2026-05-26
updated: 2026-05-26
status: current
valid_from: 2026-05-26
related: [[design/locale-typography-rules]], [[product/product-roadmap]], [[product/job-library]]
sources: [2026-05-26-two-weeks-language-map-reference-note]
---

# Language Localization Strategy

## Current state

Language support is now a separate strategy layer: `UI language` for the app surface, `document language` for generated outputs, and `market language` for acquisition surfaces.

This avoids false assumptions that UI localization and document output support must progress at the same speed.

## Current status (2026-05-26)

- `en`, `fr`, `es` are active for UI, document generation, and marketing.
- `de`, `ru`, `pl`, `ar` are available in document generation and included in safe preview/fallback logic; they are not surfaced as UI locales yet.
- `ar` is doc-ready only: document export uses `lang="ar"` and right-to-left direction, while app UI direction is still driven by UI locale only.
- Proposal generation metadata is now threaded through the pipeline as:
  - `requestedLanguage`
  - `resolvedLanguage`
  - `languageSource`
  - `jobDetectedLanguage`
- Deterministic helper copy in proposal output/signature/enforcement no longer applies English fallback text to non-`en`/`fr` document languages.
- A dedicated smoke pass has confirmed behavior for `en`, `fr`, `de`, `ru`, `ar`, `pl` with explicit checks against English salutation/signoff leakage.

## Language layers

- **UI language** controls app chrome, settings, error messages, and accessibility labels.
- **Document language** controls generated CV/proposal text, generated emails, and export text behavior.
- **Market language** controls landing pages and acquisition content.

The rule is: document language can be broader than UI language; they are independent rollout surfaces.

## Launch ordering

### P0 — Live
- `en`, `fr`, `es` for UI/documents/marketing.

### P1 — Near-term
- `de` documents + marketing-first; UI remains hidden candidate.

### P2 — Europe expansion
- `it`, `pt`, `pl`, `nl` documents first, marketing as needed.

### P3 — Document-first watchlist
- `el`, `hu`, `lt`, `et` as document-only until data justifies more.
- `ru` now moved to document-ready status from watchlist for active probe and export validation.

### P4 — Strategic + deferred UI
- `ar` as planned RTL effort; `ga` only for a specific Irish strategy.
- Optional future document candidates after production-safe probes and QA:
  - `zh` (Chinese)
  - `ta` (Tamil)

`ga` is intentionally excluded unless an explicit Irish strategy resumes.

## Architecture baseline

Language registries should be explicit and query-friendly:

- `KNOWN_LOCALES`
- `ENABLED_UI_LOCALES`
- `ENABLED_DOCUMENT_LANGUAGES`
- `ENABLED_MARKETING_LOCALES`

Document generation should preserve requested vs resolved language metadata for traceability and quality review.

## Promotion gates

Promotion from document-only to UI candidate should require multiple positive signals:

- user traffic and repeated use from that locale
- meaningful document generation in that language
- paid conversion signal
- support request pressure from non-UI users
- SEO/opportunity evidence
- translation QA and product-level acceptance

Do not promote a language merely because it is theoretically easy to add.

## UI release gates

Before surfacing a UI language:

- namespace completeness
- no missing translation keys in CI
- plural rules coverage
- date and number formatting check
- end-to-end QA on primary flows
- native or strong reviewer pass

## Related controls

- Keep RTL logic explicit (`lang`, `dir`) for future expansion.
- Prefer logical CSS (`margin-inline`, `padding-inline`) when adding direction-sensitive styles.
- Continue using `design/locale-typography-rules.md` for output-level typography behavior.
