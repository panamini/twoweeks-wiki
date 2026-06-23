---
aliases:
  - Roadmap Twoweeks ChatGPT/App SDK — PR41 à PR89
---

Roadmap Twoweeks ChatGPT/App SDK — PR41 à PR89# 

## Règle globale pour tous les PR

Chaque PR doit rester :

```txt
petit, inspectable, réversible, testé, boring by default, aligné produit.
```

But produit permanent :

```txt
safe, reviewable, user-approved job application workflows
```

Les agents doivent avancer dans l’ordre. Ils ne doivent pas inventer de PR hors roadmap. Ils ne doivent pas passer au PR suivant tant que le PR courant n’est pas vérifié, vert, relu, et aligné avec PR18–PR40.

Chaque PR doit produire un rapport avec :

```txt
- PR number and title
- base branch
- head branch
- commit SHA
- files changed
- why each file is in scope
- tests run
- typecheck run
- lint/audit run
- CI status
- failures found
- debugging performed
- unresolved uncertainties
- PR18–PR40 gates verified
- forbidden surfaces untouched
- product-purpose alignment check
- rollback plan
- exact next PR recommendation
```

Si CI est rouge ou inconnu, si les tests/typecheck/audit échouent, si le scope dérape, ou si un fichier interdit est touché, l’agent doit **arrêter** et produire un fix-forward prompt.

---

# Phase 1 — Agent contract et déverrouillage contrôlé

## PR41 — Agent Implementation Roadmap and Verify-Debug-Control Contract

**Type :** docs-only.

**But :** créer le contrat agent complet qui explique comment avancer de PR42 à PR89 sans te redemander la suite.

**Fichier attendu :**

```txt
docs/plans/2026-06-12-chatgpt-app-implementation-roadmap-agent-contract.md
```

**Contenu obligatoire :**

```txt
- roadmap complète PR41–PR89
- verify-debug-control loop obligatoire après chaque PR
- règle anti-monster
- règle de continuation
- règle de scope par PR
- rapport final obligatoire
- PR18–PR40 comme contraintes de référence
- interdiction de continuer si CI/test/audit/scope est incertain
```

**Interdit :**

```txt
- code
- package.json
- lockfile
- /mcp
- tools/list
- tools/call
- OAuth
- UI
- handlers
- real data
- outbound HTTP
- LLM calls
- export/send/apply
```

**Vérification attendue :**

```bash
rtk git diff --check
rtk git diff --name-only application-os-foundation...HEAD
rtk npx fallow audit --changed-since application-os-foundation --format compact
```

**Résultat :** les agents ont une carte complète et une boucle de contrôle stricte.

---

# Phase 2 — Dépendances, sans runtime

## PR42 — Package-Only Install for Approved MCP/App SDK Dependencies

**Type :** package-only.

**Précondition :** PR41 merged + approbation explicite des packages exacts.

**But :** installer uniquement les dépendances minimales nécessaires au travail MCP/App SDK non-production.

**Fichiers autorisés :**

```txt
package.json
lockfile
```

**Packages candidats uniquement si confirmés par docs officielles le jour du PR :**

```txt
@modelcontextprotocol/sdk
@modelcontextprotocol/ext-apps, seulement si encore requis
zod, seulement si requis par le SDK path
```

**À différer sauf décision explicite :**

```txt
openai
```

Raison : pas de LLM/model call avant budget/token policy.

**Interdit :**

```txt
- app code
- imports SDK dans le code
- /mcp
- server skeleton
- tools/list
- tools/call
- OAuth
- UI
- handlers
- outbound HTTP
- LLM calls
```

**Tests/vérifs :**

```bash
rtk git diff --check
rtk git diff --name-only application-os-foundation...HEAD
rtk npx fallow audit --changed-since application-os-foundation --format compact
```

**Résultat :** packages installés, rien ne s’exécute.

---

## PR43 — Dependency Import Boundary and No-Runtime Guard Tests

**Type :** code/tests.

**But :** prouver que les dépendances installées ne créent aucun runtime implicite.

**Fichiers probables :**

```txt
my-app/src/modules/chatgpt-app-mcp/
my-app/src/modules/chatgpt-app-mcp/__tests__/
```

**À créer :**

```txt
- petit module boundary
- tests source-level contre runtime creep
```

**Tests doivent rejeter :**

