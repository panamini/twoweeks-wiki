```
CONTEXT.RUNS.FINGERPRINTS.IDEMPOTENCY.NO UI.NO MCP.NO GENERATION REWRITE.
```
**Twoweeks should be the data engine agents use to create truthful, tailored job applications.**

Career knowledge becomes **PR 2**, after the durable execution foundation exists.

---

# Final ideal plan for Twoweeks

## The product thesis

Twoweeks should become:

> **The trusted application harness agents use to prepare truthful, tailored job applications.**

Not:

```
AI resume builderAI cover letter generatorJob trackerTemplate editor
```

But:

```
Job page→ ApplicationContext→ EvidenceGraph→ truthful draft→ resume patch plan→ human review→ approved export→ tracked application
```

Your repo already says the active product path is CV ingestion/parsing, canonical saved profile/CV data, and personalized proposal generation. Your wiki also says Twoweeks is the product truth, while CVForge and ProposalForge are internal module names, and canonical CV truth should flow through structured sections.

So the plan should **not rebuild the app**. It should add an orchestration layer above the current modules.

---

# The architecture

```
APPLICATION CONTEXT.RUN LEDGER.ARTIFACTS.EVENTS.CAREER KNOWLEDGE.EVIDENCE GRAPH.INTERNAL TOOLS.REVIEW UI.THEN MCP.
```

This is the right order.

MCP should come late because MCP is a standard way for LLM apps to connect to external data and tools, but it also introduces trust/safety requirements around user consent, tool execution, and data access. The MCP spec explicitly separates resources, prompts, and tools, and says users should retain control over shared data and actions.

Codex should be used immediately, because Codex reads `AGENTS.md` before doing work and layers global/project/directory instructions, which fits your repo discipline perfectly. Your repo’s own `AGENTS.md` already says to prefer small, testable, reversible changes and avoid broad rewrites.

---

# Correct module structure

```
my-app/src/modules/application-context/  schema.ts  domain.ts  buildApplicationContextV1.ts  fingerprints.ts  selectors.ts  readiness.ts  __tests__/my-app/src/modules/application-runs/  schema.ts  idempotency.ts  createRun.ts  completeRun.ts  failRun.ts  __tests__/my-app/src/modules/application-artifacts/  schema.ts  coverLetterArtifact.ts  resumePatchArtifact.ts  exportArtifact.tsmy-app/src/modules/application-events/  schema.ts  recordEvent.tsmy-app/src/modules/career-knowledge/  standards.schema.ts  harvardResumeRules.ts  coverLetterRules.ts  atsRules.ts  globalCvRules.ts  layoutRules.ts  ruleResolver.ts  claimRules.ts  __tests__/my-app/src/modules/evidence-graph/  schema.ts  buildEvidenceGraph.ts  claimValidator.ts  riskFlags.tsmy-app/src/modules/agent-tools/  toolContracts.ts  twCreateApplicationContext.ts  twDraftCoverLetter.ts  twPlanResumePatches.ts  twExplainEvidence.ts  twExportArtifact.ts  twTrackApplication.ts  mcpAdapter.ts      // latermy-app/src/modules/application-review/  ApplicationReviewPage.tsx  EvidencePanel.tsx  ResumePatchDiff.tsx  RiskFlags.tsx  ArtifactPreview.tsx
```

Convex side:

```
my-app/convex/applicationContexts.tsmy-app/convex/applicationRuns.tsmy-app/convex/applicationArtifacts.tsmy-app/convex/applicationEvents.ts
```

The uploaded plan already points toward this module split. I agree with the structure, but I would **delay `mcpAdapter.ts` until PR 6**.

---

# The key data model

## `ApplicationContextV1`

```
type ApplicationContextV1 = {  id: string;  userId: string;  job: {    jobId: string;    sourceUrl?: string;    rawTextHash: string;    title?: string;    company?: string;    rawDescription?: string;    extractedRequirements: RequirementV1[];  };  candidate: {    cvId: string;    cvSnapshotHash: string;    structuredSectionsHash: string;    selectedTemplateId?: string;    selectedLanguage?: string;  };  evidence: {    evidenceGraphId?: string;    matched: EvidenceMatchV1[];    missing: MissingRequirementV1[];    riskyClaims: RiskFlagV1[];  };  artifacts: {    coverLetterArtifactId?: string;    resumePatchArtifactId?: string;    exportArtifactIds: string[];  };  review: {    state:      | "draft"      | "needs_review"      | "approved"      | "exported"      | "tracked";    approvedAt?: number;    approvedBy?: string;  };  fingerprints: {    contextHash: string;    jobHash: string;    cvHash: string;    settingsHash: string;  };  version: 1;  createdAt: number;  updatedAt: number;};
```

## `ApplicationRunV1`

```
type ApplicationRunV1 = {  id: string;  userId: string;  contextId: string;  operation:    | "build_context"    | "build_evidence_graph"    | "draft_cover_letter"    | "plan_resume_patches"    | "export_pdf"    | "track_application";  idempotencyKey: string;  inputHash: string;  status: "queued" | "running" | "succeeded" | "failed";  attemptCount: number;  scheduledFunctionId?: string;  resultArtifactIds?: string[];  error?: string;  createdAt: number;  updatedAt: number;};
```

This is the most important part. Without `ApplicationRunV1`, agents will repeat actions, duplicate drafts, overwrite user edits, and make debugging impossible.

Convex supports durable workflows through scheduled functions stored in the database; scheduling from mutations is atomic with the mutation, while actions are not atomic and can have side effects. Convex also distinguishes shallow `db.patch` updates from full `db.replace`, so metadata/state changes should patch rather than replace whole documents.

---

# The corrected PR order

## PR 1 — Foundation only

**Goal:** Build the durable skeleton. No UI. No MCP. No generation rewrite.

```
ApplicationContextV1ApplicationRunV1fingerprintsidempotency keysConvex tablescreate/get/update helpersunit testsdecision doc
```

### Acceptance tests

