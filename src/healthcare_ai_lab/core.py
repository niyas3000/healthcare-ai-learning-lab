"""Small, dependency-free reference functions for the learning lab.

The implementation is intentionally conservative: it validates a narrow FHIR-shaped
fixture and produces transparent, non-clinical summaries. It is not a FHIR server,
terminology service, or clinical decision-support system.
"""

from __future__ import annotations

from collections import Counter
from typing import Any


SUPPORTED_RESOURCE_TYPES = {
    "Patient",
    "Encounter",
    "Observation",
    "Condition",
    "DiagnosticReport",
}


def load_bundle(path: str) -> dict[str, Any]:
    import json

    with open(path, encoding="utf-8") as handle:
        document = json.load(handle)
    if not isinstance(document, dict):
        raise ValueError("Bundle must be a JSON object")
    return document


def validate_bundle(bundle: dict[str, Any]) -> list[str]:
    """Return human-readable validation findings; an empty list means valid fixture."""
    findings: list[str] = []
    if bundle.get("resourceType") != "Bundle":
        findings.append("root.resourceType must be Bundle")
    entries = bundle.get("entry")
    if not isinstance(entries, list) or not entries:
        findings.append("Bundle.entry must be a non-empty list")
        return findings

    ids: set[str] = set()
    for index, entry in enumerate(entries):
        resource = entry.get("resource") if isinstance(entry, dict) else None
        prefix = f"entry[{index}]"
        if not isinstance(resource, dict):
            findings.append(f"{prefix}.resource must be an object")
            continue
        resource_type = resource.get("resourceType")
        resource_id = resource.get("id")
        if resource_type not in SUPPORTED_RESOURCE_TYPES:
            findings.append(f"{prefix} has unsupported resourceType: {resource_type}")
        if not resource_id or not isinstance(resource_id, str):
            findings.append(f"{prefix}.resource.id is required")
        elif resource_id in ids:
            findings.append(f"duplicate resource id: {resource_id}")
        else:
            ids.add(resource_id)
        if resource_type == "Patient" and not resource.get("name"):
            findings.append(f"{prefix}.Patient.name is required")
        if resource_type == "Observation":
            if not resource.get("status"):
                findings.append(f"{prefix}.Observation.status is required")
            if not isinstance(resource.get("code"), dict):
                findings.append(f"{prefix}.Observation.code must be an object")
        if resource_type in {"Encounter", "Observation", "Condition", "DiagnosticReport"}:
            subject = resource.get("subject")
            if not isinstance(subject, dict) or not subject.get("reference"):
                findings.append(f"{prefix}.{resource_type}.subject.reference is required")
    return findings


def quality_report(bundle: dict[str, Any]) -> dict[str, Any]:
    """Calculate explainable data-quality metrics for a learning exercise."""
    findings = validate_bundle(bundle)
    resources = [
        item.get("resource", {})
        for item in bundle.get("entry", [])
        if isinstance(item, dict) and isinstance(item.get("resource"), dict)
    ]
    types = Counter(resource.get("resourceType", "Unknown") for resource in resources)
    patient_ids = {r.get("id") for r in resources if r.get("resourceType") == "Patient"}
    dangling_subjects = []
    for resource in resources:
        if resource.get("resourceType") == "Patient":
            continue
        reference = resource.get("subject", {}).get("reference")
        if reference and reference.split("/")[-1] not in patient_ids:
            dangling_subjects.append(reference)
    return {
        "resource_count": len(resources),
        "resource_types": dict(sorted(types.items())),
        "validation_findings": findings,
        "dangling_subject_references": sorted(dangling_subjects),
        "valid": not findings and not dangling_subjects,
    }


def patient_summary(bundle: dict[str, Any], patient_id: str) -> dict[str, Any]:
    """Build a deterministic, provenance-preserving educational summary."""
    resources = [
        item.get("resource", {})
        for item in bundle.get("entry", [])
        if isinstance(item, dict) and isinstance(item.get("resource"), dict)
    ]
    patient = next((r for r in resources if r.get("resourceType") == "Patient" and r.get("id") == patient_id), None)
    if patient is None:
        raise KeyError(f"patient not found: {patient_id}")
    observations = [r for r in resources if r.get("resourceType") == "Observation" and r.get("subject", {}).get("reference") == f"Patient/{patient_id}"]
    conditions = [r for r in resources if r.get("resourceType") == "Condition" and r.get("subject", {}).get("reference") == f"Patient/{patient_id}"]
    encounters = [r for r in resources if r.get("resourceType") == "Encounter" and r.get("subject", {}).get("reference") == f"Patient/{patient_id}"]
    return {
        "patient_id": patient_id,
        "display_name": patient.get("name", [{}])[0].get("text", "Unknown"),
        "birth_date": patient.get("birthDate"),
        "encounter_count": len(encounters),
        "condition_count": len(conditions),
        "observation_count": len(observations),
        "observations": [
            {
                "resource_id": item.get("id"),
                "code": item.get("code", {}).get("text"),
                "value": item.get("valueQuantity", {}).get("value"),
                "unit": item.get("valueQuantity", {}).get("unit"),
                "effective": item.get("effectiveDateTime"),
            }
            for item in observations
        ],
        "provenance": [item.get("id") for item in observations + conditions + encounters],
        "disclaimer": "Educational summary only; not medical advice or a clinical recommendation.",
    }
