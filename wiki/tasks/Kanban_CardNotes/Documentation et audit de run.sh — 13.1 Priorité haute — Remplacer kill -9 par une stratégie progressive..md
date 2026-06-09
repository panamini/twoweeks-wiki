# Documentation et audit de run.sh — 13.1 Priorité haute — Remplacer `kill -9` par une stratégie progressive.

Source: `audit/Documentation et audit de run.sh.md`

Paragraphe: 13.1 Priorité haute

Amélioration proposée: Remplacer `kill -9` par une stratégie progressive.

Proposition:
	- envoyer d'abord `TERM`;
	- attendre brièvement;
	- vérifier si le processus écoute encore;
	- utiliser `KILL` seulement en dernier recours;
	- afficher la commande/processus propriétaire avant suppression.
	Etapes proposées:
	1. Créer une fonction `stop_pid_gracefully PID SERVICE_NAME`.
	2. Dans cette fonction, vérifier que le PID existe avec `kill -0`.
	3. Envoyer `TERM`.
	4. Attendre une courte période configurable, par exemple `STOP_TIMEOUT_SECONDS=10`.
	5. Recontroler si le PID existe.
	6. Envoyer `KILL` seulement si le processus est encore vivant.
	7. Journaliser chaque étape avec le service concerné.
	8. Pour les ports Vite, vérifier que le processus correspond bien au projet courant avant de le tuer.
