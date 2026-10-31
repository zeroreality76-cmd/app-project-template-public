from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = (
    "README.md",
    "TEMPLATE_VERSION.md",
    "AGENTS.md",
    "CLAUDE.md",
    ".env.example",
    "docs/START_HERE.md",
    "docs/PROJECT_PROFILE.md",
    "docs/PROJECT_STATE.md",
    "docs/REQUIREMENTS_MATRIX.md",
    "docs/DEFINITION_OF_DONE.md",
    "docs/DOCUMENT_REGISTER.md",
    "docs/TOOL_MATRIX.md",
    "docs/operations/SETUP_CHECK.md",
    "github/PROJECTS_V2_CONFIGURATION.md",
    "automation/AUTOMATION_REGISTER.md",
    "automation/AUTOMATION_SPEC_TEMPLATE.md",
    "automation/AI_RUN_POLICY.md",
    "scenarios/NEUTRAL_B2B_SAAS_SCENARIO.md",
)
REQUIRED_ISSUE_FORMS = (
    "feature.yml",
    "bug.yml",
    "technical-work.yml",
    "documentation.yml",
    "risk.yml",
    "owner-decision.yml",
)
REQUIRED_FORM_KEYS = ("name:", "description:", "labels:", "body:")
LINK_PATTERN = re.compile(r"(?<!!)\[[^]]+\]\(([^)]+)\)")


def local_link_target(source: Path, link: str) -> Path | None:
    if link.startswith(("http://", "https://", "mailto:", "#")):
        return None
    target = link.split("#", 1)[0]
    if not target:
        return None
    return (source.parent / target).resolve()


def main() -> int:
    failures: list[str] = []
    for relative_path in REQUIRED_FILES:
        if not (ROOT / relative_path).is_file():
            failures.append(f"Saknad obligatorisk fil: {relative_path}")

    active_workflows = ROOT / ".github" / "workflows"
    if active_workflows.exists() and any(active_workflows.iterdir()):
        failures.append("Aktiva workflows får inte finnas i .github/workflows före setup-godkännande")

    issue_root = ROOT / ".github" / "ISSUE_TEMPLATE"
    for filename in REQUIRED_ISSUE_FORMS:
        form = issue_root / filename
        if not form.is_file():
            failures.append(f"Saknad issue form: {form.relative_to(ROOT)}")
            continue
        content = form.read_text(encoding="utf-8")
        for key in REQUIRED_FORM_KEYS:
            if key not in content:
                failures.append(f"Issue form saknar {key}: {form.relative_to(ROOT)}")

    for markdown_file in ROOT.rglob("*.md"):
        content = markdown_file.read_text(encoding="utf-8")
        for link in LINK_PATTERN.findall(content):
            target = local_link_target(markdown_file, link)
            if target is not None and not target.exists():
                failures.append(
                    f"Bruten lokal länk: {markdown_file.relative_to(ROOT)} -> {link}"
                )

    matrix = (ROOT / "docs" / "REQUIREMENTS_MATRIX.md").read_text(encoding="utf-8")
    for field in ("Behov", "Planerad leverans", "Verifiering", "Status", "Bevis/länk"):
        if field not in matrix:
            failures.append(f"Kravmatris saknar kolumn: {field}")

    if failures:
        print("MALLKONTROLL MISSLYCKADES")
        print("\n".join(f"- {failure}" for failure in failures))
        return 1

    print("MALLKONTROLL GODKÄND")
    print(f"Kontrollerade obligatoriska filer: {len(REQUIRED_FILES)}")
    print(f"Kontrollerade issue forms: {len(REQUIRED_ISSUE_FORMS)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
