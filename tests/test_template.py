from python_package_template import hello


def test_hello() -> None:
    assert hello() == "Hello, World!"


def test_hello_world() -> None:
    assert hello("world") == "Hello, world!"
