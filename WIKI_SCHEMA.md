# WIKI_SCHEMA.md

This file is the neutral discovery contract for the twoweeks repository.

It keeps the repository understandable across tools without duplicating the write-time rulebook.
Use it for discovery, path conventions, and retrieval order.
Use `CLAUDE.md` as the canonical write-time contract, with `AGENTS.md` as a compatibility entrypoint when a tool boots from it.

## Repository contract

A valid twoweeks repository may contain two cooperating planes:

- **knowledge plane**
  - `wiki/index.md`
  - `wiki/log.md`
  - `wiki/overview.md`
  - `rawinput/`
  - `raw/`
- **code plane**
  - one or more source roots such as `src/`, `app/`, `lib/`, `packages/`, `services/`
  - test roots such as `tests/`, `__tests__/`, or language-native test files
  - build / dependency manifests such as `package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`
  - CI or automation files such as `.github/workflows/`

A repo may contain only the knowledge plane, only the code plane, or both.

## Read order

1. `WIKI_SCHEMA.md` if present
2. `AGENTS.md` and/or `CLAUDE.md` if present
3. root `README.md` if present
4. repository manifests and dependency files when code work is relevant
5. existing tests and CI / lint / build config when code work is relevant
6. relevant source files and entrypoints when code work is relevant
7. `wiki/overview.md`, `wiki/index.md`, and recent `wiki/log.md` entries when the knowledge plane exists
8. inspect `rawinput/` when ingest or repo-health work is relevant

## Write rule

- Read-only tools may operate with `WIKI_SCHEMA.md` alone.
- Mutating workflows must also read the write-time contract.
- If both `AGENTS.md` and `CLAUDE.md` exist, treat `CLAUDE.md` as canonical and `AGENTS.md` as compatibility routing.

## System files

- `wiki/index.md` — catalog of active and planned pages
- `wiki/log.md` — chronological mutation log
- `wiki/overview.md` — current project summary
- `wiki/timeline.md` — optional project timeline
- `rawinput/` — staging area for new sources
- `raw/` — immutable ingested source library

## Page classes

### Durable pages

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
| `output` | `wiki/outputs/` | saved answer, audit, analysis, or report |
| `task` | `wiki/tasks/` | operational backlog and execution tracking |
| `overview` | system files | control-plane and navigation pages |

## Path rules

- Durable wiki pages use their category directory and a kebab-case slug.
- Source pages use `wiki/sources/YYYY-MM-DD-<slug>.md`.
- Output pages use `wiki/outputs/YYYY-MM-DD-<slug>.md`.
- Archived pages mirror the live path under `wiki/archive/`.

## Retrieval priority

### For knowledge questions

1. Durable pages with `status: current`
2. Durable pages with `status: planned` when the question is about future state
3. Source pages for corroboration or newly ingested details not yet merged
4. Output pages only when the user asks for prior analyses or audits
5. Archived or deprecated pages only for historical questions

### For code questions

1. Relevant manifests and runtime entrypoints
2. Existing tests closest to the target behavior
3. The smallest source module that actually owns the behavior
4. CI / lint / build rules that define success
5. Wiki `tech/`, `howto/`, or `product/` pages when they clarify intent or policy

Do not duplicate workflows, templates, or agent-specific behavior here.
