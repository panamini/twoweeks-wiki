---
name: ingest-wiki
description: >
  The write engine for the twoweeks wiki. Use this skill for four modes:
  ingest (process files staged in rawinput/), direct-update (apply explicit wiki edits),
  lint (validate structure, links, metadata, and drift), and save-output
  (persist an answer, audit, analysis, or report to wiki/outputs/).
  Read WIKI_SCHEMA.md first if present, then CLAUDE.md.
  During the current transition, read-only inspection may work with WIKI_SCHEMA.md alone,
  but mutating operations require CLAUDE.md.
---

# ingest-wiki

Keep this skill deterministic.
Prefer updating canonical pages over creating new ones.
Do not introduce a second rulebook inside the skill.

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
The mode decides the behavior.

## 2. Locate and read the vault

A writable vault should contain:

- `wiki/index.md`
- `wiki/log.md`
- `rawinput/`
- `raw/`
- `CLAUDE.md`

Read order:

1. `WIKI_SCHEMA.md` if present
2. `CLAUDE.md` if present
3. `wiki/index.md`
4. recent entries from `wiki/log.md`
5. `wiki/overview.md` if the task needs project context

Transition behavior:

- if both `WIKI_SCHEMA.md` and `CLAUDE.md` exist, use `WIKI_SCHEMA.md` for neutral context and `CLAUDE.md` as the write authority
- if only `CLAUDE.md` exists, proceed normally
- if only `WIKI_SCHEMA.md` exists, allow read-only inspection and stop before mutating files
- if neither exists, stop and explain that the vault contract is missing

When reading `wiki/log.md`, read recent entries, not just the last physical lines.

## 3. Global rules

- Never edit files under `raw/`
- Ignore `rawinput/README.md`
- After every mutation, update `wiki/index.md` and `wiki/log.md`
- Keep one active durable page per subject
- Check for an existing page before creating a new one
- Repair live references after any move, merge, split, or reclassification
- Preserve historical log text unless it is meant to track the current active path
- Keep pages compact, predictable, and easy to chunk
- Use the category router and frontmatter contract in `CLAUDE.md`
- If `CLAUDE.md` is silent on a detail, fall back to `WIKI_SCHEMA.md`

Do not ask for blocking confirmation.
Give a brief preview when useful, then proceed unless the user redirects.

## 4. Ingest mode

Use ingest for staged files in `rawinput/`.

### 4.1 Inspect staging

Scan `rawinput/`.
If there are no files other than `README.md`, stop and say that staging is empty.

### 4.2 Read and classify each file

For each staged file:

- read it fully
- identify the source type
- extract the few facts that matter
- identify which durable pages should change
- detect whether the source contradicts an active page
- detect whether a new durable page is actually needed

### 4.3 Dedupe before writing

Before creating a source page, check whether the source already exists.

Use the strongest available signals:

- source URL
- normalized title
- file name
- same day plus same conversation/topic
- existing source page linked from the same durable page
- content hash or equivalent fingerprint if easy to obtain

If it is the same source, reuse the existing source page instead of creating a duplicate.

Before creating a new durable page, check for overlap with current pages in the same or adjacent categories.

### 4.4 Preview, then proceed

Give the user a short preview:

- what the source is
- which pages you will update or create
- whether supersede looks necessary

Then proceed unless the user redirects.

### 4.5 Write changes

1. Create or update the source page.
2. Update existing durable pages when they remain the best canonical pages.
3. Create a new durable page only when the subject is genuinely new.
4. If truth changed, apply supersede:
   - create or promote the replacement page
   - archive the old page
   - set `valid_until` and `superseded_by`
   - move it into `wiki/archive/...`
5. Move the staged file into `raw/` or `raw/assets/`.
6. Repair live references.
7. Update `wiki/index.md` and `wiki/log.md`.
8. Update `wiki/overview.md` or `wiki/timeline.md` only when the project-level summary changed.

### 4.6 Report

Tell the user:

- how many files were processed
- which pages were created
- which pages were updated
- which pages were archived or moved
- whether dedupe reused an existing source page
- what still looks unclear or worth investigating

## 5. Direct-update mode

Use this when the user wants explicit wiki edits without ingesting staged files.

Typical examples:

- create a new strategy page
- move a concept page into design
- merge two overlapping pages
- split an overloaded page
- repair links after a rename
- update a durable page from the current conversation

Apply the same rules as ingest, except there is no raw-file move.

When the user asks to save analysis from the current conversation into durable knowledge, first decide whether it belongs in a durable page or an output page:

- durable page if it changes the canonical knowledge
- output page if it is a preserved analysis or snapshot

## 6. Lint mode

Lint is a repo health check.
Return findings in chat by default.
Only save the report when the user explicitly asks for `save-output` or asks to preserve the audit.

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

When possible, suggest the smallest safe fix.

## 7. Save-output mode

Use save-output when the user wants the current answer preserved.

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
valid_from: YYYY-MM-DD
sources: []
related: []
type: analysis
---
```

Recommended body shape:

```markdown
# Title

## Context
## Result
## Recommendations
```

Then:

1. write the output page
2. add it to the outputs section in `wiki/index.md`
3. append a session entry to `wiki/log.md`

## 8. Quality bar

The repo should converge toward this shape:

- one canonical durable page per subject
- clear category boundaries
- minimal duplication
- source pages as evidence
- output pages as preserved artifacts
- archive kept for history, not mixed with active truth
- predictable headings and compact pages
- no silent drift between files, index, and links

When in doubt, choose the simpler structure.
