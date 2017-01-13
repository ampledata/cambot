#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""CamBot Constants."""

import logging
import os

__author__ = 'Greg Albrecht <oss@undef.net>'
__copyright__ = 'Copyright 2017 Greg Albrecht'
__license__ = 'Apache License, Version 2.0'

LOG_LEVEL = logging.DEBUG
LOG_FORMAT = logging.Formatter(
    ('%(asctime)s cambot %(levelname)s %(name)s.%(funcName)s:%(lineno)d - '
     '%(message)s'))

NVR_URL = os.environ.get('NVR_URL', 'NVR_URL')
NVR_API_KEY = os.environ.get('NVR_API_KEY', 'NVR_API_KEY')
FRONT_DOOR_ID = os.environ.get('FRONT_DOOR_ID', '57e935c0e4b05e057590f4df')
BACK_DOOR_ID = os.environ.get('BACK_DOOR_ID', '577aa653e4b05e0574376cac')

HELP_CMDS = """
Available Commands:

    * help
    * list - Lists all Cameras (ID, Status, Name).
    * show ID - Shows the specified Camera ID.
    * front door - Shows the Front Door (shortcut).
    * back door - Shows the Back Door (shortcut).

"""
