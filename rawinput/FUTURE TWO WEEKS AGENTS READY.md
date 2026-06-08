

> **Twoweeks should be the data engine agents use to create truthful, tailored job applications.**

## Verdict

**Twoweeks is close in product idea, but not yet ready for the “agent-native” future described in the video.**

You already have the right ingredients: CV data, job scraping, proposal generation, extension, tracking, tone/style, templates, Convex backend. But right now Twoweeks is still mostly a **human-facing web app with AI inside**.

The video’s thesis is different: the winning products become **context + tools + workflows that outside agents can use**. Less “go to my website and click buttons.” More: **Codex / Cursor / Claude / ChatGPT can call Twoweeks, understand the user, create artifacts, show diffs, and ask the human to approve.** The transcript repeats this around agent-first work, context, less UI, API/service access, skills, demos, and brand/community.

## Video summary

The speaker’s core points:

1. **The future of work is supervision, not manual doing.** Humans give intent, taste, approval, and constraints. Agents do more of the execution.
    
2. **Software is becoming agent-consumed.** Products should expose clean context, services, and actions so agents can use them directly.
    
3. **Context is the product.** Bad AI output is usually a context problem. The product that gives the model the best structured context wins.
    
4. **UI becomes secondary.** The browser or app still exists, but as a review/supervision surface, not the only place where work happens.
    
