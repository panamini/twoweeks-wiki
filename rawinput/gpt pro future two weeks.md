	# Blunt verdict
	
	**Do not build the plan as-is. Build the spine, kill the theater, delay the platform.** The durable core is worth building, but the current plan is too wide: it mixes runtime idempotency, evidence safety, Career Vault ingestion, resume variants, review UI, job sourcing, internal tools, and MCP distribution into one “impressive” architecture. Split it harder. Start with a boring harness and provenance kernel; delay Career Vault UI, Scout, MCP, ChatGPT App, campaigns, and any generation rewrite. Your own constraints ask for source-first, additive, non-regressive, Codex-friendly work; I’m applying those constraints literally.
	
	## Source-first inventory used for this review
	
	I inspected or used the following concrete sources before recommending a roadmap:
	
	| Area                                         | Source inspected                             | Why it matters                                                                                                                                                                                                                                                                                                                                                                |
	| -------------------------------------------- | -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
	| Repo rules                                   | `AGENTS.md`                                  | The repo explicitly prioritizes CV ingestion/parsing, canonical saved CV/profile data, and personalized proposal generation; it also requires small reversible changes and active-path inspection.                                                                                                                                                                            |
	| Current compressed CV snapshot               | `my-app/convex/activeCvSnapshots.ts`         | It clips experience to 3 items, skills to 12, achievements to 8. This proves a long Career Vault cannot flow through this path.                                                                                                                                                                                                                                               |
	| Current proposal personalization compression | `my-app/src/lib/proposal-personalization.ts` | It hard-caps proposal context: summary 240 chars, 8 skills, 3 experiences, 5 highlights, 6 achievements.                                                                                                                                                                                                                                                                      |
	| Current Convex schema                        | `my-app/convex/schema.ts`                    | Existing `proposals`, `jobs`, `userProfiles`, `activeCvSnapshots`, match review, and extraction shadow structures already cover part of the desired domain.                                                                                                                                                                                                                   |
	| Premium cover-letter provenance              | `premiumCoverLetter.ts`                      | Existing merged code already has cover-letter-scoped `FactGraphV1`, `JobDemandGraphV1`, `ClaimPlanV1`, and provenance-carrying writer output.                                                                                                                                                                                                                                 |
	| Premium tests                                | `premiumCoverLetter.test.ts`                 | There are already tests for stable IDs, low-value/fluff rejection, prompt provenance, unsupported numeric claims, unknown facts, greeting/signoff leakage, and writer-output validation.                                                                                                                                                                                      |
	| LinkedIn policy                              | LinkedIn Crawling Terms                      | Automated crawling without express LinkedIn permission is prohibited; LinkedIn offers user data download flows instead. ([LinkedIn](https://www.linkedin.com/legal/crawling-terms "LinkedIn Crawling Terms and Conditions")) ([LinkedIn](https://www.linkedin.com/help/linkedin/answer/a1339364/downloading-your-account-data "Download your account data \| LinkedIn Help")) |
	| MCP / Apps docs                              | MCP spec, OpenAI Apps SDK docs               | MCP is a later adapter/distribution layer with tools/resources/prompts and explicit trust/safety requirements; OpenAI Apps SDK is a ChatGPT app distribution/build layer, not your product core. ([Model Context Protocol](https://modelcontextprotocol.io/specification/2025-06-18/architecture "Architecture - Model Context Protocol"))                                    |
	| ATS sourcing docs                            | Greenhouse Job Board API                     | Scout can later use controlled adapters; Greenhouse exposes public JSON job board endpoints for published jobs, but application submission is a different and riskier path. ([Greenhouse Developers](https://developers.greenhouse.io/job-board.html "Job Board API \| Greenhouse"))                                                                                          |
	
	I did **not** run runtime tests from this boundary. This is a source-grounded architecture review, not a verified code change.
	
	---
	
	# 1. Findings first, ordered by severity
	
	## P0 — The plan is too broad to be a safe Codex task
	
	**Issue:** The plan combines at least five separate systems: durable execution, candidate knowledge, evidence validation, artifact generation, and agent/distribution integrations.
	
	**Why it matters:** Your repo rules explicitly say to avoid broad rewrites, inspect active paths, preserve existing patterns, and prefer the smallest change that solves the issue. A single “ultimate platform” PR will either fail or silently touch CV Forge, Proposal Forge, export, parser, or jobs.
	
	**Do instead:** Split into three layers:
	
	```txt
	Layer 1 — Harness: context, runs, fingerprints, artifacts shell
	Layer 2 — Proof: candidate facts, evidence graph, claim/risk validation
	Layer 3 — Product: resume variants, cover-letter artifacts, review, packages
	```
	
	**Delete / delay / split:**
	
	- **Delay:** Career Vault UI, Review UI, Scout, MCP, ChatGPT App.
	    
	- **Split:** ApplicationContext/Run from Career Vault.
	    
	- **Kill for now:** Campaigns, Google Docs/Sheets, auto-apply, send/submit tooling.
	    
	
	---
	
	## P0 — Career Vault cannot use today’s personalization context
	
	**Issue:** The current active CV snapshot and proposal personalization context intentionally compress candidate data. `activeCvSnapshots.ts` slices experience to 3 entries and limits skills/achievements; proposal personalization also hard-caps summary, skills, experience, highlights, and achievements.
	
	**Why it matters:** A long LinkedIn-style or multi-career profile becomes useless if shoved into this pipe. It will drop older-but-relevant experience, multi-role identities, certifications, languages, portfolio evidence, freelance history, and non-recent proof.
	
	**Do instead:** Treat the Career Vault as a **fact store**, not a longer CV and not a bigger prompt blob.
	
	```txt
	Source document
	→ CandidateFact[]
	→ fact eligibility / visibility
	→ evidence selection
	→ allowed claims
	→ resume variant plan
	```
	
	**Delete / delay / rename:**
	
	- **Rename internally:** `MasterProfileV1` → `CandidateEvidenceProfileV1` or `CareerVaultProfileV1`.
	    
	- **Delay:** feeding Career Vault into Proposal Forge.
	    
	- **Delete:** any plan that says “long profile text → prompt → tailored CV.”
	    
	
	---
	
	## P0 — `ApplicationRunV1` is necessary, but should be smaller than proposed
	
	**Issue:** The plan correctly identifies the need for runs, idempotency, fingerprints, and recoverability. But the proposed early model risks becoming a full workflow engine before one workflow exists.
	
	**Why it matters:** Agent workflows will duplicate drafts, overwrite edits, and become un-debuggable without a run ledger. But over-modeling run state too early creates fake durability and code paths nobody uses.
	
	**Do instead:** Make `ApplicationRunV1` boring:
	
	```ts
	{
	  id
	  userId
	  operation
	  targetType
	  targetId
	  inputHash
	  idempotencyKey
	  status
	  attemptCount
	  resultIds
	  error
	  createdAt
	  updatedAt
	  version
	}
	```
	
	**Delete / delay / split:**
	
	- **Delay:** scheduled workflow orchestration.
	    
	- **Delay:** retries beyond `attemptCount`.
	    
	- **Delay:** complex parent/child run trees.
	    
	- **Keep now:** deterministic idempotency keys and duplicate prevention.
	    
	
	---
	
	## P0 — Do not create a second global `FactGraphV1` by copying premium cover-letter code
	
	**Issue:** Premium cover letters already have `FactGraphV1`, `JobDemandGraphV1`, and `ClaimPlanV1`, but they are embedded in `premiumCoverLetter.ts` and scoped to cover-letter generation.
	
	**Why it matters:** Copying those types into `evidence-graph/` will create drift. Importing them directly will over-couple the app-level evidence layer to a writer-specific implementation.
	
	**Do instead:** Create a new app-level module with compatible concepts, then migrate the premium path later.
	
	```txt
	premiumCoverLetter FactGraph = current writer-local truth
	application evidence graph = app-level proof layer
	```
	
	**Delete / delay / split:**
	
	- **Do not move premium code in PR 1.**
	    
	- **Do not import premium writer types into Career Vault.**
	    
	- **Do not rename premium types globally until app-level tests exist.**
	    
	
	---
	
	## P0 — `CoverLetterArtifactV1` is redundant as a standalone root object
	
	**Issue:** `CoverLetterArtifactV1`, `ResumeVariantDocumentV1`, `ExportArtifactV1`, and `ApplicationArtifactV1` are competing abstractions.
	
	**Why it matters:** You will create parallel persistence systems for similar things: generated content with provenance.
	
	**Do instead:** Use one artifact model:
	
	```ts
	ApplicationArtifactV1 {
	  type: "cover_letter" | "resume_variant" | "resume_patch_plan" | "export"
	}
	```
	
	Cover-letter-specific fields belong in `content` and `provenance`, not a separate root table unless performance later requires it.
	
	**Delete / merge:**
	
	- **Merge:** `CoverLetterArtifactV1` into `ApplicationArtifactV1`.
	    
	- **Merge:** `ResumeVariantDocumentV1` into `ApplicationArtifactV1` initially, or store as `CvDocument` plus artifact pointer.
	    
	- **Keep:** typed helpers like `createCoverLetterArtifact()`.
	    
	
	---
	
	## P0 — Do not build Scout before application packets work
	
	**Issue:** Scout/job-source adapters are tempting, but they multiply scope: source detection, dedupe, location normalization, ATS-specific parsing, rate limits, policy risks, and stale jobs.
	
	**Why it matters:** The current app already has job records with `sourceUrl`, `applicationUrl`, `dedupeKey`, `rawDescription`, `summary`, `responsibilities`, `keywords`, `mustHaves`, review items, and indexes. Scout before packages just creates more jobs the product cannot safely convert into applications.
	
	**Do instead:** Make one manually imported/saved job produce one application packet first.
	
	**Delete / delay:**
	
	- **Delay:** Scout until ApplicationPackage + resume variant + cover-letter artifact + review exist.
	    
	- **Kill MVP scraping:** LinkedIn/Upwork/Indeed scraping.
	    
	- **Allow later:** controlled ATS adapters such as Greenhouse, where public published-job JSON exists. ([Greenhouse Developers](https://developers.greenhouse.io/job-board.html "Job Board API | Greenhouse"))
	    
	
	---
	
	## P0 — LinkedIn scraping must be explicitly forbidden
	
	**Issue:** The plan says not to scrape LinkedIn, but that rule needs to become a product and engineering invariant.
	
	**Why it matters:** LinkedIn’s crawling terms prohibit automated crawling/indexing without express permission, and they provide a user data download path that includes categories like positions, education, certifications, job applications, languages, projects, saved jobs, skills, and resume data. ([LinkedIn](https://www.linkedin.com/legal/crawling-terms "LinkedIn Crawling Terms and Conditions"))
	
	**Do instead:**
	
	```txt
	Allowed:
	- LinkedIn data export uploaded by user
	- LinkedIn profile PDF uploaded by user
	- copied/pasted profile text
	- manually entered facts
	
	Forbidden MVP:
	- automated LinkedIn profile scraping
	- logged-in browser crawling
	- bypassing anti-bot systems
	```
	
	**Add:** A safety decision doc and import-source enum that makes this impossible to “accidentally” add later.
	
	---
	
	## P1 — `ApplicationPackageV1` is right eventually, wrong as PR 1
	
	**Issue:** `ApplicationPackageV1` sounds like the atomic product object, but it depends on job lead, candidate source, evidence graph, resume variant, cover-letter artifact, review state, export state, and tracker state.
	
	**Why it matters:** Building it before artifacts exist creates a bag of nullable IDs.
	
	**Do instead:** Start with `ApplicationContextV1` and `ApplicationRunV1`. Introduce `ApplicationPackageV1` only after one real package can be created:
	
	```txt
	job + candidate snapshot
	→ evidence graph
	→ resume variant plan
	→ cover-letter artifact
	→ package
	```
	
	**Delete / delay:**
	
	- **Delay:** `ApplicationPackageV1` until after first artifact path.
	    
	- **Do not create:** package UI until there is something real to review.
	    
	
	---
	
	## P1 — CareerKnowledge should not be stuffed into Career Vault
	
	**Issue:** Candidate facts and career-writing rules are different domains.
	
	**Why it matters:** A fact says “worked with React.” A rule says “do not add unsupported tools.” Mixing them causes user data and editorial policy to blur.
	
	**Do instead:**
	
	```txt
	Career Vault = user-owned evidence
	CareerKnowledge = product-owned rules
	EvidenceGraph = resolver that applies rules to evidence + job
	```
	
	**Merge / split:**
	
	- **Keep separate:** `career-knowledge/`
	    
	- **Keep separate:** `career-vault/`
	    
	- **Bridge in:** `evidence-graph/ruleResolver.ts`
	    
	
	---
	
	## P1 — Review UI must be a cockpit, not another editor
	
	**Issue:** A full Career Vault UI or another proposal editor will overwhelm users and create regressions.
	
	**Why it matters:** CV Forge and Proposal Forge already exist. A third editor duplicates mental model and state.
	
	**Do instead:** First user-facing UX should be:
	
	```txt
	Upload/paste source
	→ show extracted facts
	→ approve / hide / never use
	→ generate plan for one job
	→ review risks
	```
	
	Then later:
	
	```txt
	Application Review cockpit
	```
	
	**Delay:**
	
	- Full vault management dashboard.
	    
	- Campaign board.
	    
	- Visual evidence graph editor.
	    
	- Drag/drop fact lens UI.
	    
	
	---
	
	## P1 — `CandidateFactConflictV1` should not be a first-class table until conflicts exist
	
	**Issue:** Conflict tables are often premature.
	
	**Why it matters:** You do not yet know conflict shape: duplicate facts, date mismatch, employer mismatch, certification mismatch, stale data, source-priority conflict, user correction conflict.
	
	**Do instead:** PR 1 import pipeline can return conflict candidates as transient review output. Persist conflicts only when you have review UI and unresolved conflicts.
	
	**Delay:**
	
	```txt
	CandidateFactConflictV1 table
	```
	
	Use:
	
	```ts
	fact.reviewState = "pending" | "approved" | "rejected" | "needs_conflict_review"
	```
	
	Add a conflict table later if it earns its existence.
	
	---
	
	## P1 — `CareerLensV1` should start derived, not manually managed
	
	**Issue:** Multi-role “lenses” are valuable, but a stored lens editor is premature.
	
	**Why it matters:** Stored lenses need UI, user education, merging, defaulting, and conflict behavior.
	
	**Do instead:** Start with a derived `candidateLensSuggestion` in `ResumeVariantPlanV1`.
	
	```txt
	facts + job demands
	→ suggested lens label
	→ selected facts
	```
	
	Persist `CareerLensV1` only after users repeatedly need named identities.
	
	**Delay:** lens management UI and stable lens table.
	
	---
	
	## P1 — MCP is a distribution adapter, not a product layer
	
	**Issue:** MCP tooling is real, but it should wrap internal Twoweeks tools later. It should not own scraping, writing, exporting, or application state.
	
	**Why it matters:** MCP servers expose tools/resources/prompts; the spec says hosts enforce permissions and consent, servers expose focused capabilities, and tools should have human-in-the-loop confirmation for sensitive operations. ([Model Context Protocol](https://modelcontextprotocol.io/specification/2025-06-18/architecture "Architecture - Model Context Protocol"))
	
	**Do instead:**
	
	```txt
	internal tool contracts
	→ local MCP adapter
	→ remote MCP / ChatGPT App
	```
	
	**Delay:**
	
	- Remote MCP.
	    
	- ChatGPT App.
	    
	- Public tool surface.
	    
	- Any apply/send/submit tool.
	    
	
	---
	
	## P2 — Rename for clarity
	
	Current names are partly good, partly overloaded.
	
	|Current name|Verdict|Better internal name|
	|---|--:|---|
	|Career Vault|Good product name|keep for UX later|
	|MasterProfileV1|Too broad / conflicts with `userProfiles`|`CandidateEvidenceProfileV1`|
	|CandidateFactV1|Good|keep|
	|CandidateSourceDocumentV1|Good|keep|
	|CandidateFactConflictV1|Premature|derive first; persist later|
	|CareerLensV1|Good later|`CandidateLensV1` or derived suggestion first|
	|ApplicationContextV1|Good|keep|
	|ApplicationRunV1|Good|keep|
	|ApplicationArtifactV1|Good|keep|
	|CoverLetterArtifactV1|Redundant|`ApplicationArtifactV1.type="cover_letter"`|
	|ResumeVariantDocumentV1|Over-specific early|artifact or `CvDocument` derivative with provenance|
	|ApplicationPackageV1|Good later|keep later|
	|ApplicationEventV1|Good later|table later, shell now|
	
	---
	
	# 2. Senior-engineer verdict
	
	## Will this make the current app more robust for generating CVs and letters?
	
	**Yes, if the first slice is harness + provenance + evidence boundaries.** It makes the app more robust by adding deterministic context hashes, run idempotency, source provenance, artifact immutability, and claim safety. Those are directly relevant to CV and letter generation.
	
	## Where could it fragilize the app?
	
	It becomes fragile if Codex:
	
	- touches CV Forge UI;
	    
	- rewrites Proposal Forge persistence;
	    
	- changes export;
	    
	- changes parser behavior;
	    
	- routes existing proposal generation through a new evidence graph too early;
	    
	- adds new Convex tables and immediately wires them into active routes;
	    
	- turns source imports into one LLM blob;
	    
	- adds MCP before internal tools and approvals exist.
	    
	
	## Which parts improve current users now?
	
	Near-term value:
	
	```txt
	1. Better job-specific resume variant planning.
	2. Fewer unsupported cover-letter claims.
	3. Recoverable generated artifacts.
	4. No accidental overwrite of user edits.
	5. Better explanation of why a job matches or does not match.
	```
	
	## Which parts are future platform/distribution?
	
	Future only:
	
	```txt
	Scout
	Campaigns
	MCP
	ChatGPT App
	Google Docs/Sheets sync
	auto-apply/send/submit
	remote agent tooling
	```
	
	OpenAI’s Apps SDK is explicitly a framework for building ChatGPT apps and publishing through app distribution/submission flows; that belongs after the Twoweeks internal product works. ([OpenAI Developers](https://developers.openai.com/apps-sdk/ "Apps SDK | OpenAI Developers"))
	
	## First production-useful slice
	
	The first slice that matters to users is **not** Career Vault UI. It is:
	
	```txt
	saved job + selected CV
	→ deterministic ApplicationContext
	→ evidence/claim summary
	→ reviewable resume variant plan
	```
	
	Then:
	
	```txt
	→ cover letter artifact
	→ export after approval
	```
	
	---
	
	# 3. Product critique
	
	## Career Vault / MasterProfileV1
	
	**Exist now?** Yes as a backend evidence store, not UI-heavy product.
	
	**Exist later?** Full UX, source refresh, conflict resolution, multi-lens management.
	
	**Do not build yet:** Beautiful Career Vault dashboard.
	
	**Simplest UX:**
	
	```txt
	Add source
	Review extracted facts
	Approve / Hide / Never use
	Use approved facts for this job
	```
	
	## ApplicationPackageV1
	
	**Exist now?** No. Too many nullable dependencies.
	
	**Exist later?** Yes, after resume variant and cover-letter artifact exist.
	
	**Simplest UX:** “Application packet” page with one job, one resume variant, one letter, evidence, risks, exports.
	
	## ApplicationContextV1
	
	**Exist now?** Yes. This is the right first foundation.
	
	**Simplify:** It should identify the job, candidate snapshot, settings, fingerprints, and review state. Do not stuff artifacts and evidence deeply into it early; link by IDs.
	
	## Campaigns
	
	**Exist now?** No.
	
	**Later:** campaign = group of packages.
	
	**Kill for now:** campaign UI, batch apply, “find 50 jobs”.
	
	## Scout
	
	**Exist now?** No.
	
	**Later:** controlled adapters after packet flow works.
	
	**Forbidden MVP:** LinkedIn/Upwork/Indeed scraping.
	
	## MCP
	
	**Exist now?** No.
	
	**Later:** adapter over internal tools.
	
	**Must not own:** scraping, export, send, submit, generation logic, auth policy.
	
	## ChatGPT App
	
	**Exist now?** No.
	
	**Later:** distribution wrapper after local MCP and approvals.
	
	## Review UI
	
	**Exist now?** Minimal only after evidence/artifact exists.
	
	**Simplest UX:**
	
	```txt
	What matched
	What is missing
	What is risky
	What will change in resume
	Approve
	```
	
	## Agent tools
	
	**Exist now?** Contract-only after internal services exist.
	
	**Later:** callable wrappers.
	
	**Do not expose:** apply/send/submit.
	
	---
	
	# 4. Architecture critique
	
	## Should CareerKnowledge be separate from Career Vault?
	
	**Yes.** Career Vault is user-owned evidence. CareerKnowledge is product-owned rules. EvidenceGraph consumes both.
	
	```txt
	CareerVault facts
	+ JobDemandGraph
	+ CareerKnowledge rules
	= EvidenceGraph / allowed claims / risks
	```
	
	## Should EvidenceGraph reuse premium cover-letter FactGraph?
	
	**Conceptually yes, structurally no at first.** Premium cover-letter provenance has useful tested ideas: stable fact IDs, demand buckets, forbidden claims, allowed verbs, writer-output provenance. But it is writer-scoped. Create app-level evidence as a separate module, then adapt the premium writer later.
	
	## Should ResumeVariantPlanV1 always come before ResumeVariantDocumentV1?
	
	**Yes. Always.** The plan is the safety boundary. A document without a reviewable plan will mutate trust.
	
	```txt
	Plan first
	Review risks
	Then generate document
	```
	
	## Should CoverLetterArtifactV1 wrap existing Proposal Forge?
	
	**No, not initially.** Keep Proposal Forge untouched. Add `ApplicationArtifactV1` separately. Later, a narrow adapter may create a proposal draft from a cover-letter artifact or save a cover-letter artifact from a generation run.
	
	## Which objects are redundant?
	
	Redundant now:
	
	```txt
	CoverLetterArtifactV1
	ResumeVariantDocumentV1 as its own table
	CandidateFactConflictV1 as a table
	ApplicationPackageV1 before artifacts exist
	CampaignV1 before packages exist
	```
	
	## Which objects are missing?
	
	Missing or under-specified:
	
	```ts
	SourceRefV1
	ApprovalRecordV1
	AllowedClaimV1
	UnsupportedClaimV1
	FactVisibilityPolicyV1
	ArtifactSupersessionV1
	ImportBatchV1
	GenerationInputSnapshotV1
	```
	
	You do not need all as tables. But you need the concepts.
	
	## What must never mutate canonical data?
	
	Never mutate during generation:
	
	```txt
	canonical CV
	userProfiles.cvDocument
	Career Vault / CandidateEvidenceProfile
	CandidateSourceDocument raw text
	approved CandidateFact source text
	existing approved artifacts
	existing Proposal Forge saved drafts
	```
	
	## Where should feature flags or shadow mode be used?
	
	Use shadow mode for:
	
	```txt
	EvidenceGraph generated beside current match review
	ResumeVariantPlan generated but not surfaced broadly
	CoverLetterArtifact created from existing generation but not replacing Proposal Forge
	Career Vault facts extracted but not eligible until approval
	```
	
	Feature flags:
	
	```txt
	applicationHarnessV1
	careerVaultImportV1
	evidenceGraphShadowV1
	resumeVariantPlanV1
	applicationReviewV1
	internalAgentToolsV1
	```
	
	## What should stay internal-only?
	
	Internal-only until mature:
	
	```txt
	ApplicationRunV1
	ApplicationEventV1
	idempotency keys
	raw source document text
	risk classifier internals
	claim validation internals
	agent tool registry
	MCP adapter
	```
	
	---
	
	# 5. Data model improvements
	
	## ApplicationContextV1
	
	**Purpose:** Stable application input snapshot.
	
	**Minimum fields:**
	
	```ts
	type ApplicationContextV1 = {
	  id: string;
	  userId: string;
	  job: {
	    jobId: string;
	    sourceUrl?: string;
	    rawTextHash: string;
	    title?: string;
	    company?: string;
	  };
	  candidate: {
	    sourceKind: "cv" | "career_vault";
	    cvId?: string;
	    candidateEvidenceProfileId?: string;
	    candidateHash: string;
	    selectedLanguage?: string;
	    market?: string;
	  };
	  settingsHash: string;
	  contextHash: string;
	  reviewState: "draft" | "needs_review" | "approved" | "superseded";
	  createdAt: number;
	  updatedAt: number;
	  version: 1;
	};
	```
	
	**Avoid for now:**
	
	```txt
	full raw job text
	full CV document
	full evidence graph
	artifact arrays
	deep review notes
	agent state
	```
	
	**Indexes:**
	
	```txt
	by_user_context_hash
	by_user_job_candidate
	by_user_updated
	```
	
	---
	
	## ApplicationRunV1
	
	**Purpose:** Idempotent operation ledger.
	
	**Minimum fields:**
	
	```ts
	type ApplicationRunV1 = {
	  id: string;
	  userId: string;
	  contextId?: string;
	  operation:
	    | "build_context"
	    | "build_evidence_graph"
	    | "plan_resume_variant"
	    | "draft_cover_letter"
	    | "create_artifact"
	    | "export_artifact"
	    | "track_application";
	  inputHash: string;
	  idempotencyKey: string;
	  status: "queued" | "running" | "succeeded" | "failed" | "blocked";
	  attemptCount: number;
	  resultIds?: string[];
	  blockedReason?: string;
	  error?: string;
	  createdAt: number;
	  updatedAt: number;
	  version: 1;
	};
	```
	
	**Avoid for now:** workflow DAGs, step trees, retry policies, scheduled function coupling.
	
	**Indexes:**
	
	```txt
	by_user_idempotency_key
	by_context_operation
	by_status_updated
	```
	
	---
	
	## ApplicationArtifactV1
	
	**Purpose:** Recoverable generated/reviewable output.
	
	**Minimum fields:**
	
	```ts
	type ApplicationArtifactV1 = {
	  id: string;
	  userId: string;
	  contextId: string;
	  runId?: string;
	  type:
	    | "cover_letter"
	    | "resume_variant_plan"
	    | "resume_variant"
	    | "resume_patch_plan"
	    | "export";
	  status: "draft" | "needs_review" | "approved" | "superseded" | "blocked";
	  title: string;
	  content: unknown;
	  textPreview?: string;
	  sourceHashes: {
	    contextHash: string;
	    evidenceGraphHash?: string;
	    generatorInputHash?: string;
	  };
	  provenance: {
	    jobId?: string;
	    cvId?: string;
	    candidateEvidenceProfileId?: string;
	    evidenceGraphId?: string;
	    sourceFactIds?: string[];
	  };
	  approval?: ApprovalRecordV1;
	  createdAt: number;
	  updatedAt: number;
	  version: 1;
	};
	```
	
	**Avoid for now:** separate `CoverLetterArtifactV1` table.
	
	**Indexes:**
	
	```txt
	by_context_type
	by_user_status_updated
	by_run
	```
	
	---
	
	## ApplicationEventV1
	
	**Purpose:** Audit trail, not business state.
	
	**Minimum early choice:** do **not** create table in PR 1 unless needed. Use a shell type.
	
	```ts
	type ApplicationEventV1 = {
	  id: string;
	  userId: string;
	  contextId?: string;
	  runId?: string;
	  eventType: string;
	  payload?: unknown;
	  createdAt: number;
	  version: 1;
	};
	```
	
	**Avoid:** dumping raw CV/job/source text into events.
	
	---
	
	## CandidateEvidenceProfileV1
	
	**Purpose:** Internal Career Vault root.
	
	**Minimum fields:**
	
	```ts
	type CandidateEvidenceProfileV1 = {
	  id: string;
	  userId: string;
	  displayName?: string;
	  sourceDocumentIds: string[];
	  factCount: number;
	  approvedFactCount: number;
	  defaultCvId?: string;
	  createdAt: number;
	  updatedAt: number;
	  version: 1;
	};
	```
	
	**Avoid for now:** giant identity blob, UI layout preferences, generated summary, full source text.
	
	---
	
	## CandidateSourceDocumentV1
	
	**Purpose:** User-controlled import source, not final truth.
	
	```ts
	type CandidateSourceDocumentV1 = {
	  id: string;
	  userId: string;
	  profileId: string;
	  sourceType:
	    | "uploaded_pdf"
	    | "uploaded_docx"
	    | "uploaded_text"
	    | "uploaded_markdown"
	    | "pasted_text"
	    | "linkedin_export"
	    | "linkedin_pdf"
	    | "upwork_export"
	    | "portfolio_page"
	    | "project_list"
	    | "manual";
	  title?: string;
	  contentHash: string;
	  rawTextRef?: string;
	  importedAt: number;
	  reviewState: "pending" | "reviewed" | "rejected";
	  createdAt: number;
	  updatedAt: number;
	  version: 1;
	};
	```
	
	**Privacy:** source docs may contain private contacts, references, addresses, screenshots, and third-party names. Do not expose to prompts wholesale.
	
	**Indexes:**
	
	```txt
	by_user_hash
	by_profile_review
	```
	
	---
	
	## CandidateFactV1
	
	**Purpose:** Atomic evidence unit.
	
	```ts
	type CandidateFactV1 = {
	  id: string;
	  userId: string;
	  profileId: string;
	  sourceDocumentId: string;
	  sourcePath: string;
	  text: string;
	  normalizedTextHash: string;
	  category:
	    | "role"
	    | "achievement"
	    | "skill"
	    | "tool"
	    | "education"
	    | "certification"
	    | "language"
	    | "project"
	    | "portfolio"
	    | "domain"
	    | "preference";
	  extracted: {
	    company?: string;
	    roleTitle?: string;
	    startDate?: string;
	    endDate?: string;
	    metrics?: string[];
	    skills?: string[];
	  };
	  confidence: number;
	  reviewState: "pending" | "approved" | "rejected" | "needs_conflict_review";
	  visibility: "public_cv" | "private_context" | "never_use";
	  createdAt: number;
	  updatedAt: number;
	  version: 1;
	};
	```
	
	**Avoid:** generated rewritten bullet text. Facts should preserve source truth.
	
	**Indexes:**
	
	```txt
	by_profile_review
	by_profile_category
	by_profile_hash
	by_source_document
	```
	
	---
	
	## CandidateFactConflictV1
	
	**Verdict:** Delay.
	
	**Use first:** transient conflict output.
	
	Later:
	
	```ts
	type CandidateFactConflictV1 = {
	  id: string;
	  userId: string;
	  profileId: string;
	  factIds: string[];
	  conflictType: "duplicate" | "date_mismatch" | "employer_mismatch" | "credential_mismatch";
	  status: "open" | "resolved" | "ignored";
	  resolution?: unknown;
	  createdAt: number;
	  updatedAt: number;
	  version: 1;
	};
	```
	
	---
	
	## CareerLensV1
	
	**Verdict:** Derived first, persisted later.
	
	Later:
	
	```ts
	type CareerLensV1 = {
	  id: string;
	  userId: string;
	  profileId: string;
	  label: string;
	  includedFactIds: string[];
	  excludedFactIds: string[];
	  defaultDocumentType?: "resume" | "cv" | "proposal";
	  createdAt: number;
	  updatedAt: number;
	  version: 1;
	};
	```
	
	**Avoid now:** UI-heavy lens management.
	
	---
	
	## CareerKnowledgeRuleV1
	
	**Purpose:** Product-owned rule, separate from user facts.
	
	```ts
	type CareerKnowledgeRuleV1 = {
	  id: string;
	  market: "us" | "uk" | "eu" | "fr" | "global";
	  documentType: "resume" | "cv" | "cover_letter" | "proposal";
	  category: "ats" | "layout" | "claim_safety" | "tone" | "structure" | "evidence";
	  severity: "must" | "should" | "advisory";
	  rule: string;
	  validatorKey?: string;
	  version: 1;
	};
	```
	
	**Avoid:** raw PDF/source chunks in runtime prompts.
	
	---
	
	## EvidenceGraphV1
	
	**Purpose:** Proof layer between job, facts, and generated claims.
	
	```ts
	type EvidenceGraphV1 = {
	  id: string;
	  userId: string;
	  contextId: string;
	  requirements: EvidenceRequirementV1[];
	  matches: EvidenceMatchV1[];
	  missing: MissingRequirementV1[];
	  riskFlags: RiskFlagV1[];
	  allowedClaims: AllowedClaimV1[];
	  sourceHashes: {
	    contextHash: string;
	    jobHash: string;
	    candidateHash: string;
	    rulesHash: string;
	  };
	  createdAt: number;
	  updatedAt: number;
	  version: 1;
	};
	```
	
	**Avoid:** writer-specific prose.
	
	---
	
	## JobDemandGraphV1
	
	**Verdict:** Can be nested inside EvidenceGraph early.
	
	Minimum:
	
	```ts
	type JobDemandGraphV1 = {
	  demands: Array<{
	    id: string;
	    text: string;
	    type: "hard" | "soft" | "nice_to_have" | "fluff";
	    mustNotBecomeCandidateClaim: boolean;
	  }>;
	  jobHash: string;
	  version: 1;
	};
	```
	
	---
	
	## ResumeVariantPlanV1
	
	**Purpose:** Reviewable plan before CV generation.
	
	```ts
	type ResumeVariantPlanV1 = {
	  id: string;
	  userId: string;
	  contextId: string;
	  evidenceGraphId: string;
	  selectedFactIds: string[];
	  excludedFactIds: string[];
	  unsupportedKeywords: string[];
	  summaryPlan?: string;
	  sectionOrder?: string[];
	  bulletRewritePlans: Array<{
	    sourceFactIds: string[];
	    targetSection: string;
	    action: "keep" | "reorder" | "rewrite" | "omit";
	    rationale: string;
	    riskFlags?: string[];
	  }>;
	  status: "draft" | "needs_review" | "approved" | "blocked";
	  sourceHashes: {
	    contextHash: string;
	    evidenceGraphHash: string;
	  };
	  createdAt: number;
	  updatedAt: number;
	  version: 1;
	};
	```
	
	---
	
	## ResumeVariantDocumentV1
	
	**Verdict:** Do not make a root table early.
	
	Early implementation:
	
	```txt
	ApplicationArtifactV1.type = "resume_variant"
	content.cvDocument = CvDocument
	provenance.sourceFactIds = [...]
	```
	
	Later, if needed, split into dedicated table.
	
	---
	
	## ApplicationPackageV1
	
	**Purpose:** Product-level application packet.
	
	**Add later:**
	
	```ts
	type ApplicationPackageV1 = {
	  id: string;
	  userId: string;
	  contextId: string;
	  jobId: string;
	  resumeVariantArtifactId?: string;
	  coverLetterArtifactId?: string;
	  reviewState: "needs_review" | "approved" | "exported" | "tracked";
	  status: "draft" | "ready" | "applied" | "interview" | "rejected" | "archived";
	  createdAt: number;
	  updatedAt: number;
	  version: 1;
	};
	```
	
	**Avoid now:** campaign fields, source adapter fields, send/apply fields.
	
	---
	
	# 6. Revised PR roadmap
	
	## PR 1 — Harness kernel, no persistence wiring
	
	**Goal:** Define pure deterministic primitives.
	
	**Allowed scope:**
	
	```txt
	my-app/src/modules/application-harness/
	  schema.ts
	  fingerprints.ts
	  idempotency.ts
	  __tests__/
	docs/decisions/YYYY-MM-DD-application-harness-kernel.md
	```
	
	**Forbidden scope:**
	
	```txt
	No Convex schema writes
	No UI
	No MCP
	No generation changes
	No parser changes
	No Proposal Forge changes
	No CV Forge changes
	```
	
	**Acceptance:**
	
	```txt
	stable JSON hash
	same context input = same hash
	changed job = changed jobHash
	changed candidate = changed candidateHash
	same operation input = same idempotencyKey
	input objects are not mutated
	```
	
	**Tests:** unit tests only.
	
	**Rollback risk:** tiny.
	
	**Regression risk:** none if unimported.
	
	**Stop conditions:** any active route import, UI edit, Convex mutation, generation prompt change.
	
	---
	
	## PR 2 — Harness persistence shadow tables
	
	**Goal:** Add additive Convex tables/functions for contexts/runs/artifacts shell.
	
	**Allowed scope:**
	
	```txt
	my-app/convex/applicationContexts.ts
	my-app/convex/applicationRuns.ts
	my-app/convex/applicationArtifacts.ts
	my-app/convex/schema.ts additive tables only
	```
	
	**Forbidden:** wiring into existing generation or UI.
	
	**Acceptance:**
	
	```txt
	createOrReuseContext by contextHash
	createOrReuseRun by idempotencyKey
	artifact shell can be inserted
	no old tables changed except additive schema
	```
	
	**Tests:** Convex helper tests / pure function tests.
	
	**Rollback risk:** low but schema-touching.
	
	**Regression risks:** schema compile, index mistakes.
	
	**Stop conditions:** touching existing `proposals`, `jobs`, `userProfiles`, `activeCvSnapshots` behavior.
	
	---
	
	## PR 3 — ApplicationContext builder shadow mode
	
	**Goal:** Build a context from existing job + selected CV/profile without changing flows.
	
	**Allowed:**
	
	```txt
	read existing jobs
	read existing userProfiles/cvDocument/currentCv shape
	prefer structured sections when present
	compute hashes
	persist/reuse context
	```
	
	**Forbidden:** generation, UI, export, parser.
	
	**Acceptance:**
	
	```txt
	existing job + CV builds context
	missing source URL handled
	same build reuses context
	canonical CV not mutated
	no active route behavior changes
	```
	
	**Tests:** mocked job/CV builder tests.
	
	**Rollback risk:** low.
	
	**Regression risks:** accidental assumptions about `CvDocument`.
	
	**Stop conditions:** rewriting profile mapper, parser, Proposal Forge.
	
	---
	
	## PR 4 — CareerKnowledge rules module
	
	**Goal:** Add product-owned writing/ATS/claim-safety rules.
	
	**Allowed:** static typed rules + resolver.
	
	**Forbidden:** raw PDF prompt stuffing, generation rewrite, UI.
	
	**Acceptance:** deterministic resolver, no duplicate rule IDs, market/document filtering.
	
	**Rollback risk:** tiny.
	
	---
	
	## PR 5 — Candidate facts import kernel
	
	**Goal:** Parse user-controlled text/Markdown/pasted content into fact candidates.
	
	**Allowed:** source document shell, fact extraction from text fixtures, dedupe hash.
	
	**Forbidden:** PDF/DOCX binary parsing unless already available and inspected; LinkedIn scraping; UI-heavy review.
	
	**Acceptance:** sourcePath preserved, duplicate source dedupes, pending facts not eligible.
	
	**Rollback risk:** moderate.
	
	**Stop conditions:** parser rewrite, external scraper.
	
	---
	
	## PR 6 — Candidate source documents persistence
	
	**Goal:** Store source docs and pending facts.
	
	**Allowed:** additive tables/functions.
	
	**Forbidden:** replacing `userProfiles`, CV Forge, parser.
	
	**Acceptance:** facts persisted pending approval; private/never_use fields exist; source hash index.
	
	**Regression risks:** privacy/storage mistakes.
	
	---
	
	## PR 7 — EvidenceGraph shadow module
	
	**Goal:** Build app-level evidence graph from job + CV/facts + rules.
	
	**Allowed:** pure graph builder, risk flags, claim validator.
	
	**Forbidden:** replacing premium cover-letter path.
	
	**Acceptance:** unsupported metrics/certs/languages/tools flagged; prompt injection from job ignored; deterministic output.
	
	**Regression risk:** low if shadow-only.
	
	---
	
	## PR 8 — ResumeVariantPlanV1
	
	**Goal:** Produce reviewable resume plan, no document generation.
	
	**Allowed:** plan artifact, selected facts, unsupported keywords, risk flags.
	
	**Forbidden:** mutating CV, generating final CV, UI.
	
	**Acceptance:** canonical CV/Profile unchanged; every plan item maps to fact IDs.
	
	---
	
	## PR 9 — Minimal review surface
	
	**Goal:** Show context/evidence/plan/risk for one application.
	
	**Allowed:** read-only page or dev-gated route.
	
	**Forbidden:** editor replacement.
	
	**Acceptance:** risks/missing visible; no fake artifacts; approval state explicit.
	
	---
	
	## PR 10 — Resume variant artifact
	
	**Goal:** Create separate resume variant artifact from approved plan.
	
	**Allowed:** `ApplicationArtifactV1.type="resume_variant"`.
	
	**Forbidden:** mutating canonical CV.
	
	**Acceptance:** provenance complete; reload-safe; unsupported claims blocked.
	
	---
	
	## PR 11 — Cover-letter artifact adapter
	
	**Goal:** Save a cover-letter artifact using existing writer path or generated proposal output.
	
	**Allowed:** adapter, artifact persistence.
	
	**Forbidden:** Proposal Forge rewrite.
	
	**Acceptance:** old Proposal Forge still works; approved artifact immutable; changed evidence creates new artifact.
	
	---
	
	## PR 12 — ApplicationPackageV1
	
	**Goal:** Bundle job + resume variant + letter + evidence + review state.
	
	**Allowed:** additive package table and route.
	
	**Forbidden:** campaigns, Scout, MCP.
	
	---
	
	## PR 13 — Internal tool contracts
	
	**Goal:** Typed internal tools over stable services.
	
	**Forbidden:** public MCP.
	
	**Acceptance:** no apply/send/submit; export/track require approval.
	
	---
	
	## PR 14 — Controlled Scout adapters
	
	**Goal:** Greenhouse/Lever/Ashby-style public job discovery.
	
	**Forbidden:** LinkedIn/Upwork/Indeed scraping.
	
	---
	
	## PR 15 — Local MCP beta
	
	**Goal:** Wrap internal tools locally.
	
	**Forbidden:** remote MCP, ChatGPT App, send/submit.
	
	---
	
	## Build later or defer indefinitely
	
	|Item|Verdict|
	|---|---|
	|LinkedIn scraping|**Kill for MVP**|
	|Upwork scraping|**Kill for MVP**|
	|Auto-apply / auto-submit|**Defer indefinitely** unless explicit consent/legal model exists|
	|Campaigns|Delay until packages work|
	|Google Docs/Sheets sync|Delay; export adapter only|
	|ChatGPT App|Last-mile distribution only|
	|Full Career Vault UI|Delay until import/review proves value|
	
	---
	
	# 7. Migration strategy
	
	## CV Forge
	
	Old CVs keep working because PRs 1–8 do not alter CV Forge routes, renderer, or canonical CV save paths. The new harness reads CV data as input and stores separate context/artifact records.
	
	**Rule:** resume variants must be separate artifacts or new CV documents, never updates to the canonical CV.
	
	## Proposal Forge
	
	Existing proposals keep working because artifacts are separate from the current `proposals` table. The current schema already stores proposal content, sections, metadata, and structured `proposalDocument` fields.
	
	**Rule:** cover-letter artifacts should not replace Proposal Forge state until a migration adapter exists.
	
	## JobsWorkspace
	
	Use existing jobs as source. The job table already has `sourceUrl`, `applicationUrl`, `dedupeKey`, `rawDescription`, summary, responsibilities, keywords, must-haves, status, and review items.
	
	**Rule:** ApplicationContext references jobs; it does not migrate jobs.
	
	## Active CV snapshots
	
	Do not treat active CV snapshots as complete career truth. They are lightweight proposal context and intentionally compressed.
	
	**Rule:** use snapshots only for compatibility, not Career Vault.
	
	## Parser/import pipeline
	
	Do not rewrite parser. Add source-document import wrappers that can use existing parser outputs where available.
	
	**Shadow-only:** CandidateFact extraction until approval UI exists.
	
	## Export
	
	Do not rewrite export. First, export only approved artifacts through existing export path when possible.
	
	**Approval gate:** no export before explicit approval.
	
	## Telemetry/debug proof before enabling UX
	
	Required debug data:
	
	```txt
	contextHash
	jobHash
	candidateHash
	rulesHash
	evidenceGraphHash
	run idempotencyKey
	artifact source hashes
	sourceFactIds used
	riskFlags count
	missing count
	approval record
	```
	
	---
	
	# 8. Quality gates and tests
	
	## Harness
	
	```txt
	same context input produces same contextHash
	changed job rawDescription changes jobHash
	changed candidate facts/CV changes candidateHash
	same operation input produces same idempotencyKey
	duplicate run returns/reuses existing run
	artifact reused for same sourceHashes
	approved artifact cannot be overwritten
	input objects are not mutated
	```
	
	## Career Vault
	
	```txt
	PDF import creates source document — only after current PDF path inspected
	DOCX import creates source document — only after DOCX path inspected
	text import creates source document
	Markdown import creates source document
	pasted text import creates source document
	LinkedIn export import maps source files without scraping
	duplicate source dedupes by contentHash
	fact sourcePath preserved
	conflict candidates detected
	user approval required before eligibility
	never_use/private facts never selected for public CV
	canonical CV not mutated
	```
	
	## Evidence
	
	```txt
	hard requirement matched to fact
	missing requirement flagged
	unsupported keyword rejected
	unsupported exact metric blocked
	unsupported certification blocked
	unsupported language blocked
	unsupported tool blocked
	old but relevant experience selectable
	multi-role profile suggests correct lens
	job-description prompt injection ignored
	job fluff cannot become candidate claim
	```
	
	## Resume variants
	
	```txt
	ResumeVariantPlan required before document generation
	summary rewrite uses selected facts only
	bullet reorder does not invent claims
	JD keywords added only when fact-backed
	canonical CV unchanged
	Career Vault unchanged
	provenance map complete
	variant survives refresh/reload
	approved variant not overwritten
	```
	
	## Cover-letter artifacts
	
	```txt
	existing Proposal Forge still works
	artifact linked to context/run/job/evidence
	approved artifact not overwritten
	changed evidence creates new artifact
	legacy proposal persistence unaffected
	writer output provenance validated
	unsupported numeric claim blocked
	```
	
	Existing premium tests already cover some of this for cover-letter provenance and writer safety.
	
	## Review UI
	
	```txt
	risk flags visible
	missing requirements visible
	export disabled before approval
	track disabled before approval
	no fake resume patch if no variant exists
	absent source URL does not crash
	```
	
	## Regression
	
	```txt
	CV Forge load/save unchanged
	Proposal Forge generation/edit/save unchanged
	export unchanged
	job import unchanged
	match review unchanged
	active CV snapshot unchanged
	premium cover-letter tests still pass
	```
	
	---
	
	# 9. Safety, privacy, and platform risk
	
	## Safe inputs
	
	```txt
	uploaded PDF resumes
	uploaded DOCX resumes
	uploaded plain text
	uploaded Markdown
	pasted profile text
	LinkedIn data export uploaded by user
	LinkedIn profile PDF uploaded by user
	Upwork/freelance export uploaded by user
	portfolio/project list supplied by user
	manual edits
	```
	
	LinkedIn data download is the safe path because LinkedIn documents a user-initiated data export flow and lists career-relevant categories like certifications, education, job applications, languages, positions, projects, saved jobs, skills, and resume data. ([LinkedIn](https://www.linkedin.com/help/linkedin/answer/a1339364/downloading-your-account-data "Download your account data | LinkedIn Help"))
	
	## Risky inputs
	
	```txt
	portfolio URLs
	imported Markdown
	job descriptions
	ATS pages
	copied third-party recommendations
	old resumes with stale dates
	freelance profiles with unverifiable claims
	```
	
	These need prompt-injection filtering, source labeling, and user review.
	
	## Forbidden actions
	
	```txt
	scrape LinkedIn
	scrape Upwork as MVP
	bypass anti-bot systems
	auto-submit applications
	auto-send emails
	auto-message recruiters
	rewrite canonical CV
	silently expose private facts
	export before approval
	track/apply before approval
	```
	
	## Approval-required actions
	
	```txt
	approve facts for eligibility
	create final resume variant
	approve cover letter
	export PDF/DOCX
	track application status
	send anything outside Twoweeks
	```
	
	## MCP/tool risk
	
	MCP tool definitions are model-discoverable and model-invoked; the spec recommends human-in-the-loop confirmation for operations and requires servers to validate inputs, implement access controls, rate-limit calls, sanitize outputs, and clients to show tool inputs and log usage. ([Model Context Protocol](https://modelcontextprotocol.io/specification/2025-06-18/server/tools "Tools - Model Context Protocol"))
	
	So your MCP phase needs:
	
	```txt
	tool allowlist
	approval gates
	structured outputs
	audit logs
	no private raw source document access by default
	no cross-user access
	no send/submit tools
	```
	
	## Audit logs needed
	
	```txt
	source document imported
	fact extracted
	fact approved/rejected/never_use
	context built
	evidence graph built
	artifact generated
	artifact approved
	export requested
	export completed
	tool invoked
	tool blocked
	```
	
	---
	
	# 10. Codex implementation strategy
	
	## What Codex should do first
	
	Codex should build **pure harness primitives** first:
	
	```txt
	schemas
	stable serialization
	hashing
	idempotency key builder
	unit tests
	decision doc
	```
	
	No active route wiring.
	
	## What Codex should never do in a broad pass
	
	```txt
	touch CV Forge UI
	rewrite Proposal Forge
	change export
	rewrite parser
	add MCP
	add Scout
	add browser automation
	change generation prompts
	run broad schema migration
	opportunistic refactors
	delete legacy support
	remove tests
	```
	
	## What belongs in AGENTS.md
	
	Only stable repo guardrails:
	
	```txt
	do not mutate canonical CV for variants
	do not scrape LinkedIn
	MCP must wrap internal tools only
	export/track/send/submit require approval
	Career Vault facts must keep provenance
	```
	
	Do not put the whole roadmap into `AGENTS.md`.
	
	## What belongs in SKILL.md
	
	Operational recipes:
	
	```txt
	how to add an application-harness module
	how to add a Career Vault import source
	how to write evidence graph tests
	how to run focused verification
	```
	
	## What belongs in docs/decisions
	
	Architecture decisions:
	
	```txt
	application harness kernel
	candidate evidence profile
	source document import policy
	evidence graph boundary
	resume variant immutability
	MCP delayed adapter decision
	```
	
	## What belongs in tests
	
	Behavior locks:
	
	```txt
	fingerprints
	idempotency
	immutability
	dedupe
	risk flags
	approval gates
	artifact reuse
	regression tests for CV/Proposal/export
	```
	
	## Feature flags
	
	```txt
	applicationHarnessV1
	applicationHarnessPersistenceV1
	careerVaultImportV1
	evidenceGraphShadowV1
	resumeVariantPlanV1
	applicationReviewV1
	internalAgentToolsV1
	```
	
	## Shadow mode
	
	```txt
	context builder
	evidence graph
	candidate fact extraction
	resume variant plan
	cover-letter artifact adapter
	```
	
	---
	
	## Exact first Codex prompt for PR 1
	
	```text
	Context:
	You are working in panamini/neyssan. Read AGENTS.md first. Treat v1 as the active baseline.
	
	Twoweeks is evolving toward a trusted job-application harness, but this PR must be a tiny additive kernel only. Existing CV Forge, Proposal Forge, export, parser/import, JobsWorkspace, active CV snapshots, proposal persistence, premium cover-letter generation, and match review must keep working unchanged.
	
	Goal:
	Add a pure TypeScript application harness kernel with deterministic schemas, fingerprints, and idempotency helpers. This PR must not add UI, Convex persistence, MCP, Scout, generation changes, parser changes, or route wiring.
	
	Scope:
	Allowed:
	- Add a new module under my-app/src/modules/application-harness/
	- Add pure TypeScript types/schemas for:
	  - ApplicationContextV1
	  - ApplicationRunV1
	  - minimal ApplicationArtifactV1 shell
	  - minimal ApplicationEventV1 shell
	- Add stable serialization and hash helpers
	- Add idempotency key builder
	- Add focused unit tests
	- Add one short decision doc in docs/decisions/
	
	Do NOT change:
	- CV Forge UI or state
	- Proposal Forge UI or state
	- proposal generation prompts
	- premiumCoverLetter.ts
	- export pipeline
	- parser/import pipeline
	- JobsWorkspace
	- activeCvSnapshots
	- Convex schema or Convex functions
	- package dependencies
	- route definitions
	- MCP / ChatGPT App / Scout code
	- styles or unrelated formatting
	
	Required work:
	1. Inspect existing test conventions and package scripts before adding tests.
	2. Create:
	   my-app/src/modules/application-harness/schema.ts
	   my-app/src/modules/application-harness/fingerprints.ts
	   my-app/src/modules/application-harness/idempotency.ts
	   my-app/src/modules/application-harness/__tests__/fingerprints.test.ts
	   my-app/src/modules/application-harness/__tests__/idempotency.test.ts
	   docs/decisions/YYYY-MM-DD-application-harness-kernel.md
	
	3. Define minimal types:
	   - ApplicationContextV1
	   - ApplicationRunV1
	   - ApplicationArtifactV1
	   - ApplicationEventV1
	
	1. Implement stable serialization:
	   - object keys sorted
	   - undefined omitted or normalized consistently
	   - arrays preserve order
	   - no mutation of input objects
	
	1. Implement fingerprint helpers:
	   - buildStableHash(value)
	   - buildJobHash({ jobId, rawDescription, sourceUrl, title, company })
	   - buildCandidateHash({ cvId, candidateEvidenceProfileId, structuredSectionsHash, cvSnapshotHash })
	   - buildSettingsHash(settings)
	   - buildContextHash({ jobHash, candidateHash, settingsHash })
	
	1. Implement idempotency:
	   - buildApplicationRunIdempotencyKey({
	       userId,
	       operation,
	       contextHash,
	       inputHash
	     })
	
	1. Add tests proving:
	   - same object with different key order hashes the same
	   - changed job text changes jobHash
	   - changed candidate hash input changes candidateHash
	   - changed settings changes settingsHash
	   - same operation input produces same idempotency key
	   - different operation changes idempotency key
	   - helper functions do not mutate input objects
	   - artifact/event shell types compile through test fixtures
	
	Constraints:
	- Smallest safe change.
	- No active route imports.
	- No schema migration.
	- No broad refactor.
	- No opportunistic cleanup.
	- No package additions.
	- Use existing project test framework.
	- Keep public behavior unchanged.
	
	Acceptance criteria:
	- New unit tests pass.
	- TypeScript passes for changed files or the narrowest available typecheck passes.
	- No existing user route behavior changes.
	- No UI changed.
	- No Convex schema changed.
	- No MCP added.
	- No generation output changed.
	- Decision doc explains:
	  - why this is pure/additive
	  - why persistence is deferred to PR 2
	  - why generation/UI/MCP/Scout are out of scope
	  - how this prepares idempotent application workflows
	
	Tests to add/run:
	- Add Vitest tests under the new module.
	- Run the narrowest relevant command, likely:
	  cd my-app
	  rtk npm test -- application-harness --run
	- If feasible, also run:
	  rtk npx tsc --noEmit
	
	Required output:
	- Short audit summary
	- Files changed
	- Tests run and results
	- What was verified
	- What remains deferred
	- Next smallest PR
	```
	
	## Stop conditions
	
	Stop Codex immediately if it:
	
	```txt
	touches CV Forge UI
	touches Proposal Forge UI
	changes proposal generation prompts
	edits premiumCoverLetter.ts
	changes export
	rewrites parser/import
	adds MCP
	adds Scout/job-source adapters
	adds browser automation
	changes Convex schema in PR 1
	adds package dependencies
	creates a Career Vault UI
	creates ApplicationPackageV1 table in PR 1
	adds campaigns
	adds Google/Drive/Docs integration
	adds apply/send/submit
	mutates canonical CVs
	deletes legacy support
	removes current tests
	does broad formatting/style rewrites
	```
	
	---
	
	# 11. Final recommended master plan
	
	## Improved final architecture
	
	```txt
	Current app remains:
	CV Forge
	Proposal Forge
	JobsWorkspace
	parser/import
	export
	active CV snapshots
	premium cover-letter path
	
	Add beside it:
	application-harness/
	  context, runs, hashes, artifacts, events
	
	career-vault/
	  source documents, candidate facts, visibility, approval
	
	career-knowledge/
	  ATS/resume/CV/cover-letter/claim-safety rules
	
	evidence-graph/
	  job demands, fact matches, allowed claims, missing/risk flags
	
	resume-variants/
	  plan first, document later, never mutate canonical CV
	
	application-review/
	  read-first approval cockpit
	
	application-packages/
	  bundle only after artifacts exist
	
	agent-tools/
	  internal contracts after services are stable
	
	mcp/
	  local/remote adapter last
	```
	
	## Improved PR roadmap
	
	```txt
	PR 1  Harness kernel, no persistence
	PR 2  Harness Convex persistence shadow tables
	PR 3  Context builder from existing job + CV, shadow only
	PR 4  CareerKnowledge rules
	PR 5  Candidate fact import kernel from safe text sources
	PR 6  Source docs + facts persistence, approval states
	PR 7  EvidenceGraph shadow module
	PR 8  ResumeVariantPlan artifact
	PR 9  Minimal review surface
	PR 10 Resume variant artifact/document
	PR 11 Cover-letter artifact adapter
	PR 12 ApplicationPackage
	PR 13 Internal tool contracts
	PR 14 Controlled ATS Scout adapters
	PR 15 Local MCP beta
	PR 16 Remote MCP / ChatGPT App exploration
	```
	
	## First implementation prompt
	
	Use the PR 1 prompt above. It is intentionally boring. That is the point.
	
	## Shortest possible strategy sentence
	
	**Build proof and idempotency before generation, packages, Scout, or MCP.**