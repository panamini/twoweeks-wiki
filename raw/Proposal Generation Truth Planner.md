

## Scratchpad Note — Safety, Evidence, and Recruiter-Readiness

### Status

**Current phase:** safety architecture repaired.  
**Next phase:** semantic truth planner in shadow mode.  
**Do not make planner live yet.**

The current proposal / cover-letter engine now has the right safety backbone:

```
LLM draft→ deterministic risk detector→ constrained repair pass→ deterministic verifier→ fallback / fail-closed
```

The next step is not more prompt stacking.  
The next step is a **structured truth plan** that defines what the writer is allowed to say before it writes.

---

# Why this exists

Two Weeks generates proposals, cover letters, and application messages.

The product bar:

- ATS-friendly
- recruiter-ready
- source-backed
- short enough to use
- specific enough to matter
- honest about gaps
- no invented experience
- no invented tools
- no invented metrics
- no fake seniority
- no fake company-value alignment
- no unsupported job-keyword stuffing

The long-term system should feel like elite business software, not a prompt pile.

The model can write.  
The code must enforce truth.  
The harness must measure regressions.

---

# Current completed layer

We already repaired the safety layer:

```
Draft→ detect unsafe claims→ repair once→ verify→ fallback if still unsafe
```

This fixed or improved:

- weak SEO overclaims
- no-context personal claims
- company-praise drift
- unsupported mentoring / leadership risk
- fallback copy leaking internal “no candidate background” phrasing
- repeated no-context filler

This layer should be committed separately before planner work begins.

---

# Next layer: semantic truth planner

The planner should answer:

```
What is true?What can we safely claim?What must we not claim?What is missing?What writing mode should the proposal use?
```

It should **not** write the proposal.

It should create a compact, typed contract:

```
candidate + job inputs→ truth plan→ current writer→ verifier→ repair/fallback→ harness report
```

The planner is a **truth boundary**, not a paragraph outline.

---

# Core principle

Bad direction:

```
Planner writes a better prompt.Writer follows it blindly.
```

Good direction:

```
Planner defines the legal claim space.Writer writes inside that space.Verifier checks final output.Harness records plan vs output.
```

---

# ProposalTruthPlanV1

```
export type ProposalTruthPlanV1 = {  planVersion: "proposal_truth_plan_v1"  writingMode: "normal" | "adjacent_only" | "no_context_safe"  modeConfidence: "high" | "medium" | "low"  writerPolicy:    | "normal_writer"    | "constrained_writer"    | "bypass_writer_use_fallback"  jobPriorities: Array<{    id: string    requirement: string    importance: "critical" | "important" | "nice_to_have"    sourceText: string  }>  candidateFacts: Array<{    id: string    fact: string    source:      | "candidate_summary"      | "candidate_skill"      | "candidate_experience"      | "candidate_achievement"      | "candidate_project"    sourceText: string  }>  allowedClaims: Array<{    claim: string    factIds: string[]    strength: "direct" | "soft" | "adjacent"    claimType:      | "candidate_fact"      | "role_interest"      | "job_surface"      | "discussion_forward"      | "collaboration_area"  }>  blockedClaims: Array<{    claim: string    reason:      | "no_candidate_evidence"      | "job_description_only"      | "missing_requirement"      | "overstated_seniority"      | "unsupported_tool"      | "unsupported_metric"      | "unsupported_leadership"      | "company_praise"      | "no_context_personal_claim"  }>  missingCriticalRequirements: Array<{    requirement: string    sourceText: string    safeTreatment:      | "omit"      | "frame_as_gap"      | "collaboration_area"      | "refer_to_specialist"  }>}
```

---

# Important schema rules

## 1. `factIds: []` is allowed, but only for soft claims

Allowed:

```
{  claim: "Interest in the Sales Assistant role",  factIds: [],  strength: "soft",  claimType: "role_interest"}
```

Allowed:

```
{  claim: "The role centers on follow-up, records, and professional communication",  factIds: [],  strength: "soft",  claimType: "job_surface"}
```

