---
title: "Import OCR Pipeline — Call Path"
category: tech
tags: [import, ocr, pipeline, convex, parser, canonicalize, architecture]
created: 2026-04-12
updated: 2026-04-12
status: current
valid_from: 2026-04-12
valid_until:
superseded_by:
horizon: present
version: v1
sources: [pipeline-note-2026-04-12]
related: [[concepts/cv-parsing-pipeline]], [[concepts/parsing-poc-progress]], [[entities/cv-forge]]
---

# Import OCR Pipeline — Call Path

Référence exacte du chemin de code emprunté quand l'utilisateur clique le bouton **"Mistral OCR"** pour importer un CV.

---

## Chemin complet (de l'UI au parser)

```
StructuredUploadButton.tsx
  → api.actions.structuredUpload.structuredUpload
  → my-app/convex/actions/structuredUpload.ts
  → canonicalizeParserResult(...)
  → my-app/convex/lib/parsing/canonicalize.ts
  → canonicalizeExperience(...)      ← frontière de diagnostic active
  → POST https://parser.dasti.ai/mistral-ocr/parse
```

## Stack live de référence

| Variable | Valeur |
|----------|--------|
| Frontend | local (`./run.sh up --ui`) |
| Convex deployment | `cloud/default` |
| Parser base URL | `https://parser.dasti.ai` |
| Route parser | `/mistral-ocr/parse` |
| Bouton UI | "Mistral OCR" (= `StructuredUploadButton`) |

## Points d'attention

- **`structuredUpload.ts`** est le wrapper/action Convex — point d'entrée, pas de décision de sélection de source.
- **`canonicalizeExperience(...)`** dans `canonicalize.ts` est la **frontière de diagnostic active**.
- `canonicalize.ts` orchestre toutes les familles — chaque famille a sa propre fonction `canonicalize[Family](...)`.

## Fichiers clés

| Fichier | Rôle |
|---------|------|
| `my-app/src/components/StructuredUploadButton.tsx` | Bouton UI qui déclenche l'import |
| `my-app/convex/actions/structuredUpload.ts` | Action Convex — wrapper d'appel au parser |
| `my-app/convex/lib/parsing/canonicalize.ts` | Normalisation résultat parser → sections structurées |
| `my-app/convex/lib/parsing/__tests__/canonicalize.test.ts` | Tests unitaires |
| `cv_parser_service/mistral_ocr.py` | Service parser Python |
| `cv_parser_service/tests/test_mistral_layout_sections.py` | Tests layout parser |

## Voir aussi

- [[concepts/cv-parsing-pipeline]] — stratégie d'évolution du parser
- [[concepts/parsing-poc-progress]] — état par famille
- [[howto/cloudflare-zero-trust-tunnel]] — runbook tunnel parser.dasti.ai