```txt
/mcp
tools/list runtime
tools/call runtime
server listener
OAuth
OpenAI/model call
outbound HTTP
real handler
real data
export/send/apply
```

**Résultat :** dépendances présentes, mais aucune surface runtime.

---

# Phase 3 — Descriptors avant serveur

## PR44 — PR38 Descriptor Adapter Tests

**Type :** code/tests.

**But :** transformer la mapping PR38 en tests et fixtures de descriptors, sans runtime.

**Tools concernées :**

```txt
twoweeks.application_package.summarize
twoweeks.evidence_graph.summarize
twoweeks.resume_variant_plan.summarize
twoweeks.review_cockpit.summarize
```

**À vérifier :**

```txt
- names
- descriptions
- closed input schemas
- safe-summary-only output policy
- annotations readOnlyHint/destructiveHint/openWorldHint
- _meta policy
- forbidden names/actions
```

**Interdit :**

```txt
- tools/list runtime
- tools/call runtime
- handler execution
- network
```

**Résultat :** les descriptors futurs sont testés contre PR38.

---

## PR45 — Static Descriptor Registry, Fixture-Only

**Type :** code/tests.

**But :** créer un registre statique interne des descriptors validés.

**Autorisé :**

```txt
- descriptor constants
- schema objects
- policy metadata
- fixture-only registry
```

**Interdit :**

```txt
- endpoint
- listener
- tools/list exposé
- tools/call
- handlers
```

**Résultat :** l’app possède un registre statique sûr, non exposé.

---

# Phase 4 — Skeleton local désactivé

## PR46 — Local MCP Server Skeleton, Disabled by Default

**Type :** code/tests.

**But :** créer le premier skeleton serveur local, mais impossible à joindre.

**Règles :**

```txt
- disabled by default
- no route
- no listener
- no transport
- no public tunnel
- no ChatGPT connection
- no real handlers
- no real data
```

**Fichiers probables :**

```txt
my-app/src/modules/chatgpt-app-mcp/serverSkeleton.ts
my-app/src/modules/chatgpt-app-mcp/__tests__/serverSkeleton.test.ts
```

**Résultat :** skeleton existant mais non reachable.

---

## PR47 — Internal Simulated `tools/list`, Fixture-Only

**Type :** code/tests.

**But :** créer une fonction interne simulée qui retourne les descriptors.

**Important :** ce n’est pas un endpoint.

**Autorisé :**

```txt
listToolsFixtureOnly()
descriptor registry
fixture-only tests
```

**Interdit :**

```txt
/mcp
network
runtime transport
real ChatGPT connector
real data
```

**Résultat :** on peut tester `tools/list` localement sans serveur réel.

---

## PR48 — Internal Simulated `tools/call`, No-Op Fixture-Only

**Type :** code/tests.

**But :** créer une fonction interne simulée qui refuse ou retourne un safe summary fixture.

**Autorisé :**

```txt
callToolFixtureOnly()
input validation
unknown tool rejection
blocked output
safe-summary fixture output
```

**Interdit :**

```txt
real handlers
Convex
real data
export/download/send/submit/apply
outbound HTTP
LLM call
```

**Résultat :** `tools/call` existe seulement en simulation no-op.

---

## PR49 — Golden Safety Tests for Simulated MCP Behavior

**Type :** tests.

**But :** figer les garanties de PR44–PR48.

**Tests obligatoires :**

```txt
- descriptors match PR38
- outputs safe-summary-only
- no raw CV/job/private facts
- no never_use
- no write actions
- no real handler path
- no network
- no OAuth
- no ChatGPT connector
- negative prompt refusal
```

**Résultat :** les comportements simulés sont verrouillés.

---

# Phase 5 — Transport local dev et première démo fake

## PR50 — Local Dev Transport Adapter, Disabled by Default

**Type :** code/tests.

**But :** ajouter un adaptateur de transport local/dev, sans exposition publique.

**Autorisé :**

```txt
local-only adapter
disabled by default
test harness
```

**Interdit :**

```txt
public endpoint
public tunnel
real user data
real handlers
OAuth
production behavior
```

**Résultat :** le skeleton peut être exercé localement en tests.

---

## PR51 — Dev-Only `/mcp` Endpoint Behind Explicit Flag

**Type :** code/tests.

**But :** créer le premier endpoint `/mcp`, uniquement derrière flag explicite local.

**Protections obligatoires :**

```txt
disabled by default
fails closed without env flag
fake data only
request size limits
method allowlist
malformed payload tests
no production deploy
```

