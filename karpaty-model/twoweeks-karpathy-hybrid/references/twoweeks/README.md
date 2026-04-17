# twoweeks-wiki

Knowledge base for the [twoweeks](https://twoweeks.ai) project — maintained by LLM + human collaboration.

## For LLMs and AI agents

**Start here, in this order:**

1. Read `WIKI_SCHEMA.md` if present — neutral discovery contract
2. Read `CLAUDE.md` — operational write contract for the current workflow
3. Read `wiki/overview.md` — current project summary
4. Read `wiki/index.md` — the active page catalogue
5. Read recent entries from `wiki/log.md`
6. Check `rawinput/` when ingest or repo-health work is relevant

Bootstrap is not `CLAUDE.md`-only.
During the current transition, `WIKI_SCHEMA.md` is the neutral schema entrypoint and `CLAUDE.md` remains the operational contract for mutations.

Do not read the entire wiki blindly. The index is designed to let you find the right pages without loading everything.

## Structure

```text
twoweeks-wiki/
├── WIKI_SCHEMA.md      ← neutral schema entrypoint
├── CLAUDE.md           ← operational contract for writes
├── rawinput/           ← staging: new sources to ingest
├── raw/                ← immutable source library
└── wiki/
    ├── overview.md     ← current project summary
    ├── index.md        ← active/planned page catalogue
    ├── log.md          ← append-only operation log
    ├── timeline.md     ← project event timeline
    ├── entities/       ← products, orgs, people
    ├── concepts/       ← patterns, policies, technical concepts
    ├── design/         ← visual systems and layout rules
    ├── product/        ← roadmap, KPIs, user-facing capabilities
    ├── strategy/       ← market, positioning, prioritization
    ├── tech/           ← call paths, architecture, infra reference
    ├── howto/          ← operational runbooks
    ├── meta/           ← schema and wiki-maintenance docs
    ├── sources/        ← ingested source summaries
    ├── outputs/        ← saved analyses and reports
    ├── tasks/          ← operational backlog, excluded from default retrieval
    └── archive/        ← superseded pages (never deleted)
```

## For humans

Drop new sources in `rawinput/` and run `/ingest-wiki` in Cowork to process them into the wiki.
