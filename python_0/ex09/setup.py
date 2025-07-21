from setuptools import setup, find_packages

# This setup.py is minimal as most configuration is in pyproject.toml
# It primarily serves as an entry point for setuptools build commands.
setup(
    # The name, version, etc. are read from pyproject.toml
    # This file primarily provides the entry point for build tools.
    # We still need to tell setuptools where to find the package code.
    packages=find_packages(),
)