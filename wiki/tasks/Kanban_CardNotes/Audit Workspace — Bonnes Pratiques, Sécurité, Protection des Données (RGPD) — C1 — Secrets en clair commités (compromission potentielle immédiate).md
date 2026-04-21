# Audit Workspace — Bonnes Pratiques, Sécurité, Protection des Données (RGPD) — C1 — Secrets en clair commités (compromission potentielle immédiate)


Preuves:
- `my-app/env.md:11` contient `OPENAI_API_KEY=...`
- `my-app/env.md:14` contient `MISTRAL_API_KEY=...`

Risque:
- accès non autorisé aux fournisseurs IA, coûts et abus API,
- risque de fuite de données si les clés ont été utilisées en production,
- non-conformité sécurité (RGPD art. 32: confidentialité/intégrité).

Actions immédiates (ordre strict):

```bash
# 1) retirer le fichier de l’index git (sans le supprimer localement)
git rm --cached my-app/env.md

# 2) remplacer par un template non secret
cp my-app/.env.local.example my-app/env.md

# 3) vérifier l’absence de clés en clair
rg -n "(OPENAI_API_KEY=|MISTRAL_API_KEY=|sk-[A-Za-z0-9_-]{20,})" my-app

# 4) commit de remédiation
git add my-app/env.md
git commit -m "security: remove committed secrets and replace with template"
```

Rotation obligatoire hors dépôt:
- OpenAI key,
- Mistral key,
- toute clé dérivée associée au même projet.

Si fuite historique publique/synchronisée:

```bash
# réécriture d’historique (coordination équipe obligatoire)
git filter-repo --path my-app/env.md --invert-paths
```

---
