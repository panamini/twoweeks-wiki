# Audit Workspace — Bonnes Pratiques, Sécurité, Protection des Données (RGPD) — H1 — Stockage étendu de données CV/PII (backend + navigateur)


Preuves:
- `my-app/convex/schema.ts:405` `llmJobs.rawText`
- `my-app/convex/schema.ts:430` `llmHistory.full_response`
- `my-app/convex/schema.ts:431` `llmHistory.patch`
- `my-app/convex/jobs.ts:398` + `:429` insertion `full_response`
- `my-app/src/adapters/StorageAdapter.ts:44` + `:173-177` cache CV complet en `localStorage`

Risque RGPD:
- minimisation insuffisante,
- conservation locale de données CV sur poste utilisateur,
- difficulté de purge complète.

Actions:

```bash
# 1) supprimer la persistance du payload brut LLM (full_response)
# conserver uniquement les champs strictement nécessaires

# 2) mettre en place TTL/purge automatique (llmJobs, llmHistory, données temporaires)

# 3) retirer le fallback localStorage pour CV complet,
# ou chiffrer côté client + expiration stricte et effacement à logout
```

---
