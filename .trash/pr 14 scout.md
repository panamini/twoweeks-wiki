You are working in:

```
panamini/neyssan
```

Read `AGENTS.md` first.

Act like a skeptical senior engineer implementing one narrow Distribution-layer PR.

Do not build UI, routes, persistence, Convex functions, generation, export, MCP, Scout runtime, browser automation, crawling, scraping, send/apply/track workflows, approval workflows, or a platform.

This is a cold-start handoff. Start by verifying the current repo state. Do not assume this prompt is fresher than the repository.

# Cold-start handoff — PR14 Controlled ATS Scout Adapters

## Current base

Continue from:

```
application-os-foundation
```

PR13 / PR121 should already be merged.

Expected latest base commit should include:

```
PR13: Internal tool contracts
```

Known merge information from the handoff:

```
PR #121: PR13: Internal tool contracts
state: merged
base: application-os-foundation
```

If the exact SHA differs, do not fail only because of SHA text. Verify that branch history/top commit includes PR13.

Do not touch `main`.

Before implementation, verify the local base state:

```
rtk git fetch origin
rtk git checkout application-os-foundation
rtk git pull --ff-only origin application-os-foundation
rtk git status --short
rtk git log -n 1 --oneline
```

Expected:

```
working tree clean
top commit includes PR13: Internal tool contracts
```

If `application-os-foundation` is not synced after PR13 merge, stop and report:

```
PR14 cannot start until application-os-foundation is synced after PR13 merge.
```

Create the PR14 branch only after this gate passes.

---

# Mandatory baseline verification before coding

Before creating the PR14 branch or editing files, prove the current base is already green.

From `my-app`, run:

```
rtk npx vitest --run src/modules/internal-tool-contracts/__tests__/internalToolContracts.test.ts
rtk npx vitest --run src/modules/application-package/__tests__/applicationPackage.test.ts
rtk npx vitest --run src/modules/cover-letter-artifact/__tests__/coverLetterArtifact.test.ts
rtk npx vitest --run src/modules/resume-variant-artifact/__tests__/resumeVariantArtifact.test.ts
rtk npx vitest --run src/modules/review-cockpit/__tests__/reviewCockpit.test.ts
rtk npx vitest --run src/modules/resume-variant-plan/__tests__/resumeVariantPlan.test.ts
rtk npx vitest --run src/modules/evidence-graph/__tests__/evidenceGraph.test.ts
rtk npx vitest --run src/modules/candidate-evidence/__tests__/candidateEvidence.test.ts
rtk npx vitest --run src/modules/career-knowledge/__tests__/careerKnowledge.test.ts
rtk npx vitest --run convex/__tests__/candidateEvidence.test.ts
rtk npx vitest --run convex/__tests__/applicationHarness.test.ts
rtk npx vitest --run convex/lib/tests/applicationContextBuilder.test.ts
rtk npm test -- application-harness --run
rtk npx tsc --noEmit
```

Then from repo root:

```
rtk git diff --check
rtk git status --short
```

If any baseline command fails before PR14 edits, stop and report the exact failure. Do not implement PR14 on top of a broken base unless the failure is clearly unrelated and explicitly approved.

Do not run the PR14 test before implementation because it does not exist yet.

Do not create the PR14 branch until the base sync gate and baseline verification pass.

---

# Target PR

Implement:

```
PR14 — Controlled ATS Scout adapters
```

Branch:

```
codex/pr14-controlled-ats-scout-adapters
```

Base:

```
application-os-foundation
```

PR title:

```
PR14: Controlled ATS Scout adapters
```

Open the PR as draft.

Do not merge.  
Do not undraft.  
Do not start PR15.  
Do not add MCP.  
Do not add Scout runtime.  
Do not add browser automation.  
Do not add network fetch.  
Do not add persistence.  
Do not add job import wiring.

---

# Context

Twoweeks is evolving toward an Application OS.

The current Distribution chain is:

```
ApplicationPackageV1
→ Internal tool contracts
→ Controlled ATS Scout adapters
→ local MCP later
```

PR14 is the first Scout-related PR, but it must remain controlled and deterministic.

PR14 should add **pure TypeScript ATS adapter primitives** for supported ATS sources.

This PR is not a live crawler.

This PR is not a web scraper.

This PR is not a job source product.

This PR is not LinkedIn / Upwork / Indeed scraping.

This PR is not network fetch.

This PR is not job persistence.

This PR is not application submission.

---

# Goal

Add a pure TypeScript `controlled-ats-scout` module that normalizes **caller-supplied ATS job payloads** into deterministic `ControlledAtsJobLeadV1` records.

Core pipeline:

```
caller-supplied ATS payload
+ supported ATS vendor descriptor
→ deterministic normalized job leads
```

Supported vendors for PR14:

```
greenhouse
lever
ashby
```

Unsupported / forbidden vendors:

```
linkedin
upwork
indeed
generic_web
unknown_scraper
```

The module should define:

- supported ATS vendor types
- source descriptor types
- raw payload envelope types
- normalized job lead type
- adapter registry
- vendor-specific normalizers for safe fixture/payload shapes
- URL/vendor validation helpers
- dedupe/canonicalization helpers
- stable job lead hash helpers
- focused Vitest tests
- one decision doc

