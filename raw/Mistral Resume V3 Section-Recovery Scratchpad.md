

This note is for future LLMs or engineers debugging the current main behavior of Mistral OCR resume parsing.

Scope:

- explicit Languages / Skills section detection
- deterministic section-local recovery
- acceptance and contradiction gating
- one allowed OCR retry
- request-level parser-quality telemetry

Relevant files:

- cv_parser_service/mistral_resume_v3/pipeline.py
- cv_parser_service/mistral_resume_v3/post_validation.py
- cv_parser_service/mistral_ocr.py
- cv_parser_service/tests/test_mistral_resume_v3_pipeline.py

## Mental Model

The parser does not blindly trust the annotation when OCR markdown shows explicit section evidence.

Current order on main:

1. fetch OCR + annotation
2. normalize parsed annotation
3. detect explicit section evidence from OCR markdown
4. gate normalized output against that evidence
5. if needed, run deterministic section-local recovery
6. re-parse and re-normalize recovered payload
7. run a second validation pass
8. if still contradictory, mark retry-eligible
9. bytes/url entrypoint may perform exactly one OCR re-fetch

10. after retry, either accept or fail with section_evidence_contradiction

The important design constraint is:

- _run_resume_pipeline_from_ocr_result(...) is pure with respect to OCR fetch
- retry ownership lives in run_resume_pipeline_from_bytes(...) and run_resume_pipeline_from_url(...)

## Where Section Detection Comes From

Explicit section detection is derived from OCR markdown, not from the annotation.

Code path:

- _extract_explicit_sections_from_pages(...)
- _classify_heading(...)
- RAW_SECTION_HEADING_ALIASES

Matching is normalized through _normalize_lookup(...), so heading detection is:

- case-insensitive
- accent-insensitive
- whitespace-normalized
- tolerant of trailing : / dashes

Current language aliases include:

- language
- languages
- language skills
- languages spoken
- linguistic skills

Current skills aliases include:

- skills
- expertise
- areas of expertise
- core competencies
- technical skills
- tech stack
- technical stack
- technical background
- capabilities
- key capabilities
- core skills
- tools
- technologies

Important restriction:

- skills recovery is not allowed for every skills-family alias
- actual deterministic skills recovery is only eligible for headings normalized to:
    - skills
    - areas of expertise

That restriction lives in SKILL_RECOVERY_HEADING_ALIASES.

Meaning:

- a heading can count as explicit section evidence for gating
- but still be ineligible as a recovery source

That is intentional.

## Language Recovery Behavior

Language recovery only mines lines inside the explicit language section body.

Code path:

- _extract_explicit_languages_from_sections(...)
- _parse_language_candidate(...)
- _split_inline_language_candidates(...)

Accepted shapes include:

- English
- English: Fluent
- English - Fluent
- English (Fluent)
- split inline multi-values like English | Portuguese

Language recovery preserves explicit levelRaw when present.

Recovery rejects polluted values through:

- _looks_like_language_name(...)
- _language_level_is_polluted(...)
- _language_entry_is_polluted(...)
- _looks_like_section_blob(...)
- _is_heading_value(...)

Examples of things treated as pollution:

- headings as values
- fused multi-section blobs
- values containing obvious skills/expertise markers
- language levels that appear to mention another language or another section

## Skills Recovery Behavior

Skills recovery is section-local and never document-wide.

Code path:

- _skill_sections_eligible_for_recovery(...)
- _extract_explicit_skills_from_sections(...)
- _split_skill_tokens(...)
- _looks_like_grouped_skill_label(...)

Grouped lines are flattened into atomic labels:

- Backend: Python, Node.js  
    becomes:
    - Python
    - Node.js

Important constraints:

- only the matched skills section body is used
- grouped category labels are not emitted as skills
- section blobs and fused content are rejected
- recovery does not run from the whole document

Pollution checks live in:

- _skill_entry_is_polluted(...)
- _looks_like_grouped_skill_blob(...)
- _looks_like_section_blob(...)

## Acceptance Gate

The first gate happens after the initial normalize step.

Code path:

- _collect_section_gate_issues(...)

Current rules:

- if explicit languages section exists and normalized languages is empty, reject
- if explicit languages section exists and normalized languages is polluted, reject
- if explicit skills section exists and normalized skills is empty, reject
- if explicit skills section exists and normalized skills is polluted, reject

This gate is based on explicit OCR markdown evidence, not on model confidence.

## Second Validation Pass

After deterministic recovery, the pipeline re-parses and re-normalizes the repaired payload, then validates again.

Code path:

- _collect_second_validation_issues_after_recovery(...)
- _collect_post_recovery_issues(...)
- _validated_recovered_languages(...)
- _validated_recovered_skills(...)

This second pass is what prevents noisy recovered data from being silently accepted.

If recovered values are still:

- empty
- polluted
- not actually preserved through re-normalization

then the result is rejected.

## Retry Semantics

There is exactly one allowed retry.

Code path:

