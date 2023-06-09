"""
This script runs the FlaskWebProjectMMSS application using a development server.
"""
import requests
import exifread
from io import BytesIO
import sqlite3
from sqlite3 import Error
from geopy import Point
import EXIF2DB

from os import environ

from FlaskWebProjectMMSS import app

if __name__ == '__main__':
    EXIF2DB.doAthing()
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