---

# Product boundary

Controlled ATS Scout adapters mean:

```
deterministic pure adapters for known ATS payloads supplied by the caller
```

They do not mean:

```
crawler
scraper
browser automation
network fetch
public Scout product
job import into database
job application submission
LinkedIn scraping
Indeed scraping
Upwork scraping
MCP
external API service
```

PR14 should be deletion-safe.

Rollback should be deleting the new module and decision doc.

---

# Inspect first

Read these before editing:

```
AGENTS.md
my-app/package.json

docs/decisions/2026-06-08-application-os-master-plan.md
docs/decisions/2026-06-10-internal-tool-contracts.md

my-app/src/modules/application-harness/fingerprints.ts

my-app/src/modules/internal-tool-contracts/schema.ts
my-app/src/modules/internal-tool-contracts/contracts.ts
my-app/src/modules/internal-tool-contracts/contractRules.ts
my-app/src/modules/internal-tool-contracts/__tests__/internalToolContracts.test.ts

my-app/src/modules/application-package/schema.ts
my-app/src/modules/application-package/buildApplicationPackage.ts
my-app/src/modules/application-package/packageRules.ts
my-app/src/modules/application-package/__tests__/applicationPackage.test.ts
```

Also inspect nearest existing pure TypeScript module tests before adding tests.

Do not inspect broad unrelated UI/product surfaces unless needed to confirm a stop condition.

Do not inspect or edit:

```
premiumCoverLetter.ts
Proposal Forge
CV Forge
export/PDF/DOCX
MCP
Scout runtime
routes
Convex functions
jobs persistence
network clients
```

After inspection, summarize briefly:

- whether PR13 is present on base
- current internal tool contracts shape
- current stable hash pattern
- current test style
- whether any existing Scout-related files exist
- blockers before implementation, if any

If existing Scout files exist, inspect only enough to avoid conflicting names. Do not modify them unless they are clearly existing empty placeholders for this exact PR.

---

# Expected changed files

Limit changes to:

```
my-app/src/modules/controlled-ats-scout/schema.ts
my-app/src/modules/controlled-ats-scout/adapters.ts
my-app/src/modules/controlled-ats-scout/scoutRules.ts
my-app/src/modules/controlled-ats-scout/__tests__/controlledAtsScout.test.ts
docs/decisions/2026-06-10-controlled-ats-scout-adapters.md
```

Use different paths only if repo conventions clearly require it. Explain why in the final report.

Do not create or modify:

- UI files
- route files
- Convex files
- package dependency files
- export files
- generation files
- prompt files
- `premiumCoverLetter.ts`
- Proposal Forge
- CV Forge
- JobsWorkspace
- MCP files
- Scout runtime files
- external connector files
- network client files

---

# Allowed scope

Allowed:

- pure TypeScript schema/types for controlled ATS Scout adapters
- supported vendor descriptors
- deterministic normalizers for caller-supplied payloads
- deterministic canonical URL helpers
- deterministic job lead hash helpers
- dedupe helpers
- adapter registry
- focused Vitest tests
- one decision doc

---

# Forbidden scope

Do not touch:

```
main
Convex schema
Convex functions
persistence
public routes
UI
Review UI
generation
prompt files
premiumCoverLetter.ts
parser/import
PDF/DOCX handling
export
remote fetch
network clients
browser automation
LinkedIn scraping
Upwork scraping
Indeed scraping
generic crawling
CV Forge
Proposal Forge
JobsWorkspace
active CV snapshots
userProfiles behavior
jobs behavior
ApplicationContext builder behavior
CandidateEvidenceProfile builder
EvidenceGraph behavior
ResumeVariantPlan behavior
ReviewCockpit behavior
ResumeVariantArtifact behavior
CoverLetterArtifact behavior
ApplicationPackage behavior
InternalToolContracts behavior
PR15 MCP work
MCP
Scout runtime
ChatGPT App work
package dependencies
unrelated docs
broad refactors
formatting-only rewrites
```

---

# Required V1 types

Create Scout-adapter-level V1 types only.

## ControlledAtsVendorV1

Values:

```
greenhouse
lever
ashby
```

Do not include:

```
linkedin
upwork
indeed
generic_web
unknown
```

## ControlledAtsForbiddenVendorV1

Values:

```
linkedin
upwork
indeed
generic_web
unknown_scraper
```

This type is for rejection/guard tests only.

Do not register these as supported adapters.

## ControlledAtsSourceKindV1

Values:

```
public_job_board_payload
public_job_detail_payload
manual_fixture
```

Rules:

- means caller supplied payload data
- does not mean PR14 fetched data
- does not imply network access

Do not add:

```
browser_scrape
crawler
api_fetch
remote_fetch
```

## ControlledAtsJobStatusV1

Values:

```
open
closed
unknown
```

## ControlledAtsWorkplaceTypeV1

Values:

```
remote
hybrid
onsite
unknown
```

## ControlledAtsCompensationV1

Fields:

```
currency?: string;
minAmount?: number;
maxAmount?: number;
interval?: "hour" | "day" | "week" | "month" | "year" | "unknown";
rawText?: string;
version: 1;
```

Rules:

- do not invent compensation
- preserve rawText if supplied
- numeric min/max must be finite if present
- currency must be caller-supplied or absent

