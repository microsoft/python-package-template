# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

import io
import os

# NOTE: DO NOT change the import order, as sometimes there is a conflict between setuptools and distutils,
# it will cause following error:
# error: each element of 'ext_modules' option must be an Extension instance or 2-tuple
from setuptools import find_packages
from distutils.core import setup

def read(file_path, encoding):
    return io.open(file_path, encoding=encoding).read()

readme = read("./README.md", encoding="utf-8")

setuptools = "setuptools>=54.2.0,<=54.2.0"

core_requires = read("./requirements.txt")
test_requires = read("./requirements.test.txt")

EXTRAS = {
    "required": core_requires,
    "test": test_requires,   
}

SETUP_REQUIRES = [
]


setup(
    name="ai-python-package",
    version="0.0.1",
    description="Microsoft Python Package Template",
    long_description=readme,
    long_description_content_type="text/x-rst",
    author="Daniel Ciborowski",
    author_email="dciborow@microsoft.com",
    url="https://github.com/microsoft/ai-python",
    project_urls={
        "Code": "https://github.com/microsoft/python-package",
        "Issues": "https://github.com/microsoft/python-package/issues",
        "Documents": "https://github.com/microsoft/python-package"
    },
    license="MIT License",
    platforms=["Windows", "Linux", "macOS"],
    keywords=["template"],
    classifiers=[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering :: Artificial Intelligence"],
    python_requires=">=3.7,<3.8",
    setup_requires=SETUP_REQUIRES,
    extras_require=EXTRAS,
    packages=find_packages(exclude=["tests", "tests.*", "examples", "examples.*"]),
    include_package_data=True,
    zip_safe=False,
)