```
same CV + same job → same context fingerprintchanged CV → changed CV hashchanged job → changed job hashsame operation input → same idempotency keysame build twice → no duplicate logical contextbuildApplicationContextV1 does not mutate input objects
```

This is the first Codex task.

---

## PR 2 — Career knowledge + standards

**Goal:** Make the agent smarter without stuffing PDFs into prompts every time.

```
career-knowledge/  Harvard resume rules  cover-letter rules  ATS-safe rules  global CV rules  layout rules  claim rules  market resolver
```

The structure from your friend’s plan is right: rules should become typed data, not random prompt text.

Example:

```
type CareerRule = {  id: string;  sourceId: string;  market: "us" | "fr" | "uk" | "eu" | "global";  documentType: "resume" | "cv" | "cover_letter" | "proposal";  severity: "must" | "should" | "advisory";  rule: string;  validatorKey?: string;};
```

---

## PR 3 — EvidenceGraphV1

**Goal:** Make proof the moat.

```
Job requirement→ matched CV evidence→ source section→ source text→ confidence→ allowed claim→ risky / missing / unsupported
```

This should run **before** the writer. The writer should not invent claims. It should consume allowed claims.

```
type EvidenceGraphV1 = {  id: string;  contextId: string;  requirements: Array<{    id: string;    text: string;    type: "hard" | "soft" | "nice_to_have";    source: "job_post" | "manual" | "inferred";  }>;  matches: Array<{    requirementId: string;    cvSectionId: string;    cvItemId?: string;    sourceText: string;    confidence: number;    allowedClaim: string;  }>;  missing: Array<{    requirementId: string;    reason: "no_evidence" | "weak_evidence" | "ambiguous";  }>;  riskFlags: Array<{    claim: string;    severity: "low" | "medium" | "high";    reason: string;  }>;  version: 1;};
```

This matches the best part of your friend’s plan: Twoweeks should generate “apply with proof, not slop.”

---

## PR 4 — One deterministic generation path

**Goal:** One boringly reliable path from saved job + CV to cover letter artifact.

```
saved job + selected CV→ ApplicationContextV1→ EvidenceGraphV1→ allowed claim plan→ cover letter artifact→ hard refresh→ same artifact still exists
```

No resume patch UI yet. No MCP yet. No auto-apply.

---

## PR 5 — Minimal review UI

**Goal:** Human supervision surface.

```
Application BriefEvidence MatchMissing RequirementsRisk FlagsCover Letter ArtifactResume Patch PlanApproveExportTrack
```

The UI is not another editor. It is an approval cockpit.

```
REVIEW.APPROVE.EXPORT.DONE.
```

MCP trust/safety guidance supports this: tools and data access need user understanding, authorization, and control.

---

## PR 6 — Internal tool contracts

**Goal:** Make Twoweeks callable internally before external MCP.

```
tw_create_application_contexttw_get_application_contexttw_build_evidence_graphtw_draft_cover_lettertw_plan_resume_patchestw_explain_evidencetw_export_artifacttw_track_application
```

Each tool needs:

```
type ToolContract = {  name: string;  inputSchema: ZodSchema;  outputSchema: ZodSchema;  idempotencyKey: string;  requiresApproval: boolean;  writes: boolean;};
```

Rules:

```
draft = okayexplain = okayprepare = okayexport = approval requiredtrack = approval requiredapply/send/submit = forbidden for now
```

---

## PR 7 — Local MCP beta

Only after PR 1–6 are stable.

MCP is the adapter, not the core. MCP servers expose resources, prompts, and tools to LLM clients. Your internal tool contracts should map cleanly into MCP later.

```
Twoweeks internal tool→ MCP tool wrapper→ local Codex / Claude / ChatGPT connector
```

No remote MCP yet.

---

## PR 8 — Remote MCP / ChatGPT App exploration

Only after the local MCP beta works.

OpenAI’s Apps SDK is the future distribution layer for ChatGPT apps; it includes MCP apps, MCP server setup, UI, auth, state, deployment, and submission. But it is **not** the foundation. It is the final packaging layer.

---

# Timeline

|Phase|Time solo + Codex|Difficulty|Output|
|---|---|---|---|
|PR 1 foundation|2–4 days|Medium|Context + runs + idempotency|
|PR 2 knowledge|2–3 days|Medium|Typed career rules|
|PR 3 evidence graph|3–5 days|Hard|Claim-safe matching|
|PR 4 deterministic generation|3–5 days|Hard|One reload-safe artifact path|
|PR 5 review UI|4–7 days|Medium-hard|Approval cockpit|
|PR 6 internal tools|2–4 days|Medium|Tool contracts|
|PR 7 local MCP beta|4–7 days|Hard|Agent bridge|
|PR 8 remote MCP / Apps SDK|2–4 weeks|Very hard|Distribution layer|

## Realistic total

```
2 weeks = architecture foundation + first deterministic path4–6 weeks = real production V18–12 weeks = agent-native platform
```

Your friend’s timing is realistic.

---

# The exact first Codex prompt

Use this first. Not the whole giant plan. Start narrow.

