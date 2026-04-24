

Date: 2026-04-24

## Status

Decision note only. Do not implement these rules in Pass 1, Pass 2A, Pass 2B, Pass 3A, or Pass 3B.

The following layers are frozen unless a later pass explicitly reopens them:

- extraction shadow
- visible summary / requirements / keywords projection
- missing-signal cleanup
- current computeMatchRead
- Pass 3A structured shadow scorer mechanics
- Pass 3B evaluation matrix and invariant harness

## Pass 3B Result Readout

Pass 3B added one deterministic local fixture for each critical family:

- security/licensed
- retail/service
- technical
- admin/office
- healthcare/regulated
- short noisy jobs
- long duplicated scraped jobs
- multilingual jobs

The evaluation harness records a consistent comparison row per fixture:

- fixture id
- family
- old score/tier
- structured score/tier
- matched / partial / missing / unknown counts
- metadata leak count
- provenance completeness
- manual expected label

The current invariant expectation is:

- metadata leak count is 0
- matched/partial outcomes must cite concrete profile evidence and provenance
- absent evidence becomes unknown
- constraints remain separate from positive evidence
- old computeMatchRead remains production source

## Product Decisions For The Future Structured Scorer

### Unknown

Decision: unknown should be worth 0 match credit in the production structured scorer.

Reasoning: unknown means the scorer does not have concrete evidence. It should not increase a candidate's match score. It should be reported separately as an evidence-coverage or confidence issue.

Important distinction:

- unknown is not missing
- unknown does not prove a gap
- unknown does not earn match credit
- high unknown count should reduce score confidence, not fabricate negative evidence

Pass 3A currently uses unknown = 0.25 as temporary shadow scoring. That is not the production decision.

### License And Certification Hard Gates

Decision: licenses and certifications can become hard gates only when all of these are true:

- the job requirement category is license or regulated certification
- the requirement is explicitly required
- the source extraction is eligible, schema-valid, non-fallback, and provenance-backed
- the requirement is legally or operationally necessary for the role
- the profile has no matching license/certification evidence and no pending/equivalent evidence rule applies

Hard gates should not apply to generic optional certifications, vague preferences, or non-regulated nice-to-have credentials.

Hard-gate status should be represented explicitly, not inferred from text alone.

### Source Weights

Decision: evidence source quality should affect scoring before production rollout.

Proposed source priority:

|Source|Relative strength|
|---|---|
|license / certification evidence|strongest for credential requirements|
|experience title / description|strongest for role, skill, responsibility, and environment evidence|
|education / coursework|strong for education, foundation knowledge, and domain training|
|explicit skills|medium-strong, but weaker than concrete experience|
|projects / achievements / publications|medium-strong when directly relevant|
|summary|weak support|
|headline / desired position / target role|weak role-alignment support only|
|raw_text|weakest fallback only|

Raw text must not override structured profile sections.

### Role Alignment

Decision: role_alignment remains support-only.

Desired position, target role, headline, and similar self-declared alignment should help explanation and confidence, but should not be strong proof of capability on their own.

Actual experience titles can match title or support experience; desired roles cannot substitute for concrete experience.

### Tier Mapping

Decision: do not promote the current 75/40 thresholds yet.

Proposed production interpretation to validate in a later pass:

- strong: required evidence coverage is high, no missing hard gate, and unknown count is low
- partial: meaningful required evidence exists, but some required items are partial or unknown
- weak: little concrete evidence, or a required hard gate is missing

Before promotion, tiering should consider both score and evidence coverage. A high score with many unknown required requirements should not be strong.

## Deferred Calibration Work

Do not implement production scoring until a later pass answers:

- exact numeric weights for source quality
- whether unknown count should reduce confidence, cap tier, or both
- exact hard-gate taxonomy for regulated roles
- final score formula separating match credit from confidence/coverage
- final tier thresholds after at least two credible fixtures per critical family where data exists