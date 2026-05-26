---
title: "Two Weeks Language Map"
category: source
tags: [i18n, localization, strategy, markets, ui, documents]
created: 2026-05-26
updated: 2026-05-26
status: current
type: scratchpad
related: [[design/locale-typography-rules]], [[strategy/language-localization]], [[product/product-roadmap]]
---

# Two Weeks Language Map

## Summary

Two Weeks should separate language decisions by layer:

- **UI language**: app chrome and accessibility labels.
- **Document language**: language used by generated resumes, proposals, and export content.
- **Market language**: landing/ads/onboarding/SEO and conversion surfaces.

That separation allows fast growth without overextending UI translation.

## Key points

- Product launch can keep a narrow live UI and a broader document language registry.
- Recommended core order:  
  - P0 UI + documents + marketing: English (`en`), French (`fr`)
  - P1 documents + marketing, later UI: Spanish (`es`), German (`de`)
  - P2 serious Europe: Italian (`it`), Portuguese (`pt`), Polish (`pl`), Dutch (`nl`)
  - P3 document-first/watch: Greek (`el`), Hungarian (`hu`), Lithuanian (`lt`), Estonian (`et`), Russian (`ru`)
  - P4 later: Arabic (`ar`) with RTL work; Irish (`ga`) only if explicit strategy.
- Keep base languages first (`en`, `fr`, `es`, `de`, `pt`) and only split regional variants when there is real need.
- Suggested data model:
  - `KNOWN_LOCALES`
  - `ENABLED_UI_LOCALES`
  - `ENABLED_DOCUMENT_LANGUAGES`
  - `ENABLED_MARKETING_LOCALES`
- UI should show only QA-complete translated locales; document picker can be broader.
- Track promotion to UI candidate from product signals (traffic, generation volume, conversion, requests, support friction, translation QA, etc.) rather than theoretical parity.
- For Arabic/RTL, set language and direction coherently at document root (`lang`, `dir`) and validate logical CSS.
- Generated content language should remain decoupled from UI locale by default and logged in metadata for debugging.

## Implications

- Localization scope can be treated as an onboarding and market-expansion roadmap, not as an all-or-nothing all-language release.
- Language expansion should be evidence-driven with explicit gates and QA before exposing new UI locales.
- The document layer can progress faster than the UI layer as long as generated language remains correct and observable.

## Touched pages

- [[design/locale-typography-rules]]
- [[product/product-roadmap]]
- [[strategy/language-localization]]
