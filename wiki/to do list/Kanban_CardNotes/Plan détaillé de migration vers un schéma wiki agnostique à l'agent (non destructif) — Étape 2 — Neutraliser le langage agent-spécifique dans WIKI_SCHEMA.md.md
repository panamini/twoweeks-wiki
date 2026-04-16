# Plan détaillé de migration vers un schéma wiki agnostique à l'agent (non destructif) — Étape 2 — Neutraliser le langage agent-spécifique dans `WIKI_SCHEMA.md`


### 2.1 Intention (important pour lecteur novice)

Objectif de cette étape:
- Ne pas supprimer la notion de LLM.
- Supprimer la dépendance à un agent nommé (ex: Claude uniquement).

Règle simple:
- Garder une formulation neutre qui inclut explicitement LLM entre parenthèses, par exemple:
  - `système opérateur (humain et/ou LLM)`

Pourquoi:
- Tu conserves le contexte réel (un LLM peut opérer le wiki).
- Tu évites le verrouillage sur un seul agent ou fournisseur.

### 2.2 Lister les occurrences à transformer

```bash
rg -n "(LLM|Claude|agent LLM|Règle de priorité LLM|Quand l'utilisateur dit|Nouvelle session|Le LLM est l'unique auteur)" WIKI_SCHEMA.md
```

Résultat attendu:
- Tu obtiens une liste de lignes à réécrire.

### 2.3 Transformations à appliquer (mapping précis FR -> FR, avec mention LLM conservée)

Appliquer les remplacements suivants dans `WIKI_SCHEMA.md`.

1. Occurrence à remplacer:
`# CLAUDE.md — Schema LLM Wiki · twoweeks (v2)`

Texte cible:
`# WIKI_SCHEMA.md — Schéma opérationnel du wiki · twoweeks (v2)`

2. Occurrence à remplacer:
`L'agent LLM le lit en premier à chaque session...`

Texte cible:
`Ce document définit le schéma opérationnel du wiki. Au démarrage d'une session, le système opérateur (humain et/ou LLM) DOIT appliquer ce document en priorité.`

3. Occurrence à remplacer:
`### Règle de priorité LLM pour les réponses`

Texte cible:
`### Règle de priorité des sources pour les réponses`

4. Occurrence à remplacer:
`Quand l'utilisateur dit "ingère les nouvelles sources"...`

Texte cible:
`Déclencheur: demande d'ingestion de nouvelles sources.`

5. Occurrence à remplacer:
`Quand l'utilisateur pose une question sur le wiki:`

Texte cible:
`Déclencheur: question sur le wiki.`

6. Occurrence à remplacer:
`Quand l'utilisateur demande un health check:`

Texte cible:
`Déclencheur: demande de health check/lint.`

7. Occurrence à remplacer:
`### Workflow : Nouvelle session`

Texte cible:
`### Workflow : Démarrage de session`

8. Occurrence à remplacer:
`Le LLM est l'unique auteur du wiki.`

Texte cible:
`Le système opérateur du wiki (humain et/ou LLM) est l'unique auteur du wiki.`

9. Occurrence à remplacer:
`Annoncer à l'utilisateur : ...`

Texte cible:
`Produire un état de session : ...`

### 2.4 Contrôle après transformation

```bash
rg -n "(Claude|Le LLM est l'unique auteur|Règle de priorité LLM pour les réponses)" WIKI_SCHEMA.md
rg -n "humain et/ou LLM|système opérateur" WIKI_SCHEMA.md
```

Résultat attendu:
- 1re commande: 0 occurrence (les anciennes formulations agent-spécifiques ont disparu).
- 2e commande: au moins une occurrence (la mention neutre incluant LLM est bien présente).

