---
aliases:
  - Match Review V1 Dogfood Tool — Developer / LLM Note
---

## Purpose  
  
This tool exists to review real saved jobs and validate whether Match Review V1 feels useful in live dogfood.  
  
It is not a benchmark generator.  
It is not a matcher rewrite tool.  
It is not an ATS evaluation tool.  
It is a safe internal review loop for the user-facing job match panel.  
  
The product question is:  
  
Is this scraped job worth this user’s attention?

Not:

Should this employer hire this candidate?

## Current product status

Match Review V1 is dogfood-ready.

Already completed:

- backend `matchReview` contract
- Jobs UI rendering
- compact user-facing copy
- PII/raw-evidence protection
- role-family calibration floor
- 30-fixture deterministic benchmark
- live export workflow
- summary workflow
- dogfood status note

Current status language:

DOGFOOD. READY.  
  
Export simple.  
Labels clear.  
Summary fast.  
Use it now.

## What the dogfood loop does

The loop exports safe visible review records for recent saved jobs.

It lets a reviewer label whether the visible match output makes sense.

It tracks repeated failure types so we patch only real product patterns, not one-off anecdotes.

Flow:

Export live records  
→ label safe visible records  
→ summarize KPI/failure types  
→ patch only repeated patterns

## Commands

### Export 50 live review records

cd my-app  
rtk ./node_modules/.bin/tsx scripts/evals/run-live-match-review-dogfood.ts --limit 50

Default output:

/tmp/match-review-live.json

### Label records

Create or edit:

/tmp/match-review-live-labeled.json

Fill these fields per record:

human_label  
failure_types  
reviewer_notes

### Summarize labeled records

cd my-app  
rtk ./node_modules/.bin/tsx scripts/evals/run-live-match-review-dogfood.ts \  
  --summary-only \  
  --labeled /tmp/match-review-live-labeled.json

## Exported record shape

Each record is safe and compact. It should include only visible/product-facing fields:

type LiveMatchReviewRecord = {  
  jobId: string;  
  jobTitle: string;  
  company: string | null;  
  profileLabel: string | null;  
  
  tier: "strong" | "partial" | "weak" | "unknown";  
  
  verdict:  
    | "strong_lead"  
    | "possible_lead"  
    | "probably_skip"  
    | "not_enough_signal";  
  
  score: number | null;  
  
  one_liner: string | null;  
  why_this_may_interest_you: string[];  
  watch_out: string[];  
  suggested_next_step: string | null;  
  
  visible_requirements_summary: string[];  
  hard_gate_status: "present" | "none" | "unknown";  
  
  human_label: HumanReviewLabel | null;  
  failure_types: MatchReviewFailureType[];  
  reviewer_notes: string;  
};

## Human labels

Use exactly one `human_label` per record.

type HumanReviewLabel =  
  | "makes_sense"  
  | "too_harsh"  
  | "too_generous"  
  | "wrong_reason"  
  | "credential_wrong"  
  | "unsafe_or_leaky"  
  | "not_enough_signal_correct"  
  | "not_enough_signal_wrong";

### Label meanings

#### `makes_sense`

Use when the output is coherent.

Criteria:

- verdict fits score
- reasons support verdict
- watch-outs are fair
- next step is reasonable
- no leak
- no credential hallucination

#### `too_harsh`

Use when the visible job/profile signals suggest more relevance than the system gives.

Examples:

- same-family job gets `probably_skip`
- title family matches but score is 0
- multiple overlaps exist but the score stays very low

#### `too_generous`

Use when the system overrates a weak or unrelated match.

Examples:

- unrelated role gets `possible_lead` or `strong_lead`
- hard credential is missing but score stays high
- generic/weak overlap creates a strong match

#### `wrong_reason`

Use when verdict may be acceptable but explanation is poor.

Examples:

- reasons are vague
- reasons do not explain the score
- reasons are irrelevant
- watch-outs are confusing

#### `credential_wrong`

Use when credential handling is wrong.

Examples:

- required license inferred without evidence
- required credential ignored
- preferred credential treated as blocker

#### `unsafe_or_leaky`

Use if the visible export contains raw/unsafe data.

Examples:

- email
- phone
- raw resume paragraph
- raw job source text
- source blob
- debug phrase

#### `not_enough_signal_correct`

Use when the system correctly avoids a confident match because data is insufficient.

#### `not_enough_signal_wrong`

Use when the system had enough visible signal but still fell back to no-signal, or when it made a confident judgment despite insufficient signal.

## Failure types

Use zero or more `failure_types`.

type MatchReviewFailureType =  
  | "false_zero"  
  | "dangerous_overmatch"  
  | "credential_hallucination"  
  | "preferred_as_blocker"  
  | "generic_fragment_leak"  
  | "raw_evidence_leak"  
  | "verdict_reason_contradiction"  
  | "bad_next_step"  
  | "no_signal_misclassified"  
  | "too_harsh"  
  | "too_generous"  
  | "unclear_copy";

## Special tracked risk

Known current dogfood risk:

Sparse same-family jobs can still look too harsh.

Tracking convention:

