#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7775005658:AAGEyNwJbWLd5tp5hFZ4gCgG6P9koHDTW38")
    API_ID = int(os.environ.get("API_ID", "29773843"))
    API_HASH = os.environ.get("API_HASH", "8b40e91c29a00fecb905d6eb6aee2b3b")
    AUTH_USERS = os.environ.get("AUTH_USERS", "6350117077")
