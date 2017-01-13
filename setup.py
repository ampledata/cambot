#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Cambot Package."""

__author__ = 'Greg Albrecht <oss@undef.net>'
__copyright__ = 'Copyright 2017 Orion Labs, Inc.'
__license__ = 'Apache License, Version 2.0'


import setuptools


setuptools.setup(
    name='cambot',
    version='0.0.2b1',
    description='Cambot - Slack Camera Bot.',
    license='Apache License, Version 2.0',
    author='Greg Albrecht',
    author_email='gba@orionlabs.io',
    zip_safe=False,
    packages=['cambot'],
    install_requires=[
        'requests >= 2.8.1',
        'slackbot',
        'uvsnap'
    ],
    entry_points={'console_scripts': ['cambot = cambot.cmd:cli']}

)
