---
name: ingest-wiki
description: >
  The hybrid write engine for the twoweeks knowledge plane. Supports four modes:
  ingest, direct-update, lint, and save-output. Read WIKI_SCHEMA.md first if present,
  then the write-time contract (AGENTS.md or CLAUDE.md). Mutating operations require
  the write-time contract.
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
2. `AGENTS.md` and/or `CLAUDE.md`
3. `wiki/hot.md` if present
4. `wiki/overview.md`
5. `wiki/index.md`
6. recent entries from `wiki/log.md`
7. inspect `rawinput/` when the task is ingest, lint, or repo-health work

Transition behavior:

- if both `AGENTS.md` and `CLAUDE.md` exist, treat `CLAUDE.md` as canonical and `AGENTS.md` as compatibility routing
- if only one write-time contract exists, proceed with it
- if only `WIKI_SCHEMA.md` exists, allow read-only inspection and stop before mutating files
- if neither exists, stop and explain that the vault contract is missing

When reading `wiki/log.md`, read recent entries, not just the last physical lines.

## 2.1 Active memory retrieval

Treat `wiki/hot.md` as the cheap LLM memory gateway, not as a heavy wiki lookup.
Keep it under 500 words whenever you update it. It is a cache, not a journal.

Read `wiki/hot.md` first when the request touches the project, product, parser, design,
tech architecture, jobs, brand, wiki operations, or local workflow.

Use these query modes when the user asks a knowledge question or when you need context:

| Mode | Reads | Use when |
| --- | --- | --- |
| `quick` | `wiki/hot.md` and the retrieval map / top section of `wiki/index.md` | simple lookup, active context, or finding the owning page |
| `standard` | `wiki/hot.md`, `wiki/index.md`, and 1-3 targeted pages | normal product, tech, design, or wiki questions |
| `deep` | `wiki/hot.md`, `wiki/index.md`, recent `wiki/log.md`, and every relevant page | audits, synthesis, duplicate review, or migration planning |

If `wiki/hot.md` answers the question or points to the canonical page, do not broaden the read set.
If it is stale or missing, fall back to `wiki/overview.md` and `wiki/index.md`.
Never treat `wiki/hot.md` as canonical truth when it conflicts with a current durable page.

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
- after every mutation, update `wiki/index.md`, `wiki/log.md`, and `wiki/hot.md`
- keep one active durable page per subject
- check for an existing page before creating a new one
- repair live references after any move, merge, split, or reclassification
- preserve historical log text unless it is meant to track the current active path
- keep pages compact, predictable, and easy to chunk
- use the category router and frontmatter contract in the write-time contract
- if the write-time contract is silent on a detail, fall back to `WIKI_SCHEMA.md`

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
7. Update `wiki/index.md`, `wiki/log.md`, and `wiki/hot.md`.
8. Update `wiki/overview.md` or `wiki/timeline.md` only when the project-level summary changed.

### 5.6 Verify and report

Verify:

- source page created or reused
- targeted durable pages updated
- rawinput item moved
- index updated
- log updated
- hot cache updated

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
- hot cache updated when active context or likely retrieval routes changed

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

Use the output contract from the write-time contract.
If the write-time contract does not define one, use:

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
4. `wiki/hot.md` was updated if the output should shape near-term retrieval

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
