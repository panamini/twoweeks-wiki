# CLAUDE.md — twoweeks operational wiki contract

This file is the operational source of truth for mutations in this vault.

If `WIKI_SCHEMA.md` exists, read it first for neutral vocabulary.
Then read this file for the live write contract.
Do not create a second competing rulebook.

## Project

twoweeks is a high-performance job application product.
Use `wiki/overview.md` for current business and product state.
This file defines how the wiki is structured and maintained.

## Operating principles

- Keep one canonical durable page per subject.
- Prefer updating an existing page over creating a near-duplicate.
- Optimize for retrieval first. Clean structure beats clever prose.
- Keep raw sources immutable after ingest.
- `wiki/index.md` and `wiki/log.md` are mandatory after every mutation.
- Treat source pages as evidence and output pages as snapshots, not as the primary knowledge surface.
- Older historical references generally should not be rewritten unless they are actively misleading.

## Vault layout

```text
twoweeks/
├── WIKI_SCHEMA.md            # optional neutral discovery file
├── CLAUDE.md                 # operational write contract
├── rawinput/                 # staging area for new files
├── raw/                      # immutable ingested source library
│   └── assets/               # local images and binary assets
└── wiki/
    ├── index.md              # catalog of active and planned pages
    ├── log.md                # chronological mutation log
    ├── overview.md           # short current-state summary
    ├── timeline.md           # optional project timeline
    ├── entities/
    ├── concepts/
    ├── design/
    ├── product/
    ├── strategy/
    ├── tech/
    ├── howto/
    ├── meta/
    ├── sources/
    ├── outputs/
    ├── archive/
    │   ├── entities/
    │   ├── concepts/
    │   ├── design/
    │   ├── product/
    │   ├── strategy/
    │   ├── tech/
    │   ├── howto/
    │   ├── meta/
    │   └── sources/
    └── tasks/                # optional, excluded from default retrieval
```

`index.md`, `log.md`, `overview.md`, and `timeline.md` are system files.
They are not normal category pages.

## Page contract

### Required frontmatter

Use this frontmatter on every wiki page:

```yaml
---
title: "Page title"
category: entity | concept | design | product | strategy | tech | howto | meta | source | output | task | overview
status: current | planned | archived | deprecated
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

### Optional frontmatter

Use only when relevant:

```yaml
tags: []
sources: []
related: []
valid_from: YYYY-MM-DD
valid_until: YYYY-MM-DD
superseded_by: "[[replacement-page]]"
version: v2
type: spec | conversation | runbook | analysis | other
```

### Field rules

- `status`
  - `current` — the active page to use by default
  - `planned` — future intended state
  - `archived` — historically valid but no longer active
  - `deprecated` — explicitly rejected or obsolete
- `tags`, `sources`, `related` are optional.
- `valid_from` is conditional; use it when the page is time-bound, planned, or when the start of validity matters.
- `valid_until` is conditional; set it only for `archived` or `deprecated` pages.
- `superseded_by` is conditional; set it only when a page is replaced by another page.
- `version` is optional; use it only when the page is tied to a specific project or product version.
- `type` is optional; it is mainly useful on source and output pages.
- Do not emit empty optional or temporal fields.
- Do not use `horizon` on new or edited pages. Legacy pages may still contain it until they are touched.

## Category routing

Use the smallest stable page type that matches the subject.

| Category | Directory | Use when |
| --- | --- | --- |
| `entity` | `wiki/entities/` | person, company, product, tool, competitor |
| `concept` | `wiki/concepts/` | durable idea, principle, pattern, policy, architecture concept |
| `design` | `wiki/design/` | UI system, visual rules, template system, ATS/layout guidance |
| `product` | `wiki/product/` | problem framing, feature definition, roadmap, KPI, user-facing capability |
| `strategy` | `wiki/strategy/` | market analysis, competition, positioning, GTM, prioritization rationale |
| `tech` | `wiki/tech/` | code architecture, infra, interfaces, call paths, implementation constraints |
| `howto` | `wiki/howto/` | repeatable operational procedure or runbook |
| `meta` | `wiki/meta/` | wiki rules, schema, conventions, maintenance docs |
| `source` | `wiki/sources/` | summary of an ingested source |
| `output` | `wiki/outputs/` | saved answer, audit, analysis, or deck |
| `task` | `wiki/tasks/` | operational backlog, sprint notes, migration notes |
| `overview` | system files | control pages such as index, log, overview, timeline |

## File naming

- Durable pages use a stable kebab-case slug.
- Source pages use `YYYY-MM-DD-<slug>.md`.
- Output pages use `YYYY-MM-DD-<slug>.md`.
- Archived pages keep the same slug under `wiki/archive/<directory>/`.
- Do not use spaces in directory names or filenames.

## Page body shape

Keep headings shallow and predictable.
One page should cover one subject.

### Durable pages

Use this default shape unless the page genuinely needs less:

```markdown
# Title

One-paragraph summary.

## Current state
## Details
## Sources
## Related
```

Rules:
- one durable subject per page
- split pages that become bags of unrelated facts
- keep current state near the top
- prefer stable subheadings and small sections

### Source pages

```markdown
# Title

