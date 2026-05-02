---
aliases:
  - |-
    refonte wiki 

    claude-obsidian
---
## Executive Verdict

- **Oui, ça vaut le coup, mais seulement en extraction ciblée.** `claude-obsidian` contient de bons patterns de retrieval, cache, lint et batch orchestration, mais son modèle complet est trop large et trop Obsidian-centric pour `twoweeks-wiki`.
- **Non, ne branchez pas MCP/REST maintenant.** Votre repo est déjà local, lisible en Markdown, versionné, et gouverné par `CLAUDE.md`. MCP/REST ajouterait surtout des dépendances, secrets et surfaces de write hors contrat.
- **Minimal move à meilleur ROI:** adapter `hot.md` + modes de query + manifest/hash de sources. C’est ce qui réduit le plus les tokens et le temps de recherche sans toucher au write path canonique.

Sources principales inspectées: [README](https://github.com/AgriciDaniel/claude-obsidian), [WIKI.md](https://github.com/AgriciDaniel/claude-obsidian/blob/main/WIKI.md), [skills](https://github.com/AgriciDaniel/claude-obsidian/tree/main/skills), [agents](https://github.com/AgriciDaniel/claude-obsidian/tree/main/agents), [hooks](https://github.com/AgriciDaniel/claude-obsidian/tree/main/hooks), [Local REST API](https://github.com/coddingtonbear/obsidian-local-rest-api).

## Table 1 — Skills Audit

| Skill | Ce que ça fait | Gain pour nous | Conflit potentiel | Dépendance | Verdict |
|---|---|---:|---|---|---|
| `wiki` | Orchestrateur setup/scaffold, routing, `hot.md` | Moyen | Crée un second contrat et structure concurrente | Claude plugin, Obsidian | **Adapter** uniquement le routing/cache |
| `wiki-ingest` | Ingest source, pages, index, log, hot, manifest | Fort | `.raw/`, fanout 8-15 pages, sub-indexes | WebFetch, shell, manifest | **Adapter** hash/dedupe/context discipline |
| `wiki-query` | Quick/standard/deep retrieval | Très fort | `wiki/questions/` comme canon bis | Aucun fort | **Copier/adapté** |
| `wiki-lint` | Orphans, dead links, stale claims, frontmatter, semantic tiling | Fort | Peut créer rapports/dashboards non canoniques | Python/Ollama optionnel | **Adapter** en lint read-only |
| `save` | Sauve une conversation en note | Moyen | `questions/`, `meta/decision` doublonnent `outputs/` et pages durables | Aucun | **Adapter léger** vers `wiki/outputs/` |
| `autoresearch` | Recherche web multi-round puis écrit le wiki | Moyen/faible maintenant | Peut bypasser `rawinput/ -> raw/` et créer trop de pages | WebSearch/WebFetch | **Ignorer maintenant** |
| `canvas` | Écrit des `.canvas` visuels | Faible pour ingest | Surface Obsidian non canonique | Obsidian Canvas | **Ignorer** |
| `defuddle` | Nettoie pages web avant ingest | Fort si URL ingest | Écrit dans `.raw/` chez eux | `defuddle-cli` | **Adapter** vers `rawinput/` |
| `obsidian-bases` | Dashboards `.base` | Faible moteur, moyen UX Obsidian | Dashboard devient vérité implicite | Obsidian 1.9+ | **Ignorer/P2** |
| `obsidian-markdown` | Référence syntaxe wikilinks/callouts/frontmatter | Moyen | Le schema frontmatter diffère | Obsidian | **Adapter** partiellement |
| `wiki-fold` | Rollup extractif de `wiki/log.md` | Moyen/fort quand log grossit | `wiki/folds/`, auto-commit assumptions | Aucun fort | **Adapter P1** en rollup read-only/durable contrôlé |

## Table 2 — Feature Comparison

| Capacité | ingest-wiki actuel | claude-obsidian | Meilleur choix | Pourquoi |
|---|---|---|---|---|
| Contrat canonique | `CLAUDE.md` | `WIKI.md` + skills | `ingest-wiki` | Ne pas créer une deuxième vérité |
| Source staging | `rawinput/ -> raw/` | `.raw/` direct | `ingest-wiki` | Votre flux sépare staging et bibliothèque immuable |
| Index | `wiki/index.md` central | master + `_index.md` locaux | `ingest-wiki` | Un index canonique réduit les divergences |
| Log | `wiki/log.md` obligatoire | idem + folds | Hybride | Garder log; ajouter rollup plus tard |
| Hot cache | Absent | `wiki/hot.md` | `claude-obsidian` adapté | ROI immédiat tokens/reprise contexte |
| Query modes | Implicite | quick/standard/deep | `claude-obsidian` adapté | Meilleur contrôle du budget de lecture |
| Hash manifest | Dedupe heuristique | `.raw/.manifest.json` | Adapté | Utile, mais hors `raw/` ou manifest explicitement mutable |
| Multi-agent ingest | Non central | sub-agents batch | Adapté prudemment | Parallel read oui; single writer pour index/log |
| Lint | Décrit dans skill locale | plus détaillé + tiling | Adapté | Read-only d’abord, pas dashboards auto |
| MCP/REST | Pas nécessaire | optionnel | Ne pas activer | FS direct suffit et reste plus sûr |
| Bases/Dataview | Non requis | dashboards | Ignorer | UX Obsidian, pas moteur agent |
| Hooks auto-commit | Non | PostToolUse commit | Rejeter | Risque majeur sur index/log et commits parasites |

## MCP / REST Obsidian

MCP/REST Obsidian signifie: Obsidian tourne localement avec le plugin **Local REST API**, qui expose le vault via HTTPS local avec API key. Un serveur MCP peut ensuite donner à un LLM des outils comme lire une note, chercher dans le vault, patcher un heading/frontmatter, append, supprimer, lister des fichiers, lancer des requêtes Dataview, voire utiliser la note active.

La différence avec lire les fichiers Markdown directement:

- **Fichiers directs:** simple, déterministe, compatible Codex/Claude Code/agents CLI, visible dans Git, facile à contrôler par `CLAUDE.md`.
- **Obsidian REST/MCP:** utile pour interroger l’état Obsidian: active note, recherche Obsidian, Dataview, Bases, backlinks/metadata rendus, commandes Obsidian.

Pour `twoweeks-wiki`, c’est **overkill maintenant**. La valeur de Dataview/Bases/canvas est surtout navigation humaine dans Obsidian, pas amélioration du write path agent. Les risques sont concrets: API key locale, port REST, TLS self-signed, permissions larges CRUD, dépendance à Obsidian ouvert, et chemins d’écriture hors `ingest-wiki`.

## Minimal Move Proposal

**P0: maintenant, sans MCP**

1. Ajouter un `wiki/hot.md` comme cache court, non canonique, overwrite-only.
2. Ajouter dans la skill actuelle des modes de lecture: `quick`, `standard`, `deep`.
3. Ajouter un manifest de hash/dedupe, mais **pas comme source raw mutable**: plutôt `wiki/meta/ingest-manifest.json` ou un fichier système explicitement autorisé.
4. Adapter `defuddle` seulement pour URL ingest: nettoyage vers `rawinput/`, puis flux normal `rawinput/ -> raw/`.
5. Renforcer lint read-only: pages manquantes de l’index, doublons actifs, sources dupliquées, links cassés.

**P1: ensuite si P0 marche**

1. Ajouter un rollup extractif de `wiki/log.md` inspiré `wiki-fold`, sans auto-commit et sans modifier les entrées enfants.
2. Ajouter un batch ingest safe: sub-agents ou passes parallèles uniquement pour lecture/extraction; orchestrator unique pour durable pages, `wiki/index.md`, `wiki/log.md`, move vers `raw/`.
3. Ajouter semantic tiling read-only pour candidats doublons, local-only, sans auto-merge.

**P2: seulement si Obsidian/MCP devient nécessaire**

1. Brancher MCP/REST en lecture seule d’abord.
2. Tester uniquement `search`, Dataview/Bases, active note, backlinks.
3. Interdire les writes MCP tant que `CLAUDE.md` ne définit pas une policy explicite.
4. Garder `wiki/index.md` et `wiki/log.md` comme vérité canonique; Bases/Dataview restent des vues dérivées.

Recommandation nette: **ne migrez pas vers `claude-obsidian`; prélevez `hot.md`, query modes, manifest/hash, lint taxonomy, et éventuellement log folds.** Tout le reste augmente plus la complexité du write path qu’il ne réduit les tokens.