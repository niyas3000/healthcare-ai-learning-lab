# Healthcare AI Learning Lab

An open-source, **free-to-practice learning path** for digital health architects, interoperability engineers, data professionals, and AI builders. The lab uses synthetic data only and turns healthcare architecture concepts into small, testable exercises.

> **Safety boundary:** This repository is an educational sandbox. It is not a clinical decision-support product, does not use real patient data, and must not be used to diagnose, triage, prescribe, or make care decisions.

## What you will build

You will progress from healthcare information-system foundations to a small, safety-aware clinical data and AI platform. The capstone combines a FHIR-shaped data layer, terminology normalization, quality checks, a deterministic clinical-summary generator, a retrieval boundary, evaluation, security controls, and an architecture decision record.

| Stage | Theme | Practice outcome |
|---|---|---|
| 00 | Orientation and safety | Define scope, risk, synthetic-data rules, and a learning baseline. |
| 01 | Clinical systems | Map EHR, PAS, LIS, RIS/PACS, HIE, MPI, CDR, and terminology services. |
| 02 | FHIR foundations | Read and validate Patient, Encounter, Observation, Condition, and DiagnosticReport resources. |
| 03 | Legacy integration | Explain how HL7 v2, CSV, and vendor feeds are transformed at a boundary. |
| 04 | Terminology | Apply SNOMED CT, LOINC, ICD, and RxNorm roles without inventing codes. |
| 05 | Data quality and identity | Detect missing identifiers, invalid references, duplicates, and unsafe joins. |
| 06 | Retrieval and AI safety | Design a retrieval boundary that filters by purpose, consent, and provenance. |
| 07 | Evaluation | Measure groundedness, refusal behavior, completeness, and reproducibility. |
| 08 | Privacy and security | Apply least privilege, auditability, minimization, and threat modeling. |
| 09 | Platform operations | Add quality gates, observability, incident exercises, and reproducible runs. |
| 10 | Capstone | Produce an architecture pack and pass the end-to-end scenario suite. |

## Quick start

The core lab intentionally uses only the Python standard library, so it can run on a laptop, Codespaces, or a free CI runner without paid services.

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
pip install -e '.[dev]'
pytest -q
python -m healthcare_ai_lab.cli validate data/sample_fhir/bundle.json
python -m healthcare_ai_lab.cli summarize data/sample_fhir/bundle.json --patient patient-001
```

If you do not want a virtual environment, run the pure-standard-library examples directly with `PYTHONPATH=src python -m healthcare_ai_lab.cli ...`.

## Repository map

| Path | Purpose |
|---|---|
| `lessons/` | Guided lessons with objectives, exercises, evidence of completion, and reflection prompts. |
| `scenarios/` | Testable practice scenarios for interoperability, AI safety, and platform governance. |
| `src/healthcare_ai_lab/` | Small reference implementation for validation, quality checks, and deterministic summaries. |
| `tests/` | Automated tests that act as executable learning checkpoints. |
| `data/sample_fhir/` | Synthetic FHIR-shaped fixtures; no real patient information is included. |
| `docs/` | Architecture, threat model, evaluation plan, and free-resource guide. |
| `.github/workflows/` | Public CI workflow that runs on every push and pull request. |

## Learning method

For each lesson, first read the short concept note, then run or extend the related test, complete the scenario, and record a short decision in your own notes. You should be able to explain not only **what** works but also **why the control exists**, what can fail, and how a reviewer would detect the failure.

A recommended weekly rhythm is three focused sessions: one reading session, one implementation session, and one review session. Every milestone is achievable with free local tooling and synthetic data. Optional integrations such as a FHIR server, vector database, notebook platform, or cloud service are deliberately kept outside the required path.

## Practice rules

1. Use synthetic or fully de-identified data only. The included fixture is intentionally small and fictional.
2. Never paste secrets, access tokens, identifiable patient data, or production exports into issues, notebooks, prompts, or pull requests.
3. Treat generated text as untrusted output. Require source references, deterministic checks, and human review before any downstream use.
4. Do not present the examples as medical advice or as a validated clinical product.
5. Prefer reversible, observable, least-privilege changes. Document assumptions and unresolved risks.

## Free practice options

| Need | Free option |
|---|---|
| Python practice | Local Python 3.11+, `venv`, and the standard library. |
| Version control | Git and a public GitHub repository. |
| Synthetic health data | Generate your own data with Synthea or use the small fixture included here. |
| FHIR exploration | Read the public HL7 specification or run a local open-source FHIR server as an optional extension. |
| Architecture diagrams | Mermaid source files or any free Markdown editor. |
| CI | GitHub Actions on the public repository. |
| AI experiments | Begin with deterministic baselines and local mock retrieval; add an AI provider only after the safety and evaluation lessons. |

## Milestones

You have completed a milestone when the lesson's tests pass, the scenario response is written, and you can explain the main failure mode in plain language. The capstone is complete when `pytest -q` passes and the architecture pack in `docs/capstone/` has been reviewed against the checklist.

## License and attribution

This project is released under the MIT License. Standards and external projects remain under their own licenses. The learning material links to public authoritative references in [`docs/references.md`](docs/references.md).

## References

[1]: https://www.hl7.org/fhir/ "HL7 FHIR specification"
[2]: https://www.hl7.org/fhir/security.html "FHIR Security and Privacy Module"
[3]: https://build.fhir.org/ig/HL7/smart-app-launch/ "SMART App Launch implementation guide"
[4]: https://www.who.int/publications/i/item/9789240029200 "WHO guidance on ethics and governance of artificial intelligence for health"
[5]: https://www.nist.gov/itl/ai-risk-management-framework "NIST AI Risk Management Framework"
[6]: https://owasp.org/www-project-top-10-for-large-language-model-applications/ "OWASP Top 10 for Large Language Model Applications"
[7]: https://synthea.mitre.org/ "Synthea synthetic patient generator"
[8]: https://www.hl7.org/fhir/terminology-module.html "FHIR terminology module"