```
Context:You are working in panamini/neyssan. Read AGENTS.md first. Treat v1 as the active baseline. This task is additive architecture only.Twoweeks is evolving from a human-first resume/cover-letter app into an agent-native job application harness.Core product thesis:Twoweeks should become the trusted context engine agents use to prepare truthful, tailored job applications.Current product truth:- CV ingestion/parsing, canonical saved profile/CV data, and personalized proposal generation are the core flow.- Canonical CV truth should prefer currentCv.sections[*].structuredContent when available.- Existing CV Forge, Proposal Forge, Job Library, export, and tracker flows must remain working.- Do not reshape existing surfaces in this PR.Goal:Implement the additive foundation for ApplicationContextV1 and ApplicationRunV1 so future agent tools can build on stable, idempotent, replayable application workflows.Scope:Allowed:- Add a new module under my-app/src/modules/application-context/- Add a new module under my-app/src/modules/application-runs/- Add matching Convex files for applicationContexts and applicationRuns- Add deterministic fingerprints and idempotency helpers- Add focused unit tests- Add one short decision docForbidden:- No UI work- No public MCP server- No ChatGPT App- No export rewrite- No parser rewrite- No proposal editor rewrite- No CV editor rendering changes- No broad folder migration- No opportunistic cleanup- No direct resume rewriting- No auto-apply / auto-send / auto-submitRequired work:1. Audit active code paths for:   - CV structuredContent source   - saved job source   - proposal metadata source   - existing match/evidence structures   - existing test conventions2. Define ApplicationContextV1:   - id   - userId   - job   - candidate   - evidence placeholder   - artifacts placeholder   - review state   - fingerprints   - version   - createdAt   - updatedAt3. Define ApplicationRunV1:   - id   - userId   - contextId   - operation   - idempotencyKey   - inputHash   - status   - attemptCount   - resultArtifactIds   - error   - createdAt   - updatedAt4. Add fingerprint helpers:   - stable hash for CV snapshot   - stable hash for structured sections   - stable hash for job raw text   - stable hash for operation input   - stable idempotency key builder5. Add Convex tables/functions:   - applicationContexts   - applicationRuns   - create/get/update helpers   - indexed lookup by userId + fingerprint / idempotencyKey where appropriate6. Add buildApplicationContextV1():   - reads existing CV/job records   - does not mutate existing records   - prefers structuredContent over legacy arrays   - preserves source URL and raw description when available   - preserves evidence/provenance placeholders when available   - returns deterministic output7. Add tests proving:   - same CV/job input produces same fingerprints   - changing CV changes CV hash   - changing job text changes job hash   - same operation input produces same idempotency key   - ApplicationContextV1 can be built without mutating input objects   - running same build twice returns/reuses same logical context rather than duplicating work8. Add docs/decisions/YYYY-MM-DD-application-context-v1.md explaining:   - why this is additive   - why ApplicationRunV1 exists   - what is deferred   - why MCP is not part of this PRConstraints:- Smallest safe change.- No broad refactor.- All writes must be idempotent or explicitly explain why not.- Prefer metadata/state patching over full document replacement.- Keep old flows untouched.- Use existing project scripts/tests where possible.Acceptance criteria:- TypeScript passes for changed files.- New focused tests pass.- Existing relevant tests still pass or any failure is clearly unrelated.- Convex schema compiles.- No existing user route behavior changes.- No UI changed.- No public MCP added.Final report must include:- Short audit summary- Files changed- Tests run- What was verified- What remains deferred- Next smallest PR
```

---

# My final answer

Your friend is right on the merged direction.

But the **ideal plan** is this:

```
DO NOT REBUILD.DO NOT START WITH MCP.DO NOT START WITH UI.BUILD THE HARNESS.1. ApplicationContextV12. ApplicationRunV13. ApplicationArtifactV14. ApplicationEventV15. CareerKnowledge6. EvidenceGraphV17. Review UI8. Internal tools9. Local MCP10. Remote MCP / ChatGPT App
```

The first move is **PR 1 only**. Keep it boring. Keep it additive. Make the app idempotent before making it agentic.

Write `suite` and I’ll give you the **exact Codex prompts for PR 2 → PR 8**.

suite

I’ll continue with the promised PR 2 → PR 8 prompts. I’ll keep them copy-pasteable for Codex and keep the sequencing strict: foundation first, intelligence second, MCP last.

Thought for 31s

Parfait — voici la **suite complète**: les prompts Codex pour **PR 2 → PR 8**, dans l’ordre idéal.

I’m keeping the structure from your friend’s merged plan — **context, runs, knowledge, evidence, tools, review, then MCP** — but sequenced more safely: PR 1 is already foundation; PR 2 starts the career knowledge harness; MCP only comes after internal tools are stable. Your friend’s uploaded plan is directionally right because it adds the missing execution harness and domain harness instead of just one `ApplicationContext` object.

The outside docs support this sequencing: Codex is designed to use repo instructions like `AGENTS.md`, MCP separates tools/resources/prompts for agent integrations, Convex scheduled functions/actions need durable patterns for side-effectful workflows, and OpenAI Apps SDK is a later distribution layer for ChatGPT apps, not the first foundation.

---

# Master sequence

```
PR 1 — ApplicationContextV1 + ApplicationRunV1 foundationPR 2 — CareerKnowledge rules harnessPR 3 — EvidenceGraphV1 + claim validatorPR 4 — deterministic cover-letter artifact pathPR 5 — minimal Application Review UIPR 6 — internal agent-tool contractsPR 7 — local MCP betaPR 8 — remote MCP / ChatGPT App exploration
```

---

# PR 2 — Career knowledge harness

## Goal

Turn your Harvard/ATS/CV/cover-letter knowledge into **typed rules** that the app can use consistently.

Do **not** feed PDFs/raw docs to the model every time. Convert them into a stable module:

```
career-knowledge→ rules→ validators→ market resolver→ generation constraints
```

## Codex prompt

