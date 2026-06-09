# Documentation et audit de run.sh — 14.2 Améliorations d'idempotence proposées — Ajouter des tests automatisés d'idempotence.

Source: `audit/Documentation et audit de run.sh.md`

Paragraphe: 14.2 Améliorations d'idempotence proposées

Amélioration proposée: Ajouter des tests automatisés d'idempotence.

Tests minimum recommandés:
	```text
	Test 1: ./run.sh help retourne 0 et ne crée pas d'état.
	Test 2: ./run.sh down retourne 0 si rien n'est lancé.
	Test 3: ./run.sh down peut être lancé deux fois.
	Test 4: ./run.sh status retourne 0 même si aucun service ne tourne.
	Test 5: ./run.sh up --dry-run ne modifie pas tmp/dev-stack.
	Test 6: ./run.sh config-validate échoue si une property inconnue est présente.
	Test 7: ./run.sh local-fast --dry-run affiche les actions attendues sans démarrer Docker.
	```
	Tests avec services réels, à exécuter dans un environnement d'intégration:
	```text
	Test 8: ./run.sh up --local-origin lance le parser puis /ready répond 200.
	Test 9: relancer la même commande ne recrée pas inutilement le conteneur.
	Test 10: ./run.sh reload-env sans changement ne redémarre rien.
	Test 11: modifier une variable d'env provoque seulement le redémarrage attendu.
	Test 12: ./run.sh down arrête la pile.
	Test 13: relancer ./run.sh down retourne encore 0.
	```
