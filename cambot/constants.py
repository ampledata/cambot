#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Constants for Cambot module."""

import os

__author__ = 'Greg Albrecht <gba@orionlabs.io>'
__copyright__ = 'Copyright 2016 Orion Labs, Inc.'
__license__ = 'All rights reserved. Do not redistribute.'


NVR_URL = os.environ.get('NVR_URL', 'NVR_URL')
API_KEY = os.environ.get('API_KEY', 'API_KEY')
FRONT_DOOR_ID = os.environ.get('FRONT_DOOR_ID', '577a9a5fe4b05e0574376016')
BACK_DOOR_ID = os.environ.get('BACK_DOOR_ID', '577aa653e4b05e0574376cac')
