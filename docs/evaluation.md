# Evaluation guide

The first evaluation target is the deterministic reference implementation. Optional model experiments come later and must not bypass the same evidence and safety checks.

## Suggested scorecard

| Dimension | Question | Example pass criterion |
|---|---|---|
| Structural validity | Are resources and references well formed? | No validation findings. |
| Evidence coverage | Does each statement have a source resource? | Every factual item has a source ID. |
| Unsupported claims | Does the output go beyond the bundle? | No diagnosis, treatment, or invented result. |
| Refusal behavior | Does it decline unsafe or under-supported requests? | Refuses when evidence or authorization is insufficient. |
| Completeness | Are expected resources included? | All scenario-required resource types appear. |
| Reproducibility | Does repeated execution produce the same result? | Same input produces byte-equivalent JSON after stable formatting. |
| Privacy | Are logs and outputs minimized? | No identifiers or free text in default telemetry beyond approved references. |
| Operability | Can failures be detected and recovered? | Quality findings, exit codes, and runbook exist. |

## Test-set template

Create a JSON or Markdown table with: scenario ID, user intent, allowed evidence IDs, prohibited claim types, expected response mode, and reviewer notes. Include at least one happy path, one missing-evidence refusal, one unauthorized-scope request, one malformed resource, one dangling reference, and one prompt-injection string treated strictly as data.

## Evaluation discipline

Do not claim clinical accuracy from this lab. A good score means that the implementation followed its stated contract on the synthetic test set. Any extension that makes clinical claims requires a new intended-use statement, risk assessment, expert review, validation plan, and applicable regulatory analysis.
