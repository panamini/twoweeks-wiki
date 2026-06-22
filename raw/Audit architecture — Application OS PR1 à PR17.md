

Date: 2026-06-11
Branche auditée: `application-os-foundation`
Document demandé: `docs/audits/2026-06-11-application-os-pr1-pr17-architecture-audit.md`

## Statut de l'audit

Certain:
- L'audit a été fait à partir du dépôt GitHub `panamini/neyssan`, branche `application-os-foundation`.
- Le dépôt n'était pas présent en checkout Git local dans l'environnement d'audit. Les commandes locales `rtk git status`, `rtk git log` et `rtk git diff` n'ont donc pas pu être exécutées directement.
- La comparaison disponible a été adaptée en comparant `main...application-os-foundation` via GitHub.
- Le document d'audit a été créé dans l'environnement de travail disponible, sous `/mnt/data/docs/audits/...`.

Probable:
- `application-os-foundation` correspond à la branche intégrée après les PR Application OS PR1 à PR17.
- La base attendue par la demande, `origin/application-os-foundation...HEAD`, correspondrait à une branche de travail locale au-dessus de `application-os-foundation`. Comme l'audit porte directement sur `application-os-foundation`, la comparaison adaptée la plus utile est `main...application-os-foundation`.

À vérifier:
- Exécuter les commandes `rtk git ...` dans un vrai checkout local du dépôt avant merge ou avant de donner ce document comme preuve finale de CI.
- Vérifier les checks CI réels de la branche, car aucun test local n'a été lancé depuis cet environnement.

# Sources inspectées

## Sources de vérité principales

- `docs/decisions/2026-06-08-application-os-master-plan.md`
- `AGENTS.md`
- `docs/plans/2026-06-11-mcp-readiness.md`

## Docs Application OS inspectées

- `docs/decisions/2026-06-08-application-harness-kernel.md`
- `docs/decisions/2026-06-08-application-os-master-plan.md`
- `docs/decisions/2026-06-09-candidate-evidence-kernel.md`
- `docs/decisions/2026-06-09-candidate-evidence-persistence.md`
- `docs/decisions/2026-06-09-career-knowledge-rules.md`
- `docs/decisions/2026-06-09-evidence-graph-shadow.md`
- `docs/decisions/2026-06-09-minimal-review-cockpit.md`
- `docs/decisions/2026-06-09-resume-variant-artifact.md`
- `docs/decisions/2026-06-09-resume-variant-plan-artifact.md`
- `docs/decisions/2026-06-10-application-package-v1.md`
- `docs/decisions/2026-06-10-application-package-shadow-persistence.md`
- `docs/decisions/2026-06-10-cover-letter-artifact-adapter.md`
- `docs/decisions/2026-06-10-internal-tool-contracts.md`
- `docs/decisions/2026-06-10-controlled-ats-scout-adapters.md`
- `docs/decisions/2026-06-11-controlled-ats-public-endpoint-resolver.md`
- `docs/decisions/2026-06-11-local-mcp-beta.md`
- `docs/plans/2026-06-11-mcp-readiness.md`

## Modules source inspectés

- `my-app/src/modules/application-harness/`
- `my-app/src/modules/candidate-evidence/`
- `my-app/src/modules/career-knowledge/`
- `my-app/src/modules/evidence-graph/`
- `my-app/src/modules/resume-variant-plan/`
- `my-app/src/modules/resume-variant-artifact/`
- `my-app/src/modules/review-cockpit/`
- `my-app/src/modules/cover-letter-artifact/`
- `my-app/src/modules/application-package/`
- `my-app/src/modules/internal-tool-contracts/`
- `my-app/src/modules/controlled-ats-scout/`
- `my-app/src/modules/local-mcp/`

## Surfaces sensibles vérifiées

Certain:
- `my-app/convex/schema.ts` contient des tables shadow Application OS: `applicationContexts`, `applicationRuns`, `applicationArtifacts`, `candidateSourceDocuments`, `candidateFacts`, `candidateImportBatches`, `applicationPackages`.
- `my-app/convex/applicationHarness.ts`, `my-app/convex/candidateEvidence.ts` et `my-app/convex/applicationPackages.ts` exposent des mutations/queries internes pour la persistence shadow.
- La comparaison de branche inspectée n'a pas montré de changement dans `my-app/src/app/`, `my-app/src/pages/`, `my-app/src/components/`, `my-app/package.json` ni les lockfiles.

À vérifier:
- Confirmer ce résultat avec `rtk git diff --name-only origin/application-os-foundation...HEAD` dans le checkout local réel.

# État de branche

## Commandes demandées

Demandé:

```bash
rtk git status --short --branch
rtk git log --oneline -n 25
rtk git diff --name-only origin/application-os-foundation...HEAD
```

Résultat dans cet environnement:

Certain:
- Non exécuté localement: pas de checkout Git du dépôt dans `/mnt/data`.
- Inspection adaptée via GitHub: `main...application-os-foundation`.
- La branche `application-os-foundation` est ahead de `main` avec 88 commits dans la comparaison GitHub consultée.

À vérifier localement:

```bash
rtk git status --short --branch
rtk git log --oneline -n 25
rtk git diff --name-only origin/application-os-foundation...HEAD
```

Si l'audit est exécuté directement sur `application-os-foundation`, utiliser plutôt:

```bash
rtk git diff --name-only main...HEAD
```

# Résumé exécutif

Certain:
- PR1 à PR17 livrent une fondation Application OS largement additive.
- Les modules principaux sont des kernels TypeScript purs, avec quelques persistences Convex shadow internes.
- Les couches Product Value sont présentes: plan de variant CV, cockpit de revue, artifact de variant, artifact de cover letter, package d'application.
- La couche Distribution est présente mais contrôlée: contracts internes, Controlled ATS, Local MCP dry-run, spec MCP readiness.
- Aucun Remote MCP, ChatGPT App, OAuth, transport HTTP MCP, UI route, export, send, submit, apply ou auto-apply n'est livré dans les modules inspectés.

Probable:
- L'architecture respecte l'intention du plan original: construire le spine et la proof layer avant la distribution.
- Les garde-fous principaux sont en place pour éviter source truth loss, mutation de faits, exposition de `private` / `never_use`, et scraping de plateformes interdites.

À vérifier:
- Couverture CI réelle après PR17.
- Comportement Convex complet sur données réelles.
- Toute future intégration UI/export/MCP remote, car l'architecture actuelle est volontairement pré-produit pour ces actions.

Conclusion:
- P0 confirmé: aucun.
- P1 confirmé: aucun.
- Risques P2/P3 ouverts: documentation divergente, numérotation PR confuse, tests à renforcer sur edge cases, gates d'approbation/export à formaliser avant toute action produit.

# Roadmap réelle reconstituée

