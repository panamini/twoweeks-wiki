---
title: "Industrialisation AWS — sécurité, scalabilité et exploitation"
category: tech
status: current
created: 2026-08-13
updated: 2026-08-19
valid_from: 2026-08-13
version: v1
tags: [aws, security, industrialization, scalability, automation, production, capacity]
related:
  - "[[strategy/us-first-cloud-region]]"
  - "[[tech/local-vs-remote-parser-architecture]]"
  - "[[howto/cloudflare-zero-trust-tunnel]]"
  - "[[howto/local-parser-operations]]"
---

# Industrialisation AWS — sécurité, scalabilité et exploitation

Ce document fixe le cadre d’industrialisation de Twoweeks sur AWS. **La sécurité est un préalable d’architecture et une condition de mise en production**, pas une étape de finition. Les quatre maîtres mots sont : **sécurité, industrialisation, scalabilité et automatisation**.

L’objectif n’est pas de migrer prématurément vers une architecture complexe. Il est de rendre la beta actuelle mesurable, reproductible et réversible, puis de déclencher chaque évolution AWS à partir de seuils observés. Le cloud fournit les mécanismes de mise à l’échelle; Twoweeks doit d’abord définir ses invariants, ses métriques et ses responsabilités.

## Décision directrice

1. Aucun trafic utilisateur ne justifie de contourner un contrôle de sécurité.
2. Aucun changement manuel non traçable ne constitue un processus de production.
3. Aucune montée en gamme d’infrastructure ne se décide sans mesure de saturation, de latence, d’erreur et de coût.
4. Toute ressource de production doit être reconstructible, observable, sauvegardée selon son rôle et assortie d’un rollback testé.
5. Les données CV, offres et documents générés sont des données personnelles; leur minimisation, leur isolation et leur durée de conservation guident l’architecture.

Le cadre suit les six piliers AWS Well-Architected : excellence opérationnelle, sécurité, fiabilité, efficacité des performances, optimisation des coûts et durabilité. La sécurité demeure le filtre transversal de chaque décision.

## Périmètre

Ce document couvre :

- le frontend public, l’identité, les fonctions applicatives et le parser/export;
- le compte AWS, le réseau, les accès, les secrets et la chaîne de livraison;
- la capacité, les SLO d’ingénierie, l’observabilité et la réponse aux incidents;
- la trajectoire du serveur beta vers une plateforme horizontalement scalable;
- les critères d’entrée et de sortie de chaque palier.

Il ne remplace pas le runbook de déploiement, ne fixe pas un SLA commercial et n’autorise pas à lui seul une migration, un nouveau service payant ou une nouvelle région de données.

## État de référence

Le baseline versionné après la PR Neyssan #406 est :

```text
Utilisateur
   │
   ├── Cloudflare Pages ── twoweeks.ai
   ├── Clerk ───────────── identité
   └── Convex Cloud ────── données, fichiers et actions
                              │
                              ▼
                    parser.twoweeks.ai
                              │
                    Cloudflare Access/Tunnel
                              │
                              ▼
                    AWS Lightsail us-east-1
                    Docker Compose
                    ├── FastAPI + Mistral OCR
                    ├── Node + Playwright export
                    └── cloudflared
```

Le parser beta est stateless du point de vue métier : aucun CV ne doit être conservé sur le disque de la VM. Son port applicatif reste lié à `127.0.0.1:8001`; HTTP/HTTPS ne sont pas ouverts directement au public. Les images sont immuables et adressées par SHA Git complet. Les secrets sont récupérés à l’exécution depuis Infisical. La cible beta documentée est une VM Lightsail `2 vCPU / 2 GiB / 60 GiB` en `us-east-1`.

Cette architecture est adaptée à une beta contrôlée, mais elle possède un point unique de défaillance et aucune élasticité horizontale. Elle ne constitue donc pas l’architecture de croissance.

## Checkpoint réel Neyssan — 2026-08-19

