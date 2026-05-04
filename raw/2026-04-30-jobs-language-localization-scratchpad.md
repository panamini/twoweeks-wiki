# Jobs Language Localization Scratchpad

## Status

- Current PR3 fixed multilingual job understanding for `en`, `fr`, `es`, `pt`, `it`, and `de`.
- Current PR3 did not implement user-preferred output language.
- Job extraction can now preserve valid non-English LLM rows when the saved job language was previously misdetected.

## Follow-Up Goal

Let the Jobs module display extracted summary, requirements, keywords, and match explanation in the user's preferred language, while preserving the original job-posting source language.

## Why This Should Be A Separate Slice

- It touches preference storage, extraction prompt contract, cache identity, review expectations, and possibly match wording.
- It should not be mixed into PR3 split-pane/extraction readiness.
- Existing cache rows were generated without a target display language, so cache keys need to account for output language before localization is enabled.

## Proposed Shape

1. Define a `preferredLanguage` / `outputLanguage` source of truth.
   - Start with profile/account preference if already present.
   - Otherwise default to `en`.

2. Pass output language into job extraction.
   - Keep `rawLanguageDetected` as source language.
   - Add `displayLanguage` or `outputLanguage` to the extraction request metadata.
   - Prompt: preserve facts from the source posting; write normalized display text in the requested output language.

3. Update cache identity.
   - Include output language in the job extraction cache key or row metadata.
   - Do not reuse an English normalized row for a French display preference.

4. Add UI/review semantics.
   - Show extracted fields in preferred language.
   - Keep "Open Posting" and raw posting source unchanged.
   - Optional: small "Source language: French / Display: English" metadata in a low-noise details area, not a permanent banner.

5. Tests.
   - Spanish/French job + English preference returns English display text.
   - French job + French preference returns French display text.
   - Cache does not cross-contaminate between output languages.
   - Existing English default behavior remains unchanged.

## Product Note

Do not add a visible language dropdown inside the Jobs detail pane in the first pass. Prefer account/profile preference first. Add per-job override later only if users need it.
