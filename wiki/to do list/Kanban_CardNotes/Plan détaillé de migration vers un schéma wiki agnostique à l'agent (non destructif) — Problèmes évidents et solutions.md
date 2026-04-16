#


1. Outil qui lit exclusivement `CLAUDE.md`.
- Symptôme: workflow cassé après migration.
- Solution: conserver le shim `CLAUDE.md` le temps de la transition.

2. Divergence entre `CLAUDE.md` et `WIKI_SCHEMA.md`.
- Symptôme: règles contradictoires.
- Solution: interdire toute règle métier dans `CLAUDE.md`.

3. Skill non alignée.
- Symptôme: l'agent applique encore l'ancienne logique.
- Solution: mettre à jour immédiatement `skills/twoweeks-wiki-operator`.

4. Références internes oubliées.
- Symptôme: docs qui pointent encore vers `CLAUDE.md`.
- Solution: exécuter `rg -n "CLAUDE.md" .` puis corriger.

5. Fichiers de test oubliés en fin de validation.
- Symptôme: pollution de `raw/` ou `wiki/sources/`.
- Solution: faire systématiquement le rollback test de l'étape 7.4 puis `git status`.
