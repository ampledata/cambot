#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Cambot Commands."""

from __future__ import print_function

from slackbot import settings

settings.PLUGINS = ['cambot.plugin']
settings.ERRORS_TO = 'gba'

from slackbot.bot import Bot

__author__ = 'Greg Albrecht <oss@undef.net>'
__copyright__ = 'Copyright 2017 Orion Labs, Inc.'
__license__ = 'Apache License, Version 2.0'


def cli():
    bot = Bot()
    print('Starting Cambot...')
    bot.run()


if __name__ == '__main__':
    cli()
