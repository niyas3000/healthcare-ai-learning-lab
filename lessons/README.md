# Lessons

Each lesson is designed for a 60–120 minute practice block. Do the exercise, run the related tests, write down one architectural decision, and record one unresolved risk.

## 00 — Orientation, safety, and scope

**Objective.** Establish synthetic-data rules, intended users, prohibited uses, and a risk register before writing code.

**Practice.** Write a one-page intended-use statement for a learning-only patient-summary tool. Add three prohibited uses, three human-review points, and a rollback condition. Compare your answer with [`docs/safety-and-governance.md`](../docs/safety-and-governance.md).

**Evidence.** A completed scope statement and a test that asserts the output includes an educational disclaimer.

**Reflection.** Which failure would create the greatest harm: a wrong summary, an unavailable service, or an unauthorized disclosure? Why?

## 01 — Clinical systems and ecosystem mapping

**Objective.** Distinguish systems of capture, exchange, record, and intelligence.

**Practice.** Draw a context diagram for an outpatient journey involving PAS, EHR, LIS, HIE, MPI, terminology service, CDR, and a patient portal. Mark where HL7 v2, FHIR, CSV, or DICOM may appear and where normalization occurs.

**Evidence.** A Mermaid diagram and a table of system ownership, source-of-truth responsibility, and failure mode.

**Reflection.** Which systems may remain locally autonomous, and which shared services must enforce national consistency?

## 02 — FHIR foundations

**Objective.** Understand resource identity, references, status, subject links, and provenance.

**Practice.** Run `validate` and `quality` on `data/sample_fhir/bundle.json`. Add one valid Observation and one invalid Observation, then explain every finding.

**Evidence.** Passing tests plus a resource profile table describing Patient, Encounter, Observation, Condition, and DiagnosticReport.

**Reflection.** What information is lost when a structured observation is reduced to plain text?

## 03 — Legacy integration at the boundary

**Objective.** Keep legacy transformation at the integration boundary rather than leaking vendor formats into downstream services.

**Practice.** Create a mapping table from a fictional HL7 v2 ORU observation to a FHIR Observation. Identify message segments, source identifiers, status, coding, value, units, and timestamps. Do not use real messages or real codes outside official references.

**Evidence.** Mapping table, rejection rules, and a replay/idempotency note.

**Reflection.** How would you detect a duplicate message versus a corrected result?

## 04 — Terminology and semantic interoperability

**Objective.** Assign appropriate roles to SNOMED CT, LOINC, ICD, and RxNorm, and understand that codes require governed context.

**Practice.** For five fictional clinical concepts, specify the intended terminology domain, version, source value, target value, and mapping confidence. Mark any concept that requires a terminology-server lookup rather than a guess.

**Evidence.** A terminology decision log and a policy for unmapped or deprecated concepts.

**Reflection.** Why is a syntactically valid code not automatically semantically safe?

## 05 — Data quality, identity, and consent

**Objective.** Detect duplicates, dangling references, missing identifiers, unsafe joins, and missing purpose-of-use.

**Practice.** Modify the fixture to add a duplicate Patient identifier, a dangling subject reference, and a second local identifier. Run the tests and document how an MPI would resolve or quarantine each case.

**Evidence.** Quality report, quarantine policy, and a minimal consent/purpose-of-use matrix.

**Reflection.** Which data-quality issue should block an AI response entirely?

## 06 — Retrieval and AI safety

**Objective.** Design a retrieval boundary that returns only authorized, relevant, provenance-preserving context.

**Practice.** Implement a mock retriever that filters documents by patient, purpose-of-use, consent status, and source trust. Add a test for prompt injection in a retrieved note and a test that rejects missing provenance.

**Evidence.** Retrieval contract, threat cases, and a refusal example.

**Reflection.** What should the system say when the user asks for a conclusion that the available evidence does not support?

## 07 — Evaluation and reproducibility

**Objective.** Evaluate groundedness, citation coverage, refusal behavior, completeness, latency, and repeatability.

**Practice.** Create ten synthetic question/expected-evidence pairs. Score a baseline summary for evidence coverage and unsupported claims. Repeat the run and record whether results change.

**Evidence.** Evaluation rubric, test set, scorecard, and a failure analysis.

**Reflection.** Which metric could look good while hiding a serious safety failure?

## 08 — Privacy, security, and threat modeling

**Objective.** Apply least privilege, data minimization, auditability, secret hygiene, and abuse-case analysis.

**Practice.** Build a lightweight STRIDE-style threat table for the retrieval boundary. Include unauthorized patient access, model prompt injection, log leakage, replay, and denial of service. Map each threat to a preventive and detective control.

**Evidence.** Threat model and an access-control matrix.

**Reflection.** What should never be placed in an application log, even during debugging?

## 09 — Platform operations and governance

**Objective.** Make learning artifacts reproducible and reviewable.

**Practice.** Add CI, a quality gate, structured logs without identifiers, a change record, and an incident drill. Run the suite locally and in CI.

**Evidence.** Green CI run, runbook, and post-incident template.

**Reflection.** How will a reviewer reproduce the exact behavior that you observed?

## 10 — Capstone architecture and demonstration

**Objective.** Integrate interoperability, terminology, identity, retrieval, AI evaluation, governance, and operations into one defensible design.

**Practice.** Complete every item in [`scenarios/capstone.md`](../scenarios/capstone.md), produce the architecture decision record, and present a five-minute walkthrough.

**Evidence.** Architecture diagram, data-flow narrative, risk register, evaluation report, and passing test suite.

**Reflection.** What would you explicitly refuse to deploy, and what evidence would change your decision?

## Completion rubric

| Level | Evidence |
|---|---|
| Explorer | Can explain the main systems, resources, terminology roles, and safety boundaries. |
| Practitioner | Can modify the fixture, add tests, produce a quality report, and complete two scenarios. |
| Builder | Can implement a safe retrieval boundary, evaluation set, threat model, and CI quality gate. |
| Reviewer | Can challenge assumptions, identify unsafe claims, and defend a capstone design with evidence. |
