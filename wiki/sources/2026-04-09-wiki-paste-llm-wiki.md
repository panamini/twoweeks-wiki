---
title: "Wiki Paste — LLM Wiki (document de référence)"
category: source
tags: [llm, wiki, knowledge-management, architecture, pattern]
created: 2026-04-09
updated: 2026-04-09
type: document
date: 2026-04-09
url: ""
related: [[llm-wiki-pattern]], [[overview]]
---

# Wiki Paste — LLM Wiki (document de référence)

**Type** : Document de référence
**Auteur** : Inconnu (partagé par l'utilisateur)
**Date** : 2026-04-09

## Résumé

Document détaillé exposant le pattern LLM Wiki : une base de connaissance persistante construite et maintenue par un LLM, contrastée avec le RAG classique. Conçu pour être copié-collé à un agent LLM pour instancier le pattern.

## Points clés

### Différence avec le RAG classique
RAG = récupère des chunks à chaque requête, re-dérive la connaissance à chaque fois. LLM Wiki = compile une fois, maintient en continu. La connaissance s'accumule au lieu d'être re-découverte.

### Architecture en 3 couches
1. **Raw sources** — immuables, source de vérité
2. **Wiki** — markdown généré par LLM, artefact persistant et composant
3. **Schema** (CLAUDE.md / AGENTS.md) — configuration des conventions et workflows

### Cas d'usage documentés
- Personnel : objectifs, santé, psychologie, journaling
- Recherche : lectures académiques sur plusieurs semaines/mois
- Lecture d'un livre : wiki des personnages, thèmes, connexions au fil des chapitres
- Business/team : wiki interne alimenté par Slack, transcripts, réunions

### Fichiers spéciaux
- **index.md** : catalogue orienté contenu, lu en premier pour toute query
- **log.md** : journal chronologique append-only, parseable avec `grep "^## \["...`

### Opérations
- **Ingest** : lire source → résumé → mise à jour pages existantes → index + log
- **Query** : lire index → lire pages pertinentes → synthèse avec citations → option de filer en output
- **Lint** : contradictions, pages orphelines, concepts sans page, données manquantes

### Outils mentionnés
- Obsidian Web Clipper — conversion articles web → markdown
- Download images localement (Obsidian Settings → Hotkeys)
- Graph view Obsidian — visualiser les connexions
- Marp — slides depuis markdown
- Dataview — requêtes sur frontmatter YAML
- qmd — moteur de recherche local pour markdown (BM25/vector + LLM re-ranking, CLI + MCP)
- Git — versioning du wiki

### Pourquoi ça marche
Les humains abandonnent les wikis parce que la maintenance (cross-références, cohérence, mises à jour) devient trop lourde. Les LLMs font ça sans se lasser, touchant 15 fichiers en une passe. Le wiki reste maintenu parce que le coût de maintenance est proche de zéro.

## Implications pour twoweeks

Ce document est la spécification de référence pour ce vault. Il a guidé la création de CLAUDE.md, la structure des dossiers, et les workflows d'ingest/query/lint.

## Pages wiki mises à jour

- [[llm-wiki-pattern]] — implémentation directe de ce document
- `CLAUDE.md` — schema construit depuis ce document
