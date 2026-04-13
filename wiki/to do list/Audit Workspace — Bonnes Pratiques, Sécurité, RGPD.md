

  

Date: 2026-04-03

Périmètre audit: Workspace/Neyssan`

Référentiel projet: `v1` prioritaire (conformément à AGENTS)

  

## 1) Méthodologie

  

- Revue statique ciblée sur le code actif `my-app/` (frontend + Convex backend) puis revue transversale du workspace.

- Recherche de secrets, endpoints publics, contrôles d'auth, stockage de données personnelles, rétention et suppression.

- Vérification de la présence de code legacy/obsolète pouvant impacter la sécurité opérationnelle.

  

Commandes de collecte principales utilisées:

  

```bash

rg --files

rg -n "(OPENAI_API_KEY|MISTRAL_API_KEY|SECRET|TOKEN|CLERK|SENTRY|CONVEX)" my-app

rg -n "(localStorage|sessionStorage|console\\.log|console\\.error|persist|storage)" my-app/src my-app/convex --glob '!**/*.test.*'

rg -n "(email|phone|linkedin|raw_text|profile|privacy|GDPR|RGPD|retention|delete)" my-app/convex my-app/src --glob '!**/*.test.*'

```

  

## 2) Classification des zones (avec niveau de certitude)

  

### Active code (forte confiance)

  

- `my-app/src/`

- `my-app/convex/`

- `my-app/.env.local.example`

- `my-app/docs/*` (documentation active récente)

  

### Legacy mais informatif (confiance moyenne)

  

- `cv_parser_service/` (service parser séparé, encore cohérent avec certains flux)

- scripts opérationnels racine (`scripts/`, `run*.sh`) selon usage local

  

### Obsolète / dead code (probable)

  

- `pdf-ingest/` (explicitement non autoritaire selon AGENTS)

- code spaCy/training historique: `cv_parser/`, `training/`, fichiers `*.bak`

- routers Convex non raccordés à `my-app/convex/http.ts`:

- `my-app/convex/clerk_webhook.ts`

- `my-app/convex/actions/persistProfile.ts`

  

Incertitude à lever: confirmer que `pdf-ingest/` n'est plus déployé/accessible publiquement.

  

## 3) Constat principal (sécurité + RGPD)

  

## Critique

  

### C1 — Secrets/API keys exposés en clair dans le repo

  

Preuves:

- `my-app/env.md:11` (`OPENAI_API_KEY=...`)

- `my-app/env.md:14` (`MISTRAL_API_KEY=...`)

- `my-app/mistral_integration_backend.md:20` (exemple de clé explicite)

  

Risque:

- Compromission immédiate des comptes fournisseurs (coûts, fuite de données, abus API).

- Non-conformité sécurité (RGPD art. 32: mesures techniques appropriées).

  

Actions immédiates:

  

```bash

# 1) Stopper l'exposition future

git rm --cached my-app/env.md

  

# 2) Remplacer le fichier par un template sans secret

cp my-app/.env.local.example my-app/env.md

  

# 3) Commit de remédiation

git add my-app/env.md

git commit -m "security: remove plaintext secrets from repo"

```

  

Rotation obligatoire (hors git, dashboards fournisseurs):

- OpenAI API key

- Mistral API key

- Toute clé potentiellement dérivée/associée

  

Purge historique (si repo partagé):

  

```bash

# ATTENTION: réécriture d'historique

git filter-repo --path my-app/env.md --invert-paths

# puis forcer push coordonné

```

  

---

  

### C2 — Mutations/actions publiques sans contrôle d'identité explicite (surface d'abus)

  

Preuves (code actif):

- `my-app/convex/llm.ts:307` `startRefineByString` (pas de `getUserIdentity`, création possible de profile placeholder)

- `my-app/convex/workerGateway.ts:13` `processJobRequest` (opérations sensibles jobs/history)

- `my-app/convex/actions/uploads.ts:5` `getUploadUrl` (génération URL upload)

- `my-app/convex/functions.ts:215` `transformEditorSelection`, `runCvSectionAiAction` (usage IA sans garde auth explicite)

- `my-app/convex/alerts.ts:5`, `my-app/convex/model/monitoring.ts:41` (création/lecture alertes publiques)

  

Risque:

- Abus de ressources LLM, flood de données, coûts non contrôlés.

- Exposition indirecte de données et surfaces DoS applicatives.

  

Actions immédiates (pattern minimal):

  

```bash

# appliquer dans chaque mutation/action publique sensible

const identity = await ctx.auth.getUserIdentity();

if (!identity) throw new Error("Not authenticated");

```

  

Checklist rapide:

  

```bash

rg -n "export const .* = (mutation|action)\\(" my-app/convex my-app/convex/actions

rg -n "getUserIdentity\\(" my-app/convex my-app/convex/actions

```

  

---

  

### C3 — Données CV/PII stockées en clair et durablement (backend + navigateur)

  

Preuves:

- Backend: `my-app/convex/schema.ts` (`userProfiles.raw_text`, `llmJobs.rawText`, `llmHistory.full_response`, `llmHistory.patch`)

- Persist history: `my-app/convex/jobs.ts:425` (insert `full_response`)

- Frontend cache local: `my-app/src/adapters/StorageAdapter.ts:42`, `:156` (localStorage)

- Clés localStorage dédiées CV: `my-app/src/lib/cv-local-storage.ts:1`

  

Risque:

- Données personnelles CV conservées sans politique de minimisation/rétention stricte.

- Exposition locale en cas de poste partagé/compromis navigateur.

  

Actions immédiates:

  

```bash

# 1) Minimiser llmHistory: ne pas stocker full_response brut

# conserver seulement champs nécessaires (patch normalisé + métriques)

  

# 2) Ajouter TTL applicatif (cron/scheduler) pour:

# llmHistory, llmJobs, raw_text non nécessaire

  

# 3) Supprimer fallback localStorage pour CV complets

# ou chiffrer côté client + expiration stricte

```

  

## Élevé

  

### H1 — Droit à l'effacement incomplet (suppression non cascade)

  

Preuves:

- `my-app/convex/users.ts:115` `deleteUser` supprime seulement `userProfiles`

- Pas de cascade explicite vers `proposals`, `llmJobs`, `llmHistory`, `activeCvSnapshots`, `proposalHandoffs`

  

Risque:

- Non-conformité RGPD (droit à l'effacement incomplet).

  

Action:

  

```bash

# créer mutation interne orchestrée deleteUserData(clerkId)

# suppression transactionnelle logique sur toutes tables liées

```

  

Tables à purger:

- `userProfiles`

- `proposals` (via `userId`)

- `llmJobs` (via `profileId`)

- `llmHistory` (via `profileId`)

- `activeCvSnapshots` (via `clerkId`)

- `proposalHandoffs` (via `clerkId`)

  

---

  

### H2 — Journalisation potentielle de contenu sensible

  

Preuves:

- `my-app/convex/lib/parsing/hybridParser.ts:29` log de preview prompt

- multiples `console.log/console.warn` en parcours parsing/LLM

- `my-app/convex/auth.config.ts:1` log variables auth

  

Risque:

- PII en logs (opérations, observabilité, crash reports).

  

Action:

  

```bash

# remplacer logs verbeux par logger structuré redacted

# interdire logs de prompt/raw CV/email/phone

rg -n "console\\.(log|warn|error)\\(" my-app/convex my-app/src --glob '!**/*.test.*'

