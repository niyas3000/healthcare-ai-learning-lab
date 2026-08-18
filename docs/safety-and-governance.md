# Safety and governance

This lab is a learning artifact, not a healthcare product. The default design is intentionally conservative: synthetic data, narrow scope, explicit provenance, deterministic checks, least privilege, and human review.

## Intended use

The reference implementation demonstrates how to validate a small FHIR-shaped bundle, calculate explainable quality findings, and create a non-clinical summary that names the source resources used. It is suitable for training, code review, architecture discussion, and test design.

## Prohibited use

The implementation must not be used to diagnose, triage, prescribe, recommend treatment, make eligibility decisions, infer sensitive traits, or replace clinical judgment. It must not be connected to production data without a separate privacy, security, clinical safety, regulatory, and operational review.

## Control principles

| Principle | Practice control |
|---|---|
| Data minimization | Use only the fields needed for the exercise; keep fixtures synthetic. |
| Purpose limitation | Reject retrieval requests that lack an approved purpose-of-use. |
| Provenance | Preserve source resource IDs and make unsupported claims visible. |
| Human oversight | Require review for ambiguous identity, incomplete evidence, or high-impact use. |
| Least privilege | Separate read, transform, evaluate, and administrative permissions. |
| Auditability | Record policy decisions and correlation IDs without defaulting to free-text payload logging. |
| Reversibility | Quarantine invalid data and disable a policy path rather than silently changing records. |
| Transparency | Include the educational disclaimer and document limitations. |

## Minimum release gate

A change is not ready for this learning lab when it removes provenance, makes an unsupported clinical claim, accepts a dangling patient reference, logs sensitive free text by default, or weakens a test without an explanatory decision record.

## Review questions

Before accepting a pull request, ask: What data enters the boundary? What is the source of truth? Which terminology version is assumed? What happens on an uncertain identity match? Which policy blocks unauthorized access? How is the output evaluated? How can the change be rolled back?

## References

[1]: https://www.who.int/publications/i/item/9789240029200 "WHO guidance on ethics and governance of artificial intelligence for health"
[2]: https://www.nist.gov/itl/ai-risk-management-framework "NIST AI Risk Management Framework"
[3]: https://www.hl7.org/fhir/security.html "FHIR Security and Privacy Module"
