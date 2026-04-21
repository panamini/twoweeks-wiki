# Audit Workspace — Bonnes Pratiques, Sécurité, Protection des Données (RGPD) — M1 — Configuration sensible hardcodée


Preuve:
- `my-app/convex/config/sentry.ts:5` DSN codé en dur.

Risque:
- mauvaise séparation des environnements,
- gouvernance sécurité plus difficile.

Action:

```bash
# remplacer DSN hardcodé par variable d’environnement obligatoire
# ex: process.env.SENTRY_DSN, avec échec explicite en production si absent
```

---
