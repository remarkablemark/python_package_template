# python_package_template

🐍 Python package template

## Development

Create virtual environment:

```sh
python3 -m venv .venv
```

Activate virtual environment:

```sh
source .venv/bin/activate
```

Install PyPA's [build](https://github.com/pypa/build):

```sh
python3 -m pip install --upgrade build
```

Generate distribution packages:

```sh
python3 -m build
```

Install [Twine](https://github.com/pypa/twine):

```sh
python3 -m pip install --upgrade twine
```

Upload all of the archives under `dist`:

```sh
python3 -m twine upload --repository testpypi dist/*
```

## License

[MIT](LICENSE)
