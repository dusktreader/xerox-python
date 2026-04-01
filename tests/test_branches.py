"""Branch smoke tests.

Each test generates a full project from the named branch (via the session-
scoped fixtures in conftest.py), then runs ``uv run pytest`` inside it and
asserts the exit code is zero.

These tests are intentionally slow -- ``uv sync`` + ``pytest`` for a full
generated project takes tens of seconds each.  They are marked ``slow`` so
they can be skipped during rapid iteration:

    uv run pytest -m "not slow"   # skip these
    uv run pytest -m slow         # only these (default via make qa/test)
"""

import subprocess
from pathlib import Path

import pytest


def _run_pytest(project_dir: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["uv", "run", "pytest", "--no-header", "-q"],
        cwd=project_dir,
        capture_output=True,
        text=True,
    )


@pytest.mark.slow
def test_main_branch_passes(main_project: Path):
    """The base template (main branch) generates a project whose tests pass."""
    result = _run_pytest(main_project)
    assert result.returncode == 0, (
        f"pytest failed in generated main project.\nstdout:\n{result.stdout}\nstderr:\n{result.stderr}"
    )


@pytest.mark.slow
def test_flask_branch_passes(flask_project: Path):
    """The flask branch generates a project whose tests pass."""
    result = _run_pytest(flask_project)
    assert result.returncode == 0, (
        f"pytest failed in generated flask project.\nstdout:\n{result.stdout}\nstderr:\n{result.stderr}"
    )


@pytest.mark.slow
def test_typerdrive_branch_passes(typerdrive_project: Path):
    """The typerdrive branch generates a project whose tests pass."""
    result = _run_pytest(typerdrive_project)
    assert result.returncode == 0, (
        f"pytest failed in generated typerdrive project.\nstdout:\n{result.stdout}\nstderr:\n{result.stderr}"
    )


@pytest.mark.slow
def test_fastapi_branch_passes(fastapi_project: Path):
    """The fastapi branch generates a project whose tests pass."""
    result = _run_pytest(fastapi_project)
    assert result.returncode == 0, (
        f"pytest failed in generated fastapi project.\nstdout:\n{result.stdout}\nstderr:\n{result.stderr}"
    )
