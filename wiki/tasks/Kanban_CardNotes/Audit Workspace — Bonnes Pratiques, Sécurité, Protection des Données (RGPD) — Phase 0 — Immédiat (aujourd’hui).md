# Audit Workspace — Bonnes Pratiques, Sécurité, Protection des Données (RGPD) — Phase 0 — Immédiat (aujourd’hui)


```bash
# Secrets
git rm --cached my-app/env.md
cp my-app/.env.local.example my-app/env.md
rg -n "(OPENAI_API_KEY=|MISTRAL_API_KEY=|sk-[A-Za-z0-9_-]{20,})" my-app

# Commit remédiation
git add my-app/env.md
git commit -m "security: remove committed secrets"
```