Le code fusionné, l’artefact Edge et la configuration d’identité doivent rester trois preuves séparées :

| Surface | État observé | Conséquence |
| --- | --- | --- |
| Code | #408/#409 et #411–#414 fusionnées; référence `main@83872148d91263591d4cb9025cd39fbe60acfef4` | le code et le SHA source sont prouvés |
| Cloudflare Pages Production | build `my-app` réussi sur `main@83872148`, alias `twoweeks.ai` et `beta.twoweeks.ai`; les deux domaines renvoient anonymement HTTP 302 vers Cloudflare Access | le déploiement Pages immédiatement précédent est `5de4e349`; le smoke des deux identités autorisées reste à terminer |
| Convex Production | cible `prod:giddy-basilisk-88`; déploiement depuis un worktree propre de `main@83872148` avec build réussi; fonctions profils/Jobs/propositions/génération/suppression présentes; issuer `https://clerk.twoweeks.ai` | le SHA et l’issuer sont prouvés; le seul delta de schéma est optionnel, sans migration destructive; l’historique instantané reste indisponible |
| Clerk dans Cloudflare Production | `VITE_CLERK_PUBLISHABLE_KEY` est une clé `pk_live` liée à `clerk.twoweeks.ai`; template JWT `convex` présent | identité Production alignée; sessions anciennes à renouveler |
| Canary | compte synthétique supprimé en Production; tombstone `purged`/`complete`, 41 lots, `deleteClerkUser` en succès | canary de suppression validé; smoke des deux identités autorisées et rollback Convex restent à traiter |
| Parser Lightsail | image `sha-83872148` construite, testée PDF/DOCX et publiée; image live toujours `sha-408e428577704007a5fbafce179b14ef8765a0f2` | alignement de maintenance recommandé, non blocker fonctionnel de la bêta privée |

La bascule Clerk Production est effectuée et l’issuer Convex est aligné. Le canary de suppression synthétique est validé. Le code, Pages et Convex sont alignés sur `83872148`; restent le smoke des deux identités autorisées, l’isolation A/B et l’exercice du repli coordonné vers la source pré-#411 `966890d9df580ca2c404faa8e1ed3da87f691ffd`. Le confinement Cloudflare actuel reste en place. Les bugs non bloquants de bêta, dont la course d’upload/suppression, restent documentés en backlog séparé. Le détail et les limites sont consignés dans [[sources/2026-08-14-neyssan-auth-production-transition-checkpoint]].

Les secrets ne doivent jamais être copiés dans ce document. La rotation/révocation observée pendant le dry-run reste une gate finale pré-production différée; ce report ne vaut pas preuve de rotation.

## Modèle de responsabilité

| Domaine | Autorité actuelle | Exigence Twoweeks |
| --- | --- | --- |
| Frontend statique et Edge | Cloudflare | TLS, domaines maîtrisés, headers de sécurité, rollback de build |
| Identité | Clerk | instance correcte par environnement, MFA opérateur, isolation multi-compte testée |
| Données applicatives | Convex | contrôle d’accès par utilisateur, sauvegarde/export validés, suppression vérifiable |
| Calcul parser/export | AWS | hôte privé, image immuable, capacité mesurée, logs sans données sensibles |
| OCR génératif | Mistral | secrets serveur uniquement, timeouts, quotas, erreurs et coûts observés |
| Secrets | Infisical | moindre privilège, Machine Identity dédiée, rotation et révocation testées |
| Code et release | GitHub/GHCR | branches protégées, CI obligatoire, provenance/SBOM, déploiement par SHA |

Un fournisseur gère la sécurité **de** son cloud; Twoweeks reste responsable de la configuration, des identités, des données, du code, des secrets et de la réponse aux incidents.

## Sécurité au centre

### Identités et privilèges

