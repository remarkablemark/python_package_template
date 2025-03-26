# python_package_template

🐍 Python Package Template

## Install

[Python](https://pypi.org/project/python_package_template/):

```sh
pip install python_package_template
```

## Usage

Print greeting:

```py
from python_package_template import template
print(template.hello())
```

## Development

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
pip install -e '.[test]'
```

Install pre-commit into your git hooks:

```sh
pre-commit install
```

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

## License

[MIT](LICENSE)