```
Context:You are working in panamini/neyssan. Read AGENTS.md first. Treat v1 as the active baseline.PR 1 should already have introduced the additive ApplicationContextV1 and ApplicationRunV1 foundation. This PR must build on that foundation without changing existing CV Forge, Proposal Forge, parser, export, tracker, or editor behavior.Twoweeks is becoming an agent-native job application harness. The next missing layer is not more generation. It is a career-knowledge standards module that turns resume, CV, ATS, cover-letter, layout, and evidence rules into typed reusable constraints.Goal:Add a career-knowledge module that stores structured writing/layout/ATS rules for resumes, CVs, cover letters, and proposals. This module should be used later by EvidenceGraphV1 and generation tools, but this PR must not rewrite generation yet.Scope:Allowed:- Add my-app/src/modules/career-knowledge/- Add TypeScript rule schemas- Add static rule sets for US resume, cover letter, ATS, global CV, layout, and claim safety- Add a rule resolver- Add tests for rule filtering and deterministic resolution- Add one decision docForbidden:- No generation rewrite- No prompt rewrite except adding deferred TODO notes if necessary- No UI work- No MCP work- No parser changes- No CV editor or Proposal editor changes- No export changes- No migration of existing app folders- No importing raw PDFs into runtime prompts- No broad cleanupRequired files:Create:my-app/src/modules/career-knowledge/standards.schema.tsmy-app/src/modules/career-knowledge/harvardResumeRules.tsmy-app/src/modules/career-knowledge/coverLetterRules.tsmy-app/src/modules/career-knowledge/atsRules.tsmy-app/src/modules/career-knowledge/globalCvRules.tsmy-app/src/modules/career-knowledge/layoutRules.tsmy-app/src/modules/career-knowledge/claimRules.tsmy-app/src/modules/career-knowledge/ruleResolver.tsmy-app/src/modules/career-knowledge/__tests__/ruleResolver.test.tsdocs/decisions/YYYY-MM-DD-career-knowledge-v1.mdDefine:type CareerRule = {  id: string;  sourceId: string;  sourceLabel: string;  market: "us" | "fr" | "uk" | "eu" | "global";  documentType: "resume" | "cv" | "cover_letter" | "proposal";  category:    | "structure"    | "content"    | "ats"    | "layout"    | "tone"    | "claim_safety"    | "evidence"    | "export";  severity: "must" | "should" | "advisory";  rule: string;  rationale?: string;  validatorKey?: string;  appliesTo?: Array<    | "profile"    | "summary"    | "experience"    | "education"    | "skills"    | "languages"    | "achievements"    | "cover_letter_opening"    | "cover_letter_body"    | "cover_letter_closing"    | "resume_patch"    | "export"  >;};Add rule sets:1. Harvard-style US resume rules:   - concise, tailored, strongest assets first   - scan-friendly for humans and ATS   - action verbs and concrete outcomes   - no personal pronouns   - no photos/age/gender/reference lines   - bullets should be specific and evidence-based2. Cover-letter rules:   - why them / why you / closing structure   - one page max   - concrete examples from resume/CV   - not flowery, not generic   - job description skills connected to candidate evidence3. ATS rules:   - plain section headings   - explicit skills   - avoid text boxes and overly decorative structures for ATS-oriented templates   - preserve readable chronology   - no unsupported keyword stuffing4. Global CV rules:   - market-aware distinction between US resume and global CV   - document type controls layout and content expectations   - do not apply US-only constraints blindly to all markets5. Layout rules:   - export truth is final generated PDF/DOCX output, not preview DOM alone   - layout changes must preserve print/export correctness   - templates must not destroy content hierarchy6. Claim safety rules:   - no unsupported credentials   - no invented employers, degrees, dates, quantified outcomes, languages, tools, or certifications   - unsupported job requirements must become missing/risk flags, not invented claimsImplement:resolveCareerRules(input: {  market: CareerRule["market"];  documentType: CareerRule["documentType"];  categories?: CareerRule["category"][];  appliesTo?: NonNullable<CareerRule["appliesTo"]>[number][];  includeAdvisory?: boolean;}): CareerRule[]Rules:- Deterministic order.- "global" rules may apply alongside market-specific rules.- "must" and "should" included by default.- "advisory" included only when includeAdvisory is true.- No duplicate rule ids.Tests:- resolves US resume rules with global rules- excludes advisory rules by default- includes advisory rules when requested- filters by documentType- filters by category- filters by appliesTo- produces deterministic order- no duplicate ids across all rule setsDocs:The decision doc must explain:- why career knowledge is structured data, not raw prompt stuffing- why this module is additive- how it will later connect to EvidenceGraphV1 and generation- what is deferredAcceptance criteria:- New tests pass.- TypeScript passes for changed files.- No existing route behavior changes.- No UI changed.- No generation output changed in this PR.- No MCP added.Final report:- Files changed- Tests run- What was verified- What remains deferred- Next smallest PR
```

---

# PR 3 — EvidenceGraphV1 + claim validator

## Goal

Make proof first-class:

```
job requirement→ CV evidence→ allowed claim→ risk/missing flag
```

This is your moat. It prevents generic AI slop.

## Codex prompt