- MFA obligatoire pour le compte root AWS; root est réservé à la récupération et aux opérations exceptionnelles.
- IAM Identity Center pour les opérateurs; aucun accès quotidien par clé AWS longue durée.
- Rôles séparés au minimum entre lecture/audit, déploiement et administration exceptionnelle.
- Accès machine limité à une fonction, un environnement et un chemin de secrets précis.
- Revue trimestrielle des accès et révocation immédiate lors d’un départ ou d’un incident.
- Déploiement CI vers AWS par fédération OIDC lorsque la chaîne AWS sera automatisée; aucun secret AWS permanent dans GitHub.

### Réseau et exposition

- Aucun port parser public; seul le tunnel sortant ou l’ingress approuvé atteint le service.
- SSH restreint aux CIDR opérateur approuvés, puis remplacé à terme par un accès administré et audité si la plateforme retenue le permet.
- Segmentation par environnement et, au palier managé, tâches dans des subnets privés répartis sur au moins deux zones de disponibilité.
- WAF/rate limiting au point d’entrée public, avec limites distinctes pour health, parsing et export.
- Egress explicite vers les fournisseurs nécessaires; aucun accès réseau général non justifié.

### Secrets et cryptographie

- Aucun secret dans Git, les images, les variables `VITE_*`, les logs ou les artefacts CI.
- Infisical reste l’autorité tant qu’une migration explicite vers AWS Secrets Manager n’est pas décidée; ne pas maintenir deux sources de vérité.
- Chiffrement TLS en transit et chiffrement au repos pour tout stockage persistant.
- Rotation documentée des identifiants Cloudflare, Mistral, GHCR, Clerk et Machine Identity.
- Les credentials temporaires de registre utilisent une configuration Docker éphémère détruite après déploiement.

### Données personnelles

- Minimiser les données envoyées au parser et aux fournisseurs IA.
- Traitement temporaire en mémoire ou `tmpfs`; aucun volume CV persistant sur le compute parser.
- Interdire les CV, offres, prompts complets, tokens et identifiants personnels dans les logs.
- Définir et tester les durées de conservation, l’export, la suppression de compte et l’effacement des fichiers liés.
- Documenter la région et le sous-traitant de chaque flux : Convex, Clerk, Cloudflare, AWS et Mistral.

### Chaîne logicielle

- Dépendances verrouillées; images de base et images `cloudflared` épinglées.
- Scan de vulnérabilités, Semgrep, tests et build production obligatoires avant release.
- SBOM et provenance produits par CI; image déployée identifiée par digest ou SHA immuable.
- Signature d’image et politique d’admission deviennent obligatoires avant le palier multi-instance.
- Correctif critique : objectif de qualification sous 24 h et déploiement dès validation; les autres sévérités suivent une fenêtre planifiée.

### Détection et incident

- CloudTrail, alertes de facturation et détection de menace activés au niveau adapté au compte.
- Alertes techniques routées vers un canal avec propriétaire, sévérité et accusé de réception.
- Playbooks minimaux : secret compromis, compte opérateur compromis, fuite de données, indisponibilité parser, erreur de déploiement, dérive de coût.
- Chaque incident conserve une chronologie, une cause racine, les actions de confinement et un suivi vérifiable.

## Objectifs de service provisoires

Ces objectifs sont des **SLO d’ingénierie à valider**, pas des SLA clients.

| Indicateur | Objectif beta initial | Mesure |
| --- | --- | --- |
| Disponibilité du chemin parser | 99,5 % mensuel | probe externe authentifié, hors maintenance annoncée |
| Santé locale parser | p95 < 500 ms | `/healthz` depuis l’hôte |
| Parsing CV complet | p95 < 45 s, p99 < 90 s | de l’acceptation à la réponse utilisable |
| Export PDF/DOCX | p95 < 20 s, p99 < 45 s | requête à téléchargement disponible |
| Erreurs techniques parser/export | < 1 % sur 15 min hors erreurs utilisateur | taux 5xx, timeouts et échecs worker |
| Déploiement | rollback vers le dernier SHA sain < 15 min | exercice chronométré |
| Alerte critique | détection < 5 min, prise en charge < 15 min | horodatage monitor/accusé |

