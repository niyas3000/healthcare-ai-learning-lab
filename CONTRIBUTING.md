# Contributing

Thank you for improving this learning lab. Contributions should make the learning path clearer, safer, more reproducible, or more accessible without introducing real health information or paid-service requirements.

## Before opening a pull request

Run `pytest -q`, run the CLI against the sample bundle, and check that documentation links and examples are correct. Explain the learning objective, the change, the test scenario, and any remaining limitation.

## Content rules

Use synthetic or fully de-identified examples only. Do not add credentials, patient exports, screenshots containing identifiers, or vendor content that cannot be redistributed. Avoid clinical claims and label optional integrations clearly. New examples should include a failure mode and a testable pass condition.

## Review standard

A reviewer should be able to reproduce the exercise on a free local setup, understand the data flow, see the safety boundary, and verify that the change does not weaken provenance, authorization, or refusal behavior.
