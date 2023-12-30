from typing import List


console_scripts: List[str] = [
    "pyapt_update=pyapt.scripts.update:main",
]
config_requires: List[str] = [
    "pyclassifiers",
]
install_requires: List[str] = [
    "pytconf",
    "pylogconf",
]
make_requires: List[str] = [
    "pymakehelper",
    "pydmt",
    "pyclassifiers",
]
test_requires: List[str] = [
    "pylint",
    "pytest",
    "pytest-cov",
    "pyflakes",
    "flake8",
    "mypy",
]
dev_requires: List[str] = [
    "pypitools",
]
requires = config_requires + install_requires + make_requires + test_requires