| PR logique | PR GitHub / titre observé | Livré réellement | Statut | Certitude |
|---|---|---|---|---|
| PR0.5 | PR102 — Document Application OS master plan | Plan maître Application OS | docs-only | Certain |
| PR1 | PR101 — Pure TypeScript application harness kernel | Kernel `application-harness` pur: schémas, hash, idempotency | actif, pure TS | Certain |
| PR1.1 | PR103 — Harden application harness persistence preflight | Ancrage candidat, helper raw job hash, durcissement hash | actif, fix-forward | Certain |
| PR2 | PR104 — Add application harness Convex shadow persistence | Tables/fonctions Convex shadow `applicationContexts`, `applicationRuns`, `applicationArtifacts` | shadow-only actif | Certain |
| PR3 | PR105 — shadow ApplicationContext builder persistence guards | Builder Convex ApplicationContext | shadow-only actif | Certain |
| PR3.1 | PR106 — Fix shadow context builder review issues | Typage projection, contact/identity hash, `cvSnapshotHash` requis | fix-forward | Certain |
| PR4 | PR111 — Candidate source/fact kernel | Kernel candidate source/fact | actif, pure TS | Certain |
| PR5 | PR112 — CareerKnowledge static rules and resolver | Règles statiques et resolver CareerKnowledge | actif, pure TS | Certain |
| PR6 | PR113 — Candidate evidence Convex shadow persistence | Persistence shadow source docs/facts/import batches | shadow-only actif | Certain |
| PR6.1 | PR114 — require canonical source document IDs | Durcissement IDs canonicals candidate evidence | fix-forward | Certain |
| PR7 | PR115 — EvidenceGraph shadow | EvidenceGraph déterministe + risk rules | actif, pure TS | Certain |
| PR8 | PR116 — ResumeVariantPlan artifact | Plan de variant CV depuis EvidenceGraph | actif, pure TS | Certain |
| PR9 | PR117 — Minimal review cockpit | Modèle ReviewCockpit, sans UI | actif, model-only | Certain |
| PR10 | PR118 — Resume Variant Artifact | Artifact metadata de variant CV, provenance-backed | actif, pure TS | Certain |
| PR11 | PR119 — Cover-letter artifact adapter | Artifact cover letter depuis texte fourni, provenance héritée | actif, pure TS | Certain |
| PR12 | PR120 — ApplicationPackageV1 | Package d'application qui référence artifacts + provenance | actif, pure TS | Certain |
| PR13 | PR121 — Internal tool contracts | Catalogue de contracts internes read-only/pure-compute | actif, pure TS | Certain |
| PR14 bis | PR122 — ApplicationPackageV1 Convex shadow persistence | Persistence shadow `applicationPackages` | shadow-only actif | Certain, numérotation confuse |
| PR14 | PR124 — Controlled ATS Scout adapters | Adapters/normalizers Controlled ATS pour payloads fournis | actif, pure TS | Certain |
| PR15 | PR125 — Controlled ATS Public Endpoint Resolver | Resolver/fetcher public no-auth pour endpoints ATS connus | actif, boundary contrôlée | Certain |
| PR16 | PR126 — Local MCP Beta | Registry Local MCP, authz, dry-run adapter | actif, dry-run only | Certain |
| PR17 | PR127 — MCP / ChatGPT App Readiness Spec | Spec readiness MCP/ChatGPT App, pas de code | docs-only | Certain |

Écart de numérotation:
- Certain: deux éléments portent le label PR14 dans les sources PR: `ApplicationPackageV1 Convex shadow persistence` et `Controlled ATS Scout adapters`.
- Probable: la persistence ApplicationPackage est un PR additionnel inséré entre PR13 et PR14 Distribution.
- Action: clarifier la chronologie dans un document de roadmap ou une note d'audit.

# Comparaison au plan original

| Phase | Plan original | Implémentation réelle | Conforme ? | Écart | Action recommandée |
|---|---|---|---|---|---|
| Spine | Construire d'abord `application-harness`: contexte, runs, artifacts, idempotency, Convex shadow, ApplicationContext builder. Pas d'UI, export, tracking, Scout, MCP, génération. | `application-harness` pur + Convex shadow + builder. PR1.1/PR3.1 durcissent les anchors. | Oui | Les enums contiennent `export_artifact` et `track_application`, mais aucune exécution produit observée. | Ne pas câbler ces opérations avant approval/export gates explicites. |
| Proof Layer | Candidate evidence, CareerKnowledge, EvidenceGraph. Source truth stricte, facts approuvés, private/never_use exclus. | Modules `candidate-evidence`, `career-knowledge`, `evidence-graph` + persistence CandidateEvidence. Risk flags pour private, never_use, generated text, missing evidence, unsupported claims. | Oui | Matching EvidenceGraph déterministe mais simple. Cycle complet de suppression/rejet source doc à vérifier. | Renforcer tests edge cases et docs lifecycle facts/source docs. |
| Product Value Layer | ResumeVariantPlan, ReviewCockpit, artifacts, package, sans mutation CV canonical et sans export prématuré. | `resume-variant-plan`, `review-cockpit`, `resume-variant-artifact`, `cover-letter-artifact`, `application-package`, persistence package. | Oui | Noms réels diffèrent du plan: `resume-variant-plan`/`resume-variant-artifact` au lieu de `resume-variants`. Pas de statut `approved` package, seulement `ready_for_review`. | Clarifier noms et approval boundary avant tout export. |
| Distribution Layer | Internal tools, Controlled ATS, MCP local, readiness spec. Pas de scraping, pas d'auto-apply, pas de remote MCP trop tôt. | `internal-tool-contracts`, `controlled-ats-scout`, `local-mcp`, `mcp-readiness.md`. Local MCP est dry-run only. Controlled ATS limite les vendors et endpoints. | Oui | PR15 ajoute un fetcher public injecté. Remote MCP/ChatGPT App non prêt. Checklist PR17 non cochée. | PR18 doit rester pure schema projection. Pas de transport/OAuth/UI/real handler. |

# Modules audités

## Module: application-harness

### Type de fichier/module

Kernel TypeScript pur + persistence Convex shadow.

### Rôle dans l'architecture

Spine Application OS. Il définit les frontières `ApplicationContext`, `ApplicationRun`, `ApplicationArtifact`, `SourceRef`, les hashes stables et l'idempotency.

### Statut

- actif
- shadow-only pour Convex
- non UI
- non export réel

### Fichiers importants à lire

- `my-app/src/modules/application-harness/schema.ts`
- `my-app/src/modules/application-harness/fingerprints.ts`
- `my-app/src/modules/application-harness/idempotency.ts`
- `my-app/src/modules/application-harness/__tests__/fingerprints.test.ts`
- `my-app/src/modules/application-harness/__tests__/idempotency.test.ts`
- `my-app/convex/lib/applicationHarness.ts`
- `my-app/convex/applicationHarness.ts`
- `my-app/convex/applicationContextBuilder.ts`
- `my-app/convex/lib/applicationContextBuilder.ts`

### Fichiers à ne pas toucher sans demande explicite

- `my-app/convex/schema.ts`
- `my-app/convex/applicationHarness.ts`
- `my-app/convex/applicationContextBuilder.ts`
- Tout code UI/routes/export lié aux applications.

### Ce qui semble conforme au plan

Certain:
- Hash stable SHA-256 avec serializer déterministe.
- Rejet des valeurs non stables: fonctions, symboles, `Map`, `Set`, `RegExp`, `Promise`, cycles, arrays sparse, objets non plain.
- Candidate hash ancré par `cvId` ou `candidateEvidenceProfileId`.
- Convex `createContext` réutilise un contexte existant par stable id/hash et détecte collisions.
- Les runs Convex ont des transitions explicites `queued -> running -> succeeded/failed/blocked`.

### Écarts ou risques

Probable:
- Les opérations `export_artifact` et `track_application` existent comme valeurs de type. Ce n'est pas un problème actuel si elles restent non exécutées.

À vérifier:
- Aucun workflow produit ne doit appeler ces opérations sans approval gate.
- Les tests Convex doivent être exécutés localement.

### Cas limites à vérifier

- IDs inconnus dans queries Convex.
- Collision stable id/hash.
- Transition invalide de run.
- Input mutation dans builder ApplicationContext.
- `cvSnapshotHash` manquant côté builder.

### Tests existants

Certain:
- `fingerprints.test.ts` couvre hash stable, serializer, anchors candidats, non mutation.
- Des tests Convex existent pour `applicationHarness` et `applicationContextBuilder`.

### Vérifications recommandées

```bash
cd my-app
rtk npx vitest --run src/modules/application-harness/__tests__/*.test.ts
rtk npx vitest --run convex/__tests__/applicationHarness.test.ts
rtk npx vitest --run convex/lib/tests/applicationContextBuilder.test.ts
```

### Améliorations proposées

- Ajouter une note docs courte: `export_artifact` et `track_application` sont des intents typés, pas des actions produit autorisées.

## Module: candidate-evidence

### Type de fichier/module

Kernel TypeScript pur + persistence Convex shadow.

### Rôle dans l'architecture

Proof layer. Il transforme des sources candidat en documents/facts source-backed, avec review state et visibilité.

### Statut

- actif
- shadow-only pour Convex
- source-truth boundary

### Fichiers importants à lire

- `my-app/src/modules/candidate-evidence/schema.ts`
- `my-app/src/modules/candidate-evidence/fingerprints.ts`
- `my-app/src/modules/candidate-evidence/sourcePaths.ts`
- `my-app/src/modules/candidate-evidence/__tests__/candidateEvidence.test.ts`
- `my-app/convex/lib/candidateEvidence.ts`
- `my-app/convex/candidateEvidence.ts`