Not allowed:

```
{  claim: "I communicate clearly with customers",  factIds: [],  strength: "direct",  claimType: "candidate_fact"}
```

Rule:

```
No direct candidate claim can have empty factIds.
```

---

## 2. `writingMode` stays simple

Keep the mode enum small:

```
"normal" | "adjacent_only" | "no_context_safe"
```

Do not add too many modes yet.

Use separate fields for confidence and behavior:

```
modeConfidence: "high" | "medium" | "low"writerPolicy: "normal_writer" | "constrained_writer" | "bypass_writer_use_fallback"
```

This avoids bloating `writingMode`.

---

## 3. `writerPolicy` is not live yet

For now, `writerPolicy` is recorded in shadow reports only.

Eventually:

|writerPolicy|Meaning|
|---|---|
|`normal_writer`|Enough candidate proof. Let writer draft normally within safety rules.|
|`constrained_writer`|Some proof, but risk exists. Writer must stay close to allowed claims.|
|`bypass_writer_use_fallback`|No useful candidate evidence. Skip creative writing and use safe fallback.|

But in the first implementation, **do not let this change production output**.

---

# Writing modes

## `normal`

Use when candidate evidence directly supports the job.

Example:

```
Senior Frontend EngineerCandidate has React, TypeScript, design systems, performance optimization, A/B testing.
```

Allowed:

- React / TypeScript experience
- design system migration
- performance improvement
- product/design collaboration
- provided metrics

Blocked:

- unsupported mentoring
- people management
- backend ownership
- mobile development
- unsupported analytics instrumentation

---

## `adjacent_only`

Use when candidate evidence is related but not enough to claim direct expertise.

Example:

```
Technical SEO jobCandidate has frontend, landing pages, conversion optimization.
```

Allowed:

- frontend implementation
- landing-page structure
- conversion-aware page improvements
- collaboration after SEO specialist defines recommendations

Blocked:

- technical SEO specialist
- schema strategy
- crawl diagnostics
- indexing fixes
- internal-linking recommendations
- canonical tags
- crawlability fixes

Missing requirements:

- indexing
- schema
- crawl diagnostics
- internal linking

Safe treatment:

```
refer_to_specialistcollaboration_areaframe_as_gap
```

---

## `no_context_safe`

Use when no candidate context exists.

Allowed:

- interest in the role
- role work-surface summary
- willingness to discuss the team process

Blocked:

- experience
- skills
- traits
- habits
- abilities
- work style
- confidence
- comfort
- strengths
- “how I approach”
- “my attention to detail”
- “I prioritize”
- “I value”
- “I make sure”

Example safe fallback:

```
I’m interested in the Sales Assistant role. The work appears centered on follow-up coordination, organized records, and professional communication with prospects and customers. I’d welcome the chance to learn more about the team’s process and discuss the role.
```

---

# Example truth plan: weak SEO

```
{  planVersion: "proposal_truth_plan_v1",  writingMode: "adjacent_only",  modeConfidence: "high",  writerPolicy: "constrained_writer",  jobPriorities: [    {      id: "job_technical_seo",      requirement: "Technical SEO audit for indexing, schema, crawl diagnostics, and internal linking",      importance: "critical",      sourceText: "audit and improve technical SEO for a large marketplace site, including indexing, schema, crawl diagnostics, and internal linking recommendations"    }  ],  candidateFacts: [    {      id: "fact_frontend",      fact: "Frontend-focused freelance designer-developer",      source: "candidate_summary",      sourceText: "Frontend-focused freelance designer-developer with conversion and landing page experience"    },    {      id: "fact_landing_pages",      fact: "Landing page and conversion optimization experience",      source: "candidate_skill",      sourceText: "Landing Pages, Conversion Optimization"    }  ],  allowedClaims: [    {      claim: "Can support frontend implementation after a technical SEO specialist defines recommendations",      factIds: ["fact_frontend", "fact_landing_pages"],      strength: "adjacent",      claimType: "collaboration_area"    },    {      claim: "Can improve landing-page structure and conversion-aware page presentation",      factIds: ["fact_landing_pages"],      strength: "adjacent",      claimType: "candidate_fact"    }  ],  blockedClaims: [    {      claim: "technical SEO specialist",      reason: "no_candidate_evidence"    },    {      claim: "indexing fixes",      reason: "job_description_only"    },    {      claim: "schema strategy",      reason: "job_description_only"    },    {      claim: "crawl diagnostics",      reason: "job_description_only"    },    {      claim: "internal-linking recommendations",      reason: "job_description_only"    }  ],  missingCriticalRequirements: [    {      requirement: "indexing",      sourceText: "including indexing",      safeTreatment: "refer_to_specialist"    },    {      requirement: "schema",      sourceText: "including schema",      safeTreatment: "refer_to_specialist"    },    {      requirement: "crawl diagnostics",      sourceText: "including crawl diagnostics",      safeTreatment: "refer_to_specialist"    },    {      requirement: "internal linking",      sourceText: "internal linking recommendations",      safeTreatment: "refer_to_specialist"    }  ]}
```

