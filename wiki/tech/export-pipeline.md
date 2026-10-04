---
title: "Export Pipeline — OCR to ATS / Styled Output"
category: tech
tags: [export, pdf, docx, ats, renderer, worker, preview, stylePreset]
created: 2026-04-14
updated: 2026-10-01
status: current
valid_from: 2026-04-14
version: v1
sources: [2026-04-14-export-pipeline-brief-ocr-to-ats-styled-output, 2026-04-15-a4-grid-canon-spec-writer, 2026-04-15-typography-mode, 2026-04-15-french-typography-scratch-pad, 2026-04-15-english-typography-scratch-pad, 2026-04-15-conversation-locale-typography-rules, 2026-04-16-live-proposal-preview-to-print-pipeline-scratchpad, 2026-04-16-live-resume-preview-to-print-pipeline-scratchpad, 2026-04-16-pdf-pipeline, 2026-04-16-token-classes-for-the-layout, 2026-04-16-proposal-style-persistence-quickmap-scratchpad, 2026-04-16-verbati-style-pipeline-scratchpad, 2026-04-21-2026-elite-design-system-implementation-handoff, 2026-04-27-workshop-pagination]
related: [[tech/import-ocr-pipeline]], [[concepts/cv-parsing-pipeline]], [[design/ats-safety]], [[design/a4-layout-systems]], [[design/locale-typography-rules]], [[design/document-token-contract]], [[tech/preview-to-print-pipeline]], [[tech/workshop-pagination]], [[entities/twoweeks]]
---

# Export Pipeline — OCR to ATS / Styled Output

Référence technique du pipeline document final, de la donnée normalisée jusqu'au fichier téléchargé.

## Architecture en un coup d'œil

```text
OCR / parsing / state document normalisé
  -> export source builders
  -> unified export client
  -> parser export endpoints
  -> Node export worker
  -> export-only renderers
  -> PDF ou DOCX
  -> direct browser download
```

## Deux mondes de rendu

### Monde preview

Utilisé pour :

- édition à l'écran
- preview CvForge / ProposalForge
- zoom
- viewport fit
- preview shell UI

### Monde export

Utilisé pour :

- Resume ATS PDF
- Resume Styled PDF
- Proposal ATS PDF
- Proposal Styled PDF
- Proposal DOCX

Ces deux mondes peuvent partager :

- contenu normalisé
- style tokens
- layout intent
- `stylePreset`

Ils ne doivent pas partager :

- preview DOM monté comme source d'export
- wrappers de zoom / viewport
- screenshot export
- logique géométrique purement preview

## Source de vérité export

Les exports sont construits depuis des objets normalisés :

- `ResumePrintSource`
- `ProposalPrintSource`

Pour le styled export preview-driven, la chaîne active passe ensuite par des payloads print-route (`ResumePreviewPrintSource`, `ProposalPreviewPrintSource`) avant la route print Playwright.

La source visuelle est gouvernée par :

- `stylePreset`
- les style/layout tokens partagés
- le contrat de géométrie Robial grid

Pour proposal, le wiki ajoute désormais une séparation plus stricte :

- `metadata.verbatiStyle` = vérité visuelle persistée
- `templateId` = structure/template/géométrie

Un export styled correct doit transporter les deux sans laisser l'un reconstruire implicitement l'autre.

Pour les templates résumé A4, le wiki distingue désormais explicitement :

- `Canon 12` comme option classique dense et pratique
- `Canon 9` comme option éditoriale plus généreuse
- `Robial 17/18` comme système modulaire moderne recommandé

La typographie locale forme une couche distincte :

- conventions FR/EN de ponctuation et citations
- dates, décimales, nombre-unité
- normalisation textuelle dépendante de la locale

Elle ne doit pas modifier implicitement la géométrie ou les flow tokens.

## Couches principales

### Frontend trigger layer

Entrées UI typiques :

- `ResumeExportControl.tsx`
- `ProposalExportActions.tsx`
- `CvForge.tsx`
- `ProposalForge.tsx`

### Unified export client

Fichier principal :

- `my-app/src/lib/exportDocumentFile.ts`

Rôle :

- reçoit l'intention d'export depuis l'UI
- envoie un payload normalisé au parser service (en production : via le relais Convex, voir ci-dessous)
- reçoit un blob fichier
- déclenche le téléchargement direct navigateur

### Export source builders

Fichier principal :

- `my-app/src/lib/document-export-models.ts`

Builders principaux :

- `buildResumeExportSource(...)`
- `buildProposalExportSource(...)`