### Fichiers à ne pas toucher sans demande explicite

- `my-app/convex/schema.ts`
- `my-app/convex/candidateEvidence.ts`
- Toute logique qui modifie les facts source-truth.

### Ce qui semble conforme au plan

Certain:
- `visibility` supporte `private`, `use_in_applications`, `never_use`.
- `reviewState` supporte `pending`, `approved`, `rejected`, `needs_review`.
- `sourcePath` est normalisé et validé.
- Les chemins qui ressemblent à des artifacts générés, proposals, cover letters ou generated resumes sont rejetés.
- Les valeurs de fact contenant des clés comme `generatedText`, `polishedText`, `marketingCopy`, `proposalId`, `resumeVariantArtifactId` sont rejetées comme source material.
- La persistence Convex refuse de stocker du raw source text dans `CandidateSourceDocument`.
- Les facts sont hashés à partir de `userId`, `sourceDocumentId`, `sourcePath`, `factType`, `value`, et source quote/normalized text si présents.

### Écarts ou risques

À vérifier:
- Le plan original dit qu'un source doc supprimé/rejeté doit rendre les derived pending facts inéligibles sauf préservation explicite. Le code inspecté expose patch review/visibility, mais le cycle complet source-doc -> facts dérivés doit être testé en intégration.
- Les patchs Convex peuvent changer `reviewState` et `visibility`; cela doit rester interne et auditable.

### Cas limites à vérifier

Couvert dans tests:
- sourcePath vide.
- chemins generated/proposal/cover-letter.
- valeurs non JSON-like (`Map`, `Promise`, class instance).
- input mutation.

À vérifier:
- duplicate fact same sourcePath/value.
- sourceDocumentId inconnu.
- rejet/archivage source doc et effet sur facts.
- confidence hors plage.

### Tests existants

Certain:
- Tests source/fact hash, sourcePath validation, generated text guard, non mutation, import batch identity.
- Tests Convex candidate evidence présents.

### Vérifications recommandées

```bash
cd my-app
rtk npx vitest --run src/modules/candidate-evidence/__tests__/*.test.ts
rtk npx vitest --run convex/__tests__/candidateEvidence.test.ts
```

### Améliorations proposées

- Ajouter des tests lifecycle source doc rejeté/archivé -> facts non sélectionnables.
- Documenter que les mutations autorisées sont metadata-only (`reviewState`, `visibility`, batch status), pas mutation sémantique de `value`.

## Module: career-knowledge

### Type de fichier/module

Kernel TypeScript pur.

### Rôle dans l'architecture

Proof layer. Il fournit des règles statiques de sécurité carrière: source truth, claim safety, review gates, localization.

### Statut

- actif
- pure TS
- static rules only

### Fichiers importants à lire

- `my-app/src/modules/career-knowledge/schema.ts`
- `my-app/src/modules/career-knowledge/rules.ts`
- `my-app/src/modules/career-knowledge/resolver.ts`
- `my-app/src/modules/career-knowledge/__tests__/careerKnowledge.test.ts`

### Fichiers à ne pas toucher sans demande explicite

- `rules.ts`, car chaque règle influence EvidenceGraph et downstream.

### Ce qui semble conforme au plan

Certain:
- Le resolver filtre par document kind, market, language, target role, seniority, source types, fact types, artifact type.
- Les IDs de règles sont vérifiés uniques.
- Les marchés inconnus deviennent `other`.

### Écarts ou risques

Probable:
- Le corpus de règles est volontairement petit et statique.

À vérifier:
- Normalisation des languages/roles/seniority: le resolver compare les strings telles quelles pour certains champs.
- Couverture marché hors `global`.

### Cas limites à vérifier

- Input vide ou documentKind inconnu.
- Language/market casing.
- Règles dupliquées.
- Règles blocker sans downstream risk flag.

### Tests existants

Certain:
- Suite `careerKnowledge.test.ts` présente.

### Vérifications recommandées

```bash
cd my-app
rtk npx vitest --run src/modules/career-knowledge/__tests__/*.test.ts
```

### Améliorations proposées

- Ajouter un petit tableau docs: règle -> risque downstream attendu.

## Module: evidence-graph

### Type de fichier/module

Kernel TypeScript pur.

### Rôle dans l'architecture

Proof layer. Il connecte `JobDemand`, `CandidateFact`, `CareerKnowledgeRule`, puis produit matches, missing evidence, risk flags, allowed claims, blocked claims.

### Statut

- actif
- pure TS
- shadow graph

### Fichiers importants à lire

- `my-app/src/modules/evidence-graph/schema.ts`
- `my-app/src/modules/evidence-graph/buildEvidenceGraph.ts`
- `my-app/src/modules/evidence-graph/riskRules.ts`
- `my-app/src/modules/evidence-graph/__tests__/evidenceGraph.test.ts`

### Fichiers à ne pas toucher sans demande explicite

- `riskRules.ts`
- `buildEvidenceGraph.ts`

### Ce qui semble conforme au plan

Certain:
- Allowed claims ne viennent que de facts `approved` + `use_in_applications`.
- `private` et `never_use` créent des blockers et ne deviennent pas des allowed claims.
- Le generated text en fact est bloqué.
- Missing evidence et unsupported metrics/language/certification sont signalés.
- Les tests couvrent déterminisme, non mutation, ordering, private, never_use, generated text, source support.

### Écarts ou risques

Probable:
- Le matching est lexical/déterministe et volontairement simple. Il n'est pas une preuve sémantique forte.
- Les fichiers source sont très minifiés. C'est maintenable par tests, mais difficile pour un junior.

À vérifier:
- Comportement avec duplicate demands/facts.
- Labels vides ou très longs.
- User mismatch entre facts et graph input.

### Cas limites à vérifier

Couvert dans tests:
- ordre déterministe.
- input mutation.
- `private` / `never_use`.
- generated fact.
- metric sans source numérique.

À vérifier:
- IDs dupliqués.
- sourceDocumentId inconnu.
- demanded skill avec synonymes non triviaux.
- facts approuvés mais hors user/application.

### Tests existants

Certain:
- `evidenceGraph.test.ts` est dense et couvre beaucoup de garde-fous de sécurité.

### Vérifications recommandées

```bash
cd my-app
rtk npx vitest --run src/modules/evidence-graph/__tests__/*.test.ts
```

### Améliorations proposées

- Ajouter tests duplicate IDs et empty labels.
- Ne pas remplacer le matching par LLM.
- Si lisibilité nécessaire, faire une PR format-only avec snapshot avant/après et aucun changement logique.

## Module: resume-variants

### Type de fichier/module

Le plan parle de `resume-variants`. L'implémentation réelle est séparée en:

- `my-app/src/modules/resume-variant-plan/`
- `my-app/src/modules/resume-variant-artifact/`

### Rôle dans l'architecture

Product Value layer. Transformer EvidenceGraph + review state en plan, puis en artifact metadata source-backed, sans modifier le CV canonical.

### Statut

- actif
- pure TS
- pas de génération texte finale dans `resume-variant-artifact`

### Fichiers importants à lire

- `my-app/src/modules/resume-variant-plan/schema.ts`
- `my-app/src/modules/resume-variant-plan/buildResumeVariantPlan.ts`
- `my-app/src/modules/resume-variant-plan/planRules.ts`
- `my-app/src/modules/resume-variant-artifact/schema.ts`
- `my-app/src/modules/resume-variant-artifact/buildResumeVariantArtifact.ts`
- `my-app/src/modules/resume-variant-artifact/artifactRules.ts`

### Fichiers à ne pas toucher sans demande explicite

- Builders plan/artifact.
- Tout code de CV canonical.
- Tout export PDF/DOCX.

### Ce qui semble conforme au plan

Certain:
- `ResumeVariantPlan` référence EvidenceGraph, allowed claims, source facts, risks, blocked claims.
- Claim-backed plan items exigent allowed claims, candidate facts, accepted matches et refusent les excluded facts.
- Le plan bloque si warnings blocker.
- `ResumeVariantArtifact` vérifie les IDs connus et la provenance.
- `ResumeVariantArtifact` ne construit pas un CV final; il construit des sections/items metadata.

