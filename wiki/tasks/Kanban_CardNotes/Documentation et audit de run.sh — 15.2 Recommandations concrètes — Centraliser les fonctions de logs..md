# Documentation et audit de run.sh — 15.2 Recommandations concrètes — Centraliser les fonctions de logs.

Source: `audit/Documentation et audit de run.sh.md`

Paragraphe: 15.2 Recommandations concrètes

Amélioration proposée: Centraliser les fonctions de logs.

Créer des fonctions `log_info`, `log_warn`, `log_error`, `log_debug`, puis remplacer progressivement les `echo "[run] ..."` par ces fonctions.