## ControlledAtsJobLeadV1

Fields:

```
id: string;
vendor: ControlledAtsVendorV1;
sourceKind: ControlledAtsSourceKindV1;
sourceUrl?: string;
canonicalUrl?: string;
externalJobId?: string;
companyName?: string;
title: string;
department?: string;
team?: string;
location?: string;
workplaceType: ControlledAtsWorkplaceTypeV1;
status: ControlledAtsJobStatusV1;
descriptionText?: string;
descriptionHash?: string;
applyUrl?: string;
postedAt?: string;
updatedAt?: string;
compensation?: ControlledAtsCompensationV1;
rawPayloadHash: string;
leadHash: string;
createdAt: number;
updatedAt: number;
version: 1;
```

Rules:

- `title` is required.
- `vendor` is required.
- `rawPayloadHash` is required.
- `leadHash` is deterministic and must exclude `createdAt` / `updatedAt`.
- `id` should be `controlled-ats-job-lead:<leadHash>`.
- `descriptionText` may be included only if supplied in the payload.
- Do not summarize or rewrite `descriptionText`.
- Do not extract candidate claims from job text.
- Do not create ApplicationContext.
- Do not persist to jobs table.
- Do not auto-apply.

## ControlledAtsPayloadEnvelopeV1

Fields:

```
vendor: ControlledAtsVendorV1;
sourceKind: ControlledAtsSourceKindV1;
sourceUrl?: string;
payload: unknown;
createdAt: number;
updatedAt: number;
version: 1;
```

Rules:

- `payload` is caller-supplied.
- PR14 must not fetch it.
- `createdAt` / `updatedAt` are metadata only.
- timestamps must not affect `rawPayloadHash` or `leadHash`.

## ControlledAtsAdapterV1

Fields:

```
vendor: ControlledAtsVendorV1;
title: string;
description: string;
supportedSourceKinds: readonly ControlledAtsSourceKindV1[];
version: 1;
```

Rules:

- adapter is a descriptor + pure normalizer, not runtime fetch.
- description must not claim network access.
- description must not claim scraping.
- description must not claim auto-apply.

## ControlledAtsAdapterRegistryV1

Fields:

```
adapters: readonly ControlledAtsAdapterV1[];
vendors: readonly ControlledAtsVendorV1[];
version: 1;
```

Rules:

- sorted by vendor
- no duplicate vendors
- only supported vendors

## ControlledAtsNormalizationResultV1

Fields:

```
vendor: ControlledAtsVendorV1;
sourceKind: ControlledAtsSourceKindV1;
leads: readonly ControlledAtsJobLeadV1[];
rejected: readonly ControlledAtsRejectedRecordV1[];
warnings: readonly string[];
version: 1;
```

## ControlledAtsRejectedRecordV1

Fields:

```
reason: string;
vendor?: string;
sourceUrl?: string;
rawPayloadHash?: string;
version: 1;
```

Rules:

- rejection reasons are deterministic short strings
- no raw full payload text in rejection reason
- unsupported vendor must be rejected, not coerced

## ControlledAtsScoutContentV1

Fields:

```
kind: "controlled_ats_scout_adapters";
registry: ControlledAtsAdapterRegistryV1;
version: 1;
```

This is content shape only.

Do not persist it in PR14.

---

# Required helpers

Create pure TypeScript helpers:

```
buildControlledAtsAdapterRegistry()
buildControlledAtsAdapterRegistryHash(registry)
buildControlledAtsScoutContent(registry)

normalizeControlledAtsPayload(envelope)
normalizeGreenhousePayload(envelope)
normalizeLeverPayload(envelope)
normalizeAshbyPayload(envelope)

buildControlledAtsRawPayloadHash(payload)
buildControlledAtsJobLeadHash(input)
buildControlledAtsJobLead(input)
dedupeControlledAtsJobLeads(leads)

canonicalizeControlledAtsUrl(vendor, url)
inferControlledAtsVendorFromUrl(url)

assertControlledAtsPayloadEnvelope(envelope)
assertControlledAtsJobLead(lead)
assertControlledAtsAdapterRegistry(registry)
assertControlledAtsDoesNotUseForbiddenVendor(vendorOrUrl)
assertControlledAtsScoutDoesNotContainGeneratedText(value)
```

Use the existing stable SHA/hash style from:

```
my-app/src/modules/application-harness/fingerprints.ts
```

Do not invent weak hashes.

Do not mutate inputs.

Do not add runtime fetch functions.

Do not add names that imply runtime fetch/crawl/scrape.

Forbidden helper names:

```
fetchJobs
crawlJobs
scrapeJobs
fetchGreenhouse
fetchLever
fetchAshby
runScout
executeScout
startScout
applyToJob
submitApplication
```

---

# Vendor payload handling

PR14 must support simple fixture-shaped payloads, not every real ATS edge case.

## Greenhouse accepted payload shapes

Support caller-supplied payloads shaped like either:

```
{
  jobs: Array<{
    id?: string | number;
    title: string;
    absolute_url?: string;
    location?: { name?: string } | string;
    departments?: Array<{ name?: string }>;
    content?: string;
    updated_at?: string;
  }>;
}
```

or a single job object with the same fields.

