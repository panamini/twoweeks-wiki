# Documentation et audit de run.sh — 13.2 Priorité moyenne — Rendre le nettoyage Vite plus ciblé.

Source: `audit/Documentation et audit de run.sh.md`

Paragraphe: 13.2 Priorité moyenne

Amélioration proposée: Rendre le nettoyage Vite plus ciblé.

Au lieu de tuer toute la plage `5173-5215`, conserver le PID exact de Vite et ne tuer les ports que si le processus correspond au projet courant ou à une commande Vite.
	Etapes proposées:
	1. Lire d'abord `VITE_PID` depuis le fichier d'état.
	2. Vérifier que ce PID correspond à un processus Vite lancé depuis `my-app`.
	3. Arrêter ce PID proprement.
	4. Ne scanner les ports qu'en fallback.
	5. En fallback, afficher le processus trouvé et demander confirmation hors mode CI.
	6. En production, interdire le kill par plage de ports.
