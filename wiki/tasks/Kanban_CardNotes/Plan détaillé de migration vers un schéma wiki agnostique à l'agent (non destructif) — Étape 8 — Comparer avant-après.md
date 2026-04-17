# Plan détaillé de migration vers un schéma wiki agnostique à l'agent (non destructif) — Étape 8 — Comparer avant/après


```bash
git diff -- CLAUDE.md WIKI_SCHEMA.md adapters/ skills/twoweeks-wiki-operator/
```

Résultat attendu:
- Diff lisible: séparation nette entre spec neutre et adaptateurs agent.

