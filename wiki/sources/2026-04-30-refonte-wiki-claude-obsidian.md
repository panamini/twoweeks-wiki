---
title: "Revue: refonte wiki claude-obsidian"
category: source
tags: [obsidian, wiki, retrieval, skill, tooling]
created: 2026-04-30
updated: 2026-05-04
status: current
type: decision
related: [[meta/llm-wiki-pattern]], [[meta/codex-prompting-standards]], [[wiki/hot]]
---

# Revue: refonte wiki claude-obsidian

This note evaluates the `claude-obsidian` plugin model against the twoweeks wiki contract.

## Executive verdict

- Keep twoweeks contract as-is (`CLAUDE.md` + `WIKI_SCHEMA.md`) and avoid introducing a competing truth layer.
- Do not adopt MCP/REST as a primary write path now; direct Markdown + Git remains lower-risk.
- The highest-value move is to adopt concepts, not tooling: hot cache, query modes, manifest/dedupe discipline, and richer read-only linting.
- Defer `wiki-fold`-like rollup and batch tooling until the contract is stable.

## Selected minimal move (P0)

1. Add/keep `wiki/hot.md` as short retrieval cache.
2. Add explicit quick/standard/deep retrieval modes.
3. Add lightweight hash/dedupe manifest outside the write plane when needed.
4. Add read-only duplicate/orphan/lint checks.
5. Keep `rawinput/ -> raw/` as mandatory ingest flow.

## What was rejected for now

- No Obsidian-native secondary dashboards or MCP write routes.
- No automatic multi-index fanout that would create parallel truth sources.
- No REST-driven writes or automatic commit hooks from tool triggers.

## Source

- `raw/refonte wiki claude-obsidian.md`