---

# Example truth plan: no-context Sales Assistant

```
{  planVersion: "proposal_truth_plan_v1",  writingMode: "no_context_safe",  modeConfidence: "high",  writerPolicy: "bypass_writer_use_fallback",  jobPriorities: [    {      id: "job_followup",      requirement: "coordinate follow-up",      importance: "important",      sourceText: "coordinate follow-up"    },    {      id: "job_records",      requirement: "keep records organized",      importance: "important",      sourceText: "keep records organized"    },    {      id: "job_customer_comm",      requirement: "communicate professionally with prospects and customers",      importance: "important",      sourceText: "communicate professionally with prospects and customers"    }  ],  candidateFacts: [],  allowedClaims: [    {      claim: "Interest in the Sales Assistant role",      factIds: [],      strength: "soft",      claimType: "role_interest"    },    {      claim: "The role centers on follow-up, organized records, and professional communication",      factIds: [],      strength: "soft",      claimType: "job_surface"    },    {      claim: "Willingness to discuss the team process",      factIds: [],      strength: "soft",      claimType: "discussion_forward"    }  ],  blockedClaims: [    {      claim: "prior sales experience",      reason: "no_context_personal_claim"    },    {      claim: "CRM expertise",      reason: "no_candidate_evidence"    },    {      claim: "quota ownership",      reason: "no_candidate_evidence"    },    {      claim: "how I approach new responsibilities",      reason: "no_context_personal_claim"    },    {      claim: "attention to detail",      reason: "no_context_personal_claim"    },    {      claim: "confidence handling customer communication",      reason: "no_context_personal_claim"    }  ],  missingCriticalRequirements: [    {      requirement: "all candidate-specific qualifications",      sourceText: "",      safeTreatment: "omit"    }  ]}
```

---

# Example truth plan: strong frontend

