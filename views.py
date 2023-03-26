"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProjectMMSS import app
import sqlite3
from flask import Flask, jsonify
from sqlite3 import Error
from geopy import Point
from flask import Flask, request
from twilio.rest import Client


@app.route('/')
@app.route('/home')
def index():
    return render_template('test.html')

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

#@app.route('/about')
@app.route('/pics')
def show_entries():
    conn = sqlite3.connect('photos.db')
    c = conn.cursor()
    c.execute('SELECT * FROM photos')
    rows = c.fetchall()
    for row in rows:
          print(row)
    conn.close()
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='rows'
    )

@app.route('/data')
def get_data():
    conn = sqlite3.connect('photos.db')
    c = conn.cursor()

    # query the database to get GeoJSON data
    c.execute('SELECT url, latitude, longitude FROM photos')
    rows = c.fetchall()

    # convert the rows to a GeoJSON FeatureCollection
    features = []
    for row in rows:
        feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [row[2], row[1]]
            },
            'properties': {
                'url': row[0]
            }
        }
        features.append(feature)

    geojson = {
        'type': 'FeatureCollection',
        'features': features
    }

    conn.close()

    return jsonify(geojson)

@app.route('/send_text', methods=['POST'])
def send_text():
    phone_number = request.form['phone_number']
    url = request.form['url']
    

    # Send a text message using Twilio API
    message = client.messages.create(
        to=phone_number,
        from_='YOUR_TWILIO_PHONE_NUMBER',
        body='Your current location: url {}'.format(url)
    )

    return 'Text message has been sent to {}'.format(phone_number)