## Lever accepted payload shapes

Support caller-supplied payloads shaped like either:

```
{
  postings: Array<{
    id?: string;
    text: string;
    hostedUrl?: string;
    applyUrl?: string;
    categories?: {
      location?: string;
      team?: string;
      department?: string;
      commitment?: string;
    };
    descriptionPlain?: string;
    createdAt?: number;
  }>;
}
```

or a single posting object with the same fields.

## Ashby accepted payload shapes

Support caller-supplied payloads shaped like either:

```
{
  jobs: Array<{
    id?: string;
    title: string;
    jobUrl?: string;
    applyUrl?: string;
    location?: string;
    department?: string;
    team?: string;
    descriptionPlain?: string;
    employmentType?: string;
    publishedAt?: string;
  }>;
}
```

or a single job object with the same fields.

Rules:

- If payload shape is unsupported, return rejected record with deterministic reason.
- If job title is missing or blank, reject that record.
- If URL is present, canonicalize it deterministically.
- If URL is forbidden vendor domain, reject it.
- Do not throw for a single malformed record if other records are valid.
- Throw only for invalid envelope/vendor/sourceKind/timestamps.

---

# Hash semantics

## `buildControlledAtsRawPayloadHash(payload)`

Must hash caller-supplied payload deterministically.

Must not include timestamps unless timestamps are part of the payload itself.

## `buildControlledAtsJobLeadHash(input)`

Must exclude:

```
createdAt
updatedAt
```

Should include stable lead inputs:

```
vendor
sourceKind
canonicalUrl
externalJobId
companyName
title
department
team
location
workplaceType
status
descriptionHash
applyUrl
postedAt
compensation
rawPayloadHash
```

Rationale:

- same logical job lead with different build timestamps should produce same ID
- changed title/url/external ID/description should change lead hash
- no live clock should affect identity

---

# URL / vendor safety rules

Allowed vendor URL host patterns:

```
greenhouse.io
boards.greenhouse.io
job-boards.greenhouse.io
lever.co
jobs.lever.co
ashbyhq.com
jobs.ashbyhq.com
```

Forbidden URL host patterns:

```
linkedin.com
www.linkedin.com
upwork.com
www.upwork.com
indeed.com
www.indeed.com
```

Rules:

- `inferControlledAtsVendorFromUrl` may return supported vendor only for allowlisted hosts.
- forbidden hosts must be rejected deterministically.
- unknown hosts return undefined or throw consistently; choose one behavior and test it.
- do not attempt to fetch the URL.
- do not follow redirects.
- do not parse remote pages.

---

# Dedupe rules

Deduplicate leads by stable key preference:

```
vendor + externalJobId
vendor + canonicalUrl
vendor + leadHash
```

Rules:

- deterministic output order
- sorted by vendor, title, canonicalUrl/externalJobId/id
- do not drop distinct jobs with same title but different canonical URL/external ID
- do not mutate input leads

---

# Required behavior

The module must be deterministic.

It must:

- build same registry/hash for same adapters
- reject unsupported vendors
- reject forbidden vendor URLs
- normalize Greenhouse fixture payloads
- normalize Lever fixture payloads
- normalize Ashby fixture payloads
- return rejected records for malformed individual records
- preserve supplied descriptions without rewriting
- compute deterministic raw payload hash
- compute deterministic lead hash
- exclude createdAt/updatedAt from lead identity
- canonicalize supported ATS URLs
- dedupe deterministic leads
- sort deterministic outputs
- never fetch network
- never crawl
- never scrape
- never touch jobs table
- never create ApplicationContext
- never call internal tool runtime
- never call MCP/Scout runtime
- never auto-apply
- never generate text

---

# Generated text / prose guard

Implement:

```
assertControlledAtsScoutDoesNotContainGeneratedText(value)
```

It should inspect adapter titles/descriptions, warnings, rejection reasons, and internal labels.

It must not reject supplied job descriptions just because they contain prose, because job descriptions are caller-supplied payload content.

It must reject:

```
cover-letter prose
resume bullet prose
marketing claims invented by adapter metadata
auto-apply language
scraping/crawling/runtime claims
```

---

# Required tests

Create:

```
my-app/src/modules/controlled-ats-scout/__tests__/controlledAtsScout.test.ts
```

Tests must be focused but strong.

Required tests:

1. builds deterministic adapter registry
2. registry hash is stable
3. scout content helper returns `kind: "controlled_ats_scout_adapters"`
4. registry includes only greenhouse, lever, ashby
5. registry rejects duplicate vendors
6. unsupported vendor is rejected
7. forbidden vendors are not registered
8. forbidden LinkedIn URL is rejected
9. forbidden Upwork URL is rejected
10. forbidden Indeed URL is rejected
11. supported Greenhouse URL infers greenhouse
12. supported Lever URL infers lever
13. supported Ashby URL infers ashby
14. unknown URL returns deterministic unsupported result
15. Greenhouse fixture normalizes to job lead
16. Lever fixture normalizes to job lead
17. Ashby fixture normalizes to job lead
18. missing title record is rejected without rejecting valid records
19. unsupported payload shape returns rejected result
20. raw payload hash is deterministic
21. lead hash is deterministic
22. lead hash ignores createdAt / updatedAt
23. changed title changes lead hash
24. changed canonical URL changes lead hash
25. description hash changes when supplied description changes
26. supplied description text is preserved exactly
27. dedupe removes duplicate externalJobId deterministically
28. dedupe removes duplicate canonicalUrl deterministically
29. dedupe does not merge same-title distinct URLs
30. output order is deterministic
31. helpers do not mutate inputs
32. no imports/calls from:
    - Convex
    - UI/routes
    - generation
    - `premiumCoverLetter.ts`
    - Proposal Forge
    - CV Forge
    - export/PDF/DOCX
    - MCP
    - Scout runtime
    - network clients
