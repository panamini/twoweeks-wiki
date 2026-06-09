# Twoweeks Application OS — Execution Starter Pack

**Status:** starter execution pack  
**Purpose:** convert the accepted Twoweeks architecture direction into a safe ChatGPT/GPT Pro + Codex + skills workflow.  
**Audience:** you, GPT Pro, Codex, future Codex skills, and PR reviewers.  
**Core rule:** this document is a planning/control artifact. It is **not** a single Codex implementation task.

---

## Table of contents

1. [How to use this file](#1-how-to-use-this-file)
2. [Blunt execution recommendation](#2-blunt-execution-recommendation)
3. [Master Architecture Decision Record draft](#3-master-architecture-decision-record-draft)
4. [Execution model: ChatGPT + Codex + skills](#4-execution-model-chatgpt--codex--skills)
5. [Compact PR roadmap](#5-compact-pr-roadmap)
6. [Full PR spec — PR 1](#6-full-pr-spec--pr-1)
7. [Full PR spec — PR 2](#7-full-pr-spec--pr-2)
8. [Full PR spec — PR 3](#8-full-pr-spec--pr-3)
9. [Codex-ready prompt — PR 1 only](#9-codex-ready-prompt--pr-1-only)
10. [Reusable GPT Pro next-PR prompt template](#10-reusable-gpt-pro-next-pr-prompt-template)
11. [When to ask GPT Pro again](#11-when-to-ask-gpt-pro-again)
12. [Hard stop conditions](#12-hard-stop-conditions)
13. [Draft Codex skill / SKILL.md](#13-draft-codex-skill--skillmd)
14. [PR context-pack template](#14-pr-context-pack-template)
15. [PR 1 context pack](#15-pr-1-context-pack)
16. [Start checklist](#16-start-checklist)

---

# 1. How to use this file

Use this file as the starter execution system for the Twoweeks Application OS transition.

## Do this first

1. Save the ADR section into:

   ```txt
   docs/decisions/2026-06-08-application-os-master-plan.md
   ```

2. Give Codex **only** the PR 1 prompt in section 9, plus the PR 1 context pack in section 15 if useful.

3. After Codex finishes PR 1, paste the Codex report, changed files, diff, and test output back into GPT Pro using the template in section 10.

4. GPT Pro should then either:
   - create a fix-forward prompt if PR 1 has issues, or
   - create the next narrow PR prompt for PR 2.

## Do not do this

Do **not** paste the full master plan into Codex as an implementation task.

Do **not** ask Codex to build Career Vault, EvidenceGraph, ResumeVariantPlan, Review UI, Scout, MCP, or ChatGPT App in the first execution cycle.

Do **not** ask Codex to “build the application OS.”

## Operating model

```txt
Master plan = documentation
PR spec = scope control
Context pack = source/constraint memory
Codex prompt = one narrow execution task
Codex final report = evidence
GPT Pro after each PR = reviewer + next prompt generator
```

---

# 2. Blunt execution recommendation

**This is the right execution format if you keep it boring.**

Build the spine first:

```txt
PR 1 — pure TypeScript application-harness kernel
PR 2 — Convex shadow persistence
PR 3 — shadow ApplicationContext builder from existing job + CV/profile
```

Do not give Codex the full roadmap. Give Codex one PR prompt at a time.

Do not start with MCP, Scout, Career Vault UI, EvidenceGraph, ResumeVariantPlan, generation changes, parser changes, or UI.

The first three PRs should make Twoweeks safer to extend without changing current user behavior.

---

# 3. Master Architecture Decision Record draft

Save as:

```txt
docs/decisions/2026-06-08-application-os-master-plan.md
```

```md
# Application OS master plan

Date: 2026-06-08  
Status: accepted direction, phased execution  
Scope: architecture sequencing and Codex execution boundaries

## Product thesis

Twoweeks is an AI job-application operating system.

The product should become a trusted application harness where a user can bring a job opportunity and receive a truthful, reviewable application packet:

```txt
job
→ stable application context
→ evidence-backed match
→ resume variant plan
→ tailored resume artifact
→ cover-letter artifact
→ human review
→ approved export
→ tracked application
```

Twoweeks is not trying to become a generic job scraper, a blind AI resume generator, or an auto-apply bot.

## Current baseline

The existing app already has:

- CV/profile ingestion
- canonical CV/profile data
- CV Forge
- Proposal Forge
- JobsWorkspace
- job records
- match review
- proposal / cover-letter generation
- export
- active CV snapshots
- Chrome extension handoff

Existing flows must keep working during migration.

## Execution environment

The intended execution workflow is:

- ChatGPT / GPT Pro for senior architecture review, source-grounded planning, and PR prompt generation.
- Codex for repository execution.
- `SKILL.md` / skills for reusable agent workflows.
- PR-specific Codex prompts for implementation.
- Context packs and execution packs for each PR.
- MCP only later as an adapter over stable internal Twoweeks tools.
- ChatGPT Apps SDK only much later as a distribution layer, not core architecture.

This is not a GPT Store/custom GPT plan.

## Architecture layers

### Spine

Owns durable identity and replay safety.

```txt
application-harness/
  SourceRefV1
  ApplicationContextV1
  ApplicationRunV1
  ApplicationArtifactV1 shell
  ApplicationEventV1 shell
  fingerprints
  idempotency
```

### Proof

Owns source truth and claim safety.

```txt
candidate-evidence/
  CandidateEvidenceProfileV1
  CandidateSourceDocumentV1
  CandidateFactV1
  import batches
  dedupe
  review states
  visibility/privacy

career-knowledge/
  ATS rules
  resume/CV rules
  cover-letter rules
  claim-safety rules
  market resolver

evidence-graph/
  JobDemandGraphV1
  EvidenceGraphV1
  allowed claims
  missing requirements
  risk flags
```

### Product value

Owns reviewable user outcomes.

```txt
resume-variants/
  ResumeVariantPlanV1
  resume variant artifacts

application-review/
  read-first approval cockpit

application-packages/
  approved application packet
```

### Distribution

Owns agent interfaces only after internal services are stable.

```txt
agent-tools/
  internal typed tool contracts

mcp/
  local/remote adapter later
```

## Hard invariants

1. The master architecture plan is documentation, not a Codex task.
2. Codex must receive exactly one narrow PR-specific prompt at a time.
3. PR 1 must be pure TypeScript only.
4. PR 1 must not touch Convex schema/functions, UI, generation, parser/import, routes, CV Forge, Proposal Forge, export, JobsWorkspace, active CV snapshots, or premium cover-letter generation.
5. `application-harness/` is deliberately narrow. It is not `application-core/`.
6. The harness is not a workflow engine.
7. The harness owns deterministic fingerprints, idempotency, context identity, run identity, artifact identity, and provenance references.
8. Candidate facts must preserve source truth.
9. AI may classify, dedupe, extract metadata, and propose review states, but it must not rewrite candidate facts into polished resume claims.
10. Polished generated text belongs only in generated artifacts.
11. Every generated claim must map back to approved source facts or be flagged as unsupported.
12. Canonical CVs must not be mutated when generating tailored variants.
13. Candidate evidence profiles must not be mutated when generating variants.
14. Approval gates are required before export, tracking, send, submit, or apply.
15. MCP must call internal Twoweeks tools later. MCP must not own business logic.

## Source and privacy rules

Source material is sensitive.

Allowed later, after the foundation block:

- pasted text
- Markdown
- user-uploaded LinkedIn export
- LinkedIn profile PDF
- uploaded CVs
- Upwork/freelance exports supplied by the user
- project lists
- portfolio material supplied by the user
- manual facts

Rules:

- Each import is a source document, not final truth.
- Source documents parse into pending candidate facts.
- Pending facts require review before they become eligible.
- Private facts must never enter public CVs, cover letters, exports, MCP outputs, or application packages.
- `never_use` facts must never be selected.
- Raw source documents must not be sent wholesale to generation prompts.
- Deleting or rejecting a source document must make derived pending facts ineligible unless the user explicitly preserves them.
- Portfolio material is user-supplied but untrusted. Remote portfolio content must be fetched/sanitized separately, stored as source material, parsed into pending facts, and never treated as approved evidence until user review.

## Forbidden actions

Forbidden for MVP:

- LinkedIn scraping
- logged-in LinkedIn crawling
- anti-bot bypass
- Upwork scraping
- Indeed scraping
- automated apply
- automated submit
- automated send
- mutating canonical CVs during generation
- mutating source candidate facts into marketing copy
- exporting before approval
- tracking before approval

## Why `application-harness/` is narrow

The name is intentional.

`application-harness/` means a thin identity and replay-safety layer. It does not own product behavior.

It may define:

- stable types
- source references
- fingerprints
- hashes
- idempotency keys
- context/run/artifact/event shell identities

It may not define:

- CV editing
- Proposal editing
- parser behavior
- export behavior
- generation prompts
- job import behavior
- UI routes
- MCP tools
- Scout adapters
- application package UX

## Why this master plan is documentation, not a Codex task

The master plan contains many future modules. Giving the whole plan to Codex would invite broad implementation, opportunistic refactors, and architecture drift.

Execution must happen through narrow PR prompts only.

Each Codex prompt must include:

- exact PR goal
- source files to inspect first
- allowed scope
- forbidden scope
- likely files
- required tests
- acceptance criteria
- stop conditions
- required final report

## Foundation block

PR 1–3 are one logical foundation block:

```txt
PR 1 — pure TypeScript application-harness kernel
PR 2 — additive Convex shadow persistence for contexts/runs/artifact shells
PR 3 — shadow ApplicationContext builder from existing job + CV/profile
```

No Career Vault import, EvidenceGraph, ResumeVariantPlan, Review UI, Scout, MCP, ChatGPT App, or generation changes are allowed before these three PRs are complete and tested.

## Why later layers are delayed

### Career Vault

Delayed until the harness can identify application contexts and runs safely.

### EvidenceGraph

Delayed until candidate/job context identity exists and shadow persistence is available.

### ResumeVariantPlan

Delayed until evidence selection and risk flags exist.

### Review UI

Delayed until there is real context/evidence/artifact data to review.

### Scout

Delayed until Twoweeks can convert one saved/manual job into a safe application packet.

### MCP

Delayed until internal tools, approval gates, artifacts, and audit logs exist.

### ChatGPT App

Delayed until internal product workflows are stable. ChatGPT App distribution is packaging, not the core architecture.

## LinkedIn scraping policy

LinkedIn scraping is forbidden for MVP.

Safe LinkedIn paths are:

- user-uploaded LinkedIn data export
- user-uploaded LinkedIn profile PDF
- pasted profile text
- manually entered facts

## Stop-condition philosophy

Stop conditions are not suggestions. They are execution brakes.

If Codex touches forbidden surfaces, expands scope, rewrites active flows, adds platform work, changes generation behavior, or performs broad cleanup, stop the run and review the diff before continuing.

The safest path is boring, additive, testable PRs.
```

---

# 4. Execution model: ChatGPT + Codex + skills

## Roles

### ChatGPT / GPT Pro

Use GPT Pro for:

```txt
senior architecture review
source-grounded planning
PR spec writing
Codex prompt generation
reviewing Codex final reports
deciding fix-forward vs next PR
creating context packs
creating/revising SKILL.md workflow docs
```

Do not use GPT Pro as the executor.

### Codex

Use Codex for:

```txt
repo inspection
implementation
focused tests
typecheck
PR final report
```

Codex receives one PR-specific execution pack at a time.

### SKILL.md / skills

Use skills for reusable workflow memory:

```txt
how to work in Twoweeks
how to inspect source first
how to avoid broad rewrites
how to prepare final reports
how to respect stop conditions
how to use context packs
```

Skills should not contain the full product roadmap as an implementation task.

### Context packs

A context pack is a curated source/constraint bundle for one PR.

It should include:

```txt
confirmed existing paths
proposed paths
forbidden paths
source files to inspect first
test commands
open uncertainties
stop conditions
```

### Execution packs

An execution pack is:

```txt
context pack
+ PR-specific Codex prompt
+ hard stop conditions
+ required final report format
```

### MCP later

MCP should eventually expose stable internal Twoweeks tools such as:

```txt
tw_create_application_context
tw_build_evidence_graph
tw_plan_resume_variant
tw_draft_cover_letter
tw_export_artifact
tw_track_application
```

But MCP must come after internal tools, approval gates, artifacts, and audit logs.

MCP is an adapter over Twoweeks business logic, not the business logic.

---

# 5. Compact PR roadmap

| PR | Title | Phase | Goal | Allowed scope | Forbidden scope | Tests | Stop conditions | Rollback risk |
|---:|---|---|---|---|---|---|---|---|
| 1 | Pure `application-harness/` kernel | Spine | Define pure TS types, stable hashes, source refs, idempotency | Proposed `my-app/src/modules/application-harness/*`; decision doc; Vitest tests | Convex, UI, generation, parser, routes, CV Forge, Proposal Forge, export, active snapshots, JobsWorkspace, `premiumCoverLetter.ts`, MCP, Scout | hash/idempotency/unit fixtures | Any active route import or schema/function change | Very low |
| 2 | Convex shadow persistence | Spine | Add additive context/run/artifact shell persistence | Proposed `my-app/convex/applicationContexts.ts`, `applicationRuns.ts`, `applicationArtifacts.ts`; additive schema | UI wiring, generation, parser, export, existing behavior changes, event table unless justified | create/reuse context/run; artifact insert; schema compile | Touching existing table behavior or active routes | Low-medium |
| 3 | Shadow ApplicationContext builder | Spine | Build context from existing job + CV/profile in shadow mode | Proposed builder module + Convex helper; reads existing job/profile/CV | generation, UI, parser, export, route behavior | same inputs reuse context; changed job/CV hash; no mutation | Any active user-visible behavior change | Medium |
| 4 | Candidate source/fact kernel | Proof | Define source/fact pure types and text-fixture extraction only | Proposed candidate-evidence module; text/Markdown/manual fixtures | PDF/DOCX binding, remote fetch, UI, generation | sourcePath, dedupe, pending facts, source truth preserved | LLM rewriting facts or parser rewrite | Low |
| 5 | CareerKnowledge rules | Proof | Add static rules + resolver | Proposed career-knowledge module | prompt rewrite, UI, generation | deterministic rules, filtering, duplicate IDs | raw PDF prompt stuffing | Low |
| 6 | Candidate evidence persistence | Proof | Persist source docs and pending facts | Additive tables/functions | replacing `userProfiles`, parser, CV Forge | dedupe, review state, privacy fields | changing canonical profile behavior | Medium |
| 7 | EvidenceGraph shadow | Proof | Build matches/missing/risk/allowed claims | Proposed evidence-graph module | replacing premium cover-letter path | unsupported metric/tool/cert/language flags | editing `premiumCoverLetter.ts` prematurely | Medium |
| 8 | ResumeVariantPlan artifact | Product Value | Reviewable plan before CV generation | Plan artifact only | final CV generation, canonical CV mutation | every plan item maps to facts | generating polished CV text | Medium |
| 9 | Minimal review cockpit | Product Value | Read-first context/evidence/plan review | Additive gated route/component | editor replacement, export rewrite | risks visible, missing visible, disabled actions | CV/Proposal UI drift | Medium |
| 10 | Resume variant artifact | Product Value | Create separate variant artifact/document | Artifact or derived CV document with provenance | canonical CV mutation | provenance complete, reload-safe | overwriting canonical CV | Medium-high |
| 11 | Cover-letter artifact adapter | Product Value | Store cover-letter output as artifact | Narrow adapter around existing output | Proposal Forge rewrite, prompt rewrite | artifact reuse, approved immutability | generation behavior drift | Medium-high |
| 12 | ApplicationPackageV1 | Product Value | Bundle approved job/resume/letter/review | Additive package table/page | campaigns, Scout, MCP | approved packet state, export gates | bag-of-null package object | Medium |
| 13 | Internal tool contracts | Distribution | Typed internal tool API | Proposed agent-tools contracts | public MCP, send/apply/submit | schemas, approval gates | exposing unsafe tools | Medium |
| 14 | Controlled ATS Scout adapters | Distribution | Deterministic supported job sourcing | Greenhouse/Lever/Ashby-style adapters | LinkedIn/Upwork/Indeed scraping | dedupe, normalized job leads | crawler/bot behavior | High |
| 15 | Local MCP beta | Distribution | Local wrapper over internal tools | Local-only adapter | remote/public MCP | allowlist, approval-required tools blocked | bypassing approval | High |
| 16 | Remote MCP / ChatGPT App exploration | Distribution | Readiness/spec only | Docs/audit/spec | shipping public integration | none or docs validation | production integration creep | Medium |

---

# 6. Full PR spec — PR 1

## Title

Pure TypeScript `application-harness/` kernel.

## Goal

Add a pure TypeScript harness kernel that defines stable application identity primitives:

```txt
SourceRefV1
ApplicationContextV1
ApplicationRunV1
ApplicationArtifactV1 shell
ApplicationEventV1 shell
stable serialization
hash helpers
source-ref hash helper
idempotency helper
unit tests
decision doc
```

## Why now

The app needs deterministic context/run/artifact identity before any durable execution, generation artifact, evidence graph, review UI, or agent tool exists.

This avoids:

```txt
duplicate work
accidental overwrites
broad route coupling
premature workflows
agent side effects
```

## Confirmed existing source files Codex must inspect first

Confirmed existing repo paths:

```txt
AGENTS.md
my-app/package.json
```

Why:

```txt
AGENTS.md establishes small, reversible, active-path work.
my-app/package.json defines current project scripts and test commands.
```

To inspect before implementation:

```txt
my-app/vitest.config.*              # if present
nearest existing __tests__ files    # for test style
tsconfig files                      # for import/path conventions
```

Mark as “to inspect” if the exact path is unknown.

## Allowed scope

Proposed future paths:

```txt
my-app/src/modules/application-harness/schema.ts
my-app/src/modules/application-harness/fingerprints.ts
my-app/src/modules/application-harness/idempotency.ts
my-app/src/modules/application-harness/__tests__/fingerprints.test.ts
my-app/src/modules/application-harness/__tests__/idempotency.test.ts
docs/decisions/2026-06-08-application-harness-kernel.md
```

## Forbidden scope

```txt
Convex schema
Convex functions
UI
generation
parser/import
route wiring
CV Forge
Proposal Forge
export
active CV snapshots
JobsWorkspace
premiumCoverLetter.ts
MCP
Scout
package dependencies
unrelated refactors
formatting rewrites
```

## Required planning-level types

No implementation code here; these are field specs.

### SourceRefV1

Fields:

```txt
sourceType:
  job
  cv
  candidate_source_document
  candidate_fact
  proposal
  artifact
sourceId
sourcePath?
sourceHash?
```

### ApplicationContextV1

Fields:

```txt
id
userId
job:
  jobId
  sourceUrl?
  title?
  company?
  rawTextHash
candidate:
  sourceKind: cv | candidate_evidence_profile
  cvId?
  candidateEvidenceProfileId?
  candidateHash
  selectedLanguage?
  market?
settingsHash
contextHash
reviewState:
  draft
  needs_review
  approved
  superseded
sourceRefs: SourceRefV1[]
createdAt
updatedAt
version: 1
```

### ApplicationRunV1

Fields:

```txt
id
userId
contextId?
operation:
  build_context
  build_evidence_graph
  plan_resume_variant
  draft_cover_letter
  create_artifact
  export_artifact
  track_application
inputHash
idempotencyKey
status:
  queued
  running
  succeeded
  failed
  blocked
attemptCount
resultIds?
blockedReason?
error?
createdAt
updatedAt
version: 1
```

### ApplicationArtifactV1 shell

Fields:

```txt
id
userId
contextId
runId?
type:
  cover_letter
  resume_variant_plan
  resume_variant
  resume_patch_plan
  export
status:
  draft
  needs_review
  approved
  superseded
  blocked
title
content: unknown
textPreview?
sourceHashes:
  contextHash
  evidenceGraphHash?
  generatorInputHash?
provenance:
  jobId?
  cvId?
  candidateEvidenceProfileId?
  evidenceGraphId?
  sourceFactIds?
sourceRefs: SourceRefV1[]
createdAt
updatedAt
version: 1
```

### ApplicationEventV1 shell

Fields:

```txt
id
userId
contextId?
runId?
eventType
payload?
createdAt
version: 1
```

## Required functions

```txt
stableSerialize(value)
buildStableHash(value)
buildJobHash({ jobId, rawDescription, sourceUrl, title, company })
buildCandidateHash({ cvId, candidateEvidenceProfileId, structuredSectionsHash, cvSnapshotHash })
buildSettingsHash(settings)
buildContextHash({ jobHash, candidateHash, settingsHash })
buildSourceRefHash(sourceRef)
buildApplicationRunIdempotencyKey({ userId, operation, contextHash, inputHash })
```

## Required tests

```txt
same object with different key order hashes the same
arrays preserve order in hash behavior
changed job text changes jobHash
changed candidate hash input changes candidateHash
changed settings changes settingsHash
same operation input produces same idempotency key
different operation changes idempotency key
SourceRefV1 hash changes when sourcePath/sourceHash changes
helper functions do not mutate inputs
artifact/event shell fixtures compile and hash predictably
```

## Acceptance criteria

```txt
new unit tests pass
narrow typecheck or project typecheck passes if feasible
no existing user route behavior changes
no UI changes
no Convex schema/function changes
no generation output changes
decision doc explains pure/additive scope and deferrals
only intended files changed
```

## Rollback risk

Very low.

Rollback:

```txt
delete proposed application-harness module
delete PR 1 decision doc
```

## Stop conditions

Stop if Codex touches:

```txt
my-app/convex/**
CV Forge files
Proposal Forge files
export files
parser/import files
route files
premiumCoverLetter.ts
package.json dependencies
```

## Deferred

```txt
Convex persistence
context builder
Career Vault
candidate facts
EvidenceGraph
ResumeVariantPlan
Review UI
Scout
MCP
generation changes
```

---

# 7. Full PR spec — PR 2

## Title

Additive Convex shadow persistence for contexts/runs/artifact shells.

## Goal

Add additive Convex persistence for the harness objects without wiring active routes:

```txt
applicationContexts
applicationRuns
applicationArtifacts
createOrReuseContext
createOrReuseRun
insertArtifactShell
read helpers
indexes
tests
decision doc/update
```

## Why now

PR 1 proves deterministic identity in pure TypeScript.

PR 2 proves those identities can be stored/reused safely without changing current product behavior.

## Confirmed existing source files Codex must inspect first

Confirmed:

```txt
AGENTS.md
my-app/package.json
my-app/convex/schema.ts
my-app/convex/activeCvSnapshots.ts
```

Why:

```txt
schema.ts owns current Convex schema and table/index style.
activeCvSnapshots.ts shows current query/mutation style and active snapshot behavior.
```

To inspect:

```txt
my-app/convex/_generated/*          # generated API conventions, do not manually edit
nearby Convex __tests__ files       # exact testing convention
existing convex helper modules      # current mutation/query patterns
```

## Allowed scope

Proposed future paths:

```txt
my-app/convex/applicationContexts.ts
my-app/convex/applicationRuns.ts
my-app/convex/applicationArtifacts.ts
my-app/convex/schema.ts             # additive tables/indexes only
my-app/convex/**/__tests__/*        # only if repo has this test pattern
docs/decisions/2026-06-08-application-harness-persistence.md
```

May import PR 1 pure helpers.

## Forbidden scope

```txt
no UI
no route wiring
no generation
no parser
no export
no changes to existing table behavior
no event table unless a real audit use case is explicitly scoped
no CV Forge changes
no Proposal Forge changes
no active JobsWorkspace changes
no MCP
no Scout
```

## Required persistence behavior

```txt
createOrReuseApplicationContext by contextHash
createOrReuseApplicationRun by idempotencyKey
insert application artifact shell
read context/run/artifact by id
patch run status safely
do not replace whole documents for routine status updates
```

## Required tests

```txt
same contextHash reuses existing context
same idempotencyKey reuses existing run
different idempotencyKey creates new run
artifact shell can be inserted and read
status patch updates only relevant run fields
schema compiles
no event table added
```

## Acceptance criteria

```txt
additive schema only
helper functions compile
new focused tests pass
schema compile / typecheck passes if feasible
existing active flows untouched
no active route imports
no user-visible behavior changes
```

## Rollback risk

Low-medium.

Reason:

```txt
schema additions require discipline, but no active route wiring limits runtime exposure
```

## Stop conditions

Stop if Codex:

```txt
modifies existing jobs/proposals/userProfiles behavior
adds UI
wires active routes
adds generation calls
adds event table without explicit reason
uses db.replace for routine state patches where patch is safer
```

## Deferred

```txt
ApplicationContext builder
events table
review UI
tool contracts
generation artifacts
candidate facts
EvidenceGraph
MCP
Scout
```

---

# 8. Full PR spec — PR 3

## Title

Shadow ApplicationContext builder from existing job + CV/profile.

## Goal

Build and persist/reuse `ApplicationContextV1` in shadow mode from existing job + selected CV/profile data.

No user-visible route behavior changes.

## Why now

PR 1 and PR 2 prove identity and persistence.

PR 3 proves the harness can wrap the current app’s real data without replacing current flows.

## Confirmed existing source files Codex must inspect first

Confirmed:

```txt
AGENTS.md
my-app/convex/schema.ts
my-app/convex/activeCvSnapshots.ts
my-app/src/lib/proposal-personalization.ts
```

Why:

```txt
jobs table has existing job identity/source fields, raw description, parsed requirements, status, and review items.
userProfiles table has default resume fields, summary, skills, experience, education, LinkedIn/raw text/languages/contact/metadata/cvDocument/idempotency/achievements.
active CV snapshots are compressed and must not be treated as full career truth.
proposal personalization has strong caps and must not become the Career Vault path.
```

To inspect:

```txt
my-app/convex/jobsPublic.ts                  # confirmed by prior search; inspect actual API before using
my-app/convex/lib/jobs/canonicalJobs.ts      # confirmed by prior search; inspect actual helpers before using
my-app/src/types/cvDocument*                 # exact current CvDocument type path to inspect
my-app/src/schemas/cvDocument.schema*        # exact schema path to inspect
current CV library/profile adapter modules   # inspect before referencing
nearest tests around jobs/proposal context   # inspect exact conventions
```

## Allowed scope

Proposed future paths:

```txt
my-app/src/modules/application-harness/buildApplicationContextV1.ts
my-app/src/modules/application-harness/selectors.ts
my-app/src/modules/application-harness/__tests__/buildApplicationContextV1.test.ts
my-app/convex/applicationContexts.ts          # extend with shadow builder only if PR 2 exists
docs/decisions/2026-06-08-application-context-shadow-builder.md
```

## Forbidden scope

```txt
no generation
no UI
no route behavior changes
no parser rewrite
no export changes
no Proposal Forge changes
no CV Forge changes
no active snapshot behavior changes
no Career Vault
no EvidenceGraph
no ResumeVariantPlan
no MCP
no Scout
```

## Required behavior

```txt
select job context fields from existing job record
select candidate context fields from existing CV/profile
prefer structured sections when available, but do not invent paths before inspecting current CvDocument shape
compute jobHash, candidateHash, settingsHash, contextHash
include SourceRefV1 entries
do not mutate inputs
optionally persist/reuse context through PR 2 helper if available
```

## Required tests

```txt
same job + same CV/profile builds same contextHash
changed job rawDescription changes jobHash/contextHash
changed candidate snapshot/hash changes candidateHash/contextHash
missing sourceUrl handled
missing company/title handled
builder does not mutate job input
builder does not mutate CV/profile input
same build twice reuses logical context if persistence path is included
compressed active snapshot is not treated as complete career truth
```

## Acceptance criteria

```txt
shadow-only builder
no active route behavior change
no generation change
no parser/export/UI change
deterministic output
no input mutation
focused tests pass
typecheck passes if feasible
```

## Rollback risk

Medium.

Reason:

```txt
PR 3 starts reading real app shapes.
Keep it shadow-only to limit runtime risk.
```

## Stop conditions

Stop if Codex:

```txt
changes active job import behavior
changes active CV/profile persistence
changes Proposal Forge generation
treats activeCvSnapshots as full candidate truth
rewrites parser/profile mapper
adds UI
```

## Deferred

```txt
CandidateEvidenceProfile
CandidateFact import
CareerKnowledge
EvidenceGraph
ResumeVariantPlan
Review UI
ApplicationPackage
tools/MCP/Scout
```

---

# 9. Codex-ready prompt — PR 1 only

Copy-paste this only. Do not paste the full roadmap.

```text
Context:
You are working in panamini/neyssan. Read AGENTS.md first. Treat v1 as the active baseline.

Twoweeks is evolving toward a trusted job-application harness, but this PR must be a tiny additive TypeScript kernel only.

Existing CV Forge, Proposal Forge, export, parser/import, JobsWorkspace, active CV snapshots, proposal persistence, premium cover-letter generation, and match review must keep working unchanged.

Goal:
Add a pure TypeScript application-harness kernel with deterministic schemas, source references, stable fingerprints, and idempotency helpers.

This PR must not add UI, Convex persistence, generation changes, parser changes, route wiring, or active product behavior changes.

Scope:
Allowed:
- Add a new module under:
  my-app/src/modules/application-harness/
- Add pure TypeScript planning-level types for:
  - SourceRefV1
  - ApplicationContextV1
  - ApplicationRunV1
  - minimal ApplicationArtifactV1 shell
  - minimal ApplicationEventV1 shell
- Add stable serialization and hash helpers.
- Add source-ref hash helper.
- Add idempotency key builder.
- Add focused Vitest unit tests.
- Add one short decision doc.

Do NOT change:
- Convex schema
- Convex functions
- CV Forge UI or state
- Proposal Forge UI or state
- proposal generation prompts
- premiumCoverLetter.ts
- export pipeline
- parser/import pipeline
- JobsWorkspace
- activeCvSnapshots
- package dependencies
- route definitions
- MCP code
- Scout/job-source adapter code
- styles or unrelated formatting
- unrelated files or tests

Required files:
Create:
- my-app/src/modules/application-harness/schema.ts
- my-app/src/modules/application-harness/fingerprints.ts
- my-app/src/modules/application-harness/idempotency.ts
- my-app/src/modules/application-harness/__tests__/fingerprints.test.ts
- my-app/src/modules/application-harness/__tests__/idempotency.test.ts
- docs/decisions/2026-06-08-application-harness-kernel.md

Before implementation:
1. Inspect AGENTS.md.
2. Inspect my-app/package.json for scripts.
3. Inspect the nearest existing Vitest test conventions before adding tests.
4. If test config path is unclear, locate the current Vitest config or nearest test setup before writing tests.
5. Do not inspect or edit broad unrelated app surfaces.

Required types:

SourceRefV1:
- sourceType:
  - "job"
  - "cv"
  - "candidate_source_document"
  - "candidate_fact"
  - "proposal"
  - "artifact"
- sourceId
- optional sourcePath
- optional sourceHash

ApplicationContextV1:
- id
- userId
- job:
  - jobId
  - optional sourceUrl
  - optional title
  - optional company
  - rawTextHash
- candidate:
  - sourceKind: "cv" | "candidate_evidence_profile"
  - optional cvId
  - optional candidateEvidenceProfileId
  - candidateHash
  - optional selectedLanguage
  - optional market
- settingsHash
- contextHash
- reviewState:
  - "draft"
  - "needs_review"
  - "approved"
  - "superseded"
- sourceRefs: SourceRefV1[]
- createdAt
- updatedAt
- version: 1

ApplicationRunV1:
- id
- userId
- optional contextId
- operation:
  - "build_context"
  - "build_evidence_graph"
  - "plan_resume_variant"
  - "draft_cover_letter"
  - "create_artifact"
  - "export_artifact"
  - "track_application"
- inputHash
- idempotencyKey
- status:
  - "queued"
  - "running"
  - "succeeded"
  - "failed"
  - "blocked"
- attemptCount
- optional resultIds
- optional blockedReason
- optional error
- createdAt
- updatedAt
- version: 1

ApplicationArtifactV1 shell:
- id
- userId
- contextId
- optional runId
- type:
  - "cover_letter"
  - "resume_variant_plan"
  - "resume_variant"
  - "resume_patch_plan"
  - "export"
- status:
  - "draft"
  - "needs_review"
  - "approved"
  - "superseded"
  - "blocked"
- title
- content: unknown
- optional textPreview
- sourceHashes:
  - contextHash
  - optional evidenceGraphHash
  - optional generatorInputHash
- provenance:
  - optional jobId
  - optional cvId
  - optional candidateEvidenceProfileId
  - optional evidenceGraphId
  - optional sourceFactIds
- sourceRefs: SourceRefV1[]
- createdAt
- updatedAt
- version: 1

ApplicationEventV1 shell:
- id
- userId
- optional contextId
- optional runId
- eventType
- optional payload
- createdAt
- version: 1

Important invariants:
- The harness is not a workflow engine.
- The harness must not own generation, UI, parser, export, active routes, or product workflows.
- SourceRefV1 is a type only, not a table.
- ApplicationEventV1 is a type shell only, not a table.
- No generated text or candidate-fact logic belongs in this PR.
- All helpers must be deterministic.
- Helper functions must not mutate input objects.

Required helpers:
- stableSerialize(value)
- buildStableHash(value)
- buildJobHash({ jobId, rawDescription, sourceUrl, title, company })
- buildCandidateHash({ cvId, candidateEvidenceProfileId, structuredSectionsHash, cvSnapshotHash })
- buildSettingsHash(settings)
- buildContextHash({ jobHash, candidateHash, settingsHash })
- buildSourceRefHash(sourceRef)
- buildApplicationRunIdempotencyKey({
    userId,
    operation,
    contextHash,
    inputHash
  })

Stable serialization rules:
- object keys sorted
- undefined omitted or normalized consistently
- arrays preserve order
- primitives handled consistently
- input objects are not mutated

Required tests:
- same object with different key order hashes the same
- arrays preserve order in hash behavior
- changed job text changes jobHash
- changed candidate hash input changes candidateHash
- changed settings changes settingsHash
- same operation input produces same idempotency key
- different operation changes idempotency key
- SourceRefV1 hash changes when sourcePath/sourceHash changes
- helper functions do not mutate input objects
- artifact shell fixture compiles and hashes predictably
- event shell fixture compiles and hashes predictably

Decision doc must explain:
- why this is pure/additive
- why persistence is deferred to PR 2
- why generation/UI/active routes/platform work are out of scope
- why SourceRefV1 is included early
- why ApplicationEventV1 is type-only
- how this prepares idempotent application workflows
- what remains deferred

Constraints:
- Smallest safe change.
- No active route imports.
- No Convex schema migration.
- No Convex functions.
- No broad refactor.
- No opportunistic cleanup.
- No package additions.
- Use existing project test framework.
- Keep public behavior unchanged.
- Do not rewrite comments/docs outside the new decision doc.
- Do not perform formatting-only rewrites.

Acceptance criteria:
- New unit tests pass.
- TypeScript passes for changed files or the narrowest available typecheck passes.
- No existing user route behavior changes.
- No UI changed.
- No Convex schema changed.
- No Convex functions added.
- No generation output changed.
- No package dependencies added.
- Only intended files changed.

Tests to run:
- Add Vitest tests under the new module.
- Run the narrowest relevant command, likely:
  cd my-app
  rtk npm test -- application-harness --run

If feasible, also run:
  rtk npx tsc --noEmit

Required final report:
- Short audit summary
- Files changed
- Tests run and results
- What was verified
- What remains deferred
- Any files touched unexpectedly
- Any uncertainties
- Next smallest PR
```

---

# 10. Reusable GPT Pro next-PR prompt template

Use this after Codex finishes each PR.

```text
You are a skeptical senior product architect, staff-level full-stack engineer, AI systems reviewer, and Codex execution planner.

Task:
Produce the next Codex-ready prompt for Twoweeks. Do not implement code. Do not generate prompts for multiple PRs. Produce exactly one narrow next-PR prompt only if the previous PR is safe to build on.

Current architecture constraints:
- Build the spine first.
- Kill theater.
- Delay platform.
- Use application-harness/, not application-core/.
- The master plan is documentation, not a Codex task.
- Codex receives only one narrow PR-specific prompt at a time.
- Existing CV Forge, Proposal Forge, export, parser/import, JobsWorkspace, active CV snapshots, job import, match review, proposal generation, and current routes must keep working.
- No broad rewrites.
- No unrelated cleanup.
- No MCP, Scout, Career Vault UI, EvidenceGraph, ResumeVariantPlan, Review UI, generation changes, or distribution work before explicitly sequenced.
- Candidate facts must preserve source truth.
- SourceRefV1 is type-only unless a later PR explicitly persists source docs.
- ApplicationEventV1 is type-only until audit needs are real.
- Stop conditions are hard brakes.

Previous PR:
- PR number/title:
- Branch:
- PR link:
- Merged/unmerged:
- Base branch:
- Head branch/commit:

Previous PR report:
PASTE CODEX FINAL REPORT HERE

Changed files:
PASTE CHANGED FILE LIST HERE

Diff summary:
PASTE DIFF SUMMARY HERE

Tests run:
PASTE COMMANDS HERE

Test output:
PASTE OUTPUT HERE

TypeScript output:
PASTE OUTPUT HERE

Failed tests or warnings:
PASTE HERE

Unexpected files touched:
PASTE HERE

Unresolved Codex uncertainty:
PASTE HERE

Review comments:
PASTE HERE

Current diff:
PASTE RELEVANT DIFF OR LINK HERE

Required behavior:
1. Inspect the real source context before producing the next prompt.
2. Confirm whether the previous PR is safe to build on.
3. Identify any P0/P1 issues in the previous PR that must be fixed before the next PR.
4. If there are blocking issues, produce a fix-forward Codex prompt instead of the planned next PR prompt.
5. If safe, produce exactly one Codex-ready prompt for the next smallest PR.
6. The prompt must include:
   - Context
   - Goal
   - Source files/functions to inspect first
   - Scope
   - Do NOT change
   - Required files
   - Required work
   - Required tests
   - Constraints
   - Acceptance criteria
   - Tests to run
   - Required final report
   - Stop conditions
7. Do not include future roadmap implementation details beyond what the next PR needs.
8. Do not broaden scope.
9. Do not write implementation code.
10. Clearly distinguish confirmed existing repo paths from proposed future paths.
11. If a source path is unknown, mark it as “to inspect,” not as fact.

Output format:
# Verdict on previous PR
# Blocking issues, if any
# Next PR selection
# Codex-ready prompt for the next PR
# Stop conditions
```

---

# 11. When to ask GPT Pro again

After each Codex PR, paste this back:

```txt
1. Codex final report
2. Full changed files list
3. Diff summary
4. Test commands run
5. Full test output or relevant failure excerpts
6. TypeScript/typecheck output
7. Lint output, if run
8. Any failed tests
9. Any skipped tests
10. Any files touched unexpectedly
11. Any Codex uncertainty or “could not verify”
12. Any runtime/browser checks, if relevant
13. Branch name
14. PR link
15. Merged/unmerged state
16. Commit SHA
17. Review comments, if any
18. Current diff or patch link
```

How GPT Pro should use it:

```txt
If previous PR has P0 issues:
  generate a fix-forward prompt, not the planned next PR.

If tests failed and failures may be related:
  generate a narrow test/fix prompt.

If unexpected files were touched:
  inspect whether they violate stop conditions before proceeding.

If previous PR is safe:
  generate exactly one prompt for the next smallest PR.

If the merged/unmerged state is unclear:
  ask for branch/PR status or produce a prompt that starts with source inspection and no code changes until state is confirmed.

If Codex reported uncertainty:
  make the next prompt inspect/verify that uncertainty before new work.

If the diff broadened scope:
  stop and review. Do not continue roadmap execution.
```

---

# 12. Hard stop conditions

Stop Codex immediately if it:

```txt
touches CV Forge UI
touches Proposal Forge UI
changes proposal generation prompts
edits premiumCoverLetter.ts
changes export
rewrites parser/import
adds Convex schema in PR 1
adds Convex functions in PR 1
adds MCP
adds Scout/job-source adapters
adds browser automation
adds a Career Vault UI
adds ApplicationPackageV1 table
adds campaigns
adds Google/Drive/Docs integration
adds apply/send/submit
mutates canonical CVs
changes active route behavior
adds package dependencies
deletes legacy support
removes current tests
does broad formatting/style rewrites
performs opportunistic cleanup
rewrites unrelated docs
renames active modules
moves existing folders
introduces remote/network behavior
```

---

# 13. Draft Codex skill / SKILL.md

This is a draft. Add only when you are ready to formalize the reusable workflow.

Proposed future path:

```txt
skills/twoweeks-application-os/SKILL.md
```

or in your wiki/skills system if that is where active skills live.

```md
# Twoweeks Application OS Codex Skill

Use this skill when implementing narrow Twoweeks Application OS PRs.

## Purpose

Help Codex execute one small, source-grounded, non-regressive PR at a time for Twoweeks.

This skill supports:

- application-harness work
- candidate evidence work
- career knowledge work
- evidence graph work
- resume variant work
- application artifact work
- review/tool work later

It does not authorize broad architecture implementation.

## Execution model

ChatGPT / GPT Pro plans and reviews.
Codex executes.
Each Codex task must come from a PR-specific prompt.
The master architecture plan is documentation, not a task.

## Required preflight

Before implementation:

1. Read `AGENTS.md`.
2. Read the PR-specific context pack.
3. Inspect the source files named in the prompt.
4. Inspect nearest existing tests and test conventions.
5. Confirm allowed scope and forbidden scope.
6. Do not inspect broad unrelated surfaces unless needed to resolve an explicit uncertainty.

## Implementation discipline

- Keep changes narrow.
- Do not rewrite active flows.
- Do not perform opportunistic cleanup.
- Do not add dependencies unless explicitly allowed.
- Do not touch forbidden files.
- Do not broaden scope because a future PR will need it.
- Prefer pure helpers and tests before persistence or UI.
- Preserve public behavior unless the PR explicitly changes it.

## Stop conditions

Stop and report if the task would require:

- CV Forge UI changes
- Proposal Forge UI changes
- proposal generation prompt changes
- parser/import rewrites
- export changes
- route behavior changes
- MCP
- Scout/job-source adapters
- browser automation
- package dependencies
- active schema changes outside scope
- canonical CV mutation
- broad formatting rewrites
- deletion of legacy support or tests

## Reporting format

Final report must include:

- short audit summary
- files changed
- tests run and results
- what was verified
- what remains deferred
- any files touched unexpectedly
- any uncertainties
- next smallest PR
```

---

# 14. PR context-pack template

Use this for future PRs.

```md
# PR <number> Context Pack — <title>

## PR goal

One sentence.

## Confirmed existing source paths

- `path`
- `path`

## Proposed new paths

- `path`
- `path`

## Source files/functions Codex must inspect first

- `path` — why
- `path` — why
- `to inspect: <unknown path/pattern>` — why

## Allowed scope

- item
- item

## Forbidden scope

- item
- item

## Required tests

- item
- item

## Commands to run

```bash
cd my-app
rtk npm test -- <filter> --run
```

Optional if feasible:

```bash
rtk npx tsc --noEmit
```

## Known uncertainties

- item
- item

## Stop conditions

Stop if Codex touches:

- path/surface
- path/surface

## Required final report

- short audit summary
- files changed
- tests run and results
- what was verified
- what remains deferred
- unexpected files
- uncertainties
- next smallest PR
```

---

# 15. PR 1 context pack

Use this with the PR 1 prompt if Codex needs a separate context pack.

```md
# PR 1 Context Pack — application-harness kernel

## PR goal

Add a pure TypeScript `application-harness/` kernel with source refs, context/run/artifact/event shell types, stable serialization, hash helpers, and idempotency helpers.

## Confirmed existing source paths

- `AGENTS.md`
- `my-app/package.json`

## Proposed new paths

- `my-app/src/modules/application-harness/schema.ts`
- `my-app/src/modules/application-harness/fingerprints.ts`
- `my-app/src/modules/application-harness/idempotency.ts`
- `my-app/src/modules/application-harness/__tests__/fingerprints.test.ts`
- `my-app/src/modules/application-harness/__tests__/idempotency.test.ts`
- `docs/decisions/2026-06-08-application-harness-kernel.md`

## Source files Codex must inspect first

- `AGENTS.md` — project operating rules.
- `my-app/package.json` — current scripts and test command.
- nearest existing Vitest tests — test style.
- `to inspect: vitest config path` — exact test setup if needed.
- `to inspect: tsconfig path` — import/path conventions if needed.

## Allowed scope

- pure TypeScript types
- pure helpers
- focused Vitest tests
- one decision doc

## Forbidden scope

- Convex schema
- Convex functions
- UI
- generation
- parser/import
- route wiring
- CV Forge
- Proposal Forge
- export
- active CV snapshots
- JobsWorkspace
- `premiumCoverLetter.ts`
- MCP
- Scout
- dependencies
- broad refactors
- formatting rewrites

## Required tests

- same object with different key order hashes the same
- arrays preserve order in hash behavior
- changed job text changes jobHash
- changed candidate input changes candidateHash
- changed settings changes settingsHash
- same operation input produces same idempotency key
- different operation changes idempotency key
- SourceRefV1 hash changes when sourcePath/sourceHash changes
- helper functions do not mutate inputs
- artifact/event shell fixtures compile and hash predictably

## Commands to run

```bash
cd my-app
rtk npm test -- application-harness --run
```

Optional if feasible:

```bash
rtk npx tsc --noEmit
```

## Known uncertainties

- exact Vitest config path must be inspected by Codex
- exact nearest test conventions must be inspected by Codex

## Stop conditions

Stop if Codex touches:

- `my-app/convex/**`
- CV Forge UI/state files
- Proposal Forge UI/state files
- export pipeline files
- parser/import files
- route files
- `premiumCoverLetter.ts`
- dependency manifests for package additions

## Required final report

- short audit summary
- files changed
- tests run and results
- what was verified
- what remains deferred
- unexpected files touched
- uncertainties
- next smallest PR
```

---

# 16. Start checklist

## Before opening Codex

- [ ] Save the ADR section to `docs/decisions/2026-06-08-application-os-master-plan.md`, or keep it as an external plan if you do not want a repo doc yet.
- [ ] Decide whether to create a `skills/twoweeks-application-os/SKILL.md` now or later.
- [ ] Keep PR 1 separate from the master ADR if you want the first PR ultra-small.
- [ ] Copy only the PR 1 Codex prompt.
- [ ] Optionally copy the PR 1 context pack.
- [ ] Do not paste the full roadmap into Codex.
- [ ] Tell Codex to stop if it hits the hard stop list.

## After Codex finishes PR 1

Paste back to GPT Pro:

- [ ] Codex final report
- [ ] changed files
- [ ] diff summary
- [ ] test commands
- [ ] test output
- [ ] typecheck output
- [ ] failures
- [ ] unexpected files
- [ ] Codex uncertainty
- [ ] branch/PR link
- [ ] merged/unmerged state

Then ask GPT Pro:

```txt
Review this PR result like a skeptical senior engineer.
If safe, produce the next narrow Codex prompt.
If unsafe, produce a fix-forward prompt.
```

---

# Shortest strategy sentence

Build the **application harness** first, prove idempotent replay and provenance in shadow mode, then add candidate evidence and artifacts; only after that should skills, MCP, Scout, or distribution call Twoweeks tools.


# Remaining roadmap

|Next|PR|Layer|Goal|
|---|---|---|---|
|✅ next|**PR4**|Proof|Candidate source/fact kernel|
|5|PR5|Proof|CareerKnowledge static rules + resolver|
|6|PR6|Proof|Candidate evidence persistence|
|7|PR7|Proof|EvidenceGraph shadow|
|8|PR8|Product value|ResumeVariantPlan artifact|
|9|PR9|Product value|Minimal review cockpit|
|10|PR10|Product value|Resume variant artifact|
|11|PR11|Product value|Cover-letter artifact adapter|
|12|PR12|Product value|ApplicationPackageV1|
|13|PR13|Distribution|Internal tool contracts|
|14|PR14|Distribution|Controlled ATS Scout adapters|
|15|PR15|Distribution|Local MCP beta|
|16|PR16|Distribution|Remote MCP / ChatGPT App exploration|