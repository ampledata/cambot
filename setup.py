#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Cambot Package."""

__author__ = 'Greg Albrecht <gba@orionlabs.io>'
__copyright__ = 'Copyright 2016 Orion Labs, Inc.'
__license__ = 'All rights reserved. Do not redistribute.'


import setuptools


setuptools.setup(
    name='cambot',
    version='0.0.1b1',
    description='Cambot - Camera bot.',
    license='All rights reserved. Do not redistribute.',
    author='Greg Albrecht',
    author_email='gba@orionlabs.io',
    zip_safe=False,
    packages=['cambot'],
    install_requires=['requests >= 2.8.1', 'slackbot','flask', 'gunicorn'],
    entry_points={'console_scripts': ['cambot = cambot.cmd:cli']}

)
