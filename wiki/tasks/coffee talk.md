---
title: "Coffee Talk"
category: task
status: current
created: 2026-05-02
updated: 2026-05-02
---

# Coffee Talk

## Note collaborateur — Codex skill

À faire côté collaborateur: mettre à jour sa skill Codex `ingest-wiki` avec la version actuelle du repo.

Étape la plus courte:

```bash
cp skills/ingest-wiki/SKILL.md ~/.codex/skills/ingest-wiki/SKILL.md
```

Pourquoi: la skill doit lire `wiki/hot.md` comme mémoire légère avant `wiki/index.md`, avec les modes `quick`, `standard` et `deep`.