**Interdit :**

```txt
real data
Convex
OAuth
public tunnel
real handler
write action
```

**Résultat :** `/mcp` existe seulement en local/dev explicite.

---

## PR52 — Local Developer Mode Fake-Data Demo

**Type :** code/docs/tests.

**But :** connecter localement ChatGPT Developer Mode au endpoint fake.

**Flow attendu :**

```txt
ChatGPT Developer Mode
→ local /mcp
→ simulated tools/list
→ simulated tools/call
→ safe fixture output
```

**Résultat :** première démo réelle visible, sans vraie donnée.

---

# Phase 6 — Auth, consent, audit, privacy foundation

## PR53 — Auth/OAuth Implementation Decision

**Type :** decision doc, possiblement code minimal si auth existante claire.

**But :** décider comment une session ChatGPT mappe vers un user Twoweeks.

**Questions :**

```txt
OAuth ou auth existante ?
account linking ?
token storage ?
revocation ?
session binding ?
local dev vs prod ?
```

**Résultat :** une seule stratégie auth approuvée.

---

## PR54 — Auth/OAuth Skeleton, No Real Tools Yet

**Type :** code/tests.

**But :** implémenter la frontière auth/session.

**Autorisé :**

```txt
auth skeleton
session binding
token redaction
revocation placeholder
```

**Interdit :**

```txt
real data access
real tool execution
write actions
```

**Résultat :** le flow est authentifiable mais ne lit rien.

---

## PR55 — Consent Gate Implementation

**Type :** code/tests.

**But :** aucun accès data sans consentement utilisateur explicite.

**À implémenter :**

```txt
consent state
deny/revoke
stale consent rejection
safe copy
tests
```

**Résultat :** no consent, no data.

---

## PR56 — Redacted Audit Log Implementation

**Type :** code/tests.

**But :** tout call futur produit un audit safe.

**Interdit dans logs :**

```txt
raw CV
raw job text
private facts
never_use
tokens
full generated artifacts
raw args
```

**Résultat :** audit utile sans fuite.

---

## PR57 — Retention and Deletion Implementation

**Type :** code/tests.

**But :** gérer suppression/revocation des traces.

**Couvre :**

```txt
audit records
cached results
connector sessions
generated artifacts
logs
```

**Résultat :** les données peuvent être nettoyées.

---

## PR58 — Semantic Privacy Test Harness

**Type :** tests.

**But :** dépasser les simples sentinelles.

**Doit détecter :**

```txt
private fact paraphrase
never_use reintroduction
raw quote leakage
generated artifact leakage
hidden data in _meta
raw args in logs
```

**Résultat :** privacy prête avant vraie donnée.

---

# Phase 7 — Read-only real data

## PR59 — Read-Only Twoweeks Data Adapter

**Type :** code/tests.

**But :** exposer des refs internes sûres vers vraies données Twoweeks.

**Autorisé :**

```txt
bounded read-only selectors
safe refs
no writes
no raw output
```

**Résultat :** base read-only réelle.

---

## PR60 — Real Application Package Summary

**Type :** code/tests.

**Tool :**

```txt
twoweeks.application_package.summarize
```

**But :** résumé safe d’un package application réel.

**Résultat :** vraie utilité read-only.

---

## PR61 — Real Evidence Graph Summary

**Type :** code/tests.

**Tool :**

```txt
twoweeks.evidence_graph.summarize
```

**But :** résumé safe de la qualité/provenance evidence.

---

## PR62 — Real Resume Variant Plan Summary

**Type :** code/tests.

**Tool :**

```txt
twoweeks.resume_variant_plan.summarize
```

**But :** résumé safe d’un plan CV, sans full resume text.

---

## PR63 — Real Review Cockpit Summary

**Type :** code/tests.

**Tool :**

```txt
twoweeks.review_cockpit.summarize
```

**But :** résumé safe des gates, blockers, next actions.

---

## PR64 — Real Read-Only ChatGPT E2E

**Type :** tests/demo.

**Flow :**

```txt
ChatGPT
→ MCP
→ auth
→ consent
→ read-only adapter
→ safe summary
→ redacted audit
```

**Résultat :** première intégration ChatGPT utile sur vraies données, read-only.

---

# Phase 8 — UI/component ChatGPT

## PR65 — ChatGPT Component/UI Data Policy

