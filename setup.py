# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import cc-test-1
version = cc-test-1.__version__

setup(
    name='cc-test-1',
    version=version,
    author='',
    author_email='olopatin@mail.ru',
    packages=[
        'cc-test-1',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.1',
    ],
    zip_safe=False,
    scripts=['cc-test-1/manage.py'],
)