33. no helper names include fetch/crawl/scrape/run/execute/apply/submit
34. generated-text guard rejects runtime/scraping/auto-apply language in adapter metadata
35. generated-text guard does not reject caller-supplied job description prose

Do not add brittle tests requiring UI, Convex, network, export, generated documents, MCP, or Scout runtime.

---

# Decision doc

Create:

```
docs/decisions/2026-06-10-controlled-ats-scout-adapters.md
```

Include:

- purpose
- why PR14 is controlled ATS adapters only
- why runtime Scout is deferred
- why network fetch is deferred
- why LinkedIn/Upwork/Indeed scraping is forbidden
- supported vendors
- unsupported/forbidden vendors
- payload-boundary rules
- hash semantics
- dedupe rules
- validation rules
- forbidden scope
- tests
- rollback notes
- deferred work

Mention explicitly:

- PR14 does not fetch jobs
- PR14 does not crawl
- PR14 does not scrape
- PR14 does not persist job leads
- PR14 does not create ApplicationContext
- PR14 does not add MCP
- PR14 does not add Scout runtime
- PR14 does not expose public APIs
- PR14 does not add export/send/apply/track
- future runtime adapters should consume these pure adapters in later PRs

---

# Verification after implementation

From `my-app`, run:

```
rtk npx vitest --run src/modules/controlled-ats-scout/__tests__/controlledAtsScout.test.ts
rtk npx vitest --run src/modules/internal-tool-contracts/__tests__/internalToolContracts.test.ts
rtk npx vitest --run src/modules/application-package/__tests__/applicationPackage.test.ts
rtk npx vitest --run src/modules/cover-letter-artifact/__tests__/coverLetterArtifact.test.ts
rtk npx vitest --run src/modules/resume-variant-artifact/__tests__/resumeVariantArtifact.test.ts
rtk npx vitest --run src/modules/review-cockpit/__tests__/reviewCockpit.test.ts
rtk npx vitest --run src/modules/resume-variant-plan/__tests__/resumeVariantPlan.test.ts
rtk npx vitest --run src/modules/evidence-graph/__tests__/evidenceGraph.test.ts
rtk npx vitest --run src/modules/candidate-evidence/__tests__/candidateEvidence.test.ts
rtk npx vitest --run src/modules/career-knowledge/__tests__/careerKnowledge.test.ts
rtk npx vitest --run convex/__tests__/candidateEvidence.test.ts
rtk npx vitest --run convex/__tests__/applicationHarness.test.ts
rtk npx vitest --run convex/lib/tests/applicationContextBuilder.test.ts
rtk npm test -- application-harness --run
rtk npx tsc --noEmit
```

Then from repo root:

```
rtk git diff --check
rtk git status --short
rtk git diff --name-only application-os-foundation...HEAD
```

Expected changed files only:

```
my-app/src/modules/controlled-ats-scout/schema.ts
my-app/src/modules/controlled-ats-scout/adapters.ts
my-app/src/modules/controlled-ats-scout/scoutRules.ts
my-app/src/modules/controlled-ats-scout/__tests__/controlledAtsScout.test.ts
docs/decisions/2026-06-10-controlled-ats-scout-adapters.md
```

If tests fail, debug and fix within PR14 scope.

Do not stop after the first failure if the issue is clearly within PR14 scope.

Do not broaden scope to fix unrelated failures.

---

# PR creation

Push branch:

```
rtk git push -u origin codex/pr14-controlled-ats-scout-adapters
```

Open draft PR:

```
gh pr create \
  --base application-os-foundation \
  --head codex/pr14-controlled-ats-scout-adapters \
  --title "PR14: Controlled ATS Scout adapters" \
  --draft \
  --body-file /tmp/pr14-controlled-ats-scout-adapters-body.md
```

PR body must include:

````
## Summary

Adds PR14 as a narrow Distribution-layer boundary: a pure TypeScript `controlled-ats-scout` module that normalizes caller-supplied Greenhouse, Lever, and Ashby ATS payloads into deterministic job leads.

This PR adds:
- `ControlledAtsScout` V1 schema/types
- supported ATS adapter descriptors
- deterministic payload normalizers
- URL/vendor safety guards
- lead hash / raw payload hash helpers
- dedupe helpers
- focused Vitest coverage
- decision doc + rollback notes

## Scope

Changed files are limited to:
- `my-app/src/modules/controlled-ats-scout/schema.ts`
- `my-app/src/modules/controlled-ats-scout/adapters.ts`
- `my-app/src/modules/controlled-ats-scout/scoutRules.ts`
- `my-app/src/modules/controlled-ats-scout/__tests__/controlledAtsScout.test.ts`
- `docs/decisions/2026-06-10-controlled-ats-scout-adapters.md`

