import setuptools
import re

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="ad_python",
    version="0.0.1",
    author="aiden-dai",
    author_email="aiden.dai@gmail.com",
    description="Test python package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aiden-dai/my_python_package",
    packages=setuptools.find_packages(exclude=('test', 'test.*')),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)