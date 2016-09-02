#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Cambot Functions."""

__author__ = 'Greg Albrecht <gba@orionlabs.io>'
__copyright__ = 'Copyright 2016 Orion Labs, Inc.'
__license__ = 'All rights reserved. Do not redistribute.'


import io
import json
import os
import tempfile

import requests

import cambot
import cambot.constants

import botlib


def get_snapshot(camera_id):
    nvr_url = cambot.constants.NVR_URL
    api_key = cambot.constants.API_KEY

    cameras_url = "%s/api/2.0/camera" % nvr_url

    requests.packages.urllib3.disable_warnings()

    get_cameras = requests.get(
        cameras_url, params={'apiKey': api_key}, verify=False)

    cameras = json.loads(get_cameras.text)

    for camera in cameras['data']:
        if camera['state'] == 'CONNECTED' and camera['_id'] == camera_id:
            get_snapshot = requests.get(
                "%s/api/2.0/snapshot/camera/%s" % (nvr_url, camera_id),
                params={'force': 'true', 'apiKey': api_key}, verify=False)

            if get_snapshot.ok:
                return get_snapshot.content


def get_snapshot_url(camera_id):
    nvr_url = cambot.constants.NVR_URL
    api_key = cambot.constants.API_KEY

    cameras_url = "%s/api/2.0/camera" % nvr_url

    requests.packages.urllib3.disable_warnings()

    get_cameras = requests.get(
        cameras_url, params={'apiKey': api_key}, verify=False)

    cameras = json.loads(get_cameras.text)

    for camera in cameras['data']:
        if camera['state'] == 'CONNECTED' and camera['_id'] == camera_id:
            get_snapshot = requests.get(
                "%s/api/2.0/snapshot/camera/%s" % (nvr_url, camera_id),
                params={'force': 'true', 'apiKey': api_key}, verify=False)

            if get_snapshot.ok:
                return get_snapshot.url


def get_snapshot_s3_url(camera_id):
    snap = cambot.get_snapshot(camera_id)

    prefix = '_'.join(['cambot', camera_id, ''])

    if snap is not None:
        tmp_fd, output_file = tempfile.mkstemp(prefix=prefix, suffix='.jpg')
        os.close(tmp_fd)

    with open(output_file, 'w') as ofd:
        ofd.write(snap)

    return botlib.upload_to_s3(output_file)


def get_cameras():
    cam_list = {}

    nvr_url = cambot.constants.NVR_URL
    api_key = cambot.constants.API_KEY

    cameras_url = "%s/api/2.0/camera" % nvr_url

    requests.packages.urllib3.disable_warnings()

    get_cameras = requests.get(
        cameras_url, params={'apiKey': api_key}, verify=False)

    cameras = json.loads(get_cameras.text)

    return cameras
