# twoweeks-wiki

Knowledge base for the [twoweeks](https://twoweeks.ai) project — maintained by LLM + human collaboration.

## For LLMs and AI agents

**Start here, in this order:**

1. Read `CLAUDE.md` — the wiki schema, conventions, and workflows (what each folder means, how to ingest sources, how to query, how to handle temporal status)
2. Read `wiki/index.md` — the full catalogue of active pages (entities, concepts, sources, tech, howto, kanban)
3. Read only the pages relevant to your task

Do not read the entire wiki blindly. The index is designed to let you find the right 2–3 pages without loading everything.

## Structure

```
twoweeks-wiki/
├── CLAUDE.md          ← schema, workflows, conventions — READ FIRST
├── rawinput/          ← staging: new sources to ingest
├── raw/               ← immutable source library
└── wiki/
    ├── index.md       ← full page catalogue — READ SECOND
    ├── log.md         ← append-only operation log
    ├── timeline.md    ← project event timeline
    ├── entities/      ← products, orgs, people
    ├── concepts/      ← patterns, decisions, technical concepts
    ├── sources/       ← ingested source summaries
    ├── tech/          ← call paths, architecture, infra reference
    ├── howto/         ← operational runbooks
    ├── to do list/    ← sprint kanban
    ├── outputs/       ← analyses, Q&A outputs
    └── archive/       ← superseded pages (never deleted)
```

## For humans

Drop new sources in `rawinput/` and run `/ingest-wiki` in Cowork to process them into the wiki.
