#!/bin/env python

import os
import sqlite3

from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash

app = Flask(__name__)

app.config.from_object(__name__)
app.config.update(dict(
    DATABASE = os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY = 'development key',
    USERNAME   = 'admin'
    PASSOWRD   = 'default'
))

app.config.from_envvar('FLASKR_SETTINGS', silen=True)
