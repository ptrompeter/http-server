# _*_ coding: utf-8 _*_
from setuptools import setup

setup(
    name="http-server",
    desc="http-server for python 401 week 2",
    version=1.0,
    author="Patrick Trompeter and Kyle Richardson",
    email="patrick@trompeter.io",
    py_modules=['server', 'client'],
    package_dir={'': 'src'},
    install_requires=['gevent'],
    extras_require={'test': ['pytest', 'pytest-xdist', 'tox']}
)