## Boundary confirmations

This PR does not add or change:
- UI/routes
- Convex schema/functions/persistence
- generation/prompts
- parser/import
- export/PDF/DOCX
- `premiumCoverLetter.ts`
- Proposal Forge / CV Forge
- JobsWorkspace
- active CV snapshots / userProfiles / jobs behavior
- EvidenceGraph behavior
- ResumeVariantPlan behavior
- ReviewCockpit behavior
- ResumeVariantArtifact behavior
- CoverLetterArtifact behavior
- ApplicationPackage behavior
- InternalToolContracts behavior
- MCP / Scout runtime / ChatGPT App work

No runtime fetching, crawling, scraping, LLM calls, embeddings, network calls, exported files, submission state, or send/apply/track behavior are introduced.

## Adapter semantics

- Adapters normalize caller-supplied ATS payloads.
- Adapters do not fetch jobs.
- Adapters do not crawl.
- Adapters do not scrape.
- Adapters do not persist leads.
- Supported vendors: Greenhouse, Lever, Ashby.
- Forbidden vendors: LinkedIn, Upwork, Indeed.

## Verification

Paste exact command output here.

## Rollback

Rollback is deletion-only:

```txt
delete my-app/src/modules/controlled-ats-scout/
delete docs/decisions/2026-06-10-controlled-ats-scout-adapters.md
rerun tests/typecheck
````

No database, migration, UI, route, generation, export, parser, CV Forge, Proposal Forge, jobs table, MCP, Scout runtime, or network rollback should be required.

````

---

# CI / Greptile loop

After opening the draft PR:

- wait for CI
- check Greptile
- if Greptile flags P0/P1/P2 correctness issues, fix them on the same branch
- do not create a new branch
- do not open a new PR
- do not merge
- do not undraft
- keep changes inside PR14 scope

Continue until:

- PR14 tests pass
- listed regression tests pass
- typecheck passes
- diff-check passes
- CI is green
- Greptile is green

For this task, “Greptile green” means:

```txt
no P0/P1 blockers
no unresolved correctness P2s
safe-to-merge / high-confidence summary if Greptile provides one
only minor style/efficiency nits may remain if explicitly non-correctness
````

---

# Hard completion rule

Do not mark this task DONE unless all of the following are true:

- PR14 branch created from clean `application-os-foundation` after PR13
- baseline verification before coding was green
- new `controlled-ats-scout` module exists
- no runtime fetching/crawling/scraping exists
- no LinkedIn/Upwork/Indeed adapter is registered
- no generation/prompt/LLM behavior changed
- no `premiumCoverLetter.ts` change
- no UI/routes/Convex/export/persistence changes
- no jobs table behavior changed
- no send/apply/track/submission behavior added
- no MCP or Scout runtime work added
- no PR15 work started
- registry/hash/dedupe/normalization tests pass
- tests and typecheck pass
- CI is green
- Greptile is green
- changed files stay inside expected PR14 scope

Use:

```
DONE_DEFINITION: DONE
```

only when all gates are green.

Use:

```
DONE_DEFINITION: PARTIAL
```

only if implementation is complete but CI or Greptile is still pending and cannot yet be checked.

Use:

```
DONE_DEFINITION: BLOCKED
```

only if base is unsynced, PR13 is missing, repo commands fail before edits, required context/runtime/files are unavailable, or a required fix would violate forbidden scope.

Do not merge.  
Do not undraft.  
Do not start PR15.  
Do not call the task complete until CI and Greptile are both green.

---

# Final report required

When finished, report:

```
branch name
PR number and URL
head SHA
files changed
implementation summary
types added
helpers added
vendors supported
tests added
exact test output
TypeScript result
diff-check result
CI result
Greptile result
confirmation no forbidden files touched
confirmation no premiumCoverLetter.ts edit
confirmation no generation/prompt/LLM behavior changed
confirmation no UI/routes/Convex/export/persistence changes
confirmation no jobs table behavior changed
confirmation no runtime fetch/crawl/scrape added
confirmation no LinkedIn/Upwork/Indeed adapter registered
confirmation no MCP or Scout runtime work added
confirmation no PR15 work started
confirmation registry is deterministic and validated
confirmation payload normalizers are fixture/caller-supplied only
remaining risks
rollback notes
```

---

# Rollback notes

Rollback should be simple:

```
delete my-app/src/modules/controlled-ats-scout/
delete docs/decisions/2026-06-10-controlled-ats-scout-adapters.md
rerun tests/typecheck
```

No database rollback, migration rollback, UI rollback, route rollback, export rollback, generation rollback, parser rollback, CV Forge rollback, Proposal Forge rollback, jobs table rollback, MCP rollback, Scout runtime rollback, or network rollback should be required.

---

# Stop conditions

Stop immediately and report if implementation requires:

