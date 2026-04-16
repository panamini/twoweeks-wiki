# Plan détaillé de migration vers un schéma wiki agnostique à l'agent (non destructif) — Étape 6 — Vérifier les références internes restantes


```bash
rg -n "CLAUDE.md" .
```

Résultat attendu:
- Liste finie de références.
- Tu corriges chaque référence qui devrait viser `WIKI_SCHEMA.md`.

