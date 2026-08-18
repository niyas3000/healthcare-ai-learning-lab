import json
from pathlib import Path

import pytest

from healthcare_ai_lab import patient_summary, quality_report, validate_bundle


FIXTURE = Path(__file__).parents[1] / "data" / "sample_fhir" / "bundle.json"


def read_fixture():
    return json.loads(FIXTURE.read_text(encoding="utf-8"))


def test_sample_bundle_is_valid():
    assert validate_bundle(read_fixture()) == []


def test_quality_report_is_explainable():
    report = quality_report(read_fixture())
    assert report["valid"] is True
    assert report["resource_count"] == 5
    assert report["resource_types"]["Observation"] == 1
    assert report["dangling_subject_references"] == []


def test_patient_summary_preserves_provenance_and_disclaimer():
    summary = patient_summary(read_fixture(), "patient-001")
    assert summary["display_name"] == "Alex Example"
    assert summary["observation_count"] == 1
    assert summary["provenance"] == ["observation-001", "condition-001", "encounter-001"]
    assert "not medical advice" in summary["disclaimer"]


def test_missing_patient_is_not_silently_invented():
    with pytest.raises(KeyError):
        patient_summary(read_fixture(), "patient-does-not-exist")


def test_dangling_reference_is_reported():
    bundle = read_fixture()
    bundle["entry"][1]["resource"]["subject"]["reference"] = "Patient/unknown"
    report = quality_report(bundle)
    assert report["valid"] is False
    assert report["dangling_subject_references"] == ["Patient/unknown"]


def test_duplicate_ids_are_reported():
    bundle = read_fixture()
    duplicate = dict(bundle["entry"][0])
    bundle["entry"].append(duplicate)
    findings = validate_bundle(bundle)
    assert "duplicate resource id: patient-001" in findings
