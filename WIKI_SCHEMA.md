# WIKI_SCHEMA.md

This file is the agent-neutral discovery contract for the twoweeks wiki.

It exists to make the vault understandable across tools without creating a second operational rulebook.
During the current transition, `CLAUDE.md` remains the write-time source of truth.
Keep this file short and stable.

## Vault contract

A valid twoweeks wiki has:

- `wiki/index.md`
- `wiki/log.md`
- `wiki/overview.md`
- `rawinput/`
- `raw/`

Optional:

- `wiki/timeline.md`
- `wiki/tasks/`
- `WIKI_SCHEMA.md`
- `CLAUDE.md`

## Read order

1. `WIKI_SCHEMA.md` if present
2. `CLAUDE.md` if present
3. `wiki/index.md`
4. recent entries from `wiki/log.md`
5. `wiki/overview.md`

## Write rule during transition

- Read-only tools may operate with `WIKI_SCHEMA.md` alone.
- Mutating tools must also read `CLAUDE.md`.
- If both files exist, `WIKI_SCHEMA.md` provides neutral vocabulary and `CLAUDE.md` provides operational rules.

## System files

- `wiki/index.md` — catalog of active and planned pages
- `wiki/log.md` — chronological mutation log
- `wiki/overview.md` — current project summary
- `wiki/timeline.md` — optional project timeline
- `rawinput/` — staging area for new files
- `raw/` — immutable ingested source library

## Page classes

### Durable pages

Canonical knowledge pages:

| Category | Directory |
| --- | --- |
| `entity` | `wiki/entities/` |
| `concept` | `wiki/concepts/` |
| `design` | `wiki/design/` |
| `product` | `wiki/product/` |
| `strategy` | `wiki/strategy/` |
| `tech` | `wiki/tech/` |
| `howto` | `wiki/howto/` |
| `meta` | `wiki/meta/` |

### Support pages

| Category | Directory | Purpose |
| --- | --- | --- |
| `source` | `wiki/sources/` | summary of an ingested source |
| `output` | `wiki/outputs/` | saved answer, audit, analysis, or deck |

### Non-canonical operational pages

- `wiki/tasks/` if used. Exclude it from default knowledge retrieval.

## Path rules

- Durable pages use their category directory and a kebab-case slug.
- Source pages use `wiki/sources/YYYY-MM-DD-<slug>.md`.
- Output pages use `wiki/outputs/YYYY-MM-DD-<slug>.md`.
- Archived pages mirror the live path under `wiki/archive/`.

## Retrieval priority

1. Durable pages with `status: current`
2. Durable pages with `status: planned` when the query is about future state
3. Source pages for corroboration or newly ingested details not yet merged
4. Output pages only when the user asks for prior analyses or audits
5. Archived or deprecated pages only for history

Do not duplicate workflows, templates, or agent-specific behavior here.
