#!/usr/bin/env python3
"""Render a redacted Gitleaks JSON report as a PR comment."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


TARGET_TYPES = "`.ipynb`, `.md`, `.R`, `.py`, `.yml`, `.yaml`, and log files"


def markdown_escape(value: Any) -> str:
    text = "" if value is None else str(value)
    return text.replace("\\", "\\\\").replace("|", "\\|").replace("\n", " ")


def normalize_path(path_value: Any, source_root: Path | None) -> str:
    path = "" if path_value is None else str(path_value)
    if not path:
        return "unknown"

    file_path = Path(path)
    if source_root and file_path.is_absolute():
        try:
            return str(file_path.relative_to(source_root))
        except ValueError:
            return path
    return path


def load_findings(report_path: Path) -> list[dict[str, Any]]:
    if not report_path.exists() or report_path.stat().st_size == 0:
        return []

    with report_path.open(encoding="utf-8") as handle:
        data = json.load(handle)

    if isinstance(data, list):
        return [item for item in data if isinstance(item, dict)]
    return []


def render(args: argparse.Namespace) -> str:
    findings = load_findings(args.report)
    lines = [
        "### Secret Scanning Report",
        "",
        f"Gitleaks scanned the pull request working tree for {TARGET_TYPES}.",
        "Secret values are redacted from this report.",
        (
            "This automated scan is a safeguard, not a guarantee. Please still review the "
            "changed files yourself and take care that no sensitive data is being leaked."
        ),
        "",
    ]

    if args.exit_code not in (0, 1):
        lines.extend(
            [
                f"Gitleaks exited with code `{args.exit_code}`. Check the workflow logs for details.",
                "",
            ]
        )

    if not findings:
        lines.append("No potential secrets were detected.")
        return "\n".join(lines) + "\n"

    lines.extend(
        [
            f"Potential secrets detected: `{len(findings)}`.",
            "",
            "| Rule | File | Line |",
            "| --- | --- | --- |",
        ]
    )

    source_root = args.source_root.resolve() if args.source_root else None
    for finding in findings[: args.max_findings]:
        rule = markdown_escape(finding.get("RuleID", "unknown"))
        file_name = markdown_escape(normalize_path(finding.get("File"), source_root))
        line = markdown_escape(finding.get("StartLine") or finding.get("Line") or "unknown")
        lines.append(f"| `{rule}` | `{file_name}` | `{line}` |")

    remaining = len(findings) - args.max_findings
    if remaining > 0:
        lines.extend(
            [
                "",
                f"Showing the first {args.max_findings} findings; {remaining} more are in the workflow logs.",
            ]
        )

    lines.extend(
        [
            "",
            (
                "Remove the secret from the PR. If the value is a deliberate fake token in "
                "course material, add a narrow allowlist entry."
            ),
        ]
    )
    return "\n".join(lines) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--source-root", type=Path)
    parser.add_argument("--exit-code", type=int, default=0)
    parser.add_argument("--max-findings", type=int, default=25)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    args.output.write_text(render(args), encoding="utf-8")


if __name__ == "__main__":
    main()
