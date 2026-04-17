# Hybrid Examples

These examples show how the twoweeks hybrid layer should behave across both planes of this repository:

- the **knowledge plane** for wiki ingest, durable pages, lint, and saved outputs
- the **code plane** for repo audits, bug fixes, feature work, and measurable verification

The point of the hybrid is not just to "do the task."
It should choose the smallest safe change, avoid hidden assumptions, and verify completion explicitly.

## Knowledge plane examples

## 1. Think before mutating

### User request

“Add a page for interviews.”

### Weak behavior

- silently creates `wiki/product/interviews.md`
- assumes product instead of howto or strategy
- adds three speculative subpages for mock interviews, rubric, and ATS prep

### Better hybrid behavior

First surface interpretations:

1. `wiki/howto/interviews.md` if the user wants an operational playbook
2. `wiki/product/interviews.md` if this is a user-facing feature area
3. `wiki/strategy/interviews.md` if this is positioning or GTM language

Then choose the smallest safe change and explain why.
Only after that should the page be created or updated.

## 2. Simplicity first

### User request

“Capture the new resume-review feature.”

### Weak behavior

- creates a product page
- creates a concept page
- creates a strategy page
- creates a design page
- adds a timeline entry and a task list without evidence that all are needed

### Better hybrid behavior

- update the existing feature page if one already covers resume review
- create one new durable page only if the subject is genuinely new
- add a source page only if a staged source exists
- update `overview.md` only if the project-level summary changed

The hybrid treats extra pages as cost, not as proof of rigor.

## 3. Surgical changes

### User request

“Fix the incorrect category on the ATS guidance page.”

### Weak behavior

- reclassifies the page
- rewrites unrelated headings
- renames nearby files
- reflows the whole document for style consistency

### Better hybrid behavior

- change the frontmatter category
- move the file only if the directory path must change
- repair affected wikilinks
- update `wiki/index.md` and `wiki/log.md`
- leave unrelated prose, headings, and formatting alone

Every changed line should map to the category fix.

## 4. Goal-driven execution

### User request

“Ingest the notes I dropped into rawinput.”

### Weak completion

> “I processed the notes.”

### Better hybrid completion

Preflight:

```text
Goal:
ingest the staged notes into canonical wiki knowledge

Assumptions:
the notes are net-new, not a duplicate source

Smallest safe change:
create or reuse one source page and update only affected durable pages

Verification:
- rawinput is empty except README
- source page exists
- touched durable pages are updated
- wiki/index.md updated
- wiki/log.md updated
```

Then execute and verify each item before reporting completion.

## 5. Lint with smallest safe fixes

### User request

“Lint the vault.”

### Weak behavior

- returns a long undifferentiated list
- suggests broad reorganization
- proposes deleting historical material without asking

### Better hybrid behavior

Group findings by:

1. correctness
2. retrieval quality
3. maintenance hygiene

For each finding, propose the minimum safe fix, such as:

- add one missing frontmatter field
- repair one broken wikilink
- merge two overlapping current pages
- archive one stale planned page that is now in the past

## 6. Save output without polluting canonical knowledge

### User request

“Save this audit.”

### Weak behavior

- writes the audit into a durable page under `wiki/strategy/`
- later teams mistake it for canonical truth

### Better hybrid behavior

- create `wiki/outputs/YYYY-MM-DD-audit-slug.md`
- keep the analysis as a snapshot
- link related durable pages in `related`
- update `wiki/index.md`
- append a save entry to `wiki/log.md`

That preserves the analysis without replacing canonical knowledge.

## Code plane examples

## 7. Bug fix: reproduce before changing code

### Weak behavior

> “Search is broken on duplicate scores, I updated the sorter and cleaned up some helper functions.”

Problems:

- no proof the bug was reproduced
- no proof the fix works
- unrelated helpers were changed

### Hybrid behavior

```text
Goal:
Fix duplicate-score ordering without changing unrelated ranking behavior.

Assumptions:
The owner is the ranking utility used by the search endpoint.

Smallest safe change:
Add one failing test for duplicate scores, then fix the local tie-break logic only.

Verification:
1. New test fails before the fix.
2. New test passes after the fix.
3. Existing ranking tests still pass.
```

## 8. Feature: avoid speculative architecture

### Weak behavior

> “I added a generic plugin system for exporters because we might add more formats later.”

Problems:

- abstraction added for a future that was not requested
- more code and more maintenance surface than needed

### Hybrid behavior

```text
Goal:
Add CSV export for the current report endpoint.

Assumptions:
Only CSV is required right now.

Smallest safe change:
Add one CSV formatter in the existing report module and one acceptance test.

Verification:
1. Endpoint returns CSV with the requested columns.
2. Existing JSON behavior is unchanged.
```

## 9. Repo audit: criteria instead of vibes

### Weak behavior

> “The repo looks decent, but I would refactor a lot of things.”

Problems:

- subjective
- not benchmarkable
- no next action path

### Hybrid behavior

Audit against explicit criteria:

- assumption / preflight discipline
- simplicity rules
- surgical diff discipline
- verification rules
- source roots and ownership clarity
- tests near behavior
- CI / lint / build presence
- artifact/reporting readiness

Then group findings by:

1. correctness risk
2. leverage / missing functionality
3. hygiene

## 10. Knowledge-plane repository with no application code

### Weak behavior

> “The repo is a codebase because I found some JavaScript files, so I’ll treat the Obsidian plugins as app code.”

Problems:

- hidden tooling files are misclassified as product code
- repo audit becomes misleading
- follow-up recommendations target the wrong surface

### Hybrid behavior

```text
Goal:
Audit the real code plane without confusing wiki tooling for application code.

Assumptions:
This repository may currently be knowledge-plane-only.

Smallest safe change:
Ignore Obsidian, wiki, and raw storage directories when scoring code-plane structure.

Verification:
1. The repo audit reports whether a real code plane is present.
2. Obsidian plugin files no longer count as application source.
3. The instruction-layer score still reflects the rule quality.
```
