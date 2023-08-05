#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name="lit2",
    version="0.0.1",
    description="Training neural nets without boilerplate",
    author="Akhilez",
    author_email="lightrescuer@gmail.com",
    url="https://github.com/Akhilez/lit",
    install_requires=["lightning", "hydra-core"],
    packages=find_packages(),
    # use this to customize global commands available in the terminal after installing the package
    entry_points={
        "console_scripts": [
            "train_command = lit.train:main",
            "eval_command = lit.eval:main",
        ]
    },
)