### Écarts ou risques

Probable:
- Le nom module diffère du plan original. Ce n'est pas un bug, mais c'est déroutant pour un junior.

À vérifier:
- `ResumeVariantPlan` hash inclut `createdAt` et `updatedAt` dans l'input hash. Cela peut être voulu, mais c'est à confirmer si l'idempotency logique doit ignorer les timestamps.

### Cas limites à vérifier

- Plan item qui référence une allowed claim inconnue.
- Allowed claim blocked après plan.
- Timestamps modifiés seulement.
- Graph vide.
- Risk flags orphelins.

### Tests existants

Certain:
- Suites `resumeVariantPlan.test.ts` et `resumeVariantArtifact.test.ts` présentes.

### Vérifications recommandées

```bash
cd my-app
rtk npx vitest --run src/modules/resume-variant-plan/__tests__/*.test.ts
rtk npx vitest --run src/modules/resume-variant-artifact/__tests__/*.test.ts
```

### Améliorations proposées

- Ajouter une note dans docs: `resume-variants` dans le plan = `resume-variant-plan` + `resume-variant-artifact` dans le code.
- Vérifier la politique timestamp/hash.

## Module: review-cockpit

### Type de fichier/module

Kernel TypeScript pur, model-only.

### Rôle dans l'architecture

Product Value layer. Regrouper les warnings, missing evidence, blocked claims, plan items et source support pour une future revue humaine.

### Statut

- actif
- model-only
- pas d'UI
- pas de Convex persistence dédiée observée

### Fichiers importants à lire

- `my-app/src/modules/review-cockpit/schema.ts`
- `my-app/src/modules/review-cockpit/buildReviewCockpit.ts`
- `my-app/src/modules/review-cockpit/__tests__/reviewCockpit.test.ts`

### Fichiers à ne pas toucher sans demande explicite

- Toute route/page UI future.
- Builder cockpit si le besoin est seulement docs/tests.

### Ce qui semble conforme au plan

Certain:
- Status: `ready`, `needs_review`, `blocked`.
- Items en buckets: allowed claims, plan items, warnings, missing evidence, blocked claims, source support.
- Le modèle référence EvidenceGraph et ResumeVariantPlan.
- PR9 indique explicitement pas de page/shell/UI.

### Écarts ou risques

À vérifier:
- Taille de sortie pour gros graph.
- Future UI doit rester read-only au début.

### Cas limites à vérifier

- Graph sans allowed claims.
- Beaucoup de warnings.
- Items dupliqués.
- Risk flag sans demandId.

### Tests existants

Certain:
- Suite `reviewCockpit.test.ts` présente.

### Vérifications recommandées

```bash
cd my-app
rtk npx vitest --run src/modules/review-cockpit/__tests__/*.test.ts
```

### Améliorations proposées

- Ajouter limites de taille attendues dans docs avant UI.

## Module: cover-letter-artifact

### Type de fichier/module

Kernel TypeScript pur.

### Rôle dans l'architecture

Product Value layer. Adapter un texte de cover letter déjà fourni en artifact provenance-backed.

### Statut

- actif
- pure TS
- artifact text réel, mais pas génération nouvelle

### Fichiers importants à lire

- `my-app/src/modules/cover-letter-artifact/schema.ts`
- `my-app/src/modules/cover-letter-artifact/buildCoverLetterArtifact.ts`
- `my-app/src/modules/cover-letter-artifact/artifactRules.ts`
- `my-app/src/modules/cover-letter-artifact/__tests__/coverLetterArtifact.test.ts`

### Fichiers à ne pas toucher sans demande explicite

- Builder cover-letter artifact.
- Générateur cover letter existant/historique.
- Export/send/submit.

### Ce qui semble conforme au plan

Certain:
- Le module conserve un texte fourni avec hash, métriques, source kind et provenance.
- Il hérite de la provenance du resume variant artifact.

### Écarts ou risques

Probable:
- Comme il peut contenir un texte final, ce module est plus sensible que `resume-variant-artifact`.

À vérifier:
- Aucun export/send ne consomme cet artifact sans approval.
- SourceKind `existing_generated_output` doit rester artifact-only, pas fact source.

### Cas limites à vérifier

- Texte vide.
- Texte très long.
- Metadata source incomplète.
- Hash stable si format/sourceKind change.

### Tests existants

Certain:
- Suite `coverLetterArtifact.test.ts` présente.

### Vérifications recommandées

```bash
cd my-app
rtk npx vitest --run src/modules/cover-letter-artifact/__tests__/*.test.ts
```

### Améliorations proposées

- Documenter clairement que `CoverLetterArtifact.text.value` peut contenir de la prose générée/importée, mais ne doit jamais devenir `CandidateFact`.

## Module: application-package

### Type de fichier/module

Kernel TypeScript pur + persistence Convex shadow.

### Rôle dans l'architecture

Product Value layer. Composer resume variant artifact + cover letter artifact + provenance en package reviewable.

### Statut

- actif
- pure TS
- shadow-only pour Convex
- pas d'export réel

### Fichiers importants à lire

- `my-app/src/modules/application-package/schema.ts`
- `my-app/src/modules/application-package/buildApplicationPackage.ts`
- `my-app/src/modules/application-package/packageRules.ts`
- `my-app/src/modules/application-package/__tests__/applicationPackage.test.ts`
- `my-app/convex/lib/applicationPackages.ts`
- `my-app/convex/applicationPackages.ts`

### Fichiers à ne pas toucher sans demande explicite

- `my-app/convex/schema.ts`
- `my-app/convex/applicationPackages.ts`
- Tout export PDF/DOCX/download/send/apply.

### Ce qui semble conforme au plan

Certain:
- Package references artifacts; il ne duplique pas le texte resume/cover letter dans les items.
- Status dérivé: `draft`, `needs_review`, `blocked`, `ready_for_review`.
- Provenance unionnée depuis les artifacts.
- Hash package stable ignore timestamps pour identité package.
- Persistence shadow stocke `ApplicationPackageV1` avec index fields, contentHash, collision detection.
- Storage refuse des champs top-level interdits comme `rawText`, `resumeText`, `coverLetterText`, `pdf`, `docx`, `exportOutput`, `toolExecutionLogs`, `approvalDecision`.

### Écarts ou risques

Certain:
- Numérotation PR confuse: persistence package est appelée PR14 dans GitHub alors que PR14 du plan est Controlled ATS.

À vérifier:
- Le status `ready_for_review` ne doit pas être traité comme `approved` par une future UI/export.
- Aucun endpoint public ne doit exposer `package.package` brut sans privacy filter.

### Cas limites à vérifier

Couvert dans tests:
- status blocked/needs_review/draft/ready_for_review.
- non mutation inputs.
- pas de texte raw direct dans package serialized.
- content hash ignore id/timestamps et change sur contenu significatif.

À vérifier:
- Artifact inconnu en persistence réelle.
- Package avec provenance vide.
- Package `ready_for_review` utilisé à tort comme approval.

### Tests existants

Certain:
- `applicationPackage.test.ts` est présent.
- `convex/__tests__/applicationPackages.test.ts` est présent.

### Vérifications recommandées

```bash
cd my-app
rtk npx vitest --run src/modules/application-package/__tests__/*.test.ts
rtk npx vitest --run convex/__tests__/applicationPackages.test.ts
```

### Améliorations proposées

- Ajouter une doc gate: `ready_for_review` signifie reviewable, pas exportable.

## Module: internal-tool-contracts

### Type de fichier/module

Kernel TypeScript pur.

### Rôle dans l'architecture

Distribution layer. Décrire les outils internes autorisés avant MCP/ChatGPT App.

### Statut

- actif
- pure TS
- contract-only
- pas d'exécution métier

### Fichiers importants à lire

- `my-app/src/modules/internal-tool-contracts/schema.ts`
- `my-app/src/modules/internal-tool-contracts/contracts.ts`
- `my-app/src/modules/internal-tool-contracts/contractRules.ts`
- `my-app/src/modules/internal-tool-contracts/__tests__/internalToolContracts.test.ts`

### Fichiers à ne pas toucher sans demande explicite