Le budget d’erreur beta correspondant à 99,5 % est d’environ 3 h 39 min sur un mois de 30,4 jours. Si plus de 50 % du budget est consommé avant la moitié du mois, les releases fonctionnelles non urgentes sont suspendues jusqu’au retour à une trajectoire sûre.

## Modèle de volumétrie

### Unités de charge

Le nombre d’utilisateurs n’est pas une mesure suffisante. Le compute AWS supporte principalement deux unités :

- **parse job** : réception d’un document, extraction, appel OCR éventuel et normalisation;
- **export job** : rendu Node/Playwright puis production PDF ou DOCX.

Les lectures d’interface et la majorité des mutations applicatives passent par Cloudflare/Convex et ne chargent pas directement Lightsail. La capacité doit donc être pilotée par les jobs, leur concurrence et leur temps de service.

### Hypothèses de planification

Les valeurs suivantes sont des ordres de grandeur à remplacer par la télémétrie réelle. Elles supposent un pic horaire équivalent à 15 % du volume quotidien et un facteur de sécurité de 2 sur la concurrence mesurée.

| Palier | Utilisateurs actifs mensuels | Actifs/jour | Sessions simultanées au pic | Parse jobs/jour | Export jobs/jour | Jobs/min au pic |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Beta contrôlée | 50 | 15 | 5 | 30 | 100 | 1–2 |
| Lancement | 1 000 | 250 | 40 | 500 | 2 000 | 6–8 |
| Croissance | 10 000 | 2 500 | 300 | 5 000 | 20 000 | 50–70 |
| Échelle | 100 000 | 25 000 | 2 000 | 50 000 | 200 000 | 400–600 |

Ces hypothèses ne sont pas des capacités garanties. Un upload volumineux, un PDF complexe et un export Chromium consomment des ressources très différentes. Les métriques doivent donc inclure le type de job, la taille d’entrée, le nombre de pages, la durée, le résultat et le fournisseur appelé, sans contenu personnel.

### Formule de capacité

Pour chaque classe de job :

```text
concurrence requise = débit de pointe (jobs/s) × durée p95 (s)
capacité provisionnée = concurrence requise × facteur de sécurité
capacité sûre d'une instance = 60 % du point de saturation mesuré
```

Exemple : 8 jobs/minute avec un temps p95 de 30 secondes représentent environ 4 jobs simultanés. Avec un facteur de sécurité de 2, la plateforme doit en absorber 8 sans dépasser ses seuils de saturation. Ce calcul doit être séparé entre parse et export.

## Test de charge obligatoire

Avant d’élargir la beta :

1. construire un corpus synthétique sans donnée personnelle couvrant PDF natif, scan, DOCX, documents courts/longs et erreurs;
2. mesurer séparément parsing, export PDF et export DOCX;
3. tester les concurrences 1, 2, 4, 8 puis 16 jusqu’à saturation contrôlée;
4. enregistrer débit, p50/p95/p99, CPU, mémoire, OOM, disque temporaire, erreurs, 429/5xx fournisseur et coût;
5. maintenir une charge stable 30 minutes, puis un pic rapide et un test d’endurance de 4 heures;
6. conserver le rapport et la configuration exacte comme preuve de capacité.

La capacité annoncée est le dernier palier qui respecte simultanément les SLO, reste sous 60 % CPU moyen, sous 70 % mémoire, sans OOM/restart et avec au moins 40 % de marge sur le quota fournisseur.

## Seuils de décision

