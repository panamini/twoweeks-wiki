---
title: "Carte des chemins de génération de lettres"
category: tech
status: current
created: 2026-10-06
updated: 2026-10-06
tags: [cover-letter, billing, mcp, convex, premium, terra]
related: ["[[product/billing-launch-readiness]]", "[[product/chatgpt-app-sdk-roadmap]]", "[[howto/production-operations]]", "[[concepts/cv-parsing-pipeline]]"]
---

# Carte des chemins de génération de lettres

Toutes les lettres de production passent par **un seul chemin** : facturation active, puis le générateur « premium » avec le rédacteur `gpt-5.6-terra`. « Premium » est un **nom historique** (il date du temps où il existait une voie standard) ; ce n'est pas une option, c'est LE chemin actuel. Tout le reste est du code ancien, présent mais refusé en production.

Références de code : dépôt `panamini/neyssan`, `origin/main` au commit `ffc385879` (2026-10-06). Chemins relatifs à `my-app/` sauf mention. **VÉRIFIÉ** = lu dans ce code ; **SUPPOSÉ** = non prouvé.

## Current state

### Schéma du flux

```
 Site web / extension                 ChatGPT (serveur MCP mcp.twoweeks.ai)
 api.functions.generateProposal       twoweeks.letter.prepare → l'utilisateur approuve → .generate
        │                                      │ (bridge signé, jamais de clé Convex lecture/écriture libre)
        │                                      ▼
        │                              convex/http.ts /mcp-oauth-storage → mcpBridgeLetters.ts
        │                                      → mcpLetters.ts (generate)
        ▼                                      ▼
   handleGenerateProposal  (generateProposalMutation.ts:13224)  ◄── même point d'entrée
        │  BILLING_LAUNCH_MODE = "enforced" ?
        ▼
   runLetterBillingWorkflow (lib/billingLetterWorkflow.ts:72)
        │ 1. réserve 1 lettre (beginOperation) → 2. verrou (claimWorkflow)
        │ 3. generateProposalCore → attemptPremiumCoverLetterGeneration (Terra)
        │      appels OpenAI via createLetterBillingFetch (2 appels max : rédaction + vérif. des faits)
        │ 4. storeProposal + débit : une seule transaction  │  échec → réservation relâchée
        ▼
   lettre enregistrée (proposalId) + contenu renvoyé
```

### Les entrées (VÉRIFIÉ)

| Entrée | Fichier:ligne | Remarque |
| --- | --- | --- |
| Site web (3 écrans : `ProposalForge`, `ProposalInputForm`, `ProposalsList`/`ProposalForgeNext`) | `src/pages/ProposalForge.tsx:3225`, `src/components/ProposalInputForm.tsx:426`, `src/pages/ProposalForgeNext.tsx:381`, `src/components/ProposalsList.tsx:649` → action `generateProposal` `convex/functions.ts:70-72` | `handler: handleGenerateProposal` |
| Extension Chrome | `clerk-chrome-extension-final/src/background/index.ts:516` (`api.functions.generateProposal`) | même action ; exige un `clientRunId` (`:497`) |
| ChatGPT / MCP | outils `twoweeks.letter.prepare`, `.generate`, `.get`, `twoweeks.job.add` : `src/modules/local-mcp/mcpLetterTools.ts:31-56` → bridge signé `convex/http.ts:70` (`/mcp-oauth-storage`, opérations `:179-184`) → `convex/lib/mcpBridgeLetters.ts:121` (`runMcpBridgeLetter`) → `convex/mcpLetters.ts:261` (`generate`) | l'action `generate` appelle `handleGenerateProposal(ctx, input, ownerId)` (`mcpLetters.ts:269`) ; le propriétaire vient du jeton vérifié, jamais des arguments |
| Export par défaut du module | `convex/generateProposalMutation.ts:13232-13234` | alias, passe aussi par `handleGenerateProposal` |

Aucune autre entrée de génération de lettre n'existe dans `convex/` ni `src/` (recherche des appels à `generateProposal` / `handleGenerateProposal`, VÉRIFIÉ).

### Le chemin actif en production

