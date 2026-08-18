from __future__ import annotations

import argparse
import json
import sys

from .core import load_bundle, patient_summary, quality_report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Healthcare AI Learning Lab CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate = subparsers.add_parser("validate", help="validate a small FHIR-shaped JSON bundle")
    validate.add_argument("path")

    quality = subparsers.add_parser("quality", help="calculate explainable data-quality metrics")
    quality.add_argument("path")

    summary = subparsers.add_parser("summarize", help="create a deterministic educational patient summary")
    summary.add_argument("path")
    summary.add_argument("--patient", required=True)

    args = parser.parse_args(argv)
    try:
        bundle = load_bundle(args.path)
        if args.command == "validate":
            findings = quality_report(bundle)["validation_findings"]
            if findings:
                print("INVALID")
                print("\n".join(f"- {finding}" for finding in findings))
                return 1
            print("VALID")
            return 0
        if args.command == "quality":
            print(json.dumps(quality_report(bundle), indent=2))
            return 0
        if args.command == "summarize":
            print(json.dumps(patient_summary(bundle, args.patient), indent=2))
            return 0
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
