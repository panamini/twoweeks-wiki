
**asking Codex to make synthetic CVs**

Yes — that is a good idea, but **not right this second**.

Use synthetic CVs when:

- you need to test underrepresented families like:

- hobbies
- certifications
- projects
- affiliations
- additional information

- or when you need very specific contamination layouts that you do not already have in real fixtures

Do **not** switch to synthetic-fixture generation before finishing this current contamination family, or you will split focus.

**Best timing**

Talk about synthetic CV generation:

- **after** this patch is deployed
- and **after** you isolate the next summary/body contamination slice

Then you can ask Codex to generate a small fixture pack for:

- certifications
- projects
- hobbies
- affiliations
- additional information

  

  
  
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

  
  
roposer un plan très concret en 3 options:

1. “continuer heuristiques”
2. “hybride heuristiques + structured JSON”
3. “pivot quasi complet vers extraction structurée”

Et ma reco produit/tech à côté :

- **oui**, ajoute un download **Raw OCR Markdown**
- **oui**, ajoute aussi un download **Normalized JSON**
- **non**, ne pivote pas tout de suite tout le parser vers annotations/JSON
- **oui**, fais un POC plus tard sur une seule famille avec extraction structurée JSON  
    La bonne stratégie, selon moi, c’est :
- **ne pas tout réécrire d’un coup**
- lancer un **POC schema-first sur une famille**
- comparer au pipeline heuristique existant
- Les meilleures familles pour un POC:
- IDENTITY / CONTACT
- ou EDUCATION
- éventuellement LANGUAGES
- Pas encore EXPERIENCE complet, car c’est la famille la plus instable.

oui, vous pouvez passer progressivement vers OCR/layout + extraction structurée par schéma + validation métier