- `contracts.ts`
- `contractRules.ts`
- Toute future passerelle MCP/remote.

### Ce qui semble conforme au plan

Certain:
- Les effects sont limités à `read_only` et `pure_compute`.
- Les tool IDs sont des summarize/describe/validate/list.
- Les terms `export`, `send`, `submit`, `apply`, `track`, `generation`, `mcp`, `scout`, `scrape`, `crawl` sont interdits dans les IDs.
- Les metadata actives ne doivent pas impliquer export/download/send/network/remote/http/scrape/write/persist.

### Écarts ou risques

À vérifier:
- Les contracts medium ont `requiresApproval: false` dans le catalogue interne, tandis que Local MCP impose approval selon riskLevel. C'est acceptable si le catalogue est descriptif, mais tout futur caller hors Local MCP doit appliquer une politique équivalente.

### Cas limites à vérifier

- Contract draft/blocked exposé par erreur.
- Metadata qui contourne les terms interdits.
- Output trop gros pour MCP futur.

### Tests existants

Certain:
- Suite `internalToolContracts.test.ts` présente.

### Vérifications recommandées

```bash
cd my-app
rtk npx vitest --run src/modules/internal-tool-contracts/__tests__/*.test.ts
```

### Améliorations proposées

- Documenter la séparation: internal contracts décrivent; Local MCP autorise/refuse.

## Module: controlled-ats-scout

### Type de fichier/module

Kernel TypeScript pur + fetch boundary injectée.

### Rôle dans l'architecture

Distribution layer contrôlée. Normaliser des payloads ATS fournis et résoudre/fetcher des endpoints publics no-auth de vendors connus.

### Statut

- actif
- boundary contrôlée
- pas de scraping LinkedIn/Upwork/Indeed
- pas de browser automation
- pas de submit/apply

### Fichiers importants à lire

- `my-app/src/modules/controlled-ats-scout/schema.ts`
- `my-app/src/modules/controlled-ats-scout/adapters.ts`
- `my-app/src/modules/controlled-ats-scout/scoutRules.ts`
- `my-app/src/modules/controlled-ats-scout/sourceResolver.ts`
- `my-app/src/modules/controlled-ats-scout/publicEndpointFetcher.ts`
- `my-app/src/modules/controlled-ats-scout/__tests__/controlledAtsScout.test.ts`
- `my-app/src/modules/controlled-ats-scout/__tests__/controlledAtsPublicEndpoints.test.ts`

### Fichiers à ne pas toucher sans demande explicite

- `publicEndpointFetcher.ts`
- `sourceResolver.ts`
- Toute intégration réseau produit/background.
- Tout support LinkedIn/Upwork/Indeed.

### Ce qui semble conforme au plan

Certain:
- Vendors supportés: Greenhouse, Lever, Ashby, SmartRecruiters, Recruitee.
- Vendors explicitement interdits: LinkedIn, Upwork, Indeed, generic web, unknown scraper.
- Endpoints publics résolus sont `GET`, `authKind: none`, avec `maxResponseBytes`, `timeoutMs`, pagination bornée.
- Fetcher utilise `fetchImpl` injecté, rejette redirects, non-200, non-JSON, oversized, invalid JSON, auth headers.
- Tests couvrent resolver Greenhouse/Lever/SmartRecruiters/Recruitee, forbidden URLs, HTTPS, fetch injected, pagination.

### Écarts ou risques

Probable:
- Ashby est dans les adapters payload, mais pas dans le resolver public endpoint inspecté. Cela peut être volontaire.

À vérifier:
- Timeout réel aborté côté fetchImpl.
- Limites rate-limit produit si ce fetcher est branché plus tard.
- Aucune intégration background automatique.

### Cas limites à vérifier

Couvert dans tests:
- unsupported/forbidden URLs.
- pagination Lever/SmartRecruiters.
- redirect, non-json, invalid JSON, too large.

À vérifier:
- timeout réseau effectif.
- max pages atteint.
- payload ATS inattendu mais JSON valide.
- URLs ATS avec sous-domaines non standards.

### Tests existants

Certain:
- `controlledAtsScout.test.ts` et `controlledAtsPublicEndpoints.test.ts` présents.

### Vérifications recommandées

```bash
cd my-app
rtk npx vitest --run src/modules/controlled-ats-scout/__tests__/*.test.ts
```

### Améliorations proposées

- Ajouter un test explicite abort/timeout.
- Garder le fetcher non câblé à un crawler produit tant qu'il n'y a pas de policy PR séparée.

## Module: local-mcp

### Type de fichier/module

Kernel TypeScript pur.

### Rôle dans l'architecture

Distribution layer locale. Préparer un modèle MCP local sans transport réseau, sans vrai handler, sans ChatGPT App.

### Statut

- actif
- dry-run only
- local-only
- pas de remote MCP
- pas de product mutation

### Fichiers importants à lire

- `my-app/src/modules/local-mcp/schema.ts`
- `my-app/src/modules/local-mcp/toolRegistry.ts`
- `my-app/src/modules/local-mcp/authz.ts`
- `my-app/src/modules/local-mcp/localMcpAdapter.ts`
- `my-app/src/modules/local-mcp/__tests__/localMcp.test.ts`

### Fichiers à ne pas toucher sans demande explicite

- Tout transport MCP réel.
- ChatGPT App.
- OAuth.
- Deployment config.
- Handlers métiers réels.

### Ce qui semble conforme au plan

Certain:
- Quatre outils locaux seulement: application package summary, evidence graph summary, resume variant plan summary, review cockpit summary.
- Tous mapent vers des internal tools allowlisted.
- Medium risk requiert approval dans Local MCP.
- Requests malformées, unknown tool, missing user, missing approval sont refusés de façon structurée.
- `executeLocalMcpRequest` retourne un `local_mcp_dry_run` et ne fait aucune exécution métier.
- Tests vérifient absence d'import réseau/UI/routes/Convex dans les fichiers local MCP.

### Écarts ou risques

À vérifier:
- Output size limits pour PR18+.
- Privacy filters explicites pour private/never_use dans schema MCP futur.
- Audit log approval pour future real handler.

### Cas limites à vérifier

Couvert dans tests:
- unknown tool.
- approval missing.
- malformed request.
- non mutation inputs.
- absence de remote host markers.

À vérifier:
- payload très gros.
- argument contenant valeurs non JSON-like.
- approval expirée ou mauvais reviewer.

### Tests existants

Certain:
- `localMcp.test.ts` présent et couvre registry, authz, adapter, dry-run, security boundaries.

### Vérifications recommandées

```bash
cd my-app
rtk npx vitest --run src/modules/local-mcp/__tests__/*.test.ts
```

### Améliorations proposées

- PR18 doit rester schema projection pure, sans transport ni handler réel.

## Module: mcp-readiness docs

### Type de fichier/module

Documentation plan/spec.

### Rôle dans l'architecture

Définir ce qui manque avant Remote MCP ou ChatGPT App.

### Statut

- docs-only
- actif comme référence future
- pas de code

### Fichiers importants à lire

- `docs/plans/2026-06-11-mcp-readiness.md`
- `docs/decisions/2026-06-11-local-mcp-beta.md`
- `docs/decisions/2026-06-10-internal-tool-contracts.md`

### Fichiers à ne pas toucher sans demande explicite

- Transport MCP.
- ChatGPT App manifest/config.
- OAuth/deployment.

### Ce qui semble conforme au plan

Certain:
- La doc dit explicitement que le système n'est pas prêt pour Remote MCP ou ChatGPT App.
- La prochaine étape sûre recommandée est une projection de schéma MCP pure TypeScript.
- Les non-goals excluent auto-apply, submit/send, scraping, browser automation, generic crawling, unaudited real actions.

### Écarts ou risques

Probable:
- La checklist sécurité est utile mais non cochée et doit devenir une gate avant transport.
- Les références de versions MCP sont possiblement hétérogènes selon la review PR17.

À vérifier:
- Mettre à jour les liens/spec versions MCP avant PR18 si la doc sert de base directe.

### Cas limites à vérifier

- Tool schema incomplet.
- Privacy filters manquants.
- Rate limit / timeout / output size.
- Approval/audit non persisté.

### Tests existants

Sans objet: docs-only.

