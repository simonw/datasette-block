from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-block",
    description="Block all access to specific path prefixes",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/datasette-block",
    project_urls={
        "Issues": "https://github.com/simonw/datasette-block/issues",
        "CI": "https://github.com/simonw/datasette-block/actions",
        "Changelog": "https://github.com/simonw/datasette-block/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["datasette_block"],
    entry_points={"datasette": ["block = datasette_block"]},
    install_requires=["datasette"],
    extras_require={"test": ["pytest", "pytest-asyncio"]},
    tests_require=["datasette-block[test]"],
    python_requires=">=3.6",
)
