from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml


FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_frontmatter(path: Path) -> dict:
    text = read_text(path)
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise ValueError(f"{path} is missing YAML frontmatter.")
    data = yaml.safe_load(match.group(1)) or {}
    if not isinstance(data, dict):
        raise ValueError(f"{path} frontmatter must be a mapping.")
    return data


def assert_exists(path: Path, label: str, errors: list[str]) -> None:
    if not path.exists():
        errors.append(f"Missing {label}: {path}")


def validate_skill(repo: Path) -> list[str]:
    errors: list[str] = []

    skill_path = repo / "SKILL.md"
    openai_path = repo / "agents" / "openai.yaml"
    readme_path = repo / "README.md"
    readme_ja_path = repo / "README.ja.md"
    docs_pkg_path = repo / "docs" / "package.json"

    assert_exists(skill_path, "skill definition", errors)
    assert_exists(openai_path, "agents/openai.yaml", errors)
    assert_exists(readme_path, "README.md", errors)
    assert_exists(readme_ja_path, "README.ja.md", errors)
    assert_exists(docs_pkg_path, "docs/package.json", errors)

    if errors:
        return errors

    frontmatter = load_frontmatter(skill_path)
    for key in ("name", "description"):
        value = frontmatter.get(key)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"SKILL.md frontmatter requires a non-empty string for '{key}'.")

    openai_data = yaml.safe_load(read_text(openai_path)) or {}
    interface = openai_data.get("interface")
    if not isinstance(interface, dict):
        errors.append("agents/openai.yaml requires an interface mapping.")
    else:
        for key in ("display_name", "short_description", "default_prompt"):
            value = interface.get(key)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"agents/openai.yaml requires a non-empty interface.{key}.")

    required_files = [
        repo / "assets" / "export_glb_to_timbermesh_template.py",
        repo / "assets" / "building_blueprint.template.json",
        repo / "assets" / "material_collection.template.json",
        repo / "assets" / "template_collection_buildings.template.json",
        repo / "references" / "workflow.md",
        repo / "references" / "troubleshooting.md",
        repo / "references" / "example-route-a.md",
        repo / "references" / "example-route-b.md",
        repo / "CONTRIBUTING.md",
        repo / "SECURITY.md",
        repo / "docs" / ".vitepress" / "config.ts",
        repo / "docs" / "index.md",
        repo / "docs" / "ja" / "index.md",
        repo / "docs" / "guide" / "getting-started.md",
        repo / "docs" / "guide" / "workflow-routes.md",
        repo / "docs" / "guide" / "repository-structure.md",
        repo / "docs" / "guide" / "troubleshooting.md",
        repo / "docs" / "ja" / "guide" / "getting-started.md",
        repo / "docs" / "ja" / "guide" / "workflow-routes.md",
        repo / "docs" / "ja" / "guide" / "repository-structure.md",
        repo / "docs" / "ja" / "guide" / "troubleshooting.md",
        repo / ".github" / "workflows" / "validate.yml",
        repo / ".github" / "workflows" / "docs.yml",
        repo / ".github" / "ISSUE_TEMPLATE" / "bug_report.yml",
        repo / ".github" / "ISSUE_TEMPLATE" / "feature_request.yml",
        repo / ".github" / "ISSUE_TEMPLATE" / "config.yml",
        repo / ".github" / "pull_request_template.md",
    ]
    for path in required_files:
        assert_exists(path, path.relative_to(repo).as_posix(), errors)

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the Timberborn skill repository structure.")
    parser.add_argument("repo", nargs="?", default=".", help="Repository path")
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    errors = validate_skill(repo)
    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