| Signal observé sur 7 jours ou lors d’un test | Action |
| --- | --- |
| CPU p95 > 60 %, mémoire p95 > 70 %, ou swap/OOM | réduire la concurrence puis redimensionner; ne pas masquer par un simple restart |
| p95 dépasse le SLO pendant 3 fenêtres de 15 min | ouvrir incident capacité et geler l’élargissement de cohorte |
| concurrence sûre < demande de lancement × 2 | ne pas ouvrir le lancement; passer au palier multi-instance |
| taux 429 fournisseur > 0,5 % ou quota restant < 40 % du pic prévu | négocier quota, limiter la demande et ajouter backoff/queue |
| un déploiement ou une panne hôte dépasse le RTO | prioriser haute disponibilité et déploiement managé |
| croissance prévue > 2× en 30 jours | exécuter un nouveau test de capacité avant acquisition |
| coût variable > objectif unitaire pendant 2 semaines | analyser coût par type de job et optimiser la cause dominante |

## Trajectoire d’industrialisation AWS

### Palier 0 — beta contrôlée sur Lightsail

Objectif : valider le produit et établir les mesures de référence.

- un hôte stateless, image immuable, firewall strict, tunnel sortant;
- snapshots automatiques de l’hôte, tout en rappelant qu’ils ne sauvegardent pas Convex;
- déploiement reproductible par SHA, healthcheck local et smoke externe authentifié;
- logs bornés, vérification CPU/mémoire/disque, alerte externe de disponibilité;
- cohortes et limites de concurrence explicites;
- rollback testé avant ajout d’utilisateurs.

Sortie du palier : charge réelle mesurée, tableau de bord opérationnel, alertes, exercice de rollback et aucun gate sécurité beta ouvert.

### Palier 1 — exploitation automatisée sans replatforming

Objectif : supprimer la dépendance aux gestes manuels avant d’ajouter de la capacité.

- infrastructure décrite en IaC pour compte, tags, firewall, alertes et ressources autorisées;
- CI/CD avec build unique, scan, SBOM, promotion de digest et approbation production;
- fédération GitHub OIDC vers un rôle de déploiement minimal;
- monitoring système et applicatif centralisé, probes synthétiques et budgets AWS;
- rotation automatique ou assistée des secrets avec test de révocation;
- tests de restauration et de remplacement complet de l’hôte;
- journal de changements et revue post-déploiement automatique.

Le palier 1 ne crée pas encore une architecture hautement disponible. Il rend la faiblesse actuelle observable et remplaçable.

### Palier 2 — compute managé et haute disponibilité

Déclencheur : demande de lancement non absorbable avec marge, RTO non tenu, ou besoin contractuel de haute disponibilité.

Architecture cible recommandée à valider par benchmark :

- image dans Amazon ECR, signée et scannée;
- service Amazon ECS sur Fargate réparti sur au moins deux zones de disponibilité;
- minimum de deux tâches pour le chemin synchrone critique;
- tâches en réseau privé, sans IP publique;
- ingress unique clairement choisi : tunnel Cloudflare répliqué **ou** endpoint AWS protégé; éviter deux autorités concurrentes;
- logs et métriques dans CloudWatch, alarmes vers le canal d’astreinte;
- autoscaling sur une métrique corrélée à la demande : CPU/mémoire pour le premier réglage, puis requêtes par cible ou métrique de jobs en cours;
- déploiement progressif avec rollback automatique sur santé et erreurs.

AWS ECS Service Auto Scaling permet le target tracking sur CPU, mémoire ou requêtes ALB par cible. Le choix final doit être fondé sur la métrique qui varie avec la demande et diminue proportionnellement quand la capacité augmente.

### Palier 3 — jobs asynchrones et élasticité

Déclencheur : pics importants, temps de traitement variables, timeouts synchrones ou besoin de protéger les fournisseurs.

- séparation API d’admission / workers de parsing / workers d’export;
- file Amazon SQS avec dead-letter queue, idempotency key et délai maximal;
- stockage temporaire chiffré avec lifecycle court uniquement si le traitement en mémoire ne suffit plus;
- autoscaling des workers sur profondeur et âge du plus ancien message;
- quotas par utilisateur et par organisation, backpressure et réponses `429` explicites;
- retries bornés avec jitter; aucune relance aveugle d’un job non idempotent;
- notification de fin de job et reprise côté produit.

