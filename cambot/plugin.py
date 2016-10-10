#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Cambot Plugin."""

__author__ = 'Greg Albrecht <gba@orionlabs.io>'
__copyright__ = 'Copyright 2016 Orion Labs, Inc.'
__license__ = 'All rights reserved. Do not redistribute.'


import json
import re

from slackbot.bot import respond_to
from slackbot.bot import listen_to

import cambot
import cambot.constants


@respond_to('list')
def list_cameras(message):
    cam_list = []
    cameras = cambot.get_cameras()

    for camera in cameras['data']:
        state = 'UNKNOWN'
        if 'DISCONNECTED' in camera['state']:
            state = 'OFFLINE'
        elif 'CONNECTED' in camera['state']:
            state = 'online'
        _msg = '{:<26}||{:^10}|| {:<30}'.format(camera['_id'], state, camera['name'])
        cam_list.append(_msg)

    message.reply("\n".join(cam_list))


@respond_to('(.*)door', re.IGNORECASE)
def show_door(message, door_name=None):
    camera_id = None
    if door_name is not None:
        if 'front' in door_name.lower():
            camera_id = cambot.constants.FRONT_DOOR_ID
        elif 'back' in door_name.lower():
            camera_id = cambot.constants.BACK_DOOR_ID
        url = cambot.get_snapshot_s3_url(camera_id)
        if url is not None:
            attachments = [{
                'title': 'Camera',
                'title_link': url,
                'image_url': url
            }]
            message.send_webapi('', json.dumps(attachments))


@respond_to('show (.*)', re.IGNORECASE)
def show_camera(message, camera_id):
    if 'all' in camera_id:
        cameras = cambot.get_cameras()
        for camera in cameras['data']:
            camera_id = camera['_id']
            url = cambot.get_snapshot_s3_url(camera_id)
            if url is not None:
                attachments = [{
                    'title': 'Camera',
                    'title_link': url,
                    'image_url': url
                }]
                message.send_webapi('', json.dumps(attachments))
    else:
        url = cambot.get_snapshot_s3_url(camera_id)
        if url is not None:
            attachments = [{
                'title': 'Camera',
                'title_link': url,
                'image_url': url
            }]
            message.send_webapi('', json.dumps(attachments))
