#!/usr/bin/env python3
"""Verify protected Hazel workflow elements against an approved manifest."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return value


def normalized_matches(pattern: str, text: str) -> list[str]:
    return sorted(
        re.sub(r"\s+", " ", match).strip()
        for match in re.findall(pattern, text, flags=re.IGNORECASE | re.MULTILINE)
    )


def compare_pattern(
    failures: list[dict[str, str]],
    check_id: str,
    label: str,
    pattern: str,
    base: str,
    candidate: str,
) -> None:
    if normalized_matches(pattern, base) != normalized_matches(pattern, candidate):
        failures.append(
            {
                "id": check_id,
                "message": f"Protected {label} changed without manifest authorization.",
            }
        )


def verify(
    base_path: Path,
    candidate_path: Path,
    manifest_path: Path,
    changed_file: str,
    config_path: Path,
) -> dict[str, Any]:
    manifest = load_json(manifest_path)
    config = load_json(config_path)
    base = base_path.read_text(encoding="utf-8")
    candidate = candidate_path.read_text(encoding="utf-8")
    failures: list[dict[str, str]] = []

    allowed_files = manifest.get("allowed_files", [])
    if changed_file not in allowed_files:
        failures.append(
            {
                "id": "file-scope",
                "message": f"{changed_file} is not listed in allowed_files.",
            }
        )

    permissions = manifest.get("permissions", {})
    protected = set(manifest.get("protected_elements", []))

    if (
        "root_css_variables" in protected
        and not permissions.get("allow_global_styles", False)
    ):
        compare_pattern(
            failures,
            "root-css",
            ":root CSS variables",
            config["root_css_pattern"],
            base,
            candidate,
        )

    if (
        {"font_imports", "font_families"} & protected
        and not permissions.get("allow_global_styles", False)
    ):
        for index, pattern in enumerate(config["font_patterns"], start=1):
            compare_pattern(
                failures,
                f"font-{index}",
                "font declarations",
                pattern,
                base,
                candidate,
            )

    if (
        "brand_assets" in protected
        and not permissions.get("allow_brand_assets", False)
    ):
        for index, pattern in enumerate(config["brand_element_patterns"], start=1):
            compare_pattern(
                failures,
                f"brand-{index}",
                "brand or logo elements",
                pattern,
                base,
                candidate,
            )

    return {
        "status": "pass" if not failures else "fail",
        "changed_file": changed_file,
        "checks": {
            "file_scope": changed_file in allowed_files,
            "global_styles_protected": not permissions.get("allow_global_styles", False),
            "brand_assets_protected": not permissions.get("allow_brand_assets", False),
        },
        "failures": failures,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", required=True, type=Path)
    parser.add_argument("--candidate", required=True, type=Path)
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--changed-file", required=True)
    parser.add_argument(
        "--config",
        type=Path,
        default=Path(__file__).with_name("protected-workflow-elements.json"),
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        report = verify(
            args.base,
            args.candidate,
            args.manifest,
            args.changed_file,
            args.config,
        )
    except (OSError, ValueError, json.JSONDecodeError) as error:
        report = {
            "status": "blocked",
            "failures": [{"id": "input", "message": str(error)}],
        }
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    sys.exit(main())
