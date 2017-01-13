#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Constants for Cambot module."""

import os

__author__ = 'Greg Albrecht <oss@undef.net>'
__copyright__ = 'Copyright 2017 Orion Labs, Inc.'
__license__ = 'Apache License, Version 2.0'


NVR_URL = os.environ.get('NVR_URL', 'NVR_URL')
NVR_API_KEY = os.environ.get('API_KEY', 'API_KEY')
FRONT_DOOR_ID = os.environ.get('FRONT_DOOR_ID', '57e935c0e4b05e057590f4df')
BACK_DOOR_ID = os.environ.get('BACK_DOOR_ID', '577aa653e4b05e0574376cac')
