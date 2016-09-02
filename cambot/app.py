#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Cambot WebHook."""

__author__ = 'Greg Albrecht <gba@orionlabs.io>'
__copyright__ = 'Copyright 2016 Orion Labs, Inc.'
__license__ = 'All rights reserved. Do not redistribute.'


import io
import json
import tempfile

import flask
import requests

import cambot
import cambot.constants


CambotApp = flask.Flask(__name__)


@CambotApp.route('/snapshot', methods=['GET'])
def snapshot(camera_id=None):
    camera_id = camera_id or cambot.constants.FRONT_DOOR_ID
    snap = cambot.get_camera(camera_id)
    if snap is not None:
        return flask.send_file(io.BytesIO(snap), mimetype='image/jpeg')


@CambotApp.route('/front_door', methods=['GET'])
def front_door():
    camera_id = cambot.constants.FRONT_DOOR_ID
    snap = cambot.get_camera(camera_id)
    if snap is not None:
        return flask.send_file(io.BytesIO(snap), mimetype='image/jpeg')


@CambotApp.route('/back_door', methods=['GET'])
def back_door():
    camera_id = cambot.constants.BACK_DOOR_ID
    snap = cambot.get_camera(camera_id)
    if snap is not None:
        return flask.send_file(io.BytesIO(snap), mimetype='image/jpeg')


if __name__ == '__main__':
    CambotApp.debug = True
    CambotApp.run(host='0.0.0.0')
