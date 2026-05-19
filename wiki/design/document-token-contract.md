---
title: "Document Token Contract"
category: design
tags: [tokens, geometry, flow, appearance, runtime, layout, export]
created: 2026-04-16
updated: 2026-05-20
status: current
valid_from: 2026-04-16
version: v1
sources: [2026-04-16-token-classes-for-the-layout, 2026-04-16-verbati-style-pipeline-scratchpad, 2026-04-16-proposal-style-persistence-quickmap-scratchpad, 2026-04-21-2026-elite-design-system-implementation-handoff, 2026-04-27-workshop-token-audit, 2026-04-27-typography-token-audit-table]
related: [[design/a4-layout-systems]], [[design/locale-typography-rules]], [[tech/export-pipeline]], [[tech/preview-to-print-pipeline]], [[tech/workshop-token-parity]]
---

# Document Token Contract

Contrat canonique des classes de tokens document pour aligner preview, export CSS et DOCX.

## Classes officielles

- `geometry`
- `flow`
- `appearance`
- `runtime`

## Règles d'ownership

- `geometry` porte la page, la live area et les dimensions structurelles
- `flow` porte les comportements typographiques/layout qui affectent la lecture et potentiellement la pagination
- `appearance` porte le décor et les choix visuels non structurels
- `runtime` porte les helpers locaux de fit, mesure et instrumentation preview

## Règles figées

- `appearance.decor` est non-structurel
- `style.ts` n'est pas une autorité de thème indépendante
- le choix primaire de police vient de `appearance.font.*`
- les littéraux fallback plateforme sont tolérés uniquement pour compatibilité sérialiseur
- les helpers `runtime` ne doivent pas fuiter dans les snapshots exportés
- `metadata.verbatiStyle` est l'autorité visuelle persistée pour proposal
- `templateId` décrit d'abord la structure et la géométrie, pas l'identité visuelle complète
- le renderer reçoit un snapshot d'apparence résolu; il ne doit pas reconstruire le style depuis des defaults de liste ou de shell
- `foundation.css` est la source de vérité des tokens chrome; les overrides document doivent être scopés à un conteneur document, jamais à un `:root` global hors fondation
- les variables preview/planner workshop qui influencent pagination doivent être partagées explicitement, pas dupliquées en littéraux invisibles

## Pourquoi ça compte

Sans ce contrat, preview, export HTML/CSS et DOCX dérivent facilement vers plusieurs systèmes concurrents. Avec lui, chaque classe sait ce qu'elle a le droit d'influencer.

## Contrat Topbar (chrome commune)

La topbar d'application partage un contrat unique `app-topbar` pour la forme visuelle des contrôles (taille, gap, padding, alignement global).  

Règles de gouvernance:

- `foundation.css` détient la vérité des tokens topbar (épaisseur, espacements, dimensions de contrôle) ; les CSS de page ne doivent pas réinventer leurs propres valeurs.
- La topbar ne change pas de colonne logique entre CV et Proposal ; seule l'étiquette interne du contenu peut varier.
- Les hauteurs minimales, largeurs de base et arrondis des contrôles sont des valeurs tokenisées, pas des literals locaux.
- Les contrôles sont alignés sur une seule unité tactile/interactive (`control-sm`) avec des gaps/paddings dédiés topbar (`app-topbar-*`) afin d'éviter les écarts visuels entre modules.
- En collapsed/mobile, la largeur visuelle doit se réduire par la mécanique topbar (wrapper + actions compactées), pas par des hacks de largeur par surface.
- La variation de largeur sémantique (identity/title/picker/new/share/search) doit rester dérivée de la géométrie topbar, pas des tailles de page document.

Quand on ajoute ou retouche un écran, la première question doit être: ce style existe déjà dans `foundation.css` / contrat topbar, ou on crée un nouveau token de chrome.

## Cas proposal

Pour les proposals, la séparation critique est :

- `geometry` : page, template, disposition, zones structurelles
- `appearance` : `verbatiStyle` résolu, familles de police, contraste, accents et décor
- `runtime` : état local de preview, fit, instrumentation et merge temporaire

Le saved-view ne doit pas écraser `appearance` avec un bundle par défaut simplement parce qu'un `templateId` a été retrouvé. Si `metadata.verbatiStyle` existe, c'est lui qui doit survivre à la sauvegarde, à la réouverture et au print payload.

## Voir aussi

- [[design/a4-layout-systems]]
- [[design/locale-typography-rules]]
- [[tech/export-pipeline]]
- [[tech/preview-to-print-pipeline]]
- [[tech/workshop-token-parity]]