{  
  "human_label": "too_harsh",  
  "failure_types": ["too_harsh"],  
  "reviewer_notes": "sparse_same_family: title family is plausible but extracted evidence is thin"  
}

Use `sparse_same_family` in `reviewer_notes`. Do not add schema churn unless repeatedly needed.

## Safety rules

The exported or labeled files must not contain:

raw CV body  
full resume text  
raw job source blob  
email addresses  
phone numbers  
UUID-like raw source identifiers  
debug scorer evidence arrays  
"maps to profile evidence"  
"weak_lead"

If any unsafe field appears:

- stop labeling
- mark `unsafe_or_leaky`
- add `raw_evidence_leak`
- report the exact field
- do not create more private review artifacts

## Optional safety scan

rtk rg -n "rawDescription|raw_text|raw resume|full resume|maps to profile evidence|weak_lead|@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}|[0-9]{3}[-. ][0-9]{3}[-. ][0-9]{4}" \  
  /tmp/match-review-live.json \  
  /tmp/match-review-live-labeled.json

Expected: no matches.

## KPI summary

The summary should report:

reviewed_count  
makes_sense_count  
makes_sense_rate  
too_harsh_count  
too_generous_count  
wrong_reason_count  
credential_wrong_count  
unsafe_or_leaky_count  
false_zero_count  
dangerous_overmatch_count  
credential_hallucination_count  
preferred_as_blocker_count  
generic_fragment_leak_count  
raw_evidence_leak_count  
verdict_reason_contradiction_count  
bad_next_step_count  
no_signal_misclassified_count  
unclear_copy_count  
sparse_same_family_too_harsh_count

## Internal dogfood target

For 30–50 live jobs:

reviewed_count >= 30  
makes_sense_rate >= 80%  
false_zero_count = 0  
credential_hallucination_count = 0  
raw_evidence_leak_count = 0  
critical verdict_reason_contradiction_count = 0

## When to patch

Do not patch because of one weird case.

Patch only when the summary shows a repeated pattern.

Examples:

### Patch calibration if:

too_harsh_count repeats  
false_zero_count > 0  
sparse_same_family_too_harsh_count repeats

### Patch credential logic if:

credential_hallucination_count > 0  
preferred_as_blocker_count > 0

### Patch copy if:

wrong_reason_count repeats  
unclear_copy_count repeats  
bad_next_step_count repeats

### Patch safety immediately if:

raw_evidence_leak_count > 0  
unsafe_or_leaky_count > 0

## Non-goals

Do not do these in the dogfood loop:

no matcher rewrite  
no scoring change unless repeated failures prove it  
no direct Mistral reviewer  
no embeddings  
no Proposal Forge change  
no Jobs UI redesign  
no scraping/import changes  
no broad migrations  
no weak_lead reintroduction

## Recommended final report format

After labeling and summarizing, report:

# Match Review V1 Dogfood Summary  
  
## Run  
  
- Exported:  
- Labeled:  
- File:  
- Date:  
  
## KPI  
  
| Metric | Value | Target | Pass |  
|---|---:|---:|---|  
| reviewed_count |  | >=30 |  |  
| makes_sense_rate |  | >=80% |  |  
| false_zero_count |  | 0 |  |  
| credential_hallucination_count |  | 0 |  |  
| raw_evidence_leak_count |  | 0 |  |  
| verdict_reason_contradiction_count |  | 0 critical |  |  
  
## Top failure types  
  
1.  
2.  
3.  
  
## Safe examples  
  
Use only safe exported fields:  
- jobTitle  
- verdict  
- score  
- one_liner  
- why  
- watch_out  
- reviewer_notes  
  
## Recommendation  
  
Choose one:  
- approve dogfood continuation  
- needs narrow calibration patch  
- needs copy patch  
- needs credential patch  
- needs safety patch  
  
## Scope confirmation  
  
- no matcher rewrite  
- no scoring change  
- no direct LLM reviewer  
- no embeddings  
- no Proposal Forge change  
- no Jobs UI redesign  
- no raw data exposure

## Final success language

DOGFOOD LOOP.  
RUN.  
  
Real jobs checked.  
Failures classified.  
Patterns visible.  
Matcher untouched.


### Use it for one real session

For the next few days, every time you scrape jobs, watch only these:

Does the verdict make sense?  
Is the reason useful?  
Is the next step useful?  
Is it too harsh?  
Is it too generous?  
Any credential weirdness?

Do **not** change code for one weird case.

### 3. Patch only if a pattern repeats

Patch only if you hit:

false_zero_count > 0  
credential_hallucination_count > 0  
raw_evidence_leak_count > 0  
verdict contradiction > 0  
sparse_same_family too_harsh >= 3  
too_generous >= 3  
unclear_copy >= 3

### 4. Move back to product UX

The next valuable product work is likely **Jobs Page v2**, not more matching logic.

Specifically:

Make the job detail page answer:  
1. Is this relevant?  
2. Am I a good fit?  
3. What should I do next?

Your Match Review now supports that. Use it as the center of the Jobs detail experience.

## One-line plan

Commit. Dogfood. Track failures. Patch only patterns. Move to Jobs Page UX.

Twoweeks version:

MATCH. DONE.  
Use it.  
Watch it.  
Patch patterns.  
Build the page.