### Vérifications recommandées

```bash
rtk git diff --check
```

### Améliorations proposées

- Ajouter un milestone clair: aucune PR transport/ChatGPT App tant que la checklist sécurité PR17 n'est pas validée.

# Risques transversaux

| Risque | Statut actuel | Preuve/source | Sévérité | Action |
|---|---|---|---|---|
| mutation involontaire des CV canoniques | Mitigé dans les modules inspectés. Aucun module inspecté ne modifie le CV canonical. | Plan original + absence de changement UI/routes/CV canonical dans diff inspecté. | P1 si réintroduit | Ne pas toucher au canonical CV. Ajouter tests d'intégration si un jour un writer apparaît. |
| mutation des candidate facts | Partiellement mitigé. `value` est créé via hash/source material; patchs Convex changent review/visibility. | `candidate-evidence`, `convex/candidateEvidence.ts`. | P2 | Documenter metadata-only mutation. Tester lifecycle source doc/facts. |
| generated text sans provenance | Mitigé dans EvidenceGraph/Plan/Package metadata. Cover letter artifact peut contenir texte fourni avec provenance. | `sourcePaths.ts`, `riskRules.ts`, `buildApplicationPackage.ts`. | P2 | Ne jamais transformer generated artifact text en CandidateFact. |
| export avant approval | Non implémenté. Type-level seulement dans harness. | `application-harness/schema.ts`, `convex/lib/applicationHarness.ts`. | P1 | Ne pas créer export. Définir approval gate avant tout export. |
| tracking avant approval | Non implémenté. Type-level seulement dans harness. | `application-harness/schema.ts`. | P1 | Ne pas créer tracking. Définir gate séparée. |
| send / submit / apply non autorisé | Non implémenté et explicitement interdit par docs/contracts/tests. | `contractRules.ts`, `localMcp.test.ts`, MCP readiness. | P1 | Garder interdit. Refuser toute PR submit/apply/send. |
| scraping LinkedIn / Upwork / Indeed | Mitigé. URLs interdites dans Controlled ATS. | `controlled-ats-scout/schema.ts`, `scoutRules.ts`, tests public endpoint. | P1 | Ne pas ajouter support LinkedIn/Upwork/Indeed. |
| réseau ou remote MCP trop tôt | Mitigé pour MCP: Local MCP dry-run only. Attention: Controlled ATS a un fetcher public injecté. | `local-mcp`, `controlled-ats-scout/publicEndpointFetcher.ts`. | P2 | Garder PR18 pure schema. Pas de transport MCP. |
| outil MCP qui possède de la logique métier | Mitigé. `executeLocalMcpRequest` retourne dry-run seulement. | `localMcpAdapter.ts`. | P1 | Ne pas ajouter real handler avant PR20/PR21 et audit/approval. |
| persistence non auditée | Partiellement auditée: AppHarness, CandidateEvidence, ApplicationPackage. Pas de tests lancés ici. | `convex/schema.ts`, `convex/*`. | P2 | Lancer tests Convex et documenter lifecycle. |
| output privé exposé publiquement | Mitigé localement, mais pas prouvé pour futures surfaces publiques. | Pas de UI/remote endpoint inspecté. | P1 | Aucun endpoint public avant privacy filter explicite. |
| never_use fact exposée | Mitigé par EvidenceGraph/Plan. À vérifier dans tout futur MCP/export. | `evidence-graph`, tests EvidenceGraph. | P1 | Ajouter tests PR18+ sur privacy projection. |
| dépendances inutilisées héritées | Hors périmètre PR1-PR17; package files non touchés dans diff inspecté. | Comparaison de branche. | P3 | Ne pas modifier deps sans besoin. |
| tests insuffisants ou trop étroits | Tests nombreux, mais edge cases intégration restent. | Suites modules + Convex présentes. | P2 | Renforcer tests ciblés, pas refactor global. |
| docs divergentes du code réel | Présent: noms modules et PR14/PR122 confus. | Docs + PR list + paths réels. | P2 | Ajouter une note de roadmap réelle. |

# Cas limites à vérifier

## application-harness

Couvert:
- serializer non déterministe / types non supportés.
- circular objects/arrays.
- candidate anchor manquant.
- input mutation helpers.

À vérifier:
- run status transition invalides côté Convex.
- collisions stable id/contextHash en environnement réel.
- opérations `export_artifact` / `track_application` jamais câblées sans gate.

## candidate-evidence

Couvert:
- sourcePath vide/unsafe/generated.
- generated artifact fields dans fact value.
- non mutation input.
- unsupported values avant hash.

À vérifier:
- sourceDocumentId inconnu.
- duplication fact même sourcePath/value.
- source doc rejected/archived et facts dérivés.
- confidence hors plage.

## career-knowledge

À vérifier:
- casing language/market.
- rôle/seniority non normalisés.
- règle blocker non propagée à downstream.

## evidence-graph

Couvert:
- private facts.
- never_use facts.
- generated text as fact.
- missing evidence.
- unsupported metric/language/certification.
- input mutation.
- ordre déterministe.

À vérifier:
- duplicate IDs.
- demands vides.
- labels très longs.
- sourceDocumentId/fact user mismatch.

## resume-variant-plan / resume-variant-artifact

À vérifier:
- timestamps seuls et idempotency attendue.
- allowed claim supprimée après plan.
- graph vide.
- risk flag orphelin.
- artifact avec review cockpit divergent.

## review-cockpit

À vérifier:
- très gros graph.
- beaucoup de warnings/blockers.
- déduplication items.
- output size pour MCP futur.

## cover-letter-artifact

À vérifier:
- texte vide.
- texte énorme.
- sourceKind `existing_generated_output` exposé sans approval.
- metadata source incomplète.

## application-package

Couvert:
- status upstream.
- no raw cover-letter/resume text direct.
- content hash stable.
- provenance union.
- non mutation inputs.

À vérifier:
- `ready_for_review` jamais traité comme approval.
- package exposé par endpoint public.
- artifact IDs inconnus en storage.

## internal-tool-contracts

À vérifier:
- futur caller hors Local MCP qui ignorerait approval.
- metadata contourne terms interdits.
- output schema trop large.

## controlled-ats-scout

Couvert:
- forbidden URLs LinkedIn/Upwork/Indeed.
- HTTPS only.
- redirects/non-json/invalid-json/oversize.
- pagination Lever/SmartRecruiters.

À vérifier:
- timeout/abort effectif.
- max pages atteint.
- Ashby resolver public absent ou volontairement payload-only.
- payload JSON inattendu.

## local-mcp

Couvert:
- unknown tool.
- missing user.
- missing approval.
- malformed request.
- dry-run only.
- absence de network/UI imports.

À vérifier:
- output trop gros.
- approval expirée ou mauvais reviewer.
- schema projection MCP officielle.
- privacy filters remote.

# Couverture de tests