**Type :** code/tests/doc.

**But :** classifier ce qui peut aller au composant UI.

**Règle :**

```txt
_meta is not a privacy boundary.
```

**Résultat :** policy UI claire.

---

## PR66 — Read-Only Review Component

**Type :** code/tests.

**But :** montrer un cockpit review safe dans ChatGPT.

**Autorisé :**

```txt
safe summaries
gate states
ref IDs
next actions
```

**Interdit :**

```txt
raw CV
raw job text
full artifacts
tokens
write actions
```

---

## PR67 — Component Error, Loading, and Refusal UX

**Type :** code/tests.

**But :** UX professionnelle pour erreurs/blocages.

**Cas :**

```txt
missing consent
expired auth
privacy blocked
budget exceeded
unsafe action refused
unavailable data
```

---

# Phase 9 — Génération d’artefacts, preview only

## PR68 — Generated Artifact Boundary

**Type :** code/tests.

**But :** séparer safe summary et full generated artifact.

**Artifacts :**

```txt
resume variant
cover letter
application package
review notes
```

**Résultat :** règles de stockage/visibilité/retention.

---

## PR69 — Resume Variant Generation Preview

**Type :** code/tests.

**But :** générer brouillons CV.

**Autorisé :**

```txt
preview only
human review required
```

**Interdit :**

```txt
export
send
apply
submit
```

---

## PR70 — Cover Letter / Application Message Preview

**Type :** code/tests.

**But :** générer lettre/message de candidature en preview.

**Interdit :**

```txt
send
submit
apply
```

---

## PR71 — Human Approval Workflow for Generated Artifacts

**Type :** code/tests.

**But :** validation explicite utilisateur avant sortie.

**Inclut :**

```txt
approval state
diff/review
reject/edit path
audit event
```

---

## PR72 — Artifact Revision Loop

**Type :** code/tests.

**But :** itérations contrôlées.

**Exemples :**

```txt
shorter
more formal
focus on X
preserve never_use
audit revisions
```

---

# Phase 10 — Export/download

## PR73 — Export/Download Policy Implementation

**Type :** code/tests.

**But :** autoriser export/download uniquement après action explicite.

**Inclut :**

```txt
preview
confirmation
audit
file naming
retention
delete/rollback
```

---

## PR74 — Resume Export

**Type :** code/tests.

**But :** exporter un CV approuvé.

**Résultat :** download resume file.

---

## PR75 — Cover Letter / Application Package Export

**Type :** code/tests.

**But :** exporter lettre/package approuvé.

**Résultat :** matériel pro téléchargeable.

---

# Phase 11 — Write actions

## PR76 — Write Action Framework

**Type :** code/tests.

**But :** base commune pour actions dangereuses.

**Obligatoire :**

```txt
explicit confirmation
final preview
idempotency key
audit event
rollback/recovery
no hidden model execution
no stale approval
no never_use leakage
```

---

## PR77 — Outbound Egress Allowlist and SSRF Protection

**Type :** code/tests.

**But :** permettre egress de façon sûre.

**Inclut :**

```txt
deny-by-default egress
allowed host list
no arbitrary URL fetch
no private IP
redirect limits
timeouts
response size limits
redacted logs
SSRF tests
```

---

## PR78 — Send Application Email/Message, Manual Confirmation Only

**Type :** code/tests.

**But :** envoyer un message approuvé via un canal contrôlé.

**Résultat :** première vraie action outbound.

---

## PR79 — Job Platform Submit/Apply Dry Run

**Type :** code/tests.

**But :** simuler submit/apply sans soumettre.

**Résultat :** mapping validé sans risque live.

---

## PR80 — Live Submit/Apply for One Integration

**Type :** code/tests.

**But :** activer apply/send live pour une intégration, derrière flags stricts.

**Obligatoire :**

```txt
manual confirmation
final preview
audit
idempotency
rollback/recovery
no model-only approval
no bulk apply
```

---

# Phase 12 — Production/business readiness

## PR81 — Rate Limits, Budget Limits, and Abuse Protection

**Type :** code/tests.

**But :** protéger coût et disponibilité.

**Inclut :**

```txt
per-user limits
per-session limits
per-tool limits
model token limits
concurrency
retry limits
budget exhaustion UX
```

---

## PR82 — Secrets, Token Storage, and Revocation Hardening

**Type :** code/tests.

**But :** sécurité credentials.

**Inclut :**

