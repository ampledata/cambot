#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Cambot WebHook."""

__author__ = 'Greg Albrecht <oss@undef.net>'
__copyright__ = 'Copyright 2017 Orion Labs, Inc.'
__license__ = 'Apache License, Version 2.0'


import io
import json
import tempfile

import flask
import requests

import cambot


CambotApp = flask.Flask(__name__)


@CambotApp.route('/snapshot', methods=['GET'])
def snapshot(camera_id=None):
    camera_id = camera_id or cambot.FRONT_DOOR_ID

    nvr = uvsnap.NVR(cambot.NVR_URL, cambot.NVR_API_KEY)
    snapshot = nvr.get_snapshot(camera_id)

    if snapshot is not None:
        return flask.send_file(io.BytesIO(snapshot), mimetype='image/jpeg')


@CambotApp.route('/front_door', methods=['GET'])
def front_door():
    camera_id = cambot.FRONT_DOOR_ID

    nvr = uvsnap.NVR(cambot.NVR_URL, cambot.NVR_API_KEY)
    snapshot = nvr.get_snapshot(camera_id)

    if snapshot is not None:
        return flask.send_file(io.BytesIO(snapshot), mimetype='image/jpeg')


@CambotApp.route('/back_door', methods=['GET'])
def back_door():
    camera_id = cambot.BACK_DOOR_ID

    nvr = uvsnap.NVR(cambot.NVR_URL, cambot.NVR_API_KEY)
    snapshot = nvr.get_snapshot(camera_id)

    if snapshot is not None:
        return flask.send_file(io.BytesIO(snapshot), mimetype='image/jpeg')


if __name__ == '__main__':
    CambotApp.debug = True
    CambotApp.run(host='0.0.0.0')
