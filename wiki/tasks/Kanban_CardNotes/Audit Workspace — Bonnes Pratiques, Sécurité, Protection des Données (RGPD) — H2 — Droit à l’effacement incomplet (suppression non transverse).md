# Audit Workspace — Bonnes Pratiques, Sécurité, Protection des Données (RGPD) — H2 — Droit à l’effacement incomplet (suppression non transverse)


Preuve:
- `my-app/convex/users.ts:115-120` `deleteUser` supprime uniquement des enregistrements `userProfiles`.

Risque RGPD:
- effacement partiel des données personnelles (non conformité art. 17).

Actions:

```bash
# 1) implémenter une mutation interne orchestrée deleteUserData(clerkId)
# 2) supprimer toutes les données liées (par profil + par clerkId)
# 3) journaliser l’opération (preuve d’exécution sans contenu sensible)
```

Tables à couvrir (minimum):
- `userProfiles`
- `proposals`
- `llmJobs`
- `llmHistory`
- `activeCvSnapshots`
- `proposalHandoffs`

---
