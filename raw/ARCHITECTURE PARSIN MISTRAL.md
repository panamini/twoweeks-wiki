
## Architecture cible et vérité de données

### 1. Vérité backend aujourd’hui

Le backend suit déjà la bonne architecture de fond :

- OCR
- extraction structurée guidée par schéma, par familles
- post-validation / normalisation
- mapping en sections applicatives

Autrement dit, le cœur fiable du système est :

- **extraction structurée par famille**
- puis **resume normalisé**
- puis **sections applicatives**

L’extraction texte heuristique seule ne doit plus être considérée comme la voie principale.

---

### 2. Vérité produit aujourd’hui

Dans le produit, la vérité pratique du rendu est :

- **`currentCv.sections[*].structuredContent`**

C’est ce que l’éditeur utilise réellement pour afficher le CV.

Donc, côté UI, la meilleure vérité actuelle n’est pas les tableaux top-level, mais bien les **sections structurées**.

---

### 3. Là où la confusion existe encore

Il reste une seconde représentation dans le flow frontend / Convex :

- `experience`
- `education`
- `skills`
- autres tableaux top-level similaires

Ces champs servent encore de compatibilité, d’export ou de convenience layer, mais ils peuvent diverger des sections si on les recalcule séparément.

Aujourd’hui, le problème n’est donc pas le backend structuré.  
Le problème est la coexistence de deux vérités :

- **vérité de rendu** = `sections`
- **vérité de compat / export** = top-level arrays parfois recalculés

C’est cette duplication qui crée les incohérences observées.

---

### 4. Source de vérité à adopter

La cible propre doit être simple :

- **quand `sections` existe et est valide, `sections[*].structuredContent` devient la vérité canonique produit**

À partir de là :

- le rendu éditeur doit dériver de `sections`
- le JSON copié / exporté doit dériver de `sections`
- les tableaux top-level doivent devenir des **vues dérivées** de `sections`
- les fallbacks heuristiques ne doivent intervenir **que si `sections` est absent ou inutilisable**

---

### 5. Ce qui doit rester du fallback seulement

Ces mécanismes doivent rester des solutions de secours, pas la vérité principale :

- canonicalisation legacy purement heuristique
- reconstruction indépendante des top-level arrays depuis `rawText`
- re-canonicalisation frontend qui peut diverger de `sections`

Ils sont utiles pour la robustesse de transition, mais pas comme modèle cible.

---

### 6. Familles déjà suffisamment mûres

Le système est déjà assez solide sur les familles principales :

- profile / contact
- summary
- experience
- education
- certifications
- skills
- languages
- projects

Ce sont les familles qui doivent guider la stabilisation du produit.

---

### 7. Familles encore moins “first-class”

Certaines familles existent déjà structurellement, mais ne sont pas encore traitées partout comme sections produit de premier rang :

- awards
- publications
- volunteering
- autres sections libres / text sections

Ce n’est pas un défaut d’architecture.  
C’est simplement un sujet de phase de produit plus tardive.

---

### 8. Roadmap logique

#### Phase 1 — stabiliser la vérité

Aligner complètement :

- sections rendues
- payload normalisé copié / exporté

autour de `sections[*].structuredContent`.

#### Phase 2 — réduire la duplication

Supprimer progressivement les cas où les tableaux top-level sont recalculés indépendamment alors que `sections` existe déjà.

#### Phase 3 — décider le support produit par famille

Choisir explicitement quelles familles méritent :

- une section UI dédiée
- ou un rendu générique de type text block / other section

---

### 9. Ce qu’il ne faut pas faire

- ne pas abandonner l’architecture structurée par familles
- ne pas revenir à un parsing principalement heuristique / text-only
- ne pas laisser frontend et backend fabriquer chacun leur propre vérité durablement

---

## Principe directeur

**Quand elles existent et sont valides, les sections structurées issues du backend doivent devenir la vérité canonique du produit ; tout le reste doit être une vue dérivée ou un fallback.**