```txt
encrypted storage
token rotation
disconnect/revoke
no token logs
no token output
```

---

## PR83 — Observability and Incident Response

**Type :** code/tests/docs.

**But :** opérer sérieusement.

**Inclut :**

```txt
redacted metrics
error categories
audit dashboards
incident runbook
kill switch
```

---

## PR84 — Workspace / Business Tenant Boundaries

**Type :** code/tests.

**But :** rendre le produit safe pour entreprises.

**Inclut :**

```txt
workspace boundaries
roles
admin/member permissions
cross-tenant tests
audit per workspace
```

---

## PR85 — Billing / Plan Limits / Entitlements

**Type :** code/tests.

**But :** modèle business.

**Inclut :**

```txt
plan limits
feature flags
tool access per plan
usage caps
```

---

## PR86 — Security Review and Pre-Launch Audit

**Type :** audit/tests.

**But :** audit final avant prod.

**Doit vérifier :**

```txt
no raw data leakage
no unsafe writes
auth works
consent works
audit works
retention works
rate limits work
SSRF protections work
dependency risks reviewed
rollback works
```

---

## PR87 — Production Deployment Gate

**Type :** config/code/docs.

**But :** autoriser prod uniquement après PR86.

**Inclut :**

```txt
production env config
feature flags
kill switch
monitoring
rollback plan
```

---

## PR88 — Private Beta Launch

**Type :** launch/config.

**But :** activer pour utilisateurs/business limités.

**Inclut :**

```txt
allowlist
support path
feedback capture
incident monitoring
```

---

## PR89 — Public Business Launch

**Type :** launch.

**But :** disponibilité générale.

**Résultat :**

```txt
Twoweeks ChatGPT/App SDK integration ready for business customers.
```

---

# Ordre court à viser

La roadmap complète va jusqu’à PR89, mais le premier objectif concret est :

```txt
PR41–PR52 = working local non-production ChatGPT demo
```

Puis :

```txt
PR53–PR64 = useful real read-only ChatGPT integration
PR65–PR75 = professional artifact generation and export
PR76–PR80 = real send/apply actions
PR81–PR89 = production/business launch
```

# Prompt agent complet à coller dans PR41

```txt
You are a senior LLM agent acting on the Twoweeks repository.

Your job is to execute the post-PR40 roadmap from PR41 to PR89, one PR at a time, without inventing extra PRs and without drifting from the product goal.

Product goal:
safe, reviewable, user-approved job application workflows.

Start from the lowest-numbered unmerged PR in the roadmap.

For every PR:
1. Read PR18–PR40 controlling docs.
2. Inspect current repo state.
3. Confirm the PR scope.
4. Decompose the work into atomic sub-tasks.
5. Implement only that PR.
6. Run the narrowest relevant tests.
7. Run related regression tests.
8. Run typecheck if feasible.
9. Run lint/audit/fallow expected by the repo.
10. Inspect CI if available.
11. Debug failures before continuing.
12. Produce the required verification report.
13. Continue only if the PR is merged or explicitly approved to build on.

Never continue to the next PR if:
- tests fail;
- typecheck fails;
- lint/audit fails in a relevant way;
- CI is red or unknown without maintainer override;
- changed files exceed scope;
- forbidden PR40 surfaces were touched;
- runtime changed unexpectedly;
- implementation drifts from PR18–PR40;
- debugging is incomplete;
- the final report cannot explain exactly what was verified.

Forbidden unless the specific PR explicitly approves it:
- dependency install;
- package.json or lockfile changes;
- server skeleton;
- /mcp endpoint;
- tools/list runtime;
- tools/call runtime;
- OAuth;
- UI/components;
- real handlers;
- real user data;
- outbound HTTP;
- LLM/model calls;
- export/download/send/submit/apply;
- production behavior.

Anti-monster rule:
Each PR must be small, inspectable, reversible, tested, and tied to one roadmap goal.
Do not create a large hidden framework.
Do not create generic platform layers.
Do not future-proof beyond the PR.

Required final report after every PR:
- PR number and title
- base branch and head branch
- commit SHA
- files changed
- why each file was in scope
- tests run
- typecheck run
- lint/audit run
- CI status
- failures found
- debugging performed
- unresolved uncertainties
- PR18–PR40 gates verified
- forbidden surfaces confirmed untouched
- product-purpose alignment check
- rollback plan
- exact next PR recommendation
```