import config.project

package_name = config.project.project_name

console_scripts = [
    'pyapt_update=pyapt.scripts.update:main',
]

setup_requires = [
]

run_requires = [
    'pytconf',
    'pylogconf',
]

test_requires = [
    'pylint',
    'pytest',
    'pyflakes',
]

dev_requires = [
    'pyclassifiers',
    'pypitools',
    'pydmt',
    'Sphinx',
]

install_requires = list(setup_requires)
install_requires.extend(run_requires)

python_requires = ">=3.6"

extras_require={
}