```
{  planVersion: "proposal_truth_plan_v1",  writingMode: "normal",  modeConfidence: "high",  writerPolicy: "normal_writer",  jobPriorities: [    {      id: "job_react_ts",      requirement: "React and TypeScript development",      importance: "critical",      sourceText: "lead React and TypeScript development"    },    {      id: "job_design_systems",      requirement: "Reusable UI systems",      importance: "critical",      sourceText: "building reusable UI systems"    },    {      id: "job_performance",      requirement: "Performance improvement",      importance: "important",      sourceText: "improving performance"    },    {      id: "job_mentoring",      requirement: "Mentoring junior engineers",      importance: "important",      sourceText: "mentoring junior engineers"    }  ],  candidateFacts: [    {      id: "fact_react_ts",      fact: "Frontend engineer focused on React and TypeScript",      source: "candidate_summary",      sourceText: "Frontend engineer focused on React, TypeScript, design systems, and product-facing web apps"    },    {      id: "fact_design_system",      fact: "Led a design system migration used across 4 product squads",      source: "candidate_experience",      sourceText: "Led a design system migration used across 4 product squads"    },    {      id: "fact_performance",      fact: "Reduced page load time by 28 percent",      source: "candidate_experience",      sourceText: "Reduced page load time by 28 percent through bundle and rendering optimizations"    },    {      id: "fact_experimentation",      fact: "Improved signup conversion by 11 percent through UI experiments",      source: "candidate_achievement",      sourceText: "Improved signup conversion by 11 percent after iterative UI experiments"    }  ],  allowedClaims: [    {      claim: "React and TypeScript frontend experience",      factIds: ["fact_react_ts"],      strength: "direct",      claimType: "candidate_fact"    },    {      claim: "Design system migration leadership",      factIds: ["fact_design_system"],      strength: "direct",      claimType: "candidate_fact"    },    {      claim: "Performance optimization with a 28 percent page-load improvement",      factIds: ["fact_performance"],      strength: "direct",      claimType: "candidate_fact"    },    {      claim: "Experimentation and conversion improvement",      factIds: ["fact_experimentation"],      strength: "direct",      claimType: "candidate_fact"    }  ],  blockedClaims: [    {      claim: "people management",      reason: "unsupported_leadership"    },    {      claim: "mentoring junior engineers",      reason: "unsupported_leadership"    },    {      claim: "backend ownership",      reason: "unsupported_tool"    },    {      claim: "mobile development",      reason: "unsupported_tool"    }  ],  missingCriticalRequirements: [    {      requirement: "mentoring junior engineers",      sourceText: "mentoring junior engineers",      safeTreatment: "omit"    },    {      requirement: "large-scale analytics instrumentation",      sourceText: "analytics instrumentation",      safeTreatment: "frame_as_gap"    }  ]}
```

---

# Phase plan

## Phase 0 — current safety branch

Status: done / commit separately.

Scope:

```
detectrepairverifyfallback
```

Do not mix semantic planner into this commit.

---

## Phase 1 — planner shadow contract

Goal:

```
Build truthPlan.Add it to harness / benchmark reports.Do not change final generated output.
```

Allowed:

- create `ProposalTruthPlanV1`
- build deterministic planner function
- classify known fixtures
- include `truthPlan` in reports
- add tests

Forbidden:

- no live planner
- no prompt rewrite
- no model routing change
- no length change
- no GPT
- no live APIs
- no UI work

---

## Phase 2 — planner assertions

Add regression tests for:

```
weak SEO → adjacent_onlyno-context support → no_context_safeno-context generalist → no_context_safestrong frontend → normaladjacent admin → adjacent_only or normal with explicit gaps
```

Also assert:

```
direct claims require factIdsno-context soft claims may use factIds: []blocked claims include known risk familiesmissing requirements are listedtruthPlan appears in harness outputfinal output remains unchanged
```

---

## Phase 3 — writer uses plan in controlled mode

Only after shadow plan is stable.

Writer rules:

```
use allowedClaimsavoid blockedClaimstreat missingCriticalRequirements according to safeTreatmentrespect writingMode
```

Still keep deterministic verifier after the writer.

The planner does not replace enforcement.

---

## Phase 4 — recruiter-readiness tuning

After safety and planner stability:

```
Improve whether safe outputs are actually good.
```

Targets:

- less robotic no-context copy
- stronger evidence flow
- less corporate filler
- better application-message rhythm
- better weak-match honesty
- better proposal-specific structure
- fewer defensive gap phrases
- more recruiter/client usefulness

This is not safety work.  
This is quality tuning.

---

# Harness expectations

The harness should eventually report:

```
truthPlanrawDraftriskFindingsrepairAttemptedrepairedOutputfinalFindingsfinalOutputmanualVerdict
```

For every fixture, reviewers should be able to answer:

```
What did the planner allow?What did the planner block?Did the draft violate the plan?Did repair fix it?Did final output stay inside the truth plan?Was the final output actually usable?
```

---

# Key fixture expectations

## Weak SEO

Expected:

```
writingMode: adjacent_only
```

Must block:

