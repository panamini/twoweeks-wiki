# Documentation et audit de run.sh — 13.3 Priorité basse — Ajouter une table de compatibilité des modes.

Source: `audit/Documentation et audit de run.sh.md`

Paragraphe: 13.3 Priorité basse

Amélioration proposée: Ajouter une table de compatibilité des modes.

Exemple:

| Mode         | Parser                 | Convex    | Vite | Tunnel | Usage                   |
| ------------ | ---------------------- | --------- | ---- | ------ | ----------------------- |
| `local-fast` | local workspace reload | local     | oui  | non    | dev rapide              |
| `local`      | local image            | cloud/env | oui  | non    | validation parser local |
| `tunnel`     | local image + edge     | cloud/env | oui  | oui    | validation stable       |
| `parser-dev` | local workspace reload | non       | non  | non    | hacking parser          |