## Summary
## Key points
## Implications
## Touched pages
```

### Output pages

```markdown
# Title

## Context
## Result
## Recommendations
```

Do not pad pages with quotes, screenshots, or history unless they change decisions or retrieval value.

## Retrieval order

For normal questions, read in this order:

1. durable pages with `status: current`
2. durable pages with `status: planned` only when the question is about future state
3. relevant source pages for evidence or newly ingested details not yet merged
4. output pages only when the user asks for a previous analysis, audit, or saved answer
5. archived or deprecated pages only for historical queries

Default answer behavior:

- prefer durable pages over sources
- prefer sources over outputs
- ignore archive unless the question is historical
- never treat `wiki/tasks/` as canonical knowledge

## Mutation rules

### Create vs update

- Update an existing durable page when the same page is still the best canonical home for the new information.
- Create a new durable page only when the subject is genuinely new or the current page is overloaded and should be split.
- Do not create multiple active pages for the same subject with slightly different wording.

### Supersede

Use supersede only when the active truth changes.

1. Create or promote the replacement page with `status: current` and a fresh `valid_from` when relevant.
2. Mark the old page `status: archived`.
3. Set `valid_until` on the old page.
4. Set `superseded_by` on the old page.
5. Move the old page to the matching archive directory.
6. Repair active references that should now point to the new page.
7. Update `timeline.md` only if the project state or decision history changed materially.

Do not supersede a page just because you added detail.
Most updates should stay in place.

### Reference repair

After any move, reclassification, or rename-like change:

- update active wikilinks in live pages
- update `wiki/index.md`
- update current-path references in `wiki/log.md` only when they are meant to track the active location
- preserve historical log text that intentionally describes an old path or old state

## Workflows

### Ingest

Use ingest when processing staged files in `rawinput/`.

1. Read `WIKI_SCHEMA.md` if present.
2. Read `CLAUDE.md`.
3. Read `wiki/overview.md`.
4. Read `wiki/index.md`.
5. Read recent entries from `wiki/log.md`.
6. Check `rawinput/` and ignore `README.md`.
7. For each file, read it fully and identify:
   - source type
   - key facts
   - affected durable pages
   - contradictions or supersessions
   - new pages, if any
8. Check whether the same source already exists:
   - same URL
   - same normalized title
   - same day plus same conversation/topic
   - same staged file moved earlier
9. Give the user a short preview of intended changes, then proceed unless they redirect.
10. Create or reuse the source page.
11. Update existing durable pages or create new ones through the category router.
12. Supersede only when truth changed.
13. Move the raw file to `raw/` or `raw/assets/`.
14. Repair references.
15. Update `wiki/index.md` and `wiki/log.md`.
16. Update `wiki/overview.md` or `wiki/timeline.md` only when the project-level summary actually changed.

### Direct update

Use direct update when the user asks to create, edit, move, reclassify, or merge wiki pages without ingesting new raw files.

Apply the same category, dedupe, supersede, and reference-repair rules.
Do not touch `raw/` unless the task is ingest.

### Lint

Lint is a repo health check.
By default it reports in chat.
Save the report to `wiki/outputs/` only when the user explicitly asks to preserve it.

Lint checks should include:

- missing or partial frontmatter
- invalid category or status values
- broken Obsidian links
- orphan current durable pages
- duplicate or overlapping current durable pages that should merge or supersede
- stale planned pages whose `valid_from` is in the past
- archived pages still referenced as current
- filesystem vs `wiki/index.md` drift
- leftover files in `rawinput/`
- source pages that were created but never linked into durable knowledge
- output pages being used as if they were canonical source of truth

### Save output

Use save output when the user wants the current answer, audit, or analysis preserved.

1. Create `wiki/outputs/YYYY-MM-DD-<slug>.md`.
2. Start with a concise summary.
3. Link the relevant durable pages or sources in `related`.
4. Update `wiki/index.md`.
5. Append a `query-save` entry to `wiki/log.md`.

## Index and log rules

### `wiki/index.md`

- list active and planned pages
- group by category
- keep archived pages out of the active catalog
- include outputs in a separate section
- include tasks in a separate section without treating them as default durable retrieval targets
- keep the stats block consistent with the filesystem

### `wiki/log.md`

- record every mutation session
- one entry per session is the default
- include created, updated, archived, moved, and output pages
- do not log pure read/query sessions unless the user asked for a saved output

## Session bootstrap

Default read sequence:

1. `WIKI_SCHEMA.md` if present
2. `CLAUDE.md`
3. `wiki/overview.md`
4. `wiki/index.md`
5. recent entries from `wiki/log.md`
6. check whether `rawinput/` contains staged files

Do not front-load unnecessary files for a narrow query.

## Maintenance rules

- `raw/` is immutable.
- `rawinput/` should be empty after ingest.
- always update `wiki/index.md` and `wiki/log.md` after persistent changes.
- prefer updating or superseding over duplicating.
- keep `overview.md` high level.
- keep `timeline.md` for project history, not general note accumulation.
- use Obsidian links for internal references.
- keep the control plane simple.
- do not add tooling layers unless there is a clear operational gain.