- technical SEO specialist
- indexing fixes
- schema strategy
- schema implementation
- crawl diagnostics
- internal-linking recommendations
- canonical tags
- crawlability fixes

Allowed:

- frontend execution
- landing-page structure
- conversion-aware page improvements
- collaboration after SEO specialist recommendations

---

## No-context Sales Assistant

Expected:

```
writingMode: no_context_safewriterPolicy: bypass_writer_use_fallbackcandidateFacts: []
```

Allowed:

- interest in role
- role work surface
- willingness to discuss process

Blocked:

- sales experience
- CRM expertise
- quota ownership
- customer-service experience
- confidence
- comfort
- attention to detail
- work style
- habits
- abilities
- “how I approach”

---

## Strong frontend

Expected:

```
writingMode: normalwriterPolicy: normal_writer
```

Allowed direct claims:

- React
- TypeScript
- design system migration
- 28% page-load improvement
- A/B testing / experimentation if sourced
- 11% signup conversion improvement

Blocked unless sourced:

- mentoring
- people management
- staff-level leadership
- backend ownership
- mobile development
- large-scale analytics instrumentation

---

## Adjacent admin

Expected:

```
writingMode: adjacent_only
```

Or:

```
writingMode: normalmissingCriticalRequirements: vendor/procurement
```

Prefer `adjacent_only` if vendor/procurement is central and unsupported.

Allowed:

- coordination
- documentation
- stakeholder communication
- process follow-through

Blocked unless sourced:

- vendor procurement ownership
- office management
- scheduling ownership if not directly sourced
- direct vendor handling if not sourced

---

# Open decisions

## 1. Should `application-adjacent-admin` be `normal` or `adjacent_only`?

Current recommendation:

```
adjacent_only if vendor/procurement is central.normal with gaps if coordination/documentation is enough for role fit.
```

Keep this as a test discussion, not a hard product decision yet.

---

## 2. When should `writerPolicy` bypass the writer?

Initial recommendation:

```
Only in no_context_safe mode when candidateFacts is empty and allowedClaims are purely generic.
```

Do not use bypass for weak-match cases with some candidate evidence.

---

## 3. Should planner be LLM-based or deterministic?

Initial recommendation:

```
Mostly deterministic for Phase 1.
```

Reason:

- no live API needed
- easier tests
- stable fixture assertions
- lower regression risk

Later, LLM planner can be tested against deterministic planner.

---

# Definition of done for Phase 1

Phase 1 is done when:

```
ProposalTruthPlanV1 exists.buildProposalTruthPlanV1(input) exists.truthPlan appears in benchmark/harness output.Known fixtures classify correctly.No final generated output changes.semantic_planner_live remains disabled.No live APIs required.Tests prove schema and fixture expectations.
```

---

# Definition of done for Phase 2

Phase 2 is done when:

```
Planner assertions are stable.truthPlan catches known risk families.Direct claims require factIds.No-context soft claims allow factIds: [] safely.Weak SEO is adjacent_only.No-context is no_context_safe.Strong frontend is normal.Harness shows planner-vs-output comparison.
```

---

# Things not to do

Do not:

```
make planner live nowturn planner into paragraph outlinereplace verifier with planneradd huge enterprise schema too earlyadd broad prompt ruleschange model routingchange length behaviorrun GPT benchmark before parity is provenenable semantic_planner_liveenable criteria_audit_livemix this with UI work
```

---

# Best next Codex task

```
Proposal generation: semantic planner shadow contract
```

Scope:

```
typed schemadeterministic plannershadow harness reportfixture assertionsno production output changes
```

Core instruction:

```
Build the truth plan. Show it in reports. Do not let it write yet.
```

---

# Final architecture target

```
Candidate + job inputs→ ProposalTruthPlanV1→ LLM writer→ deterministic detector→ constrained repair→ deterministic verifier→ fallback / fail-closed→ harness report→ production trace feedback loop
```

The planner defines the truth space.  
The writer writes inside it.  
The verifier enforces it.  
The harness compounds learning.