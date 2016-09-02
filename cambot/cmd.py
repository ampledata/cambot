#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Cambot Commands."""

from __future__ import print_function

from slackbot import settings
settings.PLUGINS = ['cambot.plugin']
settings.ERRORS_TO = 'gba'

from slackbot.bot import Bot

__author__ = 'Greg Albrecht <gba@orionlabs.io>'
__copyright__ = 'Copyright 2016 Orion Labs, Inc.'
__license__ = 'All rights reserved. Do not redistribute.'


def cli():
    bot = Bot()
    print('Starting Cambot...')
    bot.run()


if __name__ == '__main__':
    cli()