| Suite | Existe ? | Ce qu'elle couvre | Manques probables | Commande recommandée |
|---|---|---|---|---|
| application-harness | Oui | hash stable, serializer, anchors, non mutation, idempotency | transitions Convex à confirmer | `cd my-app && rtk npx vitest --run src/modules/application-harness/__tests__/*.test.ts` |
| application-harness Convex | Oui | persistence contexts/runs/artifacts | CI locale à lancer | `cd my-app && rtk npx vitest --run convex/__tests__/applicationHarness.test.ts` |
| ApplicationContext builder Convex | Oui | builder shadow, projection/hash | intégration données réelles | `cd my-app && rtk npx vitest --run convex/lib/tests/applicationContextBuilder.test.ts` |
| candidate-evidence | Oui | source/fact hash, sourcePath, generated guard, non mutation | lifecycle source doc -> facts | `cd my-app && rtk npx vitest --run src/modules/candidate-evidence/__tests__/*.test.ts` |
| candidate-evidence Convex | Oui | create/reuse, patch, validators | rejet source doc cascade | `cd my-app && rtk npx vitest --run convex/__tests__/candidateEvidence.test.ts` |
| career-knowledge | Oui | resolver/rules | casing/normalization | `cd my-app && rtk npx vitest --run src/modules/career-knowledge/__tests__/*.test.ts` |
| evidence-graph | Oui | private/never_use/generated/missing/metrics/determinism | duplicate IDs, empty labels | `cd my-app && rtk npx vitest --run src/modules/evidence-graph/__tests__/*.test.ts` |
| resume-variant-plan | Oui | plan items, blockers, provenance | timestamp/idempotency à confirmer | `cd my-app && rtk npx vitest --run src/modules/resume-variant-plan/__tests__/*.test.ts` |
| resume-variant-artifact | Oui | artifact sections, provenance, source backing | gros graph | `cd my-app && rtk npx vitest --run src/modules/resume-variant-artifact/__tests__/*.test.ts` |
| review-cockpit | Oui | summary/items/status | output size futur MCP | `cd my-app && rtk npx vitest --run src/modules/review-cockpit/__tests__/*.test.ts` |
| cover-letter-artifact | Oui | supplied text artifact, provenance | texte très long/vide | `cd my-app && rtk npx vitest --run src/modules/cover-letter-artifact/__tests__/*.test.ts` |
| application-package | Oui | status, package refs, provenance, no raw text direct | approval/export boundary | `cd my-app && rtk npx vitest --run src/modules/application-package/__tests__/*.test.ts` |
| application-package Convex | Oui | storage record, collision/contentHash | données réelles | `cd my-app && rtk npx vitest --run convex/__tests__/applicationPackages.test.ts` |
| internal-tool-contracts | Oui | registry, forbidden terms, cloning/sorting | future callers approval | `cd my-app && rtk npx vitest --run src/modules/internal-tool-contracts/__tests__/*.test.ts` |
| controlled-ats-scout | Oui | adapters, resolver, fetch boundary, forbidden URLs | timeout/max pages | `cd my-app && rtk npx vitest --run src/modules/controlled-ats-scout/__tests__/*.test.ts` |
| local-mcp | Oui | registry, authz, dry-run, security boundaries | output size, remote schemas | `cd my-app && rtk npx vitest --run src/modules/local-mcp/__tests__/*.test.ts` |

Commande TypeScript recommandée:

```bash
cd my-app
rtk npx tsc --noEmit
```

Note:
- La commande demandée `src/modules/resume-variants/__tests__/*.test.ts` ne correspond pas au path réel inspecté.
- Utiliser `resume-variant-plan` et `resume-variant-artifact`.

# Cohérence documentation ↔ code

Certain:
- Le plan original exige de construire le Spine avant Proof/Product/Distribution. L'ordre réel respecte cette intention.
- Les modules de distribution restent contrôlés: Local MCP est dry-run only; MCP readiness est docs-only; Controlled ATS interdit les vendors sensibles.
- Les dossiers docs/decisions et docs/plans contiennent les décisions par PR.

Divergences:
- Le plan parle de `resume-variants`; le code utilise `resume-variant-plan` et `resume-variant-artifact`.
- Le plan mentionne `application-review`; le code livré s'appelle `review-cockpit`.
- Le plan mentionne `application-packages`; le code utilise `application-package` et `applicationPackages` côté Convex.
- PR122 est titrée PR14 ApplicationPackageV1 Convex shadow persistence, alors que PR124 est aussi PR14 Controlled ATS Scout adapters.
- `mcp-readiness.md` contient une checklist sécurité non cochée. Elle doit devenir une gate avant transport.

À vérifier:
- Les PR bodies complètes si besoin de reconstruire une chronologie officielle.
- Les versions de specs MCP citées dans `mcp-readiness.md` avant PR18.

# Améliorations proposées

## Amélioration 1 — Clarifier la roadmap réelle PR1-PR17

### Priorité
P2

### Pourquoi
La numérotation PR14 est confuse et les noms de modules diffèrent du plan original. Un junior risque de chercher `resume-variants` ou de croire que PR14 a deux contenus concurrents.

### Fichiers à lire
- `docs/decisions/2026-06-08-application-os-master-plan.md`
- `docs/decisions/2026-06-10-application-package-shadow-persistence.md`
- `docs/decisions/2026-06-10-controlled-ats-scout-adapters.md`
- `docs/plans/2026-06-11-mcp-readiness.md`

### Fichiers à modifier
- Uniquement une doc roadmap ou audit, par exemple ce document ou un futur `docs/decisions/...roadmap-reconciliation.md`.

### Étapes exactes pour un junior
1. Lister PR logique, PR GitHub, titre, fichiers livrés.
2. Ajouter une note: PR122 est un PR additionnel de persistence package.
3. Ajouter une note de mapping: `resume-variants` = `resume-variant-plan` + `resume-variant-artifact`.
4. Ne modifier aucun fichier source.

### Risques
- Introduire une nouvelle numérotation incorrecte.

### Cas limites
- PR fix-forward comme PR1.1, PR3.1, PR6.1.

### Vérifications
```bash
rtk git diff --check
```

### Hors scope explicite
- Renommer les dossiers.
- Modifier les imports.
- Réécrire l'architecture.

## Amélioration 2 — Renforcer les tests edge cases EvidenceGraph

### Priorité
P2

### Pourquoi
EvidenceGraph est critique: c'est lui qui empêche private/never_use/generated/missing evidence de devenir des claims. Les tests sont bons, mais certains cas intégration restent à verrouiller.

### Fichiers à lire
- `my-app/src/modules/evidence-graph/buildEvidenceGraph.ts`
- `my-app/src/modules/evidence-graph/riskRules.ts`
- `my-app/src/modules/evidence-graph/__tests__/evidenceGraph.test.ts`

### Fichiers à modifier
- `my-app/src/modules/evidence-graph/__tests__/evidenceGraph.test.ts`
- Code source seulement si un test révèle un bug réel.

### Étapes exactes pour un junior
1. Ajouter un test duplicate demand ids.
2. Ajouter un test duplicate candidate fact ids.
3. Ajouter un test empty demand label.
4. Ajouter un test fact user mismatch si la politique attend un rejet.
5. Exécuter la suite EvidenceGraph.

### Risques
- Changer le matching au lieu de le caractériser.

### Cas limites
- Ordre déterministe.
- Missing evidence non contradictoire avec private/never_use.

### Vérifications
```bash
cd my-app
rtk npx vitest --run src/modules/evidence-graph/__tests__/*.test.ts
```

### Hors scope explicite
- Matching LLM.
- Synonym engine.
- Refactor global.

## Amélioration 3 — Vérifier lifecycle CandidateEvidence Convex

### Priorité
P2

### Pourquoi
Le plan exige qu'un source doc rejeté/supprimé rende les pending facts dérivés inéligibles sauf préservation explicite. Le code inspecté couvre review/visibility patchs, mais le cycle complet doit être prouvé.

### Fichiers à lire
- `my-app/convex/candidateEvidence.ts`
- `my-app/convex/lib/candidateEvidence.ts`
- `my-app/convex/__tests__/candidateEvidence.test.ts`
- `my-app/src/modules/candidate-evidence/sourcePaths.ts`

### Fichiers à modifier
- Tests Convex candidateEvidence uniquement, sauf bug.

### Étapes exactes pour un junior
1. Lire les patch functions disponibles.
2. Identifier si source doc reviewState peut être patché.
3. Ajouter un test qui vérifie l'effet attendu sur facts dérivés.
4. Si aucun comportement n'existe, documenter “à implémenter plus tard” sans inventer un cascade.

### Risques
- Ajouter une mutation destructive de facts.

### Cas limites
- Source doc `archived`.
- Fact déjà `approved`.
- Fact `never_use`.

### Vérifications
```bash
cd my-app
rtk npx vitest --run convex/__tests__/candidateEvidence.test.ts
```

### Hors scope explicite
- Import parser.
- UI review.
- Bulk delete.

## Amélioration 4 — Formaliser la gate package approval/export

### Priorité
P2

### Pourquoi
`ApplicationPackageV1` atteint `ready_for_review`, pas `approved`. Tout export futur doit vérifier une approval explicite.

### Fichiers à lire
- `my-app/src/modules/application-package/schema.ts`
- `my-app/src/modules/application-package/packageRules.ts`
- `docs/decisions/2026-06-10-application-package-v1.md`
- `docs/decisions/2026-06-08-application-os-master-plan.md`

