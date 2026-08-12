# Quality-check fixes

This journal records the focused lint and spelling cleanup applied to the template.


## Intent

Fix the reported import-order, exception-handling, string-construction, explicit-conversion, loop-variable, and
nested-patch quality failures without changing unrelated template behavior. No `delcarative` typo was present in the
template docs.


## Files changed

- `template/{{project_name}}/src/{{module_name}}/main.py.jinja`
- `template/{{project_name}}/src/{{module_name}}_demo/helpers.py.jinja`
- `template/{{project_name}}/src/{{module_name}}_demo/main.py.jinja`
- `template/{{project_name}}/tests/integration/conftest.py.jinja`
- `template/{{project_name}}/tests/integration/steps/main_steps.py.jinja`
- `template/{{project_name}}/tests/unit/test_main.py.jinja`
- `template/{{project_name}}/tests/unit/test_version.py.jinja`
- `template/{{project_name}}/src/{{module_name}}/version.py`
- `template/{{project_name}}/Makefile.jinja`


## Verification

- Generated a temporary demo project with Copier.
- Targeted Ruff rules (`I`, `BLE`, `RUF`, `PLR`, `FLY`, and `SIM117`) passed on all changed generated files.
- `git diff --check` passed.
- Typos scanning initially reported the `restults` typo in
  `template/{{project_name}}/CONTRIBUTING.md.jinja`; corrected it in both the template and repository guide.
- Added future annotations to the generated demo modules so their PEP 604 annotations remain compatible with the
  template's supported Python versions.
- Reordered the generated version imports to satisfy Ruff's import ordering check.
- Updated generated `qa/types` to run with the optional `demo` extra when the demo is included, keeping the demo
  dependencies optional while making type checking resolve them.
- The first generated QA run still reported I001 in `version.py`; separated the standard-library import groups and
  reran the generated checks after regenerating the project.
- Generated project verification used Copier with `include_demo=true`, then adjusted the generated Python requirement
  from 3.14 to 3.13 because Python 3.14 is not installed locally.
- `uv sync --quiet` completed successfully in the generated project.
- `make qa/full` completed with exit code 0: 8 tests passed, 100% coverage, Ruff and typos checks passed, Ty ran with
  `--extra demo`, and the output included `All quality checks pass!`.
- Regenerated the project after the spelling fix; its full QA run passed without the reported spelling failure.
- Repository `git diff --check` passed and the journal passed `check-markdown-format.mjs`.
- Repository `uv run pytest` was attempted: 2 tests passed and 3 branch tests errored because local branches `flask`,
  `typer`, and `typerdrive` are unavailable; this is unrelated to the template changes.
