console_scripts = [
    "pyapt_update=pyapt.scripts.update:main",
]
config_requires = [
    "pyclassifiers",
]
install_requires = [
    "pytconf",
    "pylogconf",
]
make_requires = [
    "pymakehelper",
    "pydmt",
    "pyclassifiers",
]
test_requires = [
    "pylint",
    "pytest",
    "pytest-cov",
    "pyflakes",
    "flake8",
    "mypy",
]
dev_requires = [
    "pypitools",
]
requires = config_requires + install_requires + make_requires + test_requires
