---
title: "Tweet Karpathy — LLM Knowledge Bases"
category: source
tags: [llm, wiki, knowledge-management, workflow, obsidian]
created: 2026-04-09
updated: 2026-04-09
type: tweet
date: 2026-04-09
url: ""
related: [[llm-wiki-pattern]], [[overview]]
---

# Tweet Karpathy — LLM Knowledge Bases

**Type** : Tweet / Thread
**Auteur** : Andrej Karpathy
**Date** : 2026 (approximatif)

## Résumé

Karpathy décrit son usage des LLMs pour construire des bases de connaissance personnelles sur des sujets de recherche. Flux de tokens de plus en plus orienté vers la manipulation de connaissance (markdown + images) plutôt que du code.

## Points clés

- **Data ingest** : sources indexées dans `raw/`, LLM compile incrémentalement un wiki de fichiers `.md`
- **IDE** : Obsidian comme frontend pour visualiser raw/, wiki, et visualisations — plugins comme Marp
- **Q&A** : une fois le wiki assez grand (~100 articles, ~400K mots), on pose des questions complexes et le LLM va chercher dans le wiki plutôt que dans les raw sources
- **Pas besoin de RAG** : le LLM maintient des fichiers index et résumés courts, lit les données importantes facilement à cette échelle
- **Output** : markdown, Marp slides, matplotlib — tous viewables dans Obsidian — les outputs sont "filés" dans le wiki pour l'enrichir
- **Lint** : health checks LLM pour incohérences, données manquantes, nouvelles connexions candidates
- **Outils extra** : petit moteur de recherche sur le wiki (web UI + CLI pour le LLM)
- **Vision future** : génération de données synthétiques + finetuning pour que le LLM "connaisse" la data dans ses poids

## Citation notable

> "The LLM makes edits based on our conversation, and I browse the results in real time — following links, checking the graph view, reading the updated pages. Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase."

## Implications pour twoweeks

Ce tweet est la source fondatrice du pattern utilisé dans ce vault. Il définit l'approche globale : raw/ → wiki compilé par LLM → Q&A → lint → outputs filés dans le wiki.

## Pages wiki mises à jour

- [[llm-wiki-pattern]] — concept fondateur créé depuis cette source
- [[overview]] — pattern documenté
