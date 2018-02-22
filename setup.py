# -*- coding: utf-8 -*-


"""setup.py: setuptools control. in root folder, run 'python setup.py install', then run 'fticks'"""


import re
from setuptools import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('bootstrap/bootstrap.py').read(),
    re.M
    ).group(1)


with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name = "futuresticks",
    packages = ["futuresticks"],
    entry_points = {
        "console_scripts": ['fticks = futuresticks.app:cli']
        },
    version = version,
    description = "Python command line application bare bones template.",
    long_description = long_descr,
    author = "Jan- Gehrcke",
    author_email = "jgehrcke@googlemail.com",
    url = "http://gehrcke.de/2014/02/distributing-a-python-command-line-application",
    )