5. **Skills, MCP, and agent integrations are the new distribution layer.** OpenAI’s current Codex docs already support project instructions via `AGENTS.md`, reusable skills, MCP servers, and a Codex SDK for programmatic control, so this direction is no longer speculative. ([OpenAI Developers](https://developers.openai.com/codex/guides/agents-md "Custom instructions with AGENTS.md – Codex | OpenAI Developers"))
    
6. **Demos matter as much as features.** A short, sharp demo that shows a real workflow can create distribution faster than a feature-heavy launch.
    
7. **Brand/community is the moat.** In AI, features get copied fast. The defensible layer becomes taste, workflow, trust, and a community that believes your product is “the place” for that job.
    

## What this means for Twoweeks

Twoweeks should not position itself as:

> “AI cover letter + resume generator.”

That market is already crowded. Simplify, LazyApply, JobCopilot, Teal-like tools, and many others already promise job matching, autofill, resume tailoring, cover letters, and tracking. Simplify, for example, positions itself around one profile powering matches, tailored resumes, networking, and tracking; LazyApply positions itself around automated applications across platforms; JobCopilot has resume, cover letter, tracker, and autofill messaging. ([Simplify Jobs](https://simplify.jobs/?utm_source=chatgpt.com "Simplify | AI Job Search Platform"))

Also, cover letters are becoming less defensible as a standalone product because AI-generated letters are increasingly commoditized and less trusted by hiring teams. The stronger angle is not “write me a letter.” It is:

> **Twoweeks is the agent-native job application operating system.**  
> It turns any job page into a reviewed, tailored, evidence-backed application package.

That means the user does not “use Twoweeks” only through the web app. Their agent can say:

> “Take this LinkedIn job, compare it to my best CV, draft the strongest version, show me the evidence, prepare the application, and ask before sending.”

## Readiness score

|Area|Twoweeks now|Agent-native target|Readiness|
|---|--:|--:|--:|
|CV/profile data|Strong base|Canonical structured context bundle|**7/10**|
|Job ingestion|Good via extension/scraper|Agent-callable job extraction API|**6/10**|
|Proposal generation|Working|Evidence-backed artifact generation with diffs|**6/10**|
|Resume tailoring|In progress/buggy areas|Safe patch/diff system, not full rewrite|**4/10**|
|Tracking|Present|Agent-readable application state machine|**5/10**|
|Agent integration|Mostly absent|MCP server, skills, API tools, Codex/Cursor/Claude setup|**2/10**|
|Supervision UX|Partial|Approval inbox, diffs, risk flags, “why this change”|**3/10**|
|Reliability|Not yet stable enough|Persistence, export, template, auth, extension all boringly solid|**4/10**|
|Distribution/demo|Early|One killer 45–60 sec demo|**3/10**|

**Overall: 5/10 as a product foundation. 2–3/10 as an agent-native platform.**

Not bad. But not ready yet.

## The real gap

The gap is not “more AI.”  
The gap is **agent affordance**.

Twoweeks needs to expose itself as a set of clean, reliable, inspectable tools:

### 1. Canonical context bundle

Create one object the agent can trust:

```ts
TwoweeksApplicationContext {
  userProfile
  baseCv
  selectedCv
  jobPost
  company
  extractedRequirements
  matchEvidence
  missingEvidence
  generatedArtifacts
  applicationStatus
  userPreferences
  safetyRules
}
```

This becomes the “brain” of Twoweeks. Every generator, export, tracker, and agent action reads/writes through it.

### 2. Agent-callable tools

Minimum useful tool surface:

```txt
tw_extract_job(url | rawText)
tw_score_fit(cvId, jobId)
tw_build_application_context(cvId, jobId)
tw_draft_resume_patch(contextId)
tw_draft_cover_letter(contextId)
tw_explain_changes(contextId)
tw_export_pdf(artifactId)
tw_track_application(contextId, status)
tw_prepare_interview(contextId)
```

This is the key. Codex, Claude Code, Cursor, ChatGPT, or your own agent should not need to click the UI.

### 3. MCP server / skill layer

Build a **Twoweeks MCP server** and a **Twoweeks skill**.

The skill tells the agent:

- when to use Twoweeks;
    
- how to parse a job;
    
- how to avoid hallucinating experience;
    
- how to create CV diffs;
    
- how to ask for approval;
    
- how to export final artifacts.
    

This matches where Codex and Figma are going: skills and MCP make agents work with real product context, not static docs. Figma’s 2026 agent/canvas announcement is a strong signal: major tools are opening product surfaces directly to agents, with skills encoding team standards and intent. ([Figma](https://www.figma.com/blog/the-figma-canvas-is-now-open-to-agents/ "Agents, Meet the Figma Canvas | Figma Blog"))

### 4. Human supervision mode

The UI should become less like “editor first” and more like:

```txt
Application Brief
→ Evidence Match
→ Resume Changes
→ Cover Letter
→ Risks / Missing Proof
→ Approve / Edit / Export / Track
```

The human should review **diffs and decisions**, not start from a blank composer.

### 5. Reliability before launch

Right now your recent bugs matter a lot: CV persistence, template persistence, rich text marks, image hydration, extension handoff, export consistency. In an agent-native product, bugs are worse because the agent multiplies actions. A broken persistence layer becomes broken automation.

So before pushing agent workflows, Twoweeks needs a boring-stable base:

- CV text persists after hard refresh.
    
- Template/style/font/image persist.
    
- Job link never disappears.
    
- Export matches preview.
    
- Generated document can be regenerated without destroying user edits.
    
- Extension → Forge handoff is deterministic.
    
- One application context has one source of truth.
    

## Competitive wedge

The strongest wedge is:

> **“Apply with proof, not slop.”**

Most AI job tools generate polished text. Twoweeks should generate **auditable applications**:

- every CV change is tied to a real experience;
    
- every cover letter claim has evidence;
    
- missing requirements are flagged instead of invented;
    
- user approves before export/apply;
    
- tracker remembers the exact version sent;
    
- interview prep is based on the same application context.
    

That is much more defensible than “better cover letters.”

## What to build next

### Priority 1 — Twoweeks Application Context

Build the canonical data object and make Proposal Forge, CV Forge, extension, and tracker all read/write through it.

**Acceptance test:** from one saved job, Twoweeks can reconstruct the job, CV, generated letter, tailored resume patch, source evidence, export status, and tracking status after hard refresh.

### Priority 2 — Diff-based resume tailoring

Do not let AI rewrite the whole CV freely. Make it propose patches:

```txt
Original bullet
→ Proposed bullet
→ Why changed
→ Evidence source
→ Risk level
```

This is where Twoweeks can feel premium and trustworthy.

### Priority 3 — Twoweeks MCP / local agent bridge

Expose the core workflow to Codex/Cursor/Claude:

```txt
“Use Twoweeks to prepare an application for this job URL using my main CV.
Show resume changes, letter, match score, and missing evidence. Do not export until approved.”
```

Codex already has MCP, skills, `AGENTS.md`, cloud tasks, and SDK support, so Twoweeks can ride this wave instead of inventing its own entire agent harness. ([OpenAI Developers](https://developers.openai.com/codex/cloud "Web – Codex | OpenAI Developers"))

### Priority 4 — Supervision inbox

Add a simple “Application Review” screen:

```txt
Job
Fit
Generated assets
Resume diffs
Letter
Risks
Approve
Export
Track
```

This becomes your MagicPath-style “human + agent workspace,” but for job applications.

### Priority 5 — Killer demo

One demo story only:

> “I’m on a job page. I ask Codex: use Twoweeks. It extracts the job, compares my CV, proposes three resume edits with evidence, writes a short letter, flags one missing requirement, exports a clean PDF, and adds it to my tracker. I only approve.”

That demo is stronger than showing 20 UI features.

## Final answer

**Twoweeks is not ready yet for the future described in the video.**  
But it is close enough that the right pivot is obvious.

Do **not** rebuild everything. Do **not** add a giant canvas. Do **not** chase generic auto-apply.

Build the **agent layer** on top of what you already have:

```txt
Structured context
+ callable tools
+ MCP/skills
+ diff-based supervision
+ evidence-backed generation
+ reliable export/tracking
```

That would make Twoweeks competitive because it stops being another AI writing tool and becomes the trusted application engine that agents can use.



> **Build the product as data + API calls first. UI is only the review surface.**

In the transcript, his example is: if he were building a legal AI company, he would not build a classic upload-documents website. He would build strong legal context/data so Codex or another agent can access it and work with the user’s PDFs directly. Same logic applies to Twoweeks.

## What this means for Twoweeks

Twoweeks should become less:

```txt
User opens app
→ clicks CV
→ clicks job
→ clicks generate
→ edits
→ exports
```

And more:

```txt
Agent receives job URL
→ asks Twoweeks for user/job/CV context
→ Twoweeks returns structured application data
→ agent drafts resume patch + cover letter
→ Twoweeks shows only review/approve/export
```

So the product is not mainly the interface.

The product is the **job application intelligence layer**.

## The real Twoweeks product

### Not this

```txt
AI resume builder
AI cover letter builder
Job tracker
Template editor
```

Too normal. Too much UI. Easy to copy.

### This

```txt
Twoweeks Context Engine

It gives agents everything they need to produce a truthful, tailored, application-ready package.
```

The UI becomes minimal:

```txt
Review.
Approve.
Export.
Track.
```

## The data Twoweeks must provide to the agent

This is the real moat:

```ts
ApplicationContext {
  userProfile,
  canonicalCv,
  jobPost,
  companyInfo,
  extractedRequirements,
  matchedEvidence,
  missingEvidence,
  resumePatchSuggestions,
  coverLetterDraft,
  riskFlags,
  applicationStatus,
  exportHistory
}
```

The agent should never guess.  
It should ask Twoweeks:

```txt
What does this user actually have proof for?
What does this job require?
What CV changes are safe?
What claims are risky?
What should be exported?
What was already sent?
```

## The API/tool layer Twoweeks needs

Minimum set:

```txt
tw_get_user_context()
tw_ingest_job(url | rawText)
tw_extract_requirements(jobId)
tw_match_cv_to_job(cvId, jobId)
tw_generate_resume_patches(contextId)
tw_generate_cover_letter(contextId)
tw_explain_application_strategy(contextId)
tw_export_pdf(artifactId)
tw_save_application(contextId)
tw_update_application_status(applicationId)
```

Then Codex / Cursor / Claude / ChatGPT can use Twoweeks without depending on the full UI.

## So should Twoweeks have “less UI”?

**Yes, but not ugly or empty.**

Less UI means:

|Keep UI for|Remove UI obsession around|
|---|---|
|Review|Manual setup|
|Approval|Too many editors|
|Diffs|Too many buttons|
|Export|Template tweaking first|
|Tracking|Big dashboards|
|Corrections|Repeating same forms|

The UI should feel like an **approval cockpit**, not a traditional document editor.

## Best direction

The strongest version of Twoweeks is:

```txt
APPLY. MOVE.

Paste a job.
Twoweeks builds the context.
Agent prepares the package.
You approve the truth.
PDF ready.
Tracker updated.
```

That is much closer to the video.

## Gap to fill

Right now Twoweeks still sounds like:

```txt
AI inside a job app.
```

It needs to become:

```txt
A job-application API that agents can use.
```

The biggest missing pieces are:

1. **Canonical ApplicationContext**
    
2. **Agent-callable API/tool layer**
    
3. **MCP or skill integration**
    
4. **Resume patch/diff system**
    
5. **Evidence/risk layer**
    
6. **Minimal review UI**
    
7. **Stable persistence/export**
    

## One-liner strategy

**Twoweeks should not be “the place where users manually create applications.”**

It should be:

> **The data engine agents use to create truthful, tailored job applications.**

That is the competitive version.