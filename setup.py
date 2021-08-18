#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

from lona_chartjs import VERSION_STRING

setup(
    include_package_data=True,
    name='lona-chartjs',
    version=VERSION_STRING,
    author='Florian Scherf',
    url='https://github.com/lona-web-org/lona-chartjs',
    author_email='f.scherf@pengutronix.de',
    license='MIT',
    packages=find_packages(),
    install_requires=[],
)
