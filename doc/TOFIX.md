# TOFIX

Findings from a code scan on 2026-10-04.

## Medium

- `src/pyapt/core/core.py:15` - the package has no functionality: `apply_ppa()` is an empty stub, `read_config()` (line 9) is never called, and there is no CLI entry point, yet `pyproject.toml:24` advertises `Development Status :: 4 - Beta` and the package is published to PyPI as a tool to "maintain third party apt repos". Implement the feature (the plan is in `doc/TODO.txt`) or mark the classifier as `1 - Planning` / `2 - Pre-Alpha`.
- `pyproject.toml:35` - `pytconf` and `pylogconf` are declared runtime dependencies but nothing under `src/` or `tests/` imports them, so every install of pyapt pulls two unused packages. Drop them until code actually uses them.
- `rsconstruct.toml:50` - the sphinx `dep_inputs = ["src/pyapt/*.py"]` does not match `src/pyapt/core/core.py`, although `sphinx/pyapt.core.rst:10` autodocs that module, so editing it does not rebuild the docs. Use `src/pyapt/**/*.py`.

## Low

- `pyproject.toml:83` - `mypy_path = "src:python:scripts"` names `python/` and `scripts/` directories that do not exist in this repo; reduce it to `src`.
