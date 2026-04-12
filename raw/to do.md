-modifier le add ur own section pour qu'il fasse partie du vrai blockrenderer comme summary ou EXPERIENCE, d'ailleur le add ur own permettra de choisir d'ajouter un section type skill , experience, summary. 
pour l'instant il a une legacy section nested , verifier que les autrees sections n'ont pas le meme probleme, 

**asking Codex to make synthetic CVs**


### Robert

Le contenu est encore imparfait métier :

- `education` contient une adresse
- il reste une section texte boilerplate copyright Qwikresume


- `contact.linkedin` contient en fait un lien Instagram
- `contact.website` pointe vers `enhancv.com`
- `languagesText` dit `English, French, German, Arabic`  
    alors que `languages` contient `English, Dutch, French`




—  
Ajoutez **Download raw** **.md** et **Download normalized** **.json**.  

Continuez encore un peu votre approche actuelle pour finir les plus gros bugs visibles.

En parallèle, faites un **POC sur une seule famille** en extraction structurée JSON, par exemple:

- identité/contact
  



- ou education
- ou experience

Comparez:

- coût d’implémentation
- stabilité
- taux de duplication
- facilité à supporter le multilingue

  