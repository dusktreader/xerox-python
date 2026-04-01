"""Fixtures for branch smoke tests.

Each branch under test is generated once per session into a temp directory
using copier, with `uv sync` run immediately after.  The resulting project
path is then available to individual test functions via the per-branch
fixtures defined here.

Design notes:
- `copier.run_copy` is called with `skip_tasks=True` so that git-init,
  github-push, and QA tasks are skipped.  Only the file-generation step runs.
- `defaults=True` accepts every copier question at its default value, except
  for the fields we override explicitly (project_name, initialize_git,
  push_to_github).
- Generation is session-scoped: one `uv sync` per branch for the whole
  test run, not one per test function.
- `unsafe=True` is required because the template lives in the same
  repository (local path, not a remote URL).
"""

from pathlib import Path

import copier
import pytest


_TEMPLATE_ROOT = Path(__file__).parent.parent


def _generate_project(tmp_path_factory: pytest.TempPathFactory, branch: str) -> Path:
    """Generate a project from *branch* and run `uv sync` inside it."""
    import subprocess

    base = tmp_path_factory.mktemp(f"xerox-{branch}", numbered=False)
    copier.run_copy(
        src_path=str(_TEMPLATE_ROOT),
        dst_path=str(base),
        data={
            "project_name": "smoke-test",
            "python_versions": ["3.13"],
            "default_python_version": "3.13",
            "initialize_git": False,
            "push_to_github": False,
        },
        defaults=True,
        overwrite=True,
        skip_tasks=True,
        unsafe=True,
        quiet=True,
        vcs_ref=branch,
    )
    project_dir = base / "smoke-test"
    result = subprocess.run(
        ["uv", "sync"],
        cwd=project_dir,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"uv sync failed for branch {branch!r}:\n{result.stderr}")
    return project_dir


@pytest.fixture(scope="session")
def main_project(tmp_path_factory: pytest.TempPathFactory) -> Path:
    """Generated + synced project from the `main` branch."""
    return _generate_project(tmp_path_factory, "main")


@pytest.fixture(scope="session")
def flask_project(tmp_path_factory: pytest.TempPathFactory) -> Path:
    """Generated + synced project from the `flask` branch."""
    return _generate_project(tmp_path_factory, "flask")


@pytest.fixture(scope="session")
def typerdrive_project(tmp_path_factory: pytest.TempPathFactory) -> Path:
    """Generated + synced project from the `typerdrive` branch."""
    return _generate_project(tmp_path_factory, "typerdrive")


@pytest.fixture(scope="session")
def fastapi_project(tmp_path_factory: pytest.TempPathFactory) -> Path:
    """Generated + synced project from the `fastapi` branch."""
    return _generate_project(tmp_path_factory, "fastapi")
