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


--gros chantier nouveau effectué
-passage a une petite sidebar, avec affichage dynamique template dans proposal et cv
-page today avec choix des derniers chantiers
-page documents avec preview des de la librairie
-page settings (manque paiement et ingest profile linkedin)
-selecteur temporaire de llm dans proposal, gpt/mistral, (soit a creer dans preference soit a supprimer) en fonction du resultat des test

----------------
renommer styles : BRAND KIT, comme ca l'user peut appliquer sa marque pour creer video ou lettres/cv

ajouter un module de creation d'avatar ia. 

--trucs a affiner


-les generation de proposal font plus d'une page , inclure une limite de longueur.

-mettre en dynamique affichage une toolbar de style qd le texte est sleectionné
-ajouter un profil user(avec import linkedin/upwork/indeed profile), context carreer, avec toutes les experiences achivments de l'user, puis un job/cv match engine, qui fait que l'ia va creer un cv sur mesure en fonction de l'offre d'emploi. avec aussi une creation de cartes/sections dynamiques a chocher/decocher pour créer le cv. 
-ajouter un module pour les tests, avec etoiles et champs texte,apres des actions significatives dans l'app, et relier ça au module autoresearch de karpathy sur git, pour que l'ia reprogramme l'app automatiquement en fonction des notes . 