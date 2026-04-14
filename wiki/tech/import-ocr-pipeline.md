---
title: "Import OCR Pipeline — Call Path"
category: tech
tags: [import, ocr, pipeline, convex, parser, canonicalize, architecture, sections]
created: 2026-04-12
updated: 2026-04-14
status: current
valid_from: 2026-04-12
valid_until:
superseded_by:
horizon: present
version: v1
sources: [pipeline-note-2026-04-12, 2026-04-14-structured-parsing-canonical-truth, 2026-04-14-local-dev-vs-remote-parser-architecture, 2026-04-14-run-sh-modes, 2026-04-14-run-sh-quick-note]
related: [[concepts/cv-parsing-pipeline]], [[concepts/parsing-poc-progress]], [[entities/twoweeks]], [[tech/local-vs-remote-parser-architecture]]
---

# Import OCR Pipeline — Call Path

Référence du chemin de code emprunté quand l'utilisateur clique **Mistral OCR** pour importer un CV.

---

## Chemin complet

```text
StructuredUploadButton.tsx
  -> api.actions.structuredUpload.structuredUpload
  -> my-app/convex/actions/structuredUpload.ts
  -> parser service
  -> canonicalizeParserResult(...)
  -> my-app/convex/lib/parsing/canonicalize.ts
  -> cvDocument.sections[*].structuredContent
  -> vues dérivées / exports / UI secondaires
```

---

## Vérité canonique active

Quand les sections structurées existent et sont valides, elles sont la vérité canonique du produit. Les tableaux top-level sont des vues dérivées ou des fallbacks de transition.

---

## Modes d'environnement

| Mode | Stack | Usage |
|------|-------|-------|
| `./run.sh local` | frontend local + Convex cloud/default + parser local | travail local normal |
| `./run.sh local-convex` | frontend local + Convex local + parser local | debug parser/OCR end-to-end |
| `./run.sh tunnel` | frontend local + Convex cloud/default + parser public via `PARSER_ORIGIN` | comportement edge/tunnel réel |

Le langage opérateur de référence passe désormais par `run.sh local`, `run.sh local-convex` et `run.sh tunnel`, pas par les longues variantes `up --ui ...`.

---

## Fichiers clés

| Fichier | Rôle |
|---------|------|
| `my-app/src/components/StructuredUploadButton.tsx` | point d'entrée UI |
| `my-app/convex/actions/structuredUpload.ts` | action Convex |
| `my-app/convex/lib/parsing/canonicalize.ts` | normalisation parser -> sections |
| `my-app/convex/lib/parsing/__tests__/canonicalize.test.ts` | tests unitaires |
| `cv_parser_service/mistral_ocr.py` | service parser Python |
| `cv_parser_service/tests/test_mistral_layout_sections.py` | tests layout parser |

---

## Voir aussi

- [[concepts/cv-parsing-pipeline]] — stratégie d'évolution du parser
- [[concepts/parsing-poc-progress]] — état par famille
- [[tech/local-vs-remote-parser-architecture]] — séparation local/cloud
- [[APP-launcher-command]] — commandes de debug local
- [[howto/cloudflare-zero-trust-tunnel]] — runbook tunnel parser.dasti.ai
