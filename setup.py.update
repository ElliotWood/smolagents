#!/usr/bin/env python

"""
setup.py file for smolagents package distribution.
"""

import os
import setuptools
from setuptools import setup, find_packages

PACKAGE_NAME = "smolagents"

def get_version():
    """Get version from the package without importing it."""
    # Importing the package could result in import errors if dependencies are not met
    init_path = os.path.join(os.path.dirname(__file__), "src", PACKAGE_NAME, "__init__.py")
    with open(init_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("__version__"):
                # remove quotes and whitespace
                return line.split("=")[1].strip().strip('\'"')
    return "0.0.0"  # fallback value

def get_long_description():
    """Get long description from README.md."""
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()


requires = [
    "pyyaml>=6.0",
    "tqdm",
    "rich>=13.3.5",
    "gradio>=4.0",
    "typer>=0.9.0",
]

ssetup_requires = []

dev_requires = [
    "pytest>=7.0",
    "pytest-cov",
    "black>=22.1",
    "isort",
    "pre-commit",
    "mypy",
    "jupyter",
    "jupyter-black",
    "jupytext",
]

docs_requires = ["mkdocs", "mkdocs-material"]

setup(
    name=PACKAGE_NAME,
    version=get_version(),
    author="Hugging Face",
    author_email="julien@huggingface.co",
    description="A barebones framework for experimentation with LLM agents.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/huggingface/smolagents",
    project_urls={
        "Bug Tracker": "https://github.com/huggingface/smolagents/issues",
        "Documentation": "https://github.com/huggingface/smolagents",
        "Source Code": "https://github.com/huggingface/smolagents",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    install_requires=requires,
    package_dir={"smolagents": "src/smolagents"},
    packages=["smolagents"] + ["smolagents." + pkg for pkg in find_packages("src/smolagents")],
    extras_require={
        "dev": dev_requires + docs_requires,
        "docs": docs_requires,
        # SSES extension extras
        "sses": ["gitpython>=3.1.0", "scikit-learn>=1.0.0", "numpy>=1.20.0"],
    },
    entry_points={
        "console_scripts": [
            "smolagents=smolagents.cli:app",
        ],
    },
    python_requires=">=3.10",
)
