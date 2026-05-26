

---



## Purpose

Two Weeks should support international growth without turning localization into a blocker.

The product needs a language system that is:

- **Small enough to ship**
    
- **Broad enough to adapt**
    
- **Structured enough for Europe**
    
- **Ready for document generation in more languages than the UI**
    
- **Not tied to one guessed market order forever**
    

The key principle: **UI language, document language, and market localization are separate decisions.**

---

## Core distinction

Two Weeks must not treat “language support” as one boolean.

There are three different language layers:

|Layer|Meaning|Example|
|---|---|---|
|**UI language**|App chrome: Settings, dashboard, jobs, CV editor, proposal editor, buttons, errors, accessibility labels|User runs the app in French|
|**Document language**|Language used for generated CVs, proposals, application messages, exports|User writes an English CV for a UK job while using French UI|
|**Market language**|Landing pages, ads, SEO, onboarding, support content|German landing page for DACH acquisition|

This separation protects the product from over-localizing the app too early while still allowing users to generate useful job documents in many languages.

---

## Strategic default

Launch with a **narrow live UI** and a **wide document-language registry**.

```txt
Live UI first:
English + French

Next UI candidates:
Spanish + German

Later UI candidates:
Italian + Portuguese + Polish + Dutch

Document languages:
Broader from the beginning, if model quality is acceptable.

Marketing languages:
Only where acquisition or conversion justifies dedicated pages.
```

