#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup


def get_version() -> str:
    version = ""
    with open("gitlab/_version.py", "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("__version__"):
                version = eval(line.split("=")[-1])
                break
    return version


with open("README.rst", "r", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="python-gitlab",
    version=get_version(),
    description="Interact with GitLab API",
    long_description=readme,
    long_description_content_type="text/x-rst",
    author="Gauvain Pocentek",
    author_email="gauvain@pocentek.net",
    license="LGPL-3.0-or-later",
    url="https://github.com/python-gitlab/python-gitlab",
    packages=find_packages(exclude=["docs*", "tests*"]),
    install_requires=[
        "requests>=2.25.0",
        "requests-toolbelt>=0.10.1",
        "typing-extensions>=4.0.0;python_version<'3.8'",
    ],
    package_data={
        "gitlab": ["py.typed"],
    },
    python_requires=">=3.8.0",
    entry_points={"console_scripts": ["gitlab = gitlab.cli:main"]},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Natural Language :: English",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    extras_require={
        "autocompletion": ["argcomplete>=1.10.0,<3"],
        "yaml": ["PyYaml>=6.0.1"],
    },
)
