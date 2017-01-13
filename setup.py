#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Setup for the CamBot.

Source:: https://github.com/ampledata/cambot
"""

import os
import sys
import setuptools

__title__ = 'cambot'
__version__ = '1.0.0'
__author__ = 'Greg Albrecht <oss@undef.net>'
__copyright__ = 'Copyright 2017 Greg Albrecht'
__license__ = 'Apache License, Version 2.0'


def publish():
    """Function for publishing package to pypi."""
    if sys.argv[-1] == 'publish':
        os.system('python setup.py sdist')
        os.system('twine upload dist/*')
        sys.exit()


publish()


setuptools.setup(
    name=__title__,
    version=__version__,
    description='CamBot - Slack UniFi Video Camera Bot.',
    author='Greg Albrecht',
    author_email='oss@undef.net',
    packages=['cambot'],
    package_data={'': ['LICENSE']},
    package_dir={'cambot': 'cambot'},
    license=open('LICENSE').read(),
    long_description=open('README.rst').read(),
    url='https://github.com/ampledata/cambot',
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'requests >= 2.8.1',
        'slackbot',
        'uvsnap'
    ],
    entry_points={'console_scripts': ['cambot = cambot.cmd:cli']}
)
