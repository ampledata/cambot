#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Cambot Plugin."""

__author__ = 'Greg Albrecht <gba@orionlabs.io>'
__copyright__ = 'Copyright 2016 Orion Labs, Inc.'
__license__ = 'All rights reserved. Do not redistribute.'


import json

from slackbot.bot import respond_to
from slackbot.bot import listen_to

import cambot
import cambot.constants


@respond_to('front door')
def front_door(message):
    camera_id = cambot.constants.FRONT_DOOR_ID
    url = cambot.get_snapshot_s3_url(camera_id)
    if url is not None:
        attachments = [{
            'title': 'Front Door Camera',
            'title_link': url,
            'image_url': url
        }]
        message.send_webapi('', json.dumps(attachments))


@respond_to('back door')
def back_door(message):
    camera_id = cambot.constants.BACK_DOOR_ID
    url = cambot.get_snapshot_s3_url(camera_id)
    if url is not None:
        attachments = [{
            'title': 'Back Door Camera',
            'title_link': url,
            'image_url': url
        }]
        message.send_webapi('', json.dumps(attachments))



@respond_to('list')
def list_cameras(message):
    cam_list = []
    cameras = cambot.get_cameras()

    for camera in cameras['data']:
        cam_list.append("\t\t".join([camera['name'], camera['_id'], camera['state']]))

    message.reply("\n".join(cam_list))



@respond_to('show (.*)')
def show_camera(message, something):
    camera_id = something
    url = cambot.get_snapshot_s3_url(camera_id)
    if url is not None:
        attachments = [{
            'title': 'Camera',
            'title_link': url,
            'image_url': url
        }]
        message.send_webapi('', json.dumps(attachments))