### Backend export endpoints

Fichiers principaux :

- `cv_parser_service/main.py`
- `cv_parser_service/document_export.py`

### Worker layer

Fichier principal :

- `my-app/scripts/document-export-worker.ts`

### Renderer layer

Fichier principal :

- `my-app/src/lib/export-renderers.ts`

Renderers principaux :

- `ResumeAtsExportDocument`
- `ResumeStyledExportDocument`
- `ProposalAtsExportDocument`
- `ProposalStyledExportDocument`

## Chemin de production (depuis 2026-09-30)

```text
navigateur (twoweeks.ai, utilisateur Clerk connecté)
  -> POST https://<deployment>.convex.site/document-export/{resume|proposal}/{pdf|docx}
     (Authorization: Bearer <jeton Clerk "convex">)
  -> relais Convex `my-app/convex/documentExport.ts` (route dans `convex/http.ts`)
     - refuse sans utilisateur (401), origine hors liste (403), requête > 2 Mo (413)
     - ajoute la clé de service Cloudflare Access
  -> https://parser.twoweeks.ai/api/v1/document-export/... (tunnel Cloudflare -> Lightsail)
  -> worker Node `scripts/document-export-worker.ts`
     - PDF styled CV : Chromium headless ouvre `${DOCUMENT_EXPORT_FRONTEND_URL}/print/resume`
```

Le client (`exportDocumentFile.ts`) appelle le parser **directement** seulement si `VITE_PARSER_URL` (ou `VITE_CONVEX_PARSER_URL` / `VITE_PDF_INGEST_URL`) est défini au build : c'est le mode développement local. En production, aucune de ces variables n'est définie et le relais Convex est utilisé.

### Réglages requis (noms seulement, valeurs dans Infisical `/twoweeks` prod)

| Où | Réglage | Rôle |
| --- | --- | --- |
| Convex prod (`giddy-basilisk-88`) | `CONVEX_PARSER_URL` | origine du parser (`https://parser.twoweeks.ai`) |
| Convex prod | `CF_ACCESS_CLIENT_ID`, `CF_ACCESS_CLIENT_SECRET` | clé de service Cloudflare Access « parser » |
| Convex prod | `CLIENT_ORIGIN_WHITELIST` | doit contenir `https://twoweeks.ai` (CORS du relais) |
| Cloudflare Zero Trust, app « Twoweeks parser containment » | politique **Service Auth** « Convex service token (document export) » incluant le Service Token « parser » | laisse passer le relais ; la politique « Emergency deny unauthenticated surface » continue de bloquer le public sur `/api/v1/document-export/*`, `/warmup`, `/metrics` |
| Lightsail, `deploy/parser/compose.production.yaml` | `DOCUMENT_EXPORT_FRONTEND_URL` (défaut `https://twoweeks.ai`) | sans elle, le worker ne tente que `localhost:5173` et tout PDF styled de CV échoue |

### Diagnostic

