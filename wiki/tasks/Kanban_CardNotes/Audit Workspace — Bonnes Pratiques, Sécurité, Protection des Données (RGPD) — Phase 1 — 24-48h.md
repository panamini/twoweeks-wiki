# Audit Workspace — Bonnes Pratiques, Sécurité, Protection des Données (RGPD) — Phase 1 — 24/48h


```bash
# Auth guards Convex
rg -n "export const .* = (mutation|action|query)\\(" my-app/convex my-app/convex/actions
rg -n "getUserIdentity\\(" my-app/convex my-app/convex/actions

# Implémentation + vérification
npm --prefix my-app test || true
```