The rationale: Europe is large, but language ROI is uneven. Eurostat lists Germany, France, Italy, Spain, and Poland as the five most populous EU countries, which supports prioritizing German, French, Italian, Spanish, and Polish over smaller-language UI work. ([European Commission](https://ec.europa.eu/eurostat/web/interactive-publications/demography-2025?utm_source=chatgpt.com "Demography of Europe – 2025 edition - Interactive publications")) Eurobarometer’s 2024 language survey also shows English as the dominant foreign language in the EU, followed by French, German, and Spanish, which supports an early English/French/Spanish/German focus. ([European Union](https://europa.eu/eurobarometer/surveys/detail/2979?utm_source=chatgpt.com "Europeans and their languages - May 2024 - - Eurobarometer ...")) For the US, Spanish deserves special attention because the US Census reports Spanish as the most common non-English language spoken in US homes. ([Census.gov](https://www.census.gov/library/stories/2022/12/languages-we-speak-in-united-states.html?utm_source=chatgpt.com "What Languages Do We Speak in the United States?"))

---

## Recommended priority map

|Priority|Language / Region|UI|Documents|Marketing|Notes|
|---|---|--:|--:|--:|---|
|**P0**|English `en`|Yes|Yes|Yes|Core market. Global default.|
|**P0**|French `fr`|Yes|Yes|Yes|Strong wedge. Important for France, Belgium, Switzerland, Luxembourg, Canada later.|
|**P1**|Spanish `es`|Soon|Yes|Yes|High reach: Spain, US Spanish speakers, later Latin America.|
|**P1**|German `de`|Soon|Yes|Yes|Germany, Austria, Switzerland. Use `de` first; add `de-AT` / `de-CH` only if needed.|
|**P2**|Italian `it`|Later|Yes|Maybe|Major EU market.|
|**P2**|Portuguese `pt`|Later|Yes|Maybe|Start `pt`; split `pt-PT` / `pt-BR` only when needed.|
|**P2**|Polish `pl`|Later|Yes|Maybe|Better EU ROI than many smaller languages. Strong Central/Eastern Europe candidate.|
|**P2**|Dutch `nl`|Later/maybe|Yes|Maybe|Valuable market, but English UI may be acceptable early.|
|**P3**|Greek `el`|Later|Yes|No|Technically straightforward, smaller UI priority.|
|**P3**|Hungarian `hu`|Later|Yes|No|Useful document language, not first UI.|
|**P3**|Lithuanian `lt`|Later|Yes|No|Add to registry, not live UI. More plural complexity than Estonian/Greek.|
|**P3**|Estonian `et`|Later|Yes|No|Small but tech-savvy. Document-first.|
|**P3**|Russian `ru`|Later/no|Yes|No|Document-first unless analytics justify UI.|
|**P4**|Arabic `ar`|Later|Yes|Later|High potential, but real RTL investment.|
|**P4**|Irish `ga`|No/later|Maybe|No|Low UI ROI; Ireland is covered by English for launch.|

---

## Architecture rule

Add languages to the codebase in three separate lists:

```ts
KNOWN_LOCALES
ENABLED_UI_LOCALES
ENABLED_DOCUMENT_LANGUAGES
ENABLED_MARKETING_LOCALES
```

A language can be:

```txt
Known by the system
Allowed for AI documents
Hidden from UI Settings
Not yet used for marketing
```

This allows Two Weeks to add Lithuanian, Estonian, Russian, Greek, Polish, Hungarian, Arabic, or other languages without promising a fully translated product.

---

## Suggested locale registry

```ts
export const LOCALE_REGISTRY = {
  en: {
    nativeName: "English",
    dir: "ltr",
    ui: true,
    documents: true,
    marketing: true,
    qaStatus: "production",
    priority: "P0",
  },
  fr: {
    nativeName: "Français",
    dir: "ltr",
    ui: true,
    documents: true,
    marketing: true,
    qaStatus: "production",
    priority: "P0",
  },

  es: {
    nativeName: "Español",
    dir: "ltr",
    ui: false,
    documents: true,
    marketing: true,
    qaStatus: "planned",
    priority: "P1",
  },
  de: {
    nativeName: "Deutsch",
    dir: "ltr",
    ui: false,
    documents: true,
    marketing: true,
    qaStatus: "planned",
    priority: "P1",
  },

  it: {
    nativeName: "Italiano",
    dir: "ltr",
    ui: false,
    documents: true,
    marketing: false,
    qaStatus: "planned",
    priority: "P2",
  },
  pt: {
    nativeName: "Português",
    dir: "ltr",
    ui: false,
    documents: true,
    marketing: false,
    qaStatus: "planned",
    priority: "P2",
  },
  pl: {
    nativeName: "Polski",
    dir: "ltr",
    ui: false,
    documents: true,
    marketing: false,
    qaStatus: "planned",
    priority: "P2",
  },
  nl: {
    nativeName: "Nederlands",
    dir: "ltr",
    ui: false,
    documents: true,
    marketing: false,
    qaStatus: "planned",
    priority: "P2",
  },

  el: {
    nativeName: "Ελληνικά",
    dir: "ltr",
    ui: false,
    documents: true,
    marketing: false,
    qaStatus: "watch",
    priority: "P3",
  },
  hu: {
    nativeName: "Magyar",
    dir: "ltr",
    ui: false,
    documents: true,
    marketing: false,
    qaStatus: "watch",
    priority: "P3",
  },
  lt: {
    nativeName: "Lietuvių",
    dir: "ltr",
    ui: false,
    documents: true,
    marketing: false,
    qaStatus: "watch",
    priority: "P3",
  },
  et: {
    nativeName: "Eesti",
    dir: "ltr",
    ui: false,
    documents: true,
    marketing: false,
    qaStatus: "watch",
    priority: "P3",
  },
  ru: {
    nativeName: "Русский",
    dir: "ltr",
    ui: false,
    documents: true,
    marketing: false,
    qaStatus: "watch",
    priority: "P3",
  },

  ar: {
    nativeName: "العربية",
    dir: "rtl",
    ui: false,
    documents: true,
    marketing: false,
    qaStatus: "watch",
    priority: "P4",
  },
} as const;
```

Use BCP 47 language tags for `lang` values. MDN notes that the HTML `lang` attribute takes a BCP 47 language tag, and that pages should specify an appropriate value. ([MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/lang?utm_source=chatgpt.com "lang HTML global attribute - MDN Web Docs - Mozilla"))

---

## Derived lists

```ts
export const ENABLED_UI_LOCALES = Object.entries(LOCALE_REGISTRY)
  .filter(([, meta]) => meta.ui && meta.qaStatus === "production")
  .map(([locale]) => locale);

export const ENABLED_DOCUMENT_LANGUAGES = Object.entries(LOCALE_REGISTRY)
  .filter(([, meta]) => meta.documents)
  .map(([locale]) => locale);

export const ENABLED_MARKETING_LOCALES = Object.entries(LOCALE_REGISTRY)
  .filter(([, meta]) => meta.marketing)
  .map(([locale]) => locale);
```

The UI should only show languages where the app is actually translated and QA’d.

The document-language picker may show more languages, but it must be clear that this controls generated job documents, not the app interface.

---

## Promotion rules

A language moves from **document-only** to **UI candidate** when there is enough signal.

Track:

```txt
browser locale
selected UI language
selected document language
job post language
job country
export language
paid conversion by country/language
support requests by language
failed generations by language
retention by language
```

Promote a language when at least two or three of these are true:

```txt
High traffic from that locale
High document generation in that language
Paid conversion exists
Repeated user requests
Support friction from English-only UI
Strong SEO/ad opportunity
Good translation QA available
```

Do not promote a language because it is theoretically nice to support.

---

## Release gates for UI language

Before a language becomes visible as a UI language in Settings:

```txt
All required namespaces translated
No missing keys in CI
Plural forms covered
Date and number formatting checked
Main flows QA’d:
  - signup/login
  - dashboard
  - jobs
  - CV editor
  - proposal editor
  - Settings
  - export
  - error states
Accessibility labels translated
Long text overflow checked
Native speaker or strong reviewer pass completed
```

Plural QA matters because languages vary substantially. CLDR documents that languages can have multiple plural categories, and i18next relies on plural forms such as `_one`, `_few`, `_many`, and `_other` with a `count` variable. ([Unicode](https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html?utm_source=chatgpt.com "Language Plural Rules"))

---

## Arabic / RTL rule

Arabic should be prepared architecturally, but not shipped as UI until RTL QA is done.

Implementation requirement:

```ts
document.documentElement.lang = locale;
document.documentElement.dir = LOCALE_REGISTRY[locale].dir;
```

W3C recommends setting `dir="rtl"` on the `html` tag when the overall document direction is right-to-left. ([W3C](https://www.w3.org/International/questions/qa-html-dir.en.html?utm_source=chatgpt.com "Structural markup and right-to-left text in HTML"))

CSS should gradually prefer logical properties:

```css
.card {
  padding-inline: 16px;
  margin-inline-start: 12px;
  border-inline-start: 1px solid var(--border);
}
```

Avoid building new layout code with hardcoded `left` / `right` assumptions where logical CSS is easy.

---

## Region variants

Do not start with too many regional variants.

Use base languages first:

```txt
en
fr
es
de
pt
```

Only split later when real need appears:

```txt
en-US / en-GB
fr-FR / fr-CA / fr-CH
de-DE / de-AT / de-CH
pt-PT / pt-BR
es-ES / es-MX / es-US
ar-SA / ar-AE / ar-EG / ar-MA
```

Examples:

```txt
“Austrian” is not a separate app language.
Use German `de` first.
Add `de-AT` later only for Austrian-specific wording, legal norms, date conventions, or marketing pages.
```

---

## Product rule for generated documents

Generated job documents should not blindly follow the UI language.

Correct behavior:

```txt
UI language:
French

Job post:
English

Target company:
UK

Generated proposal language:
English, unless user overrides it
```

Persist this separately:

```ts
type GeneratedDocumentLanguageMeta = {
  requestedLanguage: "auto" | KnownLocale;
  resolvedLanguage: KnownLocale;
  source: "user" | "job" | "uiFallback" | "systemDefault";
};
```

Document generation should support more languages earlier than the UI, but should store the requested and resolved language for debugging and quality review.

---

## Current recommended order

```txt
P0 live UI:
en, fr

P1 next:
es, de

P2 serious Europe:
it, pt, pl, nl

P3 document-first / watch:
el, hu, lt, et, ru

P4 later strategic expansion:
ar and selected regional variants

Deprioritized UI:
ga unless there is a specific Irish-language strategy
```

---

## One-line principle

**Two Weeks should localize the app slowly, generate documents broadly, and let real usage decide the next market.**