from setuptools import find_packages, setup

requires = ["mesa"]

setup(
    name="Ciudad",
    version="1.0.0",
    packages=find_packages(),
    install_requires=requires,
)
