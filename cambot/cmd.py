#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Cambot Commands."""

from __future__ import print_function

import sys
import logging
import logging.config

from slackbot import settings

settings.PLUGINS = ['cambot.plugin']
settings.ERRORS_TO = 'gba'
settings.DEBUG = True

from slackbot.bot import Bot  # NOQA pylint: disable=C0413


__author__ = 'Greg Albrecht <oss@undef.net>'
__copyright__ = 'Copyright 2017 Greg Albrecht'
__license__ = 'Apache License, Version 2.0'


def cli():
    lkw = {
        'format': (
            '%(asctime)s cambot %(levelname)s '
            '%(name)s.%(funcName)s:%(lineno)d - %(message)s'
        ),
        'level': logging.DEBUG if settings.DEBUG else logging.INFO,
        'stream': sys.stdout,
    }
    logging.basicConfig(**lkw)
    logging.getLogger(
        'requests.packages.urllib3.connectionpool').setLevel(logging.WARNING)

    bot = Bot()
    print('Starting Cambot...')
    bot.run()


if __name__ == '__main__':
    cli()
