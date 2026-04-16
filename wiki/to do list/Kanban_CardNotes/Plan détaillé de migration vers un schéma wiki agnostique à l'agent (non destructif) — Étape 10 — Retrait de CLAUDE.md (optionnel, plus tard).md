# Plan détaillé de migration vers un schéma wiki agnostique à l'agent (non destructif) — Étape 10 — Retrait de `CLAUDE.md` (optionnel, plus tard)


À faire seulement après validation complète des usages qui dépendaient de `CLAUDE.md`.

```bash
git rm CLAUDE.md
git commit -m "chore: remove legacy CLAUDE shim after migration"
```

Résultat attendu:
- Suppression propre de l'ancien point d'entrée.