Valeurs lues sur Convex prod le 2026-10-06 via la CLI connectée (VÉRIFIÉ, pas des secrets) : `BILLING_LAUNCH_MODE=enforced`, `PREMIUM_COVER_LETTER_BOUNDED_REQUESTS=1`, `COVER_LETTER_PREMIUM_WRITER_MODEL=gpt-5.6-terra` ; `OPENAI_PROPOSAL_MODEL` et `COVER_LETTER_PREMIUM_PATH_V1` non définies.

1. `handleGenerateProposal` : si `BILLING_LAUNCH_MODE === "enforced"` → `runLetterBillingWorkflow` (`generateProposalMutation.ts:13225`). Sinon l'ancien chemin non facturé (voir Legacy). Un propriétaire venant du bridge MCP n'est **jamais** servi hors facturation (`:13227`, erreur `BILLING_LAUNCH_DISABLED`).
2. `runLetterBillingWorkflow` impose : modèle `chatgpt` seulement (`billingLetterWorkflow.ts:75-76`, `BILLING_LETTER_MODEL_UNSUPPORTED`), route « letter » qualifiée (`:77`), `PREMIUM_COVER_LETTER_BOUNDED_REQUESTS=1` (`:78-79`, `BILLING_BOUNDED_LETTER_REQUIRED`), un `clientRunId`, un `jobId` et `proposalType === "cover_letter"` (`:83-89`). Il force `modelType: "chatgpt"` (`:172`).
3. La route « letter » n'accepte **que** `gpt-5.6-terra` (`lib/qualifiedProviderRequest.ts:36-37`). Le modèle vient de `COVER_LETTER_PREMIUM_WRITER_MODEL`, puis `OPENAI_PROPOSAL_MODEL`, puis **`gpt-5.5` par défaut** (`:18`) : sans la variable, toute lettre facturée serait refusée. D'où l'importance de la variable en prod et dans `mcp.env`.
4. Dans `generateProposalCore`, la tentative « bornée » (`boundedCoverLetterAttempt`, `generateProposalMutation.ts:11473`) exige le rédacteur Terra, un CV/contexte exploitable et `OPENAI_API_KEY` ; sinon elle s'arrête avec « This cover-letter configuration requires the Terra writer and usable candidate evidence. » (`:11730-11738`). C'est **la garde « Terra writer… »** : en mode facturé aucune autre voie ne peut produire de lettre.
5. `attemptPremiumCoverLetterGeneration` (`lib/proposals/premiumCoverLetter.ts:7020`) fait au plus **deux** appels OpenAI : une composition puis une vérification des faits (`COVER_LETTER_COMPOSITION_JSON_SCHEMA` / `COVER_LETTER_SOURCE_VERDICT_JSON_SCHEMA`, `generateProposalMutation.ts:11855-11866` ; `reasoningEffort: "medium"` pour Terra `:11871-11873`). Un troisième appel est refusé. En cas d'échec il n'y a **pas de repli** vers un autre générateur : erreur « did not produce an approved draft » (`:11921`).

### Contrôle d'adéquation CV / offre

`evaluatePrimaryCoverLetterPathEligibility` (`generateProposalMutation.ts:3176`) appelle `evaluatePremiumCoverLetterEligibility` (`premiumCoverLetter.ts:2391`). Raisons de refus (type `:404-413`) :

| Raison | Quand | Où |
| --- | --- | --- |
| `preset_not_supported` | ton (preset) non géré | `premiumCoverLetter.ts:2398` |
| `unsupported_context_class` | `inferPremiumCoverLetterContextClass` (`:2429`) renvoie `null` : CV présent mais trop peu de mots en commun avec l'offre (il faut ≥ 2 mots communs, ou 1 mot du titre + 5 au total pour « cv_direct ») | `:2406`, `:2473-2481` |
| `no_allowed_facts` | aucune preuve exploitable après classement des faits | `:2418-2424` |

Sans CV mais avec une offre exploitable, la classe est `no_cv` (`:2431-2442`). Depuis la PR #640, l'utilisateur voit un refus explicite (`COVER_LETTER_CV_JOB_TOO_DISTANT`) ; les autres échecs gardent le message générique de la garde Terra (étape 4).