```
Context:You are working in panamini/neyssan. Read AGENTS.md first. Treat v1 as the active baseline.PR 1 should have added ApplicationContextV1/ApplicationRunV1.PR 2 should have added career-knowledge typed rules.This PR adds EvidenceGraphV1. It must not rewrite generation yet. It should prepare a structured proof layer that future writers and resume patch planners can consume.Goal:Implement EvidenceGraphV1 and a basic claim validator that maps job requirements to candidate evidence from the selected CV, produces allowed claims, and flags missing/unsupported/risky claims.Scope:Allowed:- Add my-app/src/modules/evidence-graph/- Add EvidenceGraphV1 schema/types- Add buildEvidenceGraphV1()- Add claimValidator.ts- Add riskFlags.ts- Add tests using small mocked CV/job/context fixtures- Add a decision docForbidden:- No UI work- No MCP work- No export changes- No parser changes- No proposal editor changes- No CV editor rendering changes- No broad refactor- No direct resume rewrite- No generation rewrite except optional narrow adapter TODOs- No auto-apply / auto-send / auto-submitRequired files:Create:my-app/src/modules/evidence-graph/schema.tsmy-app/src/modules/evidence-graph/buildEvidenceGraph.tsmy-app/src/modules/evidence-graph/claimValidator.tsmy-app/src/modules/evidence-graph/riskFlags.tsmy-app/src/modules/evidence-graph/__tests__/buildEvidenceGraph.test.tsmy-app/src/modules/evidence-graph/__tests__/claimValidator.test.tsdocs/decisions/YYYY-MM-DD-evidence-graph-v1.mdDefine:type EvidenceRequirementV1 = {  id: string;  text: string;  normalizedText: string;  type: "hard" | "soft" | "nice_to_have";  source: "job_post" | "manual" | "inferred";  confidence: number;};type EvidenceMatchV1 = {  id: string;  requirementId: string;  cvSectionId: string;  cvItemId?: string;  sourceSectionType?: string;  sourceText: string;  confidence: number;  allowedClaim: string;};type MissingRequirementV1 = {  id: string;  requirementId: string;  reason: "no_evidence" | "weak_evidence" | "ambiguous";  note: string;};type RiskFlagV1 = {  id: string;  severity: "low" | "medium" | "high";  claim?: string;  requirementId?: string;  reason:    | "unsupported_claim"    | "weak_evidence"    | "exact_number_missing"    | "credential_missing"    | "date_mismatch"    | "language_missing"    | "tool_missing"    | "market_rule_violation";  note: string;};type EvidenceGraphV1 = {  id: string;  contextId: string;  userId: string;  requirements: EvidenceRequirementV1[];  matches: EvidenceMatchV1[];  missing: MissingRequirementV1[];  riskFlags: RiskFlagV1[];  sourceHashes: {    contextHash: string;    jobHash: string;    cvHash: string;    rulesHash: string;  };  version: 1;  createdAt: number;  updatedAt: number;};Implement:buildEvidenceGraphV1(input: {  context: ApplicationContextV1;  cvDocument: unknown;  careerRules: CareerRule[];}): EvidenceGraphV1Rules:- Prefer currentCv.sections[*].structuredContent when available.- Extract candidate evidence from summary, experience, skills, education, languages, achievements.- Use deterministic ids derived from contextId + requirement/cv evidence fingerprint.- Do not invent evidence.- If a job requirement has no CV support, create MissingRequirementV1.- If support is weak, create both a low/medium confidence match and a risk flag.- If a claim contains exact numbers, credentials, dates, languages, tools, or certifications not found in evidence, flag it.- Allowed claims must be conservative and derived from source text.Implement claimValidator:validateClaimAgainstEvidence(input: {  claim: string;  evidenceTexts: string[];  careerRules: CareerRule[];}): {  allowed: boolean;  riskFlags: RiskFlagV1[];}Minimum validation:- exact number appears in claim but not evidence → risk- credential/certification appears in claim but not evidence → risk- language appears in claim but not evidence → risk- named tool appears in claim but not evidence → risk- employer/school appears in claim but not evidence → riskTests:- matched requirement produces EvidenceMatchV1- missing requirement produces MissingRequirementV1- weak evidence produces risk flag- exact number not in CV is flagged- credential not in CV is flagged- language not in CV is flagged- deterministic output for same input- changing CV source text changes sourceHashes/cvHash- build does not mutate input context or CVDocs:Decision doc must explain:- EvidenceGraphV1 is a proof layer, not a writer- writers must consume allowed claims later- missing evidence must not become invented content- this PR intentionally avoids UI and MCPAcceptance criteria:- New tests pass.- TypeScript passes for changed files.- No user-facing route behavior changes.- No generation behavior changes unless explicitly isolated and tested.- No UI changed.- No MCP added.Final report:- Files changed- Tests run- What was verified- What remains deferred- Next smallest PR
```

---

# PR 4 — One deterministic cover-letter artifact path

## Goal

Wire one safe path:

```
saved job + selected CV→ ApplicationContextV1→ EvidenceGraphV1→ cover letter artifact→ reload proof
```

Not all surfaces. One deterministic path only.

## Codex prompt

```
Context:You are working in panamini/neyssan. Read AGENTS.md first. Treat v1 as the active baseline.PR 1 added ApplicationContextV1/ApplicationRunV1.PR 2 added career-knowledge rules.PR 3 added EvidenceGraphV1 and claim validation.This PR wires one deterministic generation path for cover-letter artifacts. Do not change the full proposal editor architecture. Do not rewrite all generation. Add a narrow adapter that saves an artifact connected to ApplicationContextV1 and EvidenceGraphV1.Goal:Create one reload-safe, idempotent path:saved job + selected CV→ ApplicationContextV1→ EvidenceGraphV1→ cover letter artifact→ hard refresh→ same artifact can be recoveredScope:Allowed:- Add my-app/src/modules/application-artifacts/- Add CoverLetterArtifactV1 type- Add Convex applicationArtifacts table/functions if not already present- Add a narrow adapter that calls existing proposal/cover-letter generation using context/evidence inputs- Add idempotent run integration through ApplicationRunV1- Add focused tests- Add one decision docForbidden:- No full ProposalDisplay rewrite- No CV editor rewrite- No export rewrite- No template system rewrite- No MCP work- No review UI yet- No auto-apply / auto-send / auto-submit- No broad prompt overhaul- No destructive regeneration that overwrites user editsRequired files:Create or update:my-app/src/modules/application-artifacts/schema.tsmy-app/src/modules/application-artifacts/coverLetterArtifact.tsmy-app/src/modules/application-artifacts/__tests__/coverLetterArtifact.test.tsmy-app/convex/applicationArtifacts.tsdocs/decisions/YYYY-MM-DD-cover-letter-artifact-v1.mdDefine:type ApplicationArtifactV1 = {  id: string;  userId: string;  contextId: string;  runId: string;  type: "cover_letter" | "resume_patch" | "export";  status: "draft" | "needs_review" | "approved" | "superseded";  title: string;  content: unknown;  textPreview?: string;  sourceHashes: {    contextHash: string;    evidenceGraphHash?: string;    generatorInputHash: string;  };  provenance: {    cvId: string;    jobId: string;    evidenceGraphId?: string;    generatorName?: string;    modelName?: string;  };  createdAt: number;  updatedAt: number;  version: 1;};Implement:createOrReuseCoverLetterArtifact(input: {  userId: string;  context: ApplicationContextV1;  evidenceGraph: EvidenceGraphV1;  generationSettings: unknown;}): Promise<ApplicationArtifactV1>Rules:- Build an idempotency key from userId + contextHash + evidenceGraphHash + generationSettingsHash + operation.- If an artifact already exists for the same idempotency key/input hash, reuse it.- If inputs change, create a new artifact and do not overwrite old user-reviewed artifacts.- Artifact content should preserve enough structured metadata for preview/export later.- The adapter should pass allowed claims and missing/risk flags into the existing writer path where possible.- If the existing writer path cannot consume the full EvidenceGraph yet, add a narrow translation layer and document the limitation.Tests:- same context/evidence/settings reuses same logical artifact- changed evidence creates new artifact- changed generation settings creates new artifact- approved artifact is not overwritten by regenerate- artifact stores provenance cvId/jobId/contextId/runId- artifact stores source hashes- no input mutationOptional focused integration test:- build mocked context + mocked evidence graph + fake writer → artifact saved/reused deterministicallyDocs:Decision doc must explain:- why artifacts are separate from proposal editor state- why regeneration creates new artifacts instead of destructive overwrite- how this prepares review UI and export- what is deferredAcceptance criteria:- Tests pass.- TypeScript passes for changed files.- Convex schema compiles.- Existing Proposal Forge route behavior remains unchanged.- No UI changed except optional hidden/internal route if absolutely needed.- No MCP added.Final report:- Files changed- Tests run- What was verified- What remains deferred- Next smallest PR
```

