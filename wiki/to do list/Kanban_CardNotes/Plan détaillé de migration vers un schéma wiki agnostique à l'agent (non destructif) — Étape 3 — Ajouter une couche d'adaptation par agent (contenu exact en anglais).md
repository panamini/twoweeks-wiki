# Plan détaillé de migration vers un schéma wiki agnostique à l'agent (non destructif) — Étape 3 — Ajouter une couche d'adaptation par agent (contenu exact en anglais)


Créer les fichiers:

```bash
mkdir -p adapters
touch adapters/claude.md adapters/codex.md
```

### 3.1 Contenu exact de `adapters/claude.md`

Copier-coller exactement ce texte:

```md
# Claude Adapter — twoweeks wiki

## Purpose

Translate the neutral schema in `WIKI_SCHEMA.md` into execution instructions for Claude.

## Context Loading

1. Read `WIKI_SCHEMA.md` first.
2. Read `wiki/index.md`.
3. Read the last 10 entries of `wiki/log.md`.
4. Read `wiki/overview.md`.
5. Check `rawinput/` for pending sources.

## Workflow Execution

- Ingest: follow the Ingest workflow from `WIKI_SCHEMA.md` exactly.
- Query: apply the temporal source-priority rules from `WIKI_SCHEMA.md`.
- Supersede: enforce `superseded_by` chain and archive moves.
- Lint: produce reports in `wiki/outputs/`.

## Document Safety Rules

- Do not manually edit files in `raw/` (except moving files from `rawinput/` during ingest).
- Keep `wiki/index.md`, `wiki/log.md`, and `wiki/timeline.md` consistent after changes.
- Never delete archived pages.
```

### 3.2 Contenu exact de `adapters/codex.md`

Copier-coller exactement ce texte:

```md
# Codex Adapter — twoweeks wiki

## Purpose

Translate the neutral schema in `WIKI_SCHEMA.md` into execution instructions for Codex.

## Context Loading

1. Read `WIKI_SCHEMA.md` first.
2. Read `wiki/index.md`.
3. Read the last 10 entries of `wiki/log.md`.
4. Read `wiki/overview.md`.
5. Check `rawinput/` for pending sources.

## Workflow Execution

- Ingest: follow the Ingest workflow from `WIKI_SCHEMA.md` exactly.
- Query: apply the temporal source-priority rules from `WIKI_SCHEMA.md`.
- Supersede: enforce `superseded_by` chain and archive moves.
- Lint: produce reports in `wiki/outputs/`.

## Document Safety Rules

- Do not manually edit files in `raw/` (except moving files from `rawinput/` during ingest).
- Keep `wiki/index.md`, `wiki/log.md`, and `wiki/timeline.md` consistent after changes.
- Never delete archived pages.
```

Vérification:

```bash
sed -n '1,220p' adapters/claude.md
sed -n '1,220p' adapters/codex.md
```

Résultat attendu:
- Les deux fichiers existent avec un contenu quasi identique (seul le nom d'agent change).