**Correctif livré (PR #640, fusionnée le 2026-10-06, commit `ca8f0a481`)** : VÉRIFIÉ dans `origin/main`.
- Les accents sont pliés avant le découpage en mots (`premiumCoverLetter.ts:1573`), donc « expérience » reste un mot ; un CV français n'est plus jugé « trop éloigné » à tort.
- Le contrôle voit tout le CV (plus de plafond à 16 faits).
- Nouveau code `COVER_LETTER_CV_JOB_TOO_DISTANT` (`convex/lib/proposals/coverLetterFit.ts:9`) : refus si `unsupported_context_class` ou `no_allowed_facts`. ChatGPT `letter.prepare` refuse **avant toute approbation**, sans réservation (`convex/mcpLetters.ts:159`) ; le rédacteur lance le même code (`generateProposalMutation.ts:11743`) ; le web affiche un message traduit (EN/FR/ES) au lieu de « réessayez ».
- Déploiement : la partie Convex part à la fusion ; le serveur MCP (message de l'outil et libellé de `prepare`) tourne avec l'image `ca8f0a481` depuis le 2026-10-06 à 08:40 UTC (VÉRIFIÉ sur la Lightsail : `MCP_IMAGE_TAG` = ce SHA, conteneur `healthy`, métadonnées 200, `/mcp` anonyme 401). Retour arrière : `c7b5c5e97`.

### Facturation : un débit par lettre (VÉRIFIÉ)

- **Une lettre = 1 unité**, réservée au début : `beginOperationForOwner` ajoute 1 à `reserved` sur la ligne d'allocation (`convex/billingEntitlementsV2.ts:451`), après contrôle du solde et du budget (`:403-425`).
- **Débit à la livraison** : le contenu et le débit sont écrits dans la même transaction Convex (`reserved − 1`, `consumed + 1`, `billingEntitlementsV2.ts:589-600`) ; `storeProposal` porte `billingOperationId` (`billingLetterWorkflow.ts:148-153`).
- **Remboursement en cas d'échec** : si la génération échoue avant livraison, `failOperation` relâche la réservation (`billingEntitlementsV2.ts:612-632`, appelé en `billingLetterWorkflow.ts:189`). Le client n'a jamais été débité ; il n'y a pas d'écriture de remboursement à part.
- **Idempotence** : clé = `clientRunId` (web, extension) ou `mcp-letter:<approvalId>` (MCP, `lib/mcpLetterApproval.ts:59`). Même clé et mêmes entrées → même opération, **jamais de second débit** (`billingEntitlementsV2.ts:356-394`) ; une lettre déjà livrée est rejouée telle quelle (`billingLetterWorkflow.ts:116-124`) ; une opération en cours renvoie `BILLING_LETTER_OPERATION_PENDING` (`:114`) ; mêmes clés mais entrées différentes → `OPERATION_INPUT_MISMATCH`. Après un échec définitif (`BILLING_LETTER_OPERATION_FINALIZED`, `:109`, `:115`, `:200`), il faut une nouvelle intention utilisateur (nouveau `clientRunId`). Côté MCP, `prepare` est lui aussi rejouable par `requestId` (`mcpLetters.ts:142-148`).
- Les appels OpenAI sont eux-mêmes comptés et plafonnés par `createLetterBillingFetch` (`billingLetterWorkflow.ts:22`) ; tout autre fournisseur est refusé (`BILLING_LETTER_FALLBACK_FORBIDDEN`, `:44`).

## Details

### Chemins legacy : présents dans le code, inactifs en production

| Chemin | Où | En prod ? | Preuve |
| --- | --- | --- | --- |
| Mistral (`mistral-small-latest` etc.) | branche `isPremiumMistralCoverLetterModel`, `generateProposalMutation.ts:11786`, `:12215` | **Non** | en mode facturé le modèle est forcé à `chatgpt` (`billingLetterWorkflow.ts:75`, `:172`) ; la prod est `enforced` (lu 2026-10-06) |
| Qwen (`qwen3.7-max`) | `generateProposalMutation.ts:11957`, `:12081` (requiert `QWEN_*`) | **Non** | idem ; `COVER_LETTER_PREMIUM_PATH_V1` non défini en prod |
| Non facturé | `handleGenerateProposal` quand `BILLING_LAUNCH_MODE !== "enforced"` (`:13226-13229`) | **Non** | prod = `enforced` ; le jour où la variable change, ce chemin se réveille. À ne pas toucher sans accord |
| Repli « legacy » après échec du premium | `console.warn("…falling back to legacy cover-letter generation")`, `:11900`, `:12042` | **Non** | `boundedCoverLetterAttempt` relance l'erreur au lieu de replier (`:11894-11896`, `:11921`) |
| `buildPremiumCoverLetterPrompt` (ancien prompt à « body parts ») | `premiumCoverLetter.ts:3304`, utilisé seulement dans les prompts de réparation `:6527`, `:6576` | **Non** pour la rédaction | le chemin Terra utilise `buildCoverLetterCompositionPrompt` (`:7155`) |

Ces branches existent encore parce que le mode non facturé et les modèles historiques restent testés ; ne pas les supprimer ni les « réparer » sans accord. SUPPOSÉ : aucune lettre de production ne les a empruntées depuis l'activation du 2026-09-24 (non vérifié dans les logs).

### Fichiers clés

| Fichier | Rôle |
| --- | --- |
| `convex/functions.ts` | déclare l'action publique `generateProposal` |
| `convex/generateProposalMutation.ts` | `handleGenerateProposal` (aiguillage), `generateProposalCore` (13 000 lignes, toute la logique) |
| `convex/lib/billingLetterWorkflow.ts` | réservation, verrou, appels OpenAI comptés, échec/relâche |
| `convex/lib/qualifiedProviderRequest.ts` | modèles et plafonds qualifiés (Terra seul pour « letter ») |
| `convex/lib/proposals/premiumCoverLetter.ts` | éligibilité, prompts, validation, générateur « premium » |
| `convex/lib/proposals/premiumCoverLetterOpenAITransport.ts` | `PREMIUM_COVER_LETTER_BOUNDED_REQUESTS`, limites d'octets/jetons |
| `convex/billingEntitlementsV2.ts` | allocations, réservation, débit, échec |
| `convex/mcpLetters.ts`, `convex/lib/mcpLetterApproval.ts`, `convex/lib/mcpBridgeLetters.ts` | approbation MCP, entrées figées, opérations autorisées du bridge |
| `src/modules/local-mcp/mcpLetterTools.ts` | outils vus par ChatGPT |
| `convex/http.ts` | `/mcp-oauth-storage` (bridge signé) |

### Variables d'environnement (noms seulement)

| Nom | Convex prod | `mcp.env` Lightsail | Rôle |
| --- | --- | --- | --- |
| `BILLING_LAUNCH_MODE` | oui (`enforced`) | oui | active la facturation ; sans elle, ancien chemin |
| `PREMIUM_COVER_LETTER_BOUNDED_REQUESTS` | oui (`1`) | oui | impose le chemin borné (2 appels) |
| `COVER_LETTER_PREMIUM_WRITER_MODEL` | oui (`gpt-5.6-terra`) | oui | choisit Terra ; défaut `gpt-5.5` = refusé |
| `OPENAI_API_KEY` | oui | oui | accès OpenAI (secret, Infisical `prod /twoweeks`) |
| `MCP_LETTER_GENERATION_ENABLED` | oui (`1`) | oui | ouvre les outils lettres (garde `convex/lib/mcpLetterApproval.ts:18`) |
| `MCP_LETTER_LOOP_TOOLS_ENABLED` | non définie | oui | ouvre `letter.get` / `job.add` côté serveur MCP |

Les noms de `mcp.env` ont été relus sur la Lightsail le 2026-10-06 (noms uniquement). Aucune valeur secrète n'est consignée ici. Voir [[howto/production-operations]] pour où et comment les lire ou les changer.

## Sources

Docs du dépôt (chemins depuis la racine) : `docs/decisions/2026-09-27-mcp-letter-workflow-contract.md`, `docs/decisions/2026-09-27-mcp-confirmed-letter-implementation.md`, `docs/decisions/2026-10-04-mcp-letter-loop-scope.md`, `docs/decisions/2026-09-08-v1-frozen-configuration.json` (contrat Terra), `docs/audits/2026-09-05-cover-letter-engine-architecture-review.md`, `docs/audits/2026-09-05-cover-letter-pipeline-quality.md`, `docs/audits/2026-06-02-proposal-premium-routing-audit.md` (historique : décrit l'avant-facturation, ne pas lire comme l'état actuel).

## Related

[[product/billing-launch-readiness]] · [[product/chatgpt-app-sdk-roadmap]] · [[howto/production-operations]] · [[howto/chatgpt-mcp-private-beta-tunnel-connector]] · [[tasks/2026-06-22-cover-letter-quality-production-roadmap]]