- Le relais renvoie des erreurs 4xx lisibles (les 5xx perdent leurs en-têtes CORS côté navigateur, d'où `Failed to fetch`) : `422 export_rejected:<status>:<raison>` si le parser refuse le document, `424 export_service_failed:<status>` / `export_service_unreachable` / `export_service_unconfigured` sinon.
- Journaux Convex : ligne `[documentExport] parser refused export` avec `status`, `detail` et `stderrTail` (fin du stderr du worker).
- Diagnostic à la demande : un appel authentifié avec l'en-tête `X-Export-Debug: 1` reçoit la fin de l'erreur du worker dans la réponse.
- Tester la chaîne sans navigateur : `curl` POST vers `parser.twoweeks.ai/api/v1/document-export/proposal/pdf` avec les en-têtes `CF-Access-Client-Id/Secret` (via `infisical run`) et le payload de `scripts/smoke_document_export.py` → attendu `200 application/pdf` ; sans en-têtes → `302` (Access).

### Incident du 2026-09-30

Symptôme : « Le service d'export n'a pas répondu » sur tout export (PDF, PDF ATS, DOCX, dossier). Trois causes empilées :

1. le build Pages n'avait pas d'URL parser → le navigateur appelait `127.0.0.1:8001` ;
2. la politique Access de confinement refusait aussi la clé de service ;
3. le worker ne connaissait pas l'URL du frontend pour `/print/resume`.

Corrections : relais Convex (PR #541–#545), politique Service Auth ajoutée par l'opérateur, `DOCUMENT_EXPORT_FRONTEND_URL` sur Lightsail (PR #546, appliqué sur l'hôte avec sauvegarde `compose.production.yaml.bak-*` et redéploiement de la même image). Vérifié depuis une session réelle : CV et lettre en PDF + DOCX en 200.

## Serveur d'export Lightsail : mise à jour MANUELLE (important)

Le site (Cloudflare Pages) et Convex se déploient tout seuls à chaque fusion sur `main`. **Le serveur d'export Lightsail, non.** Le workflow `Release (production parser image)` construit et publie l'image `ghcr.io/panamini/neyssan/cv-parser:sha-<commit>` à chaque fusion, mais rien ne l'installe sur l'hôte.

Conséquence : tout changement dans `my-app/scripts/document-export-worker.ts`, `my-app/src/lib/document-export-models.ts` (payload d'impression) ou `cv_parser_service/` n'est **pas en production** tant qu'on n'a pas redéployé. Le 2026-10-01, l'hôte tournait encore sur l'image du 17 septembre (PR #481) : l'image ajoutée sur un CV n'arrivait jamais dans le PDF.

Vérifier puis déployer (après que le run `Release` du commit voulu est vert) :

```bash
ssh -i ~/.ssh/twoweeks-lightsail ubuntu@3.220.205.193 'sudo cat /opt/twoweeks/parser/deployed-image'
ssh -i ~/.ssh/twoweeks-lightsail ubuntu@3.220.205.193 \
  'sudo /opt/twoweeks/parser/deploy.sh ghcr.io/panamini/neyssan/cv-parser:sha-<commit-complet>'
```

`deploy.sh` attend la santé du conteneur ; rollback = redéployer le tag précédent. Utiliser le `deploy.sh` de l'hôte (il garde le `compose.production.yaml` de l'hôte et ses réglages, dont `DOCUMENT_EXPORT_FRONTEND_URL`). Après déploiement, refaire un export PDF réel.

Piège Convex vu le même jour : le runtime Convex (httpActions) n'a **pas** `Buffer` de Node. Un `Buffer.from(...)` y lève une erreur ; si elle est attrapée, la fonction échoue en silence. Encoder en base64 avec `btoa` (PR #577).

Disque plein (vu le 2026-10-04) : chaque déploiement garde l'ancienne image. Quand le disque (58 Go) est plein, `deploy.sh` échoue avec un trompeur `denied` sur ghcr.io (le pull anonyme échoue faute de place, puis le repli par jeton GHCR échoue). Vérifier `df -h /`, puis `sudo docker image prune -a -f && sudo docker builder prune -a -f` (les images en cours d'utilisation sont gardées), et relancer `deploy.sh`.

Automatisation possible (pas faite) : ajouter au workflow `Release` une étape SSH qui lance `deploy.sh` avec le tag du commit, protégée par un environnement GitHub avec approbation.

## Règles d'architecture

- Le fichier final doit être généré hors preview DOM.
- Le PDF doit rester text-based, searchable et selectable.
- Le téléchargement final doit être direct-download.
- L'ancien helper raster `my-app/src/lib/document-export.ts` est legacy.
- La normalisation typographique locale doit être validée contre wrap et page-break tests.
- Preview et styled PDF doivent rester des jumeaux à travers la route print, pas deux systèmes concurrents.
- Le contrat canonique des tokens document doit séparer `geometry`, `flow`, `appearance` et `runtime`.
- Les payloads proposal doivent embarquer le snapshot visuel résolu, pas seulement un `templateId`.
- Un bug de persistance saved-view peut casser l'export styled avant même l'étape worker ou Playwright.
- Pour le workshop resume path, l'export doit lire les `committedPages`; il ne doit pas replanifier les pages.
- Le navigateur n'appelle jamais le parser de production directement : toujours via le relais Convex authentifié.
- Les body classes protégées de l'export resume doivent préserver la baseline normalisée; toute réintroduction de classes style-family doit être testée contre `export-renderers.test.ts`.

## Voir aussi

- [[tech/import-ocr-pipeline]] — chemin OCR/import jusqu'à la donnée normalisée
- [[concepts/cv-parsing-pipeline]] — stratégie parser et vérité canonique
- [[design/ats-safety]] — contraintes ATS sur les outputs
- [[design/a4-layout-systems]] — géométries A4 recommandées
- [[design/locale-typography-rules]] — règles FR/EN de typographie locale
- [[design/document-token-contract]] — classes de tokens et ownership
- [[tech/preview-to-print-pipeline]] — parité preview -> print -> PDF
- [[tech/workshop-pagination]] — committed pages pour workshop resume