Ce palier change le contrat applicatif. Il exige une spécification produit et une migration séparées; il ne doit pas être introduit uniquement pour “faire scalable”.

### Palier 4 — multi-région ou résidence EU

Déclencheur : exigence contractuelle, volumétrie géographique démontrée ou objectif de reprise qui ne peut être tenu en région unique.

- carte de données complète et décision de résidence;
- Convex/projets, parser, logs et sauvegardes alignés par région;
- stratégie de routage, réplication, cohérence, chiffrement et suppression;
- tests de bascule et de retour arrière;
- validation juridique et fournisseurs avant activation.

La multi-région n’est pas un objectif de la beta.

## Automatisation de la livraison

```text
Pull request
  → tests unitaires/contrats
  → build image production
  → scan sécurité + SBOM + provenance
  → smoke image
  → merge protégé
  → image SHA/digest immuable
  → approbation production
  → déploiement progressif
  → smoke authentifié
  → observation
  → promotion ou rollback automatique
```

Règles :

- même artefact entre validation et production;
- aucun build sur le serveur;
- migrations et changements de secrets séparés du déploiement applicatif quand leur rollback diffère;
- protection contre deux déploiements concurrents;
- journal automatique du SHA, digest, acteur, heure, résultat et rollback;
- environnement de preview sans accès aux données de production.

## Observabilité

### Métriques minimales

- trafic : jobs reçus, acceptés, refusés, terminés, débit par type;
- performance : latence p50/p95/p99 et temps d’attente;
- fiabilité : 4xx, 5xx, timeouts, retries, DLQ, restarts;
- saturation : CPU, mémoire, descripteurs, espace temporaire, concurrence active;
- dépendances : latence et erreurs Mistral, tunnel, Convex et stockage;
- sécurité : échecs d’authentification, rate limit, changements IAM, secrets expirants;
- coût : compute, transfert, observabilité et fournisseur par 1 000 jobs.

### Corrélation

Chaque requête reçoit un identifiant de corrélation non personnel propagé de Convex au parser puis aux workers. Les logs sont structurés, horodatés, redacted et associés au SHA déployé. Aucun contenu de CV ou prompt complet n’est nécessaire pour diagnostiquer la majorité des incidents.

### Alertes actionnables

Une alerte doit indiquer l’impact, le seuil, le composant, le runbook et le propriétaire. Les symptômes sans action ne doivent pas réveiller un opérateur. Les quatre alertes initiales sont : indisponibilité externe, taux 5xx, saturation mémoire/OOM et absence ou boucle de redémarrage du tunnel.

## Continuité et reprise

- Le parser est reconstruit depuis l’image et l’IaC; son RPO cible est zéro donnée métier locale.
- Les snapshots Lightsail accélèrent une récupération, mais ne remplacent ni le rebuild ni la sauvegarde des données Convex.
- Le RPO/RTO des données CV doit être défini avec les fonctions d’export/restauration réellement testées de Convex; aucune valeur ne doit être promise avant cette preuve.
- Conserver le dernier digest sain, tester le rollback mensuellement pendant la beta et le remplacement complet de l’hôte au moins trimestriellement.
- Une restauration n’est réussie qu’après authentification, parsing réel, export PDF/DOCX et vérification d’isolation utilisateur.

## Pilotage des coûts

Le coût doit être suivi par unité métier, pas uniquement par facture mensuelle :

```text
coût par 1 000 parse jobs
coût par 1 000 exports PDF/DOCX
coût fournisseur IA par document et par page
coût d'observabilité par environnement
coût fixe de capacité minimale
```

Activer tags, budgets et alertes avant le palier 1. Revoir mensuellement les ressources inutilisées, la rétention des logs, le dimensionnement, les quotas et les coûts de transfert. Une optimisation ne peut pas réduire la marge de sécurité ou supprimer une preuve opérationnelle essentielle.

