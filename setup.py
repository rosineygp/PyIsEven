import os
from setuptools import setup

_github_ref = os.getenv("GITHUB_REF", "0.0.0").split("/")[-1]
_version = _github_ref.replace("v", "")

setup(
    name="PyIsEven",
    packages=["is_even"],
    version=_version,
    license="MIT",
    description="Check is a integer is even",
    author="Rosiney Gomes Pereira",
    url="https://github.com/rosineygp/PyIsEven",
    keywords=["even"],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=[
        "requests>=2.14.0",
        "retry>=0.9.2",
        "typing-extensions>=3.10.0.0",
    ],
)
