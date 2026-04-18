---
title: "Import OCR Pipeline — Call Path"
category: tech
tags: [import, ocr, pipeline, convex, parser, canonicalize, architecture, sections]
created: 2026-04-12
updated: 2026-04-18
status: current
valid_from: 2026-04-12
valid_until:
superseded_by:
horizon: present
version: v1
sources: [pipeline-note-2026-04-12, 2026-04-14-structured-parsing-canonical-truth, 2026-04-14-local-dev-vs-remote-parser-architecture, 2026-04-14-run-sh-modes, 2026-04-14-run-sh-quick-note, 2026-04-14-export-pipeline-brief-ocr-to-ats-styled-output, 2026-04-15-mistral-resume-v3-section-recovery-scratchpad, 2026-04-15-run-sh-workspace-modes, 2026-04-15-section-detection-future-note]
related: [[concepts/cv-parsing-pipeline]], [[entities/twoweeks]], [[tech/local-vs-remote-parser-architecture]], [[tech/export-pipeline]], [[howto/local-parser-operations]]
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

Cette même donnée normalisée alimente ensuite le pipeline d'export. Le call path OCR/import ne doit pas bifurquer vers le preview DOM pour fabriquer les fichiers finaux.

---

## Modes d'environnement

| Mode | Stack | Usage |
|------|-------|-------|
| `./run.sh local-fast` | frontend local + Convex local + parser local workspace | dev parser full-stack recommandé |
| `./run.sh local-convex` | alias legacy de `local-fast` | compatibilité documentaire/transitoire |
| `./run.sh local` | frontend local + parser local, sans boucle locale complète garantie | usage partiel seulement |
| `./run.sh tunnel` | frontend local + Convex cloud/default + parser public via `PARSER_ORIGIN` | comportement edge/tunnel réel |

Le langage opérateur de référence passe désormais par `run.sh local-fast`, `run.sh tunnel` et les commandes auxiliaires `rebuild-docker` / `reset` / `status` / `logs`, pas par les longues variantes `up --ui ...`.

## Boundary de debug prioritaire

Le bon point d'entrée de diagnostic pour les erreurs de parsing n'est pas l'UI mais :

1. le markdown OCR avec headings explicites détectés
2. `diagnostics.sectionRecovery`
3. `diagnostics.annotationRetry`
4. `diagnostics.parsingQuality`

Le marker de logs `[mistral-quality]` sur la boundary request-level doit être consulté avant toute hypothèse sur le mapper ou le rendu frontend.

---

## Fichiers clés

| Fichier | Rôle |
|---------|------|
| `my-app/src/components/StructuredUploadButton.tsx` | point d'entrée UI |
| `my-app/convex/actions/structuredUpload.ts` | action Convex |
| `my-app/convex/lib/parsing/canonicalize.ts` | normalisation parser -> sections |
| `my-app/convex/lib/parsing/__tests__/canonicalize.test.ts` | tests unitaires |
| `cv_parser_service/mistral_ocr.py` | service parser Python |
| `cv_parser_service/mistral_resume_v3/section_headings.py` | aliases exacts des headings explicites |
| `cv_parser_service/mistral_resume_v3/pipeline.py` | extraction, gates, recovery et retry unique |
| `cv_parser_service/mistral_resume_v3/post_validation.py` | validation post-recovery |
| `cv_parser_service/tests/test_mistral_resume_v3_pipeline.py` | couverture des aliases multilingues et de la retry gate |
| `cv_parser_service/tests/test_mistral_layout_sections.py` | tests layout parser |

## Mistral Resume V3 section recovery

The parser boundary now has an explicit section-recovery layer inside `cv_parser_service/mistral_resume_v3/`.

- `section_headings.py` owns the raw alias list for experience-family headings, including `work history`, `career history`, `professional background`, `relevant experience`, `career experience`, `industry experience`, and the multilingual variants already covered in tests.
- `pipeline.py` normalizes headings, splits compounds only on safe delimiters (`&`, `/`, `|`, `,`, ` y `, ` et `, ` und `, ` e `), and accepts a compound heading only when every recognized segment resolves to the same family.
- `post_validation.py` re-validates recovered payloads so polluted values do not survive re-normalization.
- `RETRYABLE_SECTION_FAILURE` is `section_evidence_contradiction`, which keeps the OCR retry loop to one retry only.

Accepted examples:

- `Experience / Work History`
- `Experiência / Histórico Profissional`
- `Expérience / Expérience Professionnelle`

Rejected as mixed-family headings:

- `Experience & Skills`
- `Expérience & Compétences`
- `Experiencia Profesional y Logros`

## Voir aussi

- [[concepts/cv-parsing-pipeline]] — stratégie d'évolution du parser
- [[tech/local-vs-remote-parser-architecture]] — séparation local/cloud
- [[tech/export-pipeline]] — pipeline document final
- [[howto/local-parser-operations]] — commandes de debug local
- [[howto/cloudflare-zero-trust-tunnel]] — runbook tunnel parser.dasti.ai