```
editing premiumCoverLetter.ts
changing Proposal Forge
changing CV Forge
changing generation prompts
adding Convex schema/functions
adding persistence
adding UI/routes
adding export/PDF/DOCX
mutating jobs table behavior
mutating candidate facts
mutating EvidenceGraph
mutating ResumeVariantPlan
mutating ReviewCockpit
mutating ResumeVariantArtifact
mutating CoverLetterArtifact
mutating ApplicationPackage
mutating InternalToolContracts
mutating canonical CVs
wiring active routes
replacing existing pages
adding parser/import pipeline
adding package dependencies
adding send/apply/track behavior
adding approval/rejection workflow
marking anything approved/final/exportable/sent/submitted/applied
generating resume bullets
generating new cover-letter text
rewriting supplied cover-letter text
using an LLM
using embeddings
using network/web calls
adding MCP
adding Scout runtime
adding ChatGPT App work
adding LinkedIn scraping
adding Upwork scraping
adding Indeed scraping
adding generic crawling
starting PR15
```

---

# Next PR after this

Do not start it now.

Roadmap next PR after PR14 should remain:

```
PR15 — Local MCP beta
```

MCP, remote tools, export, send/apply/track, and ChatGPT App work remain deferred.


D’après le plan maître que tu as partagé et l’état actuel :

### ✅ Déjà terminés

|PR|Statut|
|---|---|
|PR1|Merged|
|PR2|Merged|
|PR3|Merged|
|PR109|Merged|
|PR4|Merged|
|PR5|Merged|
|PR6|Merged|
|PR6.1|Merged|
|PR7|Merged|
|PR8|Merged|
|PR9|Merged|
|PR10|Merged|
|PR11|Merged|
|PR12|Merged|
|PR13|Merged|

---

# Reste à faire

## PR14 — Controlled ATS Scout Adapters

### Phase

Distribution

### But

Créer des adaptateurs déterministes pour récupérer des offres depuis des ATS supportés.

### Autorisé

- Greenhouse
    
- Lever
    
- Ashby
    
- Types
    
- Mapping
    
- Déduplication
    
- Validation
    

### Interdit

- Scraping LinkedIn
    
- Scraping Indeed
    
- Scraping Upwork
    
- Automatisation de candidature
    
- Browser automation
    
- MCP
    
- UI
    

### Livrable

Une couche pure TS :

```txt
job-scout/
 ├─ schema.ts
 ├─ adapters/
 │   ├─ greenhouse.ts
 │   ├─ lever.ts
 │   └─ ashby.ts
 ├─ normalize.ts
 ├─ dedupe.ts
 └─ tests/
```

---

## PR15 — Local MCP Beta

### Phase

Distribution

### But

Créer un wrapper local autour des Internal Tool Contracts (PR13).

### Autorisé

- Registry local
    
- Permission checks
    
- Allowlist
    
- Approval gates
    

### Interdit

- Réseau public
    
- Serveur externe
    
- ChatGPT App
    
- OAuth
    

### Livrable

```txt
local-mcp/
 ├─ schema.ts
 ├─ registry.ts
 ├─ permissions.ts
 ├─ executeTool.ts
 └─ tests/
```

---

## PR16 — Remote MCP / ChatGPT App Exploration

### Phase

Distribution

### But

Documentation uniquement.

### Autorisé

- Audit
    
- Gap analysis
    
- Spec
    
- Architecture doc
    

### Interdit

- Code production
    
- Remote MCP
    
- Public endpoints
    
- Deployment
    

### Livrable

```txt
docs/
 └─ mcp-readiness.md
```

---

# Après PR16

Le plan original est terminé.

À ce moment-là, tu auras :

```txt
Application OS Spine      ✅
Proof Layer               ✅
Product Value Layer       ✅
Distribution Layer        ✅
```

et le système complet sera composé de :

```txt
Candidate Sources
    ↓
Candidate Facts
    ↓
Career Knowledge
    ↓
Evidence Graph
    ↓
Resume Variant Plan
    ↓
Review Cockpit
    ↓
Resume Artifact
    ↓
Cover Letter Artifact
    ↓
Application Package
    ↓
Internal Tool Contracts
    ↓
ATS Scout
    ↓
Local MCP
```

---

### Ordre recommandé

Ne pas changer l'ordre :

```txt
PR14 → ATS Scout
PR15 → Local MCP
PR16 → MCP Readiness Spec
```

PR14 est le dernier vrai gros morceau de code.

PR15 est plus petit.

PR16 est essentiellement un document d'architecture.

Donc il reste **3 PRs** pour clôturer complètement le plan maître original.

# PR15 — Local MCP Beta

## Contexte

Les PR précédentes ont déjà livré :

- Application Harness
- Candidate Evidence
- Career Knowledge
- EvidenceGraph
- ResumeVariantPlan
- ReviewCockpit
- Resume Variant Artifact
- Cover Letter Artifact
- ApplicationPackageV1
- Internal Tool Contracts
- ATS Scout adapters (PR14)

PR15 ne doit pas créer de nouvelle logique métier.

Il doit seulement exposer les outils internes existants derrière un adaptateur local contrôlé.

---

# Objectif

Créer un wrapper MCP local permettant d'exécuter uniquement des outils approuvés via une couche d'autorisation stricte.

Le MCP :

- ne doit pas être public
- ne doit pas être réseau
- ne doit pas être déployable
- ne doit pas être connecté à ChatGPT
- ne doit pas exécuter d'actions réelles

Il doit uniquement démontrer que les outils internes peuvent être exposés derrière un contrat MCP local sécurisé.

