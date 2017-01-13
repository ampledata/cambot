#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Cambot Plugin."""

import os
import re
import tempfile

import slackbot
import uvsnap

import cambot

__author__ = 'Greg Albrecht <oss@undef.net>'
__copyright__ = 'Copyright 2017 Greg Albrecht'
__license__ = 'Apache License, Version 2.0'


@slackbot.bot.default_reply
def default_handler(message):
    message.reply(cambot.HELP_CMDS)


@slackbot.bot.respond_to('list')
def list_cameras(message):
    cam_list = []

    _msg = '{:<26}||{:^10}|| {:<30}'.format('Camera ID', 'Status', 'Name')
    cam_list.append(_msg)

    nvr = uvsnap.NVR(cambot.NVR_URL, cambot.NVR_API_KEY)
    nvr.get_cameras()

    for camera in nvr.cameras:
        state = 'UNKNOWN'

        if 'DISCONNECTED' in camera['state']:
            state = 'OFFLINE'
        elif 'CONNECTED' in camera['state']:
            state = 'online'

        _msg = '{:<26}||{:^10}|| {:<30}'.format(
            camera['_id'], state, camera['name'])
        cam_list.append(_msg)

    message.reply("\n" + "\n".join(cam_list))


@slackbot.bot.respond_to('(.*)door', re.IGNORECASE)
def show_door(message, door_name=None):
    camera_id = None

    nvr = uvsnap.NVR(cambot.NVR_URL, cambot.NVR_API_KEY)

    if door_name is not None:
        if 'front' in door_name.lower():
            camera_id = cambot.FRONT_DOOR_ID
        elif 'back' in door_name.lower():
            camera_id = cambot.BACK_DOOR_ID

    if camera_id is None:
        return

    tmp_fd, tmp_file = tempfile.mkstemp()
    os.close(tmp_fd)

    snapshot = nvr.get_snapshot(camera_id)
    if snapshot is not None:
        with open(tmp_file, 'w') as ofd:
            ofd.write(snapshot)

        message.channel.upload_file(door_name, tmp_file)


@slackbot.bot.respond_to('show (.*)', re.IGNORECASE)
def show_camera(message, camera_id):
    nvr = uvsnap.NVR(cambot.NVR_URL, cambot.NVR_API_KEY)
    nvr.get_cameras()

    if 'all' in camera_id:
        snapshots = nvr.get_all_snapshots()
        for snapshot in snapshots:
            if snapshot is None:
                break

            camera_id = snapshot['_id']

            tmp_fd, tmp_file = tempfile.mkstemp()
            os.close(tmp_fd)

            with open(tmp_file, 'w') as ofd:
                ofd.write(snapshot)

            message.channel.upload_file(camera_id, tmp_file)
    else:
        tmp_fd, tmp_file = tempfile.mkstemp()
        os.close(tmp_fd)

        snapshot = nvr.get_snapshot(camera_id)
        if snapshot is not None:
            with open(tmp_file, 'w') as ofd:
                ofd.write(snapshot)

            message.channel.upload_file(camera_id, tmp_file)
