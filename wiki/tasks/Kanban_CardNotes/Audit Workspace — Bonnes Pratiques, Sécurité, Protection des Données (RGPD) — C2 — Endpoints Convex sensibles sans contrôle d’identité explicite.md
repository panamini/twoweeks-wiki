# Audit Workspace — Bonnes Pratiques, Sécurité, Protection des Données (RGPD) — C2 — Endpoints Convex sensibles sans contrôle d’identité explicite


Preuves (code actif):
- `my-app/convex/llm.ts:278` `startRefine`
- `my-app/convex/llm.ts:307` `startRefineByString`
- `my-app/convex/llm.ts:401` `enqueueRefine`
- `my-app/convex/actions/uploads.ts:5` `getUploadUrl`
- `my-app/convex/actions/structuredUpload.ts:329` `structuredUpload`
- `my-app/convex/functions.ts:215` `transformEditorSelection`
- `my-app/convex/functions.ts:256` `runCvSectionAiAction`
- `my-app/convex/alerts.ts:5` `createAlert`
- `my-app/convex/alerts.ts:26` `resolveAlert`
- `my-app/convex/alerts.ts:43` `getActiveAlerts`
- `my-app/convex/model/monitoring.ts:20` `recordMetric`
- `my-app/convex/model/monitoring.ts:41` `createAlert`
- `my-app/convex/model/monitoring.ts:63` `getActiveAlerts`

Observation associée:
- Dans ces fichiers, `getUserIdentity()` n’est pas détecté.

Risque:
- abus de ressources IA et upload,
- pollution des tables métier,
- exposition indirecte de données et surface DoS.

Actions:

```bash
# 1) inventaire endpoints publics
rg -n "export const .* = (mutation|action|query)\\(" my-app/convex my-app/convex/actions

# 2) ajout garde d’auth minimum (chaque endpoint sensible)
# pattern:
# const identity = await ctx.auth.getUserIdentity();
# if (!identity) throw new Error("Not authenticated");

# 3) contrôle post-correction
rg -n "getUserIdentity\\(" my-app/convex my-app/convex/actions
```

Complément recommandé:
- ajouter autorisation par ownership (`profileId` lié à `identity.subject`) et pas seulement authentification.
