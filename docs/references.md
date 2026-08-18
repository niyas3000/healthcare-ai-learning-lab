# References and free resources

The resources below are public starting points. Read the source itself and record the version or publication date you used in your own notes.

| Topic | Reference | Suggested practice |
|---|---|---|
| FHIR | [HL7 FHIR specification][1] | Read Patient, Observation, Bundle, references, and security sections. |
| FHIR terminology | [FHIR terminology module][2] | Explain CodeSystem, ValueSet, ConceptMap, and validation responsibilities. |
| SMART on FHIR | [SMART App Launch guide][3] | Map authorization, scopes, and launch context without placing secrets in code. |
| Health AI governance | [WHO ethics and governance guidance][4] | Extract principles for autonomy, safety, transparency, accountability, and equity. |
| AI risk management | [NIST AI RMF][5] | Turn Govern, Map, Measure, and Manage into a project checklist. |
| LLM security | [OWASP Top 10 for LLM Applications][6] | Threat-model prompt injection, sensitive information disclosure, and excessive agency. |
| Synthetic data | [Synthea][7] | Generate synthetic patients as an optional extension; never substitute real data. |
| FHIR security | [FHIR Security and Privacy Module][8] | Compare access control, audit, consent, and security-label concepts. |

## Free practice sequence

Start locally with the included fixture and tests. Then generate a larger synthetic dataset with Synthea, add a local parser or open-source FHIR server as an optional extension, and build a notebook that reports resource counts and quality findings. Only after the deterministic path is stable should you add a model provider; keep that provider optional, mockable, and outside the required test suite.

[1]: https://www.hl7.org/fhir/ "HL7 FHIR specification"
[2]: https://www.hl7.org/fhir/terminology-module.html "FHIR terminology module"
[3]: https://build.fhir.org/ig/HL7/smart-app-launch/ "SMART App Launch implementation guide"
[4]: https://www.who.int/publications/i/item/9789240029200 "WHO guidance on ethics and governance of artificial intelligence for health"
[5]: https://www.nist.gov/itl/ai-risk-management-framework "NIST AI Risk Management Framework"
[6]: https://owasp.org/www-project-top-10-for-large-language-model-applications/ "OWASP Top 10 for Large Language Model Applications"
[7]: https://synthea.mitre.org/ "Synthea synthetic patient generator"
[8]: https://www.hl7.org/fhir/security.html "FHIR Security and Privacy Module"