---

# Branche

```
codex/pr15-local-mcp-beta
```

Base :

```
application-os-foundation
```

---

# Lire avant modification

```
AGENTS.mddocs/decisions/2026-06-08-application-os-master-plan.mddocs/decisions/2026-06-09-application-package-v1.mddocs/decisions/2026-06-09-internal-tool-contracts.mdmy-app/src/modules/internal-tool-contracts/*
```

Lire aussi tous les types InternalTool déjà créés dans PR13.

---

# Vérification préalable obligatoire

Avant toute modification :

```
rtk git fetch originrtk git checkout application-os-foundationrtk git pull --ff-only origin application-os-foundationrtk git status --shortrtk git log -n 1 --oneline
```

Confirmer que PR14 est mergeée.

Si PR14 n'est pas présente dans la base :

```
STOPPR15 ne peut pas commencer.
```

---

# Scope exact

Créer uniquement :

```
my-app/src/modules/local-mcp/
```

et :

```
docs/decisions/2026-06-09-local-mcp-beta.md
```

---

# Fichiers attendus

```
my-app/src/modules/local-mcp/schema.tsmy-app/src/modules/local-mcp/toolRegistry.tsmy-app/src/modules/local-mcp/authorization.tsmy-app/src/modules/local-mcp/localMcpServer.tsmy-app/src/modules/local-mcp/__tests__/localMcp.test.tsdocs/decisions/2026-06-09-local-mcp-beta.md
```

---

# Types requis

## LocalMcpToolDefinitionV1

```
idnamedescriptionversionrequiresApproval
```

---

## LocalMcpRequestV1

```
toolIduserIdargumentsrequestedAt
```

---

## LocalMcpResponseV1

```
successtoolIdresultexecutedAt
```

---

## LocalMcpAuthorizationResultV1

```
allowedreason?
```

---

# Registry

Créer un registry statique.

Exemple :

```
review_cockpit_readresume_variant_plan_readapplication_package_readevidence_graph_read
```

Pas plus.

---

# Important

Registry READ ONLY.

Interdire :

```
deletewriteupdatepatchexecutesubmitapplysendpublish
```

---

# Authorization Layer

Créer :

```
authorizeToolCall(...)
```

Règles :

- outil inconnu => refus
- outil non allowlisté => refus
- approval requis sans approval => refus

Retour explicite :

```
allowed: falsereason: "..."
```

---

# Local MCP Server

Créer un exécuteur local.

Exemple :

```
executeLocalTool(...)
```

Mais uniquement pour démontrer :

```
validationauthorizationdispatchresponse
```

Pas d'action réelle.

---

# Interdictions absolues

Ne pas ajouter :

```
MCP network transportHTTPWebSocketSSEOAuthAuthenticationRemote executionChatGPT integrationOpenAI integrationClaude integrationRemote tool registryTool discovery serviceExternal API callsBackground jobsPersistenceConvex schemaConvex functionsUIRoutesPagesProposal ForgeCV ForgeScout behaviorApplicationPackage behaviorGenerationExportImportParserPDFDOCXPackage dependencies
```

---

# Tests requis

Créer des tests couvrant :

### Registry

```
tool enregistrétool inconnu rejeté
```

### Authorization

```
allowlisted tool acceptétool inconnu rejetéapproval requis rejeté sans approval
```

### Dispatcher

```
dispatch vers bon handlererreur handler propagéeréponse stable
```

### Sécurité

```
aucun write tool enregistréaucun send/apply tool enregistréaucun network tool enregistré
```

### Immutabilité

```
inputs non mutés
```

---

# Commandes obligatoires

Depuis :

```
cd my-app
```

Exécuter :

```
rtk npx vitest --run src/modules/local-mcp/__tests__/localMcp.test.tsrtk npx vitest --run src/modules/internal-tool-contracts/__tests__/*.test.tsrtk npx vitest --run src/modules/application-package/__tests__/*.test.tsrtk npx vitest --run src/modules/review-cockpit/__tests__/reviewCockpit.test.tsrtk npx vitest --run src/modules/evidence-graph/__tests__/evidenceGraph.test.tsrtk npx tsc --noEmitrtk git diff --checkrtk git status --shortrtk git diff --name-only application-os-foundation...HEAD
```

---

# Boucle qualité obligatoire

Ne pas s'arrêter après le code.

Faire :

```
Coder↓Tests↓Typecheck↓Corriger↓Retester↓Créer PR↓Attendre CI↓Lire Greptile↓Corriger si nécessaire↓Retester↓Repousser↓Réattendre CI↓Relire Greptile↓Répéter
```

Arrêt uniquement lorsque :

```
CI = GREENGreptile = GREEN ou Safe to mergeP0 = 0P1 = 0
```

---

# Critère DONE

PR15 est DONE uniquement si :

```
Local MCP beta existeRead-onlyAllowlist stricteApproval gatesAucun réseauAucune persistanceAucun changement produitCI verteTypeScript vertGreptile vert
```

---

# Rollback

Suppression simple :

```
delete my-app/src/modules/local-mcp/delete docs/decisions/2026-06-09-local-mcp-beta.md
```

Aucun rollback :

```
DBConvexUIRoutesExportsImportsScoutGenerationApplicationPackage
```