```

  

## Moyen

  

### M1 — Paramètres sensibles hardcodés / fallback dev en prod

  

Preuves:

- `my-app/convex/config/sentry.ts:5` DSN hardcodé

- `my-app/convex/auth.config.ts:5` fallback domain Clerk de test

  

Risque:

- Erreurs de config, fuite d'environnement, traçabilité involontaire.

  

Action:

  

```bash

# imposer env obligatoires en production

# refuser boot si SENTRY_DSN / CLERK_JWT_ISSUER_DOMAIN manquants en prod

```

  

---

  

### M2 — Politique de rétention déclarée mais non appliquée

  

Preuves:

- `my-app/convex/config/monitoring.ts` définit retention

- aucun usage effectif trouvé des constantes de rétention

  

Risque:

- Conservation non maîtrisée des données techniques.

  

Action:

  

```bash

# implémenter job scheduler de purge par age

# sur metrics/alerts + données parsing temporaires

```

  

## 4) Plan d'actions priorisé (exécutable)

  

### Phase 0 (Aujourd'hui)

  

```bash

# A. Bloquer la fuite de secrets

git rm --cached my-app/env.md

printf "# Environment variables are managed out-of-repo\n" > my-app/env.md

git add my-app/env.md

git commit -m "security: remove committed secrets"

  

# B. Scanner immédiatement le repo

rg -n "(OPENAI_API_KEY=|MISTRAL_API_KEY=|sk-[A-Za-z0-9_-]{20,})" .

```

  

### Phase 1 (24-48h)

  

```bash

# C. Lister actions/mutations publiques

rg -n "export const .* = (mutation|action)\\(" my-app/convex my-app/convex/actions

  

# D. Ajouter auth guards sur endpoints sensibles

# (édition manuelle + tests)

  

# E. Vérifier tests principaux

npm --prefix my-app test

```

  

### Phase 2 (Semaine)

  

```bash

# F. Implémenter suppression RGPD transverse

# internal.deleteUserData(clerkId) + endpoint admin sécurisé

  

# G. Implémenter purge automatique

# llmHistory / llmJobs / metrics / alerts

```

  

### Phase 3 (Industrialisation)

  

```bash

# H. Ajouter scans sécurité CI (exemple)

# - secret scan

# - dependency audit

npm --prefix my-app audit --omit=dev

```

  

## 5) Écarts RGPD (synthèse)

  

- Minimisation: partiellement respectée, mais stockage brut de payloads LLM/CV trop large.

- Limitation de conservation: insuffisante (pas de purge effective constatée).

- Intégrité/confidentialité: insuffisante sur la gestion des secrets et logs.

- Droits des personnes: suppression incomplète (pas de cascade globale).

- Accountability: pas de documentation RGPD opérationnelle trouvée dans le périmètre actif.

  

## 6) Recommandations de gouvernance minimale

  

- Créer `docs/decisions/` pour formaliser:

- politique de rétention par table

- politique de logs (redaction obligatoire)

- procédure DSR (accès/suppression/export)

- Créer un runbook incident secrets (rotation, invalidation, postmortem).

  

## 7) Limites de l'audit

  

- Audit statique uniquement (pas de tests dynamiques de pénétration).

- Pas de vérification infra cloud (WAF, réseau, policies Convex dashboard, permissions externes).

- Certaines zones legacy (`pdf-ingest/`, `cv_parser/`) sont classées non autoritaires selon AGENTS mais restent des risques si déployées hors contrôle.