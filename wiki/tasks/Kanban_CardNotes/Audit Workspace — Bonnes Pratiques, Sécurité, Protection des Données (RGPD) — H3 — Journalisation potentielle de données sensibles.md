# Audit Workspace — Bonnes Pratiques, Sécurité, Protection des Données (RGPD) — H3 — Journalisation potentielle de données sensibles


Preuves:
- `my-app/convex/lib/parsing/hybridParser.ts:33` log de preview prompt
- `my-app/convex/lib/parsing/hybridParser.ts:78` log présence clé API
- `my-app/convex/lib/parsing/hybridParser.ts:158` log shape sortante
- `my-app/convex/auth.config.ts:1` log de variable d’environnement auth

Risque:
- fuite de données personnelles/techniques via logs applicatifs et observabilité.

Actions:

```bash
# 1) bannir les logs de prompt/raw CV/identifiants
rg -n "console\\.(log|warn|error)\\(" my-app/convex my-app/src --glob '!**/*.test.*'

# 2) implémenter un logger structuré avec redaction systématique
# 3) limiter les logs debug aux environnements dev contrôlés
```
