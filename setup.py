"""
Sky
The Python utility framework -- from up High.
"""
import os
import json
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    LONG_DESCRIPTION = f.read()
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()
with open(os.path.join(here, 'package.json')) as f:
    PKG = json.loads(f.read())

requires = [
    'python-dotenv'
]

setup(
    name=PKG["name"],
    version=PKG["version"],
    author=PKG["author"],
    author_email='hello@blazed.space',
    description=README,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url=PKG["homepage"],
    project_urls={
        "Bug Tracker": PKG["bugs"]["url"],
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=requires,
    entry_points = {
        'src.main': [
            'main = src:main'
        ]
    }
)