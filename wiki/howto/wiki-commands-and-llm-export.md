---
title: "Wiki Commands and LLM Export"
category: howto
status: current
created: 2026-05-02
updated: 2026-05-02
tags: [wiki, codex, retrieval, memory]
related: [[hot]], [[index]], [[meta/llm-wiki-pattern]], [[meta/codex-prompting-standards]]
---

# Wiki Commands and LLM Export

Use this page to operate the wiki as an active LLM memory without adding extra structure.

## Commands

The trigger does not need to be exact. The intent matters.

| Intent | Say this | Result |
|--------|----------|--------|
| Ingest staged sources | `ingest rawinput/` or "process the files in rawinput" | Reads `rawinput/`, creates or reuses source pages, updates durable pages, moves files into `raw/` |
| Update knowledge | `direct-update` or "update the page about X" | Updates, merges, splits, renames, or reclassifies wiki pages |
| Check health | `lint` or "health check the wiki" | Reports broken links, duplicates, frontmatter gaps, index drift, stale references |
| Save an answer | `save-output` or "save this analysis" | Creates an output page and updates index/log |
| Query memory | "search the wiki for X" or "what is the canonical page for X?" | Reads `wiki/hot.md`, then `wiki/index.md`, then targeted pages |

## Agent Memory Command

Use this when starting a new LLM agent on the repo:

```text
Use this wiki as your project memory. Whenever you need twoweeks project context, read WIKI_SCHEMA.md and CLAUDE.md, then read wiki/hot.md first. If hot.md is enough, stop there. If not, use the Retrieval Map in wiki/index.md and open only the targeted canonical pages. Do not treat hot.md as canonical truth when it conflicts with durable pages.
```

Short version:

```text
Use the wiki as memory. For project context, check wiki/hot.md first, then wiki/index.md, then only the relevant canonical pages.
```

For read-only questions, start broad in meaning, not syntax. Examples:

- "Which page owns parser truth?"
- "What should I read for Job Library?"
- "Does the wiki already have a page for X?"
- "Find duplicates or overlap around X."

## Retrieval Modes

| Mode | Reads | Use when |
|------|-------|----------|
| `quick` | `wiki/hot.md` and the Retrieval Map in `wiki/index.md` | lookup, active context, finding the owning page |
| `standard` | `wiki/hot.md`, `wiki/index.md`, and 1-3 pages | normal product, tech, design, or wiki questions |
| `deep` | `wiki/hot.md`, `wiki/index.md`, recent `wiki/log.md`, and all relevant pages | audit, migration, duplicate review, synthesis |

Keep `wiki/hot.md` under 500 words. It is a cache, not a journal.

## `wiki/llms.txt` Proposal

`wiki/llms.txt` would be a generated read-only export for agents.
It should combine:

- the current `wiki/hot.md`
- the Retrieval Map from `wiki/index.md`
- short pointers to the most important canonical pages

It should not replace `wiki/index.md`, `wiki/log.md`, or durable pages.

## Positive Points

- Lower context cost than opening `wiki/index.md` and several pages.
- Clearer entrypoint for external agents that do not know the repo contract.
- Easier to pass into tools that expect a single text memory file.
- Keeps the write path unchanged if generated read-only.

## Negative Points

- Adds one more artifact that can become stale.
- Needs a generation rule or script, otherwise it becomes manual noise.
- Can create confusion if people start editing it directly.
- Does not solve dedupe or source integrity by itself.

## Advantages

- Best fit when another agent needs quick context but should not crawl the vault.
- Useful for Claude Code, Codex, CLI agents, and future automation.
- Safer than MCP/REST writes because it is only an export.
- Compatible with the current `rawinput/ -> raw/` ingest flow.

## Disadvantages

- It is not worth doing if only this repo's Codex instance reads the wiki.
- It has real value only if generated deterministically from canonical files.
- It should be ignored for write-time truth; durable pages stay canonical.

## Recommendation

Do not build it until `wiki/hot.md` proves useful in daily work.
If built, make it generated, read-only, and small:

```text
wiki/hot.md
Retrieval Map from wiki/index.md
Top canonical page pointers
```

No MCP, no auto-commit hook, no local `_index.md` expansion for this step.

## Implementation Plan for `wiki/llms.txt`

### P0: Do not build yet

Use `wiki/hot.md` in daily work for a short trial.

Acceptance:

- agents consistently read `wiki/hot.md` first
- `wiki/hot.md` stays under 500 words
- common questions route to the correct canonical pages

### P1: Generate a simple export

Create `wiki/llms.txt` from canonical files only.

Content:

- title and purpose
- full `wiki/hot.md` body
- Retrieval Map extracted from `wiki/index.md`
- 10-20 canonical page pointers, not full page bodies
- warning that durable pages remain canonical

Rules:

- generated read-only artifact
- no manual edits
- no source movement
- no `raw/` writes
- update only after `hot.md` or `index.md` changes

### P2: Add a generator script

Add a small deterministic script only if manual generation becomes annoying.

Recommended path:

```text
scripts/generate_llms_txt.py
```

Inputs:

- `wiki/hot.md`
- `wiki/index.md`
- optional allowlist of canonical pages

Output:

- `wiki/llms.txt`

Verification:

- output exists
- output says it is generated
- output references canonical pages instead of duplicating all content
- `wiki/hot.md` remains under 500 words

### P3: Only if multiple agents use it

Add a stricter export such as `wiki/llms-full.txt` only if agents repeatedly need more context and the small export is insufficient.

Avoid this by default because full exports get stale and can become a parallel truth.
