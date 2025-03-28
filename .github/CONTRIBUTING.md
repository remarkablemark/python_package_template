# Contributing

<details>
<summary>Table of Contents</summary>

- [Fork](#fork)
- [Install](#install)
- [Develop](#develop)
- [Test](#test)
- [Lint](#lint)
- [Build](#build)
- [Release](#release)

</details>

Pull requests are welcome! By participating in this project, you agree to abide by our [code of conduct](https://github.com/remarkablemark/.github/blob/master/CODE_OF_CONDUCT.md).

## Fork

[Fork](https://github.com/remarkablemark/python_package_template/fork) and then clone the repository:

```sh
# replace <USER> with your username
git clone git@github.com:<USER>/python_package_template.git
```

```sh
cd python_package_template
```

## Install

Install [Python](https://www.python.org/):

```sh
brew install python
```

Create the virtual environment:

```sh
python3 -m venv .venv
```

Activate the virtual environment:

```sh
source .venv/bin/activate
```

Install the dependencies:

```sh
pip install -e '.[build]'
pip install -e '.[test]'
```

Install pre-commit into your git hooks:

```sh
pre-commit install
```

## Develop

Make your changes, add tests/documentation, and ensure tests pass:

```sh
pytest
```

Write a commit message that follows the [Conventional Commits](https://www.conventionalcommits.org/) specification:

- **feat**: A new feature
- **fix**: A bug fix
- **perf**: A code change that improves performance
- **refactor**: A code change that neither fixes a bug nor adds a feature
- **test**: Add missing tests or correct existing tests
- **build**: Changes that affect the build system or external dependencies
- **ci**: Updates configuration files and scripts for continuous integration
- **docs**: Documentation only changes

Push to your fork and create a [pull request](https://github.com/remarkablemark/python_package_template/compare/).

At this point, wait for us to review your pull request. We'll try to review pull requests within 1-3 business days. We may suggest changes, improvements, and/or alternatives.

Things that will improve the chance that your pull request will be accepted:

- [ ] Write tests that pass [CI](https://github.com/remarkablemark/python_package_template/actions/workflows/test.yml).
- [ ] Write solid documentation.
- [ ] Write a good [commit message](https://github.com/angular/angular/blob/main/CONTRIBUTING.md#commit).

## Test

Run the tests:

```sh
pytest
```

## Lint

Update pre-commit hooks to the latest version:

```sh
pre-commit autoupdate
```

Run all pre-commit hooks:

```sh
pre-commit run --all-files
```

Lint all files in the current directory:

```sh
ruff check
```

Format all files in the current directory:

```sh
ruff format
```

## Build

Generate distribution packages:

```sh
python3 -m build
```

Upload all of the archives under `dist`:

```sh
twine upload --repository testpypi dist/*
```

Install the package:

```sh
pip install --index-url https://test.pypi.org/simple/ --no-deps python_package_template
```

## Release

Release and publish are automated with [Release Please](https://github.com/googleapis/release-please).

[Add a new pending publisher to PyPI.](https://pypi.org/manage/account/publishing/)
