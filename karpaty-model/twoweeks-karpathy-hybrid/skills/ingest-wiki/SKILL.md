---
name: ingest-wiki
description: >
  The hybrid write engine for a wiki vault that combines twoweeks-style durable knowledge
  management with Karpathy-style execution discipline. Supports four modes:
  ingest, direct-update, lint, and save-output. Read WIKI_SCHEMA.md first if present,
  then CLAUDE.md. Mutating operations require CLAUDE.md.
license: MIT
---

# ingest-wiki

Use this skill when you need a senior-engineer style mutation workflow:
explicit assumptions, minimal changes, and verification before completion.

## 1. Pick the mode

Choose the first matching mode:

- `ingest`
  - user says `ingest`
  - user asks to process `rawinput/`
  - user says they added a note, file, source, transcript, article, screenshot, or document to the wiki
- `lint`
  - user asks for a health check, lint, audit, consistency review, broken links check, or repo validation
- `save-output`
  - user asks to save the current answer, audit, report, architecture review, or analysis
- `direct-update`
  - any other explicit request to create, edit, move, merge, split, rename, reclassify, or repair wiki pages

Keep the existing skill name for compatibility.

## 2. Read sequence

Read in this order:

1. `WIKI_SCHEMA.md` if present
2. `CLAUDE.md`
3. `wiki/overview.md`
4. `wiki/index.md`
5. recent entries from `wiki/log.md`
6. inspect `rawinput/` when the task is ingest, lint, or repo-health work

Transition behavior:

- if both `WIKI_SCHEMA.md` and `CLAUDE.md` exist, use `WIKI_SCHEMA.md` for neutral discovery and `CLAUDE.md` as write authority
- if only `CLAUDE.md` exists, proceed normally
- if only `WIKI_SCHEMA.md` exists, allow read-only inspection and stop before mutating files
- if neither exists, stop and explain that the vault contract is missing

## 3. Mandatory preflight

Before any non-trivial write, state:

```text
Goal:
Assumptions:
Smallest safe change:
Verification:
```

Rules:

- if multiple interpretations exist, present them briefly instead of picking silently
- if a simpler approach exists, say so
- if uncertainty is material, ask or explicitly choose the safer interpretation
- do not continue with hidden confusion

## 4. Global rules

- never edit files under `raw/`
- ignore `rawinput/README.md`
- after every mutation, update `wiki/index.md` and `wiki/log.md`
- keep one active durable page per subject
- check for an existing page before creating a new one
- repair live references after any move, merge, split, or reclassification
- preserve historical log text unless it is meant to track the current active path
- keep pages compact, predictable, and easy to chunk
- use the category router and frontmatter contract in `CLAUDE.md`
- if `CLAUDE.md` is silent on a detail, fall back to `WIKI_SCHEMA.md`

Behavior constraints:

- do not overcomplicate the structure
- do not create speculative pages
- do not do drive-by cleanups
- every changed line should trace back to the request
- give a brief preview when useful, then proceed unless redirected

## 5. Ingest mode

### 5.1 Inspect staging

Scan `rawinput/`.
If there are no files other than `README.md`, stop and say that staging is empty.

### 5.2 Read and classify each file

For each staged file:

- read it fully
- identify the source type
- extract only the few facts that matter
- identify which durable pages should change
- detect contradictions or supersessions
- detect whether a new durable page is actually needed

### 5.3 Dedupe before writing

Before creating a source page, check whether the source already exists.

Use the strongest available signals:

- source URL
- normalized title
- file name
- same day plus same conversation/topic
- existing source page linked from the same durable page
- content hash if easy to obtain

If it is the same source, reuse the existing source page instead of creating a duplicate.

Before creating a new durable page, check for overlap with current pages in the same or adjacent categories.

### 5.4 Preview, then proceed

Give a short preview:

- what the source is
- which pages you will update or create
- whether supersede looks necessary
- how you will verify success

Then proceed unless the user redirects.

### 5.5 Write changes

1. Create or update the source page.
2. Update existing durable pages when they remain the best canonical pages.
3. Create a new durable page only when the subject is genuinely new.
4. If truth changed, apply supersede:
   - create or promote the replacement page
   - archive the old page
   - set `valid_until` and `superseded_by`
   - move it into `wiki/archive/...`
5. Move the staged file into `raw/` or `raw/assets/`.
6. Repair references.
7. Update `wiki/index.md` and `wiki/log.md`.
8. Update `wiki/overview.md` or `wiki/timeline.md` only when the project-level summary changed.

### 5.6 Verify and report

Verify:

- source page created or reused
- targeted durable pages updated
- rawinput item moved
- index updated
- log updated

Report:

- how many files were processed
- which pages were created
- which pages were updated
- which pages were archived or moved
- whether dedupe reused an existing source page
- what still looks unclear or worth investigating

## 6. Direct-update mode

Use this when the user wants explicit wiki edits without ingesting staged files.

Typical examples:

- create a new strategy page
- move a concept page into design
- merge two overlapping pages
- split an overloaded page
- repair links after a rename
- update a durable page from the current conversation

Apply the same rules as ingest, except there is no raw-file move.

Verification:

- only targeted pages changed
- no unrelated cleanup happened
- links repaired if paths changed
- index/log updated when persistent state changed

When the user asks to save analysis from the current conversation into durable knowledge, decide first:

- durable page if it changes canonical knowledge
- output page if it is a preserved analysis or snapshot

## 7. Lint mode

Lint is a repo health check.
Return findings in chat by default.
Only save the report when the user explicitly asks to preserve it.

Lint should check at least:

- missing or partial frontmatter
- invalid category or status values
- broken Obsidian links
- orphan current durable pages
- duplicate or overlapping current durable pages
- stale planned pages whose `valid_from` is in the past
- archived pages still referenced as current
- pages on disk missing from `wiki/index.md`
- pages in `wiki/index.md` missing on disk
- leftover files in `rawinput/`
- duplicate or near-duplicate source pages
- outputs being treated as canonical knowledge when a durable page exists
- obvious stats drift between the filesystem and the index summary

Group findings by severity:

1. correctness
2. retrieval quality
3. maintenance hygiene

For each finding, suggest the smallest safe fix.

## 8. Save-output mode

Create `wiki/outputs/YYYY-MM-DD-<slug>.md`.

Use the output contract from `CLAUDE.md`.
If `CLAUDE.md` does not define one, use:

```yaml
---
title: "Output title"
category: output
status: current
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: analysis
---
```

Recommended body shape:

```markdown
# Title

## Context
## Result
## Recommendations
## Verification
```

Then verify:

1. output file exists
2. it is added to the outputs section in `wiki/index.md`
3. a session entry was appended to `wiki/log.md`

## 9. Quality bar

The repo should converge toward this shape:

- one canonical durable page per subject
- clear category boundaries
- minimal duplication
- source pages as evidence
- output pages as preserved artifacts
- archive kept for history, not mixed with active truth
- predictable headings and compact pages
- no silent drift between files, index, and links
- no hidden assumptions in non-trivial mutations
- completion means verified outcome, not just written content

When in doubt, choose the simpler structure.
