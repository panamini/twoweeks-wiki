---
title: "Proposal Signature & Closing Layer"
category: tech
status: current
created: 2026-05-08
updated: 2026-05-08
version: v1
related: [[tech/proposal-style-layer]], [[tech/export-pipeline]], [[tech/proposal-forge-document-geometry]], [[design/brand-voice]]
---

# Proposal Signature & Closing Layer

Cette couche règle la signature de proposition comme une donnée structurée, pas comme un parsing de texte généré.

## État actuel

Le pipeline structuré est activé en production pour les nouveaux drafts et pour les chargements où le metadata `closing` existe.
Le comportement attendu est:

- le mode **Edit** manipule uniquement le corps de proposition;
- le bloc de clôture/nom/signature reste séparé en métadonnées;
- la signature image (dessin manuscrit) et l’image manuscrite n’apparaissent que dans le rendu (preview/print/export), jamais dans le champ éditable.

## Règle d’or (actuelle)

Le LLM doit générer **le corps uniquement** (sans salutation, sans closing final, sans signature).
L’affichage du closing + signature est la responsabilité de l’application via une donnée
`closing` structurée, puis est propagée en preview/print/export.

## Source de vérité (résolution)

- `proposalClosing` (métadonnée document) : priorité 1.
- Fallback legacy : extraction depuis le texte existant (`Sincerely, Name`, etc.).
- Fallback défaut : sign-off localisé (`ENGLISH_SIGNOFFS` / `FRENCH_SIGNOFFS`) + nom candidat/applicant.

Le backend n’a pas de path Python dédié pour ce sujet; tout passe aujourd’hui par TypeScript/Convex + renderer React.

## Autorité effective

1. Donnée de proposition (`metadata.closing`) si présente.
2. Donnée persistée dans le draft d’affichage.
3. Signature/settings applicables comme source de fallback.

`source` est un label de provenance:
- `settings` : fermé au paramètre global Settings.
- `document` : override local de la proposition.
- `legacy` : extrait d’un vieux contenu parsé.

## Ce qui a été implémenté (déjà en cours de travail)

- `ProposalClosingRef` + resolver/sanitizer dans
  `my-app/src/lib/proposal-closing.ts`.
- Nouveau schéma Convex de `closing` dans
  `my-app/convex/schema.ts`, `createProposalPublic.ts`,
  `updateProposalPublic.ts`, `proposalsPublic.ts`.
- Passage du `closing` dans les sources de preview/print/export :
  `my-app/src/lib/document-export-models.ts`.
- `ProposalDocumentRenderer` + `ProposalPrintPage` :
  utilisation de `resolveProposalClosingRef` + rendu deterministe de la section closing.
- Propagation du closing dans les flux ProposalForge/Preview/Saved view :
  `my-app/src/pages/ProposalForge.tsx`,
  `my-app/src/components/ProposalDisplay.tsx`,
  `my-app/src/components/ProposalsList.tsx`.
- Draft metadata + metadata persistée :
  `my-app/src/lib/proposal-output-draft.ts`.

## Plan de continuation (depuis `plans/proposal-structured-closing.md`)

Le plan de base est valide, avec ordre de sécurité :

- finaliser la persistance uniforme du closing dans tous les chemins de save/autosave,
- empêcher les doublons de closing entre texte legacy + closing structuré,
- ajouter/valider les tests autour des 3 surfaces (preview, saved, print/export),
- activer ensuite les contrôles UI avancés (toggle, sign-off/signe, reset/local override) si nécessaire.

## Problème actif remonté (2026-05-08)

- Cas observé: certaines anciennes propositions contiennent des artefacts legacy dans le corps (par ex. `Warm regards,` puis le nom).
- Symptômes: après activation signature/manuelle puis passage en Edit, la vue revient en Preview.
- Hypothèse: le state de draft persisté peut encore être contaminé par de l’ancien texte de closing lors du chargement/synchronisation de ces artefacts.
- Bonne pratique validée: traiter la signature manuscrite comme une couche de rendu uniquement, interdire son insertion dans le contenu éditable.

Actions recommandées:

1. Ajouter une migration de normalisation « legacy closing cleanup » au load des anciens drafts non migrés.
2. Interdire explicitement le bloc “signature/name” dans le mode Edit (filtre de rendu + sanitization du draft chargé).
3. Ajouter un test e2e ciblé sur proposition legacy: toggle signature en preview puis entrée en edit doit rester en edit.

## Checks en cours de garde

- Vérifier la cohérence `saved → preview → print → export`.
- Vérifier qu’un changement de Settings met à jour le comportement par défaut tant qu’il n’y a pas d’override local.
- Vérifier qu’aucune source de validation ne rejette `closing` au passage Convex (validator/schema).

## Sources

- `plans/proposal-structured-closing.md` (plan d’implémentation)
- `my-app/src/lib/proposal-closing.ts`
- `my-app/src/components/proposal-render/ProposalDocumentRenderer.tsx`
- `my-app/src/lib/document-export-models.ts`
- `my-app/src/pages/ProposalForge.tsx`
- `my-app/src/components/ProposalDisplay.tsx`
- `my-app/src/components/ProposalsList.tsx`
- `my-app/convex/schema.ts`
- `my-app/convex/createProposalPublic.ts`
- `my-app/convex/updateProposalPublic.ts`
- `my-app/convex/proposalsPublic.ts`

## Liens connexes

- [[tech/proposal-style-layer]]
- [[tech/proposal-forge-document-geometry]]
- [[design/brand-voice]]
