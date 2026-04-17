# CLAUDE.md — hybrid twoweeks + Karpathy operating contract

This file is the write-time source of truth for the hybrid vault.

Read `WIKI_SCHEMA.md` first for neutral discovery.
Read this file second for operational rules, behavior constraints, and verification.
Do not create a second competing rulebook.

## Project intent

This hybrid combines:

- the twoweeks wiki operating model for durable knowledge, retrieval, ingest, linting, and audit trails
- the Karpathy behavior layer for ambiguity control, simplicity, surgical edits, and goal-driven verification

The result should act like a senior engineer operating on a knowledge/code vault:
disciplined before writing, minimal while editing, and explicit about verification.

## Operating principles

- Keep one canonical durable page per subject.
- Prefer updating an existing page over creating a near-duplicate.
- Optimize for retrieval first. Clean structure beats clever prose.
- Keep raw sources immutable after ingest.
- `wiki/index.md` and `wiki/log.md` are mandatory after every mutation.
- Treat source pages as evidence and output pages as snapshots, not as the primary knowledge surface.
- Older historical references generally should not be rewritten unless they are actively misleading.
- On non-trivial work, define the goal and verify it instead of “just making changes”.
- Do not silently guess when multiple interpretations exist.

## Behavioral execution overlay

The original twoweeks contract is strong on structure and workflow.
The Karpathy layer improves behavior during execution.
These rules are mandatory in the hybrid.

### 1. Think before mutating

Do not assume. Do not hide confusion. Surface tradeoffs.

Before any non-trivial mutation:

- state the active source of truth
- name any ambiguity or competing interpretation
- prefer asking or explicitly choosing an interpretation over silently guessing
- push back on approaches that are broader or riskier than necessary
- explain when a simpler path is enough

Default preflight:

```text
Goal:
Assumptions:
Smallest safe change:
Verification:
```

### 2. Simplicity first

Choose the minimum change that solves the current problem.

- no speculative pages
- no extra category splits unless retrieval quality demands them
- no “future-proofing” abstractions in docs or workflows unless asked
- if one page update is enough, do not create three pages
- if a 200-line workflow rule could be 50 lines without losing clarity, simplify it

The test:
Would a senior engineer say this change added avoidable complexity?
If yes, simplify.

### 3. Surgical changes

Touch only what the request requires.

- do not reword adjacent sections just because you noticed stylistic issues
- do not clean up old history unless it became misleading
- do not rewrite comments, headings, or formatting outside the requested scope
- remove only the dead material created by your own change
- preserve existing style unless the task explicitly asks for a broader rewrite

The test:
Every changed line should trace back to the task.

### 4. Goal-driven execution

Turn vague requests into verifiable outcomes.

For each mode, define verification before writing:

- ingest → verify source page created or reused, affected durable pages updated, rawinput cleared, index/log updated
- direct-update → verify the targeted page(s) changed, links repaired, index/log updated if persistent
- lint → verify findings are grouped by severity and each finding maps to a smallest safe fix
- save-output → verify output exists, index updated, log entry appended

Do not stop at “made changes”.
Stop at “verified the requested outcome”.

## Vault layout

```text
hybrid-vault/
├── WIKI_SCHEMA.md
├── CLAUDE.md
├── rawinput/
├── raw/
│   └── assets/
├── skills/
│   └── ingest-wiki/
│       └── SKILL.md
├── .claude-plugin/
│   ├── plugin.json
│   └── marketplace.json
└── wiki/
    ├── index.md
    ├── log.md
    ├── overview.md
    ├── timeline.md
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
    └── tasks/
```

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
- do not over-abstract by inventing extra headings unless the content needs them

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
## Verification
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
- When in doubt between create and update, prefer update and explain the tradeoff.

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

## Mode-specific verification contracts

### Ingest

Verification checklist:

- staged file(s) read fully
- source page created or reused
- affected durable page(s) updated or new page created only if necessary
- supersede used only if truth changed
- raw file moved to `raw/` or `raw/assets/`
- `wiki/index.md` updated
- `wiki/log.md` updated
- `wiki/overview.md` or `wiki/timeline.md` updated only if project state changed

### Direct update

Verification checklist:

- requested page(s) updated with smallest safe diff
- no adjacent unrelated cleanup
- links repaired if paths changed
- `wiki/index.md` and `wiki/log.md` updated when persistent state changed

### Lint

Verification checklist:

- findings grouped by severity
- each finding ties to an observable file/path
- each finding suggests a smallest safe fix
- report distinguishes correctness vs retrieval quality vs hygiene

### Save output

Verification checklist:

- output file created under `wiki/outputs/`
- concise summary present
- `related` links added when useful
- `wiki/index.md` updated
- `wiki/log.md` appended with a save entry

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
