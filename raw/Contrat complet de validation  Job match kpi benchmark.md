---
aliases:
  - Contrat complet de validation  Job match kpi/benchmark
kpi:
benchmark:
---
Oui. Voilà le **contrat complet de validation** qu’on a conçu pour dire :

> **“Le système est cohérent. Il fait ce qu’on veut. Il peut être approuvé.”**

Le but n’est pas de prouver que le match est “objectivement vrai” comme un recruteur. Le but est de prouver que le système est un **indicateur fiable d’intérêt utilisateur** pour un job scrapé case-by-case.

---

# 0. Définition produit

## Le système n’est pas

```txt
ATS.
Recruiter.
Hiring decision engine.
Keyword checklist.
```

## Le système est

```txt
User-facing opportunity reviewer.
```

Il répond à :

```txt
Cette offre mérite-t-elle l’attention de cet utilisateur ?
```

Pas à :

```txt
Ce candidat doit-il être embauché ?
```

---

# 1. Contrat fonctionnel

Pour chaque job scrapé, avec un CV/profil attaché, le système doit produire :

```ts
type MatchReview = {
  tier: "strong" | "partial" | "weak" | "unknown";

  verdict:
    | "strong_lead"
    | "possible_lead"
    | "probably_skip"
    | "not_enough_signal";

  score: number; // 0-100

  one_liner: string;

  why_this_may_interest_you: string[]; // max 3

  watch_out: string[]; // max 2

  suggested_next_step:
    | "apply"
    | "apply_if_requirement_true"
    | "skip"
    | "review_manually";
};
```

## UI contract

L’utilisateur doit voir vite :

```txt
Match
Possible lead · 59%

Why this may interest you
Security experience overlaps.
Report writing overlaps.
License mostly matches.

Watch out
Driver’s license unclear.
Customer service evidence is light.

Next
Apply if true
```

Pas :

```txt
valid
ability
preferred
more
maps to profile evidence: [raw resume dump]
```

---

# 2. Architecture contract

Le pipeline valide est :

```txt
Job scraped
→ job normalized / LLM extraction
→ structured scorer
→ matchReview projection
→ compact user-facing UI
```

Pour cette phase, on a choisi :

```txt
LLM extracts job.
Deterministic structured scorer evaluates profile/job overlap.
MatchReview formats the result.
```

Pas encore :

```txt
LLM directly judges CV + job together.
```