---

# PR 5 — Minimal Application Review UI

## Goal

Create the approval cockpit.

Not a giant editor. Not another dashboard.

```
Brief.Evidence.Risks.Draft.Approve.Export.Track.
```

## Codex prompt

```
Context:You are working in panamini/neyssan. Read AGENTS.md first. Treat v1 as the active baseline.PR 1 added ApplicationContextV1/ApplicationRunV1.PR 2 added career-knowledge.PR 3 added EvidenceGraphV1.PR 4 added deterministic cover-letter artifacts.This PR adds a minimal Application Review UI. It must not replace CV Forge or Proposal Forge. It should be an additive review surface for one ApplicationContextV1.Goal:Create a minimal review cockpit where the user can inspect:- job/application brief- evidence matches- missing requirements- risk flags- cover letter artifact- resume patch placeholder- approve/export/track actions as controlled statesScope:Allowed:- Add my-app/src/modules/application-review/- Add a route only if the app routing pattern supports it safely- Add small read-only components for EvidencePanel, RiskFlags, ArtifactPreview- Add approve action for artifact/context review state- Add tests for components or state logic- Add one decision docForbidden:- No full editor replacement- No CV Forge rewrite- No Proposal Forge rewrite- No export rewrite- No MCP- No auto-apply / auto-send / auto-submit- No broad styling redesign- No large animation/polish pass- No destructive artifact mutationRequired files:Create:my-app/src/modules/application-review/ApplicationReviewPage.tsxmy-app/src/modules/application-review/ApplicationBrief.tsxmy-app/src/modules/application-review/EvidencePanel.tsxmy-app/src/modules/application-review/RiskFlags.tsxmy-app/src/modules/application-review/ArtifactPreview.tsxmy-app/src/modules/application-review/ResumePatchPlaceholder.tsxmy-app/src/modules/application-review/reviewState.tsmy-app/src/modules/application-review/__tests__/reviewState.test.tsxdocs/decisions/YYYY-MM-DD-application-review-v1.mdUI contract:Page sections:1. Application Brief   - job title/company/source URL when available   - selected CV title/id   - current review state2. Evidence Match   - matched requirements   - source section/source text   - confidence3. Missing Requirements   - requirement text   - reason4. Risk Flags   - severity   - reason   - note5. Cover Letter Artifact   - text preview   - status   - provenance6. Resume Patch Plan   - placeholder only if not implemented   - do not pretend patches exist if they do not7. Actions   - Approve   - Export placeholder or disabled if export is not wired   - Track placeholder or disabled if tracker is not wiredRules:- Review UI is read-first.- Approval is explicit.- Export/track actions must require approved state, or stay disabled with a clear reason.- No apply/send/submit action.- Do not invent evidence in the UI.- Show missing/risky evidence clearly.- If data is unavailable, show honest empty states.Implementation:- Prefer existing design tokens/components.- Keep styling minimal.- Do not introduce a new design system.- Avoid complex animations.- Do not break existing routes.Tests:- risk flags render with severity- missing requirements render honestly- approve transition changes review state- export disabled before approval- no resume patch content shown when no patch artifact exists- component handles absent source URL without crashingDocs:Decision doc must explain:- review UI is supervision surface, not primary editor- approval before export/track- why auto-apply is intentionally absent- what is deferredAcceptance criteria:- Tests pass.- TypeScript passes.- Existing routes still work.- Minimal review route renders with mocked data or existing data path.- No MCP added.- No export rewrite.- No editor rewrite.Final report:- Files changed- Tests run- What was verified- What remains deferred- Next smallest PR
```

---

# PR 6 — Internal tool contracts

## Goal

Create Twoweeks tools **inside the app first**, before MCP.

```
tw_create_application_contexttw_get_application_contexttw_build_evidence_graphtw_draft_cover_lettertw_plan_resume_patchestw_explain_evidencetw_export_artifacttw_track_application
```

No public MCP yet.

## Codex prompt