- _run_resume_pipeline_with_single_retry(...)
- run_resume_pipeline_from_bytes(...)
- run_resume_pipeline_from_url(...)

Retry only happens when the first result returns:

- diagnostics.annotationRetry.eligible == true

That is currently driven by:

- errorType == "section_evidence_contradiction"

Retry does not happen:

- for generic annotation parse failures
- for normal successful parses
- for accepted deterministic recoveries

After retry:

- if clean, return success
- if still contradictory, return fallback with:
    - errorType = "section_evidence_contradiction"

## Diagnostics Contract

Top-level diagnostics always include:

- sectionRecovery
- annotationRetry
- parsingQuality

When a canonical payload exists, the same metadata is mirrored into:

- canonical_payload.diagnostics

Important meaning:

- successful recovery remains authoritative
- successful recovery does not force legacy fallback
- successful recovery does not force partial status by itself

sectionRecovery.<family> carries:

- applied
- source
- reason
- heading

annotationRetry carries:

- attempted
- count
- reason
- eligible
- exhausted

## Parsing Quality Telemetry

Thin request-level telemetry was added to monitor parser quality drift without building a full infra stack.

Code path:

- _collect_parsing_quality_metrics(...)
- _attach_parsing_quality_metrics(...)
- _log_pipeline_quality(...)

Current diagnostics.parsingQuality fields:

- has_languages_section
- languages_extracted
- languages_success
- has_skills_section
- skills_extracted
- skills_success
- recovery_used
- retry_used
- error_type
- hard_failure

Request-level log event:

- logger marker: [mistral-quality]

Logged from:

- run_mistral_ocr_from_bytes(...)
- run_mistral_ocr_from_url(...)

Important:

- this is intentionally thin
- it only logs parser-quality signals
- it is not a general infra monitoring system
- URL logging is sanitized to scheme://host/path

## Real Debug Boundary

If behavior looks wrong in the app, debug in this order:

1. Check the request-boundary quality log in cv_parser_service/mistral_ocr.py
    
    - this tells you whether the parser believed language/skills sections existed
    - whether extraction succeeded
    - whether recovery/retry/hard failure happened
2. Inspect top-level diagnostics
    
    - sectionRecovery
    - annotationRetry
    - parsingQuality
    - mistral_parser_error_type
3. If the parse succeeded, inspect:
    
    - canonical_payload.diagnostics
    - canonical_payload.normalized.languages
    - canonical_payload.normalized.skills
4. If the wrong behavior is “section exists in markdown but field is empty”, inspect:
    
    - extracted explicit section headings
    - whether the heading is only gate-eligible or also recovery-eligible
    - whether second validation rejected the recovered values
5. If retry happened unexpectedly, inspect:
    
    - annotationRetry.reason
    - sectionRecovery.<family>.reason

The earliest useful boundary is almost always:

- OCR markdown section evidence

not:

- downstream UI state
- app mapper rendering
- generic fallback behavior

## Common Failure Modes

### 1. Language heading exists but no languages extracted

Most likely causes:

- annotation returned empty/polluted languages
- deterministic recovery extracted invalid fused values
- second validation rejected recovered values

Look at:

- sectionRecovery.languages.reason
- annotationRetry
- parsingQuality.languages_success

### 2. Skills heading exists but recovery did not run

Most likely cause:

- heading counted as explicit skills evidence for gating
- but was not recovery-eligible under SKILL_RECOVERY_HEADING_ALIASES

Look at:

- sectionRecovery.skills.heading
- sectionRecovery.skills.reason

### 3. Recovery happened but final result still failed

Most likely cause:

- second validation rejected recovered values
- retry exhausted and ended in section_evidence_contradiction

Look at:

- errorType
- sectionRecovery
- annotationRetry.exhausted
- parsingQuality.hard_failure

### 4. Telemetry looks wrong

Remember:

- languages_success and skills_success only become true when explicit section evidence exists and normalized output is non-empty
- a request with no explicit section heading should not count as success

## Tests That Matter

Primary regression file:

- test_mistral_resume_v3_pipeline.py

This file covers:

- valid annotation pass-through
- explicit languages/skills recovery
- achievements recovery
- post-recovery second validation
- one allowed retry
- retry exhaustion with section_evidence_contradiction
- heading alias mapping
- parsingQuality diagnostics

Recommended command:

`rtk pytest -q cv_parser_service/tests/test_mistral_resume_v3_pipeline.py`

## Non-Goals Of The Current System

Things intentionally not added:

- confidence-score based gating
- whole-document mining for skills/languages
- broad infra monitoring stack
- few-shot prompt redesign in this phase
- accepting noisy recovered values “just because OCR looked explicit”

## If You Need To Change This Later

Before changing behavior, decide which layer you are changing:

- heading detection
- initial acceptance gate
- deterministic recovery extraction
- second validation
- retry eligibility
- telemetry only

Do not mix those in one patch unless the bug truly spans layers.

If the real symptom is live-only, use the request-boundary quality log first and prove which boundary is wrong before patching anything else.