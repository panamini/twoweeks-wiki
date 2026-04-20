# Audit Workspace — Bonnes Pratiques, Sécurité, Protection des Données (RGPD) — M2 — Gouvernance Git: règles pouvant masquer des audits


Preuves:
- `.gitignore:91` ignore `/docs/`
- `.gitignore:148-155` ignore largement `my-app/docs/*` avec exceptions ciblées.

Risque:
- nouveaux rapports/plans non suivis en git,
- traçabilité affaiblie (auditabilité projet).

Actions:

```bash
# vérifier l’état réel de suivi
git check-ignore -v docs/audits/2026-04-15-workspace-security-rgpd-audit.md || true

# ajuster .gitignore pour autoriser docs/audits
# exemple:
# /docs/*
# !/docs/audits/
# !/docs/audits/*.md
```
