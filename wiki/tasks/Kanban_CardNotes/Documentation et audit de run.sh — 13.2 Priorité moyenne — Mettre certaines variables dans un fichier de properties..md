# Documentation et audit de run.sh — 13.2 Priorité moyenne — Mettre certaines variables dans un fichier de properties.

Source: `audit/Documentation et audit de run.sh.md`

Paragraphe: 13.2 Priorité moyenne

Amélioration proposée: Mettre certaines variables dans un fichier de properties.

Oui, c'est envisageable et recommandé, à condition de séparer les variables non sensibles des secrets.
	Objectif: sortir du script les valeurs qui changent selon l'environnement, sans rendre le script plus fragile.
	Variables candidates non sensibles:
	- `PARSER_ORIGIN`;
	- `OPEN_BROWSER`;
	- `TUNNEL_NETWORK`;
	- `PARSER_NAME`;
	- `CLOUDFLARED_NAME`;
	- `IMAGE_NAME`;
	- `PARSER_RUNTIME_MODE`;
	- `VITE_PORT`;
	- `LOCAL_CONVEX_CLOUD_PORT`;
	- `LOCAL_CONVEX_SITE_PORT`;
	- `LOCAL_CONVEX_STARTUP_TIMEOUT`;
	- `LOCAL_CONVEX_SYNC_SECRETS`;
	- `CACHE_DIR`;
	- `DOCKER_STATE_DIR`;
	- `CLOUDFLARED_IMAGE`;
	- `LOG_LEVEL`;
	- `RUN_ENV`;
	- `STOP_TIMEOUT_SECONDS`.
	Variables a ne pas mettre dans un fichier properties versionné :
	- `TUNNEL_TOKEN`;
	- `MISTRAL_API_KEY`;
	- `OPENAI_API_KEY`;
	- `DEEPSEEK_API_KEY`;
	- `QWEN_API_KEY`;
	- `CF_ACCESS_CLIENT_SECRET`;
	- tout secret, token, mot de passe ou clé privée.
	Structure cible possible:
	```text
	config/
	run.defaults.properties # valeurs par défaut versionnées
	run.dev.properties # configuration dev non sensible
	run.staging.properties # configuration staging non sensible
	run.prod.properties # configuration prod non sensible
	run.local.properties # ignore git, overrides poste local
	```
	Ordre de priorité proposé :
	a. valeurs internes minimales du script;
	b. `config/run.defaults.properties`;
	c. `config/run.${RUN_ENV}.properties`;
	d. `config/run.local.properties`;
	e. variables d'environnement déjà exportées;
	f. options CLI.
	Cette priorité permet de garder une valeur par défaut, de la surcharger par environnement, puis de laisser l'opérateur surcharger temporairement via le shell ou la ligne de commande.
	Etapes proposées:
	1. Créer une fonction `load_properties FILE`.
	2. Accepter uniquement les lignes `KEY=value` simples.
	3. Ignorer les lignes vides et les commentaires commençant par `#`.
	4. Refuser les noms de variables non autorises.
	5. Masquer les valeurs sensibles dans tout affichage.
	6. Ajouter `config-validate` pour vérifier les fichiers properties.
	7. Ajouter `config-print --redacted` pour voir la configuration finale.
	8. Documenter quelles variables appartiennent aux properties et quelles variables doivent rester dans un gestionnaire de secrets.
	9. En production, charger les secrets depuis l'environnement d'exécution ou un secret manager, pas depuis le fichier properties versionné.
	10. Ajouter un test qui prouve qu'une option CLI gagne bien sur une property.
