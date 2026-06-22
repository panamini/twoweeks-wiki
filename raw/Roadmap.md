

 restante, concise :

| PR           | Objectif                                           | Scope                                                                                                                    |
| ------------ | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **~~PR33~~** | Golden fixtures du prototype scaffold              | Pure TS fixtures/tests. Freeze les sorties attendues : hidden, blocked, ~~~~~~~~review_required, ready, mixed.~~~~~~~~   |
| **PR34**     | Snapshot / regression guard des surfaces prototype | Vérifier que les fixtures PR33 ne driftent pas et restent non-runnable. Peut être combiné avec PR33 si PR33 est complet. |
| **PR35**     | Readiness checkpoint avant vraie intégration       | Audit court : est-ce qu’on peut commencer une intégration Apps SDK non-prod ? Probablement docs-only.                    |
| **PR36**     | Non-production Apps SDK exploration spike          | Seulement si explicitement validé. Pas de vrai user data, pas de handler, pas de transport prod.                         |
| **PR37**     | Local fake server / fixture-only adapter           | Uniquement mock, local, non-production, aucun vrai MCP tool call.                                                        |
| **PR38**     | Internal review UI/component draft                 | Si besoin. Fixture-only. Pas de vraie action.                                                                            |
| **PR39**     | End-to-end non-prod demo safety review             | Avant toute connexion réelle à ChatGPT.                                                                                  |

Le plus important : **PR33 maintenant**.  
Pas besoin de partir trop loin. Fais d’abord :

```txt
PR33 — Prototype Scaffold Golden Fixtures
```

Après PR33, on décide si PR34 est nécessaire ou si PR33 couvre déjà assez de snapshot/regression guard.