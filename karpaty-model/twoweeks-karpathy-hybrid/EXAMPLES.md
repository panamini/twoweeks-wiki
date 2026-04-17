# Hybrid Examples

Real-world examples showing how the hybrid layer behaves differently from the original twoweeks contract and from a generic Karpathy-only behavior layer.

---

## 1. Think Before Mutating

### User request
“Add a page for interviews.”

### Bad behavior
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

---

## 2. Simplicity First

### User request
“Capture the new resume-review feature.”

### Bad behavior
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

---

## 3. Surgical Changes

### User request
“Fix the incorrect category on the ATS guidance page.”

### Bad behavior
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

---

## 4. Goal-Driven Execution

### User request
“Ingest the notes I dropped into rawinput.”

### Weak completion
“I processed the notes.”

### Better hybrid completion
Preflight:

```text
Goal: ingest the staged notes into canonical wiki knowledge
Assumptions: the notes are net-new, not a duplicate source
Smallest safe change: create or reuse one source page and update only affected durable pages
Verification:
- rawinput is empty except README
- source page exists
- touched durable pages are updated
- wiki/index.md updated
- wiki/log.md updated
```

Then execute and verify each item before reporting completion.

---

## 5. Lint With Smallest Safe Fixes

### User request
“Lint the vault.”

### Bad behavior
- returns a long undifferentiated list
- suggests broad reorganization
- proposes deleting historical material without asking

### Better hybrid behavior
Group findings by:

1. correctness
2. retrieval quality
3. maintenance hygiene

For each finding, propose the minimum safe fix, such as:
- add missing frontmatter field
- repair one broken wikilink
- merge two overlapping current pages
- archive one stale planned page that is now in the past

---

## 6. Save Output Without Polluting Canonical Knowledge

### User request
“Save this audit.”

### Bad behavior
- writes the audit into a durable page under `wiki/strategy/`
- later teams mistake it for canonical truth

### Better hybrid behavior
- create `wiki/outputs/YYYY-MM-DD-audit-slug.md`
- keep the analysis as a snapshot
- link related durable pages in `related`
- update `wiki/index.md`
- append a save entry to `wiki/log.md`

That preserves the analysis without replacing canonical knowledge.