### Fichiers à modifier
- Docs uniquement dans une première PR.
- Tests/contracts uniquement dans une PR séparée si demandée.

### Étapes exactes pour un junior
1. Ajouter une note docs: `ready_for_review` ne permet pas export.
2. Lister les conditions futures minimales: approval id, reviewer, timestamp, package contentHash, privacy check.
3. Ne pas créer d'export.

### Risques
- Confondre review-ready et user-approved.

### Cas limites
- Package blocked.
- Cover letter text présent mais non approuvé.
- Package contentHash changé après approval.

### Vérifications
```bash
rtk git diff --check
```

### Hors scope explicite
- PDF/DOCX.
- Download/export.
- Send/submit/apply.

## Amélioration 5 — Préparer PR18 MCP schema projection seulement

### Priorité
P2

### Pourquoi
PR17 dit que le système n'est pas prêt pour Remote MCP/ChatGPT App. La prochaine étape sûre est une projection de schema MCP pure TypeScript.

### Fichiers à lire
- `docs/plans/2026-06-11-mcp-readiness.md`
- `my-app/src/modules/local-mcp/schema.ts`
- `my-app/src/modules/internal-tool-contracts/schema.ts`
- `my-app/src/modules/internal-tool-contracts/contracts.ts`

### Fichiers à modifier
- Nouveau module/schema pure TS ou tests, selon spec PR18.
- Aucune config transport.

### Étapes exactes pour un junior
1. Mapper chaque local tool vers un schema input/output explicite.
2. Ajouter tests unknown tool, private/never_use filtering placeholders, output size limit metadata.
3. Ne pas appeler un handler réel.
4. Ne pas importer `fetch`, Convex, UI, routes, OAuth.

### Risques
- Glisser vers Remote MCP trop tôt.

### Cas limites
- Tool inconnu.
- Argument trop gros.
- Output privé.
- Fact `never_use`.

### Vérifications
```bash
cd my-app
rtk npx vitest --run src/modules/local-mcp/__tests__/*.test.ts
rtk npx vitest --run src/modules/internal-tool-contracts/__tests__/*.test.ts
```

### Hors scope explicite
- Remote MCP.
- ChatGPT App.
- OAuth.
- Deployment.
- Real handlers.

## Amélioration 6 — Ajouter un test timeout Controlled ATS

### Priorité
P3

### Pourquoi
Le fetcher passe un `AbortSignal` et installe un timeout. Les tests vérifient le signal/clearTimeout, mais un scénario abort explicite serait utile avant toute intégration réseau réelle.

### Fichiers à lire
- `my-app/src/modules/controlled-ats-scout/publicEndpointFetcher.ts`
- `my-app/src/modules/controlled-ats-scout/__tests__/controlledAtsPublicEndpoints.test.ts`

### Fichiers à modifier
- `my-app/src/modules/controlled-ats-scout/__tests__/controlledAtsPublicEndpoints.test.ts`

### Étapes exactes pour un junior
1. Créer un `fetchImpl` qui ne résout pas avant abort.
2. Vérifier que l'appel échoue proprement.
3. Ne pas changer les endpoints supportés.

### Risques
- Rendre le test flaky si timers mal contrôlés.

### Cas limites
- Abort avant response.
- Abort pendant `text()`.

### Vérifications
```bash
cd my-app
rtk npx vitest --run src/modules/controlled-ats-scout/__tests__/controlledAtsPublicEndpoints.test.ts
```

### Hors scope explicite
- Ajouter un crawler.
- Ajouter LinkedIn/Upwork/Indeed.
- Brancher un job background.

# Plan d'action recommandé

1. Corrections P0/P1 si présentes:
   - Aucun P0 confirmé.
   - Aucun P1 confirmé dans le code inspecté.
   - Ne pas créer de P1 en ajoutant export, tracking, send, submit, apply, remote MCP, UI publique ou crawler.

2. Corrections documentation:
   - Clarifier la roadmap réelle PR1-PR17.
   - Expliquer la numérotation PR14 confuse.
   - Ajouter le mapping noms plan ↔ noms code.
   - Ajouter une gate docs claire: `ready_for_review` n'est pas `approved`.

3. Renforcement tests:
   - EvidenceGraph edge cases.
   - CandidateEvidence lifecycle Convex.
   - Controlled ATS timeout.
   - Local MCP future output/privacy placeholders.

4. Prochaine PR minimale recommandée:
   - PR docs/test-only: roadmap reconciliation + tests EvidenceGraph ciblés.
   - Ensuite seulement: PR18 MCP schema projection pure TypeScript.

5. Ce qu'il faut explicitement ne pas faire:
   - Pas de remote MCP.
   - Pas de ChatGPT App.
   - Pas d'OAuth.
   - Pas de UI/routes/pages.
   - Pas de export PDF/DOCX/download.
   - Pas de send/submit/apply/auto-apply.
   - Pas de scraping LinkedIn/Upwork/Indeed.
   - Pas de refactor global.
   - Pas de mutation CV canonical.
   - Pas de mutation sémantique des CandidateFacts.

# Commandes de vérification recommandées

```bash
rtk git diff --name-only
rtk git diff --check
rtk git status --short --branch
```

```bash
cd my-app
rtk npx vitest --run src/modules/application-harness/__tests__/*.test.ts
rtk npx vitest --run src/modules/candidate-evidence/__tests__/*.test.ts
rtk npx vitest --run src/modules/career-knowledge/__tests__/*.test.ts
rtk npx vitest --run src/modules/evidence-graph/__tests__/*.test.ts
rtk npx vitest --run src/modules/resume-variant-plan/__tests__/*.test.ts
rtk npx vitest --run src/modules/resume-variant-artifact/__tests__/*.test.ts
rtk npx vitest --run src/modules/review-cockpit/__tests__/*.test.ts
rtk npx vitest --run src/modules/cover-letter-artifact/__tests__/*.test.ts
rtk npx vitest --run src/modules/application-package/__tests__/*.test.ts
rtk npx vitest --run src/modules/internal-tool-contracts/__tests__/*.test.ts
rtk npx vitest --run src/modules/controlled-ats-scout/__tests__/*.test.ts
rtk npx vitest --run src/modules/local-mcp/__tests__/*.test.ts
rtk npx vitest --run convex/__tests__/applicationHarness.test.ts
rtk npx vitest --run convex/lib/tests/applicationContextBuilder.test.ts
rtk npx vitest --run convex/__tests__/candidateEvidence.test.ts
rtk npx vitest --run convex/__tests__/applicationPackages.test.ts
rtk npx tsc --noEmit
```

# Résumé pour développeur junior

Tu dois lire d'abord:
1. `docs/decisions/2026-06-08-application-os-master-plan.md`
2. `AGENTS.md`
3. `docs/plans/2026-06-11-mcp-readiness.md`
4. `my-app/src/modules/application-harness/fingerprints.ts`
5. `my-app/src/modules/candidate-evidence/sourcePaths.ts`
6. `my-app/src/modules/evidence-graph/buildEvidenceGraph.ts`
7. `my-app/src/modules/local-mcp/localMcpAdapter.ts`

Tu peux modifier:
- Docs d'audit/roadmap.
- Tests ciblés dans un module précis.
- Un petit bugfix source seulement si un test échoue et que le scope est clair.

Tu ne dois pas toucher:
- CV canonical.
- CandidateFact `value` sémantique.
- `my-app/convex/schema.ts` sans demande explicite.
- UI/routes/pages.
- package deps/lockfiles.
- export/download/PDF/DOCX.
- send/submit/apply/auto-apply.
- Remote MCP / ChatGPT App / OAuth.
- LinkedIn/Upwork/Indeed scraping.

Le prochain travail sûr est:
- Clarifier la roadmap réelle et renforcer les tests EvidenceGraph/CandidateEvidence sans changer l'architecture.

Les pièges principaux sont:
- Confondre `ready_for_review` avec `approved`.
- Transformer du texte généré en CandidateFact.
- Laisser un fact `private` ou `never_use` devenir public.
- Brancher Local MCP sur de vrais handlers trop tôt.
- Ajouter du réseau/crawler hors Controlled ATS public endpoints.
- Renommer/refactorer les modules pour les faire coller au plan au lieu de documenter le mapping.