## Gouvernance et preuves

| Preuve | Fréquence | Propriétaire |
| --- | --- | --- |
| Revue accès/IAM/secrets | trimestrielle et à chaque changement d’équipe | responsable sécurité/technique |
| Scan dépendances/images | chaque build et revue hebdomadaire des findings | équipe engineering |
| Test de charge | avant chaque palier et après changement majeur parser/export | owner parser |
| Rollback applicatif | mensuel pendant beta | opérateur production |
| Restauration/rebuild hôte | trimestriel | opérateur AWS |
| Suppression et isolation multi-compte | avant beta puis à chaque changement d’identité/persistance | owner produit/backend |
| Revue coûts/capacité | mensuelle, hebdomadaire en phase de croissance | responsable produit/technique |
| Revue Well-Architected | avant palier 2 puis semestrielle | architecture + sécurité |

## Plan d’exécution

### Avant élargissement de la beta

- fermer les gates identité, isolation multi-compte, suppression et écritures tardives;
- mesurer la capacité 2 vCPU / 2 GiB avec le protocole défini;
- activer dashboards, alertes, budget et probe externe authentifié;
- tester rotation de secret, rollback SHA et reconstruction de l’hôte;
- documenter RACI d’incident et canal d’escalade;
- confirmer que les logs ne contiennent pas de donnée CV.

### Avant lancement

- disposer de quatre semaines de métriques beta exploitables;
- prouver que la capacité sûre absorbe le pic prévu avec facteur 2;
- terminer IaC et déploiement automatisé avec OIDC;
- valider RPO/RTO des données Convex;
- décider, à partir des mesures, maintien Lightsail redimensionné ou passage ECS/Fargate;
- réaliser une revue sécurité et un exercice d’incident.

### Avant croissance

- rendre le compute multi-instance et multi-AZ;
- introduire une queue seulement si les mesures prouvent le besoin;
- automatiser autoscaling, déploiement progressif et rollback;
- suivre coût et performance par type de job;
- tester les quotas et la dégradation contrôlée des fournisseurs.

## Definition of Done de l’industrialisation

L’industrialisation est considérée suffisante pour un palier lorsque :

- l’architecture et les flux de données sont documentés et à jour;
- les contrôles de sécurité du palier sont prouvés;
- l’infrastructure peut être reconstruite sans connaissance tacite;
- le déploiement et le rollback sont automatisés, traçables et testés;
- la capacité sûre et le coût unitaire sont mesurés;
- les SLO, dashboards et alertes sont actifs;
- les sauvegardes/restaurations correspondant aux propriétaires de données sont testées;
- les incidents ont un owner, un runbook et un canal d’escalade;
- aucun risque critique ou haut non accepté n’est ouvert;
- la décision de passer au palier suivant repose sur un seuil observé.

## Points restant à mesurer

- débit et concurrence sûrs du parser/export beta;
- distribution réelle des tailles, pages et types de documents;
- quotas, latence et coût Mistral au pic;
- RPO/RTO réellement disponibles pour Convex et ses fichiers;
- disponibilité Edge → tunnel → parser sur une période représentative;
- coût total et coût unitaire de chaque job;
- charge issue de l’extension Chrome et du futur MCP lorsqu’ils deviennent transactionnels.

## Sources

- [AWS Well-Architected Framework — piliers](https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html)
- [AWS Security Reference Architecture — approche par phases](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/phases.html)
- [Amazon ECS Service Auto Scaling — target tracking](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-autoscaling-targettracking.html)
- [Amazon ECS — caractériser l’application avant autoscaling](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/capacity-autoscaling-best-practice.html)
- Runbook versionné Neyssan : `docs/operations/deploiement-production-beta.md`
- [[strategy/us-first-cloud-region]]
- [[tech/local-vs-remote-parser-architecture]]
