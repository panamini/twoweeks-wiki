



## Summary

Build a **Job Library** as the canonical place where scraped or pasted job offers are saved, stacked, reopened, and sent into document generation. Each saved job becomes a reusable object with source data, editable extracted context, and links to generated outputs. This follows the product vision’s **Job Record** model and the gap analysis priority to make jobs first-class without turning the product into a heavy CRM.

## Product goal

Make the core loop feel simple and repeatable:

**save job → understand job → generate document → keep everything linked**

The product vision already defines the extension-driven path as: import job, then choose to tailor resume, generate cover letter, or do both. The new Job Library should become the persistent layer behind that flow.

## Why now

The app already has the right ingredients:

- shell-level **Quick Start**
    
- a dedicated **cover-letter start** surface with “Bring in the job” and “Bring in your resume”
    
- Proposal Forge with imported source, raw job text, and extracted source summary
    

What is still missing is a durable place where saved jobs accumulate across sessions.

## Core user flow

1. User scrapes a job with the Chrome extension.
    
2. Extension sends the job into the app as a new **Job**.
    
3. The job appears in **Job Library**.
    
4. User opens that job and chooses:
    
    - **Generate cover letter**
        
    - **Tailor resume**
        
    - **Do both**
        
5. Generated documents are automatically linked back to that job.
    

This keeps the extension as the acquisition layer and Proposal Forge as the writing engine.

## Main surfaces

### 1. Job Library

A lightweight list of saved jobs.

Each row or card shows:

- job title
    
- company
    
- source
    
- status
    
- last activity
    
- linked resume count
    
- linked cover letter count
    

Primary actions:

- **Open job**
    
- **Generate cover letter**
    
- **Tailor resume**
    
- **Do both**
    

This page should feel like an inbox of opportunities, not a recruiter dashboard. That matches the roadmap direction better than shipping notes, CRM fields, or batch-apply mechanics too early.

### 2. Job Brief

Opening a job shows a compact **Job Brief** view.

Fields:

- raw job description
    
- source URL / platform
    
- title
    
- company
    
- location
    
- extracted keywords
    
- extracted responsibilities
    
- extracted tone cues
    
- linked documents
    

All extracted data must be editable. The trust rule is simple: no silent magic, no fake certainty, no irreversible parsing. That is consistent with the import and confidence principles already described in the product vision.

### 3. Proposal Forge handoff

Proposal Forge should open with the selected job already attached. The user should not have to re-paste the job every time. This builds directly on the current Proposal Forge structure instead of replacing it.

## V1 scope

Ship:

- Job object
    
- Job Library page
    
- extension save-to-library flow
    
- open job → Proposal Forge handoff
    
- linked documents on each job
    
- editable extracted summary
    

Do **not** ship in V1:

- notes
    
- activity timeline
    
- batch generation
    
- batch apply queues
    
- advanced ATS / CRM features
    
- complex status systems
    

The gap analysis is clear that activation, trust, and coherent job-aware flows matter more than extra management surface area right now.

## Information architecture

Add a top-level nav item: **Jobs**.  
The product vision already calls out Jobs as a top-level object in the target IA, while the current app routes still only expose CVs, proposals, style, and settings. This makes Jobs the right next structural addition.

## Data model

Use a lean V1 model:

- `id`
    
- `userId`
    
- `createdAt`
    
- `updatedAt`
    
- `sourceUrl`
    
- `sourceDomain`
    
- `sourceType`
    
- `importedAt`
    
- `title`
    
- `company`
    
- `location`
    
- `applicationUrl`
    
- `rawDescription`
    
- `rawLanguageDetected`
    
- `responsibilities[]`
    
- `keywords[]`
    
- `toneCues[]`
    
- `contacts[]`
    
- `linkedResumeIds[]`
    
- `linkedProposalIds[]`
    
- `status`
    

This stays aligned with the product vision’s Job Record idea while matching the actual extraction capabilities already present in the app, which currently produce role, company, location, responsibilities, keywords, tone cues, and contact details.

## Success metrics

Track:

- jobs imported per user
    
- job saved rate
    
- job to first doc time
    
- proposal generation from saved job
    
- linked documents per job
    
- duplicate / retarget usage later
    

These metrics fit the KPI framework already defined for activation, import trust, and retention.

## Product definition

**Job Library is the inbox of saved opportunities. Proposal Forge is the writing engine launched from each job.**

If you want, I’ll turn this into a stricter wiki page with frontmatter, status, related docs, and implementation notes in the exact style of your existing `twoweeks-wiki` pages.