```
Context:You are working in panamini/neyssan. Read AGENTS.md first. Treat v1 as the active baseline.PR 1 added ApplicationContextV1/ApplicationRunV1.PR 2 added career-knowledge.PR 3 added EvidenceGraphV1.PR 4 added cover-letter artifacts.PR 5 added a minimal review UI.This PR adds internal agent-tool contracts. These are not public MCP tools yet. They are typed internal functions with input/output schemas, idempotency behavior, and approval requirements.Goal:Define stable internal Twoweeks tool contracts so future Codex/MCP/ChatGPT integrations can call Twoweeks through safe, typed operations.Scope:Allowed:- Add my-app/src/modules/agent-tools/- Add tool contract schemas- Add internal tool wrappers for existing modules- Add approval metadata- Add tests for schema validation and idempotency fields- Add one decision docForbidden:- No public MCP server- No remote MCP- No ChatGPT App- No auto-apply / auto-send / auto-submit- No new UI except optional dev-only documentation route if existing pattern supports it- No editor rewrite- No export rewrite beyond calling existing approved export path if already available- No generation rewriteRequired files:Create:my-app/src/modules/agent-tools/toolContracts.tsmy-app/src/modules/agent-tools/twCreateApplicationContext.tsmy-app/src/modules/agent-tools/twGetApplicationContext.tsmy-app/src/modules/agent-tools/twBuildEvidenceGraph.tsmy-app/src/modules/agent-tools/twDraftCoverLetter.tsmy-app/src/modules/agent-tools/twPlanResumePatches.tsmy-app/src/modules/agent-tools/twExplainEvidence.tsmy-app/src/modules/agent-tools/twExportArtifact.tsmy-app/src/modules/agent-tools/twTrackApplication.tsmy-app/src/modules/agent-tools/__tests__/toolContracts.test.tsdocs/decisions/YYYY-MM-DD-internal-agent-tools-v1.mdDefine:type TwoweeksToolName =  | "tw_create_application_context"  | "tw_get_application_context"  | "tw_build_evidence_graph"  | "tw_draft_cover_letter"  | "tw_plan_resume_patches"  | "tw_explain_evidence"  | "tw_export_artifact"  | "tw_track_application";type TwoweeksToolContract = {  name: TwoweeksToolName;  description: string;  inputSchema: z.ZodTypeAny;  outputSchema: z.ZodTypeAny;  operation: ApplicationRunV1["operation"];  writes: boolean;  requiresApproval: boolean;  idempotent: boolean;  riskLevel: "low" | "medium" | "high";};Rules:- Draft/explain/build operations may run without approval.- Export requires approved artifact/context.- Track requires explicit approval.- Apply/send/submit must not exist.- Every write operation must define idempotency input fields.- Tool descriptions must be compact, specific, and not vague.- Tool outputs must be structured, not free-form strings only.Implement contracts:1. tw_create_application_context   - input: cvId, jobId, optional settings   - output: contextId, contextHash, reviewState2. tw_get_application_context   - input: contextId   - output: ApplicationContextV1 summary3. tw_build_evidence_graph   - input: contextId   - output: evidenceGraphId, counts for matches/missing/riskFlags4. tw_draft_cover_letter   - input: contextId, evidenceGraphId, generationSettings   - output: artifactId, status, textPreview5. tw_plan_resume_patches   - input: contextId, evidenceGraphId   - output: patchArtifactId or explicit notImplemented/deferred status if not implemented   - must not silently rewrite CV6. tw_explain_evidence   - input: contextId or evidenceGraphId   - output: matched/missing/risk summary7. tw_export_artifact   - input: artifactId, format   - output: exportArtifactId or blocked reason   - requires approval8. tw_track_application   - input: contextId, status   - output: tracking status or blocked reason   - requires approvalTests:- every tool has description/inputSchema/outputSchema- every write tool is idempotent or explicitly blocked- export requires approval- track requires approval- no forbidden tool names include apply/send/submit- schemas reject invalid input- descriptions are non-empty and specific- tool registry order is deterministicDocs:Decision doc must explain:- internal tools come before MCP- tool contracts are the stable API boundary- approval requirements- why auto-apply is excluded- what is deferredAcceptance criteria:- Tests pass.- TypeScript passes.- No public MCP added.- No existing UI behavior changes.- No editor/export/generation rewrite.Final report:- Files changed- Tests run- What was verified- What remains deferred- Next smallest PR
```

---

# PR 7 — Local MCP beta

## Goal

Expose only the stable internal tools through a **local MCP adapter**.

Not remote. Not public. No production auth yet.

## Codex prompt

```
Context:You are working in panamini/neyssan. Read AGENTS.md first. Treat v1 as the active baseline.PR 6 added internal agent-tool contracts. This PR adds a local-only MCP beta adapter for those contracts.MCP is an adapter layer, not the core architecture. Do not rewrite internal tools to fit MCP. Wrap the stable internal tool contracts.Goal:Create a local-only MCP beta server/adapter that exposes a safe subset of Twoweeks internal tools for local agent testing.Scope:Allowed:- Add a local MCP adapter under my-app/src/modules/agent-tools/mcpAdapter.ts or a small service folder if existing project conventions require it- Expose read/build/draft/explain tools first- Mark export/track tools as approval-required or blocked if approval cannot be guaranteed locally- Add documentation for local setup- Add tests for tool registry mappingForbidden:- No remote MCP deployment- No public MCP endpoint- No production auth/scopes- No ChatGPT App- No auto-apply / auto-send / auto-submit- No bypass of approval checks- No editor rewrite- No export rewrite- No broad app restructureAllowed MCP tools for local beta:- tw_get_application_context- tw_create_application_context- tw_build_evidence_graph- tw_draft_cover_letter- tw_explain_evidenceBlocked or guarded:- tw_export_artifact must require approval and may return blocked if approval state is missing- tw_track_application must require approval and may return blocked if approval state is missingDo not expose:- apply- send- submit- auto_apply- auto_submit- email_recruiter- click_external_applyRequired files:Create or update:my-app/src/modules/agent-tools/mcpAdapter.tsmy-app/src/modules/agent-tools/__tests__/mcpAdapter.test.tsdocs/howto/YYYY-MM-DD-local-mcp-beta.mddocs/decisions/YYYY-MM-DD-local-mcp-beta.mdImplementation requirements:- MCP adapter maps from internal TwoweeksToolContract registry.- Tool names and descriptions come from the internal registry.- Input/output schemas are derived or validated from the internal tool schemas.- Local MCP must not create a second source of truth for tool contracts.- Approval-required tools must expose their approval requirement in description/metadata.- If approval state cannot be proven, return blocked rather than executing export/track.Tests:- local MCP registry includes only allowed tools- forbidden apply/send/submit tools are absent- tool descriptions are copied from internal contracts- schema validation blocks bad input- approval-required tools do not execute without approved state- registry order deterministicDocs:howto doc must explain:- local-only status- how to start/test it- which tools are exposed- which tools are blocked- known limitations- no production auth yetDecision doc must explain:- MCP is adapter layer- why local beta comes before remote MCP- approval and safety boundaries- what is deferredAcceptance criteria:- Tests pass.- TypeScript passes.- No public endpoint exposed.- No production deployment changes.- No apply/send/submit capability.- Existing app routes unchanged.Final report:- Files changed- Tests run- What was verified- What remains deferred- Next smallest PR
```