Mistral recommande les sorties structurées quand on veut une forme JSON stable, et précise que les custom structured outputs permettent d’imposer un schéma plus fiable qu’un simple JSON libre. C’est aligné avec notre choix de contrats stricts et validators. ([Mistral AI Documentation](https://docs.mistral.ai/capabilities/structured-output/structured_output_overview/?utm_source=chatgpt.com "Mistral Docs"))

---

# 3. Contrat de scoring

## Tiers

```txt
strong  = excellent / strong lead
partial = possible lead
weak    = probably skip or weak interest
unknown = no enough signal / unavailable
```

## Calibration minimale

```txt
90–100  strong lead
75–89   strong lead
55–74   possible lead / partial
35–54   weak
1–34    probably skip
0       only clear no-signal, unrelated, or unusable input
```

## Rule critique ajoutée

Si :

```txt
role-family/title overlap exists
+ at least 2 positive scorable overlaps
+ no hard_gate_missing
```

Alors :

```txt
score floor = 55
tier = partial
verdict = possible_lead
```

Ça empêche :

```txt
Security Guard mostly overlaps.
Probably skip.
```

ou :

```txt
Teacher overlaps.
Probably skip.
```

---

# 4. Contrat d’évidence

Chaque verdict doit être cohérent avec l’évidence affichée.

## Acceptable

```txt
Possible lead · 59%
Security experience overlaps.
Report writing overlaps.
Driver’s license unclear.
```

## Non acceptable

```txt
Probably skip · 34%
Security Guard mostly overlaps.
License mostly matches.
```

## Règle d’or

```txt
Positive evidence and verdict cannot contradict each other.
```

---

# 5. Contrat des credentials

Les credentials sont le point sensible.

## Required credential

Si l’offre dit clairement :

```txt
license required
certification required
valid state credential required
```

et le profil ne le montre pas :

```txt
important risk / hard gate possible
score capped or lowered
do not infer credential
```

## Preferred credential

Si l’offre dit :

```txt
license preferred
certification preferred
nice to have
```

alors :

```txt
watch_out
not blocker
not 0%
```

## Unknown credential

Si c’est flou :

```txt
evidence is light
credential unclear
```

Pas :

```txt
missing = fail
```

---

# 6. Contrat anti-keyword

Le système est invalide s’il fait ça :

```txt
Missing:
valid
ability
preferred
lift
more

Score: 0%
```

## Generic fragments interdits

Ne doivent jamais apparaître comme requirements visibles ou missing bloquants :

```txt
valid
ability
preferred
more
lift
strong
excellent
responsible
motivated
fast-paced
```

Le système peut les ignorer, les fusionner, ou les convertir en contrainte utile seulement si le contexte est clair.

---

# 7. Contrat de copy visible

## `one_liner`

```txt
max 120 chars
product-facing
no debug phrasing
no contradiction with verdict
```

## `why_this_may_interest_you`

```txt
max 3 items
max 80 chars each
short user-facing phrases
```

Bon :

```txt
Security experience overlaps.
Report writing overlaps.
Customer-facing work is relevant.
```

Mauvais :

```txt
Basic computer knowledge maps to profile evidence: Responsible for completing reports by recording...
```

## `watch_out`

```txt
max 2 items
max 100 chars each
```

Bon :

```txt
Driver’s license unclear.
Customer service evidence is light.
```

Mauvais :

```txt
No concrete profile evidence was strong enough to classify as a match or a real gap.
```

---

# 8. Contrat privacy / safety

Le `matchReview` visible ne doit jamais afficher :

```txt
email
phone number
UUID
raw resume paragraph
full CV blob
internal debug phrase
source blob
```

Interdit :

```txt
# JESSICA CLAIRE - resumesample@example.com - (555)...
```

Autorisé :

```txt
Teaching background overlaps.
Degree requirement mostly matches.
```

---

# 9. Benchmark dataset

Pour approuver le système, il faut une mini-suite benchmark locale.

## Taille minimum

```txt
20–30 fixtures = minimum merge confidence
50–100 fixtures = vrai benchmark interne
200+ fixtures = calibration sérieuse
```

Mistral recommande d’évaluer sur datasets, avec critères et sorties structurées ; leurs docs d’évaluation montrent des benchmarks avec métriques comme accuracy, et leur système de Judges recommande de tester d’abord sur 10–20 records et d’inspecter chaque jugement avant de scaler. ([Mistral AI Documentation](https://docs.mistral.ai/cookbooks/mistral-evaluation-evaluation?utm_source=chatgpt.com "How to evaluate LLMs - Mistral AI Cookbook"))

---

# 10. Benchmark cases obligatoires

## A. Positive semantic match

```txt
Security/protection CV
↔ Security Guard job
Expected: partial/strong, not weak/skip
```

```txt
Teacher CV
↔ Teacher job
Expected: partial unless required credential missing hard gate
```

```txt
Retail/customer service CV
↔ Sales associate job
Expected: partial/strong
```

```txt
Warehouse/logistics CV
↔ Inventory/operations job
Expected: partial/strong
```

## B. Credential caution

```txt
Security CV
↔ Security job with license preferred
Expected: possible_lead, watch_out, not blocker
```

## C. Credential hard gate

```txt
Unlicensed profile
↔ Job requires state license
Expected: lowered/capped, credential watch_out/hard gate
```

## D. Negative unrelated

```txt
Security CV
↔ Frontend engineer job
Expected: probably_skip
```

```txt
Teacher CV
↔ Heavy machinery mechanic job
Expected: probably_skip
```

## E. Generic fragment noise

```txt
Job extraction contains valid / ability / preferred / more
Expected: no visible missing requirement from those fragments
```

## F. No profile / no resume

```txt
No attached CV/profile evidence
Expected: not_enough_signal or fallback
Not: Probably skip · 0% as a real judgment
```

## G. Privacy leak

```txt
Profile evidence contains email/phone/raw CV
Expected: never visible in matchReview
```

---

# 11. KPI d’approbation

## KPI 1 — False-zero rate

Le système ne doit pas mettre 0 ou skip quand le match est sémantiquement évident.

```txt
Target:
0 false-zero on gold obvious-positive fixtures.
```

Exemples :

```txt
Protection Guard ↔ Security Guard
Teacher ↔ Teacher
Retail Associate ↔ Store Associate
```

## KPI 2 — Contradiction rate

Le verdict ne doit pas contredire les raisons affichées.

```txt
Target:
0 critical contradiction.
≤ 5% minor contradiction on benchmark.
```

Critical contradiction :

```txt
Probably skip
+ “Security Guard mostly overlaps”
+ no blocking gate
```

## KPI 3 — Credential safety

Le système ne doit pas halluciner un credential.

```txt
Target:
0 inferred required credentials.
0 required-license-as-match if absent.
```

## KPI 4 — Preferred-not-blocking

Un requirement `preferred` ne doit pas bloquer.

```txt
Target:
≥ 95% preferred credentials become watch_out, not blocker.
```

## KPI 5 — Negative precision

Les jobs vraiment unrelated doivent rester bas.

```txt
Target:
≥ 90% unrelated fixtures = probably_skip / weak.
```

## KPI 6 — Positive recall

Les bons jobs évidents doivent passer au moins `partial`.

```txt
Target:
≥ 90% obvious semantic matches = partial or strong.
```

## KPI 7 — Copy safety

Aucune fuite de raw evidence.

```txt
Target:
0 emails visible.
0 phone numbers visible.
0 UUIDs visible.
0 raw CV paragraphs visible.
0 “maps to profile evidence”.
```

## KPI 8 — UI usefulness

L’utilisateur doit comprendre en moins de 5 secondes :

```txt
Is this relevant?
Why?
What should I do next?
```

Tu avais déjà cette direction Jobs Page v2 : **Time to Decision < 5 seconds**. C’est le KPI produit principal.

UX metrics classiques incluent task success, time on task, error rate et satisfaction ; ici ton équivalent produit est “time to decision” + “did the user take the right next action.” Nielsen Norman Group parle aussi de mesurer l’expérience avec des métriques comportementales et attitudinales plutôt qu’un simple feeling subjectif. ([Mistral AI Documentation](https://docs.mistral.ai/cookbooks/mistral-evaluation-evaluation?utm_source=chatgpt.com "How to evaluate LLMs - Mistral AI Cookbook"))

---

# 12. Seuils d’approbation

## Mergeable internal

```txt
✅ All unit tests pass
✅ Security false-zero fixed
✅ No raw evidence leak
✅ No obvious contradiction in screenshots
✅ Unrelated negative still low
✅ Required credential not hallucinated
```

## Internal beta valid

```txt
Benchmark 30+ fixtures:
- positive recall ≥ 85%
- negative precision ≥ 85%
- contradiction rate = 0 critical
- credential hallucination = 0
- PII leak = 0
```

## Public-ready

```txt
Benchmark 100+ fixtures:
- positive recall ≥ 90%
- negative precision ≥ 90%
- false-zero = 0 on obvious positives
- credential hallucination = 0
- PII leak = 0
- time to decision median < 5 sec
- user “this makes sense” rating ≥ 80%
```

---

# 13. Human review rubric

Chaque fixture doit avoir un expected label :

```ts
type ExpectedMatchLabel =
  | "strong_recommendation"
  | "possible_recommendation"
  | "weak_recommendation"
  | "skip"
  | "not_enough_signal"
  | "dangerous_overmatch";
```

Et un reviewer humain note :

```txt
1. Verdict correct?
2. Score range acceptable?
3. Reasons support verdict?
4. Watch-outs are fair?
5. No hallucinated credential?
6. No raw/PII leak?
7. User could decide in <5 sec?
```

---

# 14. Eval table contract

Le benchmark doit sortir un tableau comme ça :

|Case|Expected|Actual|Pass|Failure type|
|---|---|---|---|---|
|security_guard_positive|possible+|possible|✅|—|
|security_license_required|weak/possible capped|possible capped|✅|—|
|teacher_missing_state_credential|possible/weak|possible|✅|—|
|frontend_unrelated|skip|skip|✅|—|
|generic_fragments|no visible junk|no junk|✅|—|
|no_resume|not_enough_signal|fallback|✅|—|

Failure types :

```txt
false_zero
dangerous_overmatch
credential_hallucination
preferred_as_blocker
generic_fragment_leak
raw_evidence_leak
verdict_reason_contradiction
bad_next_step
```

---

# 15. Final approval checklist

Le système est valide si :

```txt
[ ] same-family jobs do not get false-zero
[ ] unrelated jobs still get probably_skip
[ ] preferred credentials are watch-outs
[ ] required credentials are not hallucinated
[ ] role-family + 2 positive signals floors to partial
[ ] no hard gate missing bypass
[ ] no raw evidence visible
[ ] no PII visible
[ ] no debug phrasing visible
[ ] one_liner is short and useful
[ ] reasons are max 3
[ ] watch_outs are max 2
[ ] fallback works when no profile/no extraction
[ ] UI makes decision clear in <5 seconds
[ ] tests cover security, teacher, retail/ops, unrelated, credential, generic noise, no-profile, PII
```

---

# 16. La phrase d’approbation

Quand tout passe, tu peux dire :

```txt
The match system is valid for internal beta.

It is not an ATS and does not claim hiring accuracy.
It reliably acts as a user-facing opportunity indicator:
- it catches obvious semantic matches,
- avoids false-zero keyword failures,
- preserves credential safety,
- avoids raw evidence/PII leaks,
- explains the result compactly,
- and helps the user decide whether to act.
```

En version Twoweeks :

```txt
MATCH. USEFUL.
Same lane shows.
Noise stays out.
Credentials stay honest.
Decision under five.
```