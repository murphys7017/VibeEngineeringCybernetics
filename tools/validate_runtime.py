#!/usr/bin/env python3
"""Validate the v1 AI governance runtime structure.

The validator is intentionally dependency-free so it can run immediately after a
release archive is unpacked into a target repository.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


REQUIRED_FILES = [
    "AGENTS.md",
    ".ai/README.md",
    ".ai/constitution/core.md",
    ".ai/invariants/core.md",
    ".ai/router/task_classification.md",
    ".ai/router/risk_levels.md",
    ".ai/router/loading_rules.md",
    ".ai/policies/workflow.yaml",
    ".ai/workflows/documentation.md",
    ".ai/workflows/feature_development.md",
    ".ai/workflows/bugfix.md",
    ".ai/workflows/refactor.md",
    ".ai/workflows/review.md",
    ".ai/workflows/release.md",
    ".ai/checklists/review.md",
    ".ai/evaluation/README.md",
    ".ai/state/README.md",
    "docs/runtime/agent_execution_protocol.md",
]

EXPECTED_TASK_CLASSES = [
    "documentation",
    "feature development",
    "bugfix",
    "refactor",
    "review",
    "release",
    "repository maintenance",
]

EXPECTED_POLICY_KEYS = [
    "id",
    "severity",
    "category",
    "description",
    "applies_to",
    "enforcement",
    "exceptions",
]

EXPECTED_STATE_FIELDS = {
    "task_state.yaml": ["current_task:", "type:", "scope:", "risk:", "phase:", "owner:"],
    "context_state.yaml": ["context:", "confidence:", "required_files_loaded:", "assumptions:", "unresolved_questions:"],
    "architecture_state.yaml": ["architecture:", "stability:", "pending_breaking_change:", "boundary_changes:"],
    "risk_state.yaml": ["risk:", "current_level:", "scope_expansion_detected:", "architecture_risk_detected:", "destructive_action_pending:"],
    "execution_state.yaml": ["execution:", "phase:", "validation_passed:", "review_completed:", "correction_required:"],
    "verification_state.yaml": ["verification:", "checks_run:", "checks_failed:", "validation_gap:"],
}


@dataclass(frozen=True)
class Finding:
    severity: str
    path: str
    message: str


class Validator:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.findings: list[Finding] = []

    def error(self, path: str, message: str) -> None:
        self.findings.append(Finding("ERROR", path, message))

    def warn(self, path: str, message: str) -> None:
        self.findings.append(Finding("WARN", path, message))

    def read_text(self, relative: str) -> str:
        return (self.root / relative).read_text(encoding="utf-8")

    def exists(self, relative: str) -> bool:
        return (self.root / relative).exists()

    def validate(self) -> list[Finding]:
        self.check_required_files()
        self.check_loading_rule_links()
        self.check_task_class_coverage()
        self.check_policy_schema()
        self.check_checklist_result_schema()
        self.check_evaluation_schema()
        self.check_state_schema()
        self.check_adapter_protocol_links()
        return self.findings

    def check_required_files(self) -> None:
        for relative in REQUIRED_FILES:
            if not self.exists(relative):
                self.error(relative, "required file is missing")

    def check_loading_rule_links(self) -> None:
        relative = ".ai/router/loading_rules.md"
        if not self.exists(relative):
            return

        text = self.read_text(relative)
        refs = sorted(set(re.findall(r"`([^`]+)`", text)))
        runtime_refs = [
            ref
            for ref in refs
            if ref.startswith(
                (
                    "constitution/",
                    "invariants/",
                    "policies/",
                    "workflows/",
                    "skills/",
                    "checklists/",
                    "evaluation/",
                    "state/",
                )
            )
        ]

        for ref in runtime_refs:
            if not (self.root / ".ai" / ref).exists():
                self.error(relative, f"referenced runtime file does not exist: {ref}")

    def check_task_class_coverage(self) -> None:
        classification = ".ai/router/task_classification.md"
        loading_rules = ".ai/router/loading_rules.md"
        if not self.exists(classification) or not self.exists(loading_rules):
            return

        classification_text = self.read_text(classification)
        loading_text = self.read_text(loading_rules)

        for task_class in EXPECTED_TASK_CLASSES:
            if f"- {task_class}" not in classification_text:
                self.error(classification, f"expected task class is missing: {task_class}")
            if not re.search(rf"^### {re.escape(task_class)} \+", loading_text, re.MULTILINE):
                self.error(loading_rules, f"loading matrix has no entry for task class: {task_class}")

    def check_policy_schema(self) -> None:
        policy_dir = self.root / ".ai" / "policies"
        if not policy_dir.exists():
            self.error(".ai/policies", "policy directory is missing")
            return

        for path in sorted(policy_dir.glob("*.yaml")):
            text = path.read_text(encoding="utf-8")
            relative = path.relative_to(self.root).as_posix()
            if "rules:" not in text:
                self.error(relative, "policy file is missing rules block")
                continue

            rule_blocks = re.split(r"\n\s*-\s+id:\s+", text)
            if len(rule_blocks) <= 1:
                self.error(relative, "policy file has no rules with id")
                continue

            for index, block in enumerate(rule_blocks[1:], start=1):
                normalized = "id: " + block
                for key in EXPECTED_POLICY_KEYS:
                    if not re.search(rf"^\s*{re.escape(key)}\s*:", normalized, re.MULTILINE):
                        self.error(relative, f"rule {index} is missing key: {key}")

    def check_checklist_result_schema(self) -> None:
        checklist_dir = self.root / ".ai" / "checklists"
        if not checklist_dir.exists():
            self.error(".ai/checklists", "checklist directory is missing")
            return

        for path in sorted(checklist_dir.glob("*.md")):
            text = path.read_text(encoding="utf-8")
            relative = path.relative_to(self.root).as_posix()
            for required in ["## Result Format", "checklist_result:", "status: pass | partial | fail", "evidence:", "issues:", "required_correction:"]:
                if required not in text:
                    self.error(relative, f"checklist result schema is missing: {required}")

    def check_evaluation_schema(self) -> None:
        relative = ".ai/evaluation/README.md"
        if not self.exists(relative):
            return

        text = self.read_text(relative)
        for required in [
            "execution_quality: pass | partial | fail | not_applicable",
            "architecture_stability: pass | partial | fail | not_applicable",
            "governance_compliance: pass | partial | fail | not_applicable",
            "validation_status: passed | partial | failed | not_run",
            "evidence:",
            "required_correction:",
        ]:
            if required not in text:
                self.error(relative, f"evaluation schema is missing: {required}")

    def check_state_schema(self) -> None:
        state_dir = self.root / ".ai" / "state"
        if not state_dir.exists():
            self.error(".ai/state", "state directory is missing")
            return

        for filename, fields in EXPECTED_STATE_FIELDS.items():
            path = state_dir / filename
            relative = path.relative_to(self.root).as_posix()
            if not path.exists():
                self.error(relative, "state file is missing")
                continue
            text = path.read_text(encoding="utf-8")
            for field in fields:
                if field not in text:
                    self.error(relative, f"state field is missing: {field}")

    def check_adapter_protocol_links(self) -> None:
        adapter_dir = self.root / ".ai" / "adapters"
        if not adapter_dir.exists():
            self.warn(".ai/adapters", "adapter directory is missing")
            return

        for path in sorted(adapter_dir.glob("*.md")):
            text = path.read_text(encoding="utf-8")
            relative = path.relative_to(self.root).as_posix()
            if "docs/runtime/agent_execution_protocol.md" not in text:
                self.error(relative, "adapter does not reference the shared execution protocol")
            if "Do not bypass the router layer" not in text:
                self.error(relative, "adapter does not enforce router usage")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate the AI governance runtime structure.")
    parser.add_argument(
        "root",
        nargs="?",
        default=".",
        help="Repository root to validate. Defaults to the current directory.",
    )
    parser.add_argument(
        "--warnings-as-errors",
        action="store_true",
        help="Return a failing exit code when warnings are present.",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    root = Path(args.root).resolve()

    validator = Validator(root)
    findings = validator.validate()

    errors = [finding for finding in findings if finding.severity == "ERROR"]
    warnings = [finding for finding in findings if finding.severity == "WARN"]

    if not findings:
        print(f"PASS: governance runtime validation succeeded for {root}")
        return 0

    for finding in findings:
        print(f"{finding.severity}: {finding.path}: {finding.message}")

    print(f"\nSummary: {len(errors)} error(s), {len(warnings)} warning(s)")

    if errors or (args.warnings_as_errors and warnings):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