---

# PR 8 — Remote MCP / ChatGPT App exploration

## Goal

Plan the distribution layer, not necessarily build it all.

This is the point where you decide:

```
Remote MCP?ChatGPT App?Codex plugin?Private beta?
```

## Codex prompt

```
Context:You are working in panamini/neyssan. Read AGENTS.md first. Treat v1 as the active baseline.PR 7 added a local-only MCP beta. This PR is an exploration/spec PR for remote MCP and/or ChatGPT App readiness. Do not ship a public remote integration unless explicitly scoped after this audit.Goal:Produce a concrete implementation plan for remote MCP / ChatGPT App readiness, including auth, scopes, tool permissions, approval flows, data boundaries, rate limits, observability, and rollout stages.Scope:Allowed:- Add docs/audits/YYYY-MM-DD-remote-mcp-readiness.md- Add docs/decisions/YYYY-MM-DD-agent-distribution-layer.md- Add docs/plans/YYYY-MM-DD-remote-mcp-chatgpt-app-plan.md- Add small non-runtime type definitions only if useful- Audit current internal tool contracts for remote safety- Propose exact follow-up PRsForbidden:- No public remote MCP deployment- No production auth implementation unless explicitly requested- No ChatGPT App submission- No apply/send/submit tools- No bypass of approval checks- No UI overhaul- No editor/export rewrite- No new paid/marketplace assumptions presented as factAudit must cover:1. Tool safety   - which tools are read-only   - which tools write   - which require approval   - which are blocked from remote2. Auth model   - Clerk identity boundary   - user-owned data only   - no cross-user access   - token/session requirements   - revocation requirements3. Data scopes   - CV read   - job read   - context create   - evidence create   - artifact draft   - export after approval   - tracking after approval4. Human approval model   - draft without approval   - explain without approval   - export only after approval   - track only after approval   - apply/send/submit excluded5. Observability   - ApplicationRunV1 logs   - ApplicationEventV1 events   - errors   - blocked actions   - model/tool provenance6. Rate limits and abuse protection   - per-user run limits   - duplicate run dedupe   - expensive operation guardrails   - no repeated generation loops without user action7. Prompt/tool-description quality   - compact descriptions   - clear purpose   - input expectations   - approval requirement   - blocked action behavior8. Remote deployment options   - remote MCP server   - ChatGPT App using Apps SDK   - Codex plugin or internal bridge   - private beta first9. Security risks   - prompt injection from job posts   - malicious job descriptions   - exfiltration through generated documents   - tool confusion   - approval bypass   - stale context   - cross-user data leakage10. Rollout plan   - local beta   - private remote MCP   - limited user beta   - ChatGPT App prototype   - production hardening   - public launch only after approval/audit gatesDeliverables:1. Remote MCP readiness audit2. Agent distribution layer decision doc3. Remote MCP / ChatGPT App implementation plan4. Next PR breakdownAcceptance criteria:- Docs are concrete and tied to current code.- No runtime public integration shipped.- No auto-apply/send/submit included.- All remote write actions require approval.- Risks and blocked areas are explicit.- Follow-up PRs are small and testable.Final report:- Docs created- Current readiness score- Blockers- Recommended next PR
```

---

# Optional PR 9 — Demo path

I’d add this after PR 8, because distribution needs a story.

## Codex prompt

```
Context:You are working in panamini/neyssan. Read AGENTS.md first. Treat v1 as the active baseline.The application harness now has context, runs, career knowledge, evidence graph, artifacts, review UI, internal tools, and local MCP beta.Goal:Create one deterministic demo path that proves the Twoweeks agent-native workflow without adding broad new functionality.Demo story:I am on a saved job.Twoweeks builds the application context.It compares the job to my selected CV.It shows evidence, missing requirements, and risk flags.It drafts a truthful cover letter.It shows a resume patch placeholder or patch plan if available.I approve.Only then export/track becomes available.Scope:Allowed:- Add one demo fixture or seeded local scenario- Add one Playwright test if runtime supports it- Add one docs/demo script- Add one short product demo narrativeForbidden:- No new generation engine- No UI redesign- No MCP expansion- No auto-apply/send/submit- No fake evidence- No unsupported claimsRequired output:- docs/demo/YYYY-MM-DD-agent-native-demo.md- optional focused Playwright test- list of known limitationsAcceptance criteria:- Demo does not require hidden manual state.- Demo survives hard refresh where technically possible.- Demo shows proof/risk/missing evidence.- Demo does not invent claims.- Demo does not submit applications.
```

---

# Best practical use of Codex

Do **not** paste PR 2 → PR 8 at once.

Use one prompt per branch:

```
codex/application-context-v1        already PR 1codex/career-knowledge-v1           PR 2codex/evidence-graph-v1             PR 3codex/application-artifact-v1        PR 4codex/application-review-v1          PR 5codex/internal-agent-tools-v1        PR 6codex/local-mcp-beta                PR 7codex/remote-agent-readiness         PR 8
```

After each PR, ask Codex:

```
Before patching anything else, write a short audit of what you changed, what you verified, what remains risky, and the smallest next PR. Do not continue into the next PR.
```

This matters because OpenAI’s Codex docs put `AGENTS.md` at the center of project-specific instructions, and your repo’s `AGENTS.md` already tells agents to prefer small, testable, reversible changes.

---

# Final plan in Twoweeks language

```
CONTEXT. LOCKED.RUNS. IDEMPOTENT.RULES. STRUCTURED.EVIDENCE. ATTACHED.CLAIMS. CHECKED.DRAFT. SAFE.REVIEW. HUMAN.EXPORT. APPROVED.TOOLS. INTERNAL.MCP. LATER.
```

That